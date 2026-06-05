---
title: "Macro-CXCL9 engages ACKR1+ endothelium and LAG3+ CD8-CXCL13 cells via distinct ligand-receptor axes"
slug: macro-cxcl9-ligand-receptor-interactions-ackr1
status: weakly_supported
confidence: 0.45
tags: [cell-cell-interaction, LIANA, CXCL9, LAG3, ACKR1, macrophage]
domain: oncology / immunology
source_papers:
  - multiomics-analysis-cxcl9-macrophages-immunotherapy-response
evidence:
  - source: multiomics-analysis-cxcl9-macrophages-immunotherapy-response
    type: supports
    strength: moderate
    detail: "Quote (p.4-5): 'CXCL9 and CXCL10 secreted by Macro-CXCL9 can interact with ACKR1 ... on the surface of endothelial cells. Macro-CXCL9 also produces HLA-DRB1, HLA-DQB1, and HLA-DQA1, which bind to the LAG3 receptor on CD8-CXCL13 cells ... Macro-CXCL9 produces C1QB and APOE, which bind to their receptors LRP1 and LRP6 on Fibro-CXCL14 cells.'"
conditions: "LIANA cell-cell interaction inference from scRNA-seq co-expression; not validated by physical or spatial contact assays."
date_proposed: 2026-06-05
date_updated: 2026-06-05
---

## Statement

Inferred cell-cell interaction analysis (LIANA) suggests Macro-CXCL9 signals to neighbouring cells through three axes: CXCL9/CXCL10–ACKR1 on endothelial cells, HLA-DR/DQ–LAG3 on CD8-CXCL13 cells, and C1QB/APOE–LRP1/LRP6 on CXCL14⁺ fibroblasts.

## Evidence summary

Ligand-receptor inference from [[papers/multiomics-analysis-cxcl9-macrophages-immunotherapy-response]] using [[foundations/liana-cell-cell-interaction-inference]]. Connects Macro-CXCL9 to [[foundations/cxcl9-chemokine]] and [[foundations/cxcl10-chemokine]] signalling.

## Conditions and scope

Co-expression-based inference; ACKR1 is an atypical (decoy/chemokine-presenting) receptor; HLA–LAG3 binding here is interpreted as immunostimulatory by the authors.

## Counter-evidence

No spatial proximity or perturbation validation; interaction calls can be false positives.

## Linked ideas

## Open questions

- Are these inferred interactions spatially co-located in tissue, and which are functionally relevant to ICI response?
