---
title: "MYC oncogene gain co-occurs with elevated hypoxia in 11 tumor types"
slug: myc-gain-co-occurs-hypoxia-pancancer
status: supported
confidence: 0.85
tags:
  - MYC
  - hypoxia
  - oncogene
  - pancancer
  - amplification
  - CNA
domain: "oncology / cancer-genomics"
source_papers:
  - molecular-landmarks-tumor-hypoxia-across-cancer
evidence:
  - source: molecular-landmarks-tumor-hypoxia-across-cancer
    type: supports
    strength: strong
    detail: "Pancancer analysis of 112 cancer driver genes altered by CNAs identifies MYC as the most consistent oncogene-hypoxia association. Quote (p.309): 'gain of the MYC oncogene was associated with elevated hypoxia in 11 separate tumor types.' KIRC-specific: gain of MYC Bonferroni P=3.71×10⁻⁸. BRCA-specific: MYCN gain Bonferroni P=2.75×10⁻³². Mechanistic interpretation: MYC amplification potentiates biosynthetic capacity that may underlie hypoxia tolerance."
conditions: "Pancancer; assessed across 19 TCGA tumor types via consensus CNA clustering."
date_proposed: 2026-05-06
date_updated: 2026-05-06
---

## Statement

In a pancancer analysis of 112 cancer driver genes altered by copy-number aberrations across 19 tumor types, MYC oncogene gain co-occurs with elevated tumor hypoxia in 11 separate tumor types — the most consistent oncogene-hypoxia association in the dataset. The strongest signal is in renal clear cell carcinoma (KIRC, Bonferroni P=3.71×10⁻⁸); MYCN gain shows a complementary association in breast cancer (Bonferroni P=2.75×10⁻³²). PTEN loss is the corresponding tumor-suppressor association (7 tumor types).

## Evidence summary

- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — pancancer evidence: 11/19 tumor types significant; specific cancer-type signals (KIRC MYC, BRCA MYCN).

## Conditions and scope

- Pancancer; bulk-tumor CNA + mRNA hypoxia.
- Tumor-type-specific patterns (KIRC, BRCA, etc.) — not all 19 types significant.

## Counter-evidence

- Mechanism of MYC-hypoxia coupling not directly tested in this paper; speculative biosynthetic-tolerance link.
- Pseudohypoxia in KIRC (VHL loss → HIF1α stabilization) may confound the KIRC-MYC association.

## Linked ideas

(none yet)

## Open questions

- Why is MYC amplification more consistently linked to hypoxia than other classical oncogenes?
- Does MYC-driven biosynthetic capacity *cause* tolerance of hypoxic stress, or merely co-select with hypoxia-resistant phenotypes?
- Mechanistic basis for MYCN-hypoxia in BRCA — pediatric-tumor MYCN biology may provide leads
