---
title: "DBiT-seq — Deterministic Barcoding in Tissue via microfluidics"
slug: dbit-seq-deterministic-barcoding-in-tissue
domain: "genomics / methods / spatial omics"
status: mainstream
aliases:
  - "DBiT-seq"
  - "Deterministic Barcoding in Tissue"
  - "microfluidic spatial barcoding"
  - "perpendicular microchannel spatial barcoding"
  - "Liu 2020 DBiT-seq"
first_introduced: "Liu et al. *Cell* 2020"
date_updated: 2026-05-27
source_url: "https://doi.org/10.1016/j.cell.2020.10.026"
---

## Definition

DBiT-seq deposits a 2D combinatorial spatial barcode grid onto a tissue section by flowing two sets of barcoded oligonucleotides through perpendicular microfluidic channels (A1–A50 and B1–B50). The intersection of an Ai channel with a Bj channel defines a square pixel of size equal to the channel width; ligation of the perpendicular barcodes generates a tissue-coordinate-encoded library with up to 50×50 = 2,500 pixels per ROI.

## Intuition

Instead of arrayed capture spots (Visium) or imaging-based segmentation (MERFISH), DBiT-seq stamps coordinates onto the tissue itself by ligating two perpendicular barcodes in situ. Pixel size is set by channel width — 50 μm, 25 μm, 10 μm chips are routine — making it trivially scalable to near-single-cell resolution and compatible with diverse downstream chemistries (RNA, ATAC, CUT&Tag, methylation).

## Formal notation

- Barcode A set: BCA1…BCA50 in channels orthogonal to barcode B (BCB1…BCB50).
- Final read structure: `[P5-i5-S5][BCA][BCB][linker][assay molecule][i7-P7]`.
- Pixel identity: combination `(Ai, Bj)`.
- Throughput: 2,500 pixels per 5×5 mm ROI at 100 μm; same count at 10 μm covers a 0.5×0.5 mm ROI.

## Key variants

- **Spatial transcriptome DBiT-seq**: poly-T-biotin capture + template switching (Liu 2020).
- **Spatial ATAC / spatial ATAC–RNA**: Tn5 transposition replaces poly-T capture (Deng 2022; Zhang 2023).
- **Spatial CUT&Tag**: pA-Tn5 antibody-targeted transposition for histone marks.
- **Spatial-DMT**: extends DBiT-seq to DNA methylation via EM-seq conversion + splint ligation, co-profiling DNAm + RNA in the same section (see [[papers/spatial-joint-profiling-dna-methylome-transcriptome]]).
- **MOSAIC / MOSAICA**: multiplexed chromatin features + transcriptome + protein (Guo 2025).

## Known limitations

- Square-grid pixels — not native cell boundaries; requires deconvolution against a reference scRNA-seq atlas to recover cell-type composition.
- Throughput limited to a single ROI per chip; whole-organ profiling requires tiling.
- Low-resolution pixels (50 μm) average over many cells; high-resolution chips (10 μm) sacrifice ROI area.

## Open problems

- Variable-pixel chips that adapt grid size to local cell density.
- Higher-multiplex chemistries combining DNAm + ATAC + RNA + protein in a single pixel.

## Relevance to active research

DBiT-seq is the spatial-barcoding chassis underlying the entire microfluidic spatial-omics family — including the spatial DNA-methylome assay introduced in [[papers/spatial-joint-profiling-dna-methylome-transcriptome]]. Its perpendicular-channel design makes it the most assay-agnostic of the spatial-omics platforms.
