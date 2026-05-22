---
title: "CellCharter — spatial niche identification framework"
slug: cellcharter-framework
domain: "methods / spatial-transcriptomics / spatial-proteomics"
status: mainstream
aliases:
  - CellCharter
  - CellCharter framework
  - CellCharter algorithm
  - CellCharter spatial clustering
  - Ciriello CellCharter
  - cellcharter scverse
  - cellcharter NSCLC spatial niche tool
  - VAE+l-hop neighborhood GMM clustering
first_introduced: "Varrone et al. 2023/2024 *Nat. Genet.* (originally bioRxiv 2023)"
date_updated: 2026-05-22
source_url: "https://github.com/CSOgroup/cellcharter"
---

## Definition

CellCharter is a modular, technology-agnostic algorithmic framework for identifying, characterizing, and comparing cellular niches in spatially resolved omics datasets (proteomics, transcriptomics, ATAC, multiome). It couples (a) data-type-specific variational autoencoders for dimensionality reduction and batch correction, (b) an `l`-hop spatial neighborhood feature concatenation, (c) Gaussian mixture model (GMM) clustering with stability selection via the Fowlkes–Mallows Index, and (d) downstream modules for cluster cell-type enrichment, cluster neighborhood enrichment (NE, symmetric and asymmetric), differential NE, and cluster shape descriptors (curl, elongation, linearity, purity).

## Workflow

1. Encode spatial omics input (cells × features + x,y) with a data-type-appropriate VAE for embedding and batch correction.
2. Build a cell/spot proximity network; for each cell A concatenate its features with feature averages of its 1..l-step neighborhoods.
3. Cluster the concatenated embeddings with GMM, repeating runs to compute Fowlkes–Mallows stability and select stable solutions (n, n−1, n+1 agree).
4. Downstream: cluster proportions, cell-type enrichment, cluster NE / differential NE, cluster shape characterization.

## Strengths

- Scales to hundreds of samples and millions of cells (lowest memory among benchmarked methods; 4× faster than STAGATE on 707k cells).
- Joint multi-sample clustering with batch correction.
- Technology-agnostic: tested on Visium, CODEX, CosMx, MERFISH, IMC, and RNA+ATAC multiome.
- scverse-compatible — composable with Squidpy / scanpy ecosystem.

## Known limitations

- Performance on individual samples may be matched or exceeded by graph-attention methods (STAGATE wins single-sample ARI on DLPFC).
- VAE choice must be matched to assay type — multi-modal integration relies on the right encoder per modality.
- Stable cluster count is heuristic (cluster stability curve) — domain expert must interpret which stable solution is biologically meaningful.

## Open problems

- Integrating histology / morphology embeddings with molecular features.
- Standardized comparison across pipelines that differ in cell segmentation and signature scoring.

## Relevance to active research

CellCharter underpins the lung-cancer TAN-hypoxia niche discovery in [[papers/cellcharter-reveals-spatial-cell-niches-associated]] and is a central methodological tool for the spatial-niche detection topic; it sits adjacent to spatial-domain-detection methods benchmarked in [[papers/systematic-benchmarking-computational-methods-identify-spatially]].
