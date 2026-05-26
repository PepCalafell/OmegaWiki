# Runtime Page Templates

> On-demand reference for full wiki page templates only. See `docs/runtime-support-files.en.md` for graph-derived files plus `index.md` and `log.md`.

## 9 Page Types

### papers/{slug}.md

```yaml
---
# === Identification ===
title: ""
slug: ""
arxiv: ""
doi: ""                  # NEW: critical for biomedical papers without arXiv
pmid: ""                 # NEW: PubMed ID
venue: ""
year:
authors: []              # NEW: ordered list of authors
first_author: ""         # NEW: for citation_key generation
corresponding_author: "" # NEW

# === Source & metadata ===
source_type: tex         # tex | pdf
s2_id: ""
date_added: YYYY-MM-DD
ingested_date: YYYY-MM-DD  # NEW: same as date_added for now
ingest_version: 1        # NEW: increment on reprocess with improved skill
last_reviewed:           # NEW: null until manually reviewed

# === Classification ===
importance: 3            # 1-5
tier: TIER_3             # NEW: TIER_1 | TIER_2 | TIER_3 (deep | medium | shallow)
tags: []
keywords: []
domain: ""               # immunology / epigenetics / genomics / cell biology / methods / oncology

# === Biomedical domain (fill if applicable, else leave empty list/null) ===
tissue: []               # kidney | lung | skin | colon | stomach | liver | pancreas | bladder | ovary | bone_marrow | blood | multi | in_vitro_only
condition: []            # healthy | cancer | inflam_precancer | autoimmune
disease_specific: []     # lupus_nephritis | MASH | IgA_nephropathy | etc.
species: []              # human | mouse | both
hypoxia_relevant: false
contains_immune_cells: false
contains_myeloid: false

# === Technique ===
techniques: []           # scRNA-seq_10x | snRNA-seq | CITE-seq | spatial_visium | EPIC_array | RRBS | ChIP-seq | bulk_RNA-seq | flow_cytometry | etc.
n_samples:
n_cells_total:
integration_method: ""   # Harmony | scVI | BBKNN | Seurat_CCA | null

# === Biology captured (extracted from paper) ===
key_cell_types: []
key_markers: []
key_pathways: []

# === User project membership (multi-valued) ===
projects: []             # hypoxia | skin | thesis | methods
priority: reference      # core | context | reference
read_status: not_read    # not_read | skimmed | read | deep_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:     # candidate | included | excluded | null
exclusion_reason:        # null
data_availability: ""    # GSE id, dbGaP, EGA, etc.

# === Cross-references ===
code_url: ""
cited_by: []
---
```

Body sections (in order): `## Problem` / `## Key idea` / `## Method` / `## Results` / `## All claims (exhaustive)` / `## Discussion captured` / `## Limitations` / `## Open questions` / `## My take` / `## Related`

The `## All claims (exhaustive)` section lists 15-30 atomic claims for TIER_1 papers (5-10 for TIER_2, 3-5 for TIER_3). Each claim entry has the form:
- `[claim_id]` short-text-summary `(p.X)` "exact quote from paper" — confidence: high|medium|low — type: mechanistic|correlational|methodological|pharmacological|quantitative — links: [[concepts/...]] [[claims/...]]

The `## Discussion captured` section has the following subsections, faithful to what the AUTHORS themselves write (not your interpretation):
- `### Authors' interpretation` — how authors interpret their own findings, mechanisms they propose
- `### Comparisons with prior literature (made by authors)` — which papers they cite in the discussion and for what; include DOI/PMID when in text
- `### Mechanistic hypotheses proposed` — explicit hypotheses with quote and page
- `### Caveats and self-criticism` — limitations the authors acknowledge themselves (interpretive, distinct from methodological limitations in `## Limitations`)
- `### Future directions suggested` — directions the authors propose

The `## Open questions` section is split into two subsections:
- `### Open questions raised by authors` — verbatim or paraphrased from the paper
- `### Open questions identified during ingest` — system/user-identified gaps

### concepts/{concept-name}.md

```yaml
---
title: ""
aliases: []
tags: []
maturity: active         # OBLIGATORIO exactamente uno de: stable|active|emerging|deprecated — NINGÚN otro valor
key_papers:              # YAML list, one bare slug per line — never [[wikilinks]], never inline [brackets]
  - paper-slug-here
first_introduced: ""
date_updated: YYYY-MM-DD
related_concepts: []
---
```

Body sections: `## Definition` / `## Intuition` / `## Formal notation` / `## Variants` / `## Comparison` / `## When to use` / `## Known limitations` / `## Open problems` / `## Key papers` / `## My understanding`

### topics/{topic-name}.md

```yaml
---
title: ""
tags: []
my_involvement: none     # none | reading | side-project | main-focus
sota_updated: YYYY-MM-DD
key_venues: []
related_topics: []
key_people: []
---
```

Body sections: `## Overview` / `## Timeline` / `## Seminal works` / `## SOTA tracker` / `## Open problems` / `## My position` / `## Research gaps` / `## Key people`

### people/{firstname-lastname}.md

```yaml
---
name: ""
affiliation: ""
role:                    # pi | individual | both — academic structural role
group: ""                # lab name (e.g., "Ballestar Lab")
institution: ""          # institution name (e.g., "IJC, Badalona")
papers_in_vault: 1       # auto-incremented on each ingest mentioning this person
relevance_tier: emerging # emerging (1-3 papers) | established (4-9) | core (10+)
                         # auto-promotion thresholds: papers_in_vault ≥ 4 → established;
                         # papers_in_vault ≥ 10 → core. The /ingest skill notifies the
                         # user when a person crosses a threshold; promotion is recorded
                         # by updating this field, NOT by moving the file (file lives
                         # always at wiki/people/{slug}.md regardless of tier).
manual_override:         # optional: if the user wants to assign a tier higher than
                         # papers_in_vault would justify (e.g., the user's own profile,
                         # the thesis supervisor), set to "user_decision_<YYYY-MM-DD>_<reason>"
                         # and the auto-promotion logic will respect this override.
tags: []
homepage: ""
scholar: ""
date_updated: YYYY-MM-DD
---
```

Body sections: `## Research areas` / `## Key papers in vault` / `## Recent work` / `## Collaborators within vault` / `## My notes`

`## Key papers in vault` lists papers from this vault that this person co-authored, in citation_key form `[[papers/<slug>]]`. The list grows with each ingest mentioning this person.

`## Collaborators within vault` lists other people pages from this vault that share authorship with this person on at least one paper.

### Summary/{area-name}.md

```yaml
---
title: ""
scope: ""
key_topics: []
paper_count:
date_updated: YYYY-MM-DD
---
```

Body sections: `## Overview` / `## Core areas` / `## Evolution` / `## Current frontiers` / `## Key references` / `## Related`

### foundations/{slug}.md

```yaml
---
# CAMPOS DE FOUNDATION: EXACTAMENTE estos 8, ninguno más.
# NUNCA añadir 'type', 'category' ni otros campos inventados.
title: ""
slug: ""
domain: ""               # OBLIGATORIO — no dejar vacío
status: mainstream       # OBLIGATORIO exactamente uno de: mainstream|historical — NINGÚN otro valor
aliases: []
first_introduced: ""
date_updated: YYYY-MM-DD
source_url: ""
---
```

Body sections: `## Definition` / `## Intuition` / `## Formal notation` / `## Key variants` / `## Known limitations` / `## Open problems` / `## Relevance to active research`

Foundations have **no outward link fields**. Other pages may link to a foundation; foundations write no reverse link.

### ideas/{idea-slug}.md

```yaml
---
title: ""
slug: ""
status: proposed          # proposed | in_progress | tested | validated | failed
origin: ""
origin_gaps: []
tags: []
domain: ""
priority: 3               # 1-5
pilot_result: ""
failure_reason: ""
linked_experiments: []
date_proposed: YYYY-MM-DD
date_resolved: ""
---
```

Body sections: `## Motivation` / `## Hypothesis` / `## Approach sketch` / `## Expected outcome` / `## Risks` / `## Pilot results` / `## Lessons learned`

### experiments/{experiment-slug}.md

```yaml
---
title: ""
slug: ""
status: planned           # planned | running | completed | abandoned
target_claim: ""
hypothesis: ""
tags: []
domain: ""
setup:
  model: ""
  dataset: ""
  hardware: ""
  framework: ""
metrics: []
baseline: ""
outcome: ""               # succeeded | failed | inconclusive
key_result: ""
linked_idea: ""
date_planned: YYYY-MM-DD
date_completed: ""
run_log: ""
started: ""
estimated_hours: 0
remote:
  server: ""
  gpu: ""
  session: ""
  started: ""
  completed: ""
---
```

Body sections: `## Objective` / `## Setup` / `## Procedure` / `## Results` / `## Analysis` / `## Claim updates` / `## Follow-up`

### claims/{claim-slug}.md

```yaml
---
title: ""
slug: ""
status: proposed          # proposed | weakly_supported | supported | challenged | deprecated
confidence: 0.5           # 0.0-1.0
tags: []
domain: ""
source_papers:           # YAML list, one bare slug per line — never [[wikilinks]], never inline [brackets]
  - paper-slug-here
evidence:
  - source: ""
    type: supports        # supports | contradicts | tested_by | invalidates
    strength: moderate    # weak | moderate | strong
    detail: ""
conditions: ""
date_proposed: YYYY-MM-DD
date_updated: YYYY-MM-DD
---
```

Body sections: `## Statement` / `## Evidence summary` / `## Conditions and scope` / `## Counter-evidence` / `## Linked ideas` / `## Open questions`
