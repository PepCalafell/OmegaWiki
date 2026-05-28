---
title: "Mamba — selective state space model (SSM)"
slug: mamba-selective-state-space-model
domain: methods / deep-learning
status: mainstream
aliases:
  - Mamba
  - selective state space model
  - Bi-Mamba
  - SSM
  - state space model
first_introduced: "Gu & Dao 2024 (Mamba: linear-time sequence modeling with selective state spaces)"
date_updated: 2026-05-28
source_url: "https://arxiv.org/abs/2312.00752"
---

## Definition

Mamba is a selective state space model (SSM) for sequence modeling that achieves linear-time scaling in sequence length by making the SSM parameters input-dependent (selective), allowing the model to propagate or forget information content-dependently. It is a competitive alternative to attention for long sequences, with a hardware-aware parallel scan implementation.

## Intuition

Attention compares every token to every other (quadratic). An SSM instead maintains a compressed running state and updates it as it scans the sequence (linear). Making the update "selective" lets it choose what to keep, recovering much of attention's expressivity at lower cost.

## Formal notation

Continuous SSM: h'(t)=A h(t)+B x(t), y(t)=C h(t); discretized with step Δ; in Mamba B, C, Δ are functions of the input (selection). Bi-Mamba runs forward and backward scans.

## Key variants

- Unidirectional Mamba vs Bi-Mamba (bidirectional, used for non-causal data like gene sets).
- Mamba blocks interleaved with Transformer attention (hybrid).

## Known limitations

- On some tasks needing precise pairwise interactions, pure SSMs underperform attention; hybrids are often used.

## Open problems

- Optimal interleaving of SSM and attention; theoretical understanding of selectivity.

## Relevance to active research

AlphaCell's encoder interleaves Bi-Mamba and Transformer blocks (each with MoE) to capture long-range, genome-wide regulatory dependencies across 19,253 genes while keeping the genome-scale encoder tractable.
