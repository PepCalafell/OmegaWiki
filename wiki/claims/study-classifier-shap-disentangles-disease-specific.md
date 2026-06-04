---
title: "A study classifier (s-SHAP) disentangles disease-specific from batch-confounded genes"
slug: study-classifier-shap-disentangles-disease-specific
status: weakly_supported
confidence: 0.7
tags:
  - SHAP
  - batch-effect
  - interpretable-ML
  - feature-selection
domain: methods
source_papers:
  - interpretable-inflammation-landscape-circulating-immune-cells
evidence:
  - source: interpretable-inflammation-landscape-circulating-immune-cells
    type: supports
    strength: moderate
    detail: "A separate classifier predicting study identity (BAS 0.97 / WF1 0.99) and its SHAP values (s-SHAP) were correlated/overlapped with d-SHAP to prioritize bona fide disease-discriminative genes and demote study-confounded ones."
conditions: "Study classifier per cell type; d-SHAP vs s-SHAP overlap analysis."
date_proposed: 2026-06-04
date_updated: 2026-06-04
---

## Statement

Training a parallel classifier to predict study identity (BAS 0.97 / WF1 0.99) and computing its feature attributions (s-SHAP) enabled the authors to disentangle disease-specific from study-specific signal, prioritizing bona fide disease-discriminative genes over batch-confounded ones.

## Evidence summary

Correlation/overlap of d-SHAP and s-SHAP values (Supplementary Fig. 4; p.638). The very high study-classification accuracy itself quantifies the magnitude of batch signal.

## Conditions and scope

Works where disease and study are not perfectly collinear; per-cell-type.

## Counter-evidence

When disease and study are strongly collinear, disentanglement is imperfect — a limitation the authors acknowledge.

## Linked ideas

- [[claims/shap-gene-selection-outperforms-random-genes]]
- [[concepts/interpretable-ml-disease-discriminative-gene-discovery]]
- Foundations: [[foundations/shap-feature-attribution]]

## Open questions

- Quantitative thresholds for declaring a gene disease- vs study-driven.
