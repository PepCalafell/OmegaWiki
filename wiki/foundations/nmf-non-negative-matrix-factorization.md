---
title: "Non-negative matrix factorization (NMF)"
slug: nmf-non-negative-matrix-factorization
domain: methods
status: mainstream
aliases:
  - NMF
  - non-negative matrix factorization
  - nonnegative matrix factorisation
  - NNMF
  - parts-based factorization
  - additive matrix factorization
first_introduced: "Lee & Seung, Nature 1999"
date_updated: 2026-05-26
source_url: "https://www.nature.com/articles/44565"
---

## Definition

Non-negative matrix factorization (NMF) decomposes a non-negative matrix V (genes × cells) into two non-negative matrices W (genes × K) and H (K × cells) with V ≈ WH. Each of the K factors represents an additive component (a gene program); each cell is expressed as a non-negative combination of these programs.

## Intuition

Negative loadings are biologically meaningless for expression data (genes are either expressed or not). Forcing non-negativity yields parts-based, sparse decompositions where factors correspond to interpretable gene programs (e.g. cell-cycle, hypoxia, EMT) rather than to abstract PCA-style axes.

## Formal notation

Minimise ||V − WH||² (or the KL divergence) subject to W ≥ 0, H ≥ 0. K (the number of factors) is a hyperparameter chosen empirically; in 3CA, K is varied between 4–9 per tumour and programs robust across K values are kept.

## Key variants

- Multiplicative update rules (Lee & Seung).
- Sparse NMF / projective NMF.
- Integrative NMF (iNMF, LIGER) for joint factorization across datasets.
- Robust NMF in cancer scRNA-seq (Gavish/Tirosh framework) — per-sample NMF with cross-K and cross-tumour robustness filtering.

## Known limitations

- K selection is heuristic; results depend on initialisation and K range.
- Computationally heavier than PCA at scale.
- Factor scaling is non-identifiable up to diagonal rescaling of W and H.

## Open problems

- Principled K selection across heterogeneous tumours.
- Direct integration with batch correction without sacrificing the parts-based interpretability.

## Relevance to active research

NMF is the workhorse for [[concepts/recurrent-malignant-metaprograms-nmf|recurrent malignant metaprogram]] discovery in pan-cancer scRNA-seq and underpins LIGER, [[foundations/scenic-tf-regulon-inference|SCENIC]]-derived regulon analyses, and many tumour-state classifications.
