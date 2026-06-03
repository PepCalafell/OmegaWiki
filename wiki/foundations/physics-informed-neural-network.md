---
title: "Physics-Informed Neural Network (PINN)"
slug: physics-informed-neural-network
domain: "methods / scientific machine learning / PDE solving"
status: mainstream
aliases:
  - PINN
  - physics-informed neural networks
  - physics informed deep learning
first_introduced: "Raissi, Perdikaris & Karniadakis 2019 *J. Comput. Phys.* — Physics-informed neural networks"
date_updated: 2026-06-03
source_url: "https://doi.org/10.1016/j.jcp.2018.10.561"
---

## Definition

A physics-informed neural network is a neural network trained to approximate the solution of a (partial) differential equation by embedding the governing equation directly into the loss function. A surrogate network `uθ(x,t)` represents the unknown field; automatic differentiation supplies the required spatial and temporal derivatives; and a residual loss penalizes violation of the PDE at collocation points, supplementing data-fitting and boundary/initial-condition losses.

## Intuition

Instead of discretizing space onto a mesh (finite element / finite difference), the PDE is enforced softly as a regularizer on a continuous, mesh-free function approximator. This makes PINNs attractive for high-dimensional or irregular domains where meshing is infeasible, and lets them solve both forward problems (given parameters, find the field) and inverse problems (given sparse field observations, recover unknown parameters/source terms).

## Formal notation

For a PDE `N[u](x,t)=0` with solution `u`, define the residual `r = N[uθ]`. Train by minimizing `L = L_data + λ·L_residual (+ L_bc/ic)`, where `L_residual = ∫ |r(x,t)|² dx dt` evaluated at sampled collocation points, and derivatives of `uθ` come from autograd.

## Key variants

- Forward vs inverse PINNs (parameter/coefficient estimation).
- Conservative / variational PINNs (weak-form residuals).
- Domain-decomposition PINNs (XPINN, cPINN) for large domains.
- PINNs coupled with Neural ODE integration for time evolution.

## Known limitations

- Training can be ill-conditioned; loss-term weighting (`λ`) is sensitive and often hand-tuned.
- Stiff PDEs, sharp gradients, and high-frequency solutions are hard to fit.
- No general convergence guarantees; spectral bias of MLPs hurts fine-scale features.

## Open problems

- Principled, adaptive weighting of residual vs data losses.
- Scaling to very high-dimensional state spaces with provable accuracy.

## Relevance to active research

- Core engine of [[papers/pseudodynamics-reconstructing-population-dynamics-time-resolved]], which uses a PINN surrogate plus behaviour networks to solve the single-cell advection-reaction-diffusion PDE without pseudotime discretization, paired with [[foundations/neural-ordinary-differential-equation]] integration.
