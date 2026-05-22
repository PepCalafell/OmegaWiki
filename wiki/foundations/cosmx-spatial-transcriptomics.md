---
title: "CosMx Spatial Molecular Imager — NanoString in situ multiplex transcriptomics"
slug: cosmx-spatial-transcriptomics
domain: "molecular-biology / spatial-transcriptomics / methods"
status: mainstream
aliases:
  - "CosMx"
  - "CosMx SMI"
  - "NanoString CosMx"
  - "spatial molecular imager"
  - "in situ multiplex transcriptomics"
  - "subcellular spatial transcriptomics"
  - "1000-plex spatial transcriptomics"
  - "CosMx FFPE spatial gene expression"
  - "SMI spatial transcriptomics"
  - "He et al. 2022 CosMx"
first_introduced: "He et al. 2022 *Nat Biotechnol* (CosMx SMI platform from NanoString)"
date_updated: 2026-05-13
source_url: "https://nanostring.com/products/cosmx-spatial-molecular-imager/"
---

## Definition

The NanoString CosMx Spatial Molecular Imager (SMI) is an in situ multiplex spatial transcriptomics platform that detects mRNA transcripts in fixed tissue at subcellular resolution via repeated rounds of fluorescent in situ hybridization with encoded barcodes. Standard panels range from ~960 to ~6,000+ genes; protein readouts are also supported.

## Workflow

1. Mount FFPE / fresh-frozen tissue section.
2. Hybridize barcoded oligo probes targeting the panel genes.
3. Image multiple rounds of fluorescent reporters → decode barcodes.
4. Segment cells (e.g., via DAPI + membrane markers) to assign transcripts to cells.
5. Construct a cell × gene count matrix with x-y coordinates.
6. Downstream analysis: clustering, signature scoring (e.g., UCell), spatial neighbour analysis.

## Strengths

- Subcellular spatial resolution (vs Visium's ~55 μm spot resolution).
- Single-cell-like count matrices with spatial coordinates.
- FFPE-compatible — enables retrospective analysis of archival tissue.
- High multiplexing (~1000 genes per panel).

## Limitations

- Limited panel size (~1000 genes) — not full transcriptome.
- Segmentation errors propagate to all downstream analyses.
- Low transcript counts per cell vs droplet scRNAseq → noisier per-cell signatures.
- Cost / throughput trade-off vs sequencing-based spatial platforms.

## Use cases in this corpus

- [[papers/using-pan-cancer-atlas-investigate-tumour]] uses an open-source CosMx FFPE NSCLC dataset (5 samples, 960 genes × 771,236 cells) to validate the 18_ECMMac cluster in tissue: CD68+/COL1A1+/COL1A2+/COL3A1+ cells identified, and nearest-neighbour analysis (RANN v2.6.1) shows 18_ECMMac TAMs neighbour fibroblasts while 8_IFNGMac TAMs neighbour memory T cells.

## Relevance to active research

- [[papers/using-pan-cancer-atlas-investigate-tumour]] — Coulton et al. 2024.
- [[papers/cellcharter-reveals-spatial-cell-niches-associated]] — Varrone et al. 2024 use a CosMx 960-gene NSCLC dataset (5 patients, 8 sections, ~700k cells) to identify the LUAD hypoxic-tumour + tumour-associated-neutrophil niche (clusters C0/C11/C12).
