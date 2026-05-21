---
title: "Repurposed SVG methods fail on spatial ATAC-seq SVP detection; 'use all peaks' beats most"
slug: svg-methods-fail-spatial-atac-svp
status: supported
confidence: 0.8
tags:
  - spatial-atac-seq
  - SVP
  - methods-gap
  - benchmarking
domain: spatial-epigenomics-methods
source_papers:
  - "[[papers/systematic-benchmarking-computational-methods-identify-spatially]]"
evidence:
  - source: "[[papers/systematic-benchmarking-computational-methods-identify-spatially]]"
    type: supports
    strength: strong
    detail: "Spatial ATAC-seq data from mouse embryonic development (E12.5, E13.5, E15.5). Top-20k peaks per method used for Leiden clustering, evaluated by CHAOS. Only SpatialDE2 (mean CHAOS = 0.104) beats the all-peaks baseline (CHAOS = 0.105). BOOST-GP and GPcounts do not return results within 120 h; SPARK runs out of memory. Most other SVG methods worse than all-peaks baseline."
conditions: "Holds on mouse embryonic spatial ATAC-seq with 20–70k peaks and limited training samples (3 timepoints). CHAOS as the sole quality metric (no ground-truth SVPs); spatial coherence ≠ biological validity. SpatialDE2's narrow advantage (0.104 vs 0.105) may be noise-level."
date_proposed: 2026-05-21
date_updated: 2026-05-21
---

## Statement

When existing SVG-detection methods are applied to spatial ATAC-seq peak matrices, none yield a meaningful gain over the trivial "use all peaks" baseline for downstream Leiden clustering as measured by the spatial CHAOS score. Only SpatialDE2 marginally outperforms the all-peaks baseline; BOOST-GP, GPcounts, and SPARK fail outright due to scalability/memory limits. This identifies SVP detection as a methodological gap requiring purpose-built algorithms.

## Evidence summary

Quote (p.12): "SpatialDE2 outperformed other methods (mean CHAOS = 0.104), indicating that it has the potential to identify biologically meaningful SVPs… our analysis revealed that using all peaks yielded the second-best performance (mean CHAOS = 0.105). This finding suggests that more specialized methods are required to analyze spatial chromatin accessibility data."

Failure modes (p.10): BOOST-GP and GPcounts did not produce results after 120 h; SPARK ran out of memory.

Authors' interpretation (p.16): spatial ATAC-seq data are extremely sparse, near-binary, and ~10× higher-dimensional than gene-level ST data — violating the over-dispersed Poisson/NB count assumptions baked into SVG methods.

## Conditions and scope

Holds on mouse embryonic E12.5/13.5/15.5 spatial ATAC-seq. CHAOS-only evaluation cannot assess biological validity. SpatialDE2's edge is small enough that the practical recommendation may simply be "use all peaks" until purpose-built SVP methods exist.

## Counter-evidence

None within this paper. No competing benchmark exists yet (SVP detection is a nascent task).

## Linked ideas

(none yet)

## Open questions

- A native SVP-detection algorithm tailored to binary/Bernoulli-distributed sparse spatial signals.
- Joint SVG–SVP modelling for spatial gene-regulatory network inference.
- Extension of these findings to spatial CUT&Tag, spatial proteomics, and spatial methylation.
