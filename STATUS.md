# OmegaWiki — Estado al 2026-05-08 (final del dia)

## Resumen del dia (commits)

- 7f2921f gitignore *.backup
- 7efb442 patches Step 3 (two-pass writing) + Step 4.E (HARD FAIL)
- 67e7b44 fix lowercase [cnn]
- f80b762 reingest Lazarov to ingest_version 2 (validacion en produccion)
- 4cccd91 mejoras: validador canonico, reingest protocol, PyMuPDF declaration
- <commit-actual> normalizacion + recovery + STATUS

## Estado actual del wiki

- papers:      6
- concepts:    45
- foundations: 47
- people:      21
- claims:      75 (60 + 15 huerfanos recuperados)
- edges:       186

## Papers - estado del validador

| Paper | Validador | Bullets [cnn] | Enlazados | Estado |
|---|---|---|---|---|
| Lazarov 2023 (physiology-diseases-tissue-resident-macrophages) | PASS | 22 | 22/22 | Completo |
| Calafell 2024 (TUYO) (nf-kb-tet2-promote-macrophage-reprogramming) | FAIL | 30 | 12/30 | 18 stubs pendientes |
| cross-tissue-single-cell-landscape-human | FAIL | 27 | 5/27 | 22 stubs pendientes |
| molecular-landmarks-tumor-hypoxia-across-cancer | FAIL | 31 | 4/31 | 27 stubs pendientes |
| hypoxia-driven-crosstalk-between-tumor-tumor | FAIL | 28 | 0/28 | 28 stubs pendientes |
| tissue-resident-macrophages-provide-pro-tumorigenic | FAIL | 0 | - | Vacio (reingest necesario) |

Total: 95 bullets sin claim file + 1 paper vacio.

## Lo que se hizo hoy

1. Patches al SKILL.md de /ingest:
   - Step 3: two-pass writing para All claims con [[claims/TODO]] placeholders
   - Step 4.E: HARD FAIL si bullet [cnn] no enlaza a [[claims/{slug}]]
   - Step 2: reingest protocol explicito
   - PyMuPDF declarado canonico
2. Validador canonico tools/validate_step4e.py commiteado
3. Reingest de Lazarov para validar patches en produccion (PASS, 22/22)
4. Normalizacion de formato [C01] -> [c01] con backticks en 4 papers
5. Recovery de 15 claims que se borraron por error

## Contexto historico relevante

- Commit e49bd73 (Tue May 5 2026): "Wiki state v2: reprocessed Calafell 2024 with adapted skill"
  Eres tu, hace 3 dias. Procesaste tu paper con una skill adaptada que NO es la actual.
  Por eso tu paper tiene formato pre-canonical. Esto NO es residuo casual.

## Decision pendiente para manana

Tres caminos posibles, decidir con cabeza fresca:

### Opcion A: Crear 95 stubs (10 min, sin Opus)
Stubs minimos para cada bullet sin claim file. El validador pasaria 100% en 4
papers. Pierdes contenido rico de los claims (son esqueletos), pero la info
del paper esta en el bullet con quote y pagina.

### Opcion B: Reingest selectivo de papers que mas importan
Empezar por Calafell 2024 (el tuyo). Coste ~30% Opus por paper. Calidad
maxima de claims, pero pierdes el contenido actual del paper.

### Opcion C: Reset wiki + reingest masivo con /init mode
Borrar todo, reingerir 6 papers con la skill nueva. Coste: ~180% Opus
(2-3 dias de cuota Max). Coherencia total al final.

### Recomendacion (yo, fresco): Opcion A primero, luego decidir B vs C
Stubs ahora -> wiki coherente. Despues decidir si quieres calidad maxima
en algun paper concreto via reingest.

## Tareas pendientes adicionales

- 15 claim files huerfanos recuperados (no enlazados desde ningun bullet).
  Decidir: matchear, dejar, o borrar.
- 1 paper vacio (tissue-resident-pro-tumorigenic). Necesita reingest fresco.
- Investigar si hay mas trabajo previo en commits viejos (ver e49bd73 y
  commits anteriores del 5-9 de mayo).

## Comando util para retomar manana

Validar todos los papers:

    for f in wiki/papers/*.md; do
      .venv/bin/python tools/validate_step4e.py "$f" 2>&1 | grep -E "^(PASS|FAIL|HARD)" | head -1 | xargs -I{} echo "$(basename $f .md): {}"
    done

Ver historia git completa:

    git log --all --oneline | head -30
