---
title: "CROP-seq — CRISPR droplet sequencing"
slug: crop-seq-crispr-droplet-sequencing
domain: functional genomics
status: mainstream
aliases:
  - CROP-seq
  - CRISPR droplet sequencing
first_introduced: "Datlinger et al. 2017, Nature Methods"
date_updated: 2026-06-04
source_url: "https://doi.org/10.1038/nmeth.4177"
---

## Definition
CROP-seq (CRISPR droplet sequencing) is a pooled single-cell CRISPR screening method in which the guide RNA is expressed from a vector designed so that the guide sequence is captured as part of the cell's polyadenylated transcriptome. This lets a standard droplet-based scRNA-seq run simultaneously read out each cell's whole transcriptome and its assigned perturbation.

## Intuition
Instead of relying on a separate barcode that may be uncoupled from the functional guide, CROP-seq makes the guide itself detectable in the single-cell mRNA library, giving a direct genotype-to-phenotype link at single-cell resolution in a pooled screen.

## Formal notation
Cells transduced at low MOI (~0.1) so most receive ≤1 guide; scRNA-seq yields, per cell, a transcriptome vector plus a guide RNA assignment; knockouts are analyzed against non-targeting-guide controls.

## Key variants
Combination with CITE-seq surface-protein readout (as in the macrophage screens of Traxler et al. 2025); compatibility with Mixscape perturbation modeling; the CROPseq-3P5P vector (Addgene #219680).

## Known limitations
Guide capture efficiency and assignment ambiguity; requires high per-target cell coverage; cell-line transduction is far easier than primary cells.

## Open problems
Scaling to combinatorial perturbations and to hard-to-transduce primary cells.

## Relevance to active research
Core method for high-content functional genomics in immune cells; central to the [[papers/integrated-time-series-analysis-high-content]] macrophage regulator screens.
