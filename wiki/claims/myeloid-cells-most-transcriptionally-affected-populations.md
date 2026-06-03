---
title: "Myeloid cells are the most transcriptionally affected populations across COVID-19 sample axes"
slug: myeloid-cells-most-transcriptionally-affected-populations
status: supported
confidence: 0.8
tags: [COVID-19, myeloid, monocytes, transcriptome-wide-impact]
domain: immunology
source_papers:
  - reconstructing-developmental-disease-progression-sample-level
evidence:
  - source: reconstructing-developmental-disease-progression-sample-level
    type: supports
    strength: moderate
    detail: "TRADE-based transcriptome-wide impact across DC1-DC3: all major immune types showed measurable impact but myeloid cells (CD14/CD16 monocytes, dendritic cells) were most strongly affected; reproduced across datasets."
conditions: "Measured via TRADE-based TI on NB-GLM coefficients."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Across the three COVID-19 sample-level axes, myeloid cells — especially CD14 and CD16 monocytes and dendritic cells — show the largest transcriptome-wide impact, with the prioritization reproducible across independent datasets.

## Evidence summary

Supplementary Figure 3 and Figure 2k of [[reconstructing-developmental-disease-progression-sample-level]], using the [[trade-transcriptome-wide-impact]] model on gene-level NB-GLM coefficients. Among lymphoid cells, naive CD4 T cells were elevated along DC1, MAIT/memory CD4 T along DC2/DC3.

## Conditions and scope

Quantified by transcriptome-wide impact; reproduced on the independent COVID-19 cohort.

## Counter-evidence

None reported.

## Linked ideas

Uses [[trade-transcriptome-wide-impact]]; supports [[scslide-cell-type-prioritization-more-reproducible]].

## Open questions

Whether the same myeloid dominance holds in tissue (vs blood) COVID-19 datasets.
