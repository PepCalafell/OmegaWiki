---
title: "sci-RNA-seq3"
slug: sci-rna-seq3
domain: single-cell genomics
status: mainstream
aliases:
  - sci-RNA-seq3
  - single-cell combinatorial-indexing RNA-seq v3
first_introduced: "2019"
date_updated: 2026-06-03
source_url: ""
---

## Definition

sci-RNA-seq3 is a third-generation single-cell combinatorial-indexing RNA sequencing protocol that uses three rounds of split-pool barcoding to label the transcriptomes of very large numbers of cells (millions) without physically isolating individual cells, at low per-cell cost.

## Intuition

Instead of capturing one cell per droplet/well, cells are repeatedly distributed, barcoded, and pooled; the unique combination of barcodes a cell accumulates identifies its transcripts. Combinatorial indexing makes whole-organism and whole-embryo atlases feasible.

## Formal notation

Cell identity is encoded by the product of barcode rounds; with R rounds and B barcodes per round the addressable space is ~B^R distinct combinations.

## Key variants

- Combined with sci-Plex nuclear hashing to multiplex many individual specimens (e.g. single embryos) in one experiment.

## Known limitations

- Sparser per-cell coverage than droplet methods.
- Barcode collisions and ambient signal require careful demultiplexing.

## Open problems

- Improving sensitivity per cell while retaining throughput.

## Relevance to active research

The ZSCAPE zebrafish embryogenesis atlas analyzed by scSLIDE was generated with sci-RNA-seq3 combined with sci-Plex hashing, associating each of ~528,000 cells with one of 1,025 individual wild-type embryos — the design that enables embryo-level (sample-level) heterogeneity analysis.
