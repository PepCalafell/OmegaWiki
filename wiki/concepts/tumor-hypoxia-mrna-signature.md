---
title: "Tumor hypoxia mRNA signature"
aliases:
  - "mRNA hypoxia signature"
  - "hypoxia metagene score"
  - "hypoxia gene-expression signature"
  - "HIF1A target signature"
  - "transcriptomic hypoxia score"
  - "expression-based hypoxia score"
  - "Buffa signature"
  - "Winter signature"
  - "Ragnum signature"
  - "pancancer hypoxia score"
  - "AS89 hypoxia score"
  - "hypoxia metagene"
tags:
  - hypoxia
  - cancer
  - genomics
  - signature
  - mRNA
  - HIF1A
  - methodology
maturity: stable
key_papers:
  - molecular-landmarks-tumor-hypoxia-across-cancer
  - characterization-hypoxia-associated-molecular-features-aid
first_introduced: "Buffa et al. 2010 Br J Cancer (51-gene metagene); Winter 2007, Ragnum 2015"
date_updated: 2026-05-06
related_concepts: []
---

## Definition

A tumor hypoxia mRNA signature is a gene-expression-derived continuous score that quantifies the cellular hypoxia state of a bulk tumor sample. It is constructed by selecting a small set of genes (typically 20–100) whose mRNA abundance is concordantly correlated with reduced oxygen tension across multiple training datasets, then summing or rank-aggregating their expression per sample. Multiple independent signatures (Buffa 2010, Winter 2007, Ragnum 2015, West, Sorensen, Elvidge, Hu, Seigneuric) have been published; cross-signature correlations are strong (mean ρ≈0.42, [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]]).

## Intuition

Direct measurement of intratumor oxygen tension requires invasive needle electrode (Eppendorf) or pimonidazole IHC, neither of which scales to thousands of samples. mRNA-based signatures substitute the genomic *response* to hypoxia (HIF1A target induction, glycolysis, angiogenesis, miR-210 host) for the underlying physical variable. Because the response is stereotyped and conserved across tumor types, a single signature can rank-order samples within and across cancer types.

## Formal notation

- Score per sample: rank-sum or median Z-score over the signature gene set
- Continuous output, typically standardized to mean 0, SD 1 within each cohort
- Pancancer ensembling (AS89 algorithm in Bhandari et al. 2019): integrate ≥2 independent signatures, correct for multiple comparisons, output adjusted P-values for downstream associations
- Signature components overlap across signatures: VEGFA, LDHA, PGK1, SLC2A1, ENO1, BNIP3, ALDOA, P4HA1, P4HA2, ADM, CA9, PDK1, NDRG1

## Variants

- Buffa 51-gene signature: cross-tumor concordant; primary signature in Bhandari pancancer
- Winter 99-gene signature: HNSC-derived
- Ragnum 32-gene signature: pimonidazole-validated, prostate-derived
- Sorensen pH-independent signature
- Protein-based hypoxia score (RPPA): correlates with mRNA signatures (BRCA ρ=0.58, OV ρ=0.42, COADREAD ρ=0.32; [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]])

## Comparison

| Method | Resolution | Validation against direct O₂ | Scalability |
|--------|------------|------------------------------|-------------|
| Eppendorf needle electrode | tumor-region | gold standard | not scalable |
| Pimonidazole IHC | spatial within section | strong | low (special staining) |
| mRNA hypoxia signature | bulk tumor | validated indirectly via outcome and direct-O₂ subsets | high (any RNA-seq / microarray cohort) |
| RPPA protein hypoxia score | bulk tumor | moderate | medium (limited antibody panels) |

## When to use

- Pancancer comparisons across thousands of samples (TCGA)
- When direct oxygen measurement is impossible (retrospective archived samples)
- For correlative discovery (e.g. linking hypoxia to mutation, CNA, miRNA, outcome)
- NOT for absolute oxygen tension; signatures rank-order samples but do not map to mmHg

## Known limitations

- Bulk-tumor scores confound malignant-cell hypoxia with stromal/immune compartment hypoxia
- "Pseudohypoxia" (VHL loss in KIRC, MYC amplification) elevates HIF1A targets without reduced O₂
- Cross-platform comparisons (microarray vs RNA-seq) require rank normalization
- Tumor-type bias: thyroid is consistently low-scoring even when direct measurements show hypoxia in some thyroid tumors

## Open problems

- Single-cell deconvolution: separating tumor-cell hypoxia from stromal hypoxia
- Calibration to absolute oxygen tension across signatures
- Validation in pediatric cancers (TCGA dominated by adult tumors)
- Temporal dynamics: signatures reflect *current* hypoxia or *integrated* hypoxia history?

## Key papers

- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — pancancer 8,006 tumors / 19 types using 8 signatures + AS89 ensembling
- [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] — TCGA hypoxic-MAC signatures (downstream interpretive use)

## My understanding

The Buffa-style signature is the right default for any pancancer hypoxia analysis on TCGA-scale data. For PCa specifically, Ragnum (pimonidazole-validated) is preferred when matched extrinsic hypoxia data are available. For the user's HypoxiaVERSE thesis, the relevant question is whether the signatures behave the same in immune cells (where HIF1A target sets are partly different from epithelium) — this is *not* what these signatures were derived for and should be validated separately.
