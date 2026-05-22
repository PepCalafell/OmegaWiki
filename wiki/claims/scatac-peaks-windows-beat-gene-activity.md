---
title: "scATAC-seq integration: peak and window feature spaces preserve more biology than gene-activity features"
slug: scatac-peaks-windows-beat-gene-activity
status: supported
confidence: 0.9
tags:
  - scATAC-seq
  - feature-space
  - data-integration
  - chromatin-accessibility
domain: single-cell-methods
source_papers:
  - benchmarking-atlas-level-data-integration-single
evidence:
  - source: "[[papers/benchmarking-atlas-level-data-integration-single]]"
    type: supports
    strength: strong
    detail: "Mean bio-conservation score across all integration methods on scATAC-seq mouse brain: gene activity 0.39, peaks 0.61, windows 0.59. Mean batch removal: gene activity 0.66, peaks 0.50, windows 0.47. Even unintegrated data in gene-activity space lacks the cell-identity structure visible in peaks or windows."
conditions: "Holds for mouse brain scATAC-seq across 3 datasets. The gene-activity → score is an aggregation choice; alternative scoring (ArchR, Cicero) may improve gene-activity performance."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

For scATAC-seq integration, the choice of feature space is more consequential than the choice of integration method. Peak and window feature spaces preserve substantially more cell-type biological variation than gene-activity features (mean bio-conservation 0.61 / 0.59 vs 0.39). Gene activity yields stronger batch removal (0.66 vs 0.50/0.47) but only because it has already discarded biological variation.

## Evidence summary

Quote (p.46): "the mean bio-conservation score for integration outputs on gene activity space is substantially lower than on peaks and windows (genes 0.39; peaks 0.61; windows 0.59); although removal of biological variance leads to stronger batch removal (mean batch removal score on genes 0.66; peaks 0.50; windows 0.47). Even unintegrated data in gene activity space lacked biological variation in cell identities compared to the same data on peaks or windows."

## Conditions and scope

- Tested on mouse brain scATAC-seq (3 datasets). No scATAC tissue diversity.
- Gene activity scored with the default heuristic (sum of fragments overlapping gene body + promoter); alternative scoring (Cicero co-accessibility, ArchR gene scores) may change conclusions.
- For users running scATAC integration: prefer peaks or windows; reserve gene activity for cross-modality RNA-ATAC label transfer only.

## Counter-evidence

- scANVI, scVI, scGen retain reasonable performance on gene-activity features — useful when cross-modality label transfer with scRNA-seq is required.

## Linked ideas

(none yet)

## Open questions

- Do ArchR or Cicero gene-activity scores narrow the gap?
- Does the conclusion generalize beyond mouse brain to immune-cell scATAC-seq?
