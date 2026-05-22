---
title: "Average Silhouette Width (ASW) — clustering quality metric"
slug: silhouette-asw-metric
domain: "methods / clustering-metric / general"
status: mainstream
aliases:
  - ASW
  - average silhouette width
  - silhouette score
  - silhouette coefficient
  - Rousseeuw silhouette
  - cell-type ASW
  - batch ASW
  - scIB ASW
  - silhouette width clustering quality
  - silhouette metric single-cell
  - cluster compactness silhouette
first_introduced: "Rousseeuw 1987 *J. Comput. Appl. Math.* (Silhouettes: a graphical aid to the interpretation and validation of cluster analysis)"
date_updated: 2026-05-22
source_url: ""
---

## Definition

The silhouette width of a point measures how similar it is to its own cluster (cohesion) versus the next-nearest cluster (separation); the Average Silhouette Width (ASW) averages this across all points and lies in [-1, 1]. scIB uses two ASW variants: batch ASW (lower = better, batches well-mixed) and cell-type ASW (higher = better, cell types well-separated).

## Strengths

- Classical, well-understood, distribution-free.
- Works on any distance/dissimilarity (Euclidean for embeddings, graph distance for graphs).
- Captures both cohesion and separation in a single number.

## Known limitations

- Assumes convex / globular clusters — fails on continuous trajectories.
- Sensitive to distance-metric choice.

## Relevance to active research

ASW (batch + cell-type variants) is a standard scIB metric pair. See [[foundations/scib-benchmark-pipeline]] and [[papers/benchmarking-atlas-level-data-integration-single]].
