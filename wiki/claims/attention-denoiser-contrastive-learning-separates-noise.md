---
title: "Attention denoiser with contrastive learning separates noise, enabling robustness to unknown cell types"
slug: attention-denoiser-contrastive-learning-separates-noise
status: supported
confidence: 0.8
tags: [denoising, contrastive, attention, deconvolution]
domain: methods
source_papers:
  - decode-deep-learning-based-common-deconvolution
evidence:
  - source: decode-deep-learning-based-common-deconvolution
    type: supports
    strength: moderate
    detail: "Stage 3 self-attention denoiser produces mask matrices that split features into noise vs. purified train-tissue features; contrastive loss treats co-located train/purified features as positives and noise features as negatives."
conditions: "Mechanism validated qualitatively and by ablation (Supplementary Table 9)."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

DECODE's stage-3 attention-based denoiser, trained with a contrastive-learning strategy, separates noise from purified tissue features, which is the mechanism conferring robustness to incomplete references and measurement noise.

## Evidence summary

The denoiser generates mask matrices via self-attention that elementwise-separate noisy input into purified-train-tissue and noise features (Fig. 1e). Contrastive loss (Fig. 1f) pulls together co-located train/purified features (positives) and pushes apart noise features (negatives).

## Conditions and scope

A domain-specific use of [[contrastive-learning]]; underpins the "relative deconvolution" pathway used when unknown cell types are present.

## Counter-evidence

None reported.

## Linked ideas

## Open questions

How separation degrades as the unknown-cell fraction increases.
