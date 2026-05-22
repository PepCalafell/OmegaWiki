---
title: "BBKNN — Batch-Balanced k-Nearest Neighbors graph integration"
slug: bbknn-integration
domain: "methods / single-cell-integration"
status: mainstream
aliases:
  - BBKNN
  - Batch-Balanced k Nearest Neighbors
  - bbknn batch correction
  - Polanski BBKNN
  - bbknn graph integration
  - Teichmann BBKNN
  - BBKNN scanpy
  - graph-output scRNA-seq integration
  - batch-balanced kNN graph
  - fast scRNA-seq integration graph method
first_introduced: "Polański et al. 2019 *Bioinformatics* (BBKNN: fast batch alignment of single cell transcriptomes)"
date_updated: 2026-05-22
source_url: "https://github.com/Teichlab/bbknn"
---

## Definition

BBKNN constructs an integrated nearest-neighbor graph by, for each cell, selecting its k nearest neighbors *per batch* and combining them into a single batch-balanced graph. The output is not a corrected gene matrix or an embedding but an integrated kNN graph suitable for downstream Leiden clustering, UMAP embedding, and pseudotime.

## Strengths

- Extremely fast and memory-efficient — appears in both fastest and lowest-memory lists — see [[claims/combat-bbknn-fastest-scvi-low-memory]].
- Scales to atlas size without bottlenecks.
- Trivially integrates with scanpy Leiden / UMAP downstream.
- Strong batch removal on RNA tasks.

## Known limitations

- Prioritizes batch removal at the cost of bio-conservation — see [[claims/batch-removal-vs-bioconservation-tradeoff]].
- No gene-level corrected output and no continuous embedding (only an integrated graph).
- Optimization function similar to graph iLISI metric — risk of overfitting that metric (though scIB shows BBKNN does not unilaterally dominate batch metrics).

## Relevance to active research

BBKNN is the fast-exploratory default for atlas-scale integration when only graph-based downstream analysis is required. Validated in [[papers/benchmarking-atlas-level-data-integration-single]].
