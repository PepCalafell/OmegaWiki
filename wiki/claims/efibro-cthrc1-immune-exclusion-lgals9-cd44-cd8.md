---
title: "eFibro_CTHRC1 mediates CD8+ T cell exclusion via LGALS9–CD44 and LGALS9–CD45 interactions"
slug: efibro-cthrc1-immune-exclusion-lgals9-cd44-cd8
status: supported
confidence: 0.8
tags:
  - caf
  - cthrc1
  - immune-exclusion
  - lgals9
  - cd44
  - cd45
  - cd8-t-cell
  - havcr2
  - tme
domain: cancer immunology
source_papers:
  - spatiotemporal-analyses-pan-cancer-single-cell
evidence:
  - source: spatiotemporal-analyses-pan-cancer-single-cell
    type: supports
    strength: strong
    detail: CellChat infers LGALS9-CD44/CD45/HAVCR2 as top CTHRC1+ CAF → CD8+ T cell interactions (Fig. 4g,h); ST and TCGA both show negative correlation between eFibro_CTHRC1 score and CD8+ T infiltration across nearly all cancer types.
conditions: "Pan-cancer scRNA-seq + ST + TCGA; correlative + receptor-ligand inference, not direct knockout."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

eFibro_CTHRC1 cells exclude CD8+ T cells from the tumor core through both physical-matrix barrier and signaling interactions: CellChat identifies LGALS9–CD44 and LGALS9–CD45 as preferential ligand-receptor pairs between CTHRC1+ CAFs and CD8+ T cells; TCGA CD8+ T infiltration is anti-correlated with eFibro_CTHRC1 signature in nearly all cancer types.

## Conditions and scope

Direct quote: "eFibro_CTHRC1 fibroblasts were more likely to interact with CD8+ T cells via LGALS9–CD44 and LGALS9–CD45 interactions... the estimated infiltration of CD8+ T cells was notably higher in tumor samples with a lower eFibro_CTHRC1 signature score in the TCGA cohort in almost all cancer types" (Han 2025, p.9-10).

## Linked ideas

- Anti-Gal-9 therapy as anti-stromal-immune-exclusion combination with ICB.
