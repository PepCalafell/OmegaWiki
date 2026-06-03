---
title: "SHAP — Shapley additive feature attribution"
slug: shap-feature-attribution
domain: "machine learning / interpretability / methods"
status: mainstream
aliases:
  - "SHAP"
  - "SHAP values"
  - "Shapley additive explanations"
  - "directional SHAP importance"
first_introduced: "Lundberg and Lee 2017 *NeurIPS*"
date_updated: 2026-06-03
source_url: "https://arxiv.org/abs/1705.07874"
---

## Definition

SHAP assigns each feature an additive contribution to an individual model prediction based on Shapley values from cooperative game theory: the feature's contribution is its average marginal effect across all orderings in which features are added to the model. It unifies several earlier attribution methods under one additive-feature-attribution framework with guarantees of local accuracy, missingness, and consistency.

## Intuition

For a single prediction, SHAP says "how much did each feature push the output away from the baseline (average) prediction, and in which direction?". Summing SHAP values across many samples gives a global feature-importance ranking; signing them by correlation gives directional importance.

## Formal notation

- Explanation model: g(z') = φ₀ + Σ_j φ_j z'_j, where φ_j is the SHAP value of feature j.
- φ_j = Σ_{S ⊆ F\{j}} [|S|!(|F|-|S|-1)!/|F|!] · [f(S∪{j}) − f(S)].
- TreeSHAP gives an exact polynomial-time computation for tree ensembles.

## Key variants

- TreeSHAP (exact, for trees), KernelSHAP (model-agnostic), DeepSHAP (for neural nets).

## Known limitations

- Exact Shapley computation is exponential; tractable only with model-specific approximations.
- Assumes feature independence in some estimators, which can mislead with correlated features.
- Attributions explain the model, not necessarily ground-truth causality.

## Open problems

- Faithful attribution under strongly correlated/collinear features.
- Reconciling local explanations into trustworthy global mechanistic claims.

## Relevance to active research

[[papers/integrative-epigenome-based-strategy-unbiased-functional]] uses directional SHAP importance (mean SHAP × correlation sign) to rank which TF-occupancy feature sets (IRF/STAT vs NF-κB/AP-1/IRF3) drive each per-CKI XGBoost classifier's prediction of H3K27ac up/down-regulation, revealing CKI-specific TF dependencies.
