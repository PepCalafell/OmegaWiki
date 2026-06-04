---
title: "Batch correction (scANVI) improves disease classification over uncorrected counts"
slug: batch-correction-improves-disease-classification-over
status: supported
confidence: 0.85
tags:
  - batch-correction
  - classification
  - scANVI
domain: methods
source_papers:
  - interpretable-inflammation-landscape-circulating-immune-cells
evidence:
  - source: interpretable-inflammation-landscape-circulating-immune-cells
    type: supports
    strength: strong
    detail: "XGBoost on scANVI-corrected expression (BAS 0.87 / WF1 0.90) clearly outperformed the same classifier on uncorrected log-normalized counts (BAS 0.65 / WF1 0.78)."
conditions: "Same classifier, corrected vs uncorrected input."
date_proposed: 2026-06-04
date_updated: 2026-06-04
---

## Statement

Using scANVI batch-corrected expression as classifier input substantially improved disease classification (BAS 0.87 / WF1 0.90) compared with uncorrected log-normalized counts (BAS 0.65 / WF1 0.78), underscoring the benefit of batch correction for downstream prediction.

## Evidence summary

Direct head-to-head confusion matrices (Fig. 3a; p.637).

## Conditions and scope

Within-atlas classification; correction benefit measured on held-out samples.

## Counter-evidence

Correction does not solve cross-study (unseen-study) generalization, where batch effects still dominate.

## Linked ideas

- [[claims/gradient-boosted-trees-batch-corrected-expression]]
- [[concepts/batch-removal-vs-bioconservation-tradeoff]]
- Foundations: [[foundations/scanvi-semi-supervised]]

## Open questions

- Optimal trade-off between correction strength and biological signal retention for classification.
