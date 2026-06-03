---
title: "Heuristic dispersion band from mean expression"
aliases:
  - "order-of-magnitude dispersion estimate"
  - "ad hoc dispersion band"
tags: [dispersion, deseq2, rna-seq, power-analysis, statistics]
maturity: emerging
key_papers:
  - depower-approximate-power-analysis-deseq2
first_introduced: "Gorin, Guruge & Goodman 2026 (DEPower)"
date_updated: 2026-06-03
related_concepts: [analytical-power-analysis-deseq2-model]
---

## Definition

A data-free heuristic that places per-gene dispersion within an order-of-magnitude band as a function of mean normalized expression, used when no pilot data are available to estimate the DESeq2 mean-dispersion curve.

## Intuition

The DESeq2 dispersion curve \(d(\bar\mu)=a_0+a_1/\bar\mu\) has parameters that typically fall in narrow ranges (\(a_1\in[1,10]\), \(a_0\in[10^{-2},10^{-1}]\)). Taking the logarithmic midpoint gives a "typical" curve, and scaling it up/down by \(10^{1/2}\) gives pessimistic (high-dispersion) and optimistic (low-dispersion) bounds — a band that brackets plausible dispersion without any data.

## Formal notation

Typical: \(\tilde d(\bar\mu)=\tilde a_0 + \tilde a_1/\bar\mu\) with \(\tilde a_0=10^{-3/2}\), \(\tilde a_1=10^{1/2}\). Optimistic \(\tilde d_-=10^{-1/2}\tilde d\); pessimistic \(\tilde d_+=10^{1/2}\tilde d\). Default domain \([10^{-8}, \max(n,10)]\).

## Variants

- Replace the heuristic band with PyDESeq2-estimated dispersions when pilot data exist (much more accurate).

## Comparison

- Pilot-data dispersion estimation (scPower, Poplawski & Binder) is preferable when available; this heuristic is the fallback for de novo design.

## When to use

- Prospective power analysis before any data have been collected for the system of interest.

## Known limitations

- The ad hoc dispersion estimate is the dominant source of error in the resulting p-values; individual genes can fall outside the band.
- Using the true PyDESeq2 dispersion instead removes nearly all the deviation from the full procedure.

## Open problems

- Tightening the band using priors from related public datasets.

## Key papers

- [[papers/depower-approximate-power-analysis-deseq2]]

## My understanding

The honest part of the method: the authors are explicit that the dispersion band is the weak link and that pilot data should override it whenever possible.
