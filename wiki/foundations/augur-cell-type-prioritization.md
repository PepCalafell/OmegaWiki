---
title: "Augur (cell-type prioritization)"
slug: augur-cell-type-prioritization
domain: single-cell genomics
status: mainstream
aliases:
  - Augur
first_introduced: "2020"
date_updated: 2026-06-03
source_url: ""
---

## Definition

Augur is a method that ranks cell types by how strongly they respond to an experimental or disease perturbation. For each cell type it trains a classifier to separate cells by condition label and uses cross-validated classification accuracy (AUC) as a measure of how perturbation-responsive that population is.

## Intuition

If a classifier can easily tell apart "case" and "control" cells within a given cell type, that cell type is strongly affected by the condition. Augur turns this separability into a prioritization score.

## Formal notation

Per cell type: subsample to balance, train a random-forest classifier on condition labels, report mean cross-validated AUC as the prioritization statistic.

## Key variants

- Multi-class and continuous-covariate extensions.

## Known limitations

- Limited to binary (or single-variable) comparisons; cannot disentangle multiple coexisting sources of sample heterogeneity.
- Can be confounded when groups contain additional structured variation, reducing cross-dataset reproducibility.

## Open problems

- Robust prioritization under multiple overlapping phenotypic axes.

## Relevance to active research

Augur is a widely used baseline for disease-relevant cell-type prioritization. scSLIDE's TRADE-based transcriptome-wide-impact prioritization is benchmarked against Augur and shown to be more reproducible across independent cohorts because it is not restricted to binary contrasts.
