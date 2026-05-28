---
title: "AlphaCell Base Model was trained on over 220 million single cells (140M CELLxGENE + 80M Tahoe)"
slug: alphacell-base-model-trained-over-220
status: supported
confidence: 0.95
tags: [AlphaCell, scale, pretraining, CELLxGENE, Tahoe, foundation-model]
domain: methods / single-cell
source_papers:
  - towards-building-world-model-simulate-perturbation
evidence:
  - source: towards-building-world-model-simulate-perturbation
    type: supports
    strength: strong
    detail: "Quote (p.4): 'The Base Model (comprising the Encoder and Decoder) was trained on over 220 million single cells (140 million observational transcriptomes from CZ CELLxGENE with 80 million profiles from the Tahoe dataset).'"
conditions: "Base-building uses ~140M unpaired observational cells (CELLxGENE Discover census + Tahoe baselines)."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

The AlphaCell Base Model (encoder + decoder) that builds the Virtual Cell Space was pretrained on over 220 million single cells, combining ~140M observational transcriptomes from CZ CELLxGENE Discover with ~80M profiles from the Tahoe dataset.

## Evidence summary

Reported in [[papers/towards-building-world-model-simulate-perturbation]]. Data sources: [[foundations/czi-cellxgene-atlas]] and [[foundations/tahoe-100m-single-cell-perturbation-atlas]].

## Conditions and scope

Square-root cell-type sampling applied to balance abundant vs rare cell types.

## Counter-evidence

None; descriptive training-scale claim.

## Linked ideas

## Open questions

- How much of the 220M is redundant vs contributing marginal manifold coverage?
