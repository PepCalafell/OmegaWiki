---
title: "XGBoost — gradient-boosted decision trees"
slug: xgboost-gradient-boosting
domain: "machine learning / methods"
status: mainstream
aliases:
  - "XGBoost"
  - "gradient boosting"
  - "gradient-boosted trees"
  - "extreme gradient boosting"
first_introduced: "Chen and Guestrin 2016 *KDD* (XGBoost); Friedman 2001 (gradient boosting machine)"
date_updated: 2026-06-03
source_url: "https://doi.org/10.1145/2939672.2939785"
---

## Definition

XGBoost is a scalable, regularized implementation of gradient-boosted decision trees: an additive ensemble in which each new tree is fit to the gradient (and second-order Hessian) of a differentiable loss with respect to the current ensemble prediction. It adds L1/L2 regularization, shrinkage, column subsampling, and sparsity-aware split finding for speed and overfitting control.

## Intuition

Boosting builds a strong learner by sequentially adding weak trees that each correct the residual errors of the current model. XGBoost is a default workhorse for tabular supervised learning (classification and regression) because it handles mixed feature types, missing values, and non-linear interactions with little tuning.

## Formal notation

- Model: ŷᵢ = Σ_k f_k(xᵢ), f_k ∈ space of regression trees.
- Objective: Σ l(yᵢ, ŷᵢ) + Σ Ω(f_k), with Ω penalizing tree complexity.
- Each boosting round uses a 2nd-order Taylor expansion of l (gradient gᵢ + Hessian hᵢ) to choose splits.

## Key variants

- LightGBM, CatBoost — alternative gradient-boosting libraries.
- DART — dropout-regularized boosting.

## Known limitations

- Can overfit without regularization/early stopping on noisy data.
- Tree ensembles are not directly interpretable (motivating post-hoc attribution like SHAP).
- Less suited to raw high-dimensional unstructured data (images, sequences) than deep nets.

## Open problems

- Principled uncertainty quantification for boosted ensembles.
- Calibrated probability outputs under class imbalance.

## Relevance to active research

[[papers/integrative-epigenome-based-strategy-unbiased-functional]] trains 58 independent per-CKI XGBoost classifiers that predict H3K27ac up/down-regulation at each CRE from ~21 transformed TF-occupancy/H3K27ac features, evaluating each by ROC-AUC and PR-AUC and interpreting them with SHAP feature attribution.
