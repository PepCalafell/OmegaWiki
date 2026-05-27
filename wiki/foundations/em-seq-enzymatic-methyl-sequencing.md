---
title: "EM-seq — Enzymatic Methyl-sequencing"
slug: em-seq-enzymatic-methyl-sequencing
domain: "genomics / methods / epigenetics"
status: mainstream
aliases:
  - "EM-seq"
  - "enzymatic methyl-seq"
  - "NEBNext EM-seq"
  - "TET2-APOBEC enzymatic conversion"
  - "bisulfite-free 5mC sequencing"
first_introduced: "Vaisvila et al. *Genome Research* 2021 (NEB)"
date_updated: 2026-05-27
source_url: "https://www.neb.com/products/e7120-nebnext-enzymatic-methyl-seq-kit"
---

## Definition

EM-seq is an enzymatic alternative to bisulfite conversion for whole-genome and reduced-representation 5-methylcytosine profiling. Modified cytosines (5mC + 5hmC) are oxidised by ten-eleven translocation methylcytosine dioxygenase 2 (TET2) and then protected from APOBEC-mediated deamination; unmodified cytosines are deaminated to uracil. After PCR with uracil-tolerant polymerase, methylated C reads as C while unmethylated C reads as T — the inverse of the historical bisulfite read-out — but without the DNA damage caused by bisulfite chemistry.

## Intuition

Bisulfite converts unmodified C → U via deamination, but the harsh acidic + high-temperature conditions fragment DNA and lose 80–90% of input. EM-seq does the same C→U conversion enzymatically while shielding 5mC/5hmC enzymatically, so the input requirement drops 10–100×, library complexity rises, and short or precious inputs (FFPE, microfluidic-tagmented tissue pixels) become tractable.

## Formal notation

- TET2 oxidises 5mC → 5caC (carboxylcytosine); APOBEC cannot deaminate 5caC.
- APOBEC deaminates C → U (unmodified) and 5fC → uracil-equivalent (residual signal).
- Reads: 5mC + 5hmC → C; C → T after PCR.
- Pooled 5mC + 5hmC signal — EM-seq does NOT distinguish 5mC from 5hmC; orthogonal oxBS / TAB / ACE-seq required for that split.

## Key variants

- **NEBNext EM-seq** (E7120): bulk WGBS-equivalent input ≥10 ng.
- **EM-seq for single-cell / spatial**: paired with Tn5 tagmentation (sciMETv2; spatial-DMT) reaches femtogram-level inputs per pixel.
- **EM-seq + splint ligation**: used in spatial-DMT to add a PCR handle to deaminated fragments after the universal-linker barcode is in place (see [[papers/spatial-joint-profiling-dna-methylome-transcriptome]]).

## Known limitations

- Cannot resolve 5mC vs 5hmC without additional chemistry.
- TET2/APOBEC enzymatic step is longer than bisulfite (~overnight), though gentler.
- Conversion is sensitive to incomplete oxidation: low 5hmC in oxidative-stress contexts can leak into the unmodified-C bin.

## Open problems

- Engineered TET/APOBEC variants for one-pot bisulfite-free dual 5mC/5hmC discrimination.
- Combining EM-seq with long-read (Nanopore, PacBio) for haplotype-resolved tissue methylomes at spatial resolution.

## Relevance to active research

EM-seq is the conversion chemistry adopted by [[papers/spatial-joint-profiling-dna-methylome-transcriptome]] (spatial-DMT), enabling whole-genome spatial methylome co-profiling with [[concepts/spatial-dmt-method]] without bisulfite-induced fragmentation, and underpins recent single-cell methylome workflows that achieve ≥10⁵ CpGs per cell.
