---
title: "Malignant cells have by far the highest cancer-type specificity, followed by non-malignant epithelial cells"
slug: cca3-malignant-and-epithelial-highest-cancer-type-specificity
status: supported
confidence: 0.95
tags: [pan-cancer, pseudobulk, malignant, epithelial, scrna-seq]
domain: oncology
source_papers:
  - curated-cancer-cell-atlas-provides-comprehensive
evidence:
  - source: curated-cancer-cell-atlas-provides-comprehensive
    type: supports
    strength: strong
    detail: "Pseudobulk similarity comparison shows malignant cells with highest cancer-type specificity, with max(P)=0.0051 vs non-malignant TME cells."
conditions: "Compared via pseudobulk pairs from different studies (batch-controlled)."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

In 3CA v2, malignant cells exhibit by far the highest cancer-type specificity of average expression, followed by non-malignant epithelial cells. All differences vs non-epithelial TME cell types are significant after FDR correction.

## Evidence summary

Pseudobulk similarity analysis (Fig. 4f).

## Conditions and scope

Effect is at the average expression level; within-cell-type heterogeneity remains substantial.

## Counter-evidence

None.

## Linked ideas

—

## Open questions

- How much of the malignant cell signal is cell-of-origin vs. driver-mutation programs?
