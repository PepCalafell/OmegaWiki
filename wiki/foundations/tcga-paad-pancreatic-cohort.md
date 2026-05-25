---
title: "TCGA-PAAD — TCGA Pancreatic Adenocarcinoma cohort"
slug: tcga-paad-pancreatic-cohort
domain: "datasets / bulk transcriptomics"
status: mainstream
aliases:
  - "TCGA-PAAD"
  - "TCGA pancreatic adenocarcinoma cohort"
  - "PAAD project"
  - "Pancreatic Adenocarcinoma TCGA cohort"
first_introduced: "TCGA Research Network 2017 Cancer Cell (Bailey et al.)"
date_updated: 2026-05-25
source_url: "https://portal.gdc.cancer.gov/projects/TCGA-PAAD"
---

## Definition

The TCGA pancreatic adenocarcinoma project — bulk RNA-seq, SNV/CNV, methylation, and clinical/survival data on ~178 primary pancreatic cancer cases (typically ~150–160 after standard QC filters that exclude samples missing survival or clinical metadata).

## Intuition

TCGA-PAAD is the default bulk-cohort training ground for PDAC prognostic models. Its modest size (vs liquid or lung TCGA cohorts) is a known limitation but it remains the most widely used annotation-rich PDAC cohort for survival modelling.

## Formal notation

- Bulk RNA-seq (Illumina HiSeq) + clinical/survival + somatic mutation + CNV.
- Typical analytic n after QC: 150–160 primary tumours (Ge 2025 uses n=159).

## Key variants

- ICGC PACA-CA (Canada) and PACA-AU (Australia) are commonly used external validation cohorts.
- CPTAC-PDA / Tempus PDA for proteomics / paired data extensions.

## Known limitations

- Small sample size relative to molecular heterogeneity.
- Limited representation of metastatic or treatment-naïve / post-treatment disease.
- Pathology mixture: ductal adenocarcinoma dominates but neuroendocrine and acinar contaminants exist in some samples.

## Open problems

- Multi-cohort integration with PACA-CA / PACA-AU / CPTAC for higher-powered prognostic modelling.

## Relevance to active research

TCGA-PAAD is the central bulk cohort in [[papers/development-hypoxia-responsive-macrophage-prognostic-model]] for univariate Cox shortlisting, LASSO-Cox training, hypoxia-score-based stratification, GSEA, mutation landscape, immune deconvolution (ESTIMATE / CIBERSORT) and oncoPredict-based chemotherapy IC50 analysis.
