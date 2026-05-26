---
title: "mclust — Gaussian mixture model clustering in R"
slug: mclust-r
domain: "methods / clustering / statistics"
status: mainstream
aliases:
  - mclust
  - mclust R package
  - Scrucca mclust
  - model-based GMM clustering
  - Bayesian information criterion GMM
  - mclust spatial transcriptomics
first_introduced: "Scrucca, Fraley, Murphy & Raftery (Chapman & Hall/CRC, 2023)"
date_updated: 2026-05-26
source_url: ""
---

## Definition

mclust is the canonical R package for model-based Gaussian-mixture clustering, classification, and density estimation, using BIC to select between covariance structures and component counts.

## Strengths

- Principled probabilistic clustering with model selection.
- Standard downstream choice for spatial transcriptomics methods.

## Known limitations

- Sensitive to high-dimensional embeddings; usually preceded by PCA.
- Slow on million-cell datasets.

## Relevance to active research

External clustering dependency of STAGATE, SEDR, GraphST, SpaceFlow in benchmarks reported by [[papers/novae-graph-based-foundation-model-spatial]] and [[papers/cellcharter-reveals-spatial-cell-niches-associated]]; identified as a runtime bottleneck Novae bypasses.
