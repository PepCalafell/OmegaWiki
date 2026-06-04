---
title: "MOFA — Multi-Omics Factor Analysis"
slug: multi-omics-factor-analysis-mofa
domain: computational biology
status: mainstream
aliases:
  - MOFA
  - MOFA+
  - multi-omics factor analysis
first_introduced: "2018 (Argelaguet et al., Mol Syst Biol)"
date_updated: 2026-06-04
source_url: "https://doi.org/10.15252/msb.20178124"
---

## Definition

MOFA is an unsupervised factor-analysis framework that infers a small set of latent factors capturing the principal axes of variation shared across (and specific to) multiple data modalities measured on the same samples. It generalizes PCA to the multi-omics setting.

## Intuition

Each latent factor is a coordinated source of variability (e.g. age, sex) that loads onto features across modalities. Inspecting the high-weight features of a factor yields biological interpretation; the variance explained per modality reveals which omics layers drive each factor.

## Formal notation

Given modalities `Y_m` (samples × features), MOFA factorizes each as `Y_m ≈ Z W_m^T + ε`, where `Z` is the shared factor matrix (samples × factors) and `W_m` are modality-specific loadings.

## Key variants

- MOFA (original) and MOFA+ (scalable, group-aware)
- Application to bulk individual-level omics (metabolomics, lipidomics, cell proportions)
- Application to pseudobulk gene expression + chromatin accessibility across cell types

## Known limitations

- Linear model; nonlinear structure may be missed.
- Factor interpretation requires manual inspection of loadings.
- Sensitive to feature scaling and batch structure.

## Open problems

- Integration of >1M-cell single-cell modalities without pseudobulking.

## Relevance to active research

Used in [[papers/chinese-immune-multi-omics-atlas]] to identify sex- and age-associated latent factors across blood biochemistry, lipidomics, metabolomics, and immune cell proportions (e.g. factor 7 as the most age-associated RNA-ATAC component).
