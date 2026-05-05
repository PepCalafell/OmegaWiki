---
title: "CIBERSORTx — bulk deconvolution"
slug: cibersortx-deconvolution
domain: "computational-biology / methods"
status: mainstream
aliases:
  - "CIBERSORTx"
  - "CIBERSORT"
  - "in silico cell-type deconvolution"
  - "bulk RNA-seq cell-type proportion estimation"
  - "signature-matrix deconvolution"
  - "CIBERSORTx imputation"
first_introduced: "Newman et al. 2015 *Nat Methods*; CIBERSORTx Newman et al. 2019 *Nat Biotech*"
date_updated: 2026-05-05
source_url: "https://cibersortx.stanford.edu/"
---

## Definition

CIBERSORTx is a deconvolution method that estimates the relative proportions and cell-type-specific expression profiles of constituent cell types in a bulk RNA-seq mixture, using a reference signature matrix (often built from scRNA-seq or sorted-cell expression). It extends the original CIBERSORT (built from microarray, immune-only LM22) to allow custom signature matrices and high-resolution mode for cell-type-specific gene expression imputation.

## Intuition

When you have bulk RNA-seq from a tumor and want to know "how much of cell type X is in there?", CIBERSORTx solves a regression-style problem against a signature matrix. The output is a per-sample proportion vector summing to 1, plus optional imputed per-cell-type expression.

## Formal notation

- Input: bulk RNA-seq matrix + signature matrix (genes × cell types)
- Method: ν-SVR (support vector regression) for proportions; high-res mode adds NMF-based per-cell-type expression imputation
- Output: cell-type proportions (per sample) + optional imputed per-cell-type bulk expression

## Key variants

- LM22 (default immune signature, 22 cell types)
- Custom signature matrices from scRNA-seq atlases (e.g., MoMac-VERSE)
- Other deconvolution tools: MuSiC, SCDC, BayesPrism, EPIC, quanTIseq

## Known limitations

- Signature matrix quality is critical; missing cell types cause systematic bias.
- Closely related cell types (e.g., MAC subsets) are hard to disentangle.
- Best used for relative changes across samples, not absolute proportions.

## Open problems

- Single-cell-resolution deconvolution of rare populations.
- Cross-platform / cross-study generalization.

## Relevance to active research

[[papers/nf-kb-tet2-promote-macrophage-reprogramming]] uses CIBERSORTx with a MoMac-VERSE-derived custom signature matrix to estimate proportions of mMAC1, mMAC21, IL4I1 MAC, TREM2 MAC, FOLR2 MAC, T cells, and other populations in TCGA bladder urothelial carcinoma samples. The mMAC1 vs T-cell correlation (r=0.74) that drives the survival argument is computed on CIBERSORTx-derived proportions.
