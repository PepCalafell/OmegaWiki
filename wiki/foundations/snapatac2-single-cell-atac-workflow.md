---
title: "SnapATAC2 — single-cell ATAC analysis workflow"
slug: snapatac2-single-cell-atac-workflow
domain: single-cell genomics
status: mainstream
aliases:
  - SnapATAC2
first_introduced: "2024 (Zhang et al., Nature Methods)"
date_updated: 2026-06-04
source_url: "https://doi.org/10.1038/s41592-023-02139-9"
---

## Definition

SnapATAC2 is a scalable Python framework for single-cell ATAC-seq (and multiome) analysis covering dimensionality reduction, clustering, and peak calling. It wraps MACS3 for calling accessible chromatin peaks from per-cell-type fragment pileups.

## Intuition

It is engineered to handle millions of cells, performing memory-efficient spectral embedding and cell type–resolved peak calling so that candidate cis-regulatory elements can be defined per immune cell type at population scale.

## Formal notation

Peaks are called by MACS3 within the workflow and standardized to fixed-width windows (CIMA used 501-bp windows centered on the peak summit), yielding a per-cell-type cCRE catalog.

## Key variants

- SnapATAC2 + MACS3 peak calling
- Fixed-width cCRE definition (e.g. 501 bp)

## Known limitations

- Peak calling sensitivity depends on cell-type abundance and depth.
- Fixed-width windows may merge or split adjacent regulatory elements.

## Open problems

- Harmonizing peak sets across datasets and platforms.

## Relevance to active research

Used in [[papers/chinese-immune-multi-omics-atlas]] to call 338,036 cCREs (501-bp windows) across immune cell types via MACS3 within the SnapATAC2 workflow.
