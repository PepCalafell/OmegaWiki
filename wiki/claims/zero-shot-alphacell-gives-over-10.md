---
title: "In cell-type zero-shot, AlphaCell gives 2.5–>10x Pearson improvement and 30–50% MAE reduction over STATE"
slug: zero-shot-alphacell-gives-over-10
status: supported
confidence: 0.7
tags: [AlphaCell, zero-shot, Pearson, MAE, STATE, quantitative]
domain: methods / single-cell
source_papers:
  - towards-building-world-model-simulate-perturbation
evidence:
  - source: towards-building-world-model-simulate-perturbation
    type: supports
    strength: moderate
    detail: "Quote (p.16): 'AlphaCell delivers a 2.5- to >10-fold increase in Pearson correlation (e.g., from ~0.02 to ~0.2 in OTF, Fig. 5a) and reduces the Mean Absolute Error (MAE) by 30% to 50% across the three datasets.'"
conditions: "Cell-type zero-shot: predict response of a lineage entirely absent from training; vs STATE and PerturbMean."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

In the cell-type zero-shot regime (unseen lineage), AlphaCell reports a 2.5- to >10-fold Pearson improvement over STATE (e.g., ~0.02 → ~0.2 on OTF) and a 30–50% MAE reduction across OTF, Sci-Plex and Tahoe.

## Evidence summary

Reported in [[papers/towards-building-world-model-simulate-perturbation]] (Fig. 5). Concept: [[concepts/cell-type-zero-shot-perturbation-generalization]]; competitor [[foundations/state-perturbation-prediction-model]].

## Conditions and scope

Absolute Pearson values remain low (~0.2), so "fold" gains are over a near-random STATE baseline (~0.02).

## Counter-evidence

Low absolute correlations indicate the task is far from solved; self-reported.

## Linked ideas

## Open questions

- Is Pearson ~0.2 sufficient for actionable in-silico screening?
