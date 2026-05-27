---
title: "NiCo's three-module pipeline (annotations, interactions, covariations) integrates imaging-based single-cell-resolution spatial transcriptomics with matched scRNA-seq references to infer extrinsic drivers of cell state"
slug: nico-three-module-pipeline-spatial-scrna
status: supported
confidence: 0.9
tags: [methods,spatial-transcriptomics,scRNA-seq-integration,niche-analysis]
domain: spatial transcriptomics / methods
source_papers:
  - nico-identifies-extrinsic-drivers-cell-state
evidence:
  - source: nico-identifies-extrinsic-drivers-cell-state
    type: supports
    strength: moderate
    detail: "NiCo runs (1) soft-MNN-based cell-type annotation, (2) regularized logistic regression for niche prediction, and (3) iNMF/NMF + ridge regression for cell-state covariation, jointly leveraging spatial and scRNA-seq modalities (Fig. 1)."
conditions: "Mouse embryo seqFISH; small-intestine MERFISH; liver MERSCOPE; cerebellum Slide-seqV2."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

NiCo's three-module pipeline (annotations, interactions, covariations) integrates imaging-based single-cell-resolution spatial transcriptomics with matched scRNA-seq references to infer extrinsic drivers of cell state.

## Evidence summary

[[papers/nico-identifies-extrinsic-drivers-cell-state]] — NiCo runs (1) soft-MNN-based cell-type annotation, (2) regularized logistic regression for niche prediction, and (3) iNMF/NMF + ridge regression for cell-state covariation, jointly leveraging spatial and scRNA-seq modalities (Fig. 1).

## Conditions and scope

Mouse embryo seqFISH; small-intestine MERFISH; liver MERSCOPE; cerebellum Slide-seqV2.

## Counter-evidence

None within paper.

## Linked ideas

## Open questions

- Independent replication outside the Grün lab.
