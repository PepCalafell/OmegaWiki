#!/usr/bin/env python3
"""check_duplicates.py — detección de duplicados en OmegaWiki.

Pensado para correr DESPUÉS de cada /ingest, dentro de verify_paper.sh.
NO usa IA. NO añade dependencias (solo stdlib: difflib, re, pathlib).

Detecta DOS cosas distintas, con lógica distinta a propósito:

  1. CONCEPTOS duplicados — el mismo concepto escrito con dos nombres.
     (ej. tumor-associated-macrophage vs tumour-associated-macrophages)
     Acción esperada: fusionar los dos nodos en uno.

  2. CLAIMS duplicados INTRA-PAPER — el mismo paper generó dos veces el
     mismo claim. Es un fallo del ingest, no convergencia entre papers.
     Acción esperada: borrar uno de los dos.

Lo que este script deliberadamente NO hace:
  - NO marca conceptos "vecinos" (M1 vs M2 polarization) como duplicados.
    Son nodos legítimamente distintos. Por eso no basta similitud de
    string: se exige además una segunda señal (alias o variante
    morfológica) antes de avisar.
  - NO compara claims entre papers distintos. Dos papers que sostienen
    algo parecido es CONVERGENCIA DE EVIDENCIA, no duplicación. Marcarlo
    destruiría justo la señal que un knowledge graph existe para capturar.
  - NO detecta controversias. Un claim que contradice a otro se marca
    con status: challenged en el ingest; no es trabajo de este script.

Todos los avisos son 🟡 (no bloquean commit). Un duplicado a veces no
lo es; la decisión de fusionar la tomas tú, con el contexto fresco.

Salida: imprime avisos y SIEMPRE devuelve 0 (no bloqueante). El que
bloquea es verify_paper.sh, que decide qué hacer con esta salida.

Uso:
  python check_duplicates.py --wiki-dir wiki/
  python check_duplicates.py --wiki-dir wiki/ --threshold equilibrado
"""

import argparse
import difflib
import re
import sys
from pathlib import Path

# ----------------------------------------------------------------------
# UMBRALES
# El "umbral" solo se aplica a la señal más ruidosa: similitud de string
# pura entre slugs. Las otras dos señales (alias compartido, variante
# morfológica) van siempre activas: casi no dan falsos positivos ni en un
# dominio temático cerrado, así que no tiene sentido apagarlas.
# ----------------------------------------------------------------------
THRESHOLDS = {
    "sensible":   0.82,
    "equilibrado": 0.88,
    "estricto":   0.93,
}

# ----------------------------------------------------------------------
# Parsing de frontmatter YAML — mínimo, sin dependencia de pyyaml.
# Soporta: 'campo: valor' y listas multilínea ('campo:' + '  - item').
# ----------------------------------------------------------------------

def parse_frontmatter(path):
    """Devuelve dict {campo: valor|lista}. Valores escalares como str,
    listas como list[str]. Devuelve {} si no hay frontmatter."""
    text = path.read_text(errors="ignore")
    if not text.startswith("---"):
        return {}
    # frontmatter = entre el primer --- y el segundo ---
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    fm = parts[1]

    data = {}
    current_list_key = None
    for raw in fm.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.strip().startswith("#"):
            continue
        # item de lista multilínea: '  - valor'
        m_item = re.match(r"\s*-\s+(.*)$", line)
        if m_item and current_list_key is not None:
            val = m_item.group(1).strip().strip("\"'")
            # ignorar wikilinks vacíos / placeholders
            if val:
                data[current_list_key].append(val)
            continue
        # 'campo: valor'  ó  'campo:' (abre lista)
        m_kv = re.match(r"([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m_kv:
            key, val = m_kv.group(1), m_kv.group(2).strip()
            if val == "" or val == "[]":
                # abre una posible lista multilínea
                data[key] = []
                current_list_key = key
            else:
                # valor inline; puede ser lista inline [a, b]
                current_list_key = None
                if val.startswith("[") and val.endswith("]"):
                    inner = val[1:-1].strip()
                    data[key] = [x.strip().strip("\"'")
                                 for x in inner.split(",") if x.strip()]
                else:
                    data[key] = val.strip("\"'")
        else:
            current_list_key = None
    return data


# ----------------------------------------------------------------------
# Normalización morfológica.
# La huella de un duplicado real (frente a un vecino) es una diferencia
# trivial: plural, variante ortográfica EN/US, guion vs nada. Si tras
# normalizar dos slugs distintos COINCIDEN, es casi seguro un duplicado.
# ----------------------------------------------------------------------

_US_UK = [
    ("tumour", "tumor"), ("oedema", "edema"), ("haemo", "hemo"),
    ("signalling", "signaling"), ("ageing", "aging"),
    ("ise", "ize"), ("isation", "ization"), ("yse", "yze"),
]

def normalize(slug):
    """Reduce un slug a su 'núcleo' morfológico para comparar."""
    s = slug.lower().strip()
    s = s.replace("_", "-")
    # variantes ortográficas UK/US
    for uk, us in _US_UK:
        s = s.replace(uk, us)
    # quitar guiones para comparar el esqueleto de tokens
    tokens = [t for t in s.split("-") if t]
    norm_tokens = []
    for t in tokens:
        # despluralizar de forma conservadora
        if len(t) > 4 and t.endswith("ies"):
            t = t[:-3] + "y"
        elif len(t) > 3 and t.endswith("es") and not t.endswith("ses"):
            t = t[:-2]
        elif len(t) > 3 and t.endswith("s") and not t.endswith("ss"):
            t = t[:-1]
        norm_tokens.append(t)
    return "-".join(norm_tokens)


def token_set(slug):
    return {t for t in normalize(slug).split("-") if t}


# Un token es "discriminante" si distingue dos entidades hermanas a
# propósito (M1 vs M2, CD4 vs CD8, type-i vs type-ii). Cuando dos slugs
# casi idénticos difieren SOLO en un token de este tipo, NO son
# duplicados: son un par contrastivo legítimo y deben quedar separados.
_DISCRIMINANT = re.compile(
    r"^("
    r"m\d+|"             # M1, M2 ...
    r"cd\d+[a-z]?|"      # CD4, CD8, CD8a ...
    r"type|"             # type-i / type-ii
    r"i{1,3}v?|iv|v|"    # numerales romanos i..v
    r"\d+|"              # cualquier número suelto
    r"alpha|beta|gamma|delta|"
    r"hif\d+a?"          # HIF1 vs HIF2
    r")$"
)

def is_contrastive_pair(slug_a, slug_b):
    """True si los dos slugs difieren EXACTAMENTE en un token y ese
    token es discriminante en ambos lados. Esos pares son hermanos
    legítimos, no duplicados."""
    ta = normalize(slug_a).split("-")
    tb = normalize(slug_b).split("-")
    if len(ta) != len(tb):
        return False
    diffs = [(x, y) for x, y in zip(ta, tb) if x != y]
    if len(diffs) != 1:
        return False
    x, y = diffs[0]
    return bool(_DISCRIMINANT.match(x)) and bool(_DISCRIMINANT.match(y))


# ----------------------------------------------------------------------
# CONCEPTOS
# ----------------------------------------------------------------------

def get_concept_record(path):
    """Extrae lo necesario de un concepto. Defensivo: si falta un campo
    esperado, lo deja vacío y lo reporta — no inventa la estructura."""
    fm = parse_frontmatter(path)
    slug = path.stem
    title = fm.get("title", "")
    aliases = fm.get("aliases", [])
    if isinstance(aliases, str):
        aliases = [aliases] if aliases else []
    missing = []
    if not fm:
        missing.append("frontmatter")
    if "aliases" not in fm:
        missing.append("aliases")
    return {
        "slug": slug,
        "path": path,
        "title": title if isinstance(title, str) else "",
        "aliases": [a for a in aliases if a],
        "missing": missing,
    }


def alias_keys(rec):
    """Conjunto de strings normalizados que IDENTIFICAN el concepto:
    su slug, su title y sus aliases. Si dos conceptos comparten uno,
    casi seguro son el mismo."""
    keys = {normalize(rec["slug"])}
    if rec["title"]:
        keys.add(normalize(rec["title"].replace(" ", "-")))
    for a in rec["aliases"]:
        keys.add(normalize(a.replace(" ", "-")))
    return {k for k in keys if k}


def check_concepts(wiki_dir, threshold):
    concepts_dir = wiki_dir / "concepts"
    if not concepts_dir.exists():
        print("  [warn] no existe wiki/concepts/ — salto check de conceptos")
        return []

    records = [get_concept_record(p)
               for p in sorted(concepts_dir.glob("*.md"))]

    # aviso si el esquema no es el esperado (campo adivinado)
    schema_warned = False
    for r in records:
        if "aliases" in r["missing"] and not schema_warned:
            print(f"  [schema] '{r['slug']}' no tiene campo 'aliases'. "
                  f"Si el campo se llama distinto, ajústalo en "
                  f"get_concept_record(). Sigo solo con slug+title.")
            schema_warned = True

    findings = []
    n = len(records)
    for i in range(n):
        for j in range(i + 1, n):
            a, b = records[i], records[j]
            reasons = []

            # señal 1 — alias / title / slug compartido (la más fuerte)
            shared = alias_keys(a) & alias_keys(b)
            if shared:
                reasons.append(f"identificador compartido: {sorted(shared)}")

            # señal 2 — coinciden tras normalizar morfología
            if normalize(a["slug"]) == normalize(b["slug"]) and not shared:
                reasons.append("slugs idénticos tras normalizar "
                               "(plural / variante EN-US)")

            # señal 3 — similitud de string alta SOBRE LOS SLUGS
            #           NORMALIZADOS. Antes de avisar, se descartan los
            #           pares contrastivos (M1/M2, CD4/CD8): difieren en
            #           un único token discriminante y son hermanos
            #           legítimos, no duplicados.
            na, nb = normalize(a["slug"]), normalize(b["slug"])
            ratio = difflib.SequenceMatcher(None, na, nb).ratio()
            if (ratio >= threshold
                    and not reasons
                    and not is_contrastive_pair(a["slug"], b["slug"])):
                reasons.append(f"slugs muy similares "
                               f"tras normalizar (ratio={ratio:.2f})")

            if reasons:
                findings.append({
                    "kind": "concepto",
                    "a": a["slug"], "b": b["slug"],
                    "reasons": reasons,
                })
    return findings


# ----------------------------------------------------------------------
# CLAIMS — solo duplicado INTRA-PAPER.
# Definición estricta de "intra-paper": MISMO conjunto de source_papers.
# Si comparten un paper pero no todos, es multi-fuente legítimo
# (INGEST_AUDIT.md §9.3: 12 claims multi-fuente son válidos por esquema).
# ----------------------------------------------------------------------

def get_claim_record(path):
    fm = parse_frontmatter(path)
    srcs = fm.get("source_papers", [])
    if isinstance(srcs, str):
        srcs = [srcs] if srcs else []
    # limpiar wikilinks: [[papers/slug]] -> slug
    clean = []
    for s in srcs:
        s = s.strip()
        m = re.search(r"papers/([\w-]+)", s)
        clean.append(m.group(1) if m else s.strip("[]"))
    # texto del claim: title del frontmatter (es la afirmación)
    title = fm.get("title", "")
    return {
        "slug": path.stem,
        "path": path,
        "sources": frozenset(c for c in clean if c),
        "title": title if isinstance(title, str) else "",
        "has_fm": bool(fm),
    }


def _claim_text_norm(s):
    """Normaliza el texto de un claim para comparar: minúsculas, sin
    puntuación, espacios colapsados."""
    s = s.lower()
    s = re.sub(r"[^\w\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def check_claims(wiki_dir, threshold):
    claims_dir = wiki_dir / "claims"
    if not claims_dir.exists():
        print("  [warn] no existe wiki/claims/ — salto check de claims")
        return []

    records = [get_claim_record(p)
               for p in sorted(claims_dir.glob("*.md"))]

    if records and not any(r["sources"] for r in records):
        print("  [schema] ningún claim tiene 'source_papers' parseable. "
              "Si el campo se llama distinto, ajústalo en "
              "get_claim_record(). Salto check de claims.")
        return []

    findings = []
    n = len(records)
    for i in range(n):
        for j in range(i + 1, n):
            a, b = records[i], records[j]
            # intra-paper estricto: MISMO conjunto de fuentes, no vacío
            if not a["sources"] or a["sources"] != b["sources"]:
                continue
            if not a["title"] or not b["title"]:
                continue
            ta = _claim_text_norm(a["title"])
            tb = _claim_text_norm(b["title"])
            ratio = difflib.SequenceMatcher(None, ta, tb).ratio()
            if ratio >= threshold:
                findings.append({
                    "kind": "claim intra-paper",
                    "a": a["slug"], "b": b["slug"],
                    "reasons": [
                        f"mismas fuentes ({sorted(a['sources'])}) "
                        f"y texto casi idéntico (ratio={ratio:.2f})"
                    ],
                })
    return findings


# ----------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki-dir", default="wiki/",
                    help="ruta al directorio wiki/")
    ap.add_argument("--threshold", default="equilibrado",
                    choices=list(THRESHOLDS.keys()),
                    help="sensibilidad de la señal de similitud de string")
    args = ap.parse_args()

    wiki_dir = Path(args.wiki_dir)
    thr = THRESHOLDS[args.threshold]

    if not wiki_dir.exists():
        print(f"ERROR: no existe {wiki_dir}", file=sys.stderr)
        return 0  # no bloqueante por diseño

    print(f"  umbral: {args.threshold} ({thr})")

    concept_findings = check_concepts(wiki_dir, thr)
    claim_findings = check_claims(wiki_dir, thr)
    all_findings = concept_findings + claim_findings

    if not all_findings:
        print("  -> sin duplicados sospechosos")
        return 0

    print(f"  -> {len(all_findings)} 🟡 par(es) sospechoso(s) "
          f"({len(concept_findings)} conceptos, "
          f"{len(claim_findings)} claims):")
    for f in all_findings:
        print(f"     🟡 [{f['kind']}]")
        print(f"        A: {f['a']}")
        print(f"        B: {f['b']}")
        for r in f["reasons"]:
            print(f"        · {r}")
    print()
    print("  Conceptos: si son el mismo, fusiónalos en un nodo.")
    print("  Claims intra-paper: si son el mismo, borra uno.")
    print("  Si son entidades distintas (vecinos), ignora el aviso.")
    print("  Antes de fusionar conceptos: revisa si los claims que")
    print("  arrastran tienen status opuestos (proposed/challenged) —")
    print("  ahí hay una controversia que debes conservar, no aplastar.")

    return 0  # 🟡 nunca bloquea; verify_paper.sh decide


if __name__ == "__main__":
    sys.exit(main())
