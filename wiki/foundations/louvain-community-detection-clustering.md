---
title: "Louvain community detection clustering"
slug: louvain-community-detection-clustering
domain: "methods / clustering / single-cell"
status: mainstream
aliases:
  - Louvain
  - Louvain algorithm
  - Louvain community detection
  - modularity optimization clustering
first_introduced: "Blondel et al. 2008, J. Stat. Mech."
date_updated: 2026-06-10
source_url: "https://doi.org/10.1088/1742-5468/2008/10/P10008"
---

## Definition

Louvain is a greedy modularity-optimization algorithm for detecting communities in graphs. In single-cell analysis it is applied to a k-nearest-neighbor cell graph to partition cells into clusters; a resolution parameter tunes cluster granularity. It is Seurat's default `FindClusters` algorithm.

## Intuition

It iteratively moves nodes between communities to maximize modularity (more within-community edges than expected at random), then collapses communities into super-nodes and repeats — fast and scalable to large cell graphs.

## Known limitations

- Can produce internally disconnected communities (the defect [[leiden-clustering]] was designed to fix).
- Resolution must be chosen heuristically (e.g. via clustree); different resolutions yield different cluster counts with no objective optimum.

## Open problems

- Principled, data-driven resolution selection remains unsolved.

## Relevance to active research

The historical default clustering primitive for Seurat-based scRNA-seq pipelines; increasingly superseded by [[leiden-clustering]] but still widely used in published 10x analyses.
