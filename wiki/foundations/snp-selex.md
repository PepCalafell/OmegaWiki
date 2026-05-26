---
title: "SNP-SELEX (high-throughput allelic TF binding affinity by SELEX)"
slug: snp-selex
domain: "genomics / TF binding / noncoding variants"
status: mainstream
aliases:
  - "SNP-SELEX"
  - "SNP SELEX"
  - "preferential binding score"
  - "PBS SNP-SELEX"
  - "Yan SNP-SELEX"
  - "allelic SELEX"
  - "differential TF binding assay"
first_introduced: "Yan et al. *Nature* 2021 (SNP-SELEX, 95M variants)"
date_updated: 2026-05-26
source_url: ""
---

## Definition

SNP-SELEX is a SELEX-based assay that quantifies allelic differences in TF binding to noncoding variants (ref vs alt) at scale. Variants are placed in randomised flanking contexts; after multiple selection rounds, the preferential binding score (PBS) is computed from the enrichment ratio of ref vs alt sequences. A significant absolute PBS implies the variant differentially affects TF binding.

## Relevance to active research

In [[papers/multiple-overlapping-binding-sites-determine-transcription]], SNP-SELEX is used as the comparator gold standard for variant-effect prediction. PADIT-seq recovers 92.8% (HOXD13) and 96.4% (EGR1) of SNP-SELEX hits and detects ~5× more variants with subtler effects below the SNP-SELEX sensitivity threshold, while still correlating with PBS scores in custom PBM validation — establishing that overlapping-binding-sites accumulate at variant sites and explain otherwise-subthreshold variant effects.
