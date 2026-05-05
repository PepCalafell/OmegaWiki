#!/usr/bin/env python3
"""Semantic Scholar API wrapper.

Usage:
    python3 tools/fetch_s2.py search "low rank adaptation"
    python3 tools/fetch_s2.py paper 2106.09685                    # arXiv ID
    python3 tools/fetch_s2.py paper 10.1126/sciadv.adq5226        # DOI
    python3 tools/fetch_s2.py paper PMID:31209404                 # PubMed ID
    python3 tools/fetch_s2.py paper 31209404                      # PMID (auto-detected)
    python3 tools/fetch_s2.py citations 10.1126/sciadv.adq5226
    python3 tools/fetch_s2.py references 2106.09685
    python3 tools/fetch_s2.py recommend 2106.09685
    python3 tools/fetch_s2.py recommend 2106.09685 2305.14314 --negative 1810.04805

Identifier types accepted (auto-detected):
    - DOI:           starts with "10." (e.g. 10.1126/sciadv.adq5226)
    - arXiv ID:      digits.digits format (e.g. 2106.09685) or category/digits (e.g. cs.LG/0001234)
    - PubMed ID:     all digits, ≤9 chars (e.g. 31209404), or explicit PMID:<id>
    - S2 paperId:    40-character hex string

Explicit prefixes also accepted: ARXIV:, arxiv:, DOI:, doi:, PMID:, pmid:.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time

import _env  # noqa: F401 — load .env files for API keys
import requests

BASE_URL = "https://api.semanticscholar.org/graph/v1"
RECS_BASE_URL = "https://api.semanticscholar.org/recommendations/v1"

# Full rich field set. Accepted by `/paper/{id}` and `/paper/search` — both
# honor nested selectors like `authors.hIndex` and the `tldr` field. Extra
# keys are harmless to existing callers (they read specific keys), so the
# discovery flow picks up hIndex, influentialCitationCount, fieldsOfStudy,
# and tldr without a second round-trip.
FIELDS = (
    "paperId,title,abstract,authors.authorId,authors.name,authors.hIndex,"
    "authors.paperCount,year,citationCount,influentialCitationCount,venue,"
    "publicationTypes,fieldsOfStudy,tldr,externalIds,url"
)

# Flat field set for the endpoints that reject nested selectors and `tldr`:
# `/paper/{id}/citations`, `/paper/{id}/references`, and `/recommendations/*`.
# Authors come back as `{authorId, name}` only — h-index enrichment requires
# a follow-up `paper()` call per candidate if needed. (`/paper/search` does NOT
# share this restriction and still uses the full `FIELDS`.)
FLAT_FIELDS = (
    "paperId,title,abstract,authors,year,citationCount,influentialCitationCount,"
    "venue,publicationTypes,fieldsOfStudy,externalIds,url"
)

S2_API_KEY = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "")
RATE_LIMIT_DELAY = 1.0 if S2_API_KEY else 3.0  # faster with API key
MAX_RETRIES = 3

_HEADERS = {"x-api-key": S2_API_KEY} if S2_API_KEY else {}


# === Identifier resolution ====================================================

# arXiv IDs come in two flavors:
#   - new style: 4 digits . 4-5 digits, e.g. "2106.09685"
#   - old style: category/digits, e.g. "cs.LG/0001234"
_ARXIV_NEW_STYLE = re.compile(r"^\d{4}\.\d{4,5}(v\d+)?$")
_ARXIV_OLD_STYLE = re.compile(r"^[a-z\-]+(\.[A-Z]{2})?/\d{7}(v\d+)?$")

# DOIs always start with "10." followed by a registrant code.
_DOI_PREFIX = re.compile(r"^10\.\d{4,9}/")

# S2 paperIds are 40-character hex strings.
_S2_PAPER_ID = re.compile(r"^[0-9a-f]{40}$")


def _bare_arxiv_id(arxiv_id: str) -> str:
    """Strip optional ARXIV:/arxiv: prefix so callers can pass either form."""
    return arxiv_id.removeprefix("ARXIV:").removeprefix("arxiv:")


def _resolve_id_endpoint(paper_id: str, *, verbose: bool = True) -> str:
    """Detect the type of identifier and return the path component for S2 lookup.

    Returns a string like "DOI:10.1126/sciadv.adq5226" or "ARXIV:2106.09685"
    suitable for inserting after "/paper/" in S2 API URLs.

    Detection priority:
      1. Explicit prefix (ARXIV:, DOI:, PMID:) — used as-is (uppercased).
      2. DOI pattern (starts with "10.<digits>/").
      3. arXiv pattern (new or old style).
      4. S2 paperId (40-char hex).
      5. Numeric-only ≤9 chars → assumed PMID.
      6. Fallback: passed through as a bare paperId (S2 will return 404 if invalid).
    """
    pid = paper_id.strip()

    # Explicit prefix — normalize to uppercase scheme name.
    for prefix in ("ARXIV:", "arxiv:", "DOI:", "doi:", "PMID:", "pmid:"):
        if pid.startswith(prefix):
            scheme = prefix.rstrip(":").upper()
            value = pid[len(prefix):]
            resolved = f"{scheme}:{value}"
            if verbose:
                print(f"[fetch_s2] Explicit prefix detected: {scheme} -> {resolved}", file=sys.stderr)
            return resolved

    # DOI pattern.
    if _DOI_PREFIX.match(pid):
        if verbose:
            print(f"[fetch_s2] DOI auto-detected: {pid}", file=sys.stderr)
        return f"DOI:{pid}"

    # arXiv pattern (new or old style).
    if _ARXIV_NEW_STYLE.match(pid) or _ARXIV_OLD_STYLE.match(pid):
        if verbose:
            print(f"[fetch_s2] arXiv ID auto-detected: {pid}", file=sys.stderr)
        return f"ARXIV:{pid}"

    # S2 paperId (40-char hex).
    if _S2_PAPER_ID.match(pid):
        if verbose:
            print(f"[fetch_s2] S2 paperId auto-detected: {pid}", file=sys.stderr)
        return pid

    # Numeric-only and short → likely PMID.
    if pid.isdigit() and len(pid) <= 9:
        if verbose:
            print(f"[fetch_s2] PMID auto-detected: {pid}", file=sys.stderr)
        return f"PMID:{pid}"

    # Fallback: pass through bare (lets S2 try to resolve it).
    if verbose:
        print(f"[fetch_s2] Unrecognized ID format, passing through bare: {pid}", file=sys.stderr)
    return pid


# === HTTP plumbing ============================================================

def _request(method: str, url: str, *, params: dict | None = None, json_body: dict | None = None) -> dict | list:
    """Shared HTTP path with rate limit + 429 retry."""
    time.sleep(RATE_LIMIT_DELAY)
    for attempt in range(MAX_RETRIES):
        resp = requests.request(
            method,
            url,
            params=params or {},
            json=json_body,
            headers=_HEADERS,
            timeout=30,
        )
        if resp.status_code == 429:
            wait = 60 * (attempt + 1)  # 60s, 120s, 180s
            print(f"Rate limited, waiting {wait}s... (attempt {attempt+1}/{MAX_RETRIES})", file=sys.stderr)
            time.sleep(wait)
            continue
        resp.raise_for_status()
        return resp.json()
    raise RuntimeError(f"S2 API rate limited after {MAX_RETRIES} retries")


def _get(endpoint: str, params: dict | None = None) -> dict | list:
    return _request("GET", f"{BASE_URL}{endpoint}", params=params)


def _post(endpoint: str, params: dict | None = None, json_body: dict | None = None, base_url: str = BASE_URL) -> dict | list:
    return _request("POST", f"{base_url}{endpoint}", params=params, json_body=json_body)


# === Public API ===============================================================

def search(query: str, limit: int = 10) -> list[dict]:
    """Search papers by query string. Accepts the full rich FIELDS."""
    data = _get("/paper/search", {
        "query": query,
        "limit": limit,
        "fields": FIELDS,
    })
    return data.get("data", [])


def paper(paper_id: str) -> dict:
    """Get paper details by any supported identifier (arXiv, DOI, PMID, S2 paperId).

    This endpoint accepts the full rich FIELDS.
    """
    endpoint_id = _resolve_id_endpoint(paper_id)
    return _get(f"/paper/{endpoint_id}", {"fields": FIELDS})


def citations(paper_id: str, limit: int = 100) -> list[dict]:
    """Get papers that cite the given paper.

    Each returned paper dict carries `_is_influential_edge: bool`, lifted from
    the envelope's `isInfluential` field — S2's per-edge signal for whether this
    specific citation substantively built on the anchor (not just a name-check).

    The key is underscore-prefixed so existing key-based consumers
    (`init_discovery.py`, `/ingest`) ignore it without change.
    """
    endpoint_id = _resolve_id_endpoint(paper_id)
    data = _get(f"/paper/{endpoint_id}/citations", {
        "limit": limit,
        "fields": f"isInfluential,{FLAT_FIELDS}",
    })
    out: list[dict] = []
    for item in data.get("data", []):
        paper_obj = item.get("citingPaper") or {}
        if paper_obj:
            paper_obj["_is_influential_edge"] = bool(item.get("isInfluential"))
            out.append(paper_obj)
    return out


def references(paper_id: str, limit: int = 100) -> list[dict]:
    """Get papers referenced by the given paper.

    Each returned paper dict carries `_is_influential_edge: bool` — see `citations`.
    """
    endpoint_id = _resolve_id_endpoint(paper_id)
    data = _get(f"/paper/{endpoint_id}/references", {
        "limit": limit,
        "fields": f"isInfluential,{FLAT_FIELDS}",
    })
    out: list[dict] = []
    for item in data.get("data", []):
        paper_obj = item.get("citedPaper") or {}
        if paper_obj:
            paper_obj["_is_influential_edge"] = bool(item.get("isInfluential"))
            out.append(paper_obj)
    return out


def recommend(
    positive_ids: list[str],
    negative_ids: list[str] | None = None,
    limit: int = 50,
) -> list[dict]:
    """Recommend papers similar to the given anchors.

    Uses the lightweight forpaper GET endpoint when there is exactly one
    positive anchor and no negatives; otherwise uses the multi-anchor POST
    endpoint that supports negative examples.

    IDs accepted: arXiv (with or without prefix), DOI, PMID, or S2 paperIds.
    """
    negative_ids = negative_ids or []
    if not positive_ids:
        raise ValueError("recommend() requires at least one positive_id")

    def _normalize(pid: str) -> str:
        # arXiv-style IDs need the ARXIV: prefix; S2 paperIds (40-char hex) pass through.
        if pid.startswith(("ARXIV:", "arxiv:")):
            return f"ARXIV:{_bare_arxiv_id(pid)}"
        if "/" in pid or len(pid) == 40 or pid.isdigit() and len(pid) > 12:
            return pid  # looks like an S2 paperId already (or DOI with /)
        # Heuristic: contains a dot and starts with a digit → arXiv-style (e.g. 2106.09685)
        if pid and pid[0].isdigit() and "." in pid:
            return f"ARXIV:{pid}"
        # DOI / PMID prefixes — let _resolve_id_endpoint handle via the normal path.
        # For recommend's forpaper endpoint we need the prefixed form, so resolve here.
        if _DOI_PREFIX.match(pid):
            return f"DOI:{pid}"
        if pid.isdigit() and len(pid) <= 9:
            return f"PMID:{pid}"
        return pid

    positive = [_normalize(p) for p in positive_ids]
    negative = [_normalize(p) for p in negative_ids]

    if len(positive) == 1 and not negative:
        url = f"{RECS_BASE_URL}/papers/forpaper/{positive[0]}"
        data = _request("GET", url, params={"limit": limit, "fields": FLAT_FIELDS})
    else:
        data = _post(
            "/papers",
            params={"limit": limit, "fields": FLAT_FIELDS},
            json_body={"positivePaperIds": positive, "negativePaperIds": negative},
            base_url=RECS_BASE_URL,
        )

    # Both endpoints return {"recommendedPapers": [...]}.
    return data.get("recommendedPapers", [])


# === CLI ======================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Semantic Scholar API wrapper (supports arXiv, DOI, PMID, S2 paperId)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_search = sub.add_parser("search", help="Search papers")
    p_search.add_argument("query", help="Search query")
    p_search.add_argument("n", nargs="?", type=int, default=10, help="Number of results")

    p_paper = sub.add_parser("paper", help="Get paper details")
    p_paper.add_argument(
        "paper_id",
        help="Paper identifier: arXiv ID, DOI, PMID, or S2 paperId (auto-detected)",
    )

    p_cite = sub.add_parser("citations", help="Get citations")
    p_cite.add_argument(
        "paper_id",
        help="Paper identifier: arXiv ID, DOI, PMID, or S2 paperId",
    )

    p_refs = sub.add_parser("references", help="Get references")
    p_refs.add_argument(
        "paper_id",
        help="Paper identifier: arXiv ID, DOI, PMID, or S2 paperId",
    )

    p_rec = sub.add_parser("recommend", help="Recommend papers similar to one or more anchors")
    p_rec.add_argument("positive_ids", nargs="+", help="One or more anchor paper IDs (arXiv, DOI, PMID, or S2)")
    p_rec.add_argument(
        "--negative",
        action="append",
        default=[],
        metavar="ID",
        help="Paper ID to push recommendations away from (repeatable)",
    )
    p_rec.add_argument("--limit", type=int, default=50, help="Max recommendations to return (default 50)")

    args = parser.parse_args()

    if args.command == "search":
        result = search(args.query, args.n)
    elif args.command == "paper":
        result = paper(args.paper_id)
    elif args.command == "citations":
        result = citations(args.paper_id)
    elif args.command == "references":
        result = references(args.paper_id)
    elif args.command == "recommend":
        result = recommend(args.positive_ids, args.negative, args.limit)
    else:
        result = {}

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
