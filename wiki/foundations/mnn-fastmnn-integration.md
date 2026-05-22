---
title: "MNN and FastMNN — mutual-nearest-neighbor scRNA-seq integration"
slug: mnn-fastmnn-integration
domain: "methods / single-cell-integration"
status: mainstream
aliases:
  - MNN
  - mutual nearest neighbors
  - mnnCorrect
  - FastMNN
  - fastMNN integration
  - Haghverdi MNN
  - Marioni MNN integration
  - batchelor fastMNN
  - mnnpy
  - cosine-normalized MNN integration
  - MNN-anchor batch correction
  - mutual nearest neighbour scRNA-seq
first_introduced: "Haghverdi et al. 2018 *Nat. Biotechnol.* (Batch effects in single-cell RNA-sequencing data are corrected by matching mutual nearest neighbors)"
date_updated: 2026-05-22
source_url: "https://bioconductor.org/packages/batchelor/"
---

## Definition

MNN identifies pairs of cells in different batches that are mutual nearest neighbors in gene-expression space, computes a per-pair correction vector, and propagates it to all cells. FastMNN, a successor in the Bioconductor `batchelor` package, performs MNN matching in PCA space for speed and outputs both a corrected gene matrix and an embedding.

## Strengths

- MNN-anchor local-matching strategy generalises well across complex batch structures — see [[claims/mnn-anchor-methods-strong-rna]].
- FastMNN embedding ranks top tier on scIB RNA tasks.
- Gene-corrected output preserves cell-cycle and HVG variation well — see [[claims/label-free-metrics-capture-trajectories-cellcycle]].

## Known limitations

- Original MNN scales poorly on large datasets (fails above ~100k cells under CPU budget) — see [[claims/scvi-scales-trvae-scgen-fail]]; FastMNN is the scalable alternative.
- PCA-based; underperforms on scATAC-seq.

## Relevance to active research

FastMNN is the Bioconductor-ecosystem default for scRNA-seq integration; the underlying MNN-anchor concept also informs Seurat v3's integration and Scanorama. Validated in [[papers/benchmarking-atlas-level-data-integration-single]].
