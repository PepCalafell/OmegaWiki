---
title: "scVI — single-cell variational inference"
slug: scvi-deep-generative-model
domain: "methods / single-cell-integration / deep-learning"
status: mainstream
aliases:
  - scVI
  - single-cell variational inference
  - scVI integration
  - scvi-tools
  - Lopez scVI
  - VAE for scRNA-seq
  - probabilistic single-cell model
  - scVI normalization
  - scVI batch correction
  - deep generative scRNA-seq model
  - negative binomial VAE single cell
  - scVI Bayesian model
first_introduced: "Lopez et al. 2018 *Nat. Methods* (Deep generative modeling for single-cell transcriptomics)"
date_updated: 2026-05-22
source_url: "https://github.com/scverse/scvi-tools"
---

## Definition

scVI (single-cell variational inference) is a deep generative model for single-cell RNA-seq data that learns a Bayesian latent representation of cells while explicitly modelling batch covariates, library size, and a negative-binomial count distribution. Trained as a variational autoencoder, it produces a batch-corrected low-dimensional embedding suitable for atlas-level integration. It is the basis for an entire model family (scANVI, totalVI, MultiVI, peakVI, gimVI, destVI) implemented in scverse / scvi-tools.

## Strengths

- Atlas-scale: dataset-size-independent runtime via training-epoch scaling heuristic — see [[claims/scvi-scales-trvae-scgen-fail]].
- Probabilistic outputs: latent posterior, normalized expression, differential expression.
- Top-3 method on scIB RNA tasks — see [[claims/scanvi-scanorama-scvi-top-rna-integration]].
- Foundation for reference-mapping (scArches) and multi-modal extensions.
- Low memory footprint (top-3 most memory efficient) — see [[claims/combat-bbknn-fastest-scvi-low-memory]].

## Known limitations

- Underfits on very small datasets where deep-learning capacity is wasted.
- Requires hyperparameter tuning for optimal performance; tutorial defaults are reasonable but not task-optimal.
- Negative-binomial assumption violates on full-length protocols (Smart-seq2) and binary scATAC-seq counts — though empirically tolerable.

## Relevance to active research

scVI is one of the de-facto default integration methods for atlas-scale scRNA-seq integration in the Theis lab and the Human Cell Atlas community — used as the reference embedding for projection in scArches. Validated as top-tier in [[papers/benchmarking-atlas-level-data-integration-single]].
