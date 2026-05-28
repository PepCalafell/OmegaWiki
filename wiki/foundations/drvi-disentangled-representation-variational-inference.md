---
title: "DRVI — Disentangled Representation Variational Inference"
slug: drvi-disentangled-representation-variational-inference
domain: "methods"
status: mainstream
aliases:
  - "DRVI"
  - "Disentangled Representation Variational Inference"
first_introduced: "Moinfar & Theis 2024/2025"
date_updated: 2026-05-28
source_url: "https://github.com/theislab/drvi"
---

## Definition

A deep generative model for single-cell data that learns a disentangled latent representation in which each latent dimension maps to a largely exclusive set of genes. DRVI builds on the variational autoencoder framework but modifies the decoder so that individual latent factors correspond to interpretable, additive gene programs rather than entangled mixtures.

## Intuition

Standard VAEs (e.g. [[scvi-deep-generative-model]]) produce powerful but entangled latent spaces where no single dimension has a clean biological meaning. DRVI constrains the decoder so each latent axis can be read off as a distinct gene module — making the factors directly interpretable as biological programs. In the Human Cytokine Dictionary it is used to decompose cytokine-perturbed expression into 82 cytokine-induced immune programs (CIPs).

## Key variants

- Linear-decoder disentanglement variant
- Non-linear DRVI with per-dimension gene attribution

## Known limitations

- Manual expert annotation still required to label each latent factor biologically
- Number of programs is a model hyperparameter / interpretation choice
- Disentanglement is approximate, not guaranteed exclusive

## Open problems

- Automatic biological annotation of latent factors
- Stability of programs across datasets and batches
- Causal vs correlational interpretation of latent gene modules

## Relevance to active research

Method behind the CIP catalog of the [[human-cytokine-dictionary-dataset]]. A Theis-lab interpretable-latent method in the same family as scVI / scGen / CPA. Useful for any project decomposing perturbation responses into interpretable modules.
