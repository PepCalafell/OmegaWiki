---
title: "UMAP — Uniform Manifold Approximation and Projection"
slug: umap-dimensionality-reduction
domain: "methods / dimensionality reduction / visualization"
status: mainstream
aliases:
  - UMAP
  - Uniform Manifold Approximation and Projection
first_introduced: "McInnes, Healy & Melville 2018, arXiv:1802.03426"
date_updated: 2026-06-10
source_url: "https://arxiv.org/abs/1802.03426"
---

## Definition

UMAP is a nonlinear dimensionality-reduction technique that constructs a fuzzy topological representation of high-dimensional data and optimizes a low-dimensional embedding to preserve that structure. In single-cell genomics it is the default 2D layout for visualizing cell-type structure, typically computed on a PCA-reduced or batch-corrected embedding.

## Intuition

It assumes data lie on a manifold and tries to keep neighbors-of-neighbors close in 2D, trading exact global distances for readable local cluster structure — usually faster and with better global structure than t-SNE.

## Known limitations

- Inter-cluster distances and cluster sizes in a UMAP are not quantitatively meaningful and can mislead.
- Sensitive to `n_neighbors` and `min_dist`; embeddings are stochastic and should not be over-interpreted as trajectories.

## Open problems

- Quantitative, reproducible interpretation of embedding geometry remains contested.

## Relevance to active research

The standard visualization output of essentially every scRNA-seq, CITE-seq, and spatial pipeline in the corpus, computed downstream of integration (Harmony, scVI) and neighbor-graph construction.
