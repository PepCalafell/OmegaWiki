---
title: "d-SHAP gene selection outperforms random gene sets on unseen studies"
slug: shap-gene-selection-outperforms-random-genes
status: supported
confidence: 0.8
tags:
  - SHAP
  - feature-selection
  - interpretable-ML
domain: methods
source_papers:
  - interpretable-inflammation-landscape-circulating-immune-cells
evidence:
  - source: interpretable-inflammation-landscape-circulating-immune-cells
    type: supports
    strength: moderate
    detail: "On unseen studies, genes selected by disease-discriminative SHAP (d-SHAP) values consistently yielded more accurate XGBoost predictions than equal-sized random gene sets (top 5/10/20 genes, nested cross-validation)."
conditions: "Genes expressed in ≥5% of cells; n=20 random gene sets as comparator."
date_proposed: 2026-06-04
date_updated: 2026-06-04
---

## Statement

Ranking genes by disease-discriminative SHAP (d-SHAP) values and selecting the top features produced classifiers that consistently outperformed equal-sized random gene sets on unseen-study cells, validating d-SHAP as an effective gene-selection criterion.

## Evidence summary

Nested cross-validation on unseen studies' cells, comparing top 5/10/20 d-SHAP genes vs random gene sets and the full gene set (Fig. 3b; p.637).

## Conditions and scope

Genes expressed in ≥5% of cells; per inflammatory condition in the unseen-studies dataset.

## Counter-evidence

Absolute unseen-study performance remains modest; d-SHAP improves relative ranking, not absolute generalization.

## Linked ideas

- [[claims/study-classifier-shap-disentangles-disease-specific]]
- [[concepts/interpretable-ml-disease-discriminative-gene-discovery]]
- Foundations: [[foundations/shap-feature-attribution]]

## Open questions

- How many genes are needed for robust cross-study selection?
