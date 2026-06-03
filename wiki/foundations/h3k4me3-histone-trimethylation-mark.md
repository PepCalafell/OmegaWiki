---
title: "H3K4me3 (histone H3 lysine 4 trimethylation)"
slug: "h3k4me3-histone-trimethylation-mark"
domain: "epigenetics"
status: mainstream
aliases:
  - H3K4me3
  - H3K4 trimethylation
  - histone H3 lysine 4 trimethylation
first_introduced: "Santos-Rosa et al. 2002 Nature; Barski et al. 2007 Cell"
date_updated: 2026-06-03
source_url: "https://doi.org/10.1016/j.cell.2007.05.009"
---

## Definition
H3K4me3 is the trimethylation of lysine 4 on histone H3, the canonical chromatin mark of active and poised gene promoters, concentrated around transcription start sites.

## Intuition
H3K4me3 marks promoters; its co-occurrence with H3K27ac defines active promoters, whereas co-occurrence with the repressive H3K27me3 ("bivalent") defines poised promoters held ready for activation or repression.

## Formal notation
Profiled by ChIP-seq with anti-H3K4me3 antibody; proximal (± 2.5 kb of TSS) H3K4me3 peaks define candidate promoters.

## Key variants
- H3K4me3 + H3K27ac → active promoter (Pa)
- H3K4me3 + H3K27me3 → poised / bivalent promoter (Pp)

## Known limitations
- Broad vs narrow H3K4me3 domains carry different functional meaning not captured by simple peak calls
- Presence at a promoter does not guarantee transcription

## Open problems
- Functional role of broad H3K4me3 domains at cell-identity genes

## Relevance to active research
Used together with H3K27ac, H3K4me1 and H3K27me3 to define the five chromatin states of human macrophage promoters and enhancers.
