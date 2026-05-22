---
title: "Hierarchical stable cluster solutions reflect cancer-wide, individual-tumour, and intratumour cancer states in NSCLC"
slug: hierarchical-stable-cluster-solutions-reflect-cancer
status: supported
confidence: 0.75
tags:
  - NSCLC
  - LUAD
  - intratumor-heterogeneity
  - spatial-transcriptomics
  - CosMx
  - methodological
domain: oncology
source_papers:
  - cellcharter-reveals-spatial-cell-niches-associated
evidence:
  - source: cellcharter-reveals-spatial-cell-niches-associated
    type: supports
    strength: moderate
    detail: "Fig. 4b,c: NSCLC CosMx cohort (5 patients, 8 sections) has three stable cluster solutions at n=3, n=8, n=20. At n=3 a single shared tumour-enriched cluster spans all patients; at n=8 each patient has a private tumour cluster; at n=20 each patient shows multiple private tumour clusters reflecting distinct cancer-cell states."
conditions: "NSCLC CosMx-only; whether the hierarchy generalises to other tumour types untested in this paper."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

Stable cluster solutions selected at different cluster counts naturally reveal a biological hierarchy: low-n captures cancer-wide commonalities, mid-n captures individual-tumour identity, high-n captures intratumour cell-state heterogeneity.

## Evidence summary

Supplementary Table 1 documents tumour-enriched cluster composition (≥85–90% tumour cells, with ≥90% of tumour cells in those clusters) per stable n.

## Open questions

- Is this hierarchy reproducible in larger cohorts (e.g., 50+ patients) and across diverse cancer types?
- Could it be formalised as a multi-resolution clustering output rather than three discrete solutions?
