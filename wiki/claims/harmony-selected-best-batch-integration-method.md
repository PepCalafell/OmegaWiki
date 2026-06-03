---
title: "Harmony was the best batch-integration method for the pan-cancer TME atlas by scIB benchmark"
slug: "harmony-selected-best-batch-integration-method"
status: supported
confidence: 0.8
tags: [integration,harmony,scib,methods,methodological]
domain: methods
source_papers:
  - pan-cancer-tumor-classification-holistic-tumor
evidence:
  - source: pan-cancer-tumor-classification-holistic-tumor
    type: supports
    strength: strong
    detail: "scIB benchmark of Harmony, scVI, Scanorama, BBKNN on a 20-dataset subset (~249k cells, 12/14 metrics) ranked Harmony highest."
conditions: "Benchmark subset and metric choice are atlas-specific; ranking may differ for other data regimes."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Using the scIB pipeline on a 20-dataset subset (~249k cells, 16 cancer types) with CellTypist labels, Harmony (with dataset+sample batch keys and tuned theta) outperformed scVI, Scanorama, and BBKNN across 12 scIB metrics and was chosen for atlas integration.

## Evidence summary

Benchmark on a low-cell subset; 12 of 14 scIB metrics used (HVG and trajectory conservation excluded). (p.3,13) Quote: "Harmony17 demonstrating superior performance and being selected for our study".

## Conditions and scope

Benchmark subset and metric choice are atlas-specific; ranking may differ for other data regimes.

## Counter-evidence

None recorded at ingest.

## Linked ideas

None yet.

## Open questions

Would Harmony remain optimal on the full atlas rather than the 20-dataset benchmark subset?
