---
title: "Cell-type abundance scoring from bulk tissue RNA-seq via cell-type-specificity gene rankings recovers 195-cell-type shifts across 9 organs"
slug: cell-type-abundance-score-bulk-rnaseq-methodology
status: supported
confidence: 0.8
tags:
  - methods
  - bulk-RNA-seq
  - deconvolution
  - cell-type
domain: bioinformatics / deconvolution
source_papers:
  - pairwise-cytokine-code-explains-organism-wide
evidence:
  - source: pairwise-cytokine-code-explains-organism-wide
    type: supports
    strength: strong
    detail: "Per-gene cell-type specificity scores were computed for 195 cell types × 9 organs from a scRNA-seq atlas; ranked gene sets gave per-sample abundance scores; spatial transcriptomics + IHC validated 7/7 selected predictions (hepatocytes, kidney epithelia, colon neurons, splenic B cells, BM erythroid, whole-body neutrophils, macrophages)."
conditions: "Bulk tissue RNA-seq paired with a comprehensive single-cell tissue atlas reference."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

A specificity-ranked cell-type abundance scoring approach applied to organism-wide bulk RNA-seq recovers cell-type abundance shifts across 195 cell types in 9 organs and shows 7/7 prospective validation in spatial transcriptomics and immunohistochemistry.
