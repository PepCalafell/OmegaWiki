---
title: "LIGER — integrative non-negative matrix factorization for single-cell multi-omics"
slug: liger-nmf-integration
domain: "methods / single-cell-integration / multi-omics"
status: mainstream
aliases:
  - LIGER
  - liger integration
  - Welch LIGER
  - linked inference of genomic experimental relationships
  - integrative NMF single-cell
  - rliger
  - liger scATAC integration
  - liger multi-omic
  - liger Macosko lab
  - integrative non-negative matrix factorization
first_introduced: "Welch et al. 2019 *Cell* (Single-cell multi-omic integration compares and contrasts features of brain cell identity)"
date_updated: 2026-05-22
source_url: "https://github.com/welch-lab/liger"
---

## Definition

LIGER integrates single-cell datasets using integrative non-negative matrix factorization, decomposing data into shared and dataset-specific metagene factors. The shared factors define the integrated embedding; dataset-specific factors quantify residual batch structure. LIGER explicitly supports cross-modality integration (RNA + ATAC) by aligning gene-activity-equivalent features.

## Strengths

- One of two methods (with Harmony) that consistently integrate scATAC-seq batches on peak/window features — see [[claims/liger-harmony-best-scatac-integration]].
- Cross-modality integration is native.
- Strong batch removal on tasks with strong batch effects.

## Known limitations

- Prioritizes batch removal over bio-conservation; sacrifices nuanced cell-state variation.
- Creates artificial substructure from single-batch signal on small ATAC tasks (over-correction artifact).
- Slow on large feature spaces.

## Relevance to active research

LIGER is the recommended choice for scATAC-seq batch integration and for RNA+ATAC cross-modality alignment when batch removal is the priority. Validated in [[papers/benchmarking-atlas-level-data-integration-single]].
