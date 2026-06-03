---
title: "The DESeq2 mean-dispersion curve can be approximated by a data-free order-of-magnitude band"
slug: deseq2-mean-dispersion-curve-approximated-heuristic
status: weakly_supported
confidence: 0.6
tags: [dispersion, deseq2, power-analysis, heuristic, statistics]
domain: "statistics / methods"
source_papers:
  - depower-approximate-power-analysis-deseq2
evidence:
  - source: depower-approximate-power-analysis-deseq2
    type: supports
    strength: moderate
    detail: "Eq. 3 with typical ã0=10^-3/2, ã1=10^1/2 and ±10^1/2 optimistic/pessimistic bounds; agrees with the PyDESeq2 trend but individual genes fall outside the band (Fig 1b)."
conditions: "No pilot data available; dispersion parameters assumed in typical ranges a1∈[1,10], a0∈[10^-2,10^-1]."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

When no pilot data exist, the DESeq2 dispersion curve \(d(\bar\mu)=a_0+a_1/\bar\mu\) can be approximated by a logarithmic-midpoint "typical" curve (\(\tilde a_0=10^{-3/2}\), \(\tilde a_1=10^{1/2}\)) with optimistic and pessimistic bounds scaled by \(10^{\mp 1/2}\), bracketing plausible dispersion within an order of magnitude.

## Evidence summary

Heuristic justified by the typical empirical ranges of \(a_0,a_1\); Figure 1b shows the band tracks the PyDESeq2-inferred trend, though individual genes can lie outside it.

## Conditions and scope

A fallback for de novo design; explicitly the dominant approximation error in the method.

## Counter-evidence

Individual genes' dispersions fall outside the band; the ad hoc estimate is the largest source of p-value deviation from the full procedure (see [[claims/heuristic-deseq2-power-analysis-values-concordant]]).

## Linked ideas

- [[concepts/heuristic-dispersion-band-mean-expression]]

## Open questions

- Can priors from related public datasets tighten the band materially?
