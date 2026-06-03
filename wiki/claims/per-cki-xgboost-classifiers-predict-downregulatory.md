---
title: "Per-CKI XGBoost classifiers predict downregulatory H3K27ac effects from TF occupancy better than upregulatory effects"
slug: per-cki-xgboost-classifiers-predict-downregulatory
status: supported
confidence: 0.75
tags:
  - methodological
  - machine-learning
  - transcription-factors
  - H3K27ac
domain: methods / machine learning
source_papers:
  - integrative-epigenome-based-strategy-unbiased-functional
evidence:
  - source: integrative-epigenome-based-strategy-unbiased-functional
    type: supports
    strength: moderate
    detail: "58 independent XGBoost classifiers using ~21 transformed features from ~200 TF ChIP-seq + H3K27ac predicted down-regulatory CREs better than up-regulatory (ROC-AUC/PR-AUC); directional SHAP showed IRF/STAT and NF-κB/AP-1/IRF3 feature sets drive downregulation, with CKI-specific weighting."
conditions: "~16,500 LPS-regulated CREs as observations; per-CKI models."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Training one gradient-boosted classifier per CKI on transcription-factor genomic occupancy plus H3K27ac features predicts which CREs each inhibitor downregulates more accurately than which it upregulates, and SHAP attributions reveal CKI-specific reliance on IRF/STAT versus NF-κB/AP-1/IRF3 features.

## Evidence summary

58 [[foundations/xgboost-gradient-boosting]] models scored by ROC-AUC/PR-AUC performed better on down- than up-regulation (the latter being sparse); [[foundations/shap-feature-attribution]] showed Filgotinib weighted IRF/STAT, Mubritinib weighted NF-κB/AP-1/IRF3. Links [[foundations/irf3-interferon-regulatory-factor-3]], [[foundations/stat1-tf]], [[foundations/stat2-tf]], [[foundations/nf-kb-p65-rela]].

## Conditions and scope

LPS-regulated CREs in mouse BMDM; ~200 TF ChIP-seq datasets for 34 TFs as features.

## Counter-evidence

Models cannot assign specific inhibited kinases to TFs — only correlate H3K27ac changes with TF sets; upregulatory prediction was unreliable for most CKIs.

## Linked ideas

## Open questions

- Could richer TF panels enable reliable prediction of upregulatory effects?
