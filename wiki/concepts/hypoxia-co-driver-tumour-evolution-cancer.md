---
title: "Hypoxia is a co-driver of tumour evolution alongside cancer driver genes"
aliases:
  - hypoxia co-driver clonal evolution
  - hypoxia driver-gene synergy
  - hypoxia TP53 co-selection
  - hypoxia PTEN co-selection
  - hypoxia MYC co-selection
  - hypoxia BCL2 co-selection
  - hypoxia microenvironmental cofactor
  - hypoxia early-clonal selection
  - hypoxia driver mutation enrichment
  - hypoxia tumour evolutionary trajectory
  - hypoxia PCAWG driver enrichment
tags:
  - hypoxia
  - clonal-evolution
  - cancer-genomics
maturity: stable
key_papers:
  - tumour-hypoxia-driving-genomic-instability-tumour
  - molecular-landmarks-tumor-hypoxia-across-cancer
first_introduced: "2019"
date_updated: 2026-05-13
related_concepts:
  - hypoxia-genomic-instability-pga
  - tumor-subclonal-evolution-architecture
---

## Definition

Whole-genome sequencing of human tumours (PCAWG, prostate cohorts, HCC, TRACERx Renal) shows that high hypoxia co-occurs with — and likely selects for — driver mutations in MYC, BCL2, TP53 and PTEN, with hypoxia and the driver acting as cooperating cofactors in clonal evolution. Isogenic competition assays confirm that TP53-null or BCL2-overexpressing cells outcompete wild-type under hypoxia by escaping apoptosis.

## Intuition

Hypoxia provides the selective pressure; driver mutations provide the survival vehicle (apoptosis resistance, metabolic flexibility, deregulated AKT). 99% of hypoxia-associated CNAs in prostate cancer occur early in tumour evolution; hypoxia preferentially associates with clonal (not subclonal) mutations, suggesting hypoxia operates before subclonal diversification.

## Variants

- TP53 mutation × hypoxia (apoptosis evasion)
- BCL2 overexpression × hypoxia (anti-apoptotic)
- PTEN loss × hypoxia (HIF amplification + AKT)
- MYC activation × hypoxia (MAX-MXI1 axis, glycolytic flux)
- KRAS-mutant × PLCγ1 loss under hypoxia (lung adenocarcinoma)
- HPV E6/E7 × hypoxia (ROS amplification)

## When to use

Use for any analysis linking hypoxia score to driver-gene status or to predict early-vs-late mutation timing.

## Known limitations

Bulk-sequencing inference; needs validation via isogenic clonal models and spatial sequencing in matched normoxic/hypoxic regions.

## Open problems

- Hypoxia "niches" with locally distinct driver enrichment
- Pseudohypoxic vs true-hypoxic separation in driver-co-occurrence analyses

## Key papers

- [[papers/tumour-hypoxia-driving-genomic-instability-tumour]] — review of cofactor evidence
- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — Bhandari et al. 2019 PCAWG analysis

## My understanding

The genomics-side complement to the mutator/repair concepts. For thesis work this is the bridge between hypoxia biology and the cancer driver-gene literature.
