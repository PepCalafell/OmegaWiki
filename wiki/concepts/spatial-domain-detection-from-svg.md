---
title: "Spatial domain detection from SVG-based feature selection"
aliases:
  - spatial domain detection
  - spatial clustering
  - tissue domain identification
  - SVG-based clustering
  - SVG vs HVG clustering
  - BayesSpace clustering
  - Banksy clustering
  - Leiden spatial clustering
  - spatial niche detection
  - DLPFC layer detection
  - tissue architecture segmentation
  - ARI spatial domain
tags:
  - spatial-transcriptomics
  - clustering
  - downstream-analysis
maturity: active
key_papers:
  - "[[papers/systematic-benchmarking-computational-methods-identify-spatially]]"
  - "[[papers/cellcharter-reveals-spatial-cell-niches-associated]]"
  - "[[papers/novae-graph-based-foundation-model-spatial]]"
first_introduced: "Maynard et al. 2021 Nat Neurosci (DLPFC reference); BayesSpace, Banksy"
date_updated: 2026-05-22
related_concepts:
  - "[[concepts/spatially-variable-gene-detection]]"
---

## Definition

Spatial domain detection is the task of partitioning a spatial transcriptomics sample into spatially contiguous regions of similar gene expression — analogous to cell-type clustering in scRNA-seq but with the additional constraint that clusters be spatially coherent. The choice of input feature set (SVGs vs HVGs) is one of the main drivers of clustering quality.

## Intuition

Clustering on highly variable genes (HVGs) selected without spatial information can yield biologically valid clusters that are nonetheless spatially scrambled. SVG-based feature selection biases clustering toward features whose variability has a spatial structure, which generally improves the spatial coherence and accuracy of detected domains.

## When to use

- Default for any downstream clustering on Visium/MERFISH/Xenium data — use SVG-selected features rather than HVGs.
- Evaluate clustering via ARI against pathologist annotation when ground truth exists, or via the spatial CHAOS score (mean pairwise distance within cluster) when it does not.

## Comparison

Per Li et al. 2025 (DLPFC, OSCC, HER2 datasets across Leiden, BayesSpace, Banksy clustering): most SVG methods improve clustering ARI over HVGs. Best mean ranks: Moran's I (6.5) > SpatialDE2 (6.6) > nnSVG (6.8). A small minority — SpaGCN, scGCO, BOOST-GP, SOMDE, Sepal — fail to outperform HVGs, indicating limited sensitivity across tissue architectures.

## Known limitations

- ARI rewards both spatially coherent and biologically valid clusters but requires ground-truth annotation.
- CHAOS rewards spatial coherence regardless of biological identity — high CHAOS-quality clusters may still be biologically meaningless.
- Choice of clustering algorithm (Leiden vs BayesSpace vs Banksy) interacts non-trivially with SVG choice; benchmark numbers averaged across algorithms hide some method-specific behaviour.

## Open problems

- Joint SVG-selection-plus-clustering frameworks that learn the spatial domain partition and the feature set simultaneously.
- Spatial domain detection on spatial ATAC-seq where SVP signal is poor (see [[concepts/spatial-atac-svp-detection-gap]]).
