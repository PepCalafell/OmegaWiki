---
title: "ESTIMATE immune scores from bulk proteome separate immune-hot (blood, melanoma) from immune-cold (prostate, brain, ovary) tumors"
slug: estimate-immune-score-cold-hot-tumors-tpcpa
status: supported
confidence: 0.85
tags: [estimate, immune-infiltration, hot-cold-tumor, proteome]
domain: oncology
source_papers:
  - pan-cancer-proteome-atlas-mass-spectrometry
evidence:
  - source: pan-cancer-proteome-atlas-mass-spectrometry
    type: supports
    strength: strong
    detail: "ESTIMATE algorithm applied to bulk protein data assigns highest immune scores to non-solid blood cancers and melanoma, and lowest immune scores to prostate, high-grade glioma, and ovarian cancers — consistent with the established 'hot' vs 'cold' immunotherapy-response framework."
conditions: "ESTIMATE was designed for transcriptional data; here applied to bulk protein expression."
date_proposed: 2026-05-25
date_updated: 2026-05-25
---

## Statement
Application of the ESTIMATE algorithm to bulk TPCPA protein expression recapitulates the immune hot–cold tumor distinction: blood and melanoma rank highest in immune score; prostate, brain (high-grade glioma) and ovarian cancers rank lowest — concordant with their poor response to immune checkpoint inhibitors.

## Evidence summary
- Knol et al. 2025 Figure 4A.
- Hot/cold tumor framework documented in prior immuno-oncology literature (ref 69).

## Conditions and scope
- ESTIMATE was developed and validated on transcriptional data; protein-level application is an extrapolation, but bulk-tissue immune-score patterns appear coherent with RNA-level findings.

## Counter-evidence
- Within solid cancers, individual sample immune scores are heterogeneous and not strictly cancer-type-defined.

## Linked ideas

## Open questions
- Does protein-level ESTIMATE improve prediction of ICI response over transcriptional ESTIMATE on matched cohorts?
