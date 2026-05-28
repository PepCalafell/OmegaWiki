---
title: "AlphaCell Flow Model was trained on ~90 million perturbed profiles (Tahoe + Sci-Plex + genetic overexpression)"
slug: alphacell-flow-model-trained-90-million
status: supported
confidence: 0.9
tags: [AlphaCell, flow-model, perturbation, Tahoe, Sci-Plex, scale]
domain: methods / single-cell
source_papers:
  - towards-building-world-model-simulate-perturbation
evidence:
  - source: towards-building-world-model-simulate-perturbation
    type: supports
    strength: strong
    detail: "Quote (p.4): 'the Flow Model was trained on 90 million perturbed profiles (80 million profiles from the Tahoe dataset and nearly 10 million profiles from pharmacological, e.g. Sciplex, and genetic overexpression screens).' Methods (p.21) states 'over 80 million paired perturbation profiles' — minor internal inconsistency in headline counts."
conditions: "Interventional corpus: Tahoe-100M, Sci-Plex, OTF (TF overexpression) screens."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

The AlphaCell Flow Model, which learns the dynamic laws of cellular state transition, was trained on roughly 90 million perturbed single-cell profiles spanning large-scale genetic and chemical screens (Tahoe, Sci-Plex, OTF).

## Evidence summary

Reported in [[papers/towards-building-world-model-simulate-perturbation]]. Datasets: [[foundations/tahoe-100m-single-cell-perturbation-atlas]], [[foundations/sci-plex-chemical-transcriptomics]]. Note minor count discrepancy between Results (90M) and Methods (>80M).

## Conditions and scope

Flow training is separate from base-model pretraining; uses paired control/perturbed populations matched by intra-batch OT.

## Counter-evidence

Internal inconsistency in stated totals (90M vs >80M).

## Linked ideas

## Open questions

- What is the exact composition (genetic vs chemical) of the flow training corpus?
