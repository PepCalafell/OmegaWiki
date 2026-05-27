---
title: "WNN integration of spatial DNA methylation and RNA modalities yields enhanced cluster resolution beyond either single modality"
slug: wnn-multimodal-integration-improves-cluster-resolution-vs-single-modality
status: supported
confidence: 0.9
tags: [WNN, multimodal-integration, spatial-omics, clustering]
domain: computational biology / spatial omics
source_papers:
  - spatial-joint-profiling-dna-methylome-transcriptome
evidence:
  - source: spatial-joint-profiling-dna-methylome-transcriptome
    type: supports
    strength: strong
    detail: "Quote (p.3-4): 'The two modalities can be integrated to achieve improved discrimination of intercellular and spatial diversity using a weighted nearest neighbour (WNN) method... Each modality captured distinct yet complementary aspects of cellular identity and their integration through WNN analysis yielded clusters with enhanced resolution.' Concrete example: 14 WNN clusters (W0–W13) in E11 embryo vs fewer in DNAm-only or RNA-only views (Fig. 1f)."
conditions: "Mouse E11 embryo, 50 μm pixel size; replicates n=2."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

Joint integration of spatial DNA-methylation and RNA modalities via the WNN algorithm ([[foundations/wnn-weighted-nearest-neighbor-integration]]) produces more refined spatial clusters than either modality alone, matching anatomical structures (brain, spinal cord, heart, craniofacial regions) with higher fidelity.

## Evidence summary

Reported in [[papers/spatial-joint-profiling-dna-methylome-transcriptome]], Fig. 1f. WNN integration of DNAm and RNA modalities yields 14 spatial clusters in E11 mouse embryo, with anatomical correspondence demonstrated by overlay on histology.

## Conditions and scope

Mouse E11 embryo, 50 μm pixel size; WNN tested at one developmental stage and tissue type within the paper.

## Counter-evidence

Not all clusters benefit equally — some are dominated by a single modality (W6 by RNA, W11 by DNAm), suggesting WNN does not always reduce to "best of both worlds".

## Linked ideas

## Open questions

- Does WNN scale to >2 modalities (DNAm + RNA + ATAC + protein) in spatial multi-omics?
- Optimal WNN weighting in sparse-coverage regions.
