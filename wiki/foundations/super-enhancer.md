---
title: "Super-enhancer"
slug: "super-enhancer"
domain: "epigenetics"
status: mainstream
aliases:
  - super-enhancer
  - super enhancer
  - SE
  - stretch enhancer
first_introduced: "Whyte et al. 2013 Cell; Hnisz et al. 2013 Cell"
date_updated: 2026-06-03
source_url: "https://doi.org/10.1016/j.cell.2013.03.035"
---

## Definition
A super-enhancer (SE) is a large cluster of enhancers, densely occupied by transcription factors, cofactors (e.g. Mediator, BRD4) and activating histone marks, that drives high expression of genes defining cell identity and cell state. Operationally, SEs are called from contiguous regions of disproportionately high H3K27ac (or master-TF) ChIP-seq signal, typically by stitching nearby enhancers within a window (e.g. multiple H3K27ac peaks within < 12.5 kb) and ranking the resulting domains by total signal.

## Intuition
Ordinary (typical) enhancers contribute modestly to transcription; super-enhancers concentrate a large fraction of a cell's regulatory machinery into a few loci, making them potent but also hypersensitive to perturbation. They mark the genes most central to a cell's identity or its current activation state.

## Formal notation
SE calling (ROSE-style): rank stitched enhancer regions by total H3K27ac signal; the inflection point of the ranked-signal curve separates SEs from typical enhancers.

## Key variants
- H3K27ac-defined SEs (most common)
- Master-TF-defined SEs (e.g. by lineage TF occupancy)
- Cell-state / activation-specific SEs vs constitutive SEs

## Known limitations
- SE calls are sensitive to the stitching window and signal threshold
- The "super" designation is partly operational and continuous rather than a discrete biological category

## Open problems
- Functional dissection of which constituent enhancers within an SE are essential
- The degree to which SEs are causal drivers versus consequences of high expression

## Relevance to active research
Used to identify activation-state-defining regulatory regions in immune cells; in human macrophage activation, hundreds of SEs are detected per condition with a common core shared across stimuli.
