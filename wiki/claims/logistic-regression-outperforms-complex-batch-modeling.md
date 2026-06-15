---
title: "Logistic regression outperforms complex batch-modeling methods for label projection"
slug: logistic-regression-outperforms-complex-batch-modeling
status: supported
confidence: 0.8
tags:
  - label-projection
  - simple-baselines
  - benchmarking
domain: methods / benchmarking / single-cell
source_papers:
  - defining-benchmarking-open-problems-single-cell
evidence:
  - source: papers/defining-benchmarking-open-problems-single-cell
    type: supports
    strength: strong
    detail: "Held across all four reference datasets in the label-projection task, even with added training noise (Supplementary Note 1.2)."
conditions: "Open Problems label-projection task; four reference datasets currently included."
date_proposed: 2026-06-15
date_updated: 2026-06-15
---

## Statement

On all four reference datasets in the Open Problems label-projection task, a simple logistic regression model outperforms more complex methods that explicitly model batch effects, even when noise is added to the training data.

## Evidence summary

"on all four reference datasets currently included in the Open Problems label projection task, a simple logistic regression model outperforms more complex methods that explicitly model batch effects, even when noise is added to the training data" (p.1038; Supplementary Note 1.2). A flagship instance of the recurring "simple baselines win" pattern.

## Conditions and scope

Label projection (cell-type transfer) with the current four reference datasets; complex methods may still help in regimes not represented here.

## Counter-evidence

Four datasets is a limited basis; deep batch-aware models may win on harder cross-modality or cross-species transfers.

## Linked ideas

Flagship evidence for [[concepts/simple-baselines-outperform-complex-single-cell]].

## Open questions

In which label-projection regimes, if any, batch-modeling complexity actually pays off.
