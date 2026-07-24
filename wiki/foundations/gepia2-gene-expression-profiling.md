---
title: "GEPIA2 — Gene Expression Profiling Interactive Analysis 2"
slug: gepia2-gene-expression-profiling
domain: "bioinformatics / cancer genomics tools"
status: mainstream
aliases:
  - "GEPIA2"
  - "GEPIA"
  - "Gene Expression Profiling Interactive Analysis"
first_introduced: "Tang et al. 2019 (Nucleic Acids Res)"
date_updated: 2026-07-24
source_url: "http://gepia2.cancer-pku.cn/"
---

## Definition

GEPIA2 is a web server for interactive analysis of RNA-seq expression data from TCGA and GTEx. It provides differential-expression, correlation, and survival (Kaplan–Meier) analyses across cancer types, including custom multi-gene signature scoring, without requiring local processing of the underlying cohorts.

## Intuition

A point-and-click front end to TCGA/GTEx: paste a gene or a gene-signature list, pick a tumor type (e.g. LIHC, CESC), and get correlation-with-a-gene and overall-survival curves — the route the source paper used to link its in vitro HIF-1α protein signatures to patient outcomes.

## Formal notation

- Data: TCGA + GTEx RNA-seq (TPM)
- Signature survival: cohort split into high vs low signature-expression groups; log-rank test
- Cancer codes used here: LIHC (liver HCC), CESC (cervical carcinoma)
- Underlying resource: [[tcga-the-cancer-genome-atlas]]

## Key variants

- Related survival/expression portals: cBioPortal, UALCAN, Kaplan–Meier Plotter

## Known limitations

- Bulk RNA-seq only — no protein-level or single-cell resolution; signature scoring uses mRNA as a proxy for the measured proteome
- Standardized processing may not match cohort-specific covariate adjustment
- Correlation/survival associations are not causal

## Open problems

- Reconciling protein-level (in vitro) signatures with mRNA-based (in vivo) survival readouts

## Relevance to active research

Tool used to show that Huh7-derived normoxic and hypoxic HIF-1α-dependent protein signatures correlate with HIF1A expression and poor survival in LIHC patients. Relevant to cancer-genomics and hypoxia-signature themes.
