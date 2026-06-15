---
title: "Magnitude-based cell–cell communication scoring outperforms specificity-based scoring"
slug: magnitude-based-cell-cell-communication-scoring
status: supported
confidence: 0.8
tags:
  - cell-cell-communication
  - benchmarking
  - single-cell
domain: methods / benchmarking / single-cell
source_papers:
  - defining-benchmarking-open-problems-single-cell
evidence:
  - source: papers/defining-benchmarking-open-problems-single-cell
    type: supports
    strength: moderate
    detail: "CCC task across source–target (spatial co-localization) and ligand–target (cytokine activity) subtasks on TNBC and mouse-brain atlases."
conditions: "Open Problems CCC task v1; ground truth proxied by spatial co-localization and cytokine activity."
date_proposed: 2026-06-15
date_updated: 2026-06-15
---

## Statement

In the Open Problems cell–cell communication (CCC) task, methods that score ligand–receptor pairs by expression magnitude outperform methods that score by cell-type specificity.

## Evidence summary

"we find that methods that rely on expression magnitude outperform approaches that rely on expression specificity" (p.1038), evaluated by AUPRC and odds ratio against spatial co-localization and cytokine-activity ground truth on the TNBC and mouse-brain atlases.

## Conditions and scope

Holds under the two ground-truth proxies used; both are imperfect stand-ins for true cellular communication, which is hard to measure directly.

## Counter-evidence

Ground truth for CCC is itself contested; specificity scoring may matter more for rare or context-specific interactions not captured by these proxies.

## Linked ideas

Empirical contrast between scoring families implemented in [[foundations/liana-cell-cell-interaction-inference]] and [[foundations/cellphonedb-ligand-receptor]].

## Open questions

Whether magnitude superiority survives ground truth derived from perturbation rather than co-localization/cytokine proxies.
