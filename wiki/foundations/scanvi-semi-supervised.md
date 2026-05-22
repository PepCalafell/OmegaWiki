---
title: "scANVI — semi-supervised single-cell ANnotation using Variational Inference"
slug: scanvi-semi-supervised
domain: "methods / single-cell-integration / deep-learning"
status: mainstream
aliases:
  - scANVI
  - scANVI integration
  - single-cell annotation VAE
  - semi-supervised scVI
  - Xu scANVI
  - cell-label-aware scVI
  - probabilistic single-cell annotation
  - scANVI label transfer
  - scvi-tools scANVI
  - semi-supervised single-cell integration
  - scANVI atlas integration
first_introduced: "Xu et al. 2021 *Mol. Syst. Biol.* (Probabilistic harmonization and annotation of single-cell transcriptomics data)"
date_updated: 2026-05-22
source_url: "https://github.com/scverse/scvi-tools"
---

## Definition

scANVI extends scVI with a semi-supervised classification head that incorporates partial cell-type labels into the variational objective. The result is an integration method that exploits known annotations to preserve biological cell-state variation while removing batch effects. It can predict labels for unannotated cells and is the recommended scvi-tools method when at least some cell-type labels are available.

## Strengths

- Top performer on scIB RNA tasks when labels available — see [[claims/scanvi-scanorama-scvi-top-rna-integration]] and [[claims/cell-label-integration-methods-win-with-labels]].
- Preserves cell-state differences present in only a single batch (a feature only label-aware methods can achieve).
- Inherits scVI scalability and probabilistic interpretability.
- Among the most memory-efficient methods in scIB — see [[claims/combat-bbknn-fastest-scvi-low-memory]].

## Known limitations

- Quality of integration depends on label quality and granularity — coarse labels collapse advantage.
- Cannot escape the batch-removal-vs-bio-conservation tradeoff if labels do not encode the biological variation of interest.
- Tutorial defaults used; per-task hyperparameter tuning is rare in practice.

## Relevance to active research

scANVI is the recommended integration choice for atlas construction when per-batch annotations exist (e.g. immune-cell atlases, heart atlas of Litviňuková et al. 2020). Highly relevant for TAM / immune-cell atlas work where MoMac-VERSE annotations could seed scANVI integration. Foundational benchmark: [[papers/benchmarking-atlas-level-data-integration-single]].
