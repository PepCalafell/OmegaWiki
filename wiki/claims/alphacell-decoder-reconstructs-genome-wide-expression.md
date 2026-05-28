---
title: "AlphaCell decoder reconstructs genome-wide expression at ROC-AUC > 0.96, Pearson > 0.7, MAE < 0.25"
slug: alphacell-decoder-reconstructs-genome-wide-expression
status: supported
confidence: 0.85
tags: [AlphaCell, decoder, reconstruction-fidelity, MoE, genome-wide, quantitative]
domain: methods / single-cell
source_papers:
  - towards-building-world-model-simulate-perturbation
evidence:
  - source: towards-building-world-model-simulate-perturbation
    type: supports
    strength: strong
    detail: "Quote (p.9): 'any valid cell state embedding within the manifold can be translated into a biologically accurate genome-wise expression profile with high precision (ROC-AUC > 0.96, Pearson > 0.7, MAE < 0.25).'"
conditions: "1.2B-parameter MoE decoder translating 32x128 latent back to 19,253-gene profile."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

The massive MoE "observation interface" decoder reconstructs the full 19,253-gene expression profile from the compressed Virtual Cell Space embedding with reported ROC-AUC > 0.96, Pearson > 0.7, and MAE < 0.25, used as evidence that the latent space preserves comprehensive cell state.

## Evidence summary

Reported in [[papers/towards-building-world-model-simulate-perturbation]]. See [[foundations/mixture-experts-layer]] and concept [[concepts/manifold-rectification-continuous-virtual-cell-space]].

## Conditions and scope

Reconstruction metrics; specific dataset/split for these numbers not fully detailed in main text.

## Counter-evidence

Aggregate thresholds reported rather than per-dataset distributions; self-reported.

## Linked ideas

## Open questions

- Are reconstruction metrics uniform across rare cell types, or dominated by abundant lineages?
