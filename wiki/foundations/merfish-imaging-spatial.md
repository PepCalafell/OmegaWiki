---
title: "MERFISH — multiplexed error-robust fluorescence in situ hybridization"
slug: merfish-imaging-spatial
domain: spatial-transcriptomics
status: mainstream
aliases:
  - MERFISH
  - multiplexed error-robust FISH
  - Chen Moffitt Wang 2015 MERFISH
  - imaging-based spatial transcriptomics
  - in situ smFISH multiplex
  - Vizgen MERSCOPE
first_introduced: "Chen, Moffitt, Wang et al. 2015 Science"
date_updated: 2026-05-21
source_url: "https://vizgen.com/technology/"
---

## Definition

MERFISH is an imaging-based, single-molecule, single-cell-resolution spatial transcriptomics method. Probes against 30–300 target genes are encoded by an error-correcting binary barcode read out over multiple rounds of fluorescence hybridization, yielding sub-cellular RNA spot localisation.

## Intuition

Trade-off versus sequencing-based ST: gain sub-cellular spatial resolution and single-cell segmentation, lose transcriptome-wide coverage. Cell-by-gene expression matrices are derived after segmentation of cell boundaries.

## Key variants

- Vizgen MERSCOPE is the commercial implementation.
- seqFISH/seqFISH+ (Lubeck/Cai) and 10x Xenium are sibling imaging-based ST platforms.

## Known limitations

- Limited gene panel size (30–300 genes) requires hypothesis-driven panel design.
- Cell segmentation errors propagate into downstream SVG analyses.

## Relevance to active research

MERFISH is one of the 9 ST platforms (n = 5 datasets) covered by the Li et al. 2025 SVG benchmark. SVG-method behaviour on imaging-based platforms differs from Visium because of the smaller gene set and single-cell rather than spot resolution. In [[papers/cellcharter-reveals-spatial-cell-niches-associated]], 2 Vizgen MERFISH 500-marker lung-cancer samples independently replicate the hypoxic-tumour + tumour-associated-neutrophil niche identified in CosMx and IMC.
