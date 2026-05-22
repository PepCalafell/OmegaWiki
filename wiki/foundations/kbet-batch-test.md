---
title: "kBET — k-nearest-neighbor batch effect test"
slug: kbet-batch-test
domain: "methods / batch-effect-metric / single-cell"
status: mainstream
aliases:
  - kBET
  - k-nearest-neighbor batch effect test
  - Büttner kBET
  - kBET metric
  - scIB kBET
  - graph kBET
  - chi-square batch test single-cell
  - kBET acceptance rate
  - kBET rejection rate
  - single-cell batch effect chi-square test
first_introduced: "Büttner et al. 2019 *Nat. Methods* (A test metric for assessing single-cell RNA-seq batch correction)"
date_updated: 2026-05-22
source_url: "https://github.com/theislab/kBET"
---

## Definition

kBET tests whether the batch composition in a cell's k-nearest-neighbor neighborhood matches the expected global batch composition via a chi-square test. The output is a per-cell rejection rate; lower aggregate rejection rate indicates better batch mixing. The original kBET works on gene-expression matrices; scIB extends it to graph outputs (graph kBET) for consistent metric across output types.

## Strengths

- Statistically grounded measure of batch mixing.
- Per-cell granularity — can be analysed by cell type.
- Graph extension supports integrated graph outputs (BBKNN, Conos).

## Known limitations

- Sensitive to k choice and to imbalanced batch sizes.
- Pure batch-mixing metric — does not penalize over-mixing that erases biology.

## Relevance to active research

kBET is a core batch-removal metric in the scIB benchmark. See [[foundations/scib-benchmark-pipeline]] and [[papers/benchmarking-atlas-level-data-integration-single]].
