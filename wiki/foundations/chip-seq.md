---
title: "ChIP-seq (Chromatin Immunoprecipitation Sequencing)"
slug: chip-seq
domain: "genomics / methods"
status: mainstream
aliases:
  - "ChIP-seq"
  - "ChIP-Seq"
  - "chromatin immunoprecipitation sequencing"
  - "TF ChIP-seq"
  - "histone ChIP-seq"
  - "ChIP followed by sequencing"
  - "chromatin profiling"
first_introduced: "Johnson et al. 2007 *Science*; Robertson et al. 2007 *Nature Methods*"
date_updated: 2026-05-05
source_url: "https://www.encodeproject.org/chip-seq/"
---

## Definition

ChIP-seq couples chromatin immunoprecipitation (using a TF- or histone-mark-specific antibody) with high-throughput DNA sequencing to map genome-wide protein-DNA binding sites or histone modification distributions. After crosslinking, fragmentation, and antibody-based pulldown, bound DNA is sequenced and reads are aligned to the reference genome; peak callers (MACS2, SPP, etc.) identify regions of significant enrichment.

## Intuition

ChIP-seq is the standard for asking "where does TF X bind in the genome?" or "where is histone mark Y deposited?". Output is a BED-style peak file plus signal coverage tracks. Quality depends critically on antibody specificity and crosslinking efficiency.

## Formal notation

- Inputs: crosslinked chromatin + IP antibody + matched input/IgG control
- Outputs: peaks (narrow for TFs, broad for some histone marks) + bigWig signal tracks
- Peak callers: MACS2 (most common), SICER (broad marks), SEACR (CUT&RUN-style)

## Key variants

- CUT&RUN, CUT&Tag — antibody-tethered MNase or pA-Tn5 alternatives, lower cell input
- ChIP-exo — exonuclease trim for higher-resolution binding sites
- BioChIP — biotin-tagged TF instead of antibody

## Known limitations

- Antibody quality is the dominant source of variability and irreproducibility.
- Requires substantial cell input (millions for canonical ChIP-seq).
- "Phantom peaks" at hyperaccessible loci are a known artifact.
- Cannot distinguish direct vs indirect binding without complementary assays.

## Open problems

- Single-cell ChIP-seq sensitivity remains low.
- Reproducibility across antibodies / labs / batches.

## Relevance to active research

[[papers/nf-kb-tet2-promote-macrophage-reprogramming]] uses ChIP-seq for HIF1α and p65 (RELA) across all four MAC conditions (iMAC21, iMAC1, mMAC21, mMAC1), defining HIF1α clusters H1/H2/H3 and p65 cluster P1, identifying ~15% cobinding in mMAC1, and linking p65 binding (but not HIF1α) to cluster-C2-demethylated CpGs. ChIP-seq is the load-bearing layer connecting epigenome (DNA methylation) to TF activity.
