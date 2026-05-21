---
title: "SOMDE has the best memory and runtime scalability among SVG-detection methods up to 40,000 spots"
slug: somde-best-scalability-svg
status: supported
confidence: 0.85
tags:
  - spatial-transcriptomics
  - scalability
  - benchmarking
  - SVG
domain: spatial-transcriptomics-methods
source_papers:
  - systematic-benchmarking-computational-methods-identify-spatially
evidence:
  - source: "[[papers/systematic-benchmarking-computational-methods-identify-spatially]]"
    type: supports
    strength: strong
    detail: "Ten simulation datasets with fixed 100 genes and spot count from 100 to 40,000. SOMDE shows the lowest memory usage and the fastest runtime across all dataset sizes. SPARK-X 2nd best. SPARK requires ~250 GB at 20k spots; SpatialDE ~150 GB at 40k spots. BOOST-GP takes 3 days at 15k spots and fails at 20k and 40k within 5 days. GPcounts requires ~40 hours at 40k even on GPU."
conditions: "Holds on the synthetic 100-gene scaling benchmark across 100–40k spots; not directly measured on real high-spot-count datasets (e.g. Visium HD, Stereo-seq full-section). Scaling regime may shift at much larger spot counts."
date_proposed: 2026-05-21
date_updated: 2026-05-21
---

## Statement

In a scaling benchmark of 10 datasets with 100 genes and 100–40,000 spots, SOMDE has the lowest peak memory and the fastest runtime of all 14 SVG-detection methods evaluated; SPARK-X is a close second. SPARK, SpatialDE, BOOST-GP, and GPcounts scale poorly.

## Evidence summary

Quote (p.10): "SOMDE exhibited the most efficient memory usage across all benchmarking datasets, followed by Spanve and SPARK-X… SOMDE again achieved the best scalability, closely followed by SPARK-X and scGCO… SOMDE and SPARK-X exhibited the most favorable scalability when handling datasets with increasing spots."

SOMDE achieves this via SOM-based spatial aggregation that collapses N spots into K ≪ N nodes before the Gaussian-process fit, side-stepping the cubic scaling of standard GP regression. SPARK-X achieves competitive efficiency via direct covariance-matrix comparison rather than GP regression.

## Conditions and scope

Holds on the 100-gene scaling sweep. For datasets where SOMDE fails numerically (Stereo-seq in this benchmark) the claim does not apply. The benchmark caps at 40k spots; full-section Visium HD (~millions of spots) is unexplored.

## Counter-evidence

SOMDE fails to complete on Stereo-seq inputs (numerical-stability error) and underperforms HVGs for spatial-domain detection — efficiency is not the only criterion.

## Linked ideas

(none yet)

## Open questions

- Does SOMDE's SOM aggregation scale gracefully to millions of subcellular spots (Visium HD, large-area MERFISH)?
- Can SPARK-X's direct-covariance approach be GPU-accelerated to surpass SOMDE on real datasets with high gene counts?
