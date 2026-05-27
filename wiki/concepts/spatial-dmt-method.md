---
title: "spatial-DMT — Spatial joint profiling of DNA methylome and transcriptome"
aliases:
  - "spatial-DMT"
  - "spatial DMT"
  - "spatial DNA methylome transcriptome co-profiling"
tags:
  - spatial-omics
  - DNA-methylation
  - multi-omics
  - epigenetics
  - methods
maturity: emerging
key_papers:
  - spatial-joint-profiling-dna-methylome-transcriptome
first_introduced: "Lee et al. *Nature* 2025"
date_updated: 2026-05-27
related_concepts:
  - variably-methylated-regions-vmr
  - partially-methylated-domains-mitotic-clock
  - non-cpg-methylation-postnatal-brain
  - methylation-positive-coupling-gene-expression
---

## Definition

Spatial-DMT is a spatial multi-omics assay that co-profiles whole-genome DNA cytosine methylation and the transcriptome on the same tissue section at near single-cell pixel resolution (10–50 μm). It is the first method to spatially resolve DNA methylation alongside gene expression — closing a long-standing gap in spatial epigenomics that previously covered only histone marks (CUT&Tag), chromatin accessibility (ATAC), and transcription.

## Intuition

DBiT-seq deposits a 2D spatial barcode onto a tissue ([[foundations/dbit-seq-deterministic-barcoding-in-tissue]]); spatial-DMT then splits the captured material into a cDNA stream (template-switched, standard scRNA-seq library) and a gDNA stream (EM-seq conversion via TET2+APOBEC, splint ligation, library prep — [[foundations/em-seq-enzymatic-methyl-sequencing]]). The two libraries return mapped to the same pixel grid, enabling per-pixel methylome + transcriptome joint analysis via WNN ([[foundations/wnn-weighted-nearest-neighbor-integration]]).

## Formal notation

- Pixel size: 10 / 20 / 50 μm; 50×50 grid = up to 2,500 pixels per ROI.
- DNAm coverage: ~10⁵ CpGs per pixel (mouse genome); ~70–80% CpG retention; >99% non-CpG conversion.
- RNA coverage: ~10³–10⁴ genes per pixel; ~10³–10⁵ UMIs per pixel depending on resolution.
- DNAm + RNA replicate concordance: Pearson r ≈ 0.98 (DNAm), r ≈ 0.97 (RNA) at matched body parts.

## Variants

- **Tissue / stage**: applied to mouse E11 and E13 embryos and P21 brain in the introducing paper.
- **Resolution**: 10 μm (near single-cell), 20 μm (P21 brain), 50 μm (whole-embryo overviews).
- **Possible extensions** (discussed by the authors): pairing with chromatin conformation (HiC), accessibility (ATAC), histone marks (CUT&Tag), metabolome (MSI), protein (CITE-seq); FFPE adaptation; long-read EM-seq.

## Comparison

- vs **spatial ATAC–RNA** ([[foundations/spatial-atac-seq]]): same DBiT-seq chassis but ATAC measures accessibility, not methylation.
- vs **single-cell DNA-methylation** (sciMETv2, snmC-seq2): comparable per-cell CpG coverage but adds spatial context lost upon dissociation.
- vs **MeDIP / EPIC array** ([[foundations/medip-methylated-dna-immunoprecipitation]], [[foundations/illumina-methylationepic-array]]): genome-wide quantitative single-CpG read-out vs immunoprecipitation enrichment or array sampling, plus per-pixel spatial information.

## When to use

- Spatial epigenetic regulation of development, brain anatomy, oncogenesis.
- Distinguishing cell states that look identical transcriptionally but differ epigenetically (e.g., D0 vs D4 within RNA-cluster R3 in E11 embryo).
- Spatial mapping of mitotic-history readouts via PMDs ([[concepts/partially-methylated-domains-mitotic-clock]]).
- Spatial dissection of mCH/mCA accumulation in the postnatal brain ([[concepts/non-cpg-methylation-postnatal-brain]]).

## Known limitations

- Cannot distinguish 5mC from 5hmC (inherited from EM-seq chemistry).
- 50 μm pixels are multi-cellular; 10 μm chips trade ROI area for resolution.
- Limited to fresh-frozen sections in the launch implementation; FFPE adaptation is future work.
- Tn5 + HCl tissue treatment may degrade some labile RNA.

## Open problems

- Distinguishing 5mC vs 5hmC at spatial resolution.
- Combining spatial-DMT with chromatin accessibility / conformation / histone marks in the same pixel.
- Computational deconvolution to recover single-cell methylomes from multi-cellular pixels.

## Key papers

- [[papers/spatial-joint-profiling-dna-methylome-transcriptome]] — Lee et al. *Nature* 2025; method introduction; mouse E11/E13 embryos + P21 brain.

## My understanding

Spatial-DMT closes the last big modality gap in spatial omics. By inheriting the DBiT-seq chassis, it is immediately combinable with any future modality the same group (or others) layer on top. The bigger conceptual contribution — beyond the assay — is that the per-pixel WNN modality weights are themselves a biological read-out: regions where DNAm dominates the cell-identity signal (e.g., craniofacial W11) point to epigenetically-primed but transcriptionally-converged states that single-modality maps miss. This makes spatial-DMT not just a measurement upgrade but a way to identify spatial regions of epigenetic priming as a hypothesis-generation tool.
