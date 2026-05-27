---
title: "Spatial-DMT per-pixel CpG coverage (136,639–281,447 CpGs/pixel) is comparable to single-cell DNA-methylation assays"
slug: spatial-dmt-cpg-coverage-comparable-scbsseq
status: supported
confidence: 0.95
tags: [spatial-omics, DNA-methylation, CpG-coverage, methods, benchmark]
domain: epigenetics / spatial omics / methods
source_papers:
  - spatial-joint-profiling-dna-methylome-transcriptome
evidence:
  - source: spatial-joint-profiling-dna-methylome-transcriptome
    type: supports
    strength: strong
    detail: "Quote (p.3): 'On average, 136,639–281,447 CpGs were covered per pixel across E11, E13 and P21 samples (Supplementary Table 5), comparable to previous single-cell DNA-methylation studies of mouse embryos and brain samples'. Direct comparison shown in Fig. 1c against mouse muscle stem cells, mouse brain, human brain sciMETv2 cohorts."
conditions: "Mouse tissues; pixel sizes 10–50 μm; deep sequencing (2.8–3.9 billion raw reads per sample)."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

Spatial-DMT achieves per-pixel CpG coverage (1.4–2.8 ×10⁵ CpGs) comparable to state-of-the-art single-cell DNA-methylation assays (sciMETv2, snmC-seq2) on mouse embryos and brain.

## Evidence summary

Reported in [[papers/spatial-joint-profiling-dna-methylome-transcriptome]], Fig. 1c and Supplementary Table 5.

## Conditions and scope

Mouse fresh-frozen tissue, 2.8–3.9 billion raw reads per sample; 32.2–65.7% retention after QC; 1,699–2,493 pixels per dataset.

## Counter-evidence

None within paper.

## Linked ideas

## Open questions

- Human-tissue coverage benchmarking at equivalent sequencing depth.
- Scaling to whole-section maps with millions of pixels.
