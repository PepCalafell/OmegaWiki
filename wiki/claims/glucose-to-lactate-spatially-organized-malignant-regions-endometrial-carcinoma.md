---
title: "Glucose→lactate conversion is spatially organized in endometrial carcinoma tissue (Moran's I ≈ 0.379) with highest activity in malignant-cell regions"
slug: glucose-to-lactate-spatially-organized-malignant-regions-endometrial-carcinoma
status: supported
confidence: 0.7
tags:
  - endometrial-carcinoma
  - glycolysis
  - warburg
  - spatial-transcriptomics
  - morans-i
domain: "oncology / cancer-metabolism"
source_papers:
  - atlas-scale-metabolic-activities-inferred-single
evidence:
  - source: atlas-scale-metabolic-activities-inferred-single
    type: supports
    strength: strong
    detail: "Fig 7c: Moran's I = 0.379 for glucose→lactate task scCellFie scores across all EEC Visium spots, ranking it among spatially-organized tasks. Supp Fig 8a: malignant-cell regions show significantly higher activity than non-malignant surrounding tissue. Recapitulates the Warburg effect ([[warburg-effect-hif1a-glycolytic-reprogramming]])."
conditions: "Single EEC Visium dataset; recapitulates a generic pan-cancer phenomenon — interest is in tissue-architecture quantification, not in novelty of glycolytic reprogramming itself."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

In an endometrial-carcinoma Visium dataset, the glucose→lactate metabolic task shows significant spatial autocorrelation (Moran's I ≈ 0.379), with significantly elevated activity in malignant-cell regions versus non-malignant surrounding tissue, recapitulating the Warburg effect at spatial resolution and demonstrating scCellFie's ability to quantify tissue-architecture-aware metabolic patterns.

## Evidence summary

Moran's I autocorrelation over scCellFie scores for the glucose-to-lactate task ranks it among the most spatially organized of all 218 tasks (Fig 7c; Supp Fig 7 lists all spatially organized tasks). Per-region analysis (Supp Fig 8a) shows higher activity in malignant-cell regions, consistent with the Warburg effect. Non-malignant tissue retains baseline lactate production, consistent with healthy-endometrium epithelial glycolysis (Fig 5).

## Conditions and scope

Single EEC Visium dataset (Barkley et al. 2022); not a discovery claim about EEC biology — the contribution is methodological (spatial quantification + integration with malignancy annotation).

## Counter-evidence

None reported; the pattern matches well-established cancer-metabolism literature.

## Linked ideas

None yet.

## Open questions

- How does the Moran's I distribution of metabolic-task spatial organization compare across tumour types (TNBC, PDAC, EEC)?
- Can spatial co-organization of glycolysis and OXPHOS tasks be used to subtype tumour-metabolic niches?
