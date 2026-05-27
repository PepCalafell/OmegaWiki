---
title: "NCEM — Niche Cell-cell Effect Model"
slug: ncem-niche-cell-effect-model
domain: "methods / spatial-transcriptomics / cell-cell-interaction"
status: mainstream
aliases:
  - "NCEM"
first_introduced: "Fischer et al. Nat Biotechnol 2023"
date_updated: 2026-05-27
source_url: "https://github.com/theislab/ncem"
---

## Definition

NCEM is a graph-neural-network framework that explains intra-cell-type gene-expression variance as a linear (or non-linear) function of the niche composition surrounding each cell, modeled as a multivariate cell-type vector at varying spatial radii. It outputs niche-induced gene-expression coupling matrices per cell type.

## Intuition

The closest conceptual peer to NiCo: both decompose intra-cell-type variability as a function of neighboring cell-type identities. NCEM is gene-level; NiCo is latent-factor-level and explicitly leverages a paired scRNA-seq modality for transcriptome-wide interpretation of the small spatial-panel gene set.

## Known limitations

- Restricted to genes directly measured in the spatial panel.
- Not designed to detect cell-state covariation across pairs of distinct cell types — focus is on niche-driven variance within one cell type.

## Relevance to active research

Reference comparator for any new spatial cell-state/niche analysis tool, including NiCo.
