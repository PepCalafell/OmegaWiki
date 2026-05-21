---
title: "SVP detection on spatial ATAC-seq — methodological gap"
aliases:
  - SVP detection
  - spatially variable peak
  - spatially variable peaks
  - spatial ATAC SVP
  - spatial peak variability
  - spatial chromatin accessibility variability
  - spatial epigenome SVP
  - all-peaks baseline
  - CHAOS score SVP
  - spatial-ATAC clustering
  - spatial GRN gap
  - SVG-to-SVP repurposing
tags:
  - spatial-atac-seq
  - spatial-epigenomics
  - methods-gap
maturity: emerging
key_papers:
  - "[[papers/systematic-benchmarking-computational-methods-identify-spatially]]"
first_introduced: "Spatial ATAC: Deng et al. 2022 Nature; SVP gap quantified: Li et al. 2025"
date_updated: 2026-05-21
related_concepts:
  - "[[concepts/spatially-variable-gene-detection]]"
---

## Definition

Spatially variable peak (SVP) detection is the spatial-ATAC-seq analogue of SVG detection: identifying open-chromatin peaks whose accessibility shows non-random spatial patterning. There is currently no purpose-built SVP detection method — the only available approach is repurposing SVG tools.

## Intuition

The problem looks superficially identical to SVG detection (replace genes with peaks) but is structurally different: peak signal is near-binary and extremely sparse, peak matrices are 5–35× higher-dimensional than gene matrices, and the over-dispersed Poisson/NB count distributions assumed by SVG methods are a poor fit.

## When to use

Until specialised SVP methods exist, the Li et al. 2025 benchmark's pragmatic recommendation is: use SpatialDE2 (only repurposed method that beats the "all peaks" baseline) or simply retain all peaks for downstream clustering.

## Known limitations

- BOOST-GP and GPcounts fail to complete within 120 h on typical spatial-ATAC matrices.
- SPARK runs out of memory.
- "Use all peaks" achieves mean CHAOS = 0.105, only marginally worse than SpatialDE2 (0.104) and better than every other SVG-method-repurposed approach — strong evidence that current SVG methods do not extract useful spatial signal from peak data.

## Open problems

- Native SVP-detection algorithms designed for binary/Bernoulli sparse spatial signals.
- Joint SVG–SVP integration for spatially aware gene-regulatory networks (a future-directions item in Li et al. 2025).
- Analogous SVP-style methods for spatial proteomics, spatial methylation, and other spatial omics modalities.
