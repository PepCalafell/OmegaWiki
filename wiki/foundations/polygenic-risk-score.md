---
title: "Polygenic risk score (PRS)"
slug: polygenic-risk-score
domain: methods
status: mainstream
aliases: ["PRS", "polygenic risk score", "polygenic score"]
first_introduced: "2009"
date_updated: 2026-06-12
source_url: "https://doi.org/10.1038/s41596-020-0353-1"
---

## Definition

A polygenic risk score aggregates the effects of many genetic variants (weighted by GWAS effect sizes) into a single per-individual score summarizing genetic predisposition to a trait.

## Intuition

Rather than testing one SNP, a PRS sums genome-wide allelic contributions, capturing the polygenic architecture of a phenotype such as the trained-immunity cytokine response.

## Formal notation

PRS_i = Σ_j β_j · g_ij, summed over variants j with GWAS weights β_j and individual genotype dosages g_ij; often p-value-thresholded and clumped.

## Key variants

P+T (clumping + thresholding), LDpred, lassosum, PRS-CS.

## Known limitations

Portability across ancestries is poor; explains limited variance; depends on training-GWAS power.

## Open problems

Trans-ancestry transferability and integration with non-genetic omics.

## Relevance to active research

Used as the genetic data layer in variance-partition analysis of IFN-γ trained immunity, where baseline DNA methylation explained more variance than PRS.
