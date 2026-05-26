---
title: "SwAV — Swapping Assignments between Views (self-supervised learning)"
slug: swav-self-supervised-framework
domain: "methods / self-supervised-learning / representation-learning"
status: mainstream
aliases:
  - SwAV
  - Swapping Assignments between Views
  - SwAV framework
  - Caron SwAV
  - swapped prediction self-supervision
  - online clustering self-supervised
  - prototype-based self-supervised learning
  - cluster-assignment SSL
  - Sinkhorn-Knopp swapped assignment
  - SwAV vision representation
first_introduced: "Caron et al. 2020 NeurIPS"
date_updated: 2026-05-26
source_url: "https://arxiv.org/abs/2006.09882"
---

## Definition

SwAV is a self-supervised learning framework introduced by Caron et al. (2020) for visual representation learning. Two augmented views of an input are encoded; each is projected onto a set of learnable cluster centroids (prototypes); the codes assigned by an optimal-transport-based Sinkhorn-Knopp algorithm to one view are predicted from the other view's features (the "swapped" prediction task). This avoids both the need for explicit negative pairs (unlike SimCLR/MoCo) and the need for input reconstruction (unlike autoencoders).

## Workflow

1. Two augmented views of the input are encoded into feature vectors `z1`, `z2`.
2. Features are projected onto K learnable prototypes giving soft assignments `q1`, `q2` via Sinkhorn-Knopp optimal transport (equipartition constraint).
3. Cross-entropy loss predicts `q2` from `z1` and `q1` from `z2` ("swapped" prediction).
4. Prototypes and encoder are trained jointly end-to-end.

## Strengths

- No negative pairs, no large memory bank.
- Optimal-transport assignment prevents trivial collapse to a single prototype.
- Prototypes naturally provide a discrete codebook usable for downstream clustering.

## Known limitations

- Requires careful tuning of the number of prototypes and the Sinkhorn-Knopp temperature.
- Equipartition assumption can be too strong when batch composition is very uneven (mitigated in Novae by relaxing it).

## Relevance to active research

Adapted to graph-structured spatial transcriptomics data in [[papers/novae-graph-based-foundation-model-spatial]], where the equipartition constraint is relaxed to allow slide-specific prototype absences and the swapped-assignment objective drives batch-invariant spatial-domain embeddings.
