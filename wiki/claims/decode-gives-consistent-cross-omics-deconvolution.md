---
title: "DECODE gives consistent cross-omics deconvolution on PBMC CITE-seq pseudocohorts"
slug: decode-gives-consistent-cross-omics-deconvolution
status: supported
confidence: 0.75
tags: [cross-omics, consistency, CITE-seq, deconvolution]
domain: methods
source_papers:
  - decode-deep-learning-based-common-deconvolution
evidence:
  - source: decode-deep-learning-based-common-deconvolution
    type: supports
    strength: moderate
    detail: "On a PBMC CITE-seq dataset (43,791 cells, 5 cell types), transcriptomic and proteomic pseudocohorts gave nearly identical DECODE results: low KL divergence, high Spearman correlation across 1,000 test samples (Fig. 6a–d)."
conditions: "Single CITE-seq dataset; training from donor HS1, pseudocohorts from donor HS5."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

DECODE's deconvolution results are highly consistent between transcriptomic and proteomic measurements of the same cells, enabling cross-omics cohort integration.

## Evidence summary

PBMC CITE-seq (43,791 cells; CD4 T, CD8 T, B, NK, myeloid) yielded near-identical transcriptomic vs. proteomic pseudocohort estimates, confirmed by one-tailed Wilcoxon with Bonferroni correction (Supplementary Table 5) and by low KL divergence / high Spearman correlation over 1,000 test samples (Fig. 6c,d).

## Conditions and scope

Supports [[universal-multiomics-deconvolution]]; demonstrated on one paired CITE-seq dataset.

## Counter-evidence

None reported.

## Linked ideas

## Open questions

Whether consistency holds for metabolomics-paired cohorts where references are weaker.
