---
title: "Gaussian kernel density estimation (KDE)"
slug: gaussian-kernel-density-estimation
domain: "methods / nonparametric statistics / density estimation"
status: mainstream
aliases:
  - Gaussian KDE
  - kernel density estimation
  - Parzen window estimation
first_introduced: "Rosenblatt 1956; Parzen 1962 — nonparametric density estimation"
date_updated: 2026-06-03
source_url: "https://doi.org/10.1214/aoms/1177728190"
---

## Definition

Kernel density estimation is a nonparametric method for estimating a probability density from samples by placing a smooth kernel (here a Gaussian) at each data point and summing. The Gaussian KDE at point `x` is `f̂(x) = (1/n)·Σᵢ K_h(x − xᵢ)`, where `K_h` is a Gaussian kernel with bandwidth `h`.

## Intuition

Each observed sample contributes a small smooth bump; their sum approximates the underlying continuous density. Bandwidth controls the bias–variance trade-off: small `h` is spiky (overfits), large `h` oversmooths.

## Formal notation

`f̂(x) = (1/(n hᵈ)) Σᵢ (2π)^(−d/2) exp(−‖x−xᵢ‖²/(2h²))`; bandwidth often chosen by Scott's or Silverman's rule, or cross-validation.

## Key variants

- Adaptive / variable-bandwidth KDE.
- Hashing-based and fast approximate KDE for large data.
- Mixture-model and deep-learning density estimators (GMM, normalizing flows) as alternatives.

## Known limitations

- Suffers from the curse of dimensionality; unreliable in high-dimensional spaces.
- Bandwidth selection is sensitive and data-dependent.
- Boundary bias near the support edges.

## Open problems

- Reliable high-dimensional density estimation on single-cell manifolds.

## Relevance to active research

- Used by [[papers/pseudodynamics-reconstructing-population-dynamics-time-resolved]] (scipy Gaussian KDE on [[foundations/diffusion-map-embedding]] coordinates, rescaled to the observed total population size) to produce the per-timepoint density the PINN surrogate fits; benchmarked as the best estimator against TIGON GMM, Mellon and Denmarf.
