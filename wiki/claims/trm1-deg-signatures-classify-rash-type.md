---
title: "Trm1 DEG signatures classify rash type in an external validation dataset"
slug: trm1-deg-signatures-classify-rash-type
status: supported
confidence: 0.8
tags: [skin, trm, classification, validation, scrna-seq, methods]
domain: immunology / single-cell
source_papers:
  - classification-human-chronic-inflammatory-skin-disease
evidence:
  - source: classification-human-chronic-inflammatory-skin-disease
    type: supports
    strength: moderate
    detail: "Quote (p.6): 'our disease-specific DEGs accurately identified the two rash types in the Reynolds et al. dataset.' Tested on 3 PV and 4 AD external samples via gene-set scores and hyperdimensionality mapping."
conditions: "External cohort (Reynolds et al.); Trm1 AD/PV gene-set module scores."
date_proposed: 2026-06-10
date_updated: 2026-06-10
---

## Statement

The AD- and PV-specific Trm1 DEG signatures, applied to a transcriptionally analogous Trm population in an independent external dataset (Reynolds et al.; 3 PV, 4 AD), correctly identified the rash type of each sample by both gene-set scoring and hyperdimensionality mapping — demonstrating patient-level classification from Trm1 molecular data alone.

## Evidence summary

Reported in Results of [[papers/classification-human-chronic-inflammatory-skin-disease]] using [[foundations/addmodulescore-seurat]]. Supports [[concepts/trm1-th2-th17-molecular-classification-inflammatory]] and [[concepts/rashx-rash-classification-web-portal]].

## Conditions and scope

Small external validation set (7 samples); classification used signatures derived in-study.

## Counter-evidence

Limited external cohort size; broader validation pending.

## Linked ideas

## Open questions

- Does accuracy hold across platforms, batches, and a wider diagnostic spectrum?
