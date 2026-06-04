---
title: "Gradient-boosted trees on batch-corrected expression classify inflammatory disease at BAS 0.87 / WF1 0.90"
slug: gradient-boosted-trees-batch-corrected-expression
status: supported
confidence: 0.9
tags:
  - classification
  - XGBoost
  - benchmarking
  - disease-prediction
domain: methods
source_papers:
  - interpretable-inflammation-landscape-circulating-immune-cells
evidence:
  - source: interpretable-inflammation-landscape-circulating-immune-cells
    type: supports
    strength: strong
    detail: "Per-cell-type XGBoost classifiers on scANVI-corrected expression achieved balanced accuracy 0.87 and weighted F1 0.90 on held-out samples; performance consistent across cell types (lower for rare populations e.g. plasma BAS 0.78)."
conditions: "Cell-wise XGBoost, one model per Level 1 cell type; held-out samples."
date_proposed: 2026-06-04
date_updated: 2026-06-04
---

## Statement

Gradient-boosted decision trees (XGBoost) trained per cell type on scANVI-corrected single-cell expression classified inflammatory conditions with a balanced accuracy of 0.87 and a weighted F1 of 0.90 on held-out samples.

## Evidence summary

Confusion matrices and per-cell-type scores (Fig. 3a; Extended Data Fig. 3; p.637). Less abundant cell populations scored lower (e.g. plasma cells BAS 0.78).

## Conditions and scope

Cell-level classification within the atlas; held-out samples from the same studies.

## Counter-evidence

Some diseases misclassified (severe Flu as COVID); generalization to unseen studies is poor (separate claim).

## Linked ideas

- [[claims/batch-correction-improves-disease-classification-over]]
- [[concepts/interpretable-ml-disease-discriminative-gene-discovery]]
- Foundations: [[foundations/xgboost-gradient-boosting]]

## Open questions

- How much of this accuracy survives cross-study deployment?
