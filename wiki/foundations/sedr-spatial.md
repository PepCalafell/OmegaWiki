---
title: "SEDR — spatially embedded deep representation"
slug: sedr-spatial
domain: "methods / spatial-transcriptomics / deep-learning"
status: mainstream
aliases:
  - SEDR
  - Xu SEDR
  - spatially embedded deep representation
  - SEDR autoencoder spatial
  - SEDR Visium clustering
first_introduced: "Xu et al. 2024 Genome Medicine (originally bioRxiv 2021)"
date_updated: 2026-05-26
source_url: "https://github.com/JinmiaoChenLab/SEDR"
---

## Definition

SEDR jointly learns gene-expression embeddings and spatial coordinates with a deep autoencoder + graph autoencoder hybrid, producing latent representations for spatial-domain identification on Visium and similar platforms.

## Strengths

- Joint expression + spatial embedding.
- Competitive on Visium DLPFC.

## Known limitations

- Memory-heavy on millions of cells.
- Requires external batch correction (Harmony) and clustering for multi-slide analysis.

## Relevance to active research

Benchmark comparator in [[papers/novae-graph-based-foundation-model-spatial]] and [[papers/cellcharter-reveals-spatial-cell-niches-associated]].
