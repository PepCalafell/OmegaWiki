---
title: "Leiden clustering — community detection on kNN graphs"
slug: leiden-clustering
domain: "methods / clustering / single-cell"
status: mainstream
aliases:
  - Leiden
  - Leiden algorithm
  - Leiden community detection
  - Traag Leiden
  - Louvain to Leiden
  - modularity-based clustering
  - graph community detection single-cell
  - well-connected community detection
  - leidenalg
first_introduced: "Traag, Waltman & van Eck 2019 Scientific Reports"
date_updated: 2026-05-26
source_url: ""
---

## Definition

Leiden is a community-detection algorithm that improves on Louvain by guaranteeing well-connected communities and faster convergence. It is the de-facto clustering primitive for single-cell genomics, typically applied to kNN graphs built on PCA-reduced or integrated embeddings.

## Strengths

- Guarantees well-connected communities (no internal disconnection bug of Louvain).
- Resolution parameter allows control of cluster granularity.

## Known limitations

- Resolution selection is heuristic; must be re-run for every desired cluster count, a major bottleneck flagged in [[papers/novae-graph-based-foundation-model-spatial]].
- Sensitive to graph construction.

## Relevance to active research

Used downstream of nearly every scRNA-seq and spatial transcriptomics method to derive cluster labels; Novae argues that depending on Leiden becomes the time bottleneck for million-cell datasets and replaces it with prototype-based assignment.
