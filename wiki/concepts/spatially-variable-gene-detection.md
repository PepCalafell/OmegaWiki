---
title: "Spatially variable gene (SVG) detection in spatial transcriptomics"
aliases:
  - SVG detection
  - spatially variable gene
  - spatially variable genes
  - SVG identification
  - spatial gene-expression patterning
  - SVG method
  - SVG ranking
  - spatial variability score
  - SVG selection
  - spatial autocorrelation gene detection
  - SVG vs HVG
  - spatially differentially expressed gene
tags:
  - spatial-transcriptomics
  - methods
  - feature-selection
  - benchmarking
maturity: active
key_papers:
  - "[[papers/systematic-benchmarking-computational-methods-identify-spatially]]"
first_introduced: "Svensson, Teichmann, Stegle 2018 (SpatialDE); Sun, Zhu, Zhou 2020 (SPARK); Edsgärd 2018 (trendsceek)"
date_updated: 2026-05-21
related_concepts:
  - "[[concepts/svg-pvalue-calibration]]"
  - "[[concepts/spatial-domain-detection-from-svg]]"
  - "[[concepts/spatial-atac-svp-detection-gap]]"
---

## Definition

Spatially variable gene (SVG) detection is the task of identifying, from a spatial transcriptomics dataset, those genes whose expression varies non-randomly across the spatial coordinates of measured locations (spots or cells). Methods produce per-gene scores that rank genes by their degree of spatial structure, and typically also a per-gene p-value of significance against a null of spatial randomness.

## Intuition

In single-cell RNA-seq, highly variable genes (HVGs) are the standard feature-selection input. In spatial transcriptomics, this is insufficient: a gene can have low overall variance but a striking spatial pattern, or high overall variance but no spatial coherence. SVG methods explicitly incorporate spatial coordinates into the variability calculation.

## Formal notation

SVG detection methods fall into three broad families (per Li et al. 2025):

- **Graph-based**: build a KNN graph on spots, score each gene by autocorrelation (Moran's I), graph cuts (scGCO), GCN clustering (SpaGCN), Fourier transform (SpaGFT), diffusion (Sepal), or sampling divergence (Spanve).
- **Kernel/GP-based**: model expression as a GP over a spatial kernel and test the spatial covariance contribution (SpatialDE, SpatialDE2, SPARK, BOOST-GP, GPcounts) or directly compare covariance matrices (SPARK-X).
- **Hybrid graph+kernel**: nearest-neighbour GP (nnSVG), SOM-aggregated GP (SOMDE).

## Variants

- Some methods consume raw counts (SPARK, SPARK-X, BOOST-GP, GPcounts, SOMDE), others normalized expression (Moran's I, Spanve, scGCO, SpaGCN, SpaGFT, Sepal, SpatialDE, SpatialDE2, nnSVG).
- Significance tests differ: chi-square, Wilcoxon, permutation, Bayesian FDR, likelihood-ratio.

## Comparison

Per Li et al. 2025 ranking by overall benchmark performance: SPARK-X (best, avg rank 4.3) > SpaGFT (5.4) > Moran's I (3rd). Pattern-specific behaviour matters — no single method dominates across all spatial patterns (small concentrated spots vs broad gradients).

## When to use

- Comprehensive SVG ranking → SPARK-X (or SPARK if data fit).
- Spatial domain detection downstream → Moran's I, SpatialDE2, or nnSVG.
- Memory- or time-constrained large datasets (>20k spots) → SOMDE or SPARK-X.
- Quick exploratory analysis in Python/AnnData → Moran's I (Squidpy).

## Known limitations

- Most methods produce poorly calibrated p-values; rank thresholds (e.g. top 2000 genes) are safer than significance thresholds for feature selection.
- No method is rotation-invariant — same biological tissue oriented differently can yield different SVG sets.
- Continuous spatial variability is forced into binary SVG/non-SVG decisions when significance thresholds are applied.

## Open problems

- Specialised SVP detection for spatial ATAC-seq (current SVG methods fail; see [[concepts/spatial-atac-svp-detection-gap]]).
- SVG–SVP integration for spatial gene-regulatory networks.
- Rotation- and registration-invariant SVG scoring.
