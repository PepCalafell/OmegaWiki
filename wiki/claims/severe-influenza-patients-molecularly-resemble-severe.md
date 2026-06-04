---
title: "Severe influenza patients molecularly resemble severe COVID-19 cases"
slug: severe-influenza-patients-molecularly-resemble-severe
status: weakly_supported
confidence: 0.7
tags:
  - influenza
  - COVID-19
  - respiratory-infection
  - classification
domain: immunology
source_papers:
  - interpretable-inflammation-landscape-circulating-immune-cells
evidence:
  - source: interpretable-inflammation-landscape-circulating-immune-cells
    type: supports
    strength: moderate
    detail: "Severe Flu patients were frequently misclassified as COVID; retraining the GBDT on the COMBAT Flu/COVID dataset and stratifying COVID by severity showed severe Flu closely resembling severe COVID, corroborated by pseudobulk clustering."
conditions: "COMBAT dataset; severity stratification (mild/severe/critical)."
date_proposed: 2026-06-04
date_updated: 2026-06-04
---

## Statement

The classifier's misclassification of severe influenza as COVID reflected genuine biology: retraining on the COMBAT Flu/COVID dataset with COVID severity stratification, and pseudobulk-level clustering, showed that severe influenza patients closely resemble severe COVID-19 — a shared inflammatory signature of severe respiratory viral infection.

## Evidence summary

Extended Data Fig. 4a-d (p.637); convergent evidence from classifier retraining and sample-level pseudobulk clustering.

## Conditions and scope

Severe respiratory viral infection; specific external dataset (COMBAT).

## Counter-evidence

"Resemblance" is a transcriptional-signature similarity, not clinical equivalence.

## Linked ideas

- [[concepts/inflammation-atlas-circulating-immune-cells]]
- Foundations: [[foundations/influenza-virus]] · [[foundations/sars-cov-2-coronavirus]]

## Open questions

- Are shared severe-infection signatures a target for cross-disease therapy?
