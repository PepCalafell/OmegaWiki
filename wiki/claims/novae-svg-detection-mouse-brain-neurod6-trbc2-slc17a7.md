---
title: "Novae spatial-domain grouping identifies Neurod6, Slc17a7, and Trbc2 as top spatially variable genes in 2.5-month control mouse brain"
slug: novae-svg-detection-mouse-brain-neurod6-trbc2-slc17a7
status: supported
confidence: 0.7
tags:
  - spatial-transcriptomics
  - mouse-brain
  - SVG
  - methodological
  - quantitative
domain: methods
source_papers:
  - novae-graph-based-foundation-model-spatial
evidence:
  - source: novae-graph-based-foundation-model-spatial
    type: supports
    strength: medium
    detail: "Fig. 6g shows the three top spatially variable genes identified by differential expression analysis grouped on Novae domains for the 2.5-month control mouse brain: Trbc2, Slc17a7, Neurod6. log1p-normalised count maps."
conditions: "Single 2.5-month control mouse brain; SVG detection via grouped DEG on Novae domains."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Differential gene expression grouped by Novae spatial domains identifies Neurod6, Slc17a7, and Trbc2 as the three top spatially variable genes in the 2.5-month control mouse brain, demonstrating Novae's compatibility with downstream SVG analysis.

## Evidence summary

Fig. 6g: spatial maps of log1p-normalised expression for the three SVGs.

## Conditions and scope

Single 2.5-month control mouse brain; SVG detection via Novae-domain grouping.

## Counter-evidence

No formal benchmarking of this SVG list against alternative SVG detectors (Moran's I, MERINGUE, SPARK).

## Linked ideas

— none yet.

## Open questions

- How Novae-grouped SVGs compare against dedicated SVG detection methods on calibrated benchmarks.
