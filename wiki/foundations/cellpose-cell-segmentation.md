---
title: "Cellpose — deep-learning cell segmentation"
slug: cellpose-cell-segmentation
domain: "image analysis / spatial transcriptomics"
status: mainstream
aliases:
  - "Cellpose"
  - "cellpose"
  - "Cellpose v1"
  - "Cellpose v2"
first_introduced: "Stringer et al. 2021 (Nat Methods)"
date_updated: 2026-05-26
source_url: "https://www.cellpose.org/"
---

## Definition

A generalist deep-learning model for cell segmentation in microscopy images (brightfield, fluorescence, MERFISH, IF). Produces 2D or 3D segmentation masks for cells and nuclei without requiring per-dataset retraining; widely adopted in spatial transcriptomics workflows for cell-level transcript assignment.

## Intuition

Cellpose treats segmentation as a flow-field prediction problem: each pixel votes toward a cell centre, and watershed-like grouping recovers cell masks. Pretrained on diverse data, it generalises to many staining patterns without retraining.

## Key variants

- Cellpose v1.0 (original generalist)
- Cellpose v2.0 (user-finetuning interface)
- Cellpose-SAM and Cellpose3 (later releases)

## Known limitations

- Densely packed cells with low cytoplasmic contrast are challenging.
- 3D segmentation is slower and noisier than 2D.
- Peripheral transcript misassignment in MERFISH workflows (mitigated by mask shrinkage).

## Open problems

- Segmentation-uncertainty propagation into downstream transcript-count analyses.
- Integration with non-uniform z-stacks (e.g. tilted MERSCOPE imaging).
