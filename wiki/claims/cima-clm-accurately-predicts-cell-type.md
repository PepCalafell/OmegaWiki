---
title: "CIMA-CLM accurately predicts cell type–specific chromatin accessibility"
slug: cima-clm-accurately-predicts-cell-type
status: supported
confidence: 0.8
tags: [immune-genomics, xqtl, single-cell, methodological]
domain: immunology
source_papers:
  - chinese-immune-multi-omics-atlas
evidence:
  - source: chinese-immune-multi-omics-atlas
    type: supports
    strength: strong
    detail: "Median PCC 0.7661–0.9612 (overall mean 0.8951); AUROC 0.9058–0.9927 (mean 0.9560) across 32 held-out cell types (p.11-12)."
conditions: "32 cell types with adequate accessibility signal; accuracy declines at low capture depth."
date_proposed: 2026-06-04
date_updated: 2026-06-04
---

## Statement

The CIMA-CLM cell language model predicts cell type–specific chromatin accessibility with high concordance to experimental scATAC-seq across dozens of immune cell types.

## Evidence summary

- [[papers/chinese-immune-multi-omics-atlas]] (methodological): Median PCC 0.7661–0.9612 (overall mean 0.8951); AUROC 0.9058–0.9927 (mean 0.9560) across 32 held-out cell types (p.11-12).

## Conditions and scope

32 cell types with adequate accessibility signal; accuracy declines at low capture depth.

## Counter-evidence

None recorded at ingest.

## Linked ideas

_None yet._

## Open questions

- Related concepts/entities: [[concepts/cima-clm-chromatin-accessibility-cell-language]] [[foundations/hyenadna-genomic-sequence-model]] [[foundations/scgpt-single-cell-foundation-model]]
