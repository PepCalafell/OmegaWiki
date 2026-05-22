---
title: "CellCharter's analytical cluster neighbourhood enrichment is more scalable than permutation-based tests"
slug: analytical-cluster-neighborhood-enrichment-scales-beyond
status: supported
confidence: 0.75
tags:
  - spatial-statistics
  - methodological
  - cluster-NE
  - scalability
domain: methods
source_papers:
  - cellcharter-reveals-spatial-cell-niches-associated
evidence:
  - source: cellcharter-reveals-spatial-cell-niches-associated
    type: supports
    strength: moderate
    detail: "Methods + Discussion (p.75): \"CellCharter introduces an analytical approach to compute symmetric and asymmetric cluster NE, which is more efficient than currently available permutation-based methods (ref. 46 = Squidpy / Palla 2022).\" Used to compute differential NE at the 416-LUAD-core IMC scale."
conditions: "Analytical NE inherits null-model assumptions; permutation NE remains the distribution-free fallback."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

CellCharter implements an analytical (non-permutation) statistic for symmetric and asymmetric cluster neighbourhood enrichment that is more computationally efficient than permutation-based alternatives (e.g., Squidpy), enabling differential-NE analyses on hundreds of samples.

## Open questions

- How does analytical-NE's false-positive rate compare to permutation NE on biologically realistic null clusterings?
