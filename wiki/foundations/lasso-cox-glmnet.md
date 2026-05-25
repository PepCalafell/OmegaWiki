---
title: "LASSO-Cox regression (glmnet)"
slug: lasso-cox-glmnet
domain: "methods / survival modelling"
status: mainstream
aliases:
  - "LASSO Cox"
  - "L1-penalised Cox proportional hazards"
  - "glmnet Cox"
  - "cv.glmnet Cox"
  - "regularised Cox regression"
  - "LASSO survival regression"
  - "Lasso regression survival"
first_introduced: "Tibshirani 1996 (LASSO); Tibshirani 1997 Stat Med (LASSO Cox); Simon et al. 2011 (glmnet Cox implementation)"
date_updated: 2026-05-25
source_url: "https://cran.r-project.org/web/packages/glmnet/"
---

## Definition

An L1-penalised Cox proportional hazards model that performs simultaneous variable selection and shrinkage on a candidate gene/feature list. Implemented in R as `glmnet(family="cox")` with `cv.glmnet` providing k-fold cross-validated tuning of the regularisation parameter λ.

## Intuition

When the candidate predictor list (a few hundred univariate-Cox-significant genes) is larger than is desirable for a deployable model, LASSO collapses it to a sparse set by driving most coefficients to exactly zero while keeping a small subset of informative genes.

## Formal notation

- Cox partial likelihood with added penalty: maximise ℓ(β) − λ Σ|βⱼ|.
- λ chosen by minimum k-fold CV partial-likelihood deviance (`lambda.min`) or 1-SE rule (`lambda.1se`).
- Output: sparse coefficient vector; linear predictor LP(x) = β·x scored per patient.

## Key variants

- Elastic-net (mix of L1 + L2): used when predictors are correlated.
- Ridge (L2 only): no variable selection.
- Adaptive LASSO: data-driven weights for asymptotic oracle properties.

## Known limitations

- LASSO selects one of a correlated group somewhat arbitrarily.
- Stability of selection across CV folds is rarely reported.
- Train/validation overlap is common in published signatures.

## Open problems

- Robust selection-stability metrics for LASSO-Cox in small-cohort transcriptomic settings.

## Relevance to active research

LASSO-Cox is the standard shrinkage step in scRNA-anchored prognostic-signature pipelines, including [[papers/development-hypoxia-responsive-macrophage-prognostic-model]] (λ=0.0432, 23 → 13 genes).
