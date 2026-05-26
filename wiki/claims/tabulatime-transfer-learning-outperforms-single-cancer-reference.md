---
title: "TabulaTIME pretrained transfer-learning model outperforms single-cancer references for automated cell-type annotation"
slug: tabulatime-transfer-learning-outperforms-single-cancer-reference
status: supported
confidence: 0.75
tags:
  - methodological
  - transfer-learning
  - cell-type-annotation
  - scrna-seq
  - tabulatime
domain: computational single-cell methodology
source_papers:
  - spatiotemporal-analyses-pan-cancer-single-cell
evidence:
  - source: spatiotemporal-analyses-pan-cancer-single-cell
    type: supports
    strength: medium
    detail: Query BRCA_GSE176078: TabulaTIME 0.762 vs NSCLC_GSE131907 0.644 vs BRCA_EMTAB8107 0.493. Query NSCLC_GSE146100: TabulaTIME 0.723 vs NSCLC_GSE131907 0.493 vs BRCA_EMTAB8107 0.462 (Fig. 8b,c).
conditions: "Two query datasets only (BRCA, NSCLC); accuracy is ~0.72-0.76, not saturated."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

A pretrained transfer-learning model built on TabulaTIME outperforms single-cancer-type scRNA-seq references for automated cell-type annotation on independent BRCA and NSCLC query datasets (0.762 and 0.723 accuracy vs ≤0.644 for single-cancer alternatives).

## Conditions and scope

Direct quote: "Accuracy: TabulaTIME 0.762 (BRCA_GSE176078), 0.723 (NSCLC_GSE146100); single-cancer references 0.462–0.644" (Han 2025, Fig. 8).

## Linked ideas

- TabulaTIME as default pan-cancer scRNA-seq query backbone in the wiki.
