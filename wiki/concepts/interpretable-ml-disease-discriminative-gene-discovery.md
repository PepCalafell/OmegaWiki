---
title: "Interpretable ML for disease-discriminative gene discovery"
aliases:
  - disease-discriminative gene discovery
  - interpretable gene selection single-cell
tags:
  - interpretable-ML
  - feature-attribution
  - gene-discovery
  - SHAP
  - gradient-boosting
maturity: emerging
key_papers:
  - interpretable-inflammation-landscape-circulating-immune-cells
first_introduced: "Jiménez-Gracia et al. 2026 Nature Medicine (d-SHAP / s-SHAP framework)"
date_updated: 2026-06-04
related_concepts:
  - circulating-immune-cells-living-biomarkers
  - batch-removal-vs-bioconservation-tradeoff
---

## Definition

A pipeline that trains supervised classifiers (gradient-boosted decision trees) to predict disease from single-cell expression, then applies post-hoc feature attribution (SHAP) to rank genes by their disease-discriminative power per cell type. Crucially, it separates disease signal from study/batch signal by also training a study classifier and computing study-attribution (s-SHAP), so that genes ranked high only because of batch confounding are demoted relative to bona fide disease-discriminative genes (d-SHAP).

## Intuition

Standard differential expression treats genes independently and is confounded by batch. Here, the model learns gene combinations that discriminate disease, SHAP explains which genes drive each prediction, and a parallel study classifier reveals which "disease" genes are actually study artifacts. The difference/overlap between disease-SHAP and study-SHAP prioritizes genes that truly track disease.

## Formal notation

For cell type c, disease classifier f_d and study classifier f_s are trained; per-gene SHAP values φ_d (d-SHAP) and φ_s (s-SHAP) are computed; genes are prioritized by high φ_d and low/disentangled φ_s.

## Variants

- Per-cell-type classifiers versus pooled.
- d-SHAP ranking alone versus d-SHAP/s-SHAP disentanglement.

## Comparison

Generalizes SHAP-based feature importance and gradient-boosting beyond prediction to interpretable biomarker discovery, with an explicit batch-confounding control absent from naive importance ranking.

## When to use

When you need biologically interpretable, batch-robust gene markers from a multi-study single-cell classifier rather than a black-box predictor.

## Known limitations

- SHAP attributions inherit the classifier's biases and collinearity among genes.
- Disentanglement is imperfect when disease and study are strongly collinear.

## Open problems

- Calibrated thresholds for separating disease- from study-driven attributions.
- Extending to multi-class, multi-cell-type joint attribution.

## Key papers

- [[papers/interpretable-inflammation-landscape-circulating-immune-cells]] — introduces the GBDT + d-SHAP / s-SHAP gene-discovery framework; recovers known (STAT3, IFN genes) and novel (CYBA, IFITM1) markers.

## My understanding

The methodological hook is the s-SHAP control: turning the batch problem into a second supervised task whose attributions can be subtracted out. This is a transferable recipe for batch-robust interpretable biomarker discovery, building on [[foundations/shap-feature-attribution]] and [[foundations/xgboost-gradient-boosting]].
