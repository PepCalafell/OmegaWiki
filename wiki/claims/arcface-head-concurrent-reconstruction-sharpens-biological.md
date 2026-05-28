---
title: "ArcFace head with concurrent reconstruction sharpens biological identity separability without collapsing transcriptomic detail"
slug: arcface-head-concurrent-reconstruction-sharpens-biological
status: supported
confidence: 0.8
tags: [AlphaCell, ArcFace, fine-tuning, latent-structure, reconstruction]
domain: methods / single-cell
source_papers:
  - towards-building-world-model-simulate-perturbation
evidence:
  - source: towards-building-world-model-simulate-perturbation
    type: supports
    strength: strong
    detail: "Quote (p.7): 'we integrated an ArcFace head to perform explicit cell assignment and clustering, imposing angular margins to maximize the separability of distinct biological identities ... a concurrent unmasked reconstruction objective is maintained alongside ArcFace and DANN ... This ensures that the aggressive structural shaping and batch-correction do not collapse essential transcriptomic details.'"
conditions: "Stage-2 fine-tuning combines ArcFace + DANN + unmasked reconstruction."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

During fine-tuning AlphaCell adds an ArcFace angular-margin head to maximize separability of biological identities, while a concurrent unmasked reconstruction loss prevents the aggressive identity-shaping and batch-correction from collapsing essential transcriptomic detail.

## Evidence summary

Reported in [[papers/towards-building-world-model-simulate-perturbation]]. Method: [[foundations/arcface-additive-angular-margin-loss]]; complements [[claims/channel-wise-dann-strips-batch-signatures]].

## Conditions and scope

Two-stage curriculum: Stage 1 MLM + reconstruction; Stage 2 ArcFace + DANN + reconstruction.

## Counter-evidence

No ablation isolating ArcFace contribution reported in main text.

## Linked ideas

## Open questions

- How much does ArcFace separability help downstream perturbation flow accuracy?
