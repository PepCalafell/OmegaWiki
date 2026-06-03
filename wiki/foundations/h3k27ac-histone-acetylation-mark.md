---
title: "H3K27ac — histone H3 lysine-27 acetylation"
slug: h3k27ac-histone-acetylation-mark
domain: "epigenetics / chromatin biology"
status: mainstream
aliases:
  - "H3K27ac"
  - "histone H3 lysine 27 acetylation"
  - "H3 acetylated at Lys27"
  - "acetyl-H3K27"
first_introduced: "Creyghton et al. 2010 *PNAS* (H3K27ac marks active enhancers)"
date_updated: 2026-06-03
source_url: "https://doi.org/10.1073/pnas.1016071107"
---

## Definition

H3K27ac is the acetylation of lysine 27 on histone H3. It marks active promoters and, distinctively, active (as opposed to merely poised) enhancers, and is deposited by acetyltransferases such as p300/CBP and removed by HDACs. Because its levels at cis-regulatory elements change rapidly downstream of signal-induced transcription-factor binding, H3K27ac is widely used as a dynamic readout of enhancer/promoter activity.

## Intuition

Where DNA is "switched on", H3K27ac accumulates; where regulatory elements are turned off, it is removed. Mapping H3K27ac genome-wide (by ChIP-seq) therefore reports which enhancers and promoters are active in a given condition and how that activity shifts with stimulation or perturbation.

## Formal notation

- Assayed by ChIP-seq with anti-H3K27ac antibody (e.g., Abcam ab4729).
- Signal quantified per cis-regulatory element (CRE), often centered on ATAC-seq-defined accessible regions.
- Dynamic changes reported as read-count changes per CRE across time/treatment.

## Key variants

- H3K4me1 (enhancer mark, active+poised) vs H3K27ac (active only) — combinatorial enhancer annotation.
- H3K27me3 — the repressive Polycomb mark at the same residue (mutually exclusive with acetylation).

## Known limitations

- A correlate of activity, not a direct measure of transcription.
- Antibody specificity and cross-reactivity (e.g., with other acetyl marks) affect quantitation.
- Broad/overlapping signal at clustered enhancers complicates CRE assignment.

## Open problems

- Causal contribution of H3K27ac itself vs the acetyltransferase machinery to transcription.
- Single-cell resolution of H3K27ac dynamics.

## Relevance to active research

[[papers/integrative-epigenome-based-strategy-unbiased-functional]] makes H3K27ac the central, information-rich readout: ~600 H3K27ac ChIP-seq samples across 58 kinase inhibitors, two stimuli (LPS, IL-4) and five timepoints define ~16,500 LPS- and ~5,000 IL-4-regulated CREs, whose perturbation is argued to exceed the resolution of transcriptome-based profiling.
