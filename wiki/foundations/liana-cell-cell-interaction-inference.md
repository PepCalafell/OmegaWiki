---
title: "LIANA — ligand-receptor / cell-cell interaction inference"
slug: "liana-cell-cell-interaction-inference"
domain: "methods / cell-cell communication"
status: mainstream
aliases:
  - LIANA
first_introduced: "2022"
date_updated: 2026-06-05
source_url: ""
---

## Definition

LIANA (LIgand-receptor ANalysis frAmework) is a framework that aggregates multiple ligand-receptor inference methods and resources to call cell-cell interaction networks from single-cell transcriptomics, producing consensus interaction scores between cell types.

## Intuition

Different ligand-receptor tools disagree; LIANA runs several and combines their rankings so the inferred interactions are robust to any single method's idiosyncrasies.

## Formal notation

expression matrix + cell-type labels + LR resource → per-method scores → rank-aggregated consensus interactions.

## Key variants

- Wraps methods such as CellPhoneDB, NATMI, Connectome, SingleCellSignalR, and logFC scoring.

## Known limitations

- Infers interactions from co-expression, not physical contact; spatial proximity is not guaranteed.

## Open problems

- Integrating spatial constraints to filter transcriptomically plausible but spatially impossible interactions.

## Relevance to active research

Used to map the cell-cell interaction network of Macro-CXCL9, identifying CXCL9/CXCL10–ACKR1, HLA-DR/DQ–LAG3, and C1QB/APOE–LRP1/LRP6 axes with neighbouring cells.
