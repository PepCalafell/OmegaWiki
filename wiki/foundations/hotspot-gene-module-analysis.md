---
title: "Hotspot — gene module analysis on scRNA-seq latent embeddings"
slug: hotspot-gene-module-analysis
domain: "computational-biology / methods"
status: mainstream
aliases:
  - "Hotspot"
  - "Hotspot gene modules"
first_introduced: "DeTomaso & Yosef 2021 Cell Systems"
date_updated: 2026-05-27
source_url: "https://github.com/YosefLab/Hotspot"
---

## Definition

Hotspot is a method for identifying informative genes and coherent gene modules from scRNA-seq data based on local autocorrelation in a chosen latent metric space (e.g., a kNN graph built on scVI or MrVI embeddings). It detects genes whose expression varies smoothly along the embedding and clusters them into modules.

## Intuition

If two cells are close in the latent space, biologically meaningful genes should also be similar between them. Hotspot finds genes whose expression respects this proximity (autocorrelated) and groups them into modules that map onto biological programmes (proliferation, IFN response, etc.).

## Key variants

- Hotspot on scVI / MrVI / PCA embeddings — variable by metric choice
- Treatment-aware Hotspot — using MrVI latent z to capture treatment-induced modules (as in [[macrophage-targeted-immunocytokine-leverages-myeloid-nk]])

## Known limitations

- Strongly dependent on the choice of latent embedding
- Modules can conflate co-regulated programs that share environments
- Numerical scaling and normalization issues for very large datasets

## Relevance to active research

Used in [[macrophage-targeted-immunocytokine-leverages-myeloid-nk]] to derive macrophage MrVI module heatmaps revealing FcγR signaling, proliferation, Trem2 program, IFN response, inflammatory, hypoxia, and monocyte-like programs across treatment arms.
