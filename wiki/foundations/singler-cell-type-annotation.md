---
title: "SingleR — reference-based automated cell-type annotation for scRNAseq"
slug: singler-cell-type-annotation
domain: "computational-biology / methods"
status: mainstream
aliases:
  - "SingleR"
  - "Aran SingleR"
  - "reference-based cell type annotation"
  - "automated scRNAseq cell typing"
  - "correlation-based cell-type assignment"
  - "Spearman SingleR"
  - "Human Primary Cell Atlas reference"
  - "Aran 2019 SingleR"
  - "cell-type reference annotation"
first_introduced: "Aran et al. 2019 *Nat Immunol*"
date_updated: 2026-05-13
source_url: "https://bioconductor.org/packages/release/bioc/html/SingleR.html"
---

## Definition

SingleR is an R/Bioconductor tool for automated cell-type annotation of scRNAseq data by reference-based correlation scoring. Given a reference expression profile of pre-annotated cell types (e.g., Human Primary Cell Atlas, ImmGen, Monaco immune), SingleR computes per-cell Spearman correlation with each reference type and assigns the best match, refined by fine-tuning over top hits.

## Workflow

1. Choose a reference dataset (e.g., HumanPrimaryCellAtlasData() from celldex).
2. Provide normalized query expression matrix.
3. SingleR computes pairwise Spearman correlation between each query cell and each reference profile (per cell type, using a subset of marker genes).
4. Assigns the cell type with highest correlation; fine-tunes by recomputing correlations using only top candidates.
5. Outputs per-cell labels + pruned/empty labels for low-confidence cells.

## Strengths

- Reproducible, automated, no manual cluster annotation needed.
- Multiple reference panels available (immune, pan-tissue, organ-specific).
- Per-cell (not per-cluster) annotation — handles cluster heterogeneity.

## Limitations

- Reference panels are bulk-RNAseq-derived; novel cell states absent from the reference will be misassigned.
- Correlation-based — sensitive to feature selection.
- Cell-type granularity is bounded by reference granularity.

## Use cases in this corpus

- [[papers/using-pan-cancer-atlas-investigate-tumour]] uses SingleR with the Human Primary Cell Atlas reference (ref 112) to validate that the 23-cluster TAM-only atlas is composed of macrophages/monocytes (not contaminating cell types).

## Relevance to active research

- [[papers/using-pan-cancer-atlas-investigate-tumour]] — Coulton et al. 2024.
