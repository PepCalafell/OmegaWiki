---
title: "Max aggregation of ligand–receptor scores outperforms mean aggregation in CCC inference"
slug: max-aggregation-ligand-receptor-scores-outperforms
status: supported
confidence: 0.8
tags:
  - cell-cell-communication
  - aggregation
  - benchmarking
domain: methods / benchmarking / single-cell
source_papers:
  - defining-benchmarking-open-problems-single-cell
evidence:
  - source: papers/defining-benchmarking-open-problems-single-cell
    type: supports
    strength: moderate
    detail: "Max vs mean aggregation compared across CCC methods and both subtasks; max wins consistently."
conditions: "Open Problems CCC task v1, across methods and both subtasks."
date_proposed: 2026-06-15
date_updated: 2026-06-15
---

## Statement

Aggregating ligand–receptor interaction scores with a max function outperforms mean aggregation across CCC methods and tasks.

## Evidence summary

"max aggregation of ligand–receptor scores outperformed mean aggregation across tasks and methods" (p.1038). Consistent with the finding that CCC methods are most reliable on their top-scoring predictions, max aggregation emphasises the strongest signal rather than averaging it away.

## Conditions and scope

Evaluated within the CCC task's AUPRC/odds-ratio framework; the advantage is tied to prioritising the strongest interaction per cell-type pair.

## Counter-evidence

Max aggregation is more sensitive to outliers and could amplify spurious high scores in noisier datasets.

## Linked ideas

Mechanistically tied to [[claims/cell-cell-communication-methods-accurate-only]]; relevant to [[foundations/liana-cell-cell-interaction-inference]].

## Open questions

Whether a rank-based or quantile aggregation could beat max while staying robust to outliers.
