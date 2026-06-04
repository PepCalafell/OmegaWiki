---
title: "edgeR — negative-binomial differential expression"
slug: edger-differential-expression
domain: "methods / bulk-RNA-seq / differential-expression"
status: mainstream
aliases:
  - edgeR
  - edgeR quasi-likelihood
first_introduced: "Robinson, McCarthy & Smyth 2010 *Bioinformatics* (edgeR: a Bioconductor package for differential expression analysis of digital gene expression data)"
date_updated: 2026-06-04
source_url: "https://bioconductor.org/packages/edgeR/"
---

## Definition

edgeR is a Bioconductor package for differential-expression analysis of count data. It models read counts with a negative-binomial distribution, estimates gene-wise and trended dispersions by empirical Bayes, and tests for differences via exact tests or generalized linear models. The quasi-likelihood F-test (glmQLFit / glmQLFTest) provides stricter type-I error control for designed experiments.

## Intuition

RNA-seq counts are overdispersed (variance exceeds the mean), so a Poisson model underestimates variability. edgeR borrows information across genes to stabilize dispersion estimates, then fits a per-gene NB-GLM with the experimental design and tests contrasts of interest.

## Formal notation

For gene g, counts y_g ~ NB(μ_g, φ_g) with log μ_g = Xβ_g; the quasi-likelihood F-test assesses contrasts of β_g after estimating a gene-wise QL dispersion.

## Key variants

- Classic exact test versus GLM / quasi-likelihood (glmQLFTest).
- filterByExpr pre-filtering; TMM normalization (calcNormFactors).

## Known limitations

- Designed for bulk/pseudobulk counts; not for raw single-cell counts directly.
- Requires sufficient replicates per group for reliable dispersion estimates.

## Open problems

- Optimal pseudobulk aggregation strategy from single-cell data.
- Confounder handling when batch and biology are partially collinear.

## Relevance to active research

Applied to per-patient, per-cell-type pseudobulks (aggregated via decoupleR) with an additive design correcting for chemistry, sex and age to call disease-versus-healthy DEGs feeding the inflammation gene-selection pipeline. Sibling to [[deseq2-differential-expression]], [[limma-differential-expression]], [[pydeseq2]].
