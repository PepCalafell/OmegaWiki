---
title: "Consensus Molecular Subtypes (CMS) classifier for colorectal cancer"
slug: cms-classifier-crc
domain: methods
status: mainstream
aliases:
  - CMS
  - consensus molecular subtypes
  - CMS classifier
  - CMS1
  - CMS2
  - CMS3
  - CMS4
  - colorectal CMS subtyping
  - Guinney CMS
first_introduced: "Guinney et al. 2015 Nat Med"
date_updated: 2026-05-25
source_url: ""
---

## Definition
The Consensus Molecular Subtypes (CMS) classifier partitions colorectal cancers into four transcriptional subtypes (CMS1 immune / MSI-high; CMS2 canonical Wnt/MYC; CMS3 metabolic; CMS4 mesenchymal / EMT) based on bulk RNA expression. It is the most-cited CRC molecular taxonomy and underlies stratified treatment and biomarker analyses.

## Intuition
Multiple early CRC subtyping schemes converged on four robust groups; CMS consolidates them into a stable RNA-based classifier widely used as the reference taxonomy.

## Formal notation
- 4 subtypes
- Originally trained on 18 datasets / ~4,000 CRC samples
- R package `CMSclassifier`

## Key variants
- Single-sample classifier (`classifyCMS`)
- Random-forest and nearest-template-prediction implementations

## Known limitations
- Stromal contamination shifts samples toward CMS4.
- Pure tumour cell-of-origin programs may differ from bulk-tissue CMS calls.

## Open problems
- A protein- or IHC-based CMS classifier deployable in routine pathology.
- CMS-class-specific therapy stratification beyond observational evidence.

## Relevance to active research
The reference taxonomy for CRC stratification studies, including the protein-level CMS validation and immune-subtype refinement described in TPCPA.
