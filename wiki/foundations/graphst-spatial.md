---
title: "GraphST — spatially informed clustering, integration & deconvolution"
slug: graphst-spatial
domain: "methods / spatial-transcriptomics / contrastive-learning"
status: mainstream
aliases:
  - GraphST
  - Long GraphST
  - graph contrastive spatial transcriptomics
  - GraphST contrastive learning
  - spatial contrastive clustering
  - GraphST integration
first_introduced: "Long et al. 2023 Nature Communications"
date_updated: 2026-05-26
source_url: "https://github.com/JinmiaoChenLab/GraphST"
---

## Definition

GraphST is a graph contrastive-learning method for spatial transcriptomics that learns spot/cell embeddings respecting both gene expression and spatial neighborhoods, with downstream clustering, integration across slides, and cell-type deconvolution.

## Strengths

- Joint embedding+integration framework.
- Demonstrated competitive performance on Visium tasks.

## Known limitations

- Requires shared gene panels across slides (or panel intersection), restricting cross-technology use.
- Relies on external clustering and batch correction tools at downstream steps.

## Relevance to active research

Primary benchmark comparator in [[papers/novae-graph-based-foundation-model-spatial]], where it must be either trained per-slide (limited gene-panel intersection) or on a heavily reduced gene set.
