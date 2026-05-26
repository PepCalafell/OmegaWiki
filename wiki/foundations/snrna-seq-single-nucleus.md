---
title: "snRNA-seq — single-nucleus RNA sequencing"
slug: snrna-seq-single-nucleus
domain: single-cell genomics / methods
status: mainstream
aliases:
  - snRNA-seq
  - single-nucleus RNA-seq
  - sn-RNA-seq
  - nuclei RNA-seq
  - 10x snRNA-seq
  - DroNc-seq
  - frozen-tissue single-nucleus profiling
  - nucleus-only single-cell transcriptomics
first_introduced: "2016"
date_updated: 2026-05-26
source_url: "https://www.10xgenomics.com/products/single-cell-gene-expression"
---

## Definition

snRNA-seq profiles transcriptomes from isolated cell nuclei rather than whole cells. It is the canonical workflow for FFPE/frozen archival tissue or fragile cell types (alveolar epithelium, neurons, cardiomyocytes) where whole-cell dissociation is lossy.

## Key variants

- 10x Chromium snRNA-seq (most common)
- sNuc-DropSeq, DroNc-seq
- Multiome (snRNA + snATAC)

## Known limitations

snRNA-seq vs scRNA-seq protocol differences alter meta-programs ([[concepts/snrna-vs-scrna-metaprogram-differences]]) — nuclear-retained transcripts (e.g., MALAT1, NEAT1) over-represented; cytoplasmic-skewed transcripts (mitochondrial, ribosomal) depleted.

## Relevance to active research

Used by Peng et al. 2026 ([[papers/multimodal-spatial-omics-reveal-co-evolution]]) on 75 lung samples, retaining 401,635 nuclei to identify KACs and define meta-programs that map back to spatial ST data.
