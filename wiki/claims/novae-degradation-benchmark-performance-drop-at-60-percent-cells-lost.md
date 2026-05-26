---
title: "Novae's performance drops sharply at ~60% slide degradation (cell + gene-expression loss)"
slug: novae-degradation-benchmark-performance-drop-at-60-percent-cells-lost
status: supported
confidence: 0.7
tags:
  - spatial-transcriptomics
  - robustness
  - quantitative
  - methodological
domain: methods
source_papers:
  - novae-graph-based-foundation-model-spatial
evidence:
  - source: novae-graph-based-foundation-model-spatial
    type: supports
    strength: medium
    detail: "Supplementary Fig. 17: performance drop when approximately 60% of cells and gene expression are lost in a slide degradation benchmark."
conditions: "Synthetic degradation benchmark; cell + gene-expression loss."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

In a slide-degradation robustness benchmark, Novae preserves performance under mild degradation but performance drops noticeably once ~60% of cells and gene expression are lost.

## Evidence summary

Supplementary Fig. 17.

## Conditions and scope

Synthetic degradation; combines cell loss and gene-expression loss as a coupled perturbation.

## Counter-evidence

Discussed as a limitation in the Discussion section — generalisation to densely packed tissues (e.g., brain cortex) with poor segmentation quality remains untested.

## Linked ideas

— none yet.

## Open questions

- Decoupling cell loss vs gene-expression loss.
- Performance under realistic biological dropout patterns.
