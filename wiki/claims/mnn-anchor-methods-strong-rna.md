---
title: "MNN-anchor-based integration methods (Scanorama, FastMNN) are consistently strong on complex scRNA-seq integration tasks"
slug: mnn-anchor-methods-strong-rna
status: supported
confidence: 0.8
tags:
  - data-integration
  - scRNA-seq
  - MNN
  - Scanorama
  - FastMNN
domain: single-cell-methods
source_papers:
  - benchmarking-atlas-level-data-integration-single
evidence:
  - source: "[[papers/benchmarking-atlas-level-data-integration-single]]"
    type: supports
    strength: strong
    detail: "Both Scanorama and FastMNN, which build on mutual nearest neighbors as the alignment primitive, rank in the top tier on complex RNA tasks. Authors attribute this to local-anchor matching not requiring a global batch geometry assumption."
conditions: "Embedding outputs outperform gene-corrected outputs for these methods (see [[claims/embedding-outputs-outperform-gene-corrected]]). MNN advantage is RNA-specific; on scATAC-seq, MNN/FastMNN/Scanorama underperform LIGER/Harmony (PCA/SVD covariance fails on binary chromatin signal)."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

Integration methods built on mutual nearest neighbors (MNN) — Scanorama and FastMNN — consistently rank among top performers on complex scRNA-seq integration tasks. The MNN-anchor approach is hypothesized to generalize well because it matches cells locally rather than assuming a global batch geometry.

## Evidence summary

Quote (p.45): "methods based on mutual nearest neighbors to find anchors between batches (for example, Scanorama and FastMNN) tended to perform well."

## Conditions and scope

- Holds for RNA tasks. For scATAC-seq, MNN-based methods underperform because PCA/SVD covariance assumptions fail on binary chromatin data.
- Embedding outputs of these methods are stronger than their gene-corrected counterparts.

## Counter-evidence

- MNN itself (the original gene-output method) scales poorly to large datasets — only FastMNN and Scanorama variants achieve the top tier.

## Linked ideas

(none yet)

## Open questions

- Can MNN-anchor matching be combined with nonlinear scATAC-seq dimensionality reduction (SCALE) to bring MNN advantages to chromatin data?
