---
title: "SMR — Summary-data-based Mendelian Randomization"
slug: summary-data-based-mendelian-randomization-smr
domain: statistical genetics
status: mainstream
aliases:
  - SMR
  - summary-data-based Mendelian randomization
  - SMR/HEIDI
first_introduced: "2016 (Zhu et al., Nature Genetics)"
date_updated: 2026-06-04
source_url: "https://doi.org/10.1038/ng.3538"
---

## Definition

SMR (summary-data-based Mendelian randomization) is a method that integrates summary statistics from two association studies — typically a molecular QTL study (e.g. eQTL, caQTL) and a GWAS — to test whether a trait and a molecular phenotype share the same underlying causal variant. It uses a genetic variant as an instrumental variable to estimate the effect of an exposure (e.g. gene expression) on an outcome (e.g. disease risk) without requiring individual-level data.

## Intuition

If a single variant influences both gene expression and disease risk in a consistent way, the gene may mediate the genetic effect on disease. SMR quantifies this pleiotropic/causal association; the companion HEIDI test distinguishes a single shared causal variant (pleiotropy/causality) from two distinct variants in linkage disequilibrium (linkage).

## Formal notation

For an instrument SNP with GWAS effect `b_GWAS` and eQTL effect `b_eQTL`, the SMR effect estimate is `b_xy = b_GWAS / b_eQTL`, with its standard error derived from both studies. Significance is reported as `P_SMR`.

## Key variants

- SMR for eQTL–GWAS (transcriptome-wide)
- SMR for caQTL–eQTL (chromatin-mediated regulation, as used in CIMA to test variant→peak→gene)
- SMR with HEIDI filtering to exclude linkage artefacts

## Known limitations

- Number of detectable associations scales with the number of significant GWAS loci (e.g. fewer for T1D than T2D).
- Cannot fully resolve reverse causation or horizontal pleiotropy.
- Power depends on instrument strength (QTL significance).

## Open problems

- Cell type–resolved SMR at scale; multi-omic SMR chains (caQTL→eQTL→trait).

## Relevance to active research

Central to [[papers/chinese-immune-multi-omics-atlas]], which used SMR across 154 traits and 68 immune cell types to find 1196 pleiotropic associations linking variants, chromatin accessibility, gene expression, circulating proteins, and disease risk.
