---
title: "mcRigor-optimized metacell partition distinguishes biological from non-biological zeros, matching smRNA-FISH"
slug: mcrigor-distinguishes-biological-nonbiological-zeros-smfish
status: supported
confidence: 0.75
tags: [single-cell, metacell, mcRigor, dropout, smFISH, sparsity]
domain: single-cell-methods
source_papers:
  - mcrigor-statistical-method-enhance-rigor-metacell
evidence:
  - source: mcrigor-statistical-method-enhance-rigor-metacell
    type: supports
    strength: moderate
    detail: "On a Drop-seq melanoma dataset paired with smRNA-FISH for 16 genes (FISH zeros taken as gold-standard biological zeros), the γ selected by mcRigor for each method gave a zero proportion closely matching the smRNA-FISH zero proportion, and expression distributions approximating the FISH distributions."
conditions: "smRNA-FISH treated as gold standard for single-cell expression; 16 genes; melanoma cell line."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

By optimizing granularity, mcRigor balances removal of non-biological (technical) zeros against preservation of biological zeros, yielding metacell zero proportions that match the smRNA-FISH gold standard.

## Evidence summary

On a Drop-seq scRNA-seq dataset paired with smRNA-FISH for 16 genes from a melanoma cell line (FISH zeros assumed biological), the mcRigor-selected γ for MetaCell, SEACells, and SuperCell each produced a zero proportion closely matching the FISH zero proportion, and per-gene expression distributions approximating those of FISH — unlike raw single-cell data.

## Conditions and scope

Relies on smRNA-FISH as the gold standard for absent vs missed expression; minimizing dubious metacells protects biological zeros (averaging mixed states can erase them).

## Counter-evidence

None reported.

## Linked ideas

(none yet)

## Open questions

Performance on genes with very low or very high expression beyond the 16 tested.
