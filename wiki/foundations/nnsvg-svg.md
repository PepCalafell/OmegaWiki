---
title: "nnSVG — nearest-neighbour Gaussian-process SVG detection"
slug: nnsvg-svg
domain: spatial-transcriptomics-methods
status: mainstream
aliases:
  - nnSVG
  - nearest-neighbour SVG
  - Weber Bortoluzzi 2023 nnSVG
  - hierarchical nearest-neighbour GP
  - NNGP SVG
first_introduced: "Weber et al. 2023 Nature Communications"
date_updated: 2026-05-21
source_url: "https://github.com/lmweber/nnSVG"
---

## Definition

nnSVG is an R-based SVG detection method that fits a hierarchical nearest-neighbour Gaussian-process (NNGP) model to spatial transcriptomics data on normalized expression. It scales the standard Gaussian-process SVG framework (SpatialDE-style) to larger datasets by approximating the full GP with a sparse nearest-neighbour structure.

## Intuition

Standard Gaussian-process regression on N spots scales as O(N³), prohibitive for N > 10k. nnSVG replaces the dense covariance with a nearest-neighbour graph, achieving substantial efficiency while preserving GP-based likelihood-ratio testing for spatial variance.

## Known limitations

- Operates on normalized (not raw count) expression.
- R-only; preprocessing required for Python-based workflows.
- Tends to produce over-conservative p-values (poor calibration) per Li et al. 2025 benchmark.

## Relevance to active research

In Li et al. 2025 Genome Biology SVG benchmark, nnSVG ranks third in average ranking accuracy (Kendall correlation 0.80) and is recommended (alongside Moran's I and SpatialDE2) for spatial domain detection. Among GP-based methods it is the most scalable.
