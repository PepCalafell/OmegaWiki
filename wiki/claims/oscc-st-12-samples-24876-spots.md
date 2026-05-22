---
title: "12 OSCC ST samples yield 24,876 spots, of which 13,950 are malignant by CARD/Numbat thresholding"
slug: oscc-st-12-samples-24876-spots
status: supported
confidence: 0.95
tags: [quantitative, ST, OSCC, methods]
domain: methods/spatial-transcriptomics
source_papers:
  - spatial-transcriptomics-reveals-distinct-conserved-tumor
evidence:
  - source: spatial-transcriptomics-reveals-distinct-conserved-tumor
    type: supports
    strength: strong
    detail: "12 fresh-frozen surgical OSCC samples (10 unique patients) on 10x Visium; 24,876 spots, 43,648 post-normalization mean reads/spot; 13,950 malignant + 10,852 nonmalignant spots after CARD deconvolution >0.99 OR Numbat p_cnv > 0.99 plus pathologist SCC annotation."
conditions: "10x Genomics Visium, GRCh38, Space Ranger 1.3.1"
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement
The study profiled 12 HPV-negative OSCC samples (10 patients) on 10x Visium, recovering 24,876 spots with 43,648 mean reads/spot and 13,950 malignant spots.

## Evidence summary
Reported in Methods and Fig. 1; CNV analysis confirms recurrent chr3 deletions and chr9 amplifications across samples.

## Conditions and scope
HPV-negative OSCC; surgical samples; 10 µm cryosections.

## Counter-evidence
None.

## Linked ideas

## Open questions
Whether 10 patients are sufficient to claim full inter-patient TC/LE conservation.
