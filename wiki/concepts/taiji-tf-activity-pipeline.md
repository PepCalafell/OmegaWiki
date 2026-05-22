---
title: "Taiji TF activity pipeline"
aliases:
  - "Taiji"
  - "Taiji TF activity"
  - "Taiji PageRank TF activity"
  - "scTaiji"
  - "PageRank-based TF activity inference"
  - "RNA + ATAC TF activity pipeline"
  - "GRN PageRank TF importance"
  - "personalized PageRank TF analysis"
tags: [methods, transcription-factor, gene-regulatory-network, multi-omics, immunology]
maturity: active
key_papers: [atlas-guided-discovery-transcription-factors-cell]
first_introduced: "2018"
date_updated: 2026-05-22
related_concepts: [single-state-vs-multi-state-tf-classification, tf-community-analysis-grn]
---

## Definition

Computational pipeline that infers transcription factor activity in a cell state by (1) constructing a gene regulatory network where each edge weight integrates predicted TF–motif binding affinity, ATAC-seq accessibility at the target locus, and RNA-seq expression of TF and target; (2) running personalized PageRank ([[pagerank-algorithm]]) on this directed weighted graph; (3) normalizing scores across samples to produce a TF activity fingerprint per cell state.

## Intuition

TF activity ≠ TF expression. PageRank lets a TF score reflect upstream regulators, downstream targets, and feedback loops, so a TF can score high without high mRNA, and vice versa. The single-cell extension (scTaiji) builds pseudobulks per cell state from paired scRNA-seq + scATAC-seq.

## When to use

Whenever the goal is to **rank TFs by global regulatory influence** in distinct cell states (not just differential expression) and paired transcriptomic + chromatin data are available.

## Known limitations

- Requires both RNA-seq and ATAC-seq (or paired scRNA + scATAC) — incompatible with RNA-only datasets.
- TFs without DNA-binding motifs in the database (e.g. ZSCAN20) cannot be scored, only inferred via expression.
- Misclassification of "single-state" vs "multi-state" TFs near statistical thresholds (e.g. Eomes called TEXterm single-state despite known TEM/TCM/TRM roles).

## Key papers

- [[atlas-guided-discovery-transcription-factors-cell]] — Chung et al. 2025: Taiji applied to a 121-sample, 9-state CD8+ T cell atlas to discover TEXterm-selective TFs (ZSCAN20, JDP2).
