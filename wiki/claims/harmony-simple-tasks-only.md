---
title: "Harmony performs well on simple scRNA-seq integration tasks but ranks outside the top third on atlas-complexity tasks"
slug: harmony-simple-tasks-only
status: supported
confidence: 0.85
tags:
  - data-integration
  - scRNA-seq
  - Harmony
  - benchmarking
domain: single-cell-methods
source_papers:
  - benchmarking-atlas-level-data-integration-single
evidence:
  - source: "[[papers/benchmarking-atlas-level-data-integration-single]]"
    type: supports
    strength: strong
    detail: "Harmony ranks competitively on simpler RNA tasks (pancreas, simulation 1) and on data with distinct biological signal, but drops outside the top third on complex atlas tasks (lung, immune human+mouse, mouse brain). Consistent with prior benchmarks (Tran 2020) that ranked Harmony first because they used simpler tasks."
conditions: "Holds for atlas-complexity tasks (many donors / laboratories / protocols, nested batches). For single-tissue, few-batch datasets, Harmony's speed advantage makes it a reasonable choice."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

Harmony, the dominant PCA-based integration method in earlier benchmarks (Tran 2020, Chazarra-Gil 2021), performs well only on simpler scRNA-seq integration tasks (distinct biological signal, few batches). On atlas-complexity tasks with nested batch effects across donors / laboratories / protocols / species, Harmony ranks outside the top third of methods.

## Evidence summary

Quote (p.45): "Harmony ranked outside the top third of methods for more complex real data tasks, but was favorable for simulations and real data with less complex biological variation."

Quote (p.48): "the use of Harmony is appropriate for simple integration tasks with distinct batch and biological structure; however, this method typically ranks outside the top three when used for complex real data scenarios."

## Conditions and scope

- "Simple" = pancreas-like tasks with distinct cell-type variation and clean batch structure.
- "Complex" = atlas-scale tasks with confounded batch / biology.
- For TME and immune-atlas applications (relevant to thesis), use Scanorama or scVI; reserve Harmony for quick exploratory integration only.

## Counter-evidence

- Harmony has excellent usability and speed; in practice users may accept the bio-conservation tradeoff for the wall-clock saving.
- For scATAC-seq, Harmony moves to the top tier (see [[claims/liger-harmony-best-scatac-integration]]).

## Linked ideas

(none yet)

## Open questions

- Has updated Harmony (post-2022) closed the gap?
- Does Harmony improve when given iterative bio-conservation regularization?
