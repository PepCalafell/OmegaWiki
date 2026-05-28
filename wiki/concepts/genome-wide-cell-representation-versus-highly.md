---
title: "Genome-wide cell representation versus highly-variable-gene truncation"
aliases:
  - genome-wide cell representation
  - full-transcriptome cell representation
  - informational completeness of cell state
tags: [genome-wide, HVG, feature-representation, single-cell, perturbation, completeness]
maturity: emerging
key_papers:
  - towards-building-world-model-simulate-perturbation
first_introduced: "Chuai et al. 2026 bioRxiv (AlphaCell)"
date_updated: 2026-05-28
related_concepts: []
---

## Definition

The design principle that a cellular state should be represented over the full protein-coding transcriptome (here 19,253 HGNC genes) rather than a truncated set of ~1,000–2,000 highly variable genes (HVGs) or a fixed panel (e.g., L1000). The argument is that HVG truncation violates the informational completeness needed to rigorously define a cell state, systematically discarding low-abundance high-information regulatory drivers (master TFs, receptors).

## Intuition

You cannot define the full state of a system while ignoring most of its variables. HVGs are chosen for variance in the observed/control data, but a perturbation may activate genes that were quiescent (low-variance) before — so a variance-based filter is biased toward the training distribution.

## Formal notation

Input space = 19,253 genes with strict bijective gene→channel mapping (HGNC), vs HVG subset ≪ full set.

## Variants

- Full protein-coding transcriptome (AlphaCell).
- Fixed marker panels (L1000) — a more severe truncation.

## Comparison

Opposed to [[foundations/hvg-selection-scrna]], the standard practice. AlphaCell argues — and reports empirically — that naively extending baselines to the full geneset degrades them ([[claims/extending-baseline-models-hvgs-full-geneset]]); genome-wide input only helps when paired with manifold rectification ([[concepts/manifold-rectification-continuous-virtual-cell-space]]).

## When to use

- Zero-shot perturbation prediction where response genes are unknown a priori.
- Capturing low-abundance regulatory drivers excluded by HVG filters.

## Known limitations

- Genome-wide input is sparse, zero-inflated, and high-dimensional; without rectification it triggers the curse of dimensionality.

## Open problems

- Quantifying how many response-relevant genes fall outside control-derived HVG sets.

## Key papers

- [[papers/towards-building-world-model-simulate-perturbation]]

## My understanding

The strongest conceptual contribution of the paper: a clear logical case against HVG truncation for zero-shot settings (see [[claims/hvg-feature-selection-theoretically-ill-posed]]). The catch is that genome-wide input is only an asset with a denoising/rectifying encoder, otherwise it hurts.
