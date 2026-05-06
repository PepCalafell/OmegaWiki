---
title: "Tumour-associated TRMs upregulate MMPs, MHC-II, CCL17, CXCL9 and downregulate IL1B"
slug: trm-tumor-upregulate-mmp-mhcii-ccl17-cxcl9
status: supported
confidence: 0.85
tags:
  - TRM
  - NSCLC
  - tissue-remodelling
  - MHC-II
  - chemokines
  - antigen-presentation
domain: "immunology / oncology"
source_papers:
  - tissue-resident-macrophages-provide-pro-tumorigenic
evidence:
  - source: tissue-resident-macrophages-provide-pro-tumorigenic
    type: supports
    strength: strong
    detail: "Bulk RNA-seq + ATAC-seq of sorted alveolar TRMs from healthy and KP tumour-bearing lungs. Upregulated in tumour TRMs: peptidases (Mmp12, Mmp14, Adamdec1), integrin-binding (Tspan4), MHC-II (H2-M2, H2-AA, H2-AB1, H2-Q7), T-cell chemoattractants (Ccl17, Cxcl9). Downregulated: Il1b, inflammasome regulators (Nlrp1b), WNT pathway negative regulators (Amer2), cell-adhesion / migration genes (Ripor2, Dgkg, Fmnl3, Rasgrp4, Fmn1, Akap5). ATAC-seq confirms enhanced accessibility at Mmp12/Mmp13 loci early."
conditions: "Mouse KP orthotopic NSCLC; bulk RNA-seq and ATAC-seq of sorted alveolar TRMs at day 15 and day 30; n=3 biological replicates per condition."
date_proposed: 2026-05-06
date_updated: 2026-05-06
---

## Statement

In KP NSCLC, tumour-associated alveolar TRMs reprogram their transcriptome to upregulate matrix metalloproteinases (MMP12, MMP14, ADAMDEC1), integrin-binding proteins (TSPAN4), MHC class II molecules (H2-M2, H2-AA, H2-AB1, H2-Q7), and T-cell chemoattractants (CCL17, CXCL9), while downregulating IL1B and inflammasome regulators (NLRP1B), negative WNT regulators (AMER2), and cell-adhesion/migration genes (RIPOR2, DGKG, FMNL3, RASGRP4, FMN1, AKAP5).

## Evidence summary

- Bulk RNA-seq DEGs (limma P<0.05) at day 15 and day 30 KP NSCLC vs healthy lung TRMs
- ATAC-seq confirms enhanced chromatin accessibility at Mmp12/Mmp13 loci specifically in early lesions
- MHC-II loci remain accessible across conditions; reduced accessibility at Ripor2/Dgkg loci
- Coherent functional theme: tissue-remodelling, antigen-presentation, T-cell-chemokine secretion, inflammasome silencing

## Conditions and scope

- Mouse KP orthotopic NSCLC; n=3 replicates per condition
- Bulk-level resolution (no single-cell decomposition of TRM heterogeneity)

## Counter-evidence

- Cross-species conservation in human NSCLC TRMs not directly tested at bulk level
- Some genes (e.g., MMP12) are also upregulated by activated MDMs in chronic inflammation; selectivity to TRMs requires the lineage-tracing context

## Linked ideas

(none yet)

## Open questions

- Which transcription factors drive the MMP/MHC-II/CCL17 module in tumour TRMs (PPARG? IRF5? NF-κB?)
- Whether the IL1B/NLRP1B downregulation reflects active suppression of inflammation by the tumour
- Cross-species validation of the signature in human NSCLC alveolar macrophages
