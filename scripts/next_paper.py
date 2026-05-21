#!/usr/bin/env python3
"""Identifica el siguiente paper del ranking que NO esta en el wiki.

Genera slug con la herramienta oficial research_wiki.py (misma que usa
/ingest), evitando el bug de slug-adivinado. Filtra ruido del ranking:
previews, comments, biorxiv preprints sueltos, duplicados.

Uso: .venv/bin/python scripts/next_paper.py
"""
import os, re, glob, subprocess, sys

WIKI_PAPERS = "wiki/papers"
RANKING = "docs/paper_candidates.md"
RAW_DIR = "raw/papers"
PYBIN = ".venv/bin/python"

# Prefijos de filename que NO son papers completos para ingestar
NOISE_PREFIXES = ("preview_", "comment_", "biorxiv ", "brief_comm_")

# Papers ya en wiki cuyo filename cripto no resuelve al slug correcto.
# substring-del-filename -> slug real en wiki
KNOWN_ALIASES = {
    "calafell_2024_nfkb_tet2": "nf-kb-tet2-promote-macrophage-reprogramming",
}


def official_slug(title):
    """Genera el slug con la misma herramienta que usa /ingest."""
    try:
        out = subprocess.run(
            [PYBIN, "tools/research_wiki.py", "slug", title],
            capture_output=True, text=True, timeout=30
        )
        for line in out.stdout.splitlines():
            line = line.strip()
            if line and not line.startswith("-") and not line.startswith("="):
                return line
    except Exception as e:
        print(f"  [warn] slug fallo: {e}", file=sys.stderr)
    return None


def main():
    existing = set()
    for f in glob.glob(f"{WIKI_PAPERS}/*.md"):
        existing.add(os.path.basename(f)[:-3])

    print(f"Papers ya en wiki: {len(existing)}\n")

    candidates = []
    with open(RANKING) as fh:
        for line in fh:
            m = re.match(r'\|\s*(\d+)\s*\|\s*(.+?)\s*\|.*pending', line)
            if m:
                candidates.append((int(m.group(1)), m.group(2).strip()))

    print("=" * 72)
    print("BUSCANDO SIGUIENTE PAPER PENDIENTE (ruido filtrado)")
    print("=" * 72 + "\n")

    pdfs = glob.glob(f"{RAW_DIR}/*.pdf")
    found_next = False
    next_pdf = next_num = None
    seen_slugs = set()
    skipped_noise = skipped_dup = 0

    for num, title_partial in candidates:
        title_words = re.sub(r'[^\w\s]', '', title_partial.lower()).split()[:4]
        matched_pdf = None
        for pdf in pdfs:
            pdf_lower = re.sub(r'[^\w\s]', '', os.path.basename(pdf).lower())
            if all(w in pdf_lower for w in title_words[:3]):
                matched_pdf = pdf
                break
        if not matched_pdf:
            continue

        fname = os.path.basename(matched_pdf)
        fname_lower = fname.lower()

        # filtro 1: ruido (previews, comments, etc.)
        if any(fname_lower.startswith(p) for p in NOISE_PREFIXES):
            skipped_noise += 1
            continue

        # comprobar alias conocidos
        alias_hit = None
        for sub, real_slug in KNOWN_ALIASES.items():
            if sub in fname_lower:
                alias_hit = real_slug
                break

        slug = alias_hit or official_slug(fname[:-4])
        already = slug in existing if slug else False

        # filtro 2: duplicado dentro del ranking
        if slug in seen_slugs:
            skipped_dup += 1
            continue
        if slug:
            seen_slugs.add(slug)

        mark = "YA EN WIKI" if already else "PENDIENTE"
        print(f"#{num:3d} [{mark:11s}] {fname[:50]}")

        if not already and slug and not found_next:
            found_next = True
            next_pdf, next_num = matched_pdf, num

    print(f"\nFiltrados: {skipped_noise} ruido, {skipped_dup} duplicados\n")
    print("=" * 72)
    if found_next:
        print(f"SIGUIENTE PAPER: #{next_num}")
        print("=" * 72)
        print("Copia esto en Claude Code:\n")
        print("/clear")
        print("/model opus")
        print("/effort medium")
        print(f'/ingest "{next_pdf}"')
    else:
        print("No hay papers pendientes con PDF y slug resoluble.")
    print("=" * 72)


if __name__ == "__main__":
    main()
