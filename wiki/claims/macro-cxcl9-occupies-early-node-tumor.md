---
title: "Macro-CXCL9 occupies the early node of the tumor macrophage differentiation trajectory"
slug: macro-cxcl9-occupies-early-node-tumor
status: weakly_supported
confidence: 0.5
tags: [macrophage, trajectory, pseudotime, CXCL9, bladder-cancer]
domain: oncology / immunology
source_papers:
  - multiomics-analysis-cxcl9-macrophages-immunotherapy-response
evidence:
  - source: multiomics-analysis-cxcl9-macrophages-immunotherapy-response
    type: supports
    strength: moderate
    detail: "Quote (p.4): 'Macro-CXCL9 subpopulation is situated at the initial differentiation site of macrophages. We identified differentiation pathways from Macro-CXCL9 to Macro-SPP1 and Macro-FOLR2.'"
conditions: "Single-cell pseudotime/RNA-velocity inference in bladder cancer scRNA-seq (16 patients); trajectory direction is computational, not lineage-traced."
date_proposed: 2026-06-05
date_updated: 2026-06-05
---

## Statement

In bladder cancer, single-cell trajectory and RNA-velocity analysis place the Macro-CXCL9 subpopulation at the initial differentiation node of tumour macrophages, with inferred paths from Macro-CXCL9 toward Macro-SPP1 and Macro-FOLR2.

## Evidence summary

Reported from pseudotime (PAGA/scVelo) analysis in [[papers/multiomics-analysis-cxcl9-macrophages-immunotherapy-response]]. Relates to [[concepts/macro-cxcl9-progenitor-node-tumor-macrophage]].

## Conditions and scope

Computational trajectory inference on snapshot scRNA-seq; population-size effects can confound flux direction (see [[concepts/population-size-confounds-snapshot-trajectory-flux]]).

## Counter-evidence

No lineage tracing; directionality is inferred only.

## Linked ideas

## Open questions

- Is the Macro-CXCL9 → SPP1/FOLR2 path a true differentiation hierarchy or an IFN-γ-exposure state continuum?
