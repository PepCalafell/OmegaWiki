---
title: "MrVI — multi-resolution variational inference for treatment effects in scRNA-seq"
slug: mrvi-multi-resolution-variational-inference
domain: "computational-biology / methods"
status: mainstream
aliases:
  - "MrVI"
  - "multi-resolution variational inference"
first_introduced: "Boyeau et al. 2024 Nat Methods"
date_updated: 2026-05-27
source_url: "https://github.com/YosefLab/mrvi"
---

## Definition

MrVI is a deep generative model that learns a treatment-aware latent representation of scRNA-seq cells. It estimates per-sample (or per-treatment) local distances between cells, enabling treatment-specific similarity networks, perturbation-aware module discovery, and quantification of differential responses across cellular states.

## Intuition

Standard scVI captures variation in gene expression. MrVI additionally factors in sample-level / treatment-level covariates, producing a "treatment-aware" embedding (z) where cells can be compared not just by transcriptional identity but also by how their state shifted under intervention.

## Key variants

- MrVI base model (sample-level)
- Treatment-grouped MrVI used in [[macrophage-targeted-immunocytokine-leverages-myeloid-nk]] for nine-arm ICI-vs-MiTE comparisons

## Known limitations

- Requires many samples per treatment for stable distances
- Sensitive to confounding (batch, donor) when those align with treatment
- Interpretability of latent dimensions remains heuristic

## Relevance to active research

Used to derive treatment clusters (Figure 5D) and module heatmaps (Figure 5H) in the MiTE paper, supporting the claim that MiTE-based treatments form a transcriptionally distinct cluster from αPD-1 / αCTLA-4 monotherapies.
