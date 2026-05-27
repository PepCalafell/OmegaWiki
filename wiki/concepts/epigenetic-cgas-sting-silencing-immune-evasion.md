---
title: "Epigenetic cGAS/STING silencing as a tumor immune-evasion mechanism"
aliases:
  - STING promoter methylation
  - cGAS hypermethylation
  - EZH2-KDM5 STING silencing
  - epigenetic STING immune escape
tags:
  - epigenetics
  - cgas-sting
  - immune-evasion
  - dnmt
  - ezh2
  - h3k27me3
maturity: stable
key_papers:
  - targeting-sting-generate-therapeutic-anti-tumor
first_introduced: "2018"
date_updated: 2026-05-27
related_concepts: []
---

## Definition

Rather than mutating cGAS or STING, tumor cells most commonly silence the pathway epigenetically via (a) DNMT-mediated promoter CpG hypermethylation, (b) EZH2-deposited H3K27me3, and (c) KDM5-mediated H3K4me3 removal. Observed in glioblastoma, colorectal, melanoma, ovarian, TNBC, NSCLC (KRAS-LKB1), and SCLC neuroendocrine subtypes.

## Intuition

Tumors that arise in DNA-damage-prone or chronically inflamed contexts must dampen STING-IFN signaling to survive — but mutating the gene is costly (STING/cGAS are needed for normal homeostasis). Epigenetic silencing is reversible, dose-tunable, and co-regulated with antigen-presentation machinery, making it both a hallmark of immune escape AND a re-actionable target.

## Variants

- DNMT1-mediated promoter methylation — reversible with DNMT inhibitors (e.g., decitabine, azacitidine)
- EZH2-H3K27me3 — reversible with tazemetostat / valemetostat
- KDM5 H3K4me3 demethylation — KDM5 inhibitors in development
- MYC-driven repression of STING and STING-target genes (TNBC) — links oncogene activation to STING silencing

## When to use

When stratifying tumors for STING-pathway-directed therapy. cGAS/STING staining + ISG expression signatures should guide whether to (a) directly agonize STING or (b) first derepress with DNMT/EZH2 inhibition.

## Key papers

- [[papers/targeting-sting-generate-therapeutic-anti-tumor]] — review of mechanisms and tumor-type distribution

## Open problems

- Predictive cutoffs for cGAS/STING protein staining as a biomarker
- Whether epigenetic derepression alone is sufficient or always needs a co-stimulus (STING agonist, radiation, MPS1 inhibitor)

## My understanding

This concept reframes "STING-cold" tumors as a *druggable* subset — they are silent not because of genetic deletion but because of reversible chromatin state. Epigenetic priming + downstream STING agonism is the cleanest therapeutic implication.
