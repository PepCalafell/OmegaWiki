---
title: "Label-free bio-conservation metrics for single-cell integration evaluation"
aliases:
  - label-free integration metrics
  - cell-cycle conservation metric
  - HVG conservation metric
  - trajectory conservation metric
  - bio-conservation beyond labels
  - annotation-independent integration evaluation
  - integration metrics beyond cell-type
  - scIB label-free metrics
  - integration evaluation without annotations
  - gene-program preservation metric
tags:
  - benchmarking
  - data-integration
  - metrics
  - scRNA-seq
maturity: stable
key_papers:
  - "[[papers/benchmarking-atlas-level-data-integration-single]]"
first_introduced: "Luecken et al. 2022 (introduced cell-cycle, HVG, trajectory conservation as scIB metrics)"
date_updated: 2026-05-22
related_concepts:
  - "[[concepts/batch-removal-vs-bioconservation-tradeoff]]"
  - "[[concepts/atlas-level-data-integration]]"
---

## Definition

Label-free bio-conservation metrics evaluate how well an integration method preserves biological variation *beyond* cell-type identity labels. The scIB benchmark introduces three such metrics: (i) cell-cycle variance conservation (PCA on cell-cycle gene programs pre- vs post-integration), (ii) HVG overlap conservation (set-overlap of pre-/post-integration HVGs), (iii) trajectory conservation (diffusion-map-based pseudotime correlation pre/post). These complement classical label-based metrics (ARI, NMI, ASW) that depend on annotation quality.

## Intuition

Cell-type labels capture discrete identity but miss continuous variation (developmental trajectories, cell-cycle phase, metabolic state, signaling-induced states). An integration method that perfectly recovers cell-type clusters may simultaneously collapse continuous trajectory structure into a clumpy embedding. Label-free metrics catch this failure mode.

## Formal notation

- Cell-cycle conservation: `1 - |PC_var_post - PC_var_pre| / PC_var_pre` for cell-cycle gene PCA variance.
- HVG conservation: `|HVG_pre ∩ HVG_post| / |HVG_pre|` for top-N HVGs per batch.
- Trajectory conservation: Spearman correlation between pre- and post-integration diffusion pseudotime along a predefined trajectory.

## When to use

Use label-free metrics whenever:
- Annotation quality is uncertain or coarse.
- Downstream analysis depends on continuous variation (pseudotime, gene programs).
- The integration target is gene-level (functional gene scoring, regulon analysis).

## Known limitations

- Trajectory conservation requires a predefined trajectory — circularity risk.
- Cell-cycle conservation is gene-set-dependent; results vary with cell-cycle gene-list choice.
- HVG conservation is sensitive to HVG-selection method.

## Open problems

- A label-free metric for rare-cell-state preservation independent of explicit annotations.
- Cross-modality label-free metrics (RNA + ATAC + protein).
