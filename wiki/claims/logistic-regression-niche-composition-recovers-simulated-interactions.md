---
title: "A regularized logistic-regression classifier trained on cell-type frequencies in local neighborhoods recovers ground-truth interaction strengths in Lennard-Jones-simulated tissues for both juxtacrine (R=0) and paraview (R=5) settings"
slug: logistic-regression-niche-composition-recovers-simulated-interactions
status: supported
confidence: 0.8
tags: [spatial-simulation,Lennard-Jones,logistic-regression,benchmark]
domain: methods / spatial-transcriptomics
source_papers:
  - nico-identifies-extrinsic-drivers-cell-state
evidence:
  - source: nico-identifies-extrinsic-drivers-cell-state
    type: supports
    strength: strong
    detail: "Two simulation scenarios with six cell types and known LJ pairwise potentials; classifier coefficients track relative interaction-strength rankings; benchmarked against MISTy's juxtaview / paraview which yields less consistent rankings (Fig. 2c–f)."
conditions: "Synthetic 2D point-cloud simulations; six cell types; not biological tissue."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

A regularized logistic-regression classifier trained on cell-type frequencies in local neighborhoods recovers ground-truth interaction strengths in Lennard-Jones-simulated tissues for both juxtacrine (R=0) and paraview (R=5) settings.

## Evidence summary

[[papers/nico-identifies-extrinsic-drivers-cell-state]] — Two simulation scenarios with six cell types and known LJ pairwise potentials; classifier coefficients track relative interaction-strength rankings; benchmarked against MISTy's juxtaview / paraview which yields less consistent rankings (Fig. 2c–f).

## Conditions and scope

Synthetic 2D point-cloud simulations; six cell types; not biological tissue.

## Counter-evidence

None within paper.

## Linked ideas

## Open questions

- Independent replication outside the Grün lab.
