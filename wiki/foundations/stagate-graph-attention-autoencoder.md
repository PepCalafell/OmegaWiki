---
title: "STAGATE — adaptive graph attention autoencoder for spatial domains"
slug: stagate-graph-attention-autoencoder
domain: "methods / spatial-transcriptomics / graph-neural-networks"
status: mainstream
aliases:
  - STAGATE
  - STAGATE graph attention autoencoder
  - Dong STAGATE
  - Zhang STAGATE
  - adaptive graph attention autoencoder spatial
  - STAGATE spatial domains
  - graph autoencoder spatial transcriptomics
first_introduced: "Dong & Zhang 2022 Nature Communications"
date_updated: 2026-05-26
source_url: "https://github.com/QIFEIDKN/STAGATE"
---

## Definition

STAGATE uses a graph-attention autoencoder over the cell/spot proximity graph to learn embeddings that respect spatial geometry. The decoder reconstructs gene expression, and attention weights adaptively rebalance contributions of nearby cells. Downstream clustering (typically mclust or Leiden) on these embeddings yields spatial domains.

## Strengths

- Strong single-sample performance on Visium DLPFC benchmarks.
- Adaptive attention handles heterogeneous neighborhood densities.

## Known limitations

- Reconstruction-based objective is less suited for cross-slide multi-panel integration.
- Requires external batch correction (e.g., Harmony) and external clustering (Leiden/mclust), creating downstream-tool bottlenecks.
- Memory cost grows quickly on million-cell datasets.

## Relevance to active research

Used as a primary benchmark comparator in [[papers/novae-graph-based-foundation-model-spatial]] and [[papers/cellcharter-reveals-spatial-cell-niches-associated]]; Novae argues that STAGATE is limited by its dependence on the intersection of gene panels and on external batch correction.
