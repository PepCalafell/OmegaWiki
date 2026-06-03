---
title: "H3K27me3 (histone H3 lysine 27 trimethylation)"
slug: "h3k27me3-histone-trimethylation-mark"
domain: "epigenetics"
status: mainstream
aliases:
  - H3K27me3
  - H3K27 trimethylation
  - histone H3 lysine 27 trimethylation
first_introduced: "Cao et al. 2002 Science (PRC2/EZH2)"
date_updated: 2026-06-03
source_url: "https://doi.org/10.1126/science.1076997"
---

## Definition
H3K27me3 is the trimethylation of lysine 27 on histone H3, a repressive chromatin mark deposited by the Polycomb Repressive Complex 2 (PRC2) via its catalytic subunit EZH2. It is associated with transcriptional silencing.

## Intuition
H3K27me3 marks facultatively silenced regions. At promoters, its co-occurrence with H3K4me3 defines poised/bivalent promoters; at enhancers, its co-occurrence with H3K4me1 defines poised enhancers. It generally anti-correlates with active transcription.

## Formal notation
Profiled by ChIP-seq with anti-H3K27me3 antibody; deposited by PRC2 (EZH2), removed by KDM6A/B demethylases.

## Key variants
- H3K4me3 + H3K27me3 → poised promoter
- H3K4me1 + H3K27me3 → poised enhancer

## Known limitations
- Broad, low-signal domains complicate peak calling
- Repression is context-dependent and not absolute

## Open problems
- Dynamics of bivalent resolution during cell activation versus differentiation

## Relevance to active research
One of the four histone marks used to define poised promoters/enhancers in human macrophage activation; its absence at activation-TR-network loci is part of the paper's "open chromatin" signature.
