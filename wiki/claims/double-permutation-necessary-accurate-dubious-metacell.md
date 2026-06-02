---
title: "Double permutation is necessary for accurate dubious-metacell detection; within-feature permutation alone fails"
slug: double-permutation-necessary-accurate-dubious-metacell
status: supported
confidence: 0.85
tags: [single-cell, metacell, mcRigor, permutation-test, null-distribution]
domain: single-cell-methods
source_papers:
  - mcrigor-statistical-method-enhance-rigor-metacell
evidence:
  - source: mcrigor-statistical-method-enhance-rigor-metacell
    type: supports
    strength: strong
    detail: "Within-feature permutation alone misclassifies >35% of ground-truth trustworthy metacells as dubious (F-score < 0.4); double permutation correctly identifies >98% of trustworthy metacells as trustworthy (F-score > 0.9)."
conditions: "Semi-synthetic simulation with ground-truth trustworthiness; null hypothesis is conditional on cell library sizes."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

mcRigor's null divergence score must be built by double permutation (within-cell then within-feature). A within-feature-only null sets the threshold too low because it does not preserve library-size-driven correlations, falsely flagging trustworthy metacells as dubious.

## Evidence summary

In simulation, within-feature permutation alone misclassified >35% of ground-truth trustworthy metacells (F-score < 0.4). The double-permutation null correctly classified >98% of trustworthy metacells as trustworthy (<2% error), with F-score consistently > 0.9.

## Conditions and scope

The argument is grounded in the multinomial measurement model: the null hypothesis is conditional on cell library sizes, which only within-cell (row-wise) permutation preserves.

## Counter-evidence

None reported.

## Linked ideas

(none yet)

## Open questions

Whether multiple rounds of double permutation per metacell further improve robustness (raised by the authors).
