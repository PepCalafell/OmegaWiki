---
title: "DECODE deconvolves known cell types accurately when the single-cell reference is incomplete"
slug: decode-deconvolves-known-cell-types-accurately
status: supported
confidence: 0.75
tags: [deconvolution, robustness, incomplete-reference]
domain: methods
source_papers:
  - decode-deep-learning-based-common-deconvolution
evidence:
  - source: decode-deep-learning-based-common-deconvolution
    type: supports
    strength: moderate
    detail: "Robustness shown by incrementally adding unknown cell types to test data (lung+neutrophils, breast−vascular-lymphatic, bone-marrow+HSC) under four perturbation scenarios; DECODE outperforms others, especially on CCC."
conditions: "Evaluated by adding/removing specific cell types in three datasets; accuracy still drops at high unknown-type fractions."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

DECODE accurately recovers the relative abundances of n known cell types even when the single-cell reference omits m cell types present in the tissue (n+m total), the common real-world case.

## Evidence summary

Tested by incrementally introducing unknown cell types (e.g., neutrophils into lung transcriptomics, HSCs into bone-marrow metabolomics) and under four perturbation scenarios (Fig. 5). DECODE outperforms baselines in most comparisons, particularly on CCC.

## Conditions and scope

Instance of [[deconvolution-with-incomplete-reference]]; the denoiser pathway (stage 3) is the enabling mechanism. Some suboptimal cases in transcriptomic data.

## Counter-evidence

In transcriptomics, Scaden, scpDeconv and RCTD show lower coefficient of variation (better stability) than DECODE in all four scenarios despite comparable accuracy.

## Linked ideas

## Open questions

Identifying which unknown types are present, not merely removing their signal.
