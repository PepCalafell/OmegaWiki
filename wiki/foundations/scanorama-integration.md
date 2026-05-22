---
title: "Scanorama — heterogeneous scRNA-seq integration via panoramic stitching"
slug: scanorama-integration
domain: "methods / single-cell-integration"
status: mainstream
aliases:
  - Scanorama
  - Scanorama integration
  - panoramic scRNA-seq integration
  - Hie Scanorama
  - panorama stitching single-cell
  - Scanorama embedding
  - Scanorama gene correction
  - heterogeneous scRNA-seq integration
  - MNN-anchor scRNA-seq integration
  - Scanorama batch correction
  - Berger lab Scanorama
first_introduced: "Hie et al. 2019 *Nat. Biotechnol.* (Efficient integration of heterogeneous single-cell transcriptomes using Scanorama)"
date_updated: 2026-05-22
source_url: "https://github.com/brianhie/scanorama"
---

## Definition

Scanorama finds mutual nearest neighbors (MNN) between pairs of datasets and stitches them into a panoramic representation. It outputs both a corrected gene matrix and a low-dimensional embedding. It is conceptually similar to FastMNN but with a more efficient search-and-merge strategy that scales to many datasets.

## Strengths

- Top-3 method on scIB RNA atlas tasks (embedding output) — see [[claims/scanvi-scanorama-scvi-top-rna-integration]].
- Particularly strong at preserving spatial / location variation when not confounded with batch (e.g. lung endothelial cells).
- Both gene and embedding outputs — supports both functional-gene and cluster-based downstream analyses.
- MNN-based local-anchor matching generalises well across batch structures — see [[claims/mnn-anchor-methods-strong-rna]].

## Known limitations

- PCA/SVD-based; underperforms on scATAC-seq peak/window feature space.
- Scaling required (default) — may shift toward batch removal at cost of bio-conservation.
- Hyperparameter `alpha` (alignment stringency) is important but undertuned in tutorials.

## Relevance to active research

Scanorama is the recommended label-agnostic scRNA-seq integration method for atlas-scale work in the absence of cell-type labels. Validated in [[papers/benchmarking-atlas-level-data-integration-single]].
