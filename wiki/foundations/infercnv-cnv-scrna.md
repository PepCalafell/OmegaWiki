---
title: "inferCNV — Copy-number inference from scRNA-seq"
slug: infercnv-cnv-scrna
domain: methods
status: mainstream
aliases:
  - inferCNV
  - infer CNV
  - siCNV
  - scRNA CNV inference
  - copy-number from single-cell transcriptomics
  - CNV calling from scRNA-seq
  - inferCNV algorithm
first_introduced: ""
date_updated: 2026-05-25
source_url: ""
---

## Definition
inferCNV (and the related siCNV) estimates chromosome-arm copy-number alterations from single-cell or spatial transcriptomic data by sliding-window smoothing of expression along the genome and comparing against a non-malignant reference, exposing aneuploid malignant cell populations even when no DNA-seq is available.

## Relevance to active research
Used to detect CNVs in precancerous lesions of oesophageal SCC, head-and-neck and pancreatic ductal adenocarcinoma, distinguishing cancer-specific from stage-specific acquisition of large-scale chromosomal events.
