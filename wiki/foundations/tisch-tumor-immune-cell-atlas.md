---
title: "TISCH — Tumor Immune Single-cell Hub"
slug: tisch-tumor-immune-cell-atlas
domain: methods
status: mainstream
aliases:
  - TISCH
  - TISCH2
  - Tumor Immune Single-cell Hub
  - TISCH atlas
  - TISCH database
  - TISCH curated scRNA-seq resource
  - TISCH tumour immune atlas
first_introduced: "Sun et al. 2021 (TISCH); 2023 (TISCH2)"
date_updated: 2026-05-26
source_url: "http://tisch.comp-genomics.org/"
---

## Definition

TISCH (Tumor Immune Single-cell Hub) and its update TISCH2 are curated scRNA-seq databases focused on the tumor microenvironment (TME). They provide uniformly processed and annotated scRNA-seq datasets across cancer types, with emphasis on immune cell types.

## Intuition

Pre-3CA, TISCH was the leading TME-centric pan-cancer scRNA-seq resource. It standardises annotations across studies and exposes them via a web interface, complementing TME-focused analyses. 3CA imports TISCH2 cell-type labels for 9 of its 124 datasets.

## Key features

- Standardised cell-type annotations across published cancer scRNA-seq studies.
- Web-based query for gene expression by cell type and dataset.
- TME-immune-cell-focused (in contrast to 3CA's malignant-cell focus).

## Known limitations

- TME-centric — malignant cells are typically under-annotated.
- Smaller than 3CA v2 in scope.
- Annotation merges across studies can mask study-specific cell-state heterogeneity.

## Open problems

- Reconciling TISCH and 3CA annotations for cross-resource analyses.
- Coverage of rare TME populations.

## Relevance to active research

Frequently cited as the TME-cell counterpart to 3CA. In 3CA v2 ([[curated-cancer-cell-atlas-provides-comprehensive]]), TISCH2 supplied annotations for 9 component datasets.
