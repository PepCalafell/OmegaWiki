---
title: "Pan-cancer conserved leading-edge (LE) signature"
aliases:
  - pan-cancer LE signature
  - conserved leading edge program
  - LE gene signature pan-cancer
  - invasive front signature
  - pan-cancer tumor invasive edge
  - LE-associated transcriptional program
  - conserved invasive program solid tumors
  - LE prognostic signature
  - pan-tumor LE biology
  - invasive edge signature TCGA
tags: [pan-cancer, leading-edge, prognosis, TCGA, spatial-transcriptomics, EMT]
maturity: active
key_papers:
  - spatial-transcriptomics-reveals-distinct-conserved-tumor
first_introduced: "Arora & Cao et al. 2023 Nat Commun"
date_updated: 2026-05-22
related_concepts: []
---

## Definition
A transcriptional program associated with the invasive front of solid tumours that is conserved across at least 17 cancer types in ST data and is significantly associated with worse OS / DSS in roughly 20 TCGA cancer cohorts. The signature is enriched for ECM remodelling (COL1A1, COL1A2, LAMB3), EMT initiation (MT2A, NME2, IFITM3), and adhesive/inflammatory ligand-receptor pairs (LAMB3-ITGA6_ITGB4, MIF-CD74_CD44).

## Intuition
If different solid tumours converge on the same invasive transcriptional program, that program is more likely to reflect a shared cell-state attractor than a tissue-of-origin quirk — and therefore a more promising target for broadly applicable therapy.

## Variants
- ST-derived raw LE signature (~91 genes upregulated across ≥10 samples)
- Single-sample gene-set enrichment score for bulk RNA-seq (TCGA-validated)
- scPred-classifier output (per-spot LE probability for new ST samples)

## Comparison
The p-EMT signature from Puram 2017 HNSCC scRNA-seq only partially overlaps (7 DEGs). The LE signature is broader, captures ECM/fibrovascular niche components, and generalises across tumour types where p-EMT does not.

## When to use
- Stratifying bulk RNA-seq cohorts by LE enrichment for survival modelling
- Selecting candidate drugs that downregulate LE program members
- Building pan-cancer comparators across ST studies

## Known limitations
- Not associated with classical clinicopathological covariates (stage, grade, margins) in OSCC — appears to be an independent axis
- Discriminative power may degrade in tumours lacking obvious invasive-front histology (e.g. some haematological or paediatric tumours)
- Cancer types BRCA (OS) and LUSC (DSS) are exceptions to the LE → worse-outcome pattern

## Open problems
- Whether LE signature subtypes exist (e.g. ECM-dominant vs immune-cold variants)
- Causal upstream drivers shared across cancers

## Key papers
- [[papers/spatial-transcriptomics-reveals-distinct-conserved-tumor]]

## My understanding
The pan-cancer conservation is the headline finding of the paper. It reframes "tumour invasion" as a shared transcriptional attractor rather than a tissue-specific behaviour, which is a strong frame for any cross-cancer therapeutic strategy.
