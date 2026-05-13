---
title: "fgsea — fast gene-set enrichment analysis"
slug: fgsea-gene-set-enrichment
domain: "computational-biology / methods"
status: mainstream
aliases:
  - "fgsea"
  - "FGSEA"
  - "fast gene set enrichment analysis"
  - "fgsea R package"
  - "preranked GSEA"
  - "Korotkevich fgsea"
  - "rank-based enrichment scoring"
  - "GSEA fast implementation"
first_introduced: "Korotkevich, Sukhov & Sergushichev 2021 *bioRxiv* (fgsea R package)"
date_updated: 2026-05-13
source_url: "https://github.com/ctlab/fgsea"
---

## Definition

fgsea is a fast Bioconductor implementation of preranked Gene Set Enrichment Analysis (GSEA). Given a ranked gene list (e.g., DESeq2 statistics) and a collection of gene sets / pathways, fgsea computes normalized enrichment scores (NES) and adaptive multilevel-split p-values much faster than the canonical Broad GSEA implementation.

## Intuition

For each gene set, walk down the ranked list; running-sum statistic increases when a set gene is encountered and decreases otherwise. The maximum deviation from zero is the enrichment score; permutation provides significance.

## Workflow

1. Provide a named numeric vector of gene-level statistics (e.g., DESeq2 log2FC × sign × −log10(p)).
2. Provide a list of gene sets (named).
3. Run `fgsea()` with `minSize`, `maxSize`, `nPermSimple`.
4. Adjust p-values for multiple testing (BH).
5. Visualize via `plotEnrichment()` / `plotGseaTable()`.

## Strengths

- Orders-of-magnitude faster than Broad GSEA via adaptive multilevel splitting.
- Bioconductor integration; deterministic output with seed control.
- Handles signed and unsigned gene-level statistics.

## Limitations

- p-value precision capped by permutation count.
- Sensitive to ranking statistic choice.
- Gene-set redundancy (overlapping pathways) not deconvolved.

## Use cases in this corpus

- [[papers/using-pan-cancer-atlas-investigate-tumour]] uses fgsea v1.22.0 with TAM cluster top-DEG signatures as pathways and DESeq2 statistics from the CPI1000+ cohort as the ranking; identifies 18_ECMMac as non-responder-enriched (q=3.8e-5) and 8_IFNGMac / 17_IFNMac3 / 14_ProliMac etc. as responder-enriched.

## Relevance to active research

- [[papers/using-pan-cancer-atlas-investigate-tumour]] — Coulton et al. 2024.
