---
title: "limma — Linear Models for Microarray and RNA-seq"
slug: limma-differential-expression
domain: bioinformatics / differential expression
status: mainstream
aliases:
  - limma
  - limma-voom
  - linear models for microarray
  - empirical Bayes moderated t-test
  - voom transformation
  - limma differential expression
  - FDR-adjusted limma
first_introduced: "2004"
date_updated: 2026-05-22
source_url: "https://bioconductor.org/packages/limma/"
---

## Definition

limma is an R/Bioconductor package fitting per-gene linear models with empirical-Bayes moderation of variance, and (via voom) supporting count-based RNA-seq through mean-variance modeling and precision weighting.

## Intuition

limma's empirical-Bayes shrinkage borrows information across genes to stabilise variance estimates in low-replicate experiments, yielding well-calibrated p-values where naive t-tests overfit; voom extends this to heteroscedastic counts.

## Relevance to active research

limma is the default DE engine for bulk-RNA-seq sepsis studies including Takahama et al. 2024 (FDR-adjusted P value < 0.01–0.1, |log2FC| > 2) and remains the most widely used baseline against which DESeq2/edgeR are compared.
