---
title: "Chi-square-style normalization converts landmark abundances into a relative-density matrix"
slug: chi-square-normalization-yields-sample-level
status: supported
confidence: 0.85
tags: [scSLIDE, normalization, density, methods]
domain: single-cell genomics
source_papers:
  - reconstructing-developmental-disease-progression-sample-level
evidence:
  - source: reconstructing-developmental-disease-progression-sample-level
    type: supports
    strength: strong
    detail: "Method: expected counts are computed from row/column marginals and the observed deviation is scaled by the square root of the expectation, yielding residuals where positive values mean higher-than-expected density near a landmark."
conditions: "Corrects for differences in per-sample cell count and cell-state frequency."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

scSLIDE normalizes the raw landmark-abundance matrix with a chi-square-style transform — scaling observed-minus-expected deviations by the square root of the expected count — so that each entry expresses relative enrichment or depletion of a sample's cells near a landmark.

## Evidence summary

Stated explicitly in the Method of [[reconstructing-developmental-disease-progression-sample-level]]; the resulting "sample-level relative density matrix" is the input to diffusion maps / clustering.

## Conditions and scope

Accounts for sample-level cell-count and frequency differences; relies on independence-based expected counts.

## Counter-evidence

None reported.

## Linked ideas

Core step of [[landmark-based-density-estimation]].

## Open questions

How robust is the independence-based expectation when compositional shifts are extreme?
