---
title: "ATAC-seq (Assay for Transposase-Accessible Chromatin)"
slug: atac-seq
domain: "genomics / methods / epigenetics"
status: mainstream
aliases:
  - "ATAC-seq"
  - "ATAC sequencing"
  - "ATAC-Seq"
  - "assay for transposase-accessible chromatin"
  - "Tn5 transposase chromatin accessibility"
  - "open chromatin profiling"
  - "chromatin accessibility assay"
  - "Buenrostro ATAC-seq"
  - "Omni-ATAC"
  - "scATAC-seq"
first_introduced: "Buenrostro et al. *Nat Methods* 2013"
date_updated: 2026-05-06
source_url: "https://www.nature.com/articles/nmeth.2688"
---

## Definition

ATAC-seq (Assay for Transposase-Accessible Chromatin using sequencing) profiles open / accessible chromatin genome-wide by directly tagging accessible regions with adapter-loaded Tn5 transposase. The transposase preferentially integrates into nucleosome-free DNA, producing a sequencing library whose read pile-ups correspond to regions of open chromatin — typically active promoters, enhancers, and TF-binding sites. Standard input is 50,000 cells; bulk and single-cell variants exist.

## Intuition

If ChIP-seq asks "where does *this* TF bind?", ATAC-seq asks "where is the chromatin open *at all*?". A peak in ATAC-seq usually marks a regulatory element actively engaged by some combination of TFs, even when the responsible TFs are unknown. The technique is fast (single tagmentation step), low-input, and combinable with single-cell methods (scATAC-seq), making it the default chromatin-accessibility assay for primary cells and rare populations.

## Formal notation

- Inputs: 5×10⁴ FACS-sorted cells (canonical bulk); 500-50,000 cells (scaled variants); single cells (scATAC-seq, 10x Multiome)
- Library: Tn5 tagmentation of accessible chromatin → PCR amplification (typically 5 + adaptive cycles) → paired-end sequencing
- Aligners: Bowtie2 / BWA-MEM
- Peak callers: MACS2 (with `--nomodel --extsize 73 --shift -37` for ATAC), Genrich, HMMRATAC
- Counts/differential: HTSeq + DESeq2; or csaw for window-based analysis
- Annotation: GREAT, ChIPseeker
- Quality controls: TSS enrichment score, fragment-size distribution (mono-/di-/tri-nucleosome banding)

## Key variants

- **Omni-ATAC** (Corces 2017): improved fixation, lower mitochondrial contamination
- **scATAC-seq** (10x Genomics, sciATAC, Plate-based): single-cell chromatin accessibility
- **Multiome (10x ATAC + GEX)**: paired chromatin and transcriptome from same cells
- **NicheNet/ATAC-co-accessibility (Cicero)**: infer enhancer-promoter links
- **Frozen ATAC**: cryopreserved tissue input

## Known limitations

- Sensitivity to mitochondrial contamination (especially in fresh primary cells; Omni-ATAC mitigates)
- Tn5 sequence bias near GC-rich and CpG-island loci
- Resolution limited by Tn5 footprint and sequencing depth
- Cannot directly identify the bound TFs (motif enrichment via HOMER or chromVAR is downstream)
- Requires viable / fresh nuclei; FFPE compatibility is limited
- Sample-size estimation for differential accessibility analyses is non-trivial; modest n (3 replicates) is common but underpowered for small-effect changes

## Open problems

- Standardisation of peak-calling parameters across studies
- Single-cell ATAC integration with bulk reference atlases
- Spatial ATAC-seq (emerging; Deng 2022)
- Joint inference of TF activity from ATAC + transcriptome (e.g., chromVAR, SCENIC+)

## Relevance to active research

[[papers/tissue-resident-macrophages-provide-pro-tumorigenic]] uses ATAC-seq on FACS-sorted alveolar TRMs (50,000 cells; n=3 biological replicates per condition; healthy / day-15 / day-30 KP NSCLC) to ask whether the transcriptional changes induced by tumour proximity are accompanied by chromatin remodelling. The result — minimal global accessibility change with localised early changes at MMP12/MMP13 — is interpreted as evidence that TRMs are heavily tissue-imprinted and that tumour-induced reprogramming operates largely within the existing chromatin landscape. ATAC-seq is also a load-bearing methodology in [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] and is central to any thesis-level characterisation of macrophage epigenome dynamics. scATAC-seq integration is benchmarked in [[papers/benchmarking-atlas-level-data-integration-single]] (only LIGER and Harmony work consistently across peak/window feature spaces).
