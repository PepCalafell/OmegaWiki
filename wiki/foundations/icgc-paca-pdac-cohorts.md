---
title: "ICGC PACA-CA and PACA-AU — external validation cohorts for PDAC"
slug: icgc-paca-pdac-cohorts
domain: "datasets / bulk transcriptomics"
status: mainstream
aliases:
  - "PACA-CA"
  - "PACA-AU"
  - "ICGC pancreatic cohorts"
  - "ICGC PDAC validation cohorts"
  - "PACA-CA Canada PDAC"
  - "PACA-AU Australia PDAC"
first_introduced: "ICGC Pan-Cancer project; Biankin et al. 2012 Nature (PACA-AU)"
date_updated: 2026-05-25
source_url: "https://dcc.icgc.org/"
---

## Definition

Two ICGC pancreatic-cancer cohorts widely used as external validation for PDAC prognostic models: PACA-CA (Canada, ~142 samples post-QC) and PACA-AU (Australia, ~76 samples post-QC).

## Intuition

Independent cohorts that complement TCGA-PAAD for external validation of bulk RNA-seq prognostic signatures derived in TCGA training.

## Formal notation

- PACA-CA: ~142 samples with usable follow-up.
- PACA-AU: ~76 samples with usable follow-up.

## Key variants

- COMPASS / PanCuRx cohorts as additional validation in modern PDAC modelling.

## Known limitations

- Smaller sample sizes than TCGA-PAAD.
- Batch effects vs TCGA-PAAD due to different sequencing platforms and tissue handling.

## Open problems

- Joint-cohort modelling (TCGA + PACA-CA + PACA-AU + COMPASS) with consistent normalisation remains underused.

## Relevance to active research

PACA-CA and PACA-AU are used as external validation cohorts for the 13-gene hypoxia signature in [[papers/development-hypoxia-responsive-macrophage-prognostic-model]] (S1, S2 Fig).
