---
title: "TIMER — Tumor IMmune Estimation Resource"
slug: timer-tumor-immune-deconvolution
domain: methods / computational immunology
status: mainstream
aliases:
  - TIMER
  - TIMER2.0
first_introduced: "2017"
date_updated: 2026-06-03
source_url: "https://academic.oup.com/nar/article/48/W1/W509/5842187"
---

## Definition

A deconvolution method and web resource that estimates the abundance of tumor-infiltrating immune cell populations (B cells, CD4/CD8 T cells, neutrophils, macrophages, dendritic cells) from bulk tumor RNA-seq, calibrated on TCGA. TIMER2.0 extends estimates across multiple algorithms and cell types.

## Intuition

Bulk tumor expression mixes malignant and immune signals; TIMER back-computes relative immune-cell fractions so that expression-based phenotypes can be related to immune infiltration without single-cell data.

## Known limitations

Relative (not absolute) abundances; estimates depend on reference signatures and can be confounded by tumor purity. Best used for cross-sample comparisons within a cancer type.

## Relevance to active research

Standard tool for linking bulk-RNA-derived tumor phenotypes (e.g., innate-immune activation scores) to immune-cell infiltration in pan-cancer TCGA analyses.
