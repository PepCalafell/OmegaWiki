---
title: "Spatial ATAC-seq — spatially resolved chromatin accessibility profiling"
slug: spatial-atac-seq
domain: spatial-epigenomics
status: mainstream
aliases:
  - spatial ATAC-seq
  - spatial-ATAC-seq
  - spatial chromatin accessibility
  - spatial epigenomics
  - Deng et al. 2022 spatial ATAC
  - spatially resolved ATAC
  - SVP detection input
first_introduced: "Deng et al. 2022 Nature / Llorens-Bobadilla 2023"
date_updated: 2026-05-21
source_url: ""
---

## Definition

Spatial ATAC-seq is the spatial extension of bulk/single-cell ATAC-seq, profiling spatially resolved open-chromatin peaks across a tissue section. Typical outputs are (spot × peak) matrices with 20,000–70,000 peaks per sample, an order of magnitude higher dimensionality than transcriptome-based ST.

## Intuition

Where SVG analysis identifies spatially variable genes, the analogous task on spatial ATAC-seq is identifying spatially variable peaks (SVPs) — open-chromatin regions whose accessibility forms spatial patterns. SVPs can in principle anchor spatial gene-regulatory network inference.

## Key variants

- Mouse embryo developmental atlases at E12.5 / E13.5 / E15.5 are common benchmark datasets.
- Related: spatial CUT&Tag, spatial CUT&RUN.

## Known limitations

- Extreme sparsity — most peaks have zero counts at most spatial locations.
- Near-binary signal (peak open vs closed) violates the over-dispersed Poisson/NB assumptions of SVG methods designed for RNA-seq counts.
- High dimensionality (20–70k peaks vs ~2–5k genes for ST analysis) breaks Gaussian-process SVG methods on memory and time grounds.

## Open problems

- No specialised SVP detection algorithm exists. Li et al. 2025 show that "use all peaks" beats most repurposed SVG methods for downstream clustering — only SpatialDE2 marginally outperforms the all-peaks baseline.
- Integrating SVGs and SVPs to build spatially aware gene-regulatory networks is an open frontier.

## Relevance to active research

Identified as a major methodological gap by the [[papers/systematic-benchmarking-computational-methods-identify-spatially]] benchmark. The benchmark recommends developing distribution-aware (binary/Bernoulli rather than NB) SVP-specific methods.
