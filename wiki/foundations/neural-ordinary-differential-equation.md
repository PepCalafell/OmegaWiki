---
title: "Neural Ordinary Differential Equation (Neural ODE)"
slug: neural-ordinary-differential-equation
domain: "methods / deep learning / continuous-time models"
status: mainstream
aliases:
  - Neural ODE
  - NeuralODE
  - continuous-depth network
  - ODE-Net
first_introduced: "Chen, Rubanova, Bettencourt & Duvenaud 2018 *NeurIPS* — Neural Ordinary Differential Equations"
date_updated: 2026-06-03
source_url: "https://arxiv.org/abs/1806.07366"
---

## Definition

A Neural ODE parameterizes the time derivative of a hidden state with a neural network, `dz/dt = f(z,t;θ)`, and obtains the state at any time by numerically integrating with a black-box ODE solver. Gradients are computed either by backpropagating through the solver or via the adjoint sensitivity method, giving constant-memory training.

## Intuition

It replaces a discrete stack of residual layers (`z_{t+1} = z_t + f(z_t)`) with a continuous flow, letting the "depth" be set by the solver's adaptive step size and the output be evaluated at arbitrary continuous times — natural for irregularly-sampled time series and continuous dynamics.

## Formal notation

`z(t₁) = z(t₀) + ∫_{t₀}^{t₁} f(z(t),t;θ) dt`, solved with adaptive solvers (e.g. Dopri5) or fixed-step solvers (e.g. RK4). Adjoint: solve an augmented ODE backward in time for `dL/dθ`.

## Key variants

- Adjoint vs direct backprop through the solver.
- Augmented Neural ODEs (extra dimensions for expressivity).
- Latent ODEs / ODE-RNN for time series; Neural SDEs for stochastic dynamics.

## Known limitations

- Stiff dynamics force tiny steps → slow; solver tolerance trades speed vs accuracy.
- Adjoint can be numerically unstable; reversibility assumptions may fail.
- Underflow / numerical issues may require fallback fixed-step solvers.

## Open problems

- Robust training under stiffness; principled solver/tolerance selection.

## Relevance to active research

- Used in [[papers/pseudodynamics-reconstructing-population-dynamics-time-resolved]] to integrate the right-hand side of the single-cell density PDE between observed timepoints (Dopri5 default, RK4 fallback), simulating density evolution and supplying the simulation loss.
