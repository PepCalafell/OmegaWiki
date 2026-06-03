---
title: "Power analysis as a research-fraud / implausibility detector"
aliases:
  - "implausible p-value detection"
  - "forensic power analysis"
tags: [research-integrity, power-analysis, statistics, metascience, rna-seq]
maturity: emerging
key_papers:
  - depower-approximate-power-analysis-deseq2
first_introduced: "Gorin, Guruge & Goodman 2026 (DEPower)"
date_updated: 2026-06-03
related_concepts: [analytical-power-analysis-deseq2-model]
---

## Definition

The retrospective use of analytical power-analysis mathematics to check whether a published result (a reported p-value at a given effect size and sample size) is mathematically plausible under the DESeq2 model — and thus to flag possible analysis errors or misconduct.

## Intuition

The same equations that say "you need n samples to reach this p-value" can be run backwards: given the reported n, effect size, and expression, is the claimed p-value even achievable? An extreme claim such as \(p=10^{-200}\) at \(\log_2\mathrm{FC}=1\) with \(n=3\) is suspicious if the model cannot produce it.

## Formal notation

Invert the significance condition (see [[analytical-power-analysis-deseq2-model]]) and test whether the reported \((n,\mathrm{LFC},\bar\mu,p)\) tuple is feasible within the dispersion band.

## Variants

- Complements numeric-consistency forensics (GRIM/GRIMMER), image-duplication detection, and "tortured phrases"/LLM-text detection.

## Comparison

- Less scalable and more manual than other fraud-detection signals; inconsistencies are suggestive, not conclusive.

## When to use

- Diligence checks on high-stakes claims that rest on very few samples and report implausibly extreme statistics.

## Known limitations

- High-expression / low-dispersion genes can legitimately reach arbitrarily low p-values, so a single inconsistency is not proof.
- Misuse of the statistical tool is hard to distinguish from intentional fabrication; fraud at scale more often uses large public datasets (e.g. TCGA) where these constraints don't bite.
- Falsifying test statistics is laborious, so fabricators more often manipulate the underlying data instead.

## Open problems

- Automating plausibility screening at scale with acceptable false-positive rates.

## Key papers

- [[papers/depower-approximate-power-analysis-deseq2]] — proposes the idea as an "aside" and frankly enumerates why it is unlikely to scale.

## My understanding

An interesting side-use, but the authors themselves temper expectations — it's a niche diligence tool, not a fraud-detection panacea.
