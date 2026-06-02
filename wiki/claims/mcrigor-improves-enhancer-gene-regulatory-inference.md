---
title: "Removing dubious metacells improves enhancer-gene regulatory inference on multiome data"
slug: mcrigor-improves-enhancer-gene-regulatory-inference
status: supported
confidence: 0.8
tags: [single-cell, metacell, mcRigor, multiome, enhancer-gene, ATAC]
domain: single-cell-methods
source_papers:
  - mcrigor-statistical-method-enhance-rigor-metacell
evidence:
  - source: mcrigor-statistical-method-enhance-rigor-metacell
    type: supports
    strength: moderate
    detail: "On the SEACells HSPC multiome dataset (85 metacells, 7 dubious), removing dubious metacells increased gene-peak association scores: TAL1 0.8266→0.8703, GATA2 0.6904→0.7606; recovered a literature-validated GATA2 enhancer (chr3-128532902-128533402) and filtered out a poorly-supported peak."
conditions: "6881 CD34+ HSPCs, healthy bone marrow, scMultiome; gene-peak links via Signac LinkPeaks; validated against single-cell-level correlation and prior reports."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

Filtering dubious metacells with mcRigor strengthens reliable gene-peak associations and removes spurious ones, improving enhancer-gene regulatory inference from single-cell multiome data.

## Evidence summary

On the SEACells HSPC multiome dataset, mcRigor flagged 7/85 metacells as dubious. Consistently-identified gene-peak pairs had higher association scores after removal (TAL1: 0.8266→0.8703; GATA2: 0.6904→0.7606). Using trustworthy metacells recovered a literature-supported GATA2 enhancer (chr3-128532902-128533402, overlapping LOC117038772) and dropped a peak (chr3-128409363-128409863) with minimal single-cell correlation and extremely low accessibility.

## Conditions and scope

6881 CD34+ HSPCs from healthy bone marrow; peaks linked via Signac LinkPeaks (adjusted p < 0.05); corroborated at single-cell level and by prior literature.

## Counter-evidence

None reported.

## Linked ideas

(none yet)

## Open questions

Joint multi-modality optimization of metacells for regulatory inference.
