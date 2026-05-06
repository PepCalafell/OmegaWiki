---
title: "Tumor hypoxia is associated with elevated genomic instability across cancer types"
slug: hypoxia-elevates-genomic-instability-pancancer
status: supported
confidence: 0.85
tags:
  - hypoxia
  - genomic-instability
  - PGA
  - pancancer
  - cancer
domain: "oncology / cancer-genomics"
source_papers:
  - molecular-landmarks-tumor-hypoxia-across-cancer
evidence:
  - source: molecular-landmarks-tumor-hypoxia-across-cancer
    type: supports
    strength: strong
    detail: "10 of 19 tumor types showed significant association between PGA and hypoxia score (Bonferroni-adjusted P<0.05); no tumor type showed inverse association. Quote (p.309): 'Tumor hypoxia was associated with significantly elevated genomic instability in 10 of 19 tumor types, and in no case was tumor hypoxia associated with decreased genomic instability.' In localized PCa specifically: Bonferroni P=3.55×10⁻⁵, ρ=0.24."
conditions: "Holds across solid tumor adenocarcinomas and squamous carcinomas. Strongest in BRCA, PAAD, PRAD, LGG, LUSC. Not significant in THCA, OV, BLCA, PCPG, COADREAD."
date_proposed: 2026-05-06
date_updated: 2026-05-06
---

## Statement

Tumor hypoxia, measured by mRNA-based pancancer signatures, is statistically associated with elevated genomic instability (PGA / percent genome altered) in 10 of 19 TCGA tumor types. The association is unidirectional — hypoxic tumors show *more* CNA burden, never less. The mechanistic basis is supported by prior work showing hypoxic downregulation of homologous recombination (RAD51) and mismatch repair (MLH1, MSH2), and by hypoxia-driven selection of apoptosis-deficient subclones with mutant TP53.

## Evidence summary

- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — pancancer 8,006 tumors / 19 types: 10/19 significant; 0/19 inverse.
- Mechanistic priors: Bindra 2004 (RAD51 down in hypoxia), Mihaylova 2003 (MLH1 down), Koshiji 2005 (HIF1α-induced mutator), Bristow & Hill 2008 (review).

## Conditions and scope

- Cancer-type-dependent; not all 19 TCGA tumor types show the association.
- Bulk-tumor signature confounds malignant + stromal hypoxia; effect may be larger in tumor-cell compartment specifically.
- PGA is a CNA-burden proxy; SNV-burden and chromothripsis associations exist but are tested separately in the paper.

## Counter-evidence

- THCA, OV, BLCA, PCPG, COADREAD: no significant hypoxia-PGA association at the cohort level.
- Direct causal proof (longitudinal in vivo modelling under modulated hypoxia) is not in this paper.

## Linked ideas

(none yet — ideas to be added when generated)

## Open questions

- Why does the hypoxia-PGA association fail in ~9/19 tumor types? Tumor-type-specific DNA-repair compensations?
- Is the link mediated entirely by selection (hypoxia kills apoptosis-competent cells) or also by direct mutagenesis under low O₂?
- Does targeting hypoxia (evofosfamide, etc.) reduce subsequent genomic instability accumulation?
