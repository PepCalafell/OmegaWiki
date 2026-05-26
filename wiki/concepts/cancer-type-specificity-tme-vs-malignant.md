---
title: "Cancer-type specificity of malignant vs TME cell expression"
aliases:
  - cancer-type specificity
  - pan-cancer conservation of TME
  - cell-type pseudobulk similarity
  - TME pan-cancer conservation
  - malignant cancer-type specificity
  - pseudobulk cancer-type effect
  - TME cell pan-cancer
  - cancer-type effect on expression
tags: [pan-cancer, tme, malignant, pseudobulk, batch-control, scrna-seq]
maturity: emerging
key_papers:
  - curated-cancer-cell-atlas-provides-comprehensive
first_introduced: "2025 (Tyler et al., 3CA v2)"
date_updated: 2026-05-26
related_concepts: [curated-cancer-cell-atlas-3ca, pan-cancer-tam-atlas-23-clusters, momac-verse-mnp-verse-atlas]
---

## Definition

Cancer-type specificity quantifies how much a cell type's average expression profile depends on the cancer type it comes from, computed via pseudobulk similarity within vs across cancer types (restricted to pairs from different studies to control for batch effects).

## Intuition

For each tumour, aggregate the cells of a given type (e.g. T cells, macrophages, fibroblasts, malignant cells, epithelial cells) into a pseudobulk profile. Then compare the mean expression similarity of pseudobulk pairs from the **same** cancer type versus pairs from **different** cancer types. A positive difference means cancer type shapes that cell type's expression; ~zero means the cell type is pan-cancer conserved.

## Key finding (Tyler et al. 2025)

- Malignant cells have **by far the highest** cancer-type specificity.
- Non-malignant epithelial cells are next, driven by tissue-of-origin.
- Immune (T cell, B cell, NK, macrophage, dendritic, mast, plasma) and stromal (fibroblast, endothelial, pericyte) cell types show **minimal cancer-type effect** — pairwise differences among them are not significant.

## Implication

The TME cell types are largely **pan-cancer conserved** on average, supporting the validity of cross-cancer-type TME analyses (TAM atlases, T-cell exhaustion atlases, CAF atlases). Variability within a TME cell type comes from tumour-specific state distributions, not from the tumour identity itself.

## When to use

- When deciding whether to pool TME cells across cancer types in an analysis.
- When interpreting whether a TME signature reported in one cancer type generalises.

## Known limitations

- Captures average expression; within-cell-type state variability remains substantial.
- Does not separate tissue-of-origin effects (basal expression) from cancer-driven effects on TME.
- Effect sizes are within-study only; the cross-study controls reduce batch effects but do not eliminate technological differences.

## Key papers

- [[curated-cancer-cell-atlas-provides-comprehensive]] — first cross-cell-type quantification in 3CA v2.
- [[pan-cancer-tam-atlas-23-clusters|MoMac/TAM atlases]] — empirically rely on pan-cancer TME conservation.

## My understanding

This is the principled justification for pan-cancer TAM, T-cell and CAF atlases that the field has been building for years. The pseudobulk-within-vs-across-cancer-type-only-across-studies design is a clean way to make the claim quantitative.
