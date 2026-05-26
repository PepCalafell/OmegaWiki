---
title: "Scanpy — single-cell analysis in Python"
slug: scanpy
domain: "methods / single-cell / software"
status: mainstream
aliases:
  - Scanpy
  - scanpy
  - sc.pp
  - Wolf Scanpy
  - Theis Scanpy
  - scanpy library
  - Python single-cell pipeline
  - SCANPY large-scale single-cell
  - scverse scanpy
first_introduced: "Wolf, Angerer & Theis 2018 Genome Biology"
date_updated: 2026-05-26
source_url: "https://github.com/scverse/scanpy"
---

## Definition

Scanpy is a scalable Python toolkit for analyzing single-cell gene expression data. It implements preprocessing, visualization, clustering (Leiden/Louvain), trajectory inference (PAGA), differential expression, and integration. Built around the AnnData container and now the foundational pillar of the scverse ecosystem.

## Strengths

- Tight integration with AnnData / scverse ecosystem.
- Scalable to millions of cells.
- Widely used baseline; many downstream tools accept Scanpy outputs.

## Known limitations

- Default Leiden clustering on PCA-reduced expression does not respect spatial geometry — a recurring weakness when applied to spatial transcriptomics, motivating dedicated spatial methods.

## Relevance to active research

Used as a non-spatial clustering baseline in [[papers/novae-graph-based-foundation-model-spatial]] and as the underlying ecosystem for AnnData / SpatialData workflows across the spatial-omics methods covered in this wiki.
