---
title: "UCell — gene-signature scoring for single-cell RNAseq"
slug: ucell-signature-scoring
domain: "computational-biology / methods"
status: mainstream
aliases:
  - "UCell"
  - "UCell scoring"
  - "UCell signature score"
  - "Mann-Whitney U rank gene-signature scoring"
  - "robust per-cell signature score"
  - "AddModuleScore_UCell"
  - "single-cell gene set scoring"
  - "rank-based per-cell signature scoring"
first_introduced: "Andreatta & Carmona 2021 *Comput Struct Biotechnol J*"
date_updated: 2026-05-13
source_url: "https://github.com/carmonalab/UCell"
---

## Definition

UCell is a per-cell gene-signature scoring method based on the Mann-Whitney U statistic computed on ranked gene expression within each cell. It is robust to dropout and to varying numbers of genes per signature, and produces scores in the range [0,1] interpretable as the fraction of signature genes ranked among the top expressed.

## Intuition

For each cell, rank all genes by expression. The UCell score for a signature is essentially the average rank of the signature's genes (normalized) — a high score means most signature genes are highly ranked in that cell, regardless of absolute expression levels.

## Formal notation

- Input: scRNAseq expression matrix (cell × gene) + a gene-signature list.
- Per cell, rank genes by expression (ties handled deterministically).
- Compute the U statistic on the ranks of signature genes vs the rest.
- Normalize to [0,1].
- Output: per-cell signature score; comparable across cells and signatures.

## Strengths

- Robust to dropouts (rank-based).
- Robust to signature size (works for ~5-1000 genes).
- No global normalization required.

## Limitations

- Sensitive to the top-N gene-ranking ceiling parameter.
- Signatures with shared genes between clusters can produce ambiguous scores.
- Per-cell scoring is non-parametric — does not produce p-values directly.

## Use cases in this corpus

- [[papers/using-pan-cancer-atlas-investigate-tumour]] uses UCell to (i) compute the "gold-standard" signature criterion in an all-cell-type atlas (Metric1 = best - second-best mean UCell > 0.1), and (ii) score 18_ECMMac and 8_IFNGMac signatures on CosMx FFPE spatial data with thresholds >0.8 (in-cluster) and <0.4 (out-of-cluster).

## Relevance to active research

- [[papers/using-pan-cancer-atlas-investigate-tumour]] — Coulton et al. 2024.
