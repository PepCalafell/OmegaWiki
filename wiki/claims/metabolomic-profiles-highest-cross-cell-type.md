---
title: "Metabolomic profiles have the highest cross-cell-type similarity, making metabolomics deconvolution hardest"
slug: metabolomic-profiles-highest-cross-cell-type
status: supported
confidence: 0.8
tags: [metabolomics, cell-type-specificity, deconvolution]
domain: methods
source_papers:
  - decode-deep-learning-based-common-deconvolution
evidence:
  - source: decode-deep-learning-based-common-deconvolution
    type: supports
    strength: moderate
    detail: "Kendall similarity of liver cell types across omics shows metabolomic profiles most similar across cell types (Fig. 3a); only GMP cells show markedly distinct metabolites (Fig. 3b)."
conditions: "Assessed in mouse liver and across three metabolomics datasets with 107–244 features."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

Among transcriptomic, proteomic and metabolomic data, metabolomic profiles exhibit the highest similarity across cell types (lowest cell-type specificity), which together with the small number of measurable features makes metabolomics the hardest omics to deconvolve.

## Evidence summary

Kendall similarity heatmaps of mouse liver cell types show metabolomics with the highest cross-cell-type similarity (Fig. 3a). Differential-metabolite analysis found only granulocyte-monocyte progenitors markedly distinct (Fig. 3b). Detectable metabolites number in the hundreds vs. thousands of proteins or tens of thousands of RNAs.

## Conditions and scope

Correlational observation grounding [[metabolomics-deconvolution]] difficulty; based on limited datasets.

## Counter-evidence

None within the paper.

## Linked ideas

## Open questions

Whether higher-throughput single-cell metabolomics would raise feature specificity.
