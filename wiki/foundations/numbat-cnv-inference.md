---
title: "Numbat — haplotype-aware CNV inference for single-cell and ST data"
slug: numbat-cnv-inference
domain: methods/genomics
status: mainstream
aliases:
  - Numbat
  - numbat package
  - haplotype-aware CNV scRNA-seq
  - p_cnv tumor probability
  - allele-specific CNV single-cell
  - tumour clonal lineage inference scRNA-seq
  - numbat spatial transcriptomics
first_introduced: "Gao 2023 Nat Biotechnol"
date_updated: 2026-05-22
source_url: "https://kharchenkolab.github.io/numbat/"
---

## Definition
Numbat is a haplotype-aware CNV inference method for scRNA-seq and spatial transcriptomics that integrates allele frequencies with expression-based estimates to call clonal copy-number events and subclonal phylogeny.

## Intuition
Allele frequency drifts asymmetrically over CNV-containing regions; phasing reads against population haplotypes gives a much sharper signal than expression alone, especially in sparse data.

## Key variants
- scRNA-seq mode (default)
- Spatial-transcriptomics mode (per-spot p_cnv)
- Trio / matched-normal mode when available

## Known limitations
- Phasing accuracy degrades with rare-haplotype individuals
- Performance limited at very low UMI counts
- Cannot detect copy-neutral LOH from expression alone

## Open problems
- Joint integration with somatic SNV calls
- Standardised confidence reporting for downstream malignancy thresholds (e.g. p_cnv > 0.99)

## Relevance to active research
Used in [[papers/spatial-transcriptomics-reveals-distinct-conserved-tumor]] to validate malignancy of ST spots via p_cnv > 0.99, complementing CARD deconvolution-based annotation.
