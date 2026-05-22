---
title: "Batch correction is essential for joint multi-sample spatial clustering"
slug: batch-correction-essential-joint-multi-sample
status: supported
confidence: 0.85
tags:
  - batch-effect
  - spatial-transcriptomics
  - methodological
  - DLPFC
domain: methods
source_papers:
  - cellcharter-reveals-spatial-cell-niches-associated
evidence:
  - source: cellcharter-reveals-spatial-cell-niches-associated
    type: supports
    strength: strong
    detail: "Fig. 1f: without batch effect correction, CellCharter clusters in DLPFC separate by donor rather than by cortical layer; with batch correction they recover the layer structure across donors. DR.SC was excluded from runtime comparison because it does not support batch correction."
conditions: "Multi-donor / multi-batch datasets only. Single-sample clustering is unaffected."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

When jointly clustering spatial-omics samples that span donors or batches, dimensionality reduction must include a batch-correction step; otherwise the recovered clusters track batch identity, not tissue anatomy.

## Evidence summary

Fig. 1f visual comparison; absence of batch correction in DR.SC and most non-BayesSpace/UTAG tools explains a portion of their poor joint-clustering ARI.

## Conditions and scope

Quantified on DLPFC. Generalises to mouse-spleen CODEX, NSCLC CosMx, and IMC LUAD cohorts where CellCharter performs joint multi-sample clustering with VAE-level batch correction.

## Open questions

- Are existing batch-correction VAEs (scVI, totalVI, etc.) sufficient for tumour-derived spatial datasets with large biological inter-patient variability?
