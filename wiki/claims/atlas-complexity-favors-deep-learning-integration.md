---
title: "Atlas-complexity integration tasks favor nonlinear deep-learning methods over classical linear methods (reversing earlier benchmarks)"
slug: atlas-complexity-favors-deep-learning-integration
status: supported
confidence: 0.85
tags:
  - data-integration
  - deep-learning
  - atlas
  - methods-comparison
domain: single-cell-methods
source_papers:
  - benchmarking-atlas-level-data-integration-single
evidence:
  - source: "[[papers/benchmarking-atlas-level-data-integration-single]]"
    type: supports
    strength: strong
    detail: "Earlier benchmarks (Tran 2020 Genome Biology; Chazarra-Gil 2021 BatchBench) concluded ComBat and Harmony win on scRNA-seq integration. This study, on atlas-complexity tasks (multi-donor, multi-laboratory, multi-protocol, up to 1M cells), finds the opposite: nonlinear deep-learning methods (scVI, scANVI, scGen) and MNN-anchor methods (Scanorama, FastMNN) outperform Harmony and ComBat. Authors interpret the reversal as a complexity threshold effect — linear methods suffice for simple tasks; nonlinear methods are required for atlas-scale."
conditions: "Holds for atlas-complexity tasks. For simple tasks (single tissue, few batches, distinct cell-type structure), the earlier benchmarks' finding remains valid: Harmony and ComBat are competitive."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

Earlier scRNA-seq integration benchmarks (Tran 2020, Chazarra-Gil 2021) concluded that classical linear methods (ComBat, Harmony) outperform complex nonlinear methods. The scIB benchmark reverses this conclusion on atlas-complexity tasks: nonlinear deep-learning methods (scVI, scANVI, scGen) and MNN-anchor methods (Scanorama, FastMNN) dominate, while Harmony and ComBat drop in rank. The discrepancy is explained by task complexity — earlier benchmarks used simpler tasks where linear methods suffice; atlas-scale tasks expose their limits.

## Evidence summary

Quote (p.41): "Previous studies on benchmarking methods for data integration… found that ComBat or the linear, principal component analysis (PCA)-based, Harmony method outperformed more complex, nonlinear, methods."

Quote (p.48): "on more complex integration tasks, Scanorama (embeddings) and scVI worked well. Methods that used cell annotations to integrate batches (scGen and scANVI) performed well across tasks."

## Conditions and scope

- "Atlas-complexity" = multi-donor + multi-laboratory + multi-protocol; nested batch effects; up to 1M cells.
- For simple integration tasks the earlier benchmarks' conclusion is not contradicted.
- The reversal is method-class-level, not method-specific (anchor methods and deep-learning methods both rise).

## Counter-evidence

- Harmony's usability + speed advantage may justify its continued use on atlas tasks despite lower aggregate score.

## Linked ideas

(none yet)

## Open questions

- What is the exact "complexity threshold" beyond which deep learning wins — number of cells, number of batches, biological diversity?
