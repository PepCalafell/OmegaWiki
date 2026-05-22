---
title: "There is a consistent tradeoff between batch-effect removal and biological-variance conservation across scRNA-seq integration methods"
slug: batch-removal-vs-bioconservation-tradeoff
status: supported
confidence: 0.95
tags:
  - data-integration
  - scRNA-seq
  - benchmarking
  - tradeoff
domain: single-cell-methods
source_papers:
  - benchmarking-atlas-level-data-integration-single
evidence:
  - source: "[[papers/benchmarking-atlas-level-data-integration-single]]"
    type: supports
    strength: strong
    detail: "Across 5 scRNA-seq tasks, methods split predictably along this axis: SAUCIE / LIGER / BBKNN / Seurat v3 favor batch removal; DESC / Conos favor bio-conservation; Scanorama / scVI / FastMNN (gene) balance both. The tradeoff is especially visible where biological and batch effects overlap (e.g. lung endothelial cells across spatial locations). Spearman rank correlation between batch-removal and bio-conservation scores within method-task pairs is reported as consistent across all tasks."
conditions: "Holds for all 16 benchmarked methods across the 5 RNA tasks, all 6 scATAC tasks, and 2 simulations. Methods that use cell-identity labels (scGen, scANVI) escape the tradeoff partially because they exploit additional supervision. Confounded batch / biology (species, spatial location) makes the tradeoff inescapable for label-agnostic methods."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

Across scRNA-seq integration methods, there is a consistent inverse relationship between how strongly a method removes batch effects and how well it preserves biological variation. Methods that aggressively merge batches (SAUCIE, LIGER, BBKNN, Seurat v3) lose subtle biology; methods that preserve biology (DESC, Conos) under-correct batch. Only methods that balance both axes (Scanorama, scVI, FastMNN) or that use cell-identity labels (scGen, scANVI) optimize both objectives simultaneously.

## Evidence summary

- Fig. 3a scatter plot of mean batch-correction score vs mean bio-conservation score for all 16 methods on RNA tasks shows a clear Pareto frontier with the named methods at its extremes.
- The tradeoff is amplified by preprocessing choices: scaling shifts results toward batch removal at the cost of bio-conservation (79% / 72% of paired comparisons; see [[claims/scaling-shifts-integration-to-batch-removal]]).
- On the lung task, Seurat v3 CCA removes within-cell-type spatial location variation that Scanorama preserves, confirming the tradeoff at the gene-level.

## Conditions and scope

- The tradeoff is universal in label-agnostic methods but partially escapable via supervised methods (scGen, scANVI).
- It is irreducible when batch and biology are confounded (species, spatial location, single-cell-vs-nucleus).
- The 40/60 batch/bio aggregate weight is the editorial choice that operationalizes the tradeoff; alternative weightings move method tails but not the head ranking.

## Counter-evidence

- (none in this paper; this is a central, well-supported finding)

## Linked ideas

(none yet)

## Open questions

- Can a single method dominate the Pareto frontier on label-agnostic atlas tasks?
- Does the tradeoff vanish under reference-mapping (scArches) reformulations where the reference embedding is fixed?
