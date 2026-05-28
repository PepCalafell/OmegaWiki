---
title: "AlphaCell uses a 1.2-billion-parameter 'inverted pyramid' Mixture-of-Experts decoder"
slug: alphacell-uses-billion-parameter-inverted-pyramid
status: supported
confidence: 0.9
tags: [AlphaCell, decoder, MoE, inverted-pyramid, architecture, scale]
domain: methods / single-cell
source_papers:
  - towards-building-world-model-simulate-perturbation
evidence:
  - source: towards-building-world-model-simulate-perturbation
    type: supports
    strength: strong
    detail: "Quote (p.8-9, p.21): 'AlphaCell attaches a massive 1.2-billion-parameter Mixture-of-Experts (MoE) Decoder directly to the latent manifold ... 6 Transformer blocks with a wide MoE layer (8 experts, hidden dimension of 2,048).' The asymmetry (compact encoder, massive decoder) is deliberate, framing the decoder as a deep biological knowledge base."
conditions: "Encoder/decoder are intentionally asymmetric, unlike symmetric autoencoders."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

Unlike symmetric autoencoders, AlphaCell couples a compact encoder with a massive 1.2B-parameter MoE decoder (6 Transformer blocks, 8-expert wide MoE) — the "inverted pyramid" — so sparse MoE activation memorizes vast regulatory priors needed to expand a compressed embedding back to the full 19,253-gene profile.

## Evidence summary

Reported in [[papers/towards-building-world-model-simulate-perturbation]]. See [[foundations/mixture-experts-layer]]; reconstruction performance captured in [[claims/alphacell-decoder-reconstructs-genome-wide-expression]].

## Conditions and scope

Sparse activation keeps compute tractable despite high parameter count.

## Counter-evidence

No reported scaling study isolating decoder-size effect on fidelity.

## Linked ideas

## Open questions

- Does the inverted-pyramid asymmetry generalize to multi-omic decoding?
