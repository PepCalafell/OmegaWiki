---
title: "An integrated scRNA-seq reference of ~286k cells from 14 public studies anchors the MERFISH skin atlas annotation"
slug: integrated-scrnaseq-skin-reference-286k-cells
status: supported
confidence: 0.9
tags: [skin, scRNA-seq, integration, methodological]
domain: methods / single-cell
source_papers:
  - single-cell-spatial-transcriptomic-analysis-human
evidence:
  - source: single-cell-spatial-transcriptomic-analysis-human
    type: supports
    strength: strong
    detail: "Quote (Fig.1a): 'Public data scRNA-seq 286,000 cells (14 studies) 93 samples (85 donors)' — integrated reference used to derive 45 cell-type labels for MERFISH."
conditions: "Public scRNA-seq harmonised across 14 studies; used as label reference."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

A harmonised scRNA-seq reference of 286,000 cells from 14 public skin studies (93 samples, 85 donors) was built and used to derive cell-type labels and CellChat ligand-receptor priors for the MERFISH atlas.

## Evidence summary

Reported in [[papers/single-cell-spatial-transcriptomic-analysis-human]] Fig. 1a and Methods.

## Conditions and scope

Healthy adult skin; integrated using standard methods (Seurat / Harmony / scVI families).

## Counter-evidence

None.

## Linked ideas

## Open questions

- Which batch-integration choices most affect the 45-label resolution?
