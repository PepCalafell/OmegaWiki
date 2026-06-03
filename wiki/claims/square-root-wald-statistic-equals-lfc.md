---
title: "The square-root Wald statistic equals the LFC divided by its standard error"
slug: square-root-wald-statistic-equals-lfc
status: supported
confidence: 0.95
tags: [wald-test, deseq2, statistics, power-analysis]
domain: "statistics / methods"
source_papers:
  - depower-approximate-power-analysis-deseq2
evidence:
  - source: depower-approximate-power-analysis-deseq2
    type: supports
    strength: strong
    detail: "Standard DESeq2 Wald-test identity; significance at level α requires √W = z_{1−α/2}."
conditions: "Single binary covariate, two-sided Wald test under H0: θ=0, DESeq2 model."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

In DESeq2 differential testing the square-root Wald statistic is \(\sqrt{W}=\hat\theta/\sigma_{\hat\theta}=\mathrm{LFC}/\sigma_{\mathrm{LFC}}\); the two-sided nominal p-value is \(2[1-\Phi(\sqrt{W})]\), so significance at level \(\alpha\) requires \(\sqrt{W}=z_{1-\alpha/2}\).

## Evidence summary

Standard mathematical identity of the Wald test, restated as the foundation of DEPower's derivation (Eq. 1).

## Conditions and scope

Single-parameter two-sided Wald test under the DESeq2 negative-binomial GLM.

## Counter-evidence

None; this is a definitional relationship.

## Linked ideas

- Inverted to derive required sample size: [[concepts/analytical-power-analysis-deseq2-model]]

## Open questions

- Small-sample departures from the asymptotic normal approximation.
