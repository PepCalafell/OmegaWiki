---
title: "H3K27ac captures CKI functional similarity at higher resolution than RNA-seq"
slug: h3k27ac-captures-cki-functional-similarity-higher
status: supported
confidence: 0.75
tags:
  - methodological
  - H3K27ac
  - RNA-seq
  - resolution
domain: methods / epigenomics
source_papers:
  - integrative-epigenome-based-strategy-unbiased-functional
evidence:
  - source: integrative-epigenome-based-strategy-unbiased-functional
    type: supports
    strength: moderate
    detail: "Head-to-head at 2 h LPS: H3K27ac-based CKI proximity captured higher pairwise Jaccard overlaps and gave sharper quintile separation between close and distant CKI pairs than RNA-seq-based proximity (two-way ANOVA quintile/model/interaction effects significant)."
conditions: "2 h LPS timepoint; same analytical framework for both modalities."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Distances between kinase inhibitors computed from H3K27ac changes separate closely- from distantly-related compounds more sharply than distances computed from RNA-seq, indicating higher-resolution functional discrimination by the epigenomic readout.

## Evidence summary

A direct 2 h-LPS comparison of H3K27ac-based vs RNA-seq-based CKI proximity models showed the H3K27ac model captured higher Jaccard overlaps and achieved more pronounced quintile separation. Supports [[concepts/h3k27ac-functional-readout-signaling-perturbation]].

## Conditions and scope

Single (2 h LPS) timepoint; mouse BMDM; the 58-CKI panel.

## Counter-evidence

RNA-seq still captured the overall correlative and anti-correlative spectrum of CKI effects; the advantage is in resolution, not in capturing fundamentally different biology.

## Linked ideas

## Open questions

- Does the resolution advantage hold across timepoints, stimuli, and cell types?
