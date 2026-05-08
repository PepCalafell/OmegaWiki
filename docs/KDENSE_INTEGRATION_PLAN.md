---
title: KDENSE_INTEGRATION_PLAN
date: 2026-05-09
author: Pep Calafell-Segura
status: planning
related: docs/INGEST_AUDIT.md
external_repo: https://github.com/K-Dense-AI/scientific-agent-skills
external_version: v2.38.0 (1 mayo 2026)
---

# Plan de integración K-Dense Scientific Agent Skills

## 1. Contexto y decisión

Sesión 9 mayo 2026. Evaluación de K-Dense-AI/scientific-agent-skills (135 skills científicas, 20.4k stars, MIT license).

**Decisión arquitectónica**: estructura híbrida con vendoring de subset curado.

- Skills propias del proyecto (`/ingest`, `/check`, `/discover`, futuras): `~/omegawiki/.claude/skills/`
- Subset K-Dense vendored: `~/omegawiki/vendor/kdense-skills/` (en repo, NO en `.claude/skills/`)
- Symlink/sync activado por máquina vía script: `scripts/sync_kdense_skills.sh`

**Justificación**:

- K-Dense advierte explícitamente "no instalar todo, revisar cada SKILL.md, comunidad puede no estar revisada a fondo". Selección curada es la práctica recomendada por el propio autor.
- 135 skills × ~100 tokens metadata = ~13.500 tokens al inicio de cada sesión. Subset reduce a ~1.500-2.000 tokens.
- 76 releases en pocos meses. Vendoring permite version pinning y auditoría limpia de cada update.
- Patrón A (todo en repo) cumple requisito de sincronización Git entre IJC y casa.
- Sub-carpeta `vendor/` separa código tercero del propio sin mezclarlo en `.claude/skills/`.

## 2. Estructura propuesta

```
~/omegawiki/
├── .claude/
│   └── skills/                        ← skills propias (Patrón A)
│       ├── ingest/
│       ├── check/
│       ├── discover/
│       ├── tier-candidates/           ← futura
│       └── validate-wiki/             ← futura
├── vendor/                            ← código tercero, en repo pero no auto-cargado
│   └── kdense-skills/
│       ├── README.md                  ← este plan, copia abreviada
│       ├── VERSION                    ← v2.38.0
│       ├── INSTALL_LOG.md             ← bitácora de qué subset y cuándo
│       └── skills/
│           ├── paper-lookup/
│           ├── database-lookup/
│           ├── bgpt-paper-search/
│           └── ...                    ← subset curado
├── scripts/
│   ├── sync_kdense_skills.sh          ← copia/symlink vendor → ~/.claude/skills/kdense/
│   └── update_kdense_skills.sh        ← bump version, re-vendor subset
├── docs/
├── wiki/
└── tools/
```

## 3. Subset curado por iteración

### Iteración 1 — Core research workflow (3 skills)

Mínimo viable para validar integración. Si funciona, expandir.

| Skill | Función | Reemplaza/complementa | Prioridad |
|---|---|---|---|
| `paper-lookup` | 10 DBs académicas (PubMed, PMC, bioRxiv, medRxiv, arXiv, OpenAlex, Crossref, Semantic Scholar, CORE, Unpaywall) | Complementa `tools/fetch_s2.py` (más cobertura) | 🔥 |
| `database-lookup` | 78 DBs (PubChem, ChEMBL, UniProt, COSMIC, ClinVar, GEO, ClinicalTrials.gov, FDA...) | Nueva capacidad. Útil para enriquecer foundations biomédicas | 🔥 |
| `bgpt-paper-search` | 25+ campos estructurados desde full text (methods, results, sample sizes, quality scores) | Mejora `/discover`. Permite filtros más finos que solo abstract | 🔥 |

**Validación de Iteración 1**: una vez instaladas, ejecutar `/discover` con un anchor (ej. arxiv-id de Bai 2022) y comparar shortlist contra la actual. Si es ≥ y los nuevos resultados son relevantes para tu wiki, aceptar.

### Iteración 2 — Bioinformatic workflow (4 skills)

Para análisis directo (no para wiki). Útiles cuando trabajes en HypoxiaVERSE o atlas piel.

| Skill | Función | Cuándo usar |
|---|---|---|
| `scanpy` | scRNA-seq best practices, workflow recipes | HypoxiaVERSE, atlas piel |
| `scvelo` | RNA velocity | HypoxiaVERSE (si aplicable) |
| `scvi-tools` | Probabilistic models for scRNA-seq (ya usas scVI retrained) | HypoxiaVERSE |
| `cellxgene-census` | CZ CELLxGENE reference data | Comparar HypoxiaVERSE contra reference |

**Validación de Iteración 2**: pedir al modelo que diseñe un workflow scRNA-seq estándar para Bai 2022 dataset (si público). Comparar con tu workflow actual. Si añade insights, aceptar.

### Iteración 3 — Writing phase (4 skills)

Para junio en adelante (writing tesis).

| Skill | Función |
|---|---|
| `literature-review` | Systematic review structuring |
| `scientific-writing` | IMRAD, citations APA/AMA/Vancouver, reporting guidelines (CONSORT/STROBE/PRISMA) |
| `peer-review` | Self-review estructurado |
| `citation-management` | BibTeX, dedup, validación |

**Validación de Iteración 3**: usar `scientific-writing` para draftear el outline de un capítulo de tesis y comparar contra tu redacción libre. Si la estructura producida es mejor, aceptar.

### Iteración 4 — Soporte (3 skills)

Quality of life.

| Skill | Función |
|---|---|
| `markdown-mermaid-writing` | Diagramas text-based para wiki y tesis |
| `document-skills` | PDF/DOCX/PPTX export (para entregables) |
| `scholar-evaluation` | Tier-ranking de autores (hIndex, citation count) — útil para Step 4 de `/ingest` |

**Validación de Iteración 4**: usar `markdown-mermaid-writing` para regenerar el diagrama de sincronización del status doc. Si funciona limpio, aceptar.

### Iteración 5 — Open Notebook (separada porque no es trivial)

| Skill | Función | Reemplaza |
|---|---|---|
| `open-notebook` | Self-hosted NotebookLM (PDFs, videos, audio, web; 16+ providers; multi-speaker podcast) | NotebookLM (Google) |

**Caveat**: Open Notebook necesita despliegue (Docker, Postgres, etc.). NO es plug-and-play. Evaluar después de Iteración 1-4 cuando el ecosistema esté estable. Hasta entonces, NotebookLM (Google) sigue siendo la opción para writing phase tesis (R2 del usuario).

## 4. Skills K-Dense que NO instalar

De las 135, descartadas explícitamente:

- Quantum computing (Cirq, PennyLane, Qiskit, QuTiP) — fuera de dominio
- Astronomía (Astropy, Pymatgen) — fuera de dominio
- Geospatial (GeoPandas, GeoMaster) — fuera de dominio
- Cheminformatics (RDKit, Datamol, DeepChem, DiffDock, MDAnalysis, OpenMM) — fuera de dominio biomedical específico (no haces drug discovery directo)
- Lab automation (Opentrons, PyLabRobot, Benchling) — fuera de dominio
- Reinforcement learning (Stable Baselines3, PufferLib) — fuera de dominio
- Engineering (FluidSim, MATLAB) — fuera de dominio
- Materials science — fuera de dominio
- Physics — fuera de dominio
- Skills "K-Dense Web" exclusive (mencionadas pero no en repo) — no aplican

**Total descartado**: ~110 skills. Total integrado al cabo de 5 iteraciones: ~15 skills (11% del total).

## 5. Procedimiento de vendoring

### Setup inicial (una vez)

```bash
cd ~/omegawiki
mkdir -p vendor/kdense-skills/skills

# Clonar K-Dense temporalmente fuera del repo
git clone --depth 1 --branch v2.38.0 \
  https://github.com/K-Dense-AI/scientific-agent-skills.git \
  /tmp/kdense

# Copiar SOLO el subset de Iteración 1
for skill in paper-lookup database-lookup bgpt-paper-search; do
  cp -r /tmp/kdense/scientific-skills/$skill vendor/kdense-skills/skills/
done

# Documentar versión y fecha
echo "v2.38.0" > vendor/kdense-skills/VERSION
echo "## $(date -I) — Iteración 1" >> vendor/kdense-skills/INSTALL_LOG.md
echo "Added: paper-lookup, database-lookup, bgpt-paper-search" >> vendor/kdense-skills/INSTALL_LOG.md

# Limpiar clone temporal
rm -rf /tmp/kdense

# Commit
git add vendor/
git commit -m "vendor: add K-Dense Iteración 1 (paper-lookup, database-lookup, bgpt-paper-search) @ v2.38.0"
git push origin main
```

### Activación por máquina

`scripts/sync_kdense_skills.sh`:

```bash
#!/bin/bash
# Symlinks vendored K-Dense skills into ~/.claude/skills/ for Claude Code to discover
# Run once after each `git pull` that touches vendor/

set -euo pipefail

REPO_ROOT=$(git rev-parse --show-toplevel)
SOURCE_DIR="$REPO_ROOT/vendor/kdense-skills/skills"
TARGET_DIR="$HOME/.claude/skills"

mkdir -p "$TARGET_DIR"

for skill_dir in "$SOURCE_DIR"/*/; do
  skill_name=$(basename "$skill_dir")
  target_link="$TARGET_DIR/kdense-$skill_name"
  
  # Remove old symlink if exists
  [ -L "$target_link" ] && rm "$target_link"
  
  # Create new symlink with kdense- prefix to namespace
  ln -s "$skill_dir" "$target_link"
  echo "Linked: $skill_name -> $target_link"
done

echo ""
echo "Done. Restart Claude Code to load new skills."
```

**Nota sobre prefijo `kdense-`**: namespacing evita colisiones si tú creas una skill con el mismo nombre. Por ejemplo, K-Dense tiene `paper-lookup`, tú podrías querer una `paper-lookup` propia más adelante.

### Update workflow

Cuando K-Dense saque nuevas versiones:

```bash
cd ~/omegawiki
./scripts/update_kdense_skills.sh v2.39.0
git diff vendor/  # revisar qué cambió
git add vendor/
git commit -m "vendor: bump K-Dense to v2.39.0"
git push origin main
```

`scripts/update_kdense_skills.sh` (a construir cuando lleguemos al primer update):
- Clone target version
- Re-copy solo los skills actualmente en `vendor/kdense-skills/skills/`
- Mantener subset, no auto-añadir nuevos
- Update VERSION y INSTALL_LOG.md

### Sincronización entre máquinas

```bash
# IJC o casa WSL
cd ~/omegawiki
git pull origin main
./scripts/sync_kdense_skills.sh
# Restart Claude Code
```

## 6. Caveats y riesgos identificados

### Riesgo 1 — Skills K-Dense ejecutan código

K-Dense advierte explícitamente que skills pueden correr código arbitrario, instalar paquetes, hacer requests. **Mitigación**:
- Leer SKILL.md de cada skill antes de vendor
- Considerar correr Cisco AI Skill Scanner antes de aceptar:
  ```
  uv pip install cisco-ai-skill-scanner
  skill-scanner scan vendor/kdense-skills/skills/paper-lookup --use-behavioral
  ```
- Solo skills authored by `K-Dense-AI` (no community contributions) en Iteración 1-2 hasta confianza establecida

### Riesgo 2 — Solapamiento con tooling existente

`paper-lookup` y `tools/fetch_s2.py` cubren parcialmente lo mismo. **Decisión**: NO eliminar `fetch_s2.py`. Mantener ambos:
- `tools/fetch_s2.py` para `/ingest` (skill maduro, integrado, testeado con 6 papers)
- `paper-lookup` para `/discover` y exploración manual (mayor cobertura DBs)

Si en 2-3 meses `paper-lookup` demuestra ser superior, considerar migración planificada.

### Riesgo 3 — Tokens de metadata en sesiones largas

Cada skill K-Dense añade ~100 tokens de descriptor cargado al inicio. 15 skills = 1.500 tokens. Aceptable. Si alguna iteración futura sube por encima de 25 skills totales (~2.500 tokens), reconsiderar.

### Riesgo 4 — Versión K-Dense rompe compatibilidad

Mitigación: pinned a v2.38.0 en `vendor/kdense-skills/VERSION`. Updates manuales con review.

### Riesgo 5 — Integración con `/discover` requiere modificar la skill propia

La skill `/discover` actual usa `tools/discover.py`. Para que use K-Dense `paper-lookup` y `bgpt-paper-search`, hay que editar `/discover` SKILL.md. Esto es trabajo adicional, NO automático.

**Cuándo hacerlo**: después de Iteración 1 instalada y validada. Antes de Iteración 2.

## 7. Métricas de éxito

Antes de aceptar cada iteración:

- **Iteración 1**: `/discover` con anchor de Bai 2022 produce shortlist con ≥ 50% de papers relevantes para hipoxia/macrófagos según juicio del usuario. Ningún resultado obviamente irrelevante (papers de campos completamente distintos).
- **Iteración 2**: skills bioinformatic permiten al modelo dar workflow recipes correctas para datasets scRNA-seq sin pedirle pasos manuales.
- **Iteración 3**: `scientific-writing` produce outline de capítulo tesis con estructura IMRAD válida y citas correctamente formateadas en el estilo elegido.
- **Iteración 4**: `markdown-mermaid-writing` regenera diagramas existentes sin errores de sintaxis.
- **Iteración 5**: Open Notebook deployable en local sin romper el setup actual de OmegaWiki.

Si una iteración no pasa su métrica, no avanzar a la siguiente sin debug.

## 8. Calendario propuesto

Asumiendo ritmo 1 paper/día y wiki target ~40 papers junio:

| Semana | Iteración | Tareas |
|---|---|---|
| 11-17 mayo | Iteración 1 | Vendoring inicial, validar `/discover` mejorado |
| 18-24 mayo | Iteración 2 | Skills bioinformatic, validar en HypoxiaVERSE |
| 25-31 mayo | Iteración 4 | Soporte (Mermaid, document-skills, scholar-evaluation) |
| 1-7 junio | Iteración 3 | Writing phase prep |
| 8-14 junio | Pausa K-Dense | Empezar tesis chapter 1 con wiki |
| Junio | Iteración 5 (si necesaria) | Open Notebook self-hosted |

Iteración 3 antes de Iteración 4 sería válido también; orden ajustable según necesidad real.

## 9. Decisiones rechazadas (sesión 9 mayo)

| Decisión rechazada | Por qué |
|---|---|
| Instalar las 135 skills K-Dense | Aviso explícito del autor del repo. 13.5k tokens metadata. Auditoría imposible. |
| Patrón B puro (K-Dense fuera del repo, vía `gh skill install`) | Rompe sincronización Git entre IJC y casa. Patrón A híbrido lo resuelve. |
| Mezclar K-Dense en `~/omegawiki/.claude/skills/` directamente | Contamina el namespace de skills propias. Hace updates ruidosos. |
| Reemplazar `tools/fetch_s2.py` por K-Dense `paper-lookup` | Ingest v1 funciona. Riesgo innecesario. Coexistir es seguro. |
