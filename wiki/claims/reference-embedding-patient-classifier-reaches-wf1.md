---
title: "Reference-embedding patient classifier reaches WF1 0.90 / BAS 0.85 in cross-validation"
slug: reference-embedding-patient-classifier-reaches-wf1
status: supported
confidence: 0.85
tags:
  - patient-classifier
  - reference-mapping
  - majority-voting
domain: methods
source_papers:
  - interpretable-inflammation-landscape-circulating-immune-cells
evidence:
  - source: interpretable-inflammation-landscape-circulating-immune-cells
    type: supports
    strength: strong
    detail: "The embedding-pseudobulk, per-cell-type, majority-voting patient classifier achieved 0.90 ± 0.03 WF1 and 0.85 ± 0.07 BAS in five-fold cross-validation (Scenario 1)."
conditions: "Scenario 1, five-fold cross-validation on 817 reference samples."
date_proposed: 2026-06-04
date_updated: 2026-06-04
---

## Statement

The patient-level classifier — which projects query cells into the scANVI reference embedding, forms per-cell-type embedding pseudobulks, trains one classifier per cell type, and resolves the diagnosis by majority voting — achieved 0.90 ± 0.03 weighted F1 and 0.85 ± 0.07 balanced accuracy in five-fold cross-validation.

## Evidence summary

Scenario 1 results (Fig. 4c-e; p.639). Majority voting provided robustness even when some cell types (plasma, UTC) classified poorly.

## Conditions and scope

Cross-validation within the reference atlas (Scenario 1); does not reflect cross-study deployment.

## Counter-evidence

Performance collapses on unseen studies (Scenario 3) — see [[claims/patient-classifier-generalizes-unseen-patients-fails]].

## Linked ideas

- [[concepts/patient-classification-reference-embedding-projection]]
- Foundations: [[foundations/scanvi-semi-supervised]]

## Open questions

- How does within-atlas CV performance relate to real clinical deployment?
