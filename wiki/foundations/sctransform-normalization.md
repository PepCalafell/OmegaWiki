---
title: "SCTransform — regularised negative-binomial normalisation for scRNA-seq"
slug: sctransform-normalization
domain: methods/single-cell
status: mainstream
aliases:
  - SCTransform
  - sctransform
  - SCT normalization
  - regularized negative binomial scRNA-seq
  - Seurat SCTransform v2
  - variance-stabilising transformation single-cell
  - SCTransform v2 Pearson residuals
first_introduced: "Hafemeister 2019 Genome Biol"
date_updated: 2026-05-22
source_url: "https://satijalab.org/seurat/articles/sctransform_vignette.html"
---

## Definition
SCTransform fits a regularised negative-binomial generalised linear model per gene, conditioning on sequencing depth, and returns Pearson residuals that are approximately variance-stabilised and suitable for downstream PCA, integration and clustering.

## Intuition
Library-size scaling alone leaves heteroscedastic residuals; the GLM-based formulation flattens depth-dependent variance and corrects mean-variance trends without arbitrary log(1+x) heuristics.

## Key variants
- v1 (per-gene NB regression)
- v2 (glmGamPoi backend, faster, recommended)
- SCTransform with vars.to.regress for confounders

## Known limitations
- Computationally heavier than log-normalisation
- Variance stabilisation can over-flatten biologically important high-variance genes
- Sensitive to ambient RNA without prior decontamination

## Open problems
- Direct comparison with Pearson-residual-only alternatives across tasks
- Adaptation to spatial spot data with capture-area effects

## Relevance to active research
[[papers/spatial-transcriptomics-reveals-distinct-conserved-tumor]] uses SCTransform for per-sample ST normalisation before Seurat-based integration, dimensionality reduction and Louvain clustering.
