---
title: "On Sci-Plex, VAE and foundation baselines fail to exceed Pearson ~0.15 while AlphaCell achieves higher fidelity"
slug: sciplex-baselines-fail-exceed-pearson-15
status: supported
confidence: 0.7
tags: [AlphaCell, Sci-Plex, Pearson, low-signal, benchmark, quantitative]
domain: methods / single-cell
source_papers:
  - towards-building-world-model-simulate-perturbation
evidence:
  - source: towards-building-world-model-simulate-perturbation
    type: supports
    strength: moderate
    detail: "Quote (p.8): 'This performance advantage was most pronounced in the Sciplex dataset (Fig. 4b), where perturbation effects are subtle ... While VAE-based approaches and even foundation models like STATE struggled to exceed a Pearson correlation of 0.15, AlphaCell achieved significantly higher fidelity.'"
conditions: "Sci-Plex chemical perturbation, low effect-size / high batch-noise regime."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

In the low-signal Sci-Plex chemical perturbation setting, VAE-based methods and STATE plateau below Pearson ~0.15 with ground truth, whereas AlphaCell achieves substantially higher correlation, attributed to its denoised continuous manifold.

## Evidence summary

Reported in [[papers/towards-building-world-model-simulate-perturbation]] (Fig. 4b). Dataset: [[foundations/sci-plex-chemical-transcriptomics]]; competitor [[foundations/state-perturbation-prediction-model]].

## Conditions and scope

Compositional generalization task on Sci-Plex.

## Counter-evidence

Exact AlphaCell value not given in text; self-reported.

## Linked ideas

## Open questions

- Is the Sci-Plex advantage driven by denoising or by genome-wide feature coverage?
