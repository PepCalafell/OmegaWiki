---
title: "Lung precursor-to-LUAD evolution follows three distinct spatial clonal patterns (1a fully shared, 1b partially shared, 2 disjoint)"
slug: three-spatial-clonal-evolution-patterns-luad-precursor
status: supported
confidence: 0.75
tags:
  - luad
  - clonal-evolution
  - spatial-genomics
  - cna
  - phylogeny
domain: lung cancer / clonal evolution
source_papers:
  - multimodal-spatial-omics-reveal-co-evolution
evidence:
  - source: multimodal-spatial-omics-reveal-co-evolution
    type: supports
    strength: moderate
    detail: SpatialInferCNV on Visium ST + paired WES + snRNA-seq across 25 patients identifies pattern 1a (n=5, all precursor clones in LUAD + additional), pattern 1b (n=13, mixed shared and stage-specific), pattern 2 (n=5, disjoint). KRAS mutations absent from pattern 1a; EGFR/KRAS/MET enriched in pattern 1b.
conditions: "Synchronous resected precursor+LUAD pairs only; phylogenies limited by CNA-based inference noise from cell-type-mixed Visium spots."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Across 25 patients with paired precursor and invasive lesions, clonal evolution from precursor to LUAD follows three discrete spatial patterns, with KRAS-driven cases concentrated in pattern 1b (mixed sharing) and absent from pattern 1a (linear).

## Counter-evidence

Sampling bias (only synchronous resected pairs) and Visium spot heterogeneity limit confidence. Future spatial single-cell DNA-seq is needed to confirm phylogenies.

## Open questions

- Can a biopsy-resolvable signature place a patient in pattern 1a/1b/2 to guide surveillance?
- What molecular features distinguish pattern 2 (disjoint origin) from polyclonal field cancerization?
