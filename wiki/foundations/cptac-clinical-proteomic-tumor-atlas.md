---
title: "CPTAC — Clinical Proteomic Tumor Analysis Consortium"
slug: cptac-clinical-proteomic-tumor-atlas
domain: oncology
status: mainstream
aliases:
  - CPTAC
  - Clinical Proteomic Tumor Analysis Consortium
  - CPTAC proteomics
  - CPTAC cohort
  - CPTAC tumour proteome dataset
  - NCI CPTAC
first_introduced: "Ellis et al. 2013 NCI launch"
date_updated: 2026-05-25
source_url: "https://proteomic.datacommons.cancer.gov/pdc/"
---

## Definition
The Clinical Proteomic Tumor Analysis Consortium (CPTAC) is an NCI-led multi-cohort effort generating deep TMT-based proteomic and phosphoproteomic data on multiple cancer types (renal, colorectal, breast, lung, ovarian, glioblastoma, endometrial, pancreatic, others) together with matched genomic and clinical metadata.

## Intuition
CPTAC provides the canonical deep-proteome reference for individual cancer types. Newer pan-cancer DIA-MS atlases (e.g., TPCPA) trade per-cohort depth for cross-cohort comparability and use CPTAC cohorts as external validation.

## Formal notation
- TMT-10/-11/-16 multiplexed quantification per cohort
- Hundreds of samples per cancer type with matched WES, RNA-seq, methylation
- Released through the PDC and dbGaP

## Key variants
- CPTAC-3 expansion (renal, lung, head & neck, glioblastoma, pancreatic)
- CPTAC Pan-Cancer initiative integrating multiple cohorts

## Known limitations
- TMT-based: cross-cohort batch comparability limited.
- Heterogeneous acquisition workflows across cancer types.

## Open problems
- Harmonisation with DIA-MS atlases.
- Multi-omic integration at single-sample resolution.

## Relevance to active research
The de facto external proteomic reference for new pan-cancer studies; the CPTAC kidney cohort serves as one of the held-out validation datasets for TPCPA's cancer-type classifier.
