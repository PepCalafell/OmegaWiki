---
title: "DECODE deconvolves transcriptomic, proteomic and metabolomic data with one framework"
slug: decode-deconvolves-transcriptomic-proteomic-metabolomic-data
status: supported
confidence: 0.8
tags: [deconvolution, multiomics, methods]
domain: methods
source_papers:
  - decode-deep-learning-based-common-deconvolution
evidence:
  - source: decode-deep-learning-based-common-deconvolution
    type: supports
    strength: strong
    detail: "Single framework applied across three omics for both cell types and cell states, integrating multiomics tissue datasets at the cellular level."
conditions: "Requires a single-cell reference in the matching omics for each dataset; one model trained per dataset."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

A single DECODE framework estimates cell-type and cell-state abundances across transcriptomic, proteomic and metabolomic data, rather than requiring a modality-specific algorithm per omics.

## Evidence summary

The abstract and Results present one architecture applied unchanged to all three omics across 15 datasets and 7 scenarios, plus cell-state tasks and cross-omics cohort integration.

## Conditions and scope

Each dataset still needs its own trained model and a matching single-cell reference; "universal" refers to the framework form, not a single trained model.

## Counter-evidence

None within the paper; cross-omics universality is demonstrated empirically, not proven.

## Linked ideas

## Open questions

Extension to further omics layers (DNA methylation, spatial) is proposed but not shown.
