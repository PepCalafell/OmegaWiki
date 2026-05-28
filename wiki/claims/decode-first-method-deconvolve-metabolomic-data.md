---
title: "DECODE is the first method to deconvolve metabolomic data"
slug: decode-first-method-deconvolve-metabolomic-data
status: supported
confidence: 0.8
tags: [deconvolution, metabolomics, novelty]
domain: methods
source_papers:
  - decode-deep-learning-based-common-deconvolution
evidence:
  - source: decode-deep-learning-based-common-deconvolution
    type: supports
    strength: strong
    detail: "Authors state dedicated deconvolution tools for metabolomic data were lacking; DECODE demonstrated on three single-cell metabolomics datasets (mouse liver, mouse bone marrow, human colorectal cancer)."
conditions: "Limited to the small single-cell metabolomics datasets currently available (244, 107, 112 metabolite features)."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

DECODE is the first deconvolution method to address metabolomic data, filling a previously unmet methodological gap.

## Evidence summary

"Notably, dedicated deconvolution tools for metabolomic data are still lacking" (p.599). DECODE was evaluated on mouse liver, mouse bone marrow and human colorectal cancer single-cell metabolomics, outperforming all baselines on most metrics (Fig. 3c).

## Conditions and scope

Holds for the currently available single-cell metabolomics datasets, which are few and tissue-limited.

## Counter-evidence

DECODE is only slightly inferior to MuSiC on CCC for the mouse liver dataset.

## Linked ideas

## Open questions

Whether the advantage holds as larger and more diverse single-cell metabolomics references appear.
