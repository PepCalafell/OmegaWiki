---
title: "A combined CROP-seq + CITE-seq assay enables high-content CRISPR screening with joint single-cell transcriptome and surface-protein readout"
slug: combined-crop-seq-cite-seq-high
status: supported
confidence: 0.85
tags: [crispr-screen, crop-seq, cite-seq, single-cell, methodology, macrophage]
domain: methods
source_papers:
  - integrated-time-series-analysis-high-content
evidence:
  - source: integrated-time-series-analysis-high-content
    type: supports
    strength: strong
    detail: "Pooled CRISPR screens in RAW 264.7-Cas9 macrophages with combined CROP-seq (whole-transcriptome) and CITE-seq (11 surface markers) readout; 9,153 cells (15-gene proof-of-concept) and 28,303 cells (135-gene upscaled screen) passed QC, ~187-200 cells/target."
conditions: "RAW 264.7-Cas9 cell line; MOI 0.1; ~90% untransduced cells co-cultured to dilute non-cell-intrinsic effects; Listeria time course."
date_proposed: 2026-06-04
date_updated: 2026-06-04
---

## Statement
Combining the CROP-seq single-cell transcriptome readout with a CITE-seq surface-protein readout produces a high-content CRISPR screen that simultaneously captures transcriptional and cell-surface consequences of knockouts at scale, with sufficient per-target coverage for quantitative perturbation modeling.

## Evidence summary
Two screens (15 and 135 target genes) over the Listeria time course yielded 9,153 and 28,303 QC-passing single-cell profiles; gene targeting efficiency was confirmed (e.g. Csf1r/CD115 loss at RNA and protein) ([[papers/integrated-time-series-analysis-high-content]], Figures 4-5; uses [[foundations/crop-seq-crispr-droplet-sequencing]], [[foundations/cite-seq-citeseq]]).

## Conditions and scope
Macrophage cell line (RAW 264.7-Cas9); cell-intrinsic effects emphasized by co-culture design.

## Counter-evidence
None; Mixscape filtering excludes perturbations affecting few genes (e.g. Csf1r, Fcgr1).

## Linked ideas

## Open questions
How well does the cell-line screen transfer to primary macrophages, which are harder to transduce?
