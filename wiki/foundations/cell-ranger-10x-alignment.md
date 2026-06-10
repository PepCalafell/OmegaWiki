---
title: "Cell Ranger — 10x Genomics alignment and quantification pipeline"
slug: cell-ranger-10x-alignment
domain: "methods / single-cell / preprocessing"
status: mainstream
aliases:
  - Cell Ranger
  - CellRanger
  - 10x Cell Ranger
first_introduced: "10x Genomics, 2016"
date_updated: 2026-06-10
source_url: "https://www.10xgenomics.com/support/software/cell-ranger"
---

## Definition

Cell Ranger is 10x Genomics' end-to-end pipeline that demultiplexes Chromium droplet sequencing reads, aligns cDNA reads to a reference transcriptome, corrects cell barcodes and UMIs, calls cells (distinguishing real cells from empty droplets), and produces a gene-by-cell count matrix. It also processes antibody-derived tag (ADT/CITE-seq) feature barcodes.

## Intuition

It converts raw FASTQ output of a 10x run into the count matrix every downstream tool (Seurat, Scanpy) consumes, hiding barcode/UMI bookkeeping behind a single `count` command.

## Key variants

- `cellranger count` (single library), `cellranger multi` (multiplexed / feature-barcode), `cellranger aggr` (aggregation across runs).
- Reference builds: GRCh38 for human; combined GRCh38+mm10 for spike-in / xenograft experiments.

## Known limitations

- Default empty-droplet and cell-calling heuristics can over- or under-call cells; many groups supplement with EmptyDrops or manual knee-point filtering.
- Closed-source alignment internals; version drift changes counts.

## Relevance to active research

The canonical first step for essentially all 10x droplet scRNA-seq and CITE-seq datasets in the corpus; quantification quality propagates to every downstream analysis.
