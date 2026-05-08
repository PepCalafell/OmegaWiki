#!/usr/bin/env python3
"""OmegaWiki — Step 4.E HARD FAIL validator for /ingest.

Verifies that every `[cnn]` bullet under `## All claims (exhaustive)` of a
paper page reverse-links to a `[[claims/{slug}]]` wikilink in its inline
`links:` field. This enforces the bidirectional-link invariant declared in
the /ingest skill's Constraints section.

Called by the /ingest skill at Step 4.E, AFTER claim files are created and
BEFORE the paper page is written to disk. The skill must regenerate any
failing bullet and re-run this validator until it returns exit code 0.

Usage:
    python tools/validate_step4e.py <path/to/paper.md>

Exit codes:
    0 — every [cnn] bullet has [[claims/{slug}]] in its links: field
    1 — at least one bullet violates the invariant (printed with reason)
    2 — usage error (no path given)

Three failure modes are detected:
    1. Bullet has no `links:` field at all.
    2. Bullet has `links:` but no `[[claims/...]]` wikilink in it.
    3. Bullet has `[[claims/TODO]]` placeholder not yet back-filled
       (Step 3 two-pass writing leaves these; Step 4 must resolve them).
"""

import re
import sys
from pathlib import Path


def main(path: str) -> int:
    text = Path(path).read_text()

    # find the "## All claims (exhaustive)" section
    m = re.search(r"^##\s+All claims\s*\(exhaustive\)\s*$", text, re.MULTILINE)
    if not m:
        print(f"FAIL: no '## All claims (exhaustive)' section in {path}")
        return 1
    body = text[m.end():]
    # cut at the next H2
    nxt = re.search(r"^##\s+", body, re.MULTILINE)
    if nxt:
        body = body[: nxt.start()]

    bullets = re.findall(r"^-\s+`\[(c\d+)\]`.*", body, re.MULTILINE)
    if not bullets:
        print("FAIL: section present but no [cnn] bullets matched")
        return 1

    failures = []
    for line in body.splitlines():
        m2 = re.match(r"^-\s+`\[(c\d+)\]`", line)
        if not m2:
            continue
        cid = m2.group(1)
        # must contain "links:" then [[claims/...]] anywhere afterwards
        if "links:" not in line:
            failures.append((cid, "missing 'links:' field", line))
            continue
        tail = line.split("links:", 1)[1]
        if not re.search(r"\[\[claims/[A-Za-z0-9\-]+\]\]", tail):
            failures.append((cid, "no [[claims/{slug}]] in links:", line))
            continue
        # TODO is a Step-3 placeholder that Step 4 must back-fill; treat as fail.
        if re.search(r"\[\[claims/TODO\]\]", tail):
            failures.append((cid, "[[claims/TODO]] placeholder not back-filled", line))

    print(f"Checked {len(bullets)} [cnn] bullets in {path}")
    if failures:
        print(f"\nHARD FAIL: {len(failures)} bullet(s) violate Step 4.E")
        for cid, why, line in failures:
            print(f"  [{cid}] {why}")
            print(f"    {line[:160]}{'…' if len(line) > 160 else ''}")
        return 1
    print("PASS: every [cnn] bullet has [[claims/{slug}]] reverse-link")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path/to/paper.md>", file=sys.stderr)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
