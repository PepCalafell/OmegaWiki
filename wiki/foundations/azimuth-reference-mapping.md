---
title: "Azimuth — query-to-reference scRNA-seq mapping"
slug: azimuth-reference-mapping
domain: "computational-biology / methods"
status: mainstream
aliases:
  - "Azimuth"
  - "reference-based scRNA-seq mapping"
  - "Seurat Azimuth"
  - "query mapping single-cell"
  - "reference-projection scRNA-seq"
  - "cell-type label transfer Azimuth"
  - "Hao et al. 2021 Azimuth"
  - "weighted-nearest-neighbor reference mapping"
first_introduced: "Hao, Hao et al. 2021 *Cell*"
date_updated: 2026-05-06
source_url: "https://azimuth.hubmapconsortium.org/"
---

## Definition

Azimuth is a reference-based scRNA-seq mapping tool built on Seurat that projects an unannotated "query" dataset onto an integrated, annotated "reference" atlas. It supports automatic cell-type label transfer, projection of the query into the reference UMAP, and per-cell annotation confidence scores.

## Intuition

Once a high-quality cross-dataset atlas exists (e.g. MoMac-VERSE for monocytes/macrophages, the human PBMC reference, the human lung atlas), new datasets do not need to be re-integrated from scratch. Azimuth's task is to embed each query cell into the reference space and inherit its annotation, enabling rapid harmonisation across studies.

## Formal notation

- Input: query scRNA-seq + a chosen reference atlas (Seurat object with annotated metadata + SPCA + UMAP model)
- Method: anchor finding via supervised-PCA (sPCA) of the reference, then weighted-nearest-neighbor (WNN) label transfer
- Output: query cells with predicted cell-type labels, prediction-score per cell, and projected UMAP coordinates

## Key variants

- Azimuth web app (browser-based, mainstream references)
- Azimuth R package (programmatic, custom references)
- scArches / scANVI — alternative deep-learning reference mapping

## Known limitations

- Fails or mis-labels for cell types absent from the reference
- Confidence scores correlate with but do not guarantee annotation correctness
- Reference atlases need maintenance as new cell types are discovered

## Open problems

- Query cells from disease-specific contexts may not be well represented in healthy references
- Cross-species reference mapping is still imperfect

## Relevance to active research

[[papers/cross-tissue-single-cell-landscape-human]] validates the MoMac-VERSE by Azimuth-mapping three new query datasets — rheumatoid arthritis synovial tissues (Kuo 2019), COVID-19 PBMCs (Silvin 2020), and COVID-19 BAL (Liao 2020) — and recovers each study's main reported populations within the MoMac-VERSE clusters, establishing Azimuth + MoMac-VERSE as a unified annotation platform.
