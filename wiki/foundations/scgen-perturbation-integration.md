---
title: "scGen — generative VAE for perturbation modelling and label-aware integration"
slug: scgen-perturbation-integration
domain: "methods / single-cell-integration / perturbation-modelling"
status: mainstream
aliases:
  - scGen
  - scGen integration
  - Lotfollahi scGen
  - perturbation VAE single-cell
  - label-aware scRNA-seq integration
  - scGen Theis
  - generative perturbation single-cell
  - scgen batch correction
  - cell-label conditioned VAE
  - scGen predicts perturbation responses
first_introduced: "Lotfollahi et al. 2019 *Nat. Methods* (scGen predicts single-cell perturbation responses)"
date_updated: 2026-05-22
source_url: "https://github.com/theislab/scgen"
---

## Definition

scGen is a generative VAE designed primarily to predict single-cell perturbation responses by learning a label-conditioned latent space; it doubles as a label-aware integration method. Cells of the same labelled cell type across batches are aligned via latent-space subtraction of batch effect vectors. Requires cell-type labels at training time.

## Strengths

- Top-performing method on scIB when label availability and gene-corrected output are needed — see [[claims/scanvi-scanorama-scvi-top-rna-integration]] and [[claims/cell-label-integration-methods-win-with-labels]].
- One of two methods (with scANVI) that preserve single-batch cell states.
- Gene-corrected output supports trajectory and functional analysis.

## Known limitations

- Fails to scale to 1M-cell mouse-brain task within 4-day CPU budget — see [[claims/scvi-scales-trvae-scgen-fail]].
- Requires high-quality cell labels; bad labels degrade integration sharply.
- Removes spatial / nuanced biological variation when labels do not encode it (e.g. lung endothelial spatial location).

## Relevance to active research

scGen is the recommended choice for perturbation-response prediction tasks (e.g. cytokine atlas modelling) and for label-aware integration on datasets below ~100k cells. Closely related to the Theis-lab compositional perturbation autoencoder (CPA). Validated in [[papers/benchmarking-atlas-level-data-integration-single]].
