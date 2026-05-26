---
title: "SCeptre processing of scp-MS data removes donor, plate, and TMT-channel batch effects without residual technical clustering"
slug: sceptre-removes-scp-ms-batch-effects
status: supported
confidence: 0.9
tags: [SCeptre, batch-correction, scp-MS, methodological, PCA-regression]
domain: single-cell proteomics / methods
source_papers:
  - mapping-early-human-blood-cell-differentiation
evidence:
  - source: mapping-early-human-blood-cell-differentiation
    type: supports
    strength: strong
    detail: "Quote (p.2): 'we did not observe any batch effects based on the TMTpro channel, individual donors or plates (fig. S1, B to D), indicating that technical and biological (donor) variations were largely removed. We further validated this using principal component regression (32) which revealed that only very low fractions of the variance could be explained by MS run, TMTpro label, donor or age (fig. S2A).'"
conditions: "SCeptre default normalization (median-ratio); PCA regression validation."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

SCeptre processing removes the dominant technical confounders (donor, plate, TMT channel, MS run) in scp-MS data without residual technical clustering on the UMAP.

## Evidence summary

PCA regression confirms low variance attributable to technical covariates. Reported in [[papers/mapping-early-human-blood-cell-differentiation]] (Fig. S1, S2A).

## Conditions and scope

Healthy adult human bone marrow CD34+; six donors; default SCeptre median-ratio normalization.

## Counter-evidence

None within scope.

## Linked ideas

## Open questions

- Cross-laboratory and cross-instrument batch correction is not assessed in the paper.
