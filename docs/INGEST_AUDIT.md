---
title: INGEST_AUDIT
date: 2026-05-09
author: Pep Calafell-Segura
status: design-doc
related: .claude/skills/ingest/SKILL.md
---

# Auditoría de la skill `/ingest` v1 y plan de mejoras incrementales

## 1. Contexto

Sesión 9 mayo 2026. Después de procesar 6 papers con `/ingest` v1 (Calafell, Mulder, Casanova-Acebes, Park, Bhandari, Bai), se evaluó la posibilidad de refactorizar la skill en sub-skills con asignación de modelo (Sonnet/Opus) por paso.

**Decisión**: NO refactorizar. La skill v1 está bien diseñada. Aplicar mejoras incrementales que no rompen su lógica.

Este documento captura el razonamiento para no perderlo cuando regresemos a esta decisión en futuras sesiones.

## 2. Lo que `/ingest` v1 hace bien (no tocar)

### 2.1 Separación clara de responsabilidades

`/ingest` emite entidades correctas (shape check); `/check` audita semántica (backlink symmetry, dangling nodes, field-value policing). Esta separación es la "validación" que se buscaba en la sesión del 8 mayo. **No hay que reinventarla, ya existe.**

### 2.2 Sistema INIT MODE / direct mode

La skill detecta si la invoca `/init` (manifest-driven, parallel-safe via worktrees) o un usuario directamente. En INIT MODE:
- Skip Step 5 (paper-to-paper edges) — `/init` lo hace al fan-in
- Skip `rebuild-context-brief` y `rebuild-open-questions` — `/init` los corre una vez
- Skip reverse links en pages existentes — `/init` los backfilla

Romper esto al refactorizar habría introducido race conditions difíciles de debuguear. Mantener.

### 2.3 Worktree-safety

Lookup de PYTHON_BIN vía `git rev-parse --git-common-dir` para que subagents en `.worktrees/<branch>/` encuentren `.venv` del repo principal (que es gitignored). Esto es ingeniería avanzada y necesaria.

### 2.4 `/discover` integrado vía flag `--discover`

Step 9 invoca `/discover --anchor <arxiv-id>` y append una shortlist al reporte. **Esto resuelve directamente la R3 del usuario** ("buscar más papers, encontrar joyas"). No hay que construir un sistema nuevo, solo mejorar el existente.

### 2.5 Policy biomedical específica (Step 4)

Domain-adapted policy explícita para biomedical:
- Claim exhaustivity por tier: 15-30 (TIER_1) / 5-10 (TIER_2) / 3-5 (TIER_3)
- Claims tipados: mechanistic / correlational / methodological / pharmacological / quantitative
- Concept aliases broad (6-12 mínimo, paper-specific + generalizable)
- Foundations para métodos comunes (Scanpy, scVI, DoRothEA, HOMER, ChIP-seq, CUT&RUN, ATAC-seq, EPIC array, RRBS, CIBERSORTx, CellChat, NicheNet)
- HARD FAIL si `aliases` < 6 o biomedical frontmatter vacío (`tissue`, `condition`, `species`, `techniques`, `key_cell_types`, `key_markers`, `projects`)

Esta policy ya está adaptada al campo. Una refactor genérica la habría diluido.

### 2.6 People tier suggestion (no auto-update)

Step 4.4 incrementa `papers_in_vault` y sugiere tier change al usuario sin auto-modificar. Evita silent state changes. Mantener.

### 2.7 Layer Python sólido

- `tools/research_wiki.py` — slug, find-similar, add-edge, add-citation, log, rebuild
- `tools/fetch_s2.py` — Semantic Scholar
- `tools/fetch_deepxiv.py` — DeepXiv (graceful fallback)
- `tools/init_discovery.py` — single-paper arXiv source/PDF download
- `tools/prepare_paper_source.py` — PDF preprocessing
- `tools/discover.py` — discovery con anchors

`add-edge` rechaza missing confidence/evidence en paper-paper y paper-concept semantic edges, y rechaza legacy types. Validación a nivel tool. Buena defensa.

## 3. Mejoras incrementales propuestas (NO refactor)

### Mejora 1 — Asignación Sonnet en steps mecánicos vía subagents

**Problema**: Todo el `/ingest` corre en Opus 4.7. Steps 5-7 son mecánicos (matching + append + ejecutar comandos) y no requieren juicio semántico.

**Cambio propuesto**: invocar subagents con `model: sonnet` para steps mecánicos.

**Mapeo modelo por step**:

| Step | Tarea | Modelo | Razón |
|---|---|---|---|
| 1 | Resolve source | Opus | Branching, INIT MODE detection |
| 2 | Paper identity, importance score | Opus | Juicio semántico (importance) |
| 3 | Paper page (problem, key idea, claims, discussion) | Opus | Núcleo semántico del ingest |
| 4 | Concepts, claims, people | Opus | Dedup decisions, tier policy |
| 5 | Paper-to-paper edges, citations | **Sonnet** | Matching arXiv-ID → existing slug, append-only |
| 6 | Topics y index | **Sonnet** | Matching tags, append por tier |
| 7 | Log y rebuild | **Sonnet** | Ejecutar comandos |
| 8 | Report | Opus | Síntesis final |
| 9 | Optional discovery | Opus | Si se invoca |

**Ahorro estimado**: 40-50% cuota Opus por ingest.

**Cómo implementar (sin tocar Steps 1-4)**:
1. En Step 5, invocar subagent: `Task(model: sonnet, description: "Add paper-to-paper edges and citations for {arxiv-id}", prompt: <Step 5 instructions>)`
2. En Step 6, mismo patrón
3. En Step 7, mismo patrón
4. Subagents devuelven summary; Opus principal compila el reporte final en Step 8

**Riesgo**: subagent Sonnet podría no entender `references/cross-references.md` para edge-type selection en Step 5. **Mitigación**: pre-cargar la reference en el prompt del subagent.

**Validación antes de aceptar**: re-procesar Bai 2022 con la skill modificada y comparar:
- Mismos paper-paper edges?
- Mismas citations?
- Misma topic placement?
- Si hay drift > 5% en cualquier output, revertir.

### Mejora 2 — Pre-check de calidad antes de Step 3

**Problema**: La calidad de los 6 papers procesados es variable (algunos tienen claims más densos que otros). Esto sugiere que la skill funciona mejor cuando ha visto un ejemplo bueno reciente.

**Cambio propuesto**: añadir una pre-action al Step 3 que cargue como ejemplo el paper TIER_1 más reciente del wiki como referencia de calidad esperada.

**Cómo**:
- Antes de Step 3, leer `wiki/papers/Bai-2022.md` (el TIER_1 más reciente con 4 cross-paper edges)
- Pasarlo al modelo como "Reference quality target: this is the level of detail expected"
- No requiere cambios estructurales, solo añadir un párrafo a Step 3

**Riesgo bajo**, beneficio incremental en consistencia.

### Mejora 3 — `/check` skill (validar que existe y completarla)

**Problema**: `/ingest` v1 menciona repetidamente `/check` como owner de "backlink symmetry, dangling nodes, full semantic audits". Verificar:
1. ¿Existe `.claude/skills/check/SKILL.md`?
2. ¿Cubre lo que `/ingest` delega (líneas 287-288)?

**Acción**:
- Si NO existe → crearla. Sería violar el contrato de `/ingest`.
- Si existe pero incompleta → completarla.
- Si existe y completa → solo documentar en este audit que está OK.

**Tareas mínimas que `/check` debe cubrir**:
- Backlink symmetry (todo forward link tiene reverse)
- Dangling nodes (entities sin papers en `key_papers`)
- Slug duplication (semantic title similarity)
- YAML validity en todos los wiki/*.md
- Concepts sin "Key papers" section
- Foundations huérfanas (ningún paper las referencia)
- Edges referenciando archivos no existentes

### Mejora 4 — Validator Python sin LLM (Opción A del status anterior)

**Independiente de la skill**, mantiene relevancia.

`scripts/validate_wiki.py`:
- Detecta: duplicate slugs, semantic title similarity, foundations huérfanas, edges referenciando archivos no existentes, YAML inválido, concepts sin "Key papers" section
- Output: `docs/wiki_validation_report.md`
- Coste: 0 cuota Claude
- Tiempo de construcción: 30-45 min en Claude Code

Complementa `/check` (que sí usa LLM). Validator es check rápido sin gastar; `/check` es audit semántico profundo.

### Mejora 5 — Tier-ranking script Python (Opción B del status anterior)

Mantiene relevancia. La frustración real "elegir paper" sigue ahí.

`scripts/tier_candidates.py`:
- Para cada PDF en `raw/papers/`: extrae metadata, query S2 (citations, venue), computa keyword overlap con concepts/foundations existentes del wiki
- Output: ranking priorizado en markdown con justificación
- Coste: 0 cuota Claude
- Tiempo de construcción: 30-45 min

## 4. Lo que NO se va a tocar

- Steps 1-4 (lógica core)
- Policy dedup
- Policy biomedical Step 4
- Sistema INIT MODE
- Layer Python (tools/)
- HARD FAIL validations (Step 4.E)
- People tier suggestion (no auto-update)
- Worktree-safety en PYTHON_BIN lookup

## 5. Orden de ejecución propuesto

| # | Tarea | Tiempo | Coste sesión | Dónde |
|---|---|---|---|---|
| 1 | Verificar existencia y completud de `/check` | 15 min | bajo | Claude Code |
| 2 | Si falta, crear/completar `/check` | 1 sesión | medio | Claude Code |
| 3 | Construir `validate_wiki.py` | 30-45 min | 0 (sin LLM) | Claude Code |
| 4 | Construir `tier_candidates.py` | 30-45 min | 0 (sin LLM) | Claude Code |
| 5 | Aplicar Mejora 1 (subagents Sonnet en Steps 5-7) | 1 sesión | medio | Claude Code |
| 6 | Re-procesar Bai 2022 con skill modificada y comparar | 1 ingest | bajo si comparado | Claude Code |
| 7 | Aplicar Mejora 2 (pre-check calidad) | 30 min | bajo | Claude Code |
| 8 | Re-validar con paper nuevo | 1 ingest | normal | Claude Code |

## 6. Métricas de éxito

Antes de aceptar cualquier mejora aplicada al `/ingest`:

- **Cuota Opus por ingest**: medir antes y después. Target: -40% mínimo en Mejora 1.
- **Cross-paper edges**: contar antes y después. Target: ≥ que la baseline (no perder edges).
- **Claims extraídos**: contar antes y después. Target: ≥ que la baseline.
- **Tiempo wall-clock por ingest**: antes y después. Target: ≤ baseline.
- **HARD FAIL count**: target 0 (no romper validations existentes).

Si alguna métrica empeora, revertir el cambio.

## 7. Decisiones rechazadas (sesión 9 mayo)

| Decisión rechazada | Por qué |
|---|---|
| Refactorizar `/ingest` en 7 sub-skills | La v1 está bien diseñada. Refactor habría roto INIT MODE, separación `/ingest` vs `/check`, y policy biomedical adaptada. |
| Reemplazar `tools/fetch_s2.py` por K-Dense `paper-lookup` | El v1 funciona. K-Dense entra en `/discover`, no en `/ingest`. |
| Auto-procesar 30 papers en batch con subagent paralelos | Cuota Max finita. Cross-paper edges requieren wiki ya construido — orden importa. Sin supervisión humana, después de 20 papers tendríamos concepts duplicados. |
| Construir validator basado en LLM en vez de Python | Validator es check rápido y barato. Python sin LLM es lo correcto. `/check` (que sí usa LLM) cubre lo semántico. |

## 8. Notas para sesiones futuras

- Cuando regreses a este audit, lee primero la skill `/ingest` actual. Si ha cambiado, este documento puede estar desactualizado.
- Si ves que tu yo-anterior decidió no refactorizar y ahora te tienta refactorizar, vuelve a leer Sección 2 antes de proceder.
- La skill v1 evolucionará con mejoras incrementales (Mejoras 1-5). Documentar cada cambio en Git con commit message claro.
