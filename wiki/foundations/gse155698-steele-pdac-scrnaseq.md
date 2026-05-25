---
title: "GSE155698 — Steele et al. 2020 PDAC scRNA-seq dataset"
slug: gse155698-steele-pdac-scrnaseq
domain: "datasets / scRNA-seq"
status: mainstream
aliases:
  - "GSE155698"
  - "Steele 2020 PDAC scRNA-seq"
  - "Steele PDAC atlas"
  - "Multimodal mapping of pancreatic cancer tumor and peripheral blood immune landscape"
  - "Steele Nat Cancer 2020 dataset"
first_introduced: "Steele et al. 2020 Nature Cancer, doi:10.1038/s43018-020-00121-4"
date_updated: 2026-05-25
source_url: "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE155698"
---

## Definition

A 10x Genomics 5'-scRNA-seq dataset comprising 19 samples (16 primary PDAC tumours and 3 non-malignant pancreas tissues) with paired peripheral blood, characterising the tumour and peripheral immune landscape of pancreatic ductal adenocarcinoma.

## Intuition

GSE155698 is one of the most widely re-used reference PDAC scRNA-seq cohorts for downstream signature discovery, TAM characterisation and hypoxia / immune microenvironment work.

## Formal notation

- Platform: 10x Chromium 5' chemistry.
- Cohort: 16 primary PDAC + 3 non-malignant pancreas.
- Typical post-QC cell yields in re-analyses: ~37k tumour + ~7.3k normal cells.

## Key variants

- Different downstream re-analyses cluster the same data with varying choices (resolution, integration method), producing slightly different annotated cell-type sets.

## Known limitations

- All samples drawn from a single institution; limited representation of treatment-experienced disease.
- No FACS-sorted myeloid enrichment; rare TAM states may be under-sampled.

## Open problems

- Joint integration with other PDAC scRNA-seq cohorts (Peng 2019, Chan-Seng-Yue 2020) is non-trivial due to batch effects and tissue handling differences.

## Relevance to active research

GSE155698 underpins the scRNA-seq arm of [[papers/development-hypoxia-responsive-macrophage-prognostic-model]] (Ge et al. 2025), where it is used to identify the hypoxia-responsive macrophage subcluster from which the 13-gene prognostic signature is derived.
