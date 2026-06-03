---
title: "Wald test — asymptotic test of a single GLM parameter"
slug: wald-test
domain: "statistics / methods"
status: mainstream
aliases:
  - "Wald test"
  - "Wald statistic"
  - "two-sided Wald test"
first_introduced: "Wald 1943"
date_updated: 2026-06-03
source_url: "https://en.wikipedia.org/wiki/Wald_test"
---

## Definition

The Wald test assesses whether an estimated model parameter \(\hat\theta\) differs significantly from a null value (typically 0) by dividing the estimate by its standard error. The Wald statistic \(W = (\hat\theta/\sigma_{\hat\theta})^2\) is asymptotically chi-square distributed under the null; equivalently \(\sqrt{W}=\hat\theta/\sigma_{\hat\theta}\) is asymptotically standard normal.

## Intuition

It measures how many standard errors the estimate sits away from the null. The further (in SE units), the smaller the p-value. In DESeq2 differential expression, \(\hat\theta\) is the log-fold change and the Wald test is the default per-gene significance test.

## Formal notation

\(\sqrt{W} = \dfrac{\hat\theta}{\sigma_{\hat\theta}} = \dfrac{\mathrm{LFC}}{\sigma_{\mathrm{LFC}}}\); two-sided nominal p-value \(= 2\!\left[1-\Phi(\sqrt{W})\right]\); significance at level \(\alpha\) requires \(\sqrt{W}=z_{1-\alpha/2}\).

## Key variants

- Score (Lagrange-multiplier) test and likelihood-ratio test are asymptotically equivalent alternatives.
- DESeq2 offers an LRT as an alternative to the default Wald test.

## Known limitations

- Relies on asymptotic convergence to chi-square; less reliable at small sample sizes.
- Sensitive to the parameterization and to standard-error estimation quality.

## Open problems

- Small-sample corrections for negative-binomial GLM Wald inference.

## Relevance to active research

- The analytical sample-size derivation in [[papers/depower-approximate-power-analysis-deseq2]] inverts the Wald-test significance condition to solve for required replicate number.
