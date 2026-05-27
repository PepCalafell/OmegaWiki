---
title: "Anatomic site is the dominant source of variance in skin cell-type abundance across donors, sex and technical factors"
slug: site-dominates-variance-cell-abundance-skin
status: supported
confidence: 0.85
tags: [skin, variance-partitioning, anatomy, methodological]
domain: methods / dermatology
source_papers:
  - single-cell-spatial-transcriptomic-analysis-human
evidence:
  - source: single-cell-spatial-transcriptomic-analysis-human
    type: supports
    strength: strong
    detail: "Quote (p.5): 'Variance partitioning of demographic and technical covariates confirmed that the cell-type abundances largely varied by anatomic site, while quantifying other sources of variance.'"
conditions: "crumblr + variancePartition framework on MERFISH compositional data."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

Variance partitioning attributes the dominant share of cell-type-abundance variation to anatomic site, exceeding contributions from donor, sex, age and technical covariates.

## Evidence summary

[[papers/single-cell-spatial-transcriptomic-analysis-human]] Fig. 2c.

## Conditions and scope

Cohort-limited (22 donors); confounders not fully separable from site.

## Counter-evidence

None within paper.

## Linked ideas

## Open questions

- Does site dominance hold once age-matched cohorts are stratified at scale?
