---
title: "Cell type–specific genetic regulation of immune cells"
aliases:
  - cell type–specific xQTL
  - cell type–specific eQTL
tags: []
maturity: active
key_papers:
  - chinese-immune-multi-omics-atlas
first_introduced: "chinese-immune-multi-omics-atlas"
date_updated: 2026-06-04
related_concepts:
  - enhancer-driven-gene-regulatory-network-eregulon
  - ancestry-specific-immune-regulatory-variation
---

## Definition

The principle that the effect of a genetic variant on gene expression or chromatin accessibility — and on downstream trait/disease risk — is frequently restricted to, or differs across, specific immune cell types rather than acting uniformly across whole blood.

## Intuition

Bulk-tissue QTL studies average over heterogeneous cell populations and miss regulatory effects active in only one cell state. Single-cell-resolved pseudobulk QTL mapping recovers these effects, revealing that a large share of regulatory genetic architecture is cell type–specific while a substantial subset is shared but driven by independent variants.

## Formal notation

Sharing across cell-type pairs is quantified by the π1 statistic (proportion of shared significant associations) and the rb statistic (genetic effect correlation). High mean rb with lower mean π1 indicates concordant direction but partial overlap of significant signals.

## Variants

- Cell type–specific eQTL / caQTL (effect present in one cell type only)
- Pairwise-specific xQTL (significant in a reference but not a query cell type)
- Convergent-but-independent regulation (shared eGene/peak driven by different lead variants per cell type)

## Comparison

Generalizes bulk eQTL mapping (e.g. whole-blood eQTL) to cell type resolution; complements [[concepts/enhancer-driven-gene-regulatory-network-eregulon]] which explains the regulatory machinery underlying these effects.

## When to use

When interpreting GWAS loci whose causal cell type is unknown, or when prioritizing variant–gene–trait mechanisms for immune-mediated disease.

## Known limitations

Power differences across cell types (pseudobulk sample size) can inflate apparent specificity; enrichment frameworks are needed to confirm genuine specificity.

## Open problems

Single-cell (non-pseudobulk) QTL models; resolving rare cell type effects.

## Key papers

- [[papers/chinese-immune-multi-omics-atlas]] — 73.2% of 1196 SMR pleiotropic associations significant in a single cell type; ~62% of shared eGenes/caPeaks regulated by independent variants.

## My understanding

A core organizing principle for translating immune GWAS hits into mechanisms; argues strongly for cell type–resolved reference resources.
