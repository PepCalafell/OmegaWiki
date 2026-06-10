---
title: "clustree — clustering resolution selection"
slug: clustree-clustering-resolution-selection
domain: "methods / clustering / single-cell"
status: mainstream
aliases:
  - clustree
  - cluster tree
first_introduced: "Zappia & Oshlack 2018, GigaScience"
date_updated: 2026-06-10
source_url: "https://doi.org/10.1093/gigascience/giy083"
---

## Definition

clustree visualizes how cells move between clusters as the clustering resolution parameter is swept across a range, drawing a tree whose nodes are clusters at each resolution and whose edges track cell reassignment. It is used to choose a resolution at which clusters are stable rather than fragmenting.

## Intuition

Increasing resolution splits clusters; clustree shows where splits are clean (one parent → two distinct children) versus where cells shuffle incoherently (many crossing edges), guiding selection of a biologically defensible cluster count.

## Known limitations

- Provides a heuristic, not an objective optimum; the final resolution choice is still subjective.
- Becomes visually cluttered at high resolution or many clusters.

## Relevance to active research

Commonly paired with [[louvain-community-detection-clustering]] and [[leiden-clustering]] to justify the chosen number of cell-type clusters in Seurat/Scanpy pipelines.
