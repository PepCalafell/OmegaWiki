---
title: "10x Genomics Chromium scRNA-seq"
slug: scrna-seq-10x-chromium
domain: "genomics / single-cell methods"
status: mainstream
aliases:
  - "10x Chromium"
  - "10x Genomics scRNA-seq"
  - "10x 3' v2 chemistry"
  - "10x 3' v3 chemistry"
  - "10x Chromium 3'"
  - "Chromium scRNA-seq"
  - "10x single-cell"
  - "droplet-based scRNA-seq"
  - "GEM (gel bead-in-emulsion)"
  - "Cell Ranger"
  - "scRNA-seq 10x"
first_introduced: "Zheng et al. *Nat Commun* 2017 (10x Genomics Chromium platform)"
date_updated: 2026-05-06
source_url: "https://www.10xgenomics.com/products/single-cell-gene-expression"
---

## Definition

A droplet microfluidics-based single-cell RNA sequencing platform commercialised by 10x Genomics. Cells are individually encapsulated in gel-bead-in-emulsion (GEM) droplets containing barcoded oligo-dT primers, lysed, and reverse-transcribed in droplet, producing cDNA libraries with cell-of-origin and unique molecular identifier (UMI) barcodes. The 3' chemistry (v2, v3, v3.1) sequences the 3' end of each transcript; the 5' chemistry sequences the 5' end and supports paired V(D)J profiling. Standard targets are 5,000–10,000 cells per channel, with multiplexed channels per run. Output is processed with the Cell Ranger pipeline to produce cell-by-gene UMI count matrices.

## Intuition

10x Chromium is the dominant platform for population-scale scRNA-seq because it scales cleanly (thousands of cells per channel, multiplexable), has consistent chemistry between releases, and feeds into a standardised analysis ecosystem (Cell Ranger → Seurat / Scanpy → integration tools). It trades sequencing depth per cell (median 1,000–5,000 UMIs/cell) for cell number, and is therefore preferred for cell-type discovery and atlas-scale projects where breadth matters more than depth.

## Key variants

- **3' v2 chemistry**: original; 5,000 cells/channel; lower sensitivity than v3
- **3' v3 / v3.1 chemistry**: improved sensitivity; standard at present
- **5' chemistry**: paired with V(D)J profiling for TCR/BCR repertoire
- **Multiome (ATAC + GEX)**: paired chromatin accessibility and transcriptome from same cell
- **CITE-seq compatibility**: TotalSeq-A/B/C antibodies for surface protein quantification (Mulder 2021 used this with Smart-seq2)
- **Hashtag oligonucleotides (HTO)**: sample multiplexing across donors / conditions
- **Visium spatial transcriptomics**: companion spatial assay
- **Xenium** / **CosMx**: in situ targeted spatial RNA detection

## Known limitations

- Modest sensitivity per cell (typically 10-20% gene capture)
- 3' bias precludes splice-isoform analysis
- Doublets at 1-5% per channel; require computational correction (Scrublet, DoubletFinder)
- Ambient RNA contamination ("soup"); requires SoupX / decontX correction
- Cost per cell is significant; large-cohort studies often require pooling and demultiplexing
- Chemistry version differences create batch effects; integration tools (Harmony, scVI, BBKNN) are mandatory for combined analyses
- Sample preparation requires viable single-cell suspension; some tissues (e.g., adipose, brain) need specialised dissociation

## Open problems

- Higher-throughput chemistries (Parse Bio, Fluent Bio, scifi-RNA-seq) compete on cost
- Better integration of 3' and 5' chemistry datasets
- Consistent UMI normalisation across chemistries and depths
- Standardised QC thresholds across studies

## Relevance to active research

[[papers/tissue-resident-macrophages-provide-pro-tumorigenic]] uses 10x Chromium 3' v2 chemistry to scRNA-seq sorted CD45⁺LIN⁻CD11B⁺LY6G⁻ monocyte/macrophage populations from naive and KP tumour-bearing mice (8,500 cells per sample), encapsulated and sequenced on Illumina NextSeq 550 to ~100M reads per library. Cell Ranger 2.1 alignment to mm10 followed by maximum-likelihood clustering identifies the four canonical groups (TRM, MDM, monocytes I/II) used throughout the paper. 10x Chromium is also the platform underlying [[papers/cross-tissue-single-cell-landscape-human]] (MoMac-VERSE) and [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] (Calafell 2024). It is the default scRNA-seq platform for the wiki corpus.
