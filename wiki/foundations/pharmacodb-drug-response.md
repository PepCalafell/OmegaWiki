---
title: "PharmacoDB — harmonised drug-response database across cell lines"
slug: pharmacodb-drug-response
domain: methods/pharmacogenomics
status: mainstream
aliases:
  - PharmacoDB
  - pharmaco-db
  - drug sensitivity database
  - AAC area above curve
  - cell line drug sensitivity AAC
  - integrated pharmacogenomic database
  - drug response cell line panels
first_introduced: "Smirnov 2018 Nucleic Acids Res"
date_updated: 2026-05-22
source_url: "https://pharmacodb.ca"
---

## Definition
PharmacoDB harmonises and integrates large pharmacogenomic resources (CCLE, GDSC, gCSI, CTRP, others) so that drug-response measures — IC50, AAC (area above the dose-response curve), and EC50 — can be queried per drug, per cell line and per tissue.

## Intuition
Different consortia use slightly different drug concentrations, replicate counts and viability assays. PharmacoDB applies a uniform pipeline so that response values across studies can be compared and used downstream.

## Key variants
- AAC-based response metric (preferred for cross-study comparison)
- IC50 / EC50 metrics
- Tissue- or panel-restricted queries

## Known limitations
- Coverage skewed toward common cancer cell lines (often missing primary tumour panels)
- AAC is monotonic but not directly clinically actionable
- Vendor variability persists despite harmonisation

## Open problems
- Linking in-vitro response to in-vivo / patient outcomes
- Incorporating combination-drug data consistently

## Relevance to active research
[[papers/spatial-transcriptomics-reveals-distinct-conserved-tumor]] queries PharmacoDB for 417 drugs across ≥25 HPV-negative HNSCC cell lines, stratifying drugs as high/low AAC before in-silico Dynamo perturbation.
