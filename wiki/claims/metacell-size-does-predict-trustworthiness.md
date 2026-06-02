---
title: "Metacell size does not predict trustworthiness"
slug: metacell-size-does-predict-trustworthiness
status: supported
confidence: 0.7
tags: [single-cell, metacell, mcRigor, heterogeneity]
domain: single-cell-methods
source_papers:
  - mcrigor-statistical-method-enhance-rigor-metacell
evidence:
  - source: mcrigor-statistical-method-enhance-rigor-metacell
    type: supports
    strength: moderate
    detail: "Metacells vary substantially in size at the same granularity level, but no clear relationship exists between metacell size and trustworthiness as determined by mcRigor; dubious metacells cannot be identified by size alone."
conditions: "Observed across datasets; metacell size distributions differ by cell type and condition (e.g. smaller metacells in COVID-19 PBMCs vs healthy; progenitors smaller than T cells in bmcite)."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

Contrary to the intuition that larger metacells are more likely heterogeneous, metacell size shows no clear relationship with trustworthiness, so dubious metacells cannot be reliably flagged by size.

## Evidence summary

At a fixed granularity level, metacells vary widely in size, yet mcRigor-determined trustworthiness is not predicted by size. Size distributions do, however, differ by cell type and biological condition — smaller metacells are more frequent in less stable states (e.g. COVID-19 PBMCs vs healthy; progenitor cells vs T cells in the bmcite dataset) — so size distributions can serve as a coarse sanity check on partition quality.

## Conditions and scope

A qualitative observation across the paper's datasets, motivating the need for the mcDiv statistic rather than size-based filtering.

## Counter-evidence

None reported.

## Linked ideas

(none yet)

## Open questions

Whether any composite size+composition feature could pre-screen dubious metacells faster than mcDiv.
