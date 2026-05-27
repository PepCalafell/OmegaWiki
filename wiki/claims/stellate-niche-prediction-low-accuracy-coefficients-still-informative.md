---
title: "Stellate cells have low niche-classification accuracy (~0.06) in MERSCOPE liver — they are niche-promiscuous — yet the regression coefficients still recover the known sinusoidal-EC / Kupffer / central-hepatocyte stellate niche, demonstrating that low per-class accuracy does not preclude biologically meaningful niche-interaction inference"
slug: stellate-niche-prediction-low-accuracy-coefficients-still-informative
status: supported
confidence: 0.7
tags: [stellate-cell,niche-promiscuity,classification-accuracy,interpretation]
domain: spatial-transcriptomics / hepatology
source_papers:
  - nico-identifies-extrinsic-drivers-cell-state
evidence:
  - source: nico-identifies-extrinsic-drivers-cell-state
    type: supports
    strength: moderate
    detail: "Stellate confusion-matrix accuracy 0.06 yet signed regression coefficients identify sinusoidal EC, Kupffer cells, and central/mid hepatocytes as positive niche partners — matches the stellate niche characterized in Dobie 2019 (Fig. 5e)."
conditions: "Single dataset; interpretation depends on prior biological knowledge of stellate niche."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

Stellate cells have low niche-classification accuracy (~0.06) in MERSCOPE liver — they are niche-promiscuous — yet the regression coefficients still recover the known sinusoidal-EC / Kupffer / central-hepatocyte stellate niche, demonstrating that low per-class accuracy does not preclude biologically meaningful niche-interaction inference.

## Evidence summary

[[papers/nico-identifies-extrinsic-drivers-cell-state]] — Stellate confusion-matrix accuracy 0.06 yet signed regression coefficients identify sinusoidal EC, Kupffer cells, and central/mid hepatocytes as positive niche partners — matches the stellate niche characterized in Dobie 2019 (Fig. 5e).

## Conditions and scope

Single dataset; interpretation depends on prior biological knowledge of stellate niche.

## Counter-evidence

None within paper.

## Linked ideas

## Open questions

- Independent replication outside the Grün lab.
