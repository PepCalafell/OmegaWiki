---
title: "Moran's I is a competitive SVG baseline despite algorithmic simplicity"
slug: morans-i-competitive-baseline-svg
status: supported
confidence: 0.8
tags:
  - spatial-transcriptomics
  - benchmarking
  - SVG
  - baseline
domain: spatial-transcriptomics-methods
source_papers:
  - "[[papers/systematic-benchmarking-computational-methods-identify-spatially]]"
evidence:
  - source: "[[papers/systematic-benchmarking-computational-methods-identify-spatially]]"
    type: supports
    strength: strong
    detail: "Moran's I (Squidpy implementation) achieves 4th-best Kendall correlation (0.76) for gene ranking across simulated datasets, 3rd-best overall average rank, and the BEST mean rank (6.5) for spatial domain detection across DLPFC/OSCC/HER2 datasets and three clustering algorithms (Leiden, BayesSpace, Banksy). Outperformed bespoke methods such as SPARK, SpaGCN, scGCO, GPcounts on spatial-domain detection."
conditions: "Holds under the scDesign3-simulated SVG benchmark and on three real-tissue spatial-domain datasets. Note miscalibrated p-values (over-liberal) — use rank-based selection. Implementation-dependent; Squidpy's Moran's I uses KNN-graph spatial weights."
date_proposed: 2026-05-21
date_updated: 2026-05-21
---

## Statement

Moran's I, a classical spatial autocorrelation statistic implemented in Squidpy, is a top-3 SVG-detection method overall and the best single method for downstream spatial-domain detection across DLPFC, OSCC, and HER2 datasets — despite being conceptually and computationally simpler than every GP-based and graph-based competitor.

## Evidence summary

Quote (p.14): "Surprisingly, Moran's I, a simple method based on autocorrelation between spots and their spatial neighbors, achieved the third-best performance. This method demonstrated a good gene ranking ability and competitive computational efficiency, notably outperforming other methods in spatial domain detection. The strong performance of this classic metric, which has been largely overlooked in recent benchmarking and methodology development efforts, suggests that it should be included as a baseline in future studies."

Quantitative results:
- Kendall correlation 0.76 (4th place among 14 methods)
- Spatial domain detection mean rank: 6.5 (best of all SVG methods)
- Overall average rank: 3rd best

## Conditions and scope

The claim is strongest for spatial-domain detection downstream tasks. Moran's I's p-values are miscalibrated (over-liberal), so users should rank by score rather than threshold by significance. The result is also Squidpy-implementation-specific; other Moran's I implementations may differ.

## Counter-evidence

Moran's I underperforms SPARK-X on raw ranking-accuracy benchmarks and on calibration. It also performs poorly on the "pattern 1" small-concentrated-spot expression class.

## Linked ideas

(none yet)

## Open questions

- Why has Moran's I been so widely ignored in recent SVG-methodology papers (only one prior benchmark included it)?
- Is its advantage on spatial-domain detection an artifact of the KNN-graph spatial weighting matching the downstream clustering's neighbourhood structure?
