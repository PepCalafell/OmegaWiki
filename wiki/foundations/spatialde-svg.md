---
title: "SpatialDE / SpatialDE2 — Gaussian-process SVG detection"
slug: spatialde-svg
domain: spatial-transcriptomics-methods
status: mainstream
aliases:
  - SpatialDE
  - SpatialDE2
  - Svensson Teichmann 2018 SpatialDE
  - Kats et al. 2021 SpatialDE2
  - GP SVG detection
  - fraction-of-spatial-variance FSV
first_introduced: "Svensson, Teichmann, Stegle 2018 Nature Methods"
date_updated: 2026-05-21
source_url: "https://github.com/Teichlab/SpatialDE"
---

## Definition

SpatialDE is a Python-based, pioneer SVG-detection method that fits non-parametric Gaussian-process regression on normalized expression and tests the significance of the spatial covariance contribution via a chi-square test. It quantifies the fraction of spatial variance (FSV) as the gene-ranking score. SpatialDE2 (Kats et al. 2021) extends the framework with technical innovations and computational speedups.

## Intuition

Model the spot-by-spot expression as a sum of a spatial GP plus residual noise; compare model fits with and without the spatial component to obtain a p-value and FSV.

## Known limitations

- Cubic GP scaling in spot count drives high memory cost (~150 GB for 40k spots).
- Operates on normalized expression rather than raw counts.
- SpatialDE p-values are not well calibrated (over-conservative).
- SpatialDE2 does not return p-values; only FSV scores.

## Relevance to active research

In Li et al. 2025 Genome Biology SVG benchmark, SpatialDE2 ranks 2nd in Kendall correlation accuracy (0.81) and is the ONLY method that outperforms an "all peaks" baseline on spatial ATAC-seq downstream clustering, suggesting it may generalise better than competitors to non-RNA-seq spatial omics.
