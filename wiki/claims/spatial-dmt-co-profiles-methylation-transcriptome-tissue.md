---
title: "Spatial-DMT enables simultaneous whole-genome DNA methylation and transcriptome profiling on the same tissue section at near single-cell pixel resolution"
slug: spatial-dmt-co-profiles-methylation-transcriptome-tissue
status: supported
confidence: 0.95
tags: [spatial-omics, DNA-methylation, transcriptome, methods]
domain: epigenetics / spatial omics / methods
source_papers:
  - spatial-joint-profiling-dna-methylome-transcriptome
evidence:
  - source: spatial-joint-profiling-dna-methylome-transcriptome
    type: supports
    strength: strong
    detail: "Quote (abstract, p.1): 'we introduce a method for whole-genome spatial co-profiling of DNA methylation and the transcriptome of the same tissue section at near single-cell resolution'. Mouse E11/E13 embryos and P21 brain profiled at 10, 20, 50 μm resolution."
conditions: "Fresh-frozen tissue sections, 1% formaldehyde fixation; DBiT-seq microfluidic spatial barcoding; EM-seq enzymatic methylation conversion; not yet validated on FFPE."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

Spatial-DMT is the first reported method for whole-genome spatial co-profiling of DNA methylation together with the transcriptome from the same tissue section. Pixel sizes of 10–50 μm reach near single-cell resolution; DNAm uses EM-seq conversion, RNA uses template-switched poly-T capture, and the two streams are separated by streptavidin selection on the same spatial-barcoded tissue.

## Evidence summary

Reported in [[papers/spatial-joint-profiling-dna-methylome-transcriptome]] (Lee et al. *Nature* 2025). Demonstrated on E11 and E13 mouse embryos plus P21 mouse brain across 10, 20, 50 μm pixel chips.

## Conditions and scope

Fresh-frozen tissue, 1% formaldehyde fixation, 0.5% Triton X-100, 0.1 N HCl. Currently no FFPE support; long-read extension proposed but not demonstrated.

## Counter-evidence

None within the paper. Independent reproduction by another lab is not yet published.

## Linked ideas

## Open questions

- FFPE adaptation for clinical samples.
- Long-read EM-seq integration to resolve 5mC vs 5hmC at spatial resolution.
