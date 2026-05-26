---
title: "MetaCell aggregation — single-cell coarse-graining for large-scale integration"
slug: metacell-aggregation
domain: "single-cell computational method"
status: mainstream
aliases:
  - MetaCell
  - MetaCells
  - metacell aggregation
  - metacell coarse-graining
  - SEACells
  - pseudobulk per-cluster aggregation
  - similar-cell grouping for batch correction
  - MetaCell within-dataset clustering
  - 30-cell metacell aggregation
first_introduced: "2019"
date_updated: 2026-05-26
source_url: "https://doi.org/10.1186/s13059-019-1812-2"
---

## Definition

A computational strategy that groups transcriptionally similar cells within each dataset into "MetaCells" (~30 cells each) and computes mean log-TPM expression per MetaCell for downstream analysis. Reduces technical noise and computational cost, enables cross-study integration at scale, and preserves cell-type-specific biological variation.

## Key variants

- Original MetaCell (Baran et al. 2019).
- SEACells.
- MAESTRO-integrated MetaCell as used in TabulaTIME ([[foundations/tabulatime-pan-cancer-resource]]) — ~30 cells/MetaCell with CCA integration downstream.

## Known limitations

- Aggregation can mask rare cell states (≤MetaCell size).
- Resolution-batch tradeoff: smaller MetaCells preserve resolution but reduce batch-correction benefit.

## Relevance to active research

Enables integration of millions of cells without GPU-scale memory — a practical prerequisite for pan-cancer references like TabulaTIME and for any future hypoxia-corpus scRNA-seq mega-atlas.
