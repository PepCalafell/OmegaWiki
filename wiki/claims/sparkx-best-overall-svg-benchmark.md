---
title: "SPARK-X is the best-performing SVG detection method overall in a 14-method, 96-dataset benchmark"
slug: sparkx-best-overall-svg-benchmark
status: supported
confidence: 0.85
tags:
  - spatial-transcriptomics
  - benchmarking
  - SVG
domain: spatial-transcriptomics-methods
source_papers:
  - systematic-benchmarking-computational-methods-identify-spatially
evidence:
  - source: "[[papers/systematic-benchmarking-computational-methods-identify-spatially]]"
    type: supports
    strength: strong
    detail: "Average rank 4.3 across 6 metrics (ranking accuracy, calibration, memory, runtime, RNA-seq clustering, ATAC-seq clustering). Best ranking accuracy on 6/9 ST profiling technologies, average Kendall correlation 0.88; well-calibrated p-values; 2nd-best scalability beyond 20k spots."
conditions: "Holds on the scDesign3-simulated benchmark using 50 reference datasets across 9 ST technologies plus DLPFC/OSCC/HER2 real-tissue evaluations. Performance gap to SpaGFT (rank 5.4) and Moran's I is moderate; SPARK-X does NOT dominate every individual metric (Moran's I beats it on spatial-domain detection)."
date_proposed: 2026-05-21
date_updated: 2026-05-21
---

## Statement

In a systematic benchmark of 14 SVG-detection methods across 96 spatial datasets and 6 evaluation metrics, SPARK-X achieves the best overall performance (average rank 4.3), driven primarily by its high gene-ranking accuracy across 9 spatial transcriptomics technologies and its well-calibrated p-values.

## Evidence summary

Quote (p.13): "SPARK-X as the top-performing method, with an average ranking of 4.3. It demonstrated the best performance in correctly ranking genes based on estimated spatial variation for six out of nine ST profiling techniques."

Performance components:
- Kendall ranking correlation: 0.88 (best of 14)
- Calibration K-S: among best (top 2 with SPARK)
- Scalability: 2nd best on memory and time among GP-based methods
- ATAC-seq clustering CHAOS: middle-of-pack (SpatialDE2 best)

## Conditions and scope

The "best overall" claim is robust on the benchmark's six aggregated metrics but is sensitive to metric weighting. For the specific task of spatial-domain detection, Moran's I outperforms SPARK-X (mean rank 6.5 vs SPARK-X's higher rank).

## Counter-evidence

- Moran's I, despite simplicity, wins spatial-domain detection.
- SOMDE beats SPARK-X on memory/runtime.
- SpatialDE2 is the only method that beats the all-peaks baseline on spatial ATAC-seq.

## Linked ideas

(none yet)

## Open questions

- Does SPARK-X's lead hold under benchmarks that re-weight metrics by user-facing importance (e.g. user surveys)?
- Does it hold on emerging ST technologies (Slide-Tags, Visium HD, Stereo-seq large-area) not yet represented in the benchmark's 50 reference datasets?
