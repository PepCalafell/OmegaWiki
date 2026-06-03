---
title: "TRADE (transcriptome-wide impact)"
slug: trade-transcriptome-wide-impact
domain: single-cell genomics
status: mainstream
aliases:
  - TRADE
  - transcriptome-wide impact
  - transcriptome-wide association of differential expression
first_introduced: "2024"
date_updated: 2026-06-03
source_url: ""
---

## Definition

TRADE is a statistical model for quantifying the transcriptome-wide impact (TI) of a perturbation or covariate on a cell population. It aggregates gene-level differential-expression effect sizes into a single distributional summary that estimates the overall magnitude of transcriptional change, correcting for estimation noise.

## Intuition

Counting "significant genes" is threshold-dependent and underpowered. TRADE instead models the full distribution of effect sizes to ask how much the entire transcriptome of a cell type is shifted, giving a noise-aware, threshold-free measure of impact.

## Formal notation

It fits a distribution to the gene-level log-fold-change estimates while deconvolving sampling noise, yielding moments (e.g. transcriptome-wide variance of effects) used as the impact statistic.

## Key variants

- Applicable to bulk, pseudobulk, and single-cell differential-expression outputs.

## Known limitations

- Relies on well-estimated gene-level effect sizes; sparse or low-count populations degrade the estimate.

## Open problems

- Extending the impact summary to continuous and multi-axis covariates.

## Relevance to active research

scSLIDE couples TRADE with gene-level coefficients from its trajectory-based NB-GLM to compute the transcriptome-wide impact of each sample-level axis on each cell type, providing a continuous, reproducible alternative to classifier-based cell-type prioritization such as Augur.
