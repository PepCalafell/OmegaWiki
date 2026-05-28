---
title: "Cell-type abundance scoring from bulk tissue RNA-seq using specificity-ranked gene sets"
aliases:
  - cell-type abundance scoring
  - cell type deconvolution bulk RNA-seq
  - cell-type specificity score
  - cell-type abundance score bulk
  - bulk RNA-seq deconvolution cytokine
  - cell-type signature scoring
  - ranked gene set cell-type score
  - 195 cell type bulk inference
  - z-score cell type abundance bulk
tags:
  - deconvolution
  - bulk-RNA-seq
  - cell-type
  - methods
maturity: active
key_papers:
  - pairwise-cytokine-code-explains-organism-wide
  - decode-deep-learning-based-common-deconvolution
first_introduced: "2024"
date_updated: 2026-05-28
related_concepts:
  - pairwise-cytokine-code-sepsis
---

## Definition

A bulk-tissue cell-type abundance score: compute per-gene cell-type specificity from a reference scRNA-seq atlas (195 cell types × 9 organs), rank genes per cell type, score each bulk sample's enrichment of the top-ranked genes, then z-score across conditions to call significant abundance changes (|z|>1).

## Intuition

Rather than full deconvolution (CIBERSORTx, MuSiC), the method computes a directional "score" that captures abundance shifts under perturbation while remaining robust to limited reference depth. Validated downstream by spatial transcriptomics and immunohistochemistry.

## Comparison

- CIBERSORTx — produces absolute fractions; requires deeper reference and accurate signature matrix
- MuSiC — Bayesian per-subject deconvolution; sensitive to reference batch
- Specificity-score method (Takahama 2024) — directional shifts in 195 cell types across 9 organs, validated by spatial+IHC; agnostic to absolute fraction estimation

## When to use

Use when bulk-RNA-seq covers many organ-condition combinations and a matched single-cell atlas exists for tissue references.

## Key papers

- [[papers/pairwise-cytokine-code-explains-organism-wide]]
- [[papers/decode-deep-learning-based-common-deconvolution]] — a learned, distribution-agnostic deconvolver applicable across omics

## My understanding

A pragmatic, validated alternative to full deconvolution for organism-wide perturbation screens where 195 × 9 × N conditions makes single-cell profiling impractical.
