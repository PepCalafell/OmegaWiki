---
title: "Cancer cell fraction (CCF)"
slug: cancer-cell-fraction-ccf
domain: "genomics"
status: mainstream
aliases:
  - CCF
  - cancer cell fraction
  - clonality estimation
first_introduced: "2013"
date_updated: 2026-06-15
source_url: "https://en.wikipedia.org/wiki/Tumour_heterogeneity"
---

## Definition

CCF is the estimated fraction of tumor cells carrying a given somatic mutation, computed from variant allele frequency adjusted for tumor purity and local copy number. CCF ≈ 1 indicates a clonal (truncal) mutation present in essentially all tumor cells; lower CCF indicates a subclonal mutation acquired later.

## Intuition

A mutation found in every tumor cell (CCF ~1) most likely arose early and initiated the tumor; mutations in only a subset arose later during clonal evolution.

## Key variants

- Purity/ploidy-corrected CCF from WES/WGS
- Multi-region CCF for clonal architecture reconstruction

## Known limitations

Depends on accurate purity and copy-number estimates; uncertainty widens at low coverage or low purity.

## Open problems

- Robust CCF estimation from low-input or FFPE samples

## Relevance to active research

In Arenillas et al., EPAS1 mutations had median CCF ≈ 0.99–1.0 in both normoxic and hypoxic PPGL cohorts, supporting EPAS1 as a tumor-initiating (truncal) event.
