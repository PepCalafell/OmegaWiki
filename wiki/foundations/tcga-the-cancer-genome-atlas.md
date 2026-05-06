---
title: "TCGA — The Cancer Genome Atlas"
slug: tcga-the-cancer-genome-atlas
domain: "data-resource / pan-cancer-genomics"
status: mainstream
aliases:
  - "TCGA"
  - "The Cancer Genome Atlas"
  - "Cancer Genome Atlas"
  - "TCGA pan-cancer"
  - "PanCancerAtlas"
  - "GDC TCGA"
  - "TCGA cohort"
first_introduced: "Collins & Barker, NCI/NHGRI launch 2006; pilot publications 2008"
date_updated: 2026-05-06
source_url: "https://portal.gdc.cancer.gov/"
---

## Definition

TCGA is a large-scale, multi-institutional NIH-funded cancer genomics resource that profiled ~11,000 primary tumors across 33 cancer types using matched DNA-seq (whole-exome and selected whole-genome), mRNA expression, miRNA expression, DNA methylation (Illumina 450k), copy-number arrays, and reverse-phase protein array (RPPA). TCGA data are the de facto reference for pan-cancer analyses and have been re-analyzed in hundreds of secondary studies.

## Intuition

TCGA is the "Hubble Telescope" of cancer genomics: a single, harmonized, deep-multi-omic snapshot of human tumors that any analyst can access. Because the assays are standardized across centers, TCGA enables apples-to-apples cross-cancer comparisons that are impossible with smaller heterogeneous datasets.

## Formal notation

- Sample size: ~11,000 cases, 33 primary cancer types
- Assays per case (varies by tumor type): WXS (whole-exome), RNA-seq, miRNA-seq, 450k methylation, SNP6 array (CNA), RPPA
- Data tiers: open (de-identified summary), controlled (germline/individual-level via dbGaP)
- Tumor-type abbreviations: BRCA (breast), LUAD (lung adeno), LUSC (lung squamous), PRAD (prostate), KIRC (kidney clear cell), KIRP (kidney papillary), THCA (thyroid), CESC (cervical squamous), HNSC (head/neck squamous), LIHC (liver hepatocellular), PAAD (pancreatic adeno), GBM (glioblastoma), LGG (lower-grade glioma), OV (ovarian serous), COADREAD (colon+rectum), BLCA (bladder urothelial), SKCM (skin cutaneous melanoma), UCEC (uterine corpus endometrial), PCPG (pheochromocytoma/paraganglioma)
- Access: NCI Genomic Data Commons (GDC) portal; Synapse/Sage; cBioPortal

## Key variants

- TCGA Pan-Cancer Atlas (2018): final harmonized reanalysis (Hoadley et al. 2018 Cell)
- ICGC (International Cancer Genome Consortium): partner consortium with overlapping cohorts plus additional WGS-focused cohorts (CPC-GENE for prostate)
- PCAWG (Pan-Cancer Analysis of Whole Genomes): WGS-only subset/extension across ICGC + TCGA

## Known limitations

- Bias toward primary, treatment-naive tumors; metastatic and treated samples are sparse.
- Demographic bias: predominantly European-ancestry; ancestry analyses (e.g., the BRCA hypoxia-ancestry signal in [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]]) are limited in non-BRCA cancer types.
- Methylation 450k array is now superseded by EPIC (850k) but most TCGA data is 450k.
- RPPA covers ~200 antibody-validated proteins per cohort; not full proteome.

## Open problems

- Integration of TCGA with newer single-cell and spatial atlases requires careful batch-correction and cell-type deconvolution.
- Statistical models for hypoxia inference from bulk mRNA confound malignant-epithelium hypoxia with stromal/immune hypoxia.

## Relevance to active research

[[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] uses TCGA across 19 tumor types (8,006 tumors) plus the CPC-GENE prostate cohort to derive the pancancer hypoxia landscape. TCGA is also the standard pan-cancer reference for survival analyses linking macrophage / hypoxia signatures to outcome in [[papers/nf-kb-tet2-promote-macrophage-reprogramming]].
