# OmegaWiki — Estado al 2026-05-11 (sesión IJC)

## Resumen del día

Plan crítico del 9 de mayo (Tareas 1-5 del INGEST_AUDIT) COMPLETADO.

## Commits del día

- 7d9f32f ingest(reingest): Bhandari 2019 → ingest_version 2 (Tarea 3)
- 6656a1e ingest(reingest): Bai 2022 → ingest_version 2 + 16 claims nuevos (Tarea 4)

## Estado del wiki

- papers:      6
- claims:      91 (+16 hoy en Bai reingest)
- concepts:    45
- foundations: 47
- people:      21
- edges:       211 (+25 hoy)

## Validador por paper

| Paper | Validador | Bullets [cnn] |
|---|---|---|
| Lazarov 2023 | PASS | 22/22 |
| Bhandari 2019 (molecular-landmarks) | PASS | 31/31 |
| Bai 2022 (hypoxia-driven-crosstalk) | PASS | 28/28 |
| Calafell 2024 (TUYO, nf-kb-tet2) | FAIL | 12/30 |
| Park (cross-tissue) | FAIL | 5/27 |
| Tissue-resident-pro-tumorigenic | FAIL | 0 (vacío) |

## Lint global

- 🔴 (crítico) : 0
- 🟡 (warning) : 0
- 🔵 (info)    : 0

**Target de INGEST_AUDIT Tarea 5 alcanzado y excedido por primera vez.**

## Plan crítico (Tareas 1-5) - status

- [x] Tarea 1: Mejora 6 HARD FAIL Step 4.E
- [x] Tarea 2: Validar Mejora 6 con Lazarov reingest
- [x] Tarea 3: Reset selectivo Bhandari + reingest
- [x] Tarea 4: Reset selectivo Bai + reingest
- [x] Tarea 5: /check global 0/0/0

## Pendiente (no bloqueante)

### Reingests / fixes futuros

- Calafell 2024 (TU paper): 18 bullets sin claim file. Coste: ~25% Opus por
  reingest. Posibilidad: aplicar mismo procedimiento que Bai (Opus crea
  claims nuevos para bullets sin pareja).
- cross-tissue-single-cell-landscape-human (Park): 22 bullets sin claim file.
  Mismo procedimiento.
- tissue-resident-macrophages-provide-pro-tumorigenic: paper vacío. Necesita
  reingest completo desde PDF.

### Mejoras al sistema

- Mejora 1: Sonnet subagents en Steps 5-7 de /ingest (40-50% ahorro Opus)
- Mejora 2: Pre-check de calidad referencia (Lazarov como TIER_1 baseline)
- Mejora 5: scripts/tier_candidates.py (resolver frustración "elegir paper")

### Integración externa

- K-Dense Iteración 1: paper-lookup, database-lookup, bgpt-paper-search
  vendoring. Procedimiento en KDENSE_INTEGRATION_PLAN.md §5.

### Contradicción notada (worth flagging in thesis)

- hif2a-spint1-tam-suppresses-tumor-via-hgfa flag: Belzutifan/PT2385 pueden
  remover Spint1 brake en HGF activation. Confounder para tratamientos
  HIF-2α en thesis section.

## Tags actuales

- pre-reingest-bai (rollback Bai)
- pre-reingest-bhandari (rollback Bhandari)
- baseline-opus-mulder-casanova
- v1-baseline
- v2-pre-inventory

## Comando útil para retomar

    cd ~/omegawiki
    git pull origin main
    .venv/bin/python tools/lint.py --wiki-dir wiki/
    for f in wiki/papers/*.md; do
      .venv/bin/python tools/validate_step4e.py "$f" 2>&1 | grep -E "^(PASS|FAIL|HARD)" | head -1 | xargs -I{} echo "$(basename $f .md): {}"
    done

## Siguiente acción recomendada (cuando retomes)

Opción A: Reingest Calafell 2024 (TU paper, completar el más importante)
Opción B: Reingest cross-tissue Park (más bullets sin claim file)
Opción C: Construir tier_candidates.py (sin Opus, prepara escalado)
Opción D: K-Dense Iteración 1 (vendoring, prepara nuevas capacidades)
