---
title: "Perturbation as continuous flow versus discrete jump"
aliases:
  - perturbation as continuous flow
  - continuous state transition modeling
tags: [perturbation, flow-matching, optimal-transport, vector-field, dynamics, single-cell]
maturity: emerging
key_papers:
  - towards-building-world-model-simulate-perturbation
first_introduced: "Chuai et al. 2026 bioRxiv (AlphaCell)"
date_updated: 2026-05-28
related_concepts: []
---

## Definition

A modeling paradigm in which a perturbation's effect on a cell is represented as a continuous deterministic flow — a vector field transporting a control state embedding to its perturbed state along an optimal trajectory — rather than as a discrete jump (a learned mapping or vector shift from control to perturbed distribution). AlphaCell realizes this via Optimal Transport Conditional Flow Matching.

## Intuition

A discrete jump says "control distribution → perturbed distribution" in one step and tends to memorize/average noisy endpoints. A continuous flow learns the whole path; by following a coherent field across the population it averages out incoherent per-cell noise and captures non-linear dynamics.

## Formal notation

Learn v(z,t,c) such that integrating the ODE from z_ctrl yields z_pert; trained with OT-CFM and dynamic intra-batch OT coupling of unpaired populations.

## Variants

- OT-CFM with minibatch optimal transport coupling (AlphaCell).
- Discrete neural OT maps (CellOT) and direct flow in PCA space (CellFlow) — partial steps toward continuity.

## Comparison

Opposes discrete-jump models: latent-arithmetic vector shifts ([[foundations/scgen-perturbation-integration]]) and set-based distribution matching ([[foundations/state-perturbation-prediction-model]]). Built on [[foundations/flow-matching-generative-modeling]] and [[foundations/optimal-transport-sinkhorn]].

## When to use

- When perturbation effects are subtle and easily confounded by noise (e.g., Sci-Plex).
- When non-linear, population-coherent dynamics matter more than endpoint matching.

## Known limitations

- Deterministic fields cannot represent stochastic/multimodal responses.

## Open problems

- Stochastic flow formulations for heterogeneous responder populations.

## Key papers

- [[papers/towards-building-world-model-simulate-perturbation]]

## My understanding

The cleanest mechanistic rationale in the paper for why AlphaCell beats discrete-mapping baselines on DE recall ([[claims/alphacell-leads-de-overlap-accuracy-macro]]): coherent flow filters incoherent noise. The flip side — inability to model multimodal outcomes — is a real limitation.
