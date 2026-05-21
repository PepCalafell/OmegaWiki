---
title: "SPARK-X — non-parametric covariance test for spatially variable gene detection"
slug: spark-x-svg
domain: spatial-transcriptomics-methods
status: mainstream
aliases:
  - SPARK-X
  - SPARK-X SVG detection
  - non-parametric SPARK
  - covariance-test SVG
  - Zhu Sun Zhou 2021 SPARK-X
first_introduced: "Zhu, Sun, Zhou 2021 Genome Biology"
date_updated: 2026-05-21
source_url: "https://github.com/xzhoulab/SPARK"
---

## Definition

SPARK-X is an R-based statistical method for identifying spatially variable genes (SVGs) in spatial transcriptomics data. Unlike Gaussian-process-regression SVG methods, SPARK-X directly tests whether the gene-expression covariance matrix matches a spatial-distance covariance matrix derived from a panel of kernel functions, yielding chi-square-based adjusted p-values.

## Intuition

If a gene's expression pattern is non-random in space, the covariance structure of its expression across spots should align with at least one of several reasonable spatial similarity kernels (Gaussian, periodic, etc.). SPARK-X enumerates 11 kernels and combines per-kernel p-values via the Cauchy combination rule.

## Key variants

- Operates directly on raw counts (not normalized expression).
- Uses 11 kernels of varying bandwidth and shape — broader than SpatialDE2's 5 kernels.

## Known limitations

- R-only implementation; not directly applicable to Python AnnData workflows without preprocessing.
- Underperforms on small high-expression "spot" patterns (concentrated expression in a tiny region).
- Not designed for spatial ATAC-seq (peak matrices ≫ gene matrices).

## Relevance to active research

In Li et al. 2025 Genome Biology SVG benchmark, SPARK-X is the best-performing method overall (average rank 4.3 across 6 metrics) including best ranking accuracy and well-calibrated p-values. Together with Moran's I and nnSVG, it forms the field's current SVG-detection reference baseline.
