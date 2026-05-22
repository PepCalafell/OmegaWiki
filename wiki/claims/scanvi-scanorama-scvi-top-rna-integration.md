---
title: "scANVI, Scanorama and scVI are the top scRNA-seq integration methods on atlas-scale real data"
slug: scanvi-scanorama-scvi-top-rna-integration
status: supported
confidence: 0.9
tags:
  - data-integration
  - scRNA-seq
  - benchmarking
  - atlas
domain: single-cell-methods
source_papers:
  - benchmarking-atlas-level-data-integration-single
evidence:
  - source: "[[papers/benchmarking-atlas-level-data-integration-single]]"
    type: supports
    strength: strong
    detail: "Across 5 real scRNA-seq atlas tasks (pancreas, lung, human immune, human+mouse immune, mouse brain), the embedding outputs of scANVI, Scanorama and scVI rank in the top 3 most consistently. scGen ranks first most often but fails to scale to 1M cells in 4 days on CPU. Top performers conserve cell-type identity, trajectory structure and cell-cycle variation simultaneously."
conditions: "Holds under the 40/60 batch/bio-conservation weighting, tutorial-default hyperparameters, scIB metric suite, and atlas-complexity tasks (multiple donors / laboratories / protocols). For simpler integration tasks Harmony and Seurat v3 are competitive."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

On atlas-scale scRNA-seq integration (multi-donor, multi-laboratory, multi-protocol tasks of up to 1M cells), the embedding outputs of scANVI, Scanorama and scVI are the most consistent top-3 integration methods by aggregated batch-removal + bio-conservation score. scGen's gene-corrected output ranks first most often but is disqualified by failing to scale to the 1M-cell mouse-brain task within 4 days on CPU.

## Evidence summary

scIB benchmark of 16 methods × 4 preprocessing combinations × 5 scRNA-seq atlas tasks. Aggregated overall scores (40% batch removal, 60% bio-conservation; methods evaluated at their best preprocessing combination):
- scANVI* (embedding, HVG, unscaled) — top
- Scanorama (embedding, HVG, scaled) — top
- scVI (embedding, HVG, unscaled) — top
- scGen* (genes, HVG, unscaled) — ranked first most often but penalized on 1M-cell scalability

## Conditions and scope

- The benchmark uses tutorial-default hyperparameters; per-task tuning may shift the ranking.
- scANVI and scGen require cell-type labels — restrict their use to label-annotated atlases.
- For simple integration tasks (single tissue, few batches), linear methods (Harmony) remain competitive and faster.
- scATAC-seq integration follows a different ranking (LIGER, Harmony dominate) — see [[claims/liger-harmony-best-scatac-integration]].

## Counter-evidence

- Hyperparameter optimization not done; trVAE and DESC may improve substantially with tuning.
- The 40/60 weighting is editorial — alternative weightings give different ordering tails (Spearman > 0.96 across alternatives is reported but the tail still moves).

## Linked ideas

(none yet)

## Open questions

- Does the ranking transfer to multimodal (CITE-seq, RNA+ATAC) atlases?
- Does it transfer to reference-mapping / scArches-style projection workflows?
