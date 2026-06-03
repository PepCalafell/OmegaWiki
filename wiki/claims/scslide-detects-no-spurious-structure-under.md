---
title: "scSLIDE detects no spurious structure under sample-label permutation (does not overfit)"
slug: scslide-detects-no-spurious-structure-under
status: supported
confidence: 0.85
tags: [scSLIDE, negative-control, overfitting, permutation]
domain: single-cell genomics
source_papers:
  - reconstructing-developmental-disease-progression-sample-level
evidence:
  - source: reconstructing-developmental-disease-progression-sample-level
    type: supports
    strength: strong
    detail: "Permuting sample identities in Psych-AD (200 synthetic samples, random case/control labels) and running the full scSLIDE workflow produced no case/control separation in PLS, diffusion, or PCA components and no DEGs along a fitted principal curve."
conditions: "Negative-control permutation experiment."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

When sample identities are permuted to remove true biological differences, scSLIDE finds no separation of synthetic cases and controls and yields no trajectory-associated differentially expressed genes — evidence that its supervised embedding does not manufacture spurious structure.

## Evidence summary

Supplementary Figure 11 of [[reconstructing-developmental-disease-progression-sample-level]]: 200 permuted synthetic samples with random labels showed no signal in cell-level PLS, sample-level diffusion, or PCA components.

## Conditions and scope

Negative-control experiment on Psych-AD.

## Counter-evidence

None; this is the control demonstrating absence of overfitting.

## Linked ideas

Supports the validity of [[scslide-builds-semi-supervised-cell-embedding]] under supervision.

## Open questions

How does the false-positive rate scale with extreme supervision or very small sample numbers?
