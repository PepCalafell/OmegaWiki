---
title: "CellTrek — single-cell to spatial coordinate mapping"
slug: "celltrek-single-cell-spatial-mapping"
domain: "methods / spatial transcriptomics"
status: mainstream
aliases:
  - CellTrek
first_introduced: "2022"
date_updated: 2026-06-05
source_url: ""
---

## Definition

CellTrek is a computational method that maps single cells from a scRNA-seq reference onto spatial transcriptomics coordinates, transferring single-cell identities to spatial spots so cell-type composition and spatial proximity can be inferred from Visium-style data.

## Intuition

Spatial platforms like Visium are multi-cell-per-spot; CellTrek borrows the high-resolution identities from a matched scRNA-seq atlas and "places" those cells in tissue space, recovering where each cell state sits relative to others.

## Formal notation

scRNA-seq reference + spatial query → co-embedding → spot-level cell-type charting and single-cell spatial coordinates.

## Key variants

- Used with default parameters in many tumour spatial studies; alternatives include CARD, Tangram, and cell2location.

## Known limitations

- Mapping fidelity depends on reference completeness and shared variable genes; sparse spatial spots reduce resolution.

## Open problems

- Benchmarking spatial charting accuracy against ground-truth imaging-based platforms.

## Relevance to active research

Used to show that Macro-CXCL9 localises in close proximity to Macro-SPP1 and Macro-FOLR2 within bladder tumour tissue, supporting spatially organised macrophage division of labour.
