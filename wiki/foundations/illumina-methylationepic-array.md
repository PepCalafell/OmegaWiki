---
title: "Illumina Infinium MethylationEPIC array"
slug: illumina-methylationepic-array
domain: "genomics / methods"
status: mainstream
aliases:
  - "EPIC array"
  - "Infinium MethylationEPIC"
  - "EPIC v1"
  - "EPIC v2"
  - "850k array"
  - "Illumina methylation BeadChip"
  - "DNA methylation array"
  - "MethylationEPIC v2.0"
first_introduced: "Illumina 2016 (EPIC v1, ~850k CpGs); EPIC v2 in 2023"
date_updated: 2026-05-05
source_url: "https://www.illumina.com/products/by-type/microarray-kits/infinium-methylation-epic.html"
---

## Definition

The Illumina Infinium MethylationEPIC array is a bead-based bisulfite-conversion microarray that interrogates ~850,000 (v1) or ~935,000 (v2) CpG sites genome-wide, providing single-CpG-resolution DNA methylation β values (0–1) for human samples. Each CpG site is queried by a probe pair (Type I or Type II); β = methylated intensity / (methylated + unmethylated + ε).

## Intuition

EPIC is the workhorse platform for population-scale and clinical-cohort DNA methylation studies. Coverage is biased toward gene promoters, enhancers, and CpG islands, with growing representation of distal regulatory elements in v2.

## Formal notation

- Probe types: Type I (two beads per CpG), Type II (single bead, dual-color)
- Output: β value (0=unmethylated, 1=methylated) or M = log2(M/U) (more statistically tractable)
- Standard pipeline: minfi or SeSAMe for normalization (noob, BMIQ, funnorm, ssNoob)

## Key variants

- 450k array (predecessor): ~485k CpGs
- EPIC v1: ~850k CpGs
- EPIC v2: ~935k CpGs, redesigned distal-enhancer coverage

## Known limitations

- Limited to predesigned CpGs (no novel-CpG discovery, unlike WGBS or RRBS).
- Cross-reactive and SNP-affected probes need filtering.
- Cell-type composition strongly confounds whole-blood/whole-tissue analyses; deconvolution often required.

## Open problems

- v2 coverage gaps in some enhancer classes remain.
- Standardizing batch correction across consortia.

## Relevance to active research

[[papers/nf-kb-tet2-promote-macrophage-reprogramming]] uses EPIC arrays to identify the C1/C2/C3 differential-methylation clusters that anchor the entire mechanistic story. Pharmacological perturbation (BAY11-7082, PX-478, 4-octyl itaconate) is read out by EPIC array methylation changes at C2 CpGs.
