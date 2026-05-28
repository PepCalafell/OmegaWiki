---
title: "Extending baseline models from HVGs to the full geneset degrades their perturbation-prediction performance"
slug: extending-baseline-models-hvgs-full-geneset
status: supported
confidence: 0.8
tags: [AlphaCell, HVG, curse-of-dimensionality, genome-wide, baselines, benchmark]
domain: methods / single-cell
source_papers:
  - towards-building-world-model-simulate-perturbation
evidence:
  - source: towards-building-world-model-simulate-perturbation
    type: supports
    strength: strong
    detail: "Quote (p.8): 'directly extending these models from HVGs to the full gene set led to a significant degradation in their predictive performance ... without a robust manifold rectification mechanism, these models succumb to the curse of dimensionality and are overwhelmed by the zero-inflated noise inherent in genome-scale observations.'"
conditions: "Baselines (CPA, GEARS, CASCADE, scGPT, STATE) evaluated on top-2000 HVGs and on full 19,253-geneset."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

When existing perturbation models are forced from a 2,000-HVG input to the full 19,253-gene input, their predictive performance significantly degrades — attributed to the curse of dimensionality and zero-inflated genome-scale noise — whereas AlphaCell maintains performance at genome scale.

## Evidence summary

Reported in [[papers/towards-building-world-model-simulate-perturbation]]. Supports the framing of [[concepts/genome-wide-cell-representation-versus-highly]] and [[concepts/manifold-rectification-continuous-virtual-cell-space]].

## Conditions and scope

Compositional generalization benchmark across OTF, Sciplex, Tahoe-100M.

## Counter-evidence

Self-benchmarked preprint, not independently verified; baseline tuning at genome scale not detailed.

## Linked ideas

## Open questions

- Would HVG baselines recover if given a dedicated denoising/manifold layer rather than raw genome-wide input?
