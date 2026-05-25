---
title: "Proteome-defined CMS markers for colorectal cancer"
aliases:
  - protein-level CMS markers
  - proteomic CMS subtyping
  - CMS protein signatures
  - CMS1 CMS2 CMS3 CMS4 proteomic markers
  - colorectal CMS proteins
  - consensus molecular subtype proteome
  - CRC CMS prot/mRNA
  - proteome-derived CMS
  - protein-based CMS classifier
  - CMS markers from MS proteomics
tags: [crc, cms, biomarkers, proteomics, subtyping]
maturity: emerging
key_papers:
  - pan-cancer-proteome-atlas-mass-spectrometry
first_introduced: "Knol et al. 2025"
date_updated: 2026-05-25
related_concepts: []
---

## Definition
A set of proteome-derived protein markers (top 200 per CMS subtype) defined by TPCPA across 195 CRC samples that recapitulate transcriptomic CMS subtype assignments, with most markers RNA-validated externally and a 79-protein subset showing CMS-specific behaviour only at the protein level.

## Intuition
CMS subtypes were originally defined from bulk RNA. Mapping those subtypes onto the proteome both validates the RNA classifier and surfaces protein-only features (e.g., CMS2 mitochondrial respiration) that RNA misses.

## Formal notation
- Discovery cohort: 195 CRC samples (AMC + EMC + NKI)
- Top 200 differentially abundant proteins per CMS vs others
- Validation: external RNA cohorts on TPCPA "CRC CMS prot/mRNA" portal module

## Variants
- CMS1 — immune-rich + new proteome-level MTORC1 enrichment
- CMS2 — canonical Wnt/MYC RNA, plus proteome-only mitochondrial respiration / translation
- CMS3 — metabolic + new proteome peroxisome / protein-secretion features
- CMS4 — mesenchymal + new proteome ROS, p53, UV, hypoxia hallmarks

## Comparison
- vs **RNA CMS classifier (Guinney 2015)**: same subtype labels, proteome refines biology and adds prognostic immune-CC layer.
- vs **CPTAC CRC proteomics**: TPCPA is DIA-MS rather than TMT, larger cancer-type breadth.

## When to use
- Subtype confirmation on tumours where only protein extracts (e.g., FFPE) are available.
- Discovery of post-transcriptionally regulated CMS biology.

## Known limitations
- Subtype calls inherit RNA-classifier assumptions.
- No external proteome cohort for direct CMS validation.

## Open problems
- An IHC- or DIA-based CMS classifier deployable in routine pathology.

## Key papers
- [[papers/pan-cancer-proteome-atlas-mass-spectrometry]]

## My understanding
Proteome CMS markers are interesting less as a competing classifier than as a way to read out *protein-level* CMS biology — particularly the 79 RNA-discordant proteins, which point to translational control or stromal/immune contribution.
