---
title: "Tangram — deep-learning spatial mapping of scRNA-seq onto spatial transcriptomics"
slug: tangram-spatial-mapping
domain: "methods / spatial-transcriptomics / cross-modality-mapping"
status: mainstream
aliases:
  - "Tangram"
  - "tangram-spatial"
first_introduced: "Biancalani et al. Nat Methods 2021"
date_updated: 2026-05-27
source_url: "https://github.com/broadinstitute/Tangram"
---

## Definition

Tangram maps single cells from a scRNA-seq reference onto spatial coordinates by learning a probabilistic assignment matrix that aligns gene expression in shared genes between the two modalities. Outputs spatial predictions of all reference cells, allowing cell-type annotation and gene imputation for spatial spots.

## Intuition

Tangram solves the spatial-to-scRNA alignment problem as a non-convex optimization with cosine-similarity loss on shared gene sets, scalable via GPU. Works on both sequencing-based and imaging-based spatial data, but treats spatial cells as anchors to be filled by scRNA-seq, which is the inverse of NiCo's design.

## Known limitations

- Per-cell mapping is computationally intensive.
- Sensitive to gene-set overlap and depth differences between modalities.
- Lower benchmark performance than NiCo on intestinal MERFISH, primary motor cortex MERFISH, and mouse embryo seqFISH datasets per the NiCo benchmark.

## Relevance to active research

Widely used baseline for cell-type annotation and gene imputation in spatial transcriptomics, particularly for the Allen Brain Cell Atlas pipeline.
