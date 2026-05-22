---
title: "trVAE — conditional out-of-distribution VAE for unpaired single-cell data"
slug: trvae-conditional-vae
domain: "methods / single-cell-integration / deep-learning"
status: mainstream
aliases:
  - trVAE
  - transfer VAE
  - Lotfollahi trVAE
  - conditional out-of-distribution VAE
  - unpaired single-cell VAE
  - trVAE integration
  - Theis trVAE
  - conditional VAE scRNA-seq
  - MMD VAE single-cell
  - trvae perturbation modelling
first_introduced: "Lotfollahi et al. 2020 *Bioinformatics* (Conditional out-of-distribution generation for unpaired data using transfer VAE)"
date_updated: 2026-05-22
source_url: "https://github.com/theislab/trvae"
---

## Definition

trVAE is a conditional VAE with maximum mean discrepancy (MMD) regularization, designed for out-of-distribution generation across unpaired single-cell data (e.g. perturbation prediction). It can be repurposed for integration by conditioning on batch.

## Strengths

- Conditional generation supports perturbation modelling and counterfactual analysis.
- Joint embedding output suitable for downstream analysis.

## Known limitations

- Cannot scale beyond ~34k cells without GPU — see [[claims/scvi-scales-trvae-scgen-fail]].
- Underperforms scVI/scANVI on scIB integration benchmark (optimized for perturbation, not integration).
- Tutorial defaults not optimal for integration tasks.

## Relevance to active research

trVAE is primarily a perturbation-prediction tool; for integration use scVI/scANVI. Relevant to cytokine-perturbation atlas modelling. Validated in [[papers/benchmarking-atlas-level-data-integration-single]].
