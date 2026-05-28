---
title: "ArcFace — additive angular margin loss"
slug: arcface-additive-angular-margin-loss
domain: methods / deep-learning
status: mainstream
aliases:
  - ArcFace
  - additive angular margin loss
  - angular margin softmax
first_introduced: "Deng et al. 2019 (ArcFace, CVPR)"
date_updated: 2026-05-28
source_url: "https://arxiv.org/abs/1801.07698"
---

## Definition

ArcFace is a classification loss, originally for face recognition, that operates on L2-normalized features and class weights and adds a fixed angular margin to the target-class angle before the softmax. This enforces larger angular separation between classes on the unit hypersphere, producing more discriminative, tightly clustered embeddings.

## Intuition

Plain softmax only needs classes to be linearly separable. ArcFace demands a geometric "safety margin" of angle between a sample and the wrong classes, so embeddings of the same class pack together and different classes spread apart.

## Formal notation

L = −log( e^{s·cos(θ_y+m)} / ( e^{s·cos(θ_y+m)} + Σ_{j≠y} e^{s·cosθ_j} ) ), with scale s, margin m, θ the angle between normalized feature and class weight.

## Key variants

- ArcFace (additive angular margin) vs CosFace (additive cosine margin) vs SphereFace (multiplicative).

## Known limitations

- Margin/scale hyperparameters are sensitive; aggressive margins can distort the embedding geometry if used without a reconstruction/regularization counterbalance.

## Open problems

- Adapting margin losses to continuous/soft labels and to unsupervised regimes.

## Relevance to active research

AlphaCell adds an ArcFace head during Stage-2 fine-tuning to sharpen separability of biological identities in the Virtual Cell Space, paired with a concurrent reconstruction objective so identity-shaping does not collapse transcriptomic detail.
