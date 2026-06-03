---
title: "Genome-wide multiple-testing correction sharply increases the required sample size"
slug: genome-wide-fdr-correction-sharply-increases
status: supported
confidence: 0.8
tags: [multiple-testing, fdr, bonferroni, power-analysis, sample-size, quantitative]
domain: "statistics / methods"
source_papers:
  - depower-approximate-power-analysis-deseq2
evidence:
  - source: depower-approximate-power-analysis-deseq2
    type: supports
    strength: moderate
    detail: "Same rare-cell scenario over ~10,000 genes: Bonferroni needs 28 samples (14/74); Benjamini–Hochberg with q=0.1 needs 22 (11/58), vs. 6 (3/14) nominal."
conditions: "~10,000 testable genes; BH approximated as p*=qp with q≈0.1."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Applying genome-wide false-discovery control to the rare-cell example raises the required sample size from ~6/condition (nominal) to 28 (14/74) under Bonferroni and 22 (11/58) under Benjamini–Hochberg with \(q=0.1\), across ~10,000 genes — i.e. dozens of samples even under optimistic assumptions.

## Evidence summary

Worked example extending the nominal calculation with Bonferroni (\(p^*=p/N\)) and an approximate BH (\(p^*=qp\)) correction.

## Conditions and scope

BH cannot be computed exactly a priori; it is approximated via an assumed non-null quantile \(q\). See [[foundations/benjamini-hochberg-fdr]].

## Counter-evidence

The required \(q\) is itself a guess; true requirements depend on the real p-value distribution.

## Linked ideas

- [[concepts/rare-cell-type-single-cell-enrichment]]
- [[claims/rare-cell-type-log2-fold-change]]

## Open questions

- How to choose \(q\) defensibly for prospective design.
