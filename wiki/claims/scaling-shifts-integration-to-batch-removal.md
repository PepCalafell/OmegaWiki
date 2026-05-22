---
title: "Scaling input data systematically shifts scRNA-seq integration toward batch removal at the cost of bio-conservation"
slug: scaling-shifts-integration-to-batch-removal
status: supported
confidence: 0.9
tags:
  - data-integration
  - scRNA-seq
  - preprocessing
  - scaling
domain: single-cell-methods
source_papers:
  - benchmarking-atlas-level-data-integration-single
evidence:
  - source: "[[papers/benchmarking-atlas-level-data-integration-single]]"
    type: supports
    strength: strong
    detail: "Paired comparisons (same method × task, scaled vs unscaled input): scaling produced higher batch-removal scores in 79% of pairs but lower bio-conservation in 72% of pairs. Consistent with the broader batch-removal-vs-bio-conservation tradeoff (see [[claims/batch-removal-vs-bioconservation-tradeoff]])."
conditions: "Methods that cannot accept scaled input (LIGER, trVAE, scVI, scANVI) are excluded from these comparisons. The shift is method-independent within the scaled-input subset."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

Independent of integration method, scaling the input scRNA-seq counts (z-score normalization per gene) systematically shifts integration outcomes toward stronger batch removal and weaker biological-variance conservation. 79% of paired comparisons (same method × same task) had higher batch-removal scores with scaling; 72% had lower bio-conservation scores.

## Evidence summary

Quote (p.45): "Independent of the method, scaling resulted in higher batch removal scores (79% of comparisons) but lower bio-conservation (72% of comparisons). This observation is consistent with unscaled data performing better in our label-free conservation metrics."

## Conditions and scope

- LIGER, trVAE, scVI and scANVI cannot accept scaled input; comparison excludes them.
- For users prioritizing bio-conservation (rare cell-state recovery, trajectory inference), prefer unscaled input.
- For users prioritizing batch removal (rapid atlas-merge for overview), scaling helps.

## Counter-evidence

- (none in this paper)

## Linked ideas

(none yet)

## Open questions

- Is the effect driven by removal of magnitude-encoded biological signal (e.g. metabolic genes scaled to equal weight)?
- Does scaling have the same effect under deep-learning methods that internally re-scale?
