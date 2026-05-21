---
title: "Statistical calibration of SVG detection p-values"
aliases:
  - SVG p-value calibration
  - spatial variability p-value calibration
  - SVG statistical calibration
  - SVG type I error control
  - K-S calibration spatial transcriptomics
  - poorly calibrated SVG methods
  - SVG miscalibration
  - over-conservative spatial p-values
  - over-liberal spatial p-values
  - Cauchy combination SVG
  - QQ plot SVG benchmark
  - null spatial randomness test
tags:
  - spatial-transcriptomics
  - statistics
  - calibration
  - benchmarking
maturity: active
key_papers:
  - "[[papers/systematic-benchmarking-computational-methods-identify-spatially]]"
first_introduced: "Long-standing problem in genomic differential analysis; applied to SVG in Li et al. 2025"
date_updated: 2026-05-21
related_concepts:
  - "[[concepts/spatially-variable-gene-detection]]"
---

## Definition

Calibration of SVG p-values is the property that, under the null hypothesis of no spatial structure (gene expression independent of spatial location), observed p-values from a method follow a uniform U(0,1) distribution. Methods that systematically deviate are either over-liberal (too many small p-values → inflated false positives) or over-conservative (too few small p-values → missed true SVGs).

## Intuition

A QQ plot of observed p-values against the expected uniform quantiles reveals miscalibration as deviation from the diagonal. Empirically, miscalibration is measured by the Kolmogorov–Smirnov (K-S) distance between the observed and uniform distributions — smaller K-S = better calibration.

## Formal notation

Under H0 (gene expression independent of spatial location): `p ~ U(0,1)`. Calibration metric: `K-S = sup_x | F_obs(x) − x |`.

## When to use

This concept is relevant whenever an SVG analysis uses p-values for thresholding rather than a fixed rank cutoff. If calibration is poor, users should switch to rank-based feature selection (top N genes by score).

## Known limitations

- Per Li et al. 2025: only SPARK and SPARK-X produce well-calibrated p-values across both 10x Visium mouse olfactory bulb and 10x Xenium colon-cancer null datasets.
- Six methods (SpatialDE, Spanve, SOMDE, scGCO, nnSVG, BOOST-GP) are over-conservative (fail to control type II error).
- Four methods (SpaGFT, GPcounts, SpaGCN, Moran's I) are over-liberal (fail to control type I error).
- SPARK and SPARK-X's good calibration is attributed to the Cauchy combination rule for combining per-kernel p-values.

## Open problems

- A unified well-calibrated test that does not require multiple-kernel Cauchy combination.
- Calibration analysis for spatial ATAC-seq, where the binary/sparse signal further complicates the null distribution.
