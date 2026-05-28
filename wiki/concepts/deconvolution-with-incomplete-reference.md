---
title: "Deconvolution with an incomplete single-cell reference"
aliases:
  - unknown cell-type robustness in deconvolution
  - relative deconvolution
tags: [deconvolution, robustness, methods]
maturity: emerging
key_papers:
  - decode-deep-learning-based-common-deconvolution
first_introduced: "2026"
date_updated: 2026-05-28
related_concepts: [universal-multiomics-deconvolution, cell-type-abundance-from-bulk-tissue-rnaseq]
---

## Definition

The problem (and methods addressing it) of estimating cell-type proportions when the single-cell reference is missing cell types that are actually present in the tissue — i.e., the tissue has n+m cell types but the reference only covers n. A robust method must recover the relative abundances of the n known types despite the m unknown ones acting as confounding signal.

## Intuition

Comprehensive single-cell references are hard to build: some populations are lost during library prep, dissociation perturbs or destroys fragile cell types (e.g., podocytes, intercalated cells), and single-cell proteomics/metabolomics rely on in vitro lines that omit rare types. Treating the unknown-cell signal as noise to be separated lets the model still deconvolve the known types.

## Formal notation

Tissue contains types {1..n+m}; reference covers {1..n}. Estimate relative proportions over {1..n} treating contributions from {n+1..n+m} as a noise component to be removed.

## Variants

- "Relative deconvolution" inference pathway (used when unknown types present) vs. standard deconvolution (complete reference).
- Denoiser-based separation of unknown-cell signal (DECODE stage 3) vs. methods that merely characterize sensitivity (Scaden).

## Comparison

Earlier work (Scaden) examined how unknown cell types degrade stability but did not resolve it; DECODE actively separates the unknown-cell/noise component via an attention denoiser + contrastive learning.

## When to use

Whenever the reference is known to be incomplete relative to the target tissue — the common real-world case — especially for proteomics/metabolomics references from cell lines.

## Known limitations

Separation is empirical; very high unknown-type fractions still degrade accuracy.

## Open problems

Identifying *which* unknown types are present (not just removing their signal); bounding error as the unknown fraction grows.

## Key papers

- [[decode-deep-learning-based-common-deconvolution]] — addresses incomplete references via denoising + contrastive separation.

## My understanding

This is the robustness story that makes DECODE "closer to real applications" — references are essentially never complete, so this is the practically decisive property.
