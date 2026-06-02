---
title: "mcRigor's Score criterion selects an optimal granularity that matches the true value on semi-synthetic data"
slug: mcrigor-score-selects-optimal-granularity-matching
status: supported
confidence: 0.8
tags: [single-cell, metacell, mcRigor, hyperparameter-optimization]
domain: single-cell-methods
source_papers:
  - mcrigor-statistical-method-enhance-rigor-metacell
evidence:
  - source: mcrigor-statistical-method-enhance-rigor-metacell
    type: supports
    strength: strong
    detail: "On semi-synthetic data (true γ*=50), DubRate showed an elbow at γ* and Score peaked exactly at γ=50 for MetaCell; SEACells optimum γ=42 (also near γ*). The optimized MetaCell partition had only 4 dubious metacells."
conditions: "Semi-synthetic data; Score = 1 − w·DubRate − (1−w)·ZeroRate, default w=0.5; method-selectable because Score is on a common [0,1] scale."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

The DubRate/ZeroRate Score selects a granularity level γ that recovers the ground-truth γ* and, being comparable across methods, also guides method selection.

## Evidence summary

On semi-synthetic data with true γ* = 50: DubRate had an elbow at γ* and the highest Score occurred exactly at γ = 50 for MetaCell (optimized partition: only 4 dubious metacells); SEACells optimal γ = 42, also close to γ*. The maximal-Score configuration selected was MetaCell at γ = 50, best matching the ground truth.

## Conditions and scope

Score is task-agnostic and prior-free, enabling unbiased benchmarking. Recovery is poorer for methods (SuperCell, MetaCell2) that produce mostly dubious metacells even at small γ.

## Counter-evidence

For SuperCell and MetaCell2, mcRigor's selected γ = 4 is far from γ* — but this reflects those methods' partitions, not a Score failure.

## Linked ideas

(none yet)

## Open questions

Extending Score-based optimization to additional hyperparameters and multi-modality.
