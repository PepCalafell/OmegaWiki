---
title: "Noncoding variant effects on TF binding (multi-site additive model)"
aliases:
  - "noncoding variant TF binding effect"
  - "noncoding SNP TF binding"
  - "regulatory variant TF effect"
  - "GWAS variant TF binding interpretation"
  - "multi-site additive variant model"
  - "cumulative SNP effect on TF binding"
  - "overlapping-site variant model"
  - "variant interpretation in regulatory DNA"
  - "PADIT-seq variant effect prediction"
tags:
  - GWAS
  - noncoding-variant
  - transcription-factor
  - variant-effect-prediction
  - regulatory-genomics
maturity: emerging
key_papers:
  - multiple-overlapping-binding-sites-determine-transcription
first_introduced: "Khetan, Carroll & Bulyk 2025 (additive multi-site framing)"
date_updated: 2026-05-26
related_concepts:
  - overlapping-binding-sites-model
  - low-affinity-tf-binding-site
---

## Definition

A noncoding variant alters TF binding not by destroying or creating a single motif match, but by simultaneously perturbing multiple overlapping lower-affinity binding sites that together sum into total TF occupancy at that locus. The magnitude of effect on TF binding scales with the number of overlapping active k-mers altered by the variant; variants that change multiple consecutive active k-mers produce large effects, while variants altering a single k-mer produce modest but significant effects.

## Intuition

PWM/MotifBreakR-style predictors fail when a SNP creates or destroys an overlapping lower-affinity site without changing the consensus motif match — they see no effect. PADIT-seq's all-k-mer affinity table lets one tile across ref and alt alleles in 1-bp steps and count how many active k-mers change. Variants like rs606231230 (pathogenic for preaxial polydactyly in a HOXD13 limb enhancer) flip multiple overlapping HOXD13 active 8-mers; PADIT-seq catches these even when MotifBreakR doesn't.

## Formal notation

- Variant effect score: Σ (PADIT-seq activity at ref) − Σ (PADIT-seq activity at alt) across all overlapping k-mers covering the SNP
- Number of altered active k-mers correlates with absolute SNP-SELEX PBS
- PADIT-seq AUROC on custom-PBM-validated variants: 0.943 (HOXD13), 0.962 (EGR1); vs MotifBreakR 0.790 / 0.872
- In vivo validation: 91% concordance with allele-specific ChIP-seq; MPRA expression effects confirm in cells

## Variants

- Variants altering many overlapping sites (e.g. rs606231230, rs79228650): large effect, easily detected
- Variants altering a single overlapping site (e.g. rs1104802, rs73414426): modest but significant effect, missed by single-motif models

## Comparison

vs MotifBreakR: PWM-based, single-motif; misses multi-site effects
vs SNP-SELEX PBS: experimental but limited dynamic range; PADIT-seq detects ~5× more subtler variants and correlates with PBS in their shared dynamic range
vs DeepSEA / Enformer / TF-binding deep nets: model-based predictors trained on ChIP-seq; orthogonal but harder to interpret mechanistically; OBS framework gives an explicit additive mechanism

## When to use

- Prioritising noncoding GWAS variants for follow-up functional assays
- Re-scoring variants where MotifBreakR predicts no effect but ChIP-seq / MPRA disagree
- Designing CRISPR-edited single-nucleotide perturbations at enhancers

## Known limitations

- Demonstrated for HOXD13 and EGR1; not yet a genome-wide variant scorer across all TFs
- Requires PADIT-seq affinity tables per TF
- Does not yet model chromatin context, cofactor competition, or 3D contacts

## Open problems

- Building a TF-wide PADIT-seq atlas for variant interpretation
- Integrating OBS variant scoring with MPRA expression data at scale
- Quantifying cumulative effects of multiple linked variants on the same enhancer

## Relevance to active research

[[papers/multiple-overlapping-binding-sites-determine-transcription]] uses this framing to score 5,748 + 4,136 SNPs vs SNP-SELEX and confirms it experimentally on ~280 custom-PBM-validated variants per TF, including the pathogenic rs606231230 (preaxial polydactyly).
