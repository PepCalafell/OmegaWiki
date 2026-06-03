---
title: "scSLIDE cell-type prioritization is more reproducible across datasets than Augur"
slug: scslide-cell-type-prioritization-more-reproducible
status: supported
confidence: 0.8
tags: [scSLIDE, Augur, cell-type-prioritization, reproducibility, benchmark]
domain: single-cell genomics
source_papers:
  - reconstructing-developmental-disease-progression-sample-level
evidence:
  - source: reconstructing-developmental-disease-progression-sample-level
    type: supports
    strength: moderate
    detail: "Augur prioritized naive CD4 T cells above all myeloid types in one COVID-19 dataset but not the other; its binary single-variable design is confounded by additional heterogeneity, whereas scSLIDE's TI-based prioritization was reproducible."
conditions: "Comparison on two COVID-19 datasets."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

scSLIDE's transcriptome-wide-impact-based cell-type prioritization reproduces across independent COVID-19 datasets more reliably than Augur, whose binary single-variable design can be confounded by additional sources of sample heterogeneity.

## Evidence summary

Figure 2l of [[reconstructing-developmental-disease-progression-sample-level]]: Augur ranked naive CD4 T cells above all myeloid populations in one dataset but not the other; scSLIDE's prioritization was stable.

## Conditions and scope

Demonstrated on two COVID-19 datasets; argument is that binary comparisons cannot disentangle coexisting axes.

## Counter-evidence

Augur remains a valid tool for clean single-variable contrasts.

## Linked ideas

Contrasts [[augur-cell-type-prioritization]] with [[trade-transcriptome-wide-impact]].

## Open questions

Cross-method reproducibility on tissue atlases with stronger batch structure.
