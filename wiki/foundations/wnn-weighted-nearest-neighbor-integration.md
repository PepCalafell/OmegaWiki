---
title: "WNN — Weighted Nearest Neighbor multimodal integration"
slug: wnn-weighted-nearest-neighbor-integration
domain: "computational biology / methods / multi-omics"
status: mainstream
aliases:
  - "WNN"
  - "weighted nearest neighbor"
  - "weighted nearest-neighbour"
  - "Seurat WNN"
  - "multimodal weighted-nearest-neighbour integration"
  - "Hao 2021 WNN"
first_introduced: "Hao et al. *Cell* 2021 (Seurat v4)"
date_updated: 2026-05-27
source_url: "https://doi.org/10.1016/j.cell.2021.04.048"
---

## Definition

WNN is a multimodal integration algorithm that learns per-cell weights for each measured modality (e.g., RNA, ATAC, DNA methylation, protein) and constructs a joint nearest-neighbour graph in which each cell's neighbours come from a modality-weighted distance metric. The weights are estimated from how well each modality predicts its own nearest neighbours relative to the other modality — effectively asking "for this cell, which modality contains the most informative local structure?".

## Intuition

A naive concatenation of modalities forces equal contribution everywhere — bad when one modality (e.g., DNA methylation) is locally noisier than another (e.g., RNA) or vice versa. WNN instead lets the data decide cell-by-cell: a cell whose state is more sharply defined by methylation gets higher methylation weight; one defined by transcription gets higher RNA weight. The output is a single weighted-knn graph usable for clustering and UMAP.

## Formal notation

- Inputs: per-modality low-dimensional embeddings (PCA, LSI, or equivalent).
- Per-cell weight: ratio of within-modality prediction error to cross-modality prediction error.
- Joint distance: weighted combination of modality-specific kNN distances.
- Outputs: WNN graph → Louvain/Leiden clustering, WNN-UMAP embedding.

## Key variants

- **WNN in Seurat v4** (Hao 2021): original implementation for CITE-seq RNA + protein.
- **WNN for spatial multi-omics**: paired with spatial barcoding for DNAm + RNA in [[papers/spatial-joint-profiling-dna-methylome-transcriptome]].
- **MOFA+, totalVI, MultiVI**: alternative latent-variable multimodal integrators — different inductive bias (Bayesian factor models / deep generative models vs WNN's local-neighbour weighting).

## Known limitations

- Weights are local — does not produce a global modality-importance ranking.
- Sensitive to per-modality embedding quality (garbage in → garbage out).
- Does not model modality-specific noise distributions explicitly.

## Open problems

- Spatial extension: weighting that also accounts for spatial neighbours, not just feature-space neighbours.
- Stable benchmarking on >2-modality datasets (RNA + methylome + ATAC + protein).

## Relevance to active research

WNN is the integration backbone used in [[papers/spatial-joint-profiling-dna-methylome-transcriptome]] to combine DNAm and RNA modalities per spatial pixel, revealing cluster structure that neither modality recovered alone (e.g., W11 = craniofacial, defined by DNAm; W6 = cardiac, defined by RNA). The WNN weight per pixel directly quantifies the relative contribution of each modality to local cell identity.
