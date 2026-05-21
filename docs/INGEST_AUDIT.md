---
title: INGEST_AUDIT
date: 2026-05-09 (rev. afternoon)
author: Pep Calafell-Segura
status: design-doc
related: .claude/skills/ingest/SKILL.md, docs/STATUS_2026-05-09b.md
---

# Auditoría de la skill `/ingest` v1 y plan de mejoras incrementales

> **Revisión 2026-05-09 tarde**: añadida Mejora 6 (crítica). Ajustada Sección 5 con orden de ejecución revisado. Mejora 4 (validate_wiki.py) marcada como descartada — redundante con `/check` que ya existe.

## 1. Contexto

Sesión 9 mayo 2026. Después de procesar 6 papers con `/ingest` v1 (Calafell, Mulder, Casanova-Acebes, Park, Bhandari, Bai), se evaluó la posibilidad de refactorizar la skill en sub-skills con asignación de modelo (Sonnet/Opus) por paso.

**Decisión inicial (mañana 9 mayo)**: NO refactorizar. La skill v1 está bien diseñada. Aplicar mejoras incrementales que no rompen su lógica.

**Hallazgo posterior (tarde 9 mayo)**: la skill v1 tiene una regresión progresiva en escribir reverse links a claims en la sección `## All claims (exhaustive)`. Documentado en `STATUS_2026-05-09b.md`. Resultado: añadida Mejora 6 como crítica antes que las demás.

Este documento captura el razonamiento para no perderlo cuando regresemos a esta decisión en futuras sesiones.

## 2. Lo que `/ingest` v1 hace bien (no tocar)

### 2.1 Separación clara de responsabilidades

`/ingest` emite entidades correctas (shape check); `/check` audita semántica (backlink symmetry, dangling nodes, field-value policing). Esta separación es la "validación" que se buscaba en la sesión del 8 mayo. **No hay que reinventarla, ya existe.**

### 2.2 Sistema INIT MODE / direct mode

La skill detecta si la invoca `/init` (manifest-driven, parallel-safe via worktrees) o un usuario directamente. Mantener.

### 2.3 Worktree-safety

Lookup de PYTHON_BIN vía `git rev-parse --git-common-dir`. Mantener.

### 2.4 `/discover` integrado vía flag `--discover`

Step 9 invoca `/discover --anchor <arxiv-id>`. Resuelve la R3 del usuario.

### 2.5 Policy biomedical específica (Step 4)

Domain-adapted policy explícita para biomedical (claim exhaustivity por tier, aliases broad, foundations para métodos comunes, HARD FAIL en biomedical frontmatter). Mantener.

### 2.6 People tier suggestion (no auto-update)

Step 4.4 incrementa `papers_in_vault` y sugiere tier change al usuario sin auto-modificar.

### 2.7 Layer Python sólido

`tools/research_wiki.py`, `tools/fetch_s2.py`, `tools/fetch_deepxiv.py`, `tools/init_discovery.py`, `tools/prepare_paper_source.py`, `tools/discover.py`, `tools/lint.py`. Bien construido.

## 3. Mejoras propuestas (orden por prioridad)

### Mejora 6 — [CRÍTICA] Enforce `[[claims/{slug}]]` en sección `## All claims`

**Añadida 9 mayo tarde tras descubrir bug retrospectivo.**

#### Problema

La skill `/ingest` v1 declara como constraint global (línea 279 SKILL.md):
> "Every forward link writes its reverse link in the same turn — the wiki's bidirectional-link invariant"

Pero NO valida específicamente que cada `[Cnn]` line de la sección `## All claims (exhaustive)` contenga `[[claims/{slug-del-claim-creado}]]` en su campo `links`. Resultado: regresión progresiva entre paper 4 (Lazarov: 68% claims con reverse link) y paper 6 (Bai: 0% claims con reverse link). 15 claims huérfanos en wiki actual.

#### Diagnóstico ground-truth

Análisis del 9 mayo tarde (ver `STATUS_2026-05-09b.md` §2.4):

| Paper | Claims con `[[claims/X]]` link | Total claims | % |
|---|---|---|---|
| Calafell | 13 | ~13 | 100% |
| Mulder | 6 | ~6 | 100% |
| Casanova | 21 | ~22 | ~95% |
| Lazarov | 15 | 22 | 68% |
| Bhandari | 4 | 28 | 14% |
| Bai | 0 | 28 | 0% |

#### Cambio propuesto (a Step 3)

Añadir al Step 3 ("Write the paper page") una validación HARD FAIL post-write y pre-commit:

```
PAGE-WRITING VALIDATION (mandatory before saving the paper page):

After writing the paper page body, verify the `## All claims (exhaustive)`
section. For each `[Cnn]` bullet line:

1. Each bullet MUST end with a `— links:` field containing 1+ wikilinks.
2. The links field MUST include `[[claims/{slug}]]` where `{slug}` is the slug
   of the corresponding claim file just created in `wiki/claims/`.
3. Mapping rule: claim slug at position N of the claims list created in this
   ingest corresponds to `[Cnn]` bullet at position N in the `## All claims`
   section. The order MUST be preserved.

If any `[Cnn]` line is missing its `[[claims/{slug}]]` reverse-link, this is
a HARD FAIL — regenerate the section with proper links and re-validate.
This validation runs BEFORE writing the file to disk.
```

#### Variante alternativa (más robusta pero más cambios)

Cambiar Step 3 para que primero genere la lista de claims (Step 4) y DESPUÉS escriba el paper page rellenando `[[claims/{slug}]]` con los slugs ya conocidos. Implica reorden Step 3 ↔ Step 4. Más invasivo pero elimina la posibilidad estructural del bug.

**Recomendación**: empezar con la HARD FAIL validation. Si en re-ingests futuros el modelo sigue regresando, considerar el reorden.

#### Procedimiento de re-ingest después de aplicar Mejora 6

Para Bhandari y Bai (los 2 papers afectados):

```bash
cd ~/omegawiki

# 1. Backup git tag para volver atrás si algo falla
git tag pre-reingest-bhandari-bai

# 2. Reset selectivo del paper Bhandari
# Borrar paper page
rm wiki/papers/molecular-landmarks-tumor-hypoxia-across-cancer.md

# Borrar claims huérfanos generados solo por Bhandari (NO los de Bai)
rm wiki/claims/ancestry-disparity-tumor-hypoxia-brca.md
rm wiki/claims/hypoxia-cnas-occur-early-trunk-evolution.md
rm wiki/claims/hypoxia-pten-tert-three-way-telomere-interaction.md
rm wiki/claims/mir-133a-3p-tumor-suppressor-prostate-hypoxia.md
rm wiki/claims/mir-210-induced-under-hypoxia-pancancer.md
rm wiki/claims/myc-gain-co-occurs-hypoxia-pancancer.md
rm wiki/claims/nimbosus-aggressive-pca-phenotype.md

# Eliminar edges asociados (script o manual via tools/research_wiki.py)
# Aquí la skill /ingest los regenerará al re-ingestar

# 3. Re-ingest
claude
# /ingest raw/papers/Bhandari-2019.pdf

# 4. Verificar
python3 tools/lint.py --wiki-dir wiki/
# Esperado: 0 🔴, 0 🟡, ≤8 🔵 (los 8 huérfanos de Bai siguen pendientes)

# 5. Commit
git add wiki/
git commit -m "ingest(reingest): Bhandari 2019 with Mejora 6 — claims with proper reverse-links"

# 6. Repetir Pasos 2-5 para Bai
```

**Coste estimado**: 1 sesión Opus por paper. ~2 sesiones total.

**Riesgo**: si Mejora 6 no detecta el bug correctamente, segundo intento gasta 1 sesión adicional. Mitigación: probar Mejora 6 reingestando Lazarov (que ya está bien) primero, verificar que el output queda idéntico.

### Mejora 1 — Asignación Sonnet en steps mecánicos vía subagents

**Problema**: Todo el `/ingest` corre en Opus 4.7. Steps 5-7 son mecánicos.

**Cambio**: invocar subagents con `model: sonnet` para steps mecánicos.

| Step | Tarea | Modelo | Razón |
|---|---|---|---|
| 1 | Resolve source | Opus | Branching, INIT MODE detection |
| 2 | Paper identity, importance score | Opus | Juicio semántico |
| 3 | Paper page (con Mejora 6 enforcement) | Opus | Núcleo semántico |
| 4 | Concepts, claims, people | Opus | Dedup decisions |
| 5 | Paper-to-paper edges, citations | **Sonnet** | Matching, append-only |
| 6 | Topics y index | **Sonnet** | Matching, append |
| 7 | Log y rebuild | **Sonnet** | Ejecutar comandos |
| 8 | Report | Opus | Síntesis final |
| 9 | Optional discovery | Opus | Si se invoca |

**Ahorro estimado**: 40-50% cuota Opus por ingest.

**Aplicar DESPUÉS de Mejora 6**: porque Mejora 1 modifica la estructura de invocación de la skill, y queremos validar primero que Mejora 6 funciona en la skill estable.

### Mejora 2 — Pre-check de calidad antes de Step 3

**Problema**: Variabilidad en calidad por paper. Un ejemplo bueno reciente como referencia ayuda.

**Cambio**: pre-action al Step 3 que cargue `wiki/papers/Lazarov-2023.md` (TIER_1 más reciente bien construido) como reference quality target.

**Riesgo bajo**, beneficio incremental.

### Mejora 3 — `/check` skill (verificada — YA EXISTE)

`/check` está implementada y funcional. Cubre:
- Structural completeness (9 entity types)
- Field validation (enums, ranges, required fields)
- Cross-reference symmetry
- Graph edge consistency
- Content quality (LLM-assisted)

**Acción**: Ninguna — ya existe. Solo añadir como práctica recomendada correr `/check` cada 3 ingests.

### Mejora 4 — ~~Validator Python sin LLM~~ DESCARTADA

**Razón del descarte**: `tools/lint.py` (que `/check` invoca) ya implementa validation Python sin LLM. Construir un script paralelo es duplicación.

### Mejora 5 — Tier-ranking script Python

**Mantiene relevancia**. La frustración real "elegir paper" sigue ahí.

`scripts/tier_candidates.py`:
- Para cada PDF en `raw/papers/`: extrae metadata, query S2, computa keyword overlap con concepts/foundations existentes del wiki
- Output: ranking priorizado en markdown
- Coste: 0 cuota Claude
- Tiempo de construcción: 30-45 min

**Aplicar cuando**: después de Mejora 6 + reingest de Bhandari y Bai. Ningún apuro.

## 4. Lo que NO se va a tocar

- Steps 1-4 de la lógica core (excepto añadir validación HARD FAIL al final de Step 3 vía Mejora 6)
- Policy dedup
- Policy biomedical Step 4
- Sistema INIT MODE
- Layer Python (tools/)
- HARD FAIL validations existentes (Step 4.E)
- People tier suggestion (no auto-update)
- Worktree-safety en PYTHON_BIN lookup

## 5. Orden de ejecución revisado

| # | Tarea | Tiempo | Coste sesión | Dónde |
|---|---|---|---|---|
| **1** | **Implementar Mejora 6 (HARD FAIL claims links)** | 1 sesión | medio | Claude Code |
| **2** | **Probar Mejora 6 reingestando Lazarov (paper sano)** | 1 ingest | medio | Claude Code |
| **3** | **Reset selectivo Bhandari + reingest** | 1 sesión Opus | alto | Claude Code |
| **4** | **Reset selectivo Bai + reingest** | 1 sesión Opus | alto | Claude Code |
| **5** | Verificar `/check`: 0 🔴, 0 🟡, ≤5 🔵 | 5 min | bajo | Claude Code |
| 6 | Mejora 1 (subagents Sonnet en Steps 5-7) | 1 sesión | medio | Claude Code |
| 7 | Re-procesar 1 paper para validar Mejora 1 | 1 ingest | normal | Claude Code |
| 8 | Mejora 2 (pre-check calidad referencia) | 30 min | bajo | Claude Code |
| 9 | Construir `tier_candidates.py` | 30-45 min | 0 (sin LLM) | Claude Code |
| 10 | Procesar 5 papers nuevos con sistema mejorado | 5 ingests | alto | Claude Code |

**Tareas 1-5 son críticas** y deben hacerse antes que cualquier otra cosa. Bloquean al resto.

## 6. Métricas de éxito

### Para Mejora 6 (CRÍTICA)

- Después de Tarea 2 (reingest Lazarov): output idéntico al original (mismos claims, mismos edges, mismas personas). Diff `git diff wiki/papers/physiology-diseases-tissue-resident-macrophages.md` mínimo.
- Después de Tarea 3 (reingest Bhandari): paper page contiene `[[claims/X]]` en cada `[Cnn]` bullet de `## All claims`. `/check` no reporta orphans nuevos.
- Después de Tarea 4 (reingest Bai): igual.
- Después de Tarea 5 (verificación): `0 🔴, 0 🟡, 0 🔵 [orphan]` (puede haber otros 🔵 informacionales).

### Para Mejora 1 (cuando llegue)

- Cuota Opus por ingest: target -40% mínimo medido vs Tarea 7 baseline.
- Cross-paper edges, claims, tiempo wall-clock: ≥ que Tarea 7 baseline.
- Cero HARD FAIL nuevas.

## 7. Decisiones rechazadas

| Decisión rechazada | Por qué |
|---|---|
| Refactorizar `/ingest` en 7 sub-skills | La v1 está bien diseñada. Refactor habría roto INIT MODE, separación `/ingest` vs `/check`, y policy biomedical adaptada. |
| Reemplazar `tools/fetch_s2.py` por K-Dense `paper-lookup` | Coexisten sin problema. Mantener. |
| Auto-procesar 30 papers en batch | Cuota finita. Cross-paper edges requieren wiki ya construido. |
| Construir `validate_wiki.py` (Mejora 4) | Redundante con `/check` y `tools/lint.py` que ya existen. |
| Aplicar `fix_orphan_claims.py` automático | Heurística keyword overlap insuficiente. 2/3 falsos positivos en validación manual. |
| Opción C (reset wiki completo y reingestar 6 papers) | 4 papers están bien. Tirarlos sería desperdicio (~20-25h Opus). |
| Opción D (dejar 15 huérfanos como debt) | A 2 meses de tesis, ruido en grafo es inaceptable. |

## 8. Notas para sesiones futuras

- Cuando regreses a este audit, lee primero la skill `/ingest` actual. Si ha cambiado, este documento puede estar desactualizado.
- Si ves que tu yo-anterior decidió no refactorizar y ahora te tienta refactorizar, vuelve a leer Sección 2 antes de proceder.
- Mejora 6 es CRÍTICA y bloquea casi todo. No saltársela.
- **Práctica recomendada nueva**: correr `/check` cada 3 ingests (`python3 tools/lint.py --wiki-dir wiki/`). Si aparecen 🟡 o 🔵 nuevos no triviales, debug ANTES de seguir procesando.

## 9. Sesión de saneamiento 2026-05-21 — bugs de formato y linter

Sesión dedicada tras detectar 24 falsos positivos `xref-asymmetry` durante el
ingest del paper Cancer organoids. El diagnóstico destapó una cadena de bugs
de formato y de linter. Todos resueltos o documentados aquí.

### 9.1 Bug raíz — `source_papers` en 3 formatos incompatibles

`/ingest` producía el campo `source_papers` de los claims en tres formatos
distintos según el ingest:

| Origen | Formato | Estado |
|---|---|---|
| Claims históricos (pre-13 mayo) | lista YAML multilínea, slug pelado | CANÓNICO |
| Claims paper SVG (#2) | lista YAML multilínea, wikilink `[[papers/slug]]` | desviación |
| Claims paper Cancer organoids (#4) | inline `[slug]` | desviación |

Causa: `cross-references.md` L15 documentaba el formato como `[[paper-P]]`,
contradiciendo el template canónico (`runtime-page-templates`: lista de slugs
pelados). La doc de la skill dio permiso para improvisar.

Fix aplicado (commit 5d0c3e1):
- `cross-references.md` L15 (`source_papers`) y L16 (`key_papers`) reescritas:
  lista YAML de slugs pelados, nunca wikilinks ni corchetes inline.
- 31 claims normalizados al formato canónico (7 SVG + 24 organoids).
- Verificado con el ingest del paper Luo (#8): los 20 claims nuevos salieron
  ya en formato canónico. La fuente está cortada.

### 9.2 Bug del linter — check `xref-asymmetry` de claims

`tools/lint.py`, funcion `check_xref_asymmetry`. Dos defectos:

1. Prefijo: el check buscaba el reverse-link como `[[{slug}]]` pelado, pero
   `/ingest` escribe los reverse-links con prefijo `[[claims/{slug}]]`.
   → 24 falsos positivos. Fix: L340 acepta `[[claims/{slug}]]` (commit f62f641).
2. Regex: `source_papers:\s*\[(.*?)\]` solo parseaba listas inline; no
   reconocia el formato canonico YAML multilinea. El check estaba INERTE para
   el formato correcto. Fix: regex reemplazado para ambos formatos (5d0c3e1).

Al activarse el check por primera vez sobre el formato canonico, quedaron
expuestos 3 fallos reales preexistentes (ver 9.3).

### 9.3 Deuda preexistente destapada — 3 claims multi-fuente

3 claims con `source_papers` de 2 papers tenian el reverse-link solo en el
paper primario, no en el secundario (corroborante). NO era `source_papers` mal
asignado — multi-paper es legitimo (schema lo define como lista; 12 claims del
wiki lo usan, 9 ya correctos).

Fix aplicado (commit 0ad4869): anadido `[[claims/{slug}]]` en `## Related` de
los 3 papers secundarios:
- cross-tissue-single-cell-landscape-human -> mmac1-signature-enriched-momac-verse-il4i1-il1b-isg
- nf-kb-tet2-promote-macrophage-reprogramming -> trem2-macrophages-associate-poor-cancer-prognosis
- tissue-resident-macrophages-provide-pro-tumorigenic -> trem2-tam-pancancer-accumulation-momac-verse

### 9.4 Otros bugs menores observados

- Enums fuera de esquema (Mejora 7 — intermitente): `/ingest` ocasionalmente
  emite status/maturity fuera de los valores validos. Opus suele autocorregirse
  tras varios fixes en una misma sesion. No resuelto de raiz.
- Wikilink huerfano: en el paper SVG, `/ingest` escribio `[[claims/X]]` en una
  foundation sin crear `claims/X.md`. Corregido a mano (commit 66ddf3b).
- Loop de preprocessing: con el PDF de Cancer organoids (8.3 MB),
  `prepare_paper_source.py` se reejecuto ~10 veces antes de arrancar. Se
  resolvio solo. PDFs grandes pueden disparar reintentos espurios.

### 9.5 DEUDA PENDIENTE — no resuelta en esta sesión

- Checks `xref-asymmetry` 313/325/355 (concepts/people/ideas): tienen el mismo
  bug de prefijo que el de claims, Y el regex sin soporte multilinea. Solo se
  parcheo el check de claims (L340/L332). Tarea dedicada pendiente: normalizar
  los 4 checks de forma consistente.
- Campo `evidence` de los claims: no auditado. Verificar que `/ingest` lo
  produce consistente.
- `cross-references.md` L11: describe el edge concept-paper de forma vaga.
  Conviene alinear con L15/L16 en una pasada futura.

### 9.6 Lección

`/ingest` (LLM-driven) produce variaciones de formato que solo se detectan
cuando un linter las compara. Pero el linter mismo puede estar desalineado con
el formato real — un check que no salta NO significa que todo este bien; puede
estar inerte. Verificar siempre que el linter realmente evalua lo que dice.
La causa raiz casi siempre esta en la documentacion de la skill, no en el
modelo: alinear `cross-references.md` con los templates canonicos corta la
fuente.
