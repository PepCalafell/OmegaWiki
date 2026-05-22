---
title: "scATAC-seq feature-space tradeoff: peaks vs windows vs gene activity"
aliases:
  - scATAC feature space
  - scATAC peaks vs windows
  - gene activity score
  - chromatin accessibility feature space
  - scATAC-seq matrix representation
  - peaks feature space
  - windows feature space
  - gene-activity feature space
  - scATAC dimensionality reduction
  - chromatin feature selection
  - peak calling vs window binning
tags:
  - scATAC-seq
  - feature-space
  - data-integration
  - chromatin-accessibility
maturity: stable
key_papers:
  - "[[papers/benchmarking-atlas-level-data-integration-single]]"
first_introduced: "Luecken et al. 2022 (formalised in scIB benchmark)"
date_updated: 2026-05-22
related_concepts:
  - "[[concepts/batch-removal-vs-bioconservation-tradeoff]]"
---

## Definition

scATAC-seq data can be represented in three feature spaces — peaks (variable-width regions of accessible chromatin), windows (fixed-width genomic bins, typically 5kb), and gene activity (per-gene sum of fragments overlapping gene body and promoter). The choice of feature space governs integration outcomes more strongly than the choice of integration method. Peaks and windows preserve cell-type biological variation; gene activity homogenises cells across biology.

## Intuition

Gene activity scoring sums fragments over gene neighborhoods, which approximates per-gene expression and enables cross-modality alignment with scRNA-seq. But it discards the regulatory-element resolution that makes chromatin data biologically informative. Peaks and windows preserve the open-chromatin landscape itself, at the cost of much higher dimensionality (often >100,000 features).

## When to use

- Peaks / windows: for chromatin-native analysis (TF motif analysis, regulatory-element discovery, cell-type identification).
- Gene activity: for cross-modality (scRNA + scATAC) label transfer only.

## Known limitations

- Per scIB benchmark on mouse brain: mean bio-conservation 0.61 (peaks) / 0.59 (windows) / 0.39 (gene activity).
- Gene-activity scoring is heuristic; alternative scoring (ArchR, Cicero) may improve the picture but not close the gap entirely.
- Most scRNA-seq integration methods (PCA/SVD-based) fail in any scATAC feature space; only LIGER and Harmony work consistently.

## Open problems

- Can dedicated scATAC dimensionality reduction (SCALE, LSI) combined with MNN-anchor matching beat LIGER/Harmony?
- How should joint RNA + ATAC atlases reconcile the feature-space tradeoff?
