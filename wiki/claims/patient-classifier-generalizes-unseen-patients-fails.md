---
title: "Patient classifier generalizes to unseen patients (BAS 0.95) but fails on unseen studies (BAS 0.12)"
slug: patient-classifier-generalizes-unseen-patients-fails
status: supported
confidence: 0.85
tags:
  - patient-classifier
  - generalization
  - batch-effect
domain: methods
source_papers:
  - interpretable-inflammation-landscape-circulating-immune-cells
evidence:
  - source: interpretable-inflammation-landscape-circulating-immune-cells
    type: supports
    strength: strong
    detail: "Scenario 2 (unseen patients) retained high performance (BAS 0.95 / WF1 0.98), but Scenario 3 (unseen studies) collapsed (BAS 0.12 / WF1 0.23), the largest drop occurring between the two scenarios."
conditions: "Scenario 2: 144 unseen-patient samples; Scenario 3: 86 unseen-study samples."
date_proposed: 2026-06-04
date_updated: 2026-06-04
---

## Statement

The reference-mapping patient classifier generalized well to unseen patients from seen studies (Scenario 2: BAS 0.95 / WF1 0.98) but failed badly on patients from entirely unseen studies (Scenario 3: BAS 0.12 / WF1 0.23) — an honest demonstration that cross-study batch effects, not biology, are the binding constraint on atlas-based diagnostics.

## Evidence summary

Scenario 2 vs Scenario 3 results (Fig. 4f-k; p.639). The authors attribute the gap to confounders such as assay chemistry and center.

## Conditions and scope

Distinguishes intra-study patient generalization from cross-study generalization.

## Counter-evidence

A centralized single-chemistry dataset partly recovers performance — see [[claims/centralized-single-chemistry-dataset-restores-patient]].

## Linked ideas

- [[concepts/patient-classification-reference-embedding-projection]]
- [[concepts/batch-removal-vs-bioconservation-tradeoff]]

## Open questions

- Can cross-study generalization be achieved without single-chemistry centralization?
