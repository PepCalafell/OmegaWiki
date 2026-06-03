---
title: "pseudodynamics+ imputes held-out haematopoiesis timepoints at average KLD 0.097"
slug: pseudodynamics-imputes-held-out-haematopoiesis-timepoints
status: weakly_supported
confidence: 0.7
tags:
  - imputation
  - held-out
  - KLD
  - quantitative
domain: "haematopoiesis / methods"
source_papers:
  - pseudodynamics-reconstructing-population-dynamics-time-resolved
evidence:
  - source: pseudodynamics-reconstructing-population-dynamics-time-resolved
    type: supports
    strength: moderate
    detail: "Training fit averaged KLD 0.136; the model imputed cell-type density for two held-out timepoints (Day 49 and Day 161) at average KLD 0.097, spanning a transitional and a homeostatic state."
conditions: "Mouse in vivo haematopoiesis; two timepoints held out during training."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

pseudodynamics+ accurately imputes density at unobserved timepoints, achieving average KL divergence 0.097 on two held-out timepoints (Day 49, 161) versus 0.136 on seen training timepoints.

## Evidence summary

Quantitative held-out evaluation demonstrates generalization of the learned dynamic parameters across a 9-month window.

## Conditions and scope

Two held-out timepoints in one dataset.

## Counter-evidence

None reported.

## Linked ideas

## Open questions

- Imputation accuracy for timepoints outside the observed range (extrapolation).
