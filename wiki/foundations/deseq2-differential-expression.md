---
title: "DESeq2 — negative-binomial differential expression for RNAseq counts"
slug: deseq2-differential-expression
domain: "computational-biology / methods"
status: mainstream
aliases:
  - "DESeq2"
  - "DESeq2 differential expression"
  - "negative binomial RNAseq DE"
  - "Love DESeq2"
  - "Wald test DESeq2"
  - "shrinkage log fold change DESeq2"
  - "Love Huber Anders 2014"
  - "bulk RNAseq DESeq2"
  - "RNAseq count-based differential expression"
first_introduced: "Love, Huber & Anders 2014 *Genome Biology*"
date_updated: 2026-05-13
source_url: "https://bioconductor.org/packages/release/bioc/html/DESeq2.html"
---

## Definition

DESeq2 is a Bioconductor R package for differential expression analysis of count-based RNAseq data using a negative-binomial generalized linear model. It estimates per-gene dispersion via empirical-Bayes shrinkage and applies log-fold-change shrinkage to stabilize estimates for low-count genes.

## Workflow

1. Construct a `DESeqDataSet` from count matrix + sample metadata + design formula.
2. Normalize via median-of-ratios size factors.
3. Estimate per-gene dispersions with empirical-Bayes shrinkage toward a fitted mean-dispersion curve.
4. Fit negative-binomial GLM; perform Wald / LRT tests.
5. Apply LFC shrinkage (`lfcShrink`, e.g., `apeglm`) for stable effect-size estimates.
6. Multiple-testing correction via independent-filtering + BH FDR.

## Strengths

- Robust to small-sample variance estimation via shrinkage.
- Flexible design formulas (multi-factor, interactions).
- LFC shrinkage stabilizes effect sizes for downstream ranking (e.g., as input to fgsea).

## Limitations

- Designed for bulk counts; not appropriate for scRNAseq cell-level DE without aggregation.
- Negative-binomial assumption may be violated for very low-count or zero-inflated data.
- Pseudobulk aggregation is required for scRNAseq use cases.

## Use cases in this corpus

- [[papers/using-pan-cancer-atlas-investigate-tumour]] uses DESeq2 v1.36.0 with `~ tumour_type + response` design on CPI1000+ bulk RNAseq (n=1446), producing a ranked gene list for fgsea pathway analysis against TAM cluster signatures.

## Relevance to active research

- [[papers/using-pan-cancer-atlas-investigate-tumour]] — Coulton et al. 2024.
