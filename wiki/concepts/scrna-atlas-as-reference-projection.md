---
title: "scRNAseq atlas as a reference for query-to-atlas projection"
aliases:
  - "atlas projection"
  - "reference projection"
  - "query-to-reference mapping"
  - "atlas-based cell-type prediction"
  - "scRNAseq projection onto reference atlas"
  - "Seurat reference mapping"
  - "MapQuery"
  - "PCA projection of query onto atlas"
  - "reference-based annotation"
  - "TAM atlas as projection target"
  - "reference atlas projection"
tags:
  - scRNA-seq
  - atlas
  - projection
  - reference-mapping
  - cell-type-prediction
  - methodological
maturity: stable
key_papers:
  - using-pan-cancer-atlas-investigate-tumour
  - cross-tissue-single-cell-landscape-human
first_introduced: "Stuart et al. 2019 *Cell* Seurat V3; popularized as Azimuth (Hao et al. 2021); applied to TAMs in Coulton 2024 and Mulder 2021"
date_updated: 2026-05-13
related_concepts:
  - momac-verse-mnp-verse-atlas
  - pan-cancer-tam-atlas-23-clusters
related_foundations:
  - azimuth-reference-mapping
  - seurat-v3-integration
---

## Definition

A reference atlas — a large, well-annotated scRNAseq dataset — is used as a "reference frame" onto which smaller "query" datasets are projected. The query cells receive cluster / cell-type predictions based on their position in the reference's low-dimensional embedding. The strategy enables annotation of new datasets without re-clustering and standardizes cluster definitions across studies.

## Workflow (Seurat reference mapping, Coulton 2024 implementation)

1. Build the reference atlas with integrated normalization, batch correction (e.g., Seurat RPCA), and cluster annotation.
2. Process the query dataset with the same normalization workflow (SCT recommended).
3. Use `FindTransferAnchors` (or Azimuth) to identify anchor cells between query and reference.
4. Use `TransferData` / `MapQuery` to project PCA structure of the reference onto the query for cell-type prediction.
5. Use `IntegrateEmbeddings` / `ProjectUMAP` for visualization of the query within the reference UMAP.
6. Inspect mapping confidence; flag low-confidence cells that may represent states absent from the reference.

## Demonstrations in this corpus

- Coulton 2024 projects Luoma 2022 oral cancer TAMs onto the 23-cluster pan-cancer TAM atlas: C1QB+ TAM → 2_C3Mac; CD14+ Mono → 19_ClassMono; CXCL8+ TAM → 6_SPP1AREGMac; SPP1+ TAM → 16_ECMHomeoMac.
- Mulder 2021 (MoMac-VERSE) is also designed for query projection of mononuclear-phagocyte datasets onto a pan-tissue atlas.

## Strengths and limitations

- **Strength**: standardizes cluster definitions; allows comparison across studies; preserves rare-state resolution from the reference.
- **Strength**: identifies cancer-type-specific absences (e.g., 18_ECMMac is absent in oral cancer projection).
- **Limitation**: query cells in states absent from the reference are forced to nearest cluster — risk of mis-annotation.
- **Limitation**: batch effects between query and reference (different platforms, normalization) can degrade mapping quality.
- **Limitation**: requires query and reference to share a sufficient anchor set of cell types.

## When to use

- Annotation of new TAM or myeloid scRNAseq datasets against the Coulton 2024 atlas or Mulder 2021 MoMac-VERSE.
- Cross-study cluster comparison without re-integration.
- Discovery of cancer-type-specific or condition-specific cluster absences.

## Key papers

- [[papers/using-pan-cancer-atlas-investigate-tumour]] — Coulton et al. 2024. Demonstrates projection of oral cancer dataset onto 23-cluster TAM atlas.
- [[papers/cross-tissue-single-cell-landscape-human]] — Mulder et al. 2021. MoMac-VERSE pan-tissue MNP reference; companion projection tool.
