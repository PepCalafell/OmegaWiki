---
title: "STARmap — Spatially-resolved Transcript Amplicon Readout Mapping"
slug: starmap-in-situ-sequencing
domain: "spatial-transcriptomics / in-situ-sequencing"
status: mainstream
aliases:
  - "STARmap"
  - "STARmap PLUS"
first_introduced: "Wang et al. Science 2018"
date_updated: 2026-05-27
source_url: "https://www.starmapresources.com/"
---

## Definition

STARmap is an in-situ sequencing-by-ligation method that amplifies and barcodes mRNA targets within intact 3D tissue. Each round of sequencing reads one base of the gene barcode, yielding combinatorial gene identification at single-molecule resolution while preserving 3D spatial context.

## Intuition

Combines hydrogel-based tissue clearing with rolling-circle amplification and SEDAL sequencing chemistry. Enables high-plex spatial transcriptomics across thicker tissue sections, useful for cortical layer architecture.

## Known limitations

- Requires custom probe design and specialized reagents.
- Probe sets typically limited to a few hundred to ~1,000 genes per experiment.

## Relevance to active research

Visual cortex STARmap data is a standard benchmark for tissue-domain detection methods (NiCo, CellCharter, SpaGCN, Stagate, Banksy, SpatialPCA).
