---
title: "Analytical power analysis for the DESeq2 model"
aliases:
  - "analytical sample-size estimation for DESeq2"
  - "closed-form DESeq2 power analysis"
tags: [power-analysis, rna-seq, experimental-design, deseq2, statistics]
maturity: emerging
key_papers:
  - depower-approximate-power-analysis-deseq2
first_introduced: "Gorin, Guruge & Goodman 2026 (DEPower)"
date_updated: 2026-06-03
related_concepts: [heuristic-dispersion-band-mean-expression, rare-cell-type-single-cell-enrichment]
---

## Definition

A closed-form (analytical) procedure for computing the sample size required to detect a given log-fold change at a target significance level under the DESeq2 negative-binomial Wald-test model — as opposed to the simulation-based power analyses that dominate the RNA-seq literature.

## Intuition

Because DESeq2 significance reduces to a Wald test (\(\sqrt{W}=\mathrm{LFC}/\sigma_{\mathrm{LFC}}\)), and the standard error \(\sigma_{\mathrm{LFC}}\) has an approximate closed form in the fitted means, dispersion, and replicate count, one can simply invert the significance condition to solve for \(n\). No data simulation is needed for an order-of-magnitude estimate.

## Formal notation

Require \(\sqrt{W}=z_{1-\alpha/2}\); with \(\sigma_{\mathrm{LFC}}^2=\frac{1}{n}\!\left(\frac{1}{W_0}+\frac{1}{W_1}\right)\), \(W_i=\frac{\mu_i}{1+\mu_i d}\), and \(\mu_1=e^{\mathrm{LFC}}\mu_0\), solve for the minimal \(n\).

## Variants

- Balanced vs. unbalanced designs (\(n_0\neq n_1\)) with adjusted \(\sigma_{\mathrm{LFC}}^2\) and \(\bar\mu\).
- Bulk vs. single-cell (pseudobulk) RNA-seq parameterizations.
- Multiple-testing variants: Bonferroni vs. approximate Benjamini–Hochberg.

## Comparison

- Simulation-based tools (scPower, scDesign, powsimR) are more flexible but slower and opaque; this analytical route is fast and transparent but rests on stronger approximations.
- Matches the test used downstream (DESeq2), unlike generic GLM power calculators.

## When to use

- Back-of-the-envelope study-design decisions before data exist, when the planned analysis is DESeq2/PyDESeq2.
- Sanity-checking whether a target effect is even detectable at feasible sample sizes.

## Known limitations

- Treats dispersion heuristically when no pilot data exist (see [[heuristic-dispersion-band-mean-expression]]).
- Neglects between-condition read-depth variability; estimates are a lower bound.

## Open problems

- Incorporating covariates/batches and small-sample Wald non-asymptotics into the closed form.

## Key papers

- [[papers/depower-approximate-power-analysis-deseq2]] — derives the procedure and ships the DEPower web calculator.

## My understanding

Directly useful for designing my own RNA-seq / single-nucleus experiments: it turns "how many samples do I need?" into an explicit DESeq2-consistent calculation rather than a guess or a slow simulation.
