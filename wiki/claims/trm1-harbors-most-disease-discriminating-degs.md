---
title: "The Trm1 cluster harbors the most disease-discriminating DEGs between AD and PV"
slug: trm1-harbors-most-disease-discriminating-degs
status: supported
confidence: 0.85
tags: [skin, trm, deg, atopic-dermatitis, psoriasis, scrna-seq]
domain: immunology / single-cell
source_papers:
  - classification-human-chronic-inflammatory-skin-disease
evidence:
  - source: classification-human-chronic-inflammatory-skin-disease
    type: supports
    strength: strong
    detail: "Quote (p.4): 'Trm1 had a disproportionately large number of DEGs in the three comparisons (e.g., in the PV versus HC comparison, 514 DEGs for Trm1 cells compared to 197 for Tcm and 238 for eTreg1 cells).'"
conditions: "MAST DEGs, adj P < 0.001, |avg_log2FC| > 0.425, present in >=80% of disease samples."
date_proposed: 2026-06-10
date_updated: 2026-06-10
---

## Statement

Across PV-vs-HC, AD-vs-HC and AD-vs-PV comparisons, the Trm1 skin-resident memory cluster contained a disproportionately large number of robustly differentially expressed genes (e.g. 514 Trm1 DEGs in PV-vs-HC vs 197 for Tcm), making it the most informative cluster for distinguishing disease classes.

## Evidence summary

Reported in Results of [[papers/classification-human-chronic-inflammatory-skin-disease]] using [[foundations/mast-hurdle-model-single-cell-differential]]. Supports [[concepts/trm1-th2-th17-molecular-classification-inflammatory]].

## Conditions and scope

DEG counts partly track cluster size (effective sample), but Trm1 exceeded similarly sized clusters.

## Counter-evidence

MAST inflates significance for small fold changes; the >=80% heterogeneity filter mitigates this.

## Linked ideas

## Open questions

- Would deeper sampling reveal comparably discriminating signals in underpowered APC clusters?
