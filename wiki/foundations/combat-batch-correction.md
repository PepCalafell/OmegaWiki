---
title: "ComBat — empirical Bayes batch effect correction"
slug: combat-batch-correction
domain: "methods / batch-correction / bulk-and-single-cell"
status: mainstream
aliases:
  - ComBat
  - combat batch correction
  - Johnson ComBat
  - empirical Bayes batch correction
  - sva ComBat
  - ComBat-seq
  - bulk RNA batch correction
  - microarray batch correction ComBat
  - combat parametric adjustment
  - scanpy ComBat
first_introduced: "Johnson et al. 2007 *Biostatistics* (Adjusting batch effects in microarray expression data using empirical Bayes methods)"
date_updated: 2026-05-22
source_url: "https://bioconductor.org/packages/sva/"
---

## Definition

ComBat applies an empirical Bayes parametric adjustment per gene to remove batch effects in microarray, bulk RNA-seq, and scRNA-seq data. Originally a bulk method (2007), it was repurposed for single-cell data and remains in wide use as a baseline batch correction. The scanpy implementation is the standard for scRNA-seq applications.

## Strengths

- One of the fastest integration methods in scIB — see [[claims/combat-bbknn-fastest-scvi-low-memory]].
- Gene-corrected output suitable for downstream functional analysis.
- Preserves cell-cycle and HVG variation well — see [[claims/label-free-metrics-capture-trajectories-cellcycle]].
- Surprisingly strong aggregate ranking on scATAC-seq.

## Known limitations

- Linear/parametric — fails on nonlinear, nested batch structure typical of atlas data.
- No embedding output (gene matrix only).
- Underperforms on the lung and immune-human/mouse complex atlas tasks vs deep-learning methods.

## Relevance to active research

ComBat is the classical baseline against which every newer batch-correction method is compared. Validated in [[papers/benchmarking-atlas-level-data-integration-single]] as a competitive baseline on simple tasks.
