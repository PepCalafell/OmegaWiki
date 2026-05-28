---
title: "DECODE uses a four-stage adversarial and contrastive deconvolution architecture"
slug: decode-uses-four-stage-adversarial-contrastive
status: supported
confidence: 0.9
tags: [deconvolution, architecture, deep-learning]
domain: methods
source_papers:
  - decode-deep-learning-based-common-deconvolution
evidence:
  - source: decode-deep-learning-based-common-deconvolution
    type: supports
    strength: strong
    detail: "Stage 1 pseudotissue generation; stage 2 adversarial batch-effect removal (encoder/discriminator/eDeconvolver, L1 + BCE); stage 3 contrastive denoising (DimExpander, attention denoiser, linear attention, contrastive loss); stage 4 inference with two pathways."
conditions: "Architectural description from Methods/Fig. 1."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

DECODE consists of four stages: (1) pseudotissue training-data generation, (2) adversarial batch-effect removal, (3) contrastive-learning denoising with self-attention, and (4) inference with two pathways (standard vs. relative deconvolution).

## Evidence summary

Described in Methods and Fig. 1a–f. Stage 2 trains encoder, discriminator and eDeconvolver with L1 + binary-cross-entropy loss; stage 3 adds a DimExpander, an attention-based denoiser and contrastive loss; stage 4 selects the denoiser pathway when unknown cell types are present.

## Conditions and scope

Descriptive (mechanistic) claim about the model design.

## Counter-evidence

None.

## Linked ideas

## Open questions

Relative contribution of each stage is addressed by ablation (Supplementary Table 9) but only summarized in the main text.
