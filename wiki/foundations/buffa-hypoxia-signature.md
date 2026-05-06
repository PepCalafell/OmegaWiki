---
title: "Buffa hypoxia metagene signature"
slug: buffa-hypoxia-signature
domain: "methods / cancer-genomics / hypoxia-quantification"
status: mainstream
aliases:
  - "Buffa signature"
  - "Buffa hypoxia metagene"
  - "Buffa 51-gene hypoxia signature"
  - "common hypoxia metagene"
  - "mRNA hypoxia score"
  - "hypoxia metagene signature"
  - "common hypoxia signature"
  - "pancancer hypoxia signature"
  - "Buffa 2010"
first_introduced: "Buffa et al. 2010 Br J Cancer"
date_updated: 2026-05-06
source_url: "https://doi.org/10.1038/sj.bjc.6605450"
---

## Definition

The Buffa hypoxia signature is a 51-gene mRNA expression metagene derived by Buffa et al. (2010, Br J Cancer) using a meta-analysis approach that selected genes whose expression is concordantly correlated with hypoxia across head-and-neck, breast, and lung cancer datasets. The signature is computed by summing (or averaging) the relative expression rank of the 51 component genes per sample, yielding a continuous "hypoxia score" that has prognostic value for relapse and overall survival across multiple cancer types.

## Intuition

Direct measurement of tumor oxygenation (Eppendorf needle electrode, pimonidazole IHC) is invasive and not scalable. The Buffa signature substitutes a genomic readout: cells exposed to hypoxia coherently upregulate a stereotyped set of HIF1A target genes (glycolysis, angiogenesis, miR-210), and this pattern can be read off bulk mRNA expression. The signature is *robust to tumor type* — its 51 genes were selected for cross-tumor concordance — making it the workhorse for pancancer hypoxia analyses.

## Formal notation

- Composition: 51 genes selected for high-quality hypoxia association across HNSC, BRCA, NSCLC training cohorts
- Score: per-sample rank-sum of the 51 genes (or median Z-score)
- Continuous output: typically standardized to mean 0, SD 1 within a cohort; comparable across cohorts after rank-based normalization
- Component genes (representative): VEGFA, LDHA, PGK1, SLC2A1 (GLUT1), ENO1, BNIP3, ALDOA, P4HA1, P4HA2, ADM, CA9 (CAIX), ANGPTL4, NDRG1, MIF, PDK1

## Key variants

- Winter et al. 2007: 99-gene head-and-neck-derived signature (more HNSC-biased)
- Ragnum et al. 2015: 32-gene signature derived from pimonidazole-stratified prostate samples (validated against direct extrinsic hypoxia measurement)
- Sorensen et al.: pH-independent hypoxia signature from squamous-cell lines
- West et al., Elvidge et al., Hu et al., Seigneuric et al.: tumor-type-specific or context-specific signatures
- Pan-tumor ensembling: integrating ≥8 independent signatures (as in [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]]) yields robust scores with mean pairwise ρ=0.42±0.21

## Known limitations

- Relies on bulk mRNA — confounds malignant-cell hypoxia with stromal/immune hypoxia
- mRNA does not directly equal oxygen tension; high HIF1A target expression can occur via VHL loss (KIRC) or MYC amplification without true hypoxia ("pseudohypoxia")
- Cross-cohort comparisons require careful batch and rank normalization
- Tumor-type-specific outliers exist (e.g., thyroid is consistently low-scoring even though some thyroid tumors are hypoxic by direct measurement)

## Open problems

- How to deconvolve epithelium-specific hypoxia from stromal hypoxia using single-cell or spatial methods
- Pediatric tumors are underrepresented in signature derivation cohorts
- Whether absolute hypoxia scores can be calibrated across mRNA platforms (microarray vs RNA-seq) without rank normalization

## Relevance to active research

The Buffa signature is the primary mRNA-based hypoxia score used in [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] for the pancancer landscape (8,006 tumors, 19 types). It is also one of the eight signatures integrated via the AS89 algorithm in that paper's ensemble approach. Buffa-style pancancer hypoxia scoring is the de facto standard for any wiki-level cross-cancer hypoxia comparison.
