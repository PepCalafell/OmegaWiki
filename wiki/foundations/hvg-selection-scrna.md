---
title: "Highly Variable Gene (HVG) selection in scRNA-seq"
slug: hvg-selection-scrna
domain: "methods / scRNA-seq-preprocessing"
status: mainstream
aliases:
  - HVG
  - highly variable genes
  - HVG selection
  - feature selection scRNA-seq
  - scanpy highly_variable_genes
  - Seurat FindVariableFeatures
  - vst HVG
  - dispersion-based HVG
  - deviance HVG
  - HVG mean variance trend
  - HVG flavor seurat scanpy cell_ranger
first_introduced: "Brennecke et al. 2013 *Nat. Methods*; refined by Satija et al. 2015 (Seurat) and Wolf et al. 2018 (Scanpy)"
date_updated: 2026-05-22
source_url: ""
---

## Definition

Highly Variable Gene (HVG) selection identifies a subset of genes (typically 2000–5000) whose variance across cells exceeds that expected from technical noise alone. It is the standard feature-selection step in scRNA-seq workflows, used to focus integration / clustering / dimensionality-reduction on biologically informative genes. Common methods: Seurat `vst` (variance-stabilising transformation), Scanpy `seurat`/`cell_ranger`/`seurat_v3` flavors, and deviance-based selection (Townes et al.).

## Strengths

- Reduces computational cost without losing most biological signal.
- Improves scRNA-seq integration outcomes in 74% of paired comparisons — see [[claims/hvg-selection-improves-integration]].
- Standardized in scanpy / Seurat with sensible defaults.

## Known limitations

- HVG selection is sensitive to batch — per-batch HVG followed by intersection / union is often required.
- Removes biology in lowly-expressed-but-relevant gene programs (e.g. cell-cycle genes are not always HVGs).
- HVG-based integration favors cluster recovery over trajectory / cell-cycle conservation.

## Relevance to active research

HVG selection is a near-universal preprocessing step in scRNA-seq analysis pipelines. The scIB benchmark validates HVG selection as generally beneficial for integration. See [[papers/benchmarking-atlas-level-data-integration-single]].
