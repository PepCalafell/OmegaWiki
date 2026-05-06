---
title: "Hypoxia-PTEN-TERT telomere length axis"
aliases:
  - "hypoxia-PTEN-TERT axis"
  - "hypoxia-TERT-PTEN telomere model"
  - "hypoxia-modulated telomere length"
  - "PTEN-TERT negative correlation"
  - "PTEN-telomere axis"
  - "hypoxia-induced telomere shortening"
  - "TERT-PTEN-hypoxia interaction"
  - "telomere length under hypoxia"
  - "hypoxic telomere axis"
tags:
  - hypoxia
  - PTEN
  - TERT
  - telomere
  - prostate-cancer
  - HIF1A
maturity: emerging
key_papers:
  - molecular-landmarks-tumor-hypoxia-across-cancer
first_introduced: "Bhandari et al. 2019 Nat Genet"
date_updated: 2026-05-06
related_concepts: []
---

## Definition

A three-way interaction in which tumor hypoxia, PTEN mRNA abundance, and TERT mRNA abundance jointly modulate telomere length in localized prostate cancer. Demonstrated in [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] using a linear model on 333 TCGA + 215 CPC-GENE PRAD samples: hypoxia score, TERT, and PTEN each independently predict telomere length, and a significant three-way interaction term (Bonferroni-adjusted P=4.34×10⁻², linear model) indicates the effects are not additive. The lowest PTEN mRNA abundance is observed in tumors that are simultaneously hypoxic and high-TERT.

## Intuition

PTEN, hypoxia, and TERT are usually thought of as three independent axes of cancer biology. This finding shows that in localized PCa they form a coupled regulatory system: hypoxia induces TERT (a HIF1A target); TERT and PTEN show a strong negative mRNA correlation (CPC-GENE ρ=−0.36); and the joint state — hypoxic + high TERT — defines a subgroup with the lowest PTEN expression and the most aberrant telomere length. This positions telomere maintenance not as a parallel hallmark but as a downstream readout of microenvironmental and tumor-suppressor co-dysregulation.

## Formal notation

- Linear model: telomere_length ~ hypoxia + TERT + PTEN + hypoxia:TERT + hypoxia:PTEN + TERT:PTEN + hypoxia:TERT:PTEN
- Significant terms: hypoxia (P=2.17×10⁻³), TERT, PTEN, hypoxia:TERT:PTEN three-way (Bonferroni P=4.34×10⁻²)
- PTEN-TERT correlation: CPC-GENE ρ=−0.36, P=4.01×10⁻⁸; TCGA ρ=−0.15, P=7.21×10⁻³
- TERT is one of 51 HIF1A targets correlated with hypoxia in this paper
- Median PTEN mRNA: hypoxic high-TERT 5.55 < hypoxic low-TERT 5.79 < normoxic high-TERT 5.67 < normoxic low-TERT 6.05

## Variants

- TCGA replication shows weaker but consistent direction
- Hypoxia-associated CNAs in telomere-related pathways (Supplementary Fig. 6d)
- ATRX/DAXX (ALT pathway) variants not analyzed in this axis

## Comparison

| Telomere driver | Mechanism | Tissue |
|---|---|---|
| TERT promoter mutation | de novo GABP binding | melanoma, GBM, HCC |
| TERT amplification | copy-number gain | various |
| HIF1A → TERT induction | hypoxia-responsive | broad |
| ALT (ATRX/DAXX loss) | recombination-based | mesenchymal |
| PTEN-TERT-hypoxia 3-way | regulatory interaction | PCa (this paper) |

## When to use

- Modelling telomere length as outcome in PCa cohorts with matched mRNA + hypoxia
- Understanding why PTEN-loss + hypoxia tumors are clinically aggressive
- Building integrated models of nimbosus features (telomere length is one of the six pillars)

## Known limitations

- Mechanism for the three-way interaction is not characterized — descriptive linear-model finding only
- TelSeq estimation of telomere length from WGS is noisy
- Bulk-tumor mRNA confounds malignant + stromal contributions for both PTEN and TERT
- Replication in independent prospective cohorts pending

## Open problems

- Direct mechanistic test: does hypoxia → HIF1A → TERT, with PTEN loss removing brake on PI3K/AKT-mediated TERT post-translational stabilization?
- Whether targeting TERT (imetelstat) in hypoxic + PTEN-loss tumors is selectively effective
- How the axis interacts with the broader nimbosus phenotype

## Key papers

- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — primary description; linear model on 333+215 PRAD samples

## My understanding

This is one of the more mechanistically generative findings in the Bhandari paper — a multivariate interaction that, if mechanistically validated, would unify three previously separate aspects of tumor biology in localized PCa. For HypoxiaVERSE, it is a strong candidate motivating hypothesis for joint-target therapy (PTEN-loss + telomerase + hypoxia).
