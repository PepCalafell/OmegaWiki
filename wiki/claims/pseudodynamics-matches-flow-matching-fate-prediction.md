---
title: "pseudodynamics+ matches flow-matching methods on LARRY fate prediction"
slug: pseudodynamics-matches-flow-matching-fate-prediction
status: weakly_supported
confidence: 0.7
tags:
  - benchmark
  - LARRY
  - fate-prediction
  - flow-matching
domain: "methods / single-cell genomics"
source_papers:
  - pseudodynamics-reconstructing-population-dynamics-time-resolved
evidence:
  - source: pseudodynamics-reconstructing-population-dynamics-time-resolved
    type: supports
    strength: moderate
    detail: "On LARRY-barcoded in vitro haematopoiesis (Days 2/4/6), pseudodynamics+ outperformed most baselines and achieved fate-prediction accuracy comparable to the latest flow-matching models (OT-CFM, SF2M); on Wasserstein-2 trajectory accuracy it was competitive but surpassed by PRESCIENT and MIOFlow."
conditions: "All models trained in 5D diffusion-map space; clonal ground truth from LARRY barcodes."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Against a LARRY-barcoded benchmark with clonal ground truth, pseudodynamics+ achieves fate-prediction accuracy comparable to state-of-the-art flow-matching methods and better than dynamic-OT methods, while remaining competitive on Wasserstein-2 trajectory accuracy.

## Evidence summary

Multi-method benchmark; pseudodynamics+ ties (not dominates) flow-matching, an honest result for a population-aware method not specialized for fate prediction.

## Conditions and scope

Single in vitro dataset; W2 surpassed by PRESCIENT/MIOFlow.

## Counter-evidence

PRESCIENT and MIOFlow beat it on W2 distance for the selected clones.

## Linked ideas

## Open questions

- Whether population-aware modelling helps or is neutral for pure fate prediction.
