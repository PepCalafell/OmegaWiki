---
title: "Seurat V3 — scRNA-seq integration via anchors"
slug: seurat-v3-integration
domain: "computational-biology / methods"
status: mainstream
aliases:
  - "Seurat"
  - "Seurat V3"
  - "Seurat integration"
  - "CCA-anchored integration"
  - "anchor-based scRNA-seq integration"
  - "Seurat MNN"
  - "reciprocal PCA integration"
  - "Stuart et al. 2019 integration"
  - "scRNA-seq batch correction (Seurat)"
first_introduced: "Stuart, Butler et al. 2019 *Cell*"
date_updated: 2026-05-06
source_url: "https://satijalab.org/seurat/"
---

## Definition

Seurat is the most widely used R framework for single-cell RNA-seq analysis. The V3 integration workflow identifies pairwise mutual nearest neighbours (MNN-style "anchors") between datasets after a shared canonical correlation analysis (CCA) or reciprocal PCA, and uses those anchors to learn correction vectors that align cell embeddings into a common space.

## Intuition

When the same biological cell type is sequenced across multiple datasets, batches, or technologies, Seurat finds pairs of cells across those datasets that are mutually nearest neighbours in a shared low-dimensional space. Those pairs are taken as "the same cell type" and used to compute the offset that corrects technical drift, leaving biological signal intact.

## Formal notation

- Input: a list of normalized expression matrices (gene × cell) from N datasets
- Step 1: SelectIntegrationFeatures (genes consistently variable across datasets)
- Step 2: FindIntegrationAnchors via CCA or reciprocal PCA → mutual NN pairs scored on local consistency
- Step 3: IntegrateData → corrects expression with anchor-based weights (Gaussian-decayed by anchor score)
- Output: an "integrated" assay (cell × gene) in a shared embedding suitable for clustering / UMAP

## Key variants

- Seurat V3 anchor integration (Stuart et al. 2019)
- Seurat V4 / V5 SCT-based and bridge integration (multimodal, fast paths)
- Harmony — alternative iterative correction in PCA space
- scVI — deep generative integration
- BBKNN — fast graph-based NN correction

## Known limitations

- Memory and runtime scale poorly above a few hundred thousand cells (mitigated by reciprocal PCA and reference-based modes)
- Anchors can be wrong when datasets share no common cell type, leading to over-correction
- Correction is on the embedding/expression layer only; raw counts are not re-imputed

## Open problems

- Quantitative comparison of anchor-based vs deep-learning-based integration on rare cell types
- Reference-based integration where the "query" must be projected onto a fixed atlas (see Azimuth)

## Relevance to active research

[[papers/cross-tissue-single-cell-landscape-human]] uses Seurat V3 anchor integration as the backbone for organ-level and pan-tissue MNP integration across 41 datasets and 178,651 cells, producing the MNP-VERSE and MoMac-VERSE atlases.

[[papers/using-pan-cancer-atlas-investigate-tumour]] selects Seurat V4 RPCA over CCA / Harmony / Scanorama (iLISI benchmark on a 1.5 TB RAM node) to integrate 363,315 TAMs across 32 studies, 17 cancer types into a 23-cluster pan-cancer atlas.

[[papers/benchmarking-atlas-level-data-integration-single]] benchmarks Seurat v3 (CCA and RPCA) across 13 integration tasks: Seurat v3 prioritizes batch removal at the cost of bio-conservation, performs well on simple RNA tasks, and fails to scale above ~100k cells under CPU budgets (RPCA reduces but does not eliminate this).
