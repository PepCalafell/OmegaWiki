---
title: "MetaCell aggregation (~30 cells/MetaCell) plus CCA reduces batch effects more than single-cell-level CCA integration while preserving cell-type biology"
slug: metacell-cca-integration-outperforms-single-cell-batch-correction
status: supported
confidence: 0.85
tags:
  - methodological
  - scrna-seq
  - integration
  - metacell
  - batch-effect
domain: single-cell methodology
source_papers:
  - spatiotemporal-analyses-pan-cancer-single-cell
evidence:
  - source: spatiotemporal-analyses-pan-cancer-single-cell
    type: supports
    strength: strong
    detail: LISI/silhouette comparisons (Extended Data Fig. 2e,f) show better batch mixing and preserved variation for MetaCell+CCA vs single-cell-level CCA.
conditions: "Pan-cancer scRNA-seq with 30-cell MetaCells; benchmarks against batch correction at single-cell level only."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

MetaCell coarse-graining (~30 cells each) followed by CCA integration outperforms single-cell-level CCA at reducing technical batch effects while preserving cell-type-specific biological variation in pan-cancer scRNA-seq integration.

## Conditions and scope

Direct quote: "the integration using MetaCells demonstrates superior performance, significantly reducing batch effects while preserving cell-type-specific biological variation" (Han 2025, Extended Data Fig. 2e,f).

## Linked ideas

- MetaCell aggregation as a default preprocessing step for any large-scale scRNA-seq integration in the wiki.
