---
title: "qgraph — correlation network visualization"
slug: qgraph-network-visualization
domain: "methods / network biology / visualization"
status: mainstream
aliases:
  - qgraph
first_introduced: "Epskamp et al. 2012, Journal of Statistical Software"
date_updated: 2026-06-10
source_url: "https://doi.org/10.18637/jss.v048.i04"
---

## Definition

qgraph is an R package for visualizing weighted networks, most commonly correlation networks where nodes are variables (e.g. genes) and edges are pairwise correlations. Node layout is typically computed with a force-directed algorithm (Fruchterman-Reingold), placing strongly correlated nodes near each other.

## Intuition

Turning a gene-gene correlation matrix into a spring-layout graph makes co-regulated gene modules visually apparent as tightly clustered, strongly connected groups.

## Known limitations

- Force-directed layouts are stochastic and aesthetic; spatial proximity is suggestive, not a rigorous statistic.
- Dense correlation matrices need thresholding to be legible, which can hide weak structure.

## Relevance to active research

Used to display transcriptional co-expression structure of DEG signatures (e.g. segregation of disease-specific gene modules) alongside formal tests such as STRING-based normalized-cut analysis.
