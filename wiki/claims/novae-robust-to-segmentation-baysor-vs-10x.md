---
title: "Novae spatial-domain assignments are robust to cell segmentation method (10x default vs Baysor)"
slug: novae-robust-to-segmentation-baysor-vs-10x
status: supported
confidence: 0.8
tags:
  - spatial-transcriptomics
  - robustness
  - segmentation
  - methodological
domain: methods
source_papers:
  - novae-graph-based-foundation-model-spatial
evidence:
  - source: novae-graph-based-foundation-model-spatial
    type: supports
    strength: medium
    detail: "Fig. 4e: Novae yields nearly identical spatial domains under default 10x Genomics staining-based segmentation vs Baysor transcript-based segmentation. Authors note other models can also pass this test."
conditions: "Imaging-based spatial transcriptomics; restricted to one tissue / two segmentation methods."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Novae's spatial-domain output is stable across two distinct cell segmentation algorithms (10x Genomics default staining-based and Baysor transcript-based), supporting that spatial-domain detection is less sensitive to segmentation than cell-level annotations.

## Evidence summary

Fig. 4e + adjacent text; supported also by Supplementary Fig. 13 for competing methods.

## Conditions and scope

Single tissue case study. Not a comprehensive segmentation-robustness benchmark.

## Counter-evidence

Authors caveat that good segmentation is still essential for cell-level tasks (cell typing, ligand-receptor analysis).

## Linked ideas

— none yet.

## Open questions

- Robustness to extreme segmentation failures (over/under-segmentation, dense tissues like brain cortex).
