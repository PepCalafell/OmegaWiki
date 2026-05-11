#!/usr/bin/env python3
"""
tier_candidates.py - Rank candidate PDFs in raw/papers/ by ingest priority.

Output: docs/paper_candidates.md with sorted markdown table.

Score composition:
- 40% citation impact (log10 of citationCount, normalized)
- 30% recency (year delta from current year, decays over 10 years)
- 30% wiki vocabulary fit (Jaccard similarity vs wiki concepts/foundations)

Coste: 0 LLM tokens. Usa fitz (PyMuPDF) + Semantic Scholar API.
"""

import os
import re
import sys
import json
import time
import hashlib
import logging
from pathlib import Path
from collections import Counter
from datetime import datetime
from typing import Optional

import fitz  # PyMuPDF

# ============== CONFIG ==============

REPO_ROOT = Path(__file__).resolve().parent.parent
RAW_PAPERS_DIR = REPO_ROOT / "raw" / "papers"
WIKI_DIR = REPO_ROOT / "wiki"
DOCS_DIR = REPO_ROOT / "docs"
S2_CACHE_DIR = Path("/tmp/s2_cache")
S2_CACHE_DIR.mkdir(exist_ok=True, parents=True)

CURRENT_YEAR = datetime.now().year
SCORE_WEIGHTS = {
    "impact": 0.40,
    "recency": 0.30,
    "relevance": 0.30,
}
RECENCY_DECAY_YEARS = 10
IMPACT_CITATION_CAP = 10000

# Stopwords mínimas (no usamos nltk para no añadir deps)
STOPWORDS = set("""
a an the and or but if then so as for to of in on at by with from up down out
that this these those is are was were be been being have has had do does did
i you he she it we they them his her its our their which who whom what when
where why how all any some no not nor only own same than too very can will
just don should now into through during before after above below between
both each few more most other such only own same same so than too very
""".split())

# ============== LOGGING ==============

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s", datefmt="%H:%M:%S")
log = logging.getLogger()

# ============== PDF METADATA ==============

def extract_pdf_metadata(pdf_path: Path) -> dict:
    """Extract title (filename), first-page text, attempt DOI extraction."""
    try:
        doc = fitz.open(str(pdf_path))
        page0_text = doc.load_page(0).get_text() if doc.page_count > 0 else ""
        doc.close()
    except Exception as e:
        log.warning(f"[fitz fail] {pdf_path.name}: {e}")
        return {"title": pdf_path.stem, "doi": None, "first_page_text": ""}

    # Try to find DOI in first page
    doi_match = re.search(r"\b(10\.\d{4,9}/[-._;()/:\w]+)\b", page0_text)
    doi = doi_match.group(1).rstrip(".,;)") if doi_match else None

    return {
        "title": pdf_path.stem,
        "doi": doi,
        "first_page_text": page0_text[:5000],  # cap first 5KB
    }

# ============== S2 CACHE + QUERY ==============

def s2_cache_key(doi_or_title: str) -> str:
    h = hashlib.md5(doi_or_title.encode()).hexdigest()[:12]
    return f"s2_{h}.json"

def s2_query_paper(doi: Optional[str], title: str) -> Optional[dict]:
    """Query Semantic Scholar via tools/fetch_s2.py (or direct API).
    Returns dict with citationCount, year, venue, etc. None if fails."""
    cache_id = doi if doi else title[:60]
    cache_file = S2_CACHE_DIR / s2_cache_key(cache_id)

    if cache_file.exists():
        try:
            return json.loads(cache_file.read_text())
        except Exception:
            pass

    # Use tools/fetch_s2.py if available
    fetch_s2 = REPO_ROOT / "tools" / "fetch_s2.py"
    python_bin = REPO_ROOT / ".venv" / "bin" / "python"

    if not fetch_s2.exists() or not python_bin.exists():
        log.warning("tools/fetch_s2.py or .venv missing — skipping S2 query")
        return None

    import subprocess
    try:
        query = doi if doi else title
        result = subprocess.run(
            [str(python_bin), str(fetch_s2), "paper", query],
            capture_output=True, text=True, timeout=60,
        )
        stdout = result.stdout

        # Parse json (skip [fetch_s2] log lines)
        json_lines = [l for l in stdout.splitlines() if not l.startswith("[fetch_s2]")]
        if not json_lines:
            return None
        data = json.loads("\n".join(json_lines))

        # Cache
        cache_file.write_text(json.dumps(data, indent=2))
        return data
    except Exception as e:
        log.warning(f"[S2 fail] {cache_id}: {e}")
        return None

# ============== WIKI VOCABULARY ==============

def load_wiki_vocabulary() -> set[str]:
    """Build set of relevant keywords from wiki/{concepts,foundations}/*.md."""
    vocab = set()
    for sub in ["concepts", "foundations"]:
        sub_dir = WIKI_DIR / sub
        if not sub_dir.exists():
            continue
        for md_file in sub_dir.glob("*.md"):
            text = md_file.read_text(errors="ignore")
            # Extract tags and title-like terms
            # Tags lines: "  - tag-name"
            for m in re.finditer(r"^\s*-\s+([a-zA-Z][\w-]+)\s*$", text, re.MULTILINE):
                vocab.add(m.group(1).lower())
            # Title in frontmatter
            tm = re.search(r"^title:\s*\"?([^\"\n]+)\"?\s*$", text, re.MULTILINE)
            if tm:
                for word in re.findall(r"\b[a-zA-Z][\w-]{2,}\b", tm.group(1)):
                    if word.lower() not in STOPWORDS:
                        vocab.add(word.lower())
            # Slug from filename
            vocab.add(md_file.stem.lower())
    return vocab

# ============== KEYWORD EXTRACTION FROM PDF ==============

def extract_pdf_keywords(text: str, top_n: int = 200) -> set[str]:
    """Lower-case unique tokens from PDF text, top-N by frequency."""
    words = re.findall(r"\b[a-zA-Z][a-zA-Z\-]{2,}\b", text.lower())
    words = [w for w in words if w not in STOPWORDS and not w.isdigit()]
    counter = Counter(words)
    return {w for w, _ in counter.most_common(top_n)}

# ============== SCORING ==============

import math

def score_impact(citation_count: Optional[int]) -> float:
    """Log-scaled impact, normalized to [0,1]."""
    if citation_count is None or citation_count < 0:
        return 0.0
    return min(1.0, math.log10(citation_count + 1) / math.log10(IMPACT_CITATION_CAP))

def score_recency(year: Optional[int]) -> float:
    """Linear decay over 10 years."""
    if year is None or year <= 0:
        return 0.0
    delta = max(0, CURRENT_YEAR - year)
    return max(0.0, 1.0 - delta / RECENCY_DECAY_YEARS)

def score_relevance(pdf_keywords: set[str], wiki_vocab: set[str]) -> float:
    """Coverage: fraction of PDF top-keywords that appear in wiki vocabulary.
    Better than Jaccard for asymmetric set sizes (PDF<<wiki)."""
    if not pdf_keywords or not wiki_vocab:
        return 0.0
    overlap = pdf_keywords & wiki_vocab
    return len(overlap) / len(pdf_keywords) if pdf_keywords else 0.0

def composite_score(impact: float, recency: float, relevance: float) -> float:
    return (
        SCORE_WEIGHTS["impact"] * impact +
        SCORE_WEIGHTS["recency"] * recency +
        SCORE_WEIGHTS["relevance"] * relevance
    )

# ============== STATUS DETECTION ==============

def detect_status(pdf_filename: str) -> str:
    """Check if PDF appears to already be ingested in wiki/papers/."""
    pdf_stem = Path(pdf_filename).stem.lower()
    if not (WIKI_DIR / "papers").exists():
        return "pending"
    # Check wiki/papers/*.md for slug match or title match
    for paper_md in (WIKI_DIR / "papers").glob("*.md"):
        text = paper_md.read_text(errors="ignore")
        title_match = re.search(r"^title:\s*\"?([^\"\n]+)\"?", text, re.MULTILINE)
        if title_match:
            title_words = set(re.findall(r"\b[a-zA-Z][\w-]{3,}\b", title_match.group(1).lower()))
            pdf_words = set(re.findall(r"\b[a-zA-Z][\w-]{3,}\b", pdf_stem))
            if title_words and pdf_words:
                overlap = len(title_words & pdf_words) / max(len(title_words), len(pdf_words))
                if overlap > 0.5:
                    return f"✓ in wiki ({paper_md.stem})"
    return "pending"

# ============== MAIN PIPELINE ==============

def rank_candidates() -> list[dict]:
    """Process all PDFs in raw/papers/, return ranked list."""
    if not RAW_PAPERS_DIR.exists():
        log.error(f"Raw papers dir not found: {RAW_PAPERS_DIR}")
        return []

    pdf_files = sorted(RAW_PAPERS_DIR.glob("*.pdf"))
    log.info(f"Found {len(pdf_files)} PDFs in {RAW_PAPERS_DIR}")

    log.info("Loading wiki vocabulary...")
    wiki_vocab = load_wiki_vocabulary()
    log.info(f"Wiki vocabulary: {len(wiki_vocab)} terms")

    candidates = []
    for i, pdf_path in enumerate(pdf_files, 1):
        log.info(f"[{i}/{len(pdf_files)}] {pdf_path.name[:60]}")

        meta = extract_pdf_metadata(pdf_path)
        s2_data = s2_query_paper(meta["doi"], meta["title"])

        citation_count = s2_data.get("citationCount") if s2_data else None
        year = s2_data.get("year") if s2_data else None
        venue = s2_data.get("venue", "") if s2_data else ""
        influential = s2_data.get("influentialCitationCount") if s2_data else None

        pdf_kw = extract_pdf_keywords(meta["first_page_text"], top_n=200)

        impact = score_impact(citation_count)
        recency = score_recency(year)
        relevance = score_relevance(pdf_kw, wiki_vocab)
        score = composite_score(impact, recency, relevance)
        status = detect_status(pdf_path.name)

        candidates.append({
            "filename": pdf_path.name,
            "title": meta["title"][:80],
            "doi": meta["doi"] or "",
            "year": year,
            "venue": venue,
            "citations": citation_count,
            "influential": influential,
            "impact": round(impact, 3),
            "recency": round(recency, 3),
            "relevance": round(relevance, 3),
            "score": round(score, 3),
            "status": status,
        })

        # Throttle slightly to be nice to S2 API
        if i % 10 == 0:
            time.sleep(1)

    # Sort by score descending
    candidates.sort(key=lambda c: c["score"], reverse=True)
    return candidates

def write_report(candidates: list[dict], output: Path):
    """Generate markdown report."""
    output.parent.mkdir(exist_ok=True, parents=True)

    lines = [
        "# Paper candidates ranking",
        "",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"Total PDFs scanned: {len(candidates)}",
        "",
        "## Scoring weights",
        "",
        "- 40% citation impact (log10 of S2 citationCount)",
        "- 30% recency (decays over 10 years from current year)",
        "- 30% wiki relevance (Jaccard similarity vs concepts/foundations vocab)",
        "",
        "## Ranking",
        "",
        "| # | Title | Year | Citations | Impact | Recency | Wiki fit | Score | Status |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for i, c in enumerate(candidates, 1):
        title = c["title"].replace("|", "\\|")
        citations = c["citations"] if c["citations"] is not None else "?"
        year = c["year"] if c["year"] else "?"
        lines.append(
            f"| {i} | {title[:70]} | {year} | {citations} | "
            f"{c['impact']:.2f} | {c['recency']:.2f} | {c['relevance']:.2f} | "
            f"**{c['score']:.2f}** | {c['status']} |"
        )

    lines.extend([
        "",
        "## Notes",
        "",
        "- `citationCount = ?` = S2 lookup failed (no DOI extractable, or S2 outage).",
        "- `Status pending` = paper not yet ingested in wiki/papers/.",
        "- Score thresholds (rough): >0.70 high priority, 0.50-0.70 medium, <0.50 low.",
        "- Manual review recommended for top 5 before processing.",
    ])

    output.write_text("\n".join(lines))
    log.info(f"Report written: {output}")

if __name__ == "__main__":
    log.info("=== tier_candidates.py ===")
    candidates = rank_candidates()
    if not candidates:
        log.error("No candidates ranked")
        sys.exit(1)
    output_path = DOCS_DIR / "paper_candidates.md"
    write_report(candidates, output_path)
    log.info(f"Done. {len(candidates)} candidates ranked.")
    log.info(f"Top 5:")
    for i, c in enumerate(candidates[:5], 1):
        log.info(f"  {i}. [{c['score']:.2f}] {c['title'][:60]}")
