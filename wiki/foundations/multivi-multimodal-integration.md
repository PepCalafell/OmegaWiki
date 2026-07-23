---
title: "MultiVI — deep generative model for multimodal single-cell/spatial integration"
slug: "multivi-multimodal-integration"
domain: "computational biology / multi-omics integration"
status: mainstream
aliases:
  - "MultiVI"
  - "MultiVI scvi-tools"
first_introduced: "2023"
date_updated: 2026-07-23
source_url: "https://doi.org/10.1038/s41592-023-01909-9"
---

## Definition

MultiVI is a variational-autoencoder model (in the scvi-tools family) that learns a shared low-dimensional latent space from cells or spots profiled by more than one modality — and, critically, from cells/spots measured by only one modality — imputing the missing modality and enabling joint analysis. It handles batch and modality effects as covariates.

## Intuition

When a tissue is measured by transcriptomics on some spots and metabolomics on others (plus a few paired), MultiVI stitches them into one coordinate system by learning what a "complete" spot looks like, so downstream niche clustering can use both gene and metabolite information even where one was not directly measured.

## Formal notation

Encoders map each spot's observed modalities to a joint latent z; decoders reconstruct each modality. Training maximises a modality-aware evidence lower bound with `modality` as batch key and `sample` as categorical covariate; latent dimension is a set hyperparameter (e.g. `n_latent = 30`).

## Key variants

- Built on the scVI / totalVI / PeakVI probabilistic framework ([[scvi-deep-generative-model]]).
- Applied here to spatial transcriptomics + spatial metabolomics rather than the original RNA + ATAC use case.

## Known limitations

- Imputation quality degrades when the paired (jointly measured) fraction is small.
- Latent embeddings are model- and hyperparameter-dependent; interpretation requires downstream validation.
- Assumes modalities share underlying biological structure recoverable in a common latent space.

## Open problems

- Principled uncertainty on imputed modalities.
- Extending to more than two modalities with heterogeneous noise models.

## Relevance to active research

MultiVI produced the joint transcriptomic–metabolomic embedding that, fed into [[cellcharter-framework]], defined the spatial niches distinguishing glycolysis/angiogenic regions from MHC-II-high FAO regions in human NSCLC.
