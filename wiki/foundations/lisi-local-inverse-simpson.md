---
title: "LISI — Local Inverse Simpson's Index for single-cell batch/cell-type mixing"
slug: lisi-local-inverse-simpson
domain: "methods / batch-effect-metric / single-cell"
status: mainstream
aliases:
  - LISI
  - iLISI
  - cLISI
  - Local Inverse Simpson's Index
  - graph iLISI
  - graph cLISI
  - Korsunsky LISI
  - Harmony LISI metric
  - integration LISI
  - cell-type LISI
  - inverse Simpson diversity single-cell
first_introduced: "Korsunsky et al. 2019 *Nat. Methods* (Harmony LISI scoring); graph extensions in Luecken et al. 2022 *Nat. Methods*"
date_updated: 2026-05-22
source_url: "https://github.com/immunogenomics/lisi"
---

## Definition

LISI computes the inverse Simpson's diversity index in a cell's local neighborhood. Two variants: iLISI (integration LISI) measures batch mixing — higher = better batch integration; cLISI (cell-type LISI) measures cell-type purity — lower = better identity preservation. scIB extends both to graph-output methods via graph kNN neighborhoods.

## Strengths

- Captures both batch mixing and identity preservation in a unified framework.
- Graph extension supports graph-output methods.
- Continuous (not binary) measure, sensitive to subtle integration quality.

## Known limitations

- Neighborhood size choice affects results.
- Like kBET, can be optimised in isolation without improving overall integration.

## Relevance to active research

LISI (iLISI + cLISI) is a core scIB metric pair, capturing both axes of the batch-removal vs bio-conservation tradeoff. See [[foundations/scib-benchmark-pipeline]] and [[papers/benchmarking-atlas-level-data-integration-single]].
