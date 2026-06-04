---
title: "Mixscape — single-cell CRISPR perturbation analysis"
slug: mixscape-crispr-perturbation-analysis
domain: computational genomics
status: mainstream
aliases:
  - Mixscape
first_introduced: "Papalexi et al. 2021, Nature Genetics (Seurat)"
date_updated: 2026-06-04
source_url: "https://doi.org/10.1038/s41588-021-00778-2"
---

## Definition
Mixscape is a computational method (implemented in Seurat) for analyzing single-cell CRISPR (Perturb-seq/CROP-seq) data. It estimates and removes confounding cell-level variation, identifies cells in which a perturbation produced a detectable transcriptional effect (vs "escaping" cells indistinguishable from controls), and derives per-perturbation signatures suitable for downstream comparison.

## Intuition
Not every cell assigned a guide is truly perturbed; Mixscape separates genuinely affected cells from non-responders, sharpening perturbation signatures so that knockout effects can be compared and clustered reliably.

## Formal notation
Per cell, compute a perturbation score relative to non-targeting controls; classify cells as perturbed/escaping via a mixture model; LDA on perturbed cells yields a low-dimensional perturbation-signature space for visualization (UMAP) and similarity analysis.

## Key variants
LDA-transformed Mixscape signatures used as input to cross-prediction functional similarity graphs.

## Known limitations
Excludes perturbations that affect only a small number of genes (e.g. surface receptors Csf1r/CD115, Fcgr1/CD64 in the macrophage screen), so weak-effect knockouts may be dropped from analysis though present in raw data.

## Open problems
Sensitivity for subtle or highly time-dependent perturbation effects.

## Relevance to active research
Standard analysis layer for pooled single-cell CRISPR screens; used to quantify knockout effects in [[papers/integrated-time-series-analysis-high-content]].
