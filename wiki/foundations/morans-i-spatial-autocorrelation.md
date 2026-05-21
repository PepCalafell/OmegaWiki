---
title: "Moran's I — spatial autocorrelation statistic"
slug: morans-i-spatial-autocorrelation
domain: spatial-statistics
status: mainstream
aliases:
  - Moran's I
  - Moran I
  - Moran I statistic
  - spatial autocorrelation
  - squidpy Moran's I
  - Moran's I SVG
  - classical spatial autocorrelation
first_introduced: "Moran 1950 Biometrika"
date_updated: 2026-05-21
source_url: "https://squidpy.readthedocs.io/"
---

## Definition

Moran's I is a classical spatial-autocorrelation statistic measuring the correlation of a variable's value at a location with values at neighbouring locations on a graph. In spatial transcriptomics, it scores how strongly a gene's expression at a spot correlates with the expression at its spatial neighbours.

## Intuition

If high-expression spots tend to neighbour high-expression spots (and low neighbours low), Moran's I → 1. Random spatial distribution → 0. Negative I → checkerboard/avoidance patterns. Among SVG methods, it is conceptually the simplest and fastest.

## Formal notation

```
I = (N / W) · Σ_i Σ_j w_ij (x_i − x̄)(x_j − x̄) / Σ_i (x_i − x̄)²
```

with `w_ij` the spatial weight (often KNN), `W = Σ w_ij`, and `N` the number of spots.

## Key variants

- Squidpy implementation provides three significance approaches: normality assumption, permutation test, normal approximation from permutations.
- Implemented in Python on AnnData objects — most accessible Python SVG tool.

## Known limitations

- Operates on normalized expression (not raw counts).
- Tends to overestimate p-values (fails to control type I errors) per Li et al. 2025 benchmark.
- Detects autocorrelation; does not jointly model multiple spatial patterns or kernel shapes.

## Relevance to active research

In Li et al. 2025 Genome Biology SVG benchmark, Moran's I ranks 3rd overall and is the BEST method for the downstream task of spatial domain detection (best mean rank across DLPFC, OSCC, HER2 datasets). The authors recommend including it as a baseline in future SVG-method benchmarks.
