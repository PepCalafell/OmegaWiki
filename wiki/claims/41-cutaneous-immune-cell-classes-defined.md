---
title: "Iterative subclustering of CD45+ cells defined 41 cutaneous immune cell classes"
slug: 41-cutaneous-immune-cell-classes-defined
status: supported
confidence: 0.85
tags: [skin, scrna-seq, clustering, cell-types, immunology]
domain: immunology / single-cell
source_papers:
  - classification-human-chronic-inflammatory-skin-disease
evidence:
  - source: classification-human-chronic-inflammatory-skin-disease
    type: supports
    strength: strong
    detail: "Quote (p.2): 'Including the previously described mast cell cluster, this classification generated 41 final clusters.' Built from 21 CD3+/KLRB1+ lymphoid + 19 HLA-DR+ myeloid clusters + 1 mast cluster."
conditions: "Seurat Louvain clustering at resolution 0.4 (clustree-guided), then high-resolution subclustering of lymphoid and myeloid compartments."
date_proposed: 2026-06-10
date_updated: 2026-06-10
---

## Statement

Through iterative subclustering of the CD3+/KLRB1+ lymphoid and HLA-DRA+ myeloid compartments, the authors defined 41 high-resolution cutaneous immune cell classes (e.g. Trm1-3, eTreg1/2, cmTreg, CTLac, CTLex, ILC2, NK, Mac1-4, LC1-3, moDC1-3, DC1-3, Mono/InfMono, B, plasma, mast, and cycling counterparts).

## Evidence summary

Reported in Results of [[papers/classification-human-chronic-inflammatory-skin-disease]]. Methods used [[foundations/louvain-community-detection-clustering]], [[foundations/clustree-clustering-resolution-selection]], [[foundations/harmony-integration]], [[foundations/seurat-v3-integration]], and [[foundations/scdblfinder-doublet-detection]]; relates to [[concepts/treg-trm-expansion-cd8-exhaustion-chronic]].

## Conditions and scope

High cluster granularity was a deliberate choice to maximize discovery of cell-type-restricted abnormalities.

## Counter-evidence

None; methodological/descriptive claim, though cluster count depends on resolution choices.

## Linked ideas

## Open questions

- How stable are the 41 classes under alternative integration/clustering pipelines?
