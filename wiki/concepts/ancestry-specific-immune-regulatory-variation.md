---
title: "Ancestry-specific immune regulatory variation"
aliases:
  - population-specific xQTL
tags: []
maturity: active
key_papers:
  - chinese-immune-multi-omics-atlas
first_introduced: ""
date_updated: 2026-06-04
related_concepts:
  - cell-type-specific-genetic-regulation-immune
---

## Definition

The phenomenon whereby a subset of regulatory genetic effects (eQTLs/caQTLs) on immune gene expression and chromatin accessibility are driven by variants common in one ancestry but rare or absent in others, making ancestry-diverse reference panels necessary for equitable disease mapping.

## Intuition

QTL atlases built predominantly in European-ancestry cohorts under-capture regulatory variants common in East Asian or African populations. Building references in under-represented populations surfaces ancestry-enriched and even latitude-selected regulatory signals.

## Formal notation

Population specificity is assessed by comparing minor allele frequencies (MAF) of lead xQTLs across reference panels (e.g. ALFA EUR/AFR/TOT) and by cross-dataset sharing statistics (π1, effect correlations) against OneK1K (European) and ImmuNexUT (East Asian).

## Variants

- Ancestry-rare lead xQTLs (MAF < 0.01 in EUR/AFR)
- Latitude-selected regulatory loci (north–south China)
- Population-specific disease pleiotropy (e.g. SLC16A11/T2D)

## Comparison

Complements [[concepts/cell-type-specific-genetic-regulation-immune]]: specificity arises along both the cell-type and the ancestry axes.

## When to use

When transferring GWAS/eQTL findings across populations or assessing portability of polygenic and mechanistic predictions.

## Known limitations

Within-cohort regional structure (north vs south China) can confound; common-variant focus (MAF > 0.1) excludes rare-variant effects.

## Open problems

Quantifying how much disease-risk transferability improves with ancestry-matched regulatory references.

## Key papers

- [[papers/chinese-immune-multi-omics-atlas]] — 10.4% of lead xQTLs rare (MAF < 0.01) in EUR/AFR/ALFA; latitude-selected loci and population-specific pleiotropy (e.g. rs312457→SLC16A11→T2D).

## My understanding

A population-genomics counterpart to cell type specificity; the Chinese-cohort framing is the paper's central equity contribution.
