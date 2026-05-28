---
title: "AlphaCell encoder is a Mamba-Transformer hybrid compressing the transcriptome to a 32x128 latent manifold"
slug: alphacell-encoder-mamba-transformer-hybrid-compressing
status: supported
confidence: 0.9
tags: [AlphaCell, encoder, Mamba, Transformer, latent-manifold, architecture]
domain: methods / single-cell
source_papers:
  - towards-building-world-model-simulate-perturbation
evidence:
  - source: towards-building-world-model-simulate-perturbation
    type: supports
    strength: strong
    detail: "Quote (p.6, p.21): '8 alternating blocks of Bi-Directional State Space Models (Bi-Mamba) and Transformer layers, both augmented with MoE ... the encoder utilizes adaptive pooling to forcefully compress the entire transcriptome into 32 continuous latent tokens, forming a 32x128 dimensional latent representation.'"
conditions: "Encoder input is 100x-tokenized 19,253-gene expression; latent organized as 32 coupled state channels."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

The AlphaCell encoder is a Mamba-Transformer hybrid (8 alternating Bi-Mamba + Transformer blocks, each with MoE) that adaptively pools the genome-wide input into 32 continuous latent tokens (32×128), acting as a manifold rectifier rather than a plain dimensionality compressor.

## Evidence summary

Reported in [[papers/towards-building-world-model-simulate-perturbation]]. Architecture foundations: [[foundations/mamba-selective-state-space-model]], [[foundations/mixture-experts-layer]]. Supports [[concepts/manifold-rectification-continuous-virtual-cell-space]].

## Conditions and scope

L2 regularization on latents during fine-tuning to enforce topological smoothness.

## Counter-evidence

No ablation isolating Mamba vs Transformer contribution reported in main text.

## Linked ideas

## Open questions

- How sensitive is performance to the 32-channel bottleneck width?
