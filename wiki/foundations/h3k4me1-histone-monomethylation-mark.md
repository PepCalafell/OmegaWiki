---
title: "H3K4me1 (histone H3 lysine 4 monomethylation)"
slug: "h3k4me1-histone-monomethylation-mark"
domain: "epigenetics"
status: mainstream
aliases:
  - H3K4me1
  - H3K4 monomethylation
  - histone H3 lysine 4 monomethylation
first_introduced: "Heintzman et al. 2007 Nat Genet"
date_updated: 2026-06-03
source_url: "https://doi.org/10.1038/ng1966"
---

## Definition
H3K4me1 is the monomethylation of lysine 4 on histone H3, the canonical chromatin mark of enhancer elements (both active and poised). It is deposited largely by the MLL3/MLL4 (KMT2C/KMT2D) methyltransferases.

## Intuition
H3K4me1 marks enhancers genome-wide regardless of their activity state; the additional presence of H3K27ac distinguishes active/strong enhancers, while co-occurrence with H3K27me3 marks poised enhancers and absence of both marks weak enhancers.

## Formal notation
Profiled by ChIP-seq with anti-H3K4me1 antibody; distal (> 2.5 kb from TSS) H3K4me1 peaks define candidate enhancers.

## Key variants
- H3K4me1 + H3K27ac → strong/active enhancer
- H3K4me1 only → weak enhancer
- H3K4me1 + H3K27me3 → poised enhancer

## Known limitations
- Does not by itself indicate enhancer activity
- Antibody specificity and signal-to-noise vary across datasets

## Open problems
- Causal role of H3K4me1 deposition versus its being a consequence of TF binding

## Relevance to active research
One of four histone modifications used to define the five chromatin states (active/poised promoters, strong/weak/poised enhancers) in human macrophage activation.
