---
title: "EpiDISH"
slug: epidish-cell-type-deconvolution-methylation
domain: methods
status: mainstream
aliases: ["EpiDISH", "Epigenetic Dissection of Intra-Sample-Heterogeneity"]
first_introduced: "2017"
date_updated: 2026-06-12
source_url: "https://bioconductor.org/packages/EpiDISH/"
---

## Definition

EpiDISH (Epigenetic Dissection of Intra-Sample-Heterogeneity) estimates cell-type fractions from bulk DNA-methylation data using reference methylation profiles, enabling adjustment for cell composition in EWAS.

## Intuition

Because methylation is cell-type specific, bulk-tissue signals can be confounded by shifts in cell proportions. EpiDISH infers those proportions (e.g. 12 blood cell types) so they can be modeled as covariates.

## Formal notation

Reference-based deconvolution (robust partial correlation / CIBERSORT / constrained projection) against a cell-type methylation reference matrix.

## Key variants

RPC, CBS, and CP modes; whole-blood and epithelial reference panels.

## Known limitations

Accuracy depends on reference completeness; rare cell types are harder to resolve.

## Open problems

Higher-resolution deconvolution of granulocyte subtypes from array data.

## Relevance to active research

Used in sensitivity analyses (12 cell types) to confirm BCG-associated CpGs are robust to finer cell-composition adjustment.
