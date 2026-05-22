---
title: "scVI/scANVI runtime is independent of dataset size; trVAE, scGen, Seurat v3 and MNN fail at 100k+ cells under CPU limits"
slug: scvi-scales-trvae-scgen-fail
status: supported
confidence: 0.9
tags:
  - scalability
  - data-integration
  - scRNA-seq
  - deep-learning
domain: single-cell-methods
source_papers:
  - benchmarking-atlas-level-data-integration-single
evidence:
  - source: "[[papers/benchmarking-atlas-level-data-integration-single]]"
    type: supports
    strength: strong
    detail: "scVI/scANVI: runtime independent of dataset size via training-epoch-scaling heuristic. trVAE: fails above ~34k cells without GPU. Seurat v3, MNN, scGen: fail above ~100k cells under CPU runtime caps. Tested on the 1M-cell mouse-brain task; only a subset of methods completed within the 4-day CPU budget."
conditions: "Scalability is benchmarked under fixed runtime/memory budgets (4 days CPU); GPU availability changes the picture for trVAE and scGen. Holds under the scIB Snakemake pipeline default budgets."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

scVI and scANVI achieve dataset-size-independent runtime by scaling training epochs inversely with cell count. In contrast, trVAE fails to integrate datasets above ~34k cells without GPU, and Seurat v3, MNN and scGen fail above ~100k cells within the scIB CPU budget (4 days). On the 1M-cell mouse-brain task, only a subset of methods complete successfully.

## Evidence summary

Quote (p.46): "The runtime of scVI and scANVI did not increase with the dataset size due to a heuristic that was suggested to scale training epochs with the number of data points. Given runtime and memory limitations imposed in our benchmark, trVAE could not integrate datasets with >34,000 cells, while Seurat v3, MNN and scGen failed to integrate datasets with >100,000 cells (Supplementary Data 3)."

## Conditions and scope

- Under the 4-day CPU runtime cap defined by the scIB Snakemake pipeline.
- GPU availability changes the picture — trVAE and scGen are optimized for GPU.
- For atlas-scale (>100k cells), prefer scVI / scANVI / Scanorama / Harmony / BBKNN.

## Counter-evidence

- (none — these are direct benchmark observations)

## Linked ideas

(none yet)

## Open questions

- Does the scVI scaling heuristic hold on very-large atlases (10M+ cells)?
- Have Seurat v5 / SeuratIntegration changed Seurat's scaling profile?
