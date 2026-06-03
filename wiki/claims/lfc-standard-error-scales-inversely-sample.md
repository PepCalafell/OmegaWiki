---
title: "The LFC standard error scales inversely with sample size and per-sample Fisher information"
slug: lfc-standard-error-scales-inversely-sample
status: supported
confidence: 0.9
tags: [deseq2, standard-error, dispersion, power-analysis, statistics]
domain: "statistics / methods"
source_papers:
  - depower-approximate-power-analysis-deseq2
evidence:
  - source: depower-approximate-power-analysis-deseq2
    type: supports
    strength: strong
    detail: "Eq. 2: σ²_LFC = (1/n)(1/W0 + 1/W1), W_i = μ_i/(1+μ_i d); balanced design, depth variability neglected."
conditions: "Balanced design with n replicates/condition; between-replicate read-depth variability neglected."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

For a balanced two-condition DESeq2 contrast, the squared standard error of the log-fold change is approximately \(\sigma_{\mathrm{LFC}}^2=\frac{1}{n}\!\left(\frac{1}{W_0}+\frac{1}{W_1}\right)\), where the per-sample Fisher-information contributions are \(W_i=\frac{\mu_i}{1+\mu_i d}\), adjusting fitted means by the gene-specific dispersion \(d\), with \(\mu_1=e^{\mathrm{LFC}}\mu_0\).

## Evidence summary

Derived from the DESeq2 negative-binomial GLM information matrix (Eq. 2); the unbalanced generalization is Eq. 6.

## Conditions and scope

Approximation neglecting systematic read-depth differences between conditions; exact only in that idealized regime.

## Counter-evidence

Real data with depth imbalance, batch effects, or NB-model violation inflate the true standard error.

## Linked ideas

- [[concepts/analytical-power-analysis-deseq2-model]]
- Dispersion \(d\) supplied heuristically: [[concepts/heuristic-dispersion-band-mean-expression]]

## Open questions

- Magnitude of error introduced by neglecting depth variability across realistic designs.
