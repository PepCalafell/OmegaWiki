---
title: "MuSiC — multi-subject single-cell bulk deconvolution"
slug: music-deconvolution
domain: methods
status: mainstream
aliases:
  - MuSiC
first_introduced: "2019"
date_updated: 2026-05-28
source_url: "https://doi.org/10.1038/s41467-018-08023-x"
---

## Definition

MuSiC (MUlti-Subject SIngle-Cell deconvolution) estimates cell-type proportions in bulk RNA-seq from a single-cell reference, weighting genes by cross-subject and cross-cell consistency rather than using a fixed signature matrix. It uses weighted non-negative least squares with marker-gene weights that down-weight genes with high inter-subject variability.

## Intuition

A fixed signature matrix (as in CIBERSORT) ignores that some marker genes are unstable across donors. MuSiC instead learns gene weights from multi-subject single-cell data so that consistent, cell-type-specific genes dominate the regression, improving robustness across cohorts.

## Formal notation

Solves weighted NNLS: minimize over proportions p the weighted residual of bulk = reference × p, with weights derived from cross-subject and within-cell-type relative variance.

## Key variants

- MuSiC2 — extends to disease/condition mismatch between reference and bulk.
- Tree-guided (hierarchical) MuSiC for closely related cell types.

## Known limitations

- Designed for transcriptomics; assumes distributional properties (counts) unsuitable for proteomic/metabolomic data.
- Performance degrades when reference omits cell types present in the tissue (incomplete reference).
- Single-omics only.

## Open problems

Extending consistency-weighting to non-count omics and to references with missing cell types.

## Relevance to active research

A standard transcriptomic deconvolution baseline; used as a comparison method by newer universal frameworks such as DECODE.
