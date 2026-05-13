---
title: "MANA score — mutation-associated neoantigen-reactive CD8 T-cell signature"
aliases:
  - "MANA score"
  - "mutation-associated neoantigen score"
  - "neoantigen-reactive T cell signature"
  - "CXCL13 HLA-DR neoantigen T cell signature"
  - "Caushi 2021 MANA signature"
  - "tumour-reactive CD8 signature"
  - "neoantigen-stimulated CD8 transcriptional programme"
  - "MANA T cell score"
  - "CXCL13+ tumour-reactive CD8 T cell signature"
  - "antigen-experienced tumour CD8 signature"
tags:
  - T-cell
  - neoantigen
  - CD8
  - signature
  - CXCL13
  - MHC-class-II
  - lung-cancer
maturity: emerging
key_papers:
  - using-pan-cancer-atlas-investigate-tumour
first_introduced: "Caushi et al. 2021 *Nature* (CXCL13/MHC-class-II signature of mutation-associated neoantigen-reactive CD8 T cells in lung cancer); operationalized for TAM-T cell crosstalk stratification by Coulton et al. 2024"
date_updated: 2026-05-13
related_concepts:
  - ifng-mac-cxcl9-tam-ici-responder
  - ecm-mac-collagen-producing-tam
  - pan-cancer-tam-atlas-23-clusters
---

## Definition

The mutation-associated neoantigen (MANA) score is a CD8 T-cell transcriptional signature that captures the activation programme of T cells stimulated by cancer-associated neoantigens. It is computed per CD8 T cell using a 14-gene signature derived from Caushi et al. 2021 (lung cancer neoantigen-reactive T cells), consisting of CXCL13, HLA-DRA, HLA-DRB5, HLA-DQA1, HLA-DRB1, HLA-DQB1, CCL3, GZMA, GEM, ENTPD1, HLA-DPA1, TNS3, MIR4435-2HG, HLA-DPB1.

## Computation (Coulton 2024)

1. From a CD8 T-cell scRNAseq atlas, compute per-cell MANA score via Seurat `AddModuleScore` with the 14-gene signature.
2. Per sample, compute summary MANA score (e.g., mean across CD8 cells).
3. Stratify samples by quartile (upper vs lower).
4. Compare TAM compositional proportions across MANA quartiles via Propeller with FDR correction.

## Applications

- TAM-T cell crosstalk stratification: in Coulton 2024, 18_ECMMac proportions are higher in low-MANA lung tumours (Propeller q=0.078) while 8_IFNGMac is higher in high-MANA samples (q=0.060).
- Biomarker discovery for neoantigen-reactive vs neoantigen-naive T cell states.
- Patient stratification in ICI-treated cohorts.

## Validity / limitations

- Derived from lung cancer neoantigen TCR sorting (Caushi 2021); generalization to other cancer types not formally validated.
- Signature genes (CXCL13, HLA-DR) are not unique to neoantigen-reactive T cells; chronic antigen stimulation and Tfh-like states share these markers.
- Threshold-free continuous score; cutoff choices (quartile vs median) affect downstream comparisons.

## When to use

- Stratifying T cells in tumour scRNAseq for neoantigen-responsive subpopulations.
- Sample-level comparison of TAM composition by neoantigen response state.
- Hypothesis generation for TAM-T cell crosstalk experiments.

## Key papers

- [[papers/using-pan-cancer-atlas-investigate-tumour]] — Coulton et al. 2024. MANA-stratified TAM compositional analysis in lung cancer secondary atlas (31,598 macrophages + 72,585 T cells from 7 studies).
