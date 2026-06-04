---
title: "A centralized single-chemistry dataset restores patient-classifier generalization"
slug: centralized-single-chemistry-dataset-restores-patient
status: supported
confidence: 0.75
tags:
  - batch-effect
  - generalization
  - patient-classifier
domain: methods
source_papers:
  - interpretable-inflammation-landscape-circulating-immune-cells
evidence:
  - source: interpretable-inflammation-landscape-circulating-immune-cells
    type: supports
    strength: moderate
    detail: "On a Centralized Dataset (single center, single chemistry; SCGT00), with reference/query stratified by sequencing pool, WF1 and BAS rose to 0.56 and 0.53 vs Scenario 3's 0.23 / 0.12, isolating batch effects as the cause of poor cross-study generalization."
conditions: "Single-center, single-chemistry data; query pools distinct from reference."
date_proposed: 2026-06-04
date_updated: 2026-06-04
---

## Statement

Restricting to a centralized dataset generated in a single center with one assay chemistry recovered much of the lost generalization (WF1 0.56 / BAS 0.53 vs Scenario 3's 0.23 / 0.12), demonstrating that assay-chemistry and center batch effects — not biological signal — were the main barrier to cross-study patient classification.

## Evidence summary

Centralized Dataset analysis (SCGT00) with new annotation and scANVI integration (Fig. 5a-c; p.639). Provides the controlled experiment isolating the batch-effect cause.

## Conditions and scope

Single-chemistry, single-center setting; still below within-atlas CV performance.

## Counter-evidence

Even centralized performance is moderate, so additional factors beyond chemistry/center remain.

## Linked ideas

- [[claims/patient-classifier-generalizes-unseen-patients-fails]]
- [[concepts/patient-classification-reference-embedding-projection]] · [[concepts/batch-removal-vs-bioconservation-tradeoff]]

## Open questions

- What residual factors limit performance even in a centralized setting?
