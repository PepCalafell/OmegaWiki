---
title: "PyDESeq2 — Python reimplementation of DESeq2"
slug: pydeseq2
domain: "computational-biology / methods"
status: mainstream
aliases:
  - "PyDESeq2"
  - "pyDESeq2"
first_introduced: "Muzellec, Teleńczuk, Cabeli & Andreux 2023 *Bioinformatics*"
date_updated: 2026-06-03
source_url: "https://github.com/owkin/PyDESeq2"
---

## Definition

PyDESeq2 is a pure-Python reimplementation of the DESeq2 negative-binomial differential-expression workflow for bulk RNA-seq count data. It reproduces median-of-ratios normalization, empirical-Bayes dispersion shrinkage toward a fitted mean-dispersion curve, the negative-binomial GLM fit, and Wald testing, exposing them as scikit-learn-style Python objects rather than the original Bioconductor R package.

## Intuition

It lets Python-centric pipelines run DESeq2-equivalent DE without crossing the R/Python boundary, and makes the internal quantities (per-gene dispersion estimates, baseMean, LFC standard errors) directly inspectable as arrays — which is exactly what analytical power-analysis tools need as a reference baseline.

## Formal notation

Reproduces the DESeq2 model: counts \(K_{ij} \sim \mathrm{NB}(\mu_{ij}, \alpha_i)\) with \(\log_2 \mu_{ij}\) a linear function of the design, dispersion \(\alpha_i\) shrunk toward \(\alpha(\bar\mu)=a_0 + a_1/\bar\mu\).

## Key variants

- Versioned API; v0.4.8 used as the DESeq2 baseline in DEPower's validation.
- Supports the same design-formula and contrast semantics as Bioconductor DESeq2.

## Known limitations

- Inherits DESeq2's assumptions (negative-binomial, pseudobulk for single-cell).
- Numerical results can differ from R DESeq2 in edge cases (optimizer, shrinkage details).

## Open problems

- Maintaining exact parity with the evolving Bioconductor reference implementation.

## Relevance to active research

- Used as the "true"/full-procedure baseline against which approximate analytical power-analysis estimates are validated, e.g. [[papers/depower-approximate-power-analysis-deseq2]].
