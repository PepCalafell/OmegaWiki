---
title: "TensorQTL — GPU-accelerated QTL mapping"
slug: tensorqtl
domain: statistical genetics
status: mainstream
aliases:
  - TensorQTL
first_introduced: "2019 (Taylor-Weiner et al., Genome Biology)"
date_updated: 2026-06-04
source_url: "https://doi.org/10.1186/s13059-019-1836-7"
---

## Definition

TensorQTL is a GPU-accelerated software package for mapping molecular quantitative trait loci (QTLs) — associations between genetic variants and molecular phenotypes such as gene expression (eQTL) or chromatin accessibility (caQTL) — using linear models over genotype dosages and phenotype residuals.

## Intuition

By expressing the per-variant linear regressions as batched tensor operations on a GPU, TensorQTL maps cis-QTLs across millions of variant–phenotype pairs orders of magnitude faster than CPU tools, enabling cell type–resolved mapping over many pseudobulk phenotypes.

## Formal notation

For phenotype `y` (gene/peak) and genotype `g` within a cis window (±1 Mb of the TSS or peak midpoint), it fits `y = βg + Cγ + ε`, with covariates `C` (e.g. age, sex, genotype PCs, PEER factors), reporting nominal and permutation/FDR-adjusted p-values per lead variant.

## Key variants

- cis-eQTL and cis-caQTL mapping
- trans-QTL scan over the genome
- conditional/independent QTL analysis

## Known limitations

- Linear additive model; misses epistasis and nonlinear effects.
- Pseudobulk aggregation discards within-cell-type heterogeneity.
- Power tied to pseudobulk sample size per cell type.

## Open problems

- Scalable single-cell (non-pseudobulk) QTL models.

## Relevance to active research

Used in [[papers/chinese-immune-multi-omics-atlas]] to map cis-xQTLs across 69 (eQTL) and 42 (caQTL) immune cell types, yielding 9600 eGenes and 52,361 caPeaks.
