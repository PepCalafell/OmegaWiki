---
title: "ssGSEA — Single-Sample Gene Set Enrichment Analysis"
slug: ssgsea-single-sample-gsea
domain: methods
status: mainstream
aliases:
  - ssGSEA
  - single-sample GSEA
  - single-sample gene set enrichment
  - sample-level enrichment score
  - per-sample GSEA
first_introduced: "Barbie et al. 2009 Nature"
date_updated: 2026-05-25
source_url: ""
---

## Definition
A variant of gene set enrichment analysis that computes a per-sample enrichment score for a given gene set using rank-normalised within-sample expression. Unlike classical GSEA, which compares two phenotype groups, ssGSEA assigns each sample a continuous enrichment score that can be used as a feature in downstream clustering or regression.

## Intuition
ssGSEA turns gene sets into continuous sample-level signatures. Useful for converting catalogue gene sets (Hallmark, immune subsets, tissue signatures) into a per-sample matrix for unsupervised analysis.

## Formal notation
- Rank-normalise within sample → ECDF over gene set vs ECDF over complement → integrated difference → enrichment score

## Key variants
- ssGSEA on bulk RNA or protein expression
- GSVA — a related single-sample enrichment method with Gaussian kernel
- ssGSEA-based ESTIMATE scoring

## Known limitations
- Sensitive to gene set size and overlap.
- Cannot establish per-sample significance without a null model.

## Open problems
- Calibrated per-sample p-values for ssGSEA enrichment.

## Relevance to active research
ssGSEA is the workhorse for translating pre-defined biological signatures into per-sample features, broadly used in pan-cancer / pan-tissue analyses (e.g., TPCPA hallmark and immune-signature scoring).
