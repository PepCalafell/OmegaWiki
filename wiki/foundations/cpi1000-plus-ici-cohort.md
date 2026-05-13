---
title: "CPI1000+ — expanded ICI-treated bulk RNAseq cohort (Litchfield lab)"
slug: cpi1000-plus-ici-cohort
domain: "clinical / immuno-oncology / cohort"
status: mainstream
aliases:
  - "CPI1000+"
  - "CPI1000 plus"
  - "Litchfield CPI1000 cohort"
  - "ICI bulk RNAseq cohort 1446"
  - "immune checkpoint inhibitor bulk RNAseq cohort"
  - "pan-cancer ICI cohort Litchfield"
  - "checkpoint inhibitor 1000+ patient cohort"
  - "RIMA-processed ICI bulk RNAseq"
first_introduced: "Litchfield et al. 2021 *Cell* (CPI1000); expanded to 1446 patients in Coulton et al. 2024 *Nat Commun* (CPI1000+)"
date_updated: 2026-05-13
source_url: "https://doi.org/10.1038/s41467-024-49885-8"
---

## Definition

CPI1000+ is an expanded version of the CPI1000 cohort (Litchfield et al. 2021, *Cell*) — a curated multi-study pan-cancer collection of pre-treatment bulk RNAseq from patients treated with immune checkpoint inhibitors (anti-PD-1, anti-PD-L1, anti-CTLA-4, combinations). The expanded version contains 1,446 patients across five cancer types: 552 bladder, 411 lung, 226 melanoma, 212 renal, and 45 gastric (refs 115-124 in Coulton 2024).

## Processing

- Read mapping, QC, and quantification via the RIMA pipeline (ref 114).
- Differential expression analysis via DESeq2 v1.36.0 with tumour type and response in the design formula.
- Pathway / signature enrichment via fgsea v1.22.0.
- FDR correction (q < 0.1) for multiple testing.

## Use cases

- Bulk-RNAseq stratification of ICI response by macrophage cluster signatures (Coulton 2024).
- Pan-cancer ICI biomarker discovery beyond TMB / PD-L1 IHC.
- TAM-fibroblast-T-cell signature combinations as multivariate response classifiers.

## Strengths and limitations

- **Strength**: largest single ICI-treated bulk RNAseq cohort with harmonized processing.
- **Strength**: covers 5 cancer types — supports pan-cancer effect inference.
- **Limitation**: heterogeneous ICI agents and timing of biopsy not stratified in all analyses.
- **Limitation**: response definition varies by source study.
- **Limitation**: bulk-RNAseq cannot resolve cell-type-specific gene expression — relies on deconvolution / signature scoring.

## Relevance to active research

- [[papers/using-pan-cancer-atlas-investigate-tumour]] uses CPI1000+ as the bulk-RNAseq stratification cohort for TAM cluster signatures, yielding the 18_ECMMac → ICI non-responder and 8_IFNGMac → ICI responder associations.
