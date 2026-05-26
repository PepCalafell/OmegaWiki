---
title: "Four monocyte-derived macrophage states (FOLR2, TREM2, FCN1/CXCL9, FCGR2B) plus Kupffer cells partition the HCC TME mo-mac landscape"
slug: four-momac-states-hcc-tme-folr2-trem2-fcn1-fcgr2b
status: supported
confidence: 0.85
tags:
  - HCC
  - mo-mac
  - macrophage-heterogeneity
  - FOLR2
  - TREM2
  - FCN1
  - CXCL9
  - FCGR2B
  - Kupffer-cell
  - scRNA-seq
domain: "tumor immunology / single-cell genomics"
source_papers:
  - trem2-macrophages-associated-enhanced-response-pd
evidence:
  - source: trem2-macrophages-associated-enhanced-response-pd
    type: supports
    strength: strong
    detail: "scRNA-seq on tumor + adjacent liver from HCC patients (discovery + validation cohorts). Batch-aware multinomial-mixture clustering. Four mo-mac states: (1) FOLR2 (FOLR2/SEPP1/SLC40A1/F13A1/STAB1/IGF1/GPR34/RNASE1), (2) TREM2 (TREM2/GPNMB/SPP1/NUPR1/APOE/FABP4/FABP5/CAPG/CD9), (3) FCN1/CXCL9 (FCN1/THBS1/IL1R1/GPB1/PLAUR/CCL20/CXCL9/CXCL10), (4) FCGR2B (CLEC10A/CD1C/CD1E). Plus Kupffer cells (MARCO/CD5L/TIMD4/LYVE1/VCAM1/CETP/IFI27/CFP)."
conditions: "Human HCC tumor + adjacent normal liver, 10x scRNA-seq, batch-aware multinomial-mixture clustering."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Single-cell transcriptomic analysis of HCC tumor + adjacent liver identifies four mo-mac transcriptional states (FOLR2, TREM2, FCN1/CXCL9, FCGR2B) alongside resident Kupffer cells, with characteristic gene signatures matching MoMac-VERSE / NSCLC-defined mo-mac clusters.

## Evidence summary

- All four mo-mac states broadly express CD68, C1QA/B/C, CD163, GPR183.
- Distinct marker panels per cluster (see evidence detail).
- Concordant with pan-cancer MoMac-VERSE atlas.

## Conditions and scope

- HCC-specific; generalisation to other liver pathologies (HCC subtypes, cirrhotic vs non-cirrhotic) not tested here.

## Counter-evidence

- Cluster boundaries depend on the clustering method and resolution; alternative pipelines may merge/split states.

## Linked ideas

- [[concepts/trem2-tumor-associated-macrophage]]
- [[concepts/folr2-tissue-resident-macrophage]]

## Open questions

- Inter-cluster transitions / pseudotime relationships in HCC?
