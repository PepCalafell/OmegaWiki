---
title: "HyenaDNA — long-range genomic sequence model"
slug: hyenadna-genomic-sequence-model
domain: machine learning / genomics
status: mainstream
aliases:
  - HyenaDNA
first_introduced: "2023 (Nguyen et al., NeurIPS)"
date_updated: 2026-06-04
source_url: "https://arxiv.org/abs/2306.15794"
---

## Definition

HyenaDNA is a genomic foundation model that replaces attention with the sub-quadratic Hyena operator (implicit long convolutions plus gating), enabling single-nucleotide-resolution modeling of DNA sequences at context lengths up to ~1 Mb with linear scaling in sequence length.

## Intuition

Standard transformers scale quadratically with sequence length, limiting genomic context. The Hyena operator achieves long-range, single-nucleotide context cheaply, producing DNA embeddings useful for downstream regulatory prediction tasks.

## Formal notation

The Hyena operator computes `y = x ⊙ (h * x)` style gated long convolutions where the filter `h` is parameterized implicitly by an MLP over positional encodings, giving `O(L log L)` cost versus attention's `O(L^2)`.

## Key variants

- Pretrained HyenaDNA at multiple context lengths
- Use as a frozen DNA encoder feeding downstream task heads

## Known limitations

- Pretrained on reference genome; cell-context must be supplied separately.
- Single-nucleotide resolution increases compute for very long inputs.

## Open problems

- Combining sequence embeddings with cell-state embeddings for context-specific regulation.

## Relevance to active research

In [[papers/chinese-immune-multi-omics-atlas]], pretrained HyenaDNA encodes 501-bp chromatin sequences in the CIMA-CLM model, fused with scGPT cell embeddings to predict cell type–specific chromatin accessibility.
