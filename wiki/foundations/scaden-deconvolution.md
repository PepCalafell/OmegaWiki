---
title: "Scaden — deep-learning bulk deconvolution from simulated tissue"
slug: scaden-deconvolution
domain: methods
status: mainstream
aliases:
  - Scaden
first_introduced: "2020"
date_updated: 2026-05-28
source_url: "https://doi.org/10.1126/sciadv.aba2619"
---

## Definition

Scaden (Single-cell-assisted deconvolutional network) is a deep neural network that predicts cell-type proportions from bulk RNA-seq. It is trained on pseudobulk samples simulated by mixing single cells at known random proportions, so the network learns the mapping from expression profile to composition without an explicit signature matrix.

## Intuition

Rather than solving a regression against a fixed signature, Scaden learns deconvolution as a supervised regression problem on simulated mixtures, letting a multilayer perceptron capture nonlinear relationships between expression and proportion.

## Formal notation

Ensemble of MLPs trained on simulated pseudobulk (mixture of single cells with known proportion vector p) to regress p from the aggregated expression profile.

## Key variants

- Ensemble averaging over networks of different depths for stability.

## Known limitations

- Transcriptomics-focused; no batch-effect alignment between simulated training data and real target tissue.
- Examined but did not resolve the unknown-cell-type problem.
- Single-omics.

## Open problems

Cross-platform and cross-omics generalization; robustness to references missing cell types.

## Relevance to active research

A widely used deep-learning deconvolution baseline and the conceptual predecessor of simulation-trained frameworks like DECODE, which adds adversarial batch alignment and contrastive denoising on top of the pseudobulk-training idea.
