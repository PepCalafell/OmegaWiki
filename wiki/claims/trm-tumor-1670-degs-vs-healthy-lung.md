---
title: "1,670 DEGs distinguish tumour-associated TRMs from healthy-lung TRMs in NSCLC"
slug: trm-tumor-1670-degs-vs-healthy-lung
status: supported
confidence: 0.85
tags:
  - TRM
  - NSCLC
  - bulk-RNA-seq
  - DEG
  - quantitative
  - tumor-reprogramming
domain: "immunology / oncology / genomics"
source_papers:
  - tissue-resident-macrophages-provide-pro-tumorigenic
evidence:
  - source: tissue-resident-macrophages-provide-pro-tumorigenic
    type: supports
    strength: strong
    detail: "Bulk RNA-seq of FACS-sorted TRMs (CD45⁺LIN⁻CD11B⁺LY6G⁻ + alveolar TRM markers) from healthy lungs vs day-15 vs day-30 KP tumour-bearing lungs identified 1,670 DEGs (P<0.05; limma) between tumour and healthy TRMs at day 30. Of these, 1,322 DEGs were already induced in early lesions (day 15). Supplementary Table 3."
conditions: "Mouse KP orthotopic NSCLC; n=3 biological replicates per condition; ultra-low-input RNA-seq from 20,000 sorted TRMs; mm10 alignment, STAR, limma differential expression."
date_proposed: 2026-05-06
date_updated: 2026-05-06
---

## Statement

Bulk RNA-seq of FACS-sorted alveolar tissue-resident macrophages (TRMs) from KP NSCLC tumour-bearing mouse lungs identifies 1,670 differentially expressed genes (P<0.05) compared to healthy-lung TRMs, of which 1,322 are already induced in early tumour lesions (day 15).

## Evidence summary

- Sorted TRMs from healthy / day-15 / day-30 KP tumour lungs; 20,000 cells per sample, ultra-low-input RNA-seq
- mm10 alignment via STAR; limma differential expression at P<0.05
- 1,670 total DEGs at day 30; 1,322 of those already induced at day 15
- Supplementary Table 3 in the paper

## Conditions and scope

- Mouse KP orthotopic NSCLC only
- 3 biological replicates per condition (modest n)
- Bulk-level resolution; cannot resolve TRM heterogeneity within tumour

## Counter-evidence

- Not yet replicated in human NSCLC bulk or scRNA-seq datasets
- DEG counts depend strongly on threshold choice (P<0.05 unadjusted is permissive)

## Linked ideas

(none yet)

## Open questions

- Single-cell resolution of which TRM subpopulations carry the bulk-level DEG signal
- Cross-species conservation of the DEG list
- Pathway-level convergence with hypoxic / inflammation-induced macrophage programmes
