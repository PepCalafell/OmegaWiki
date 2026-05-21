---
title: "scDesign3 — realistic single-cell and spatial simulation framework"
slug: scdesign3-simulator
domain: single-cell-methods
status: mainstream
aliases:
  - scDesign3
  - scDesign 3
  - scDesign3 simulator
  - scDesign3 spatial simulation
  - Song et al. 2023 scDesign3
  - GP-based spatial simulation
  - copula spatial simulation
first_introduced: "Song et al. 2023 Nature Biotechnology"
date_updated: 2026-05-21
source_url: "https://github.com/SONGDONGYUAN1994/scDesign3"
---

## Definition

scDesign3 is a unified simulation framework for single-cell and spatial omics. It learns each gene's marginal distribution (typically negative-binomial) and the joint copula across genes from a real reference dataset, then generates synthetic data preserving realistic biological patterns.

## Intuition

For spatial transcriptomics, scDesign3 fits each gene's mean expression as a Gaussian-process function of (spatial1, spatial2), and its joint dependence with other genes through a Gaussian copula. By mixing the GP mean with a shuffled non-spatial mean via parameter α ∈ [0,1], one can generate genes with a continuous gradient of spatial variability — enabling SVG-method benchmarking against ground truth that is biologically realistic rather than predefined-cluster artificial.

## Key variants

- `fit_marginal(mu_formula="s(spatial1, spatial2, bs='gp', k=500)", family_use="nb")` for per-gene GP marginal.
- `fit_copula(family_use="nb", copula="gaussian")` for joint dependence.
- `simu_new` for sample generation with α-controlled spatial variability.

## Known limitations

- Requires pre-selection of genes with high spatial variation, which can bias benchmarks towards certain method families.
- Per-gene Kendall correlation does not compare methods across different spatial patterns simultaneously.

## Relevance to active research

scDesign3 is the simulation engine underlying the SVG benchmark in Li et al. 2025 (96 spatial datasets across 9 technologies). The benchmark argues that GP-based simulation is more biologically realistic than the binary SVG/non-SVG simulations used in prior SVG-method papers.
