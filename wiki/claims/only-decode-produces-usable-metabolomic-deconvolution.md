---
title: "Only DECODE produces usable metabolomic deconvolution under perturbation"
slug: only-decode-produces-usable-metabolomic-deconvolution
status: supported
confidence: 0.75
tags: [metabolomics, robustness, benchmark]
domain: methods
source_papers:
  - decode-deep-learning-based-common-deconvolution
evidence:
  - source: decode-deep-learning-based-common-deconvolution
    type: supports
    strength: moderate
    detail: "Under four perturbation scenarios on bone-marrow metabolomics, all methods except DECODE exhibit unusable performance (Fig. 5e); stability comparison for others was meaningless."
conditions: "Demonstrated on bone-marrow metabolomics; only DECODE yields usable results so CV comparison restricted to DECODE."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

Under noise and missing-value perturbations on metabolomic data, all comparison methods except DECODE produce unusable results.

## Evidence summary

"all methods except DECODE exhibit unusable performance on metabolomic data" (p.603). On bone-marrow metabolomics (Fig. 5e), only DECODE yields usable CCC; stability (CV) comparison was therefore restricted to DECODE.

## Conditions and scope

Shown on the available single-cell metabolomics datasets, which are small; reflects the intrinsic low-feature, low-specificity difficulty of metabolomics.

## Counter-evidence

DECODE only slightly inferior to MuSiC on CCC for the unperturbed mouse liver metabolomics dataset.

## Linked ideas

## Open questions

Whether other methods could be adapted to usable metabolomic performance.
