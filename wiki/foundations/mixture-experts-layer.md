---
title: "Mixture-of-Experts (MoE) layer"
slug: mixture-experts-layer
domain: methods / deep-learning
status: mainstream
aliases:
  - Mixture-of-Experts
  - MoE
  - sparsely-gated mixture of experts
  - shared and routed MoE
first_introduced: "Shazeer et al. 2017 (sparsely-gated MoE); DeepSeekMoE (Dai et al. 2024)"
date_updated: 2026-05-28
source_url: "https://arxiv.org/abs/1701.06538"
---

## Definition

A Mixture-of-Experts layer replaces a single dense feed-forward block with many parallel "expert" sub-networks plus a gating/router network that activates only a small subset of experts per input (sparse activation). This decouples total parameter count from per-token compute, enabling very large models that remain cheap to run.

## Intuition

Different inputs need different specialists. A router sends each input to the few experts best suited to it, so the model can hold vast specialized knowledge while only paying for the experts it actually uses.

## Formal notation

y = Σ_{i∈TopK} g_i(x) · E_i(x), with gate g(x)=softmax(W_g x) and only top-K experts active; auxiliary load-balancing loss keeps experts utilized.

## Key variants

- Token-choice top-K routing vs expert-choice.
- Shared experts (always on) + routed experts (DeepSeekMoE-style "shared and routed MoE").

## Known limitations

- Routing instability and load imbalance; expert under-/over-utilization.
- Memory footprint of holding all experts.

## Open problems

- Stable routing; optimal shared/routed expert balance.

## Relevance to active research

AlphaCell uses MoE in three places: the encoder blocks, the 1.2B-parameter "inverted pyramid" decoder (8 experts, hidden 2,048), and the Flow Model's Shared-and-Routed MoE backbone, where conditional computation mitigates gradient conflicts across heterogeneous perturbations.
