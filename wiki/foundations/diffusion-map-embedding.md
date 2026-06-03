---
title: "Diffusion map embedding"
slug: diffusion-map-embedding
domain: "methods / dimensionality reduction / single-cell trajectory"
status: mainstream
aliases:
  - diffusion map
  - diffusion maps
  - diffusion component
  - DM coordinates
first_introduced: "Coifman & Lafon 2006 *Appl. Comput. Harmon. Anal.*; single-cell use popularized by Haghverdi et al. 2015/2016 and Palantir (Setty et al. 2019)"
date_updated: 2026-06-03
source_url: "https://doi.org/10.1016/j.acha.2006.04.006"
---

## Definition

A diffusion map is a non-linear dimensionality-reduction method that embeds data using the eigenvectors of a Markov transition (random-walk) matrix built from a local affinity (Gaussian) kernel over the data graph. The resulting diffusion components capture the intrinsic geometry of the data manifold, with Euclidean distance in the embedding approximating "diffusion distance" along the manifold.

## Intuition

By modelling transitions between nearby cells as a random walk, diffusion maps preserve connectivity and continuous transitions while denoising — making them well suited to single-cell developmental landscapes where cells form continuous branching trajectories rather than discrete clusters.

## Formal notation

Build affinity `W_ij = exp(−‖x_i−x_j‖²/σ²)`, row-normalize to a Markov matrix `P = D⁻¹W`; the leading non-trivial eigenvectors of `P` (scaled by eigenvalues at diffusion time `t`) give the diffusion-map coordinates.

## Key variants

- Multiscale / adaptive-kernel diffusion maps.
- Palantir and DPT (diffusion pseudotime) build pseudotime and fate on top of diffusion components.

## Known limitations

- Kernel bandwidth `σ` and number of components are sensitive hyperparameters.
- Eigen-decomposition cost scales with cell number (mitigated by sparse/landmark methods).

## Open problems

- Reversible mapping back to gene-expression space for interpretability.

## Relevance to active research

- The cell-state space `s` on which [[papers/pseudodynamics-reconstructing-population-dynamics-time-resolved]] solves its PDE; computed with `palantir.utils.run_diffusion_maps`, chosen over PCA because density estimates from diffusion-map coordinates best matched the pseudotime ground truth.
