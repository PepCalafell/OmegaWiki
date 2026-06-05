---
title: "Bladder cancer TME contains four macrophage subpopulations: Macro-CCL4, -CXCL9, -FOLR2, -SPP1"
slug: bladder-cancer-tme-contains-four-macrophage
status: supported
confidence: 0.75
tags: [macrophage, scRNA-seq, bladder-cancer, TME, cell-states]
domain: oncology / immunology
source_papers:
  - multiomics-analysis-cxcl9-macrophages-immunotherapy-response
evidence:
  - source: multiomics-analysis-cxcl9-macrophages-immunotherapy-response
    type: supports
    strength: strong
    detail: "Quote (p.3-4): 'From 5,098 myeloid cells, extracted for further sub-clustering, we discerned four primary macrophage populations: Macro-CCL4 (CCL4), Macro-CXCL9 (CXCL9), Macro-FOLR2 (FOLR2), and Macro-SPP1 (SPP1).'"
conditions: "113,905 cells from 16 patients (public PRJNA662018 n=11 + in-house n=5); 5,098 myeloid cells sub-clustered."
date_proposed: 2026-06-05
date_updated: 2026-06-05
---

## Statement

Sub-clustering of 5,098 myeloid cells from integrated bladder cancer scRNA-seq resolves four primary macrophage populations defined by marker genes: Macro-CCL4, Macro-CXCL9, Macro-FOLR2, and Macro-SPP1.

## Evidence summary

Descriptive single-cell finding from [[papers/multiomics-analysis-cxcl9-macrophages-immunotherapy-response]]. Consistent with the broader CXCL9:SPP1 macrophage polarity framework ([[concepts/cxcl9-spp1-tam-ratio-ici-biomarker]]).

## Conditions and scope

Integrated public + in-house bladder cohort; marker-gene-named clusters, nomenclature is study-specific.

## Counter-evidence

Cluster number depends on resolution choices; M1/M2 or pan-cancer TAM atlases use different partitions.

## Linked ideas

## Open questions

- How do these four states map onto pan-cancer TAM atlas clusters?
