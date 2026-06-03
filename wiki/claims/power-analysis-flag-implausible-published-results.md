---
title: "Power-analysis mathematics can flag implausible published results but does not scale as a fraud detector"
slug: power-analysis-flag-implausible-published-results
status: proposed
confidence: 0.5
tags: [research-integrity, metascience, power-analysis, fraud-detection]
domain: "statistics / metascience"
source_papers:
  - depower-approximate-power-analysis-deseq2
evidence:
  - source: depower-approximate-power-analysis-deseq2
    type: supports
    strength: weak
    detail: "Aside proposing reverse power analysis to flag e.g. p=10^-200 at log2FC=1, n=3; authors enumerate reasons it is unlikely to be broadly fruitful at scale."
conditions: "Suggestive not conclusive; most useful as a diligence check on low-n, far-reaching claims."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

The same analytical mathematics can be run retrospectively to test whether a published p-value is mathematically plausible given the reported sample size and effect size (e.g. \(p=10^{-200}\) at \(\log_2\mathrm{FC}=1\), \(n=3\)), flagging possible analysis errors or misconduct — but the authors argue this is unlikely to be broadly fruitful at scale.

## Evidence summary

Proposed as an "aside" with an explicit list of limitations: it is laborious; inconsistencies are suggestive not conclusive; misuse is hard to distinguish from fraud; fraudulent studies more often use large public datasets where constraints don't bind; single-cell violations often stem from pseudoreplication; and fabricators more often manipulate data than test statistics.

## Conditions and scope

Best suited to diligence checks on far-reaching claims based on very few samples.

## Counter-evidence

High-expression, low-dispersion genes can legitimately yield arbitrarily low p-values, so single inconsistencies are not proof.

## Linked ideas

- [[concepts/power-analysis-research-fraud-detector]]

## Open questions

- Could plausibility screening be automated with acceptable false-positive rates?
