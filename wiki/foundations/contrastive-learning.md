---
title: "Contrastive learning"
slug: contrastive-learning
domain: methods
status: mainstream
aliases:
  - contrastive representation learning
  - InfoNCE
first_introduced: "2018"
date_updated: 2026-05-28
source_url: ""
---

## Definition

A representation-learning paradigm that learns embeddings by pulling together "positive" pairs (views that should be similar) and pushing apart "negative" pairs (views that should differ) in latent space, typically via a cross-entropy / InfoNCE-style loss over similarities.

## Intuition

Without labels, a model can still learn useful structure by enforcing that related samples (e.g., two augmentations of the same input) land close together while unrelated samples land far apart, shaping a discriminative latent geometry.

## Formal notation

For an anchor with positive z+ and negatives {z−}, minimize −log [ exp(sim(z,z+)/τ) / Σ exp(sim(z,z·)/τ) ], where sim is cosine similarity and τ a temperature.

## Key variants

- SimCLR / MoCo (self-supervised vision).
- Supervised contrastive learning.
- Feature-level contrast for denoising (positive = same-position purified feature, negative = noise feature, as in DECODE).

## Known limitations

- Sensitive to choice of positive/negative pairing and temperature; needs many negatives.

## Open problems

Principled pair construction for structured biological data.

## Relevance to active research

Used in DECODE stage 3 to separate purified tissue features from noise features (positives = co-located train-tissue/purified features; negatives = noise features), conferring robustness to incomplete references.
