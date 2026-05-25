---
title: "Immune consensus cluster (immune CC) for CRC prognosis"
aliases:
  - immune CC
  - immune consensus cluster
  - CRC immune subtypes
  - immune CC1 CC2
  - proteome-defined CRC immune subtypes
  - immune cluster prognostic CRC
  - CRC immune phenotype subtypes
  - proteomics-derived CRC immune subtypes
  - immune-active vs immune-suppressed CRC
  - immune CC RFS
tags: [crc, immune-subtypes, prognosis, proteomics, treg, cd8]
maturity: emerging
key_papers:
  - pan-cancer-proteome-atlas-mass-spectrometry
first_introduced: "Knol et al. 2025"
date_updated: 2026-05-25
related_concepts: []
---

## Definition
Immune consensus clusters (CC1, CC2; CC3 in NKI cohort only) are proteome-derived CRC subgroups defined by hierarchical clustering of Tamborero immune-signature ssGSEA scores across 195 CRC samples. CC1 is adaptive-cytotoxic-skewed (high CD8+ T, Th, low Treg, low innate); CC2 is innate-immune-skewed (high macrophages, neutrophils, Tregs, mast cells); CC1 has better RFS than CC2 in stage-2 disease.

## Intuition
RNA-defined CMS subtypes correlate with immune infiltration but mix multiple immune phenotypes. Clustering the immune-signature space directly (rather than the whole proteome) extracts an orthogonal prognostic axis, dominated by the activated CD8+ / Th vs Treg / macrophage balance.

## Formal notation
- 195 CRC bulk DIA-MS proteomes
- Tamborero immune signatures via ssGSEA → hierarchical clustering
- Two reproducible CCs across AMC + EMC; CC3 NKI-specific

## Variants
- Stage-2 AMC cohort (RFS)
- Stage-1/2 EMC cohort (DFS) — immune-CC direction preserved despite CMS direction inversion

## Comparison
- vs **CMS classification (Guinney 2015)**: immune CC is more significantly prognostic for RFS than CMS in the AMC cohort.
- vs **IHC-based CD8 / CD3 scoring**: immune CC integrates multiple subsets and aligns with Galon-style immune-score logic but operates on bulk proteome.

## When to use
- Prognostic stratification of stage-2 CRC
- Hypothesis generation for adaptive-vs-innate immune balance as the dominant prognostic axis

## Known limitations
- One discovery cohort with RFS; no orthogonal IHC validation.
- ssGSEA signatures inherit Tamborero-set biases.
- Multivariable adjustment for MSI, KRAS, BRAF, stage not reported.

## Open problems
- Translation to deployable IHC or targeted-MS panel.
- Mechanistic link between Treg/macrophage skew and recurrence.

## Key papers
- [[papers/pan-cancer-proteome-atlas-mass-spectrometry]]

## My understanding
The cleanest result of the paper — a proteome immune-axis that out-predicts CMS for RFS in stage-2 CRC. Deserves prospective validation with multivariate models; if it holds, it is a candidate adjuvant-therapy decision biomarker.
