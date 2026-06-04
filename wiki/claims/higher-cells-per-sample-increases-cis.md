---
title: "Higher average cells per sample, not sample count, drives greater cis-eGene discovery"
slug: higher-cells-per-sample-increases-cis
status: supported
confidence: 0.7
tags: [immune-genomics, xqtl, single-cell, methodological]
domain: immunology
source_papers:
  - chinese-immune-multi-omics-atlas
evidence:
  - source: chinese-immune-multi-omics-atlas
    type: supports
    strength: moderate
    detail: "Correlation, linear-modeling, and downsampling analyses showed higher cells-per-sample in CIMA largely explains more cis-eGenes vs OneK1K (p.8)."
conditions: "Cross-dataset comparison of single-cell eQTL discovery power."
date_proposed: 2026-06-04
date_updated: 2026-06-04
---

## Statement

CIMA detected more cis-eGenes than OneK1K despite fewer individuals; modeling attributes the gain to the higher average number of cells captured per sample.

## Evidence summary

- [[papers/chinese-immune-multi-omics-atlas]] (methodological): Correlation, linear-modeling, and downsampling analyses showed higher cells-per-sample in CIMA largely explains more cis-eGenes vs OneK1K (p.8).

## Conditions and scope

Cross-dataset comparison of single-cell eQTL discovery power.

## Counter-evidence

None recorded at ingest.

## Linked ideas

_None yet._

## Open questions

- Related concepts/entities: [[foundations/tensorqtl]]
