---
title: "PageRank algorithm"
slug: pagerank-algorithm
domain: methods
status: mainstream
aliases: ["PageRank", "personalized PageRank", "PPR", "network centrality PageRank", "PageRank node importance"]
first_introduced: "1998"
date_updated: 2026-05-22
source_url: "http://infolab.stanford.edu/~backrub/google.html"
---

## Definition

Iterative graph-centrality algorithm that assigns an importance score to each node based on the quantity and quality of incoming edges, originally developed for web-page ranking. Personalized PageRank biases the random restart towards seed nodes.

## Relevance to active research

- Core score in the Taiji TF-activity pipeline: a personalized PageRank is computed over the gene regulatory network to rank TFs by global regulatory influence, integrating chromatin accessibility, motif binding, and expression.
- Choice of PageRank reflects that TF function depends on upstream regulators, downstream targets, and feedback loops, not just expression level.
