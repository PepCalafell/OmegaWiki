---
title: "Flow matching / Optimal Transport Conditional Flow Matching (OT-CFM)"
slug: flow-matching-generative-modeling
domain: methods / generative-modeling
status: mainstream
aliases:
  - flow matching
  - conditional flow matching
  - OT-CFM
  - optimal transport conditional flow matching
  - CFM
first_introduced: "Lipman et al. 2022 (Flow Matching); Tong et al. 2023 (minibatch OT-CFM)"
date_updated: 2026-05-28
source_url: "https://arxiv.org/abs/2210.02747"
---

## Definition

Flow matching is a simulation-free objective for training continuous normalizing flows: instead of solving an ODE during training, the model regresses a time-dependent vector field that transports a source distribution to a target distribution along prescribed probability paths. Conditional Flow Matching (CFM) conditions paths on endpoints; Optimal Transport CFM (OT-CFM) couples source and target samples via (minibatch) optimal transport so the learned paths approximate OT geodesics — straighter trajectories that are cheaper to integrate.

## Intuition

Rather than learning "where to jump", learn "which direction to move at every point and time". Coupling control/perturbed samples by optimal transport gives the straightest, least-crossing paths, which are easy to integrate and stable to train.

## Formal notation

Learn v_θ(z,t) minimizing E‖v_θ(z_t,t) − u_t(z_t|z_0,z_1)‖² along interpolant z_t between coupled (z_0,z_1); OT coupling π chosen by minibatch optimal transport.

## Key variants

- Vanilla CFM vs OT-CFM (minibatch OT coupling).
- Conditional fields v(z,t,c) with external condition c (e.g., perturbation embedding).

## Known limitations

- Deterministic vector fields model unimodal transport; stochastic/multimodal targets need stochastic bridges.
- Minibatch OT is an approximation to full OT.

## Open problems

- Stochastic and multimodal flow formulations; better couplings beyond minibatch OT.

## Relevance to active research

Adopted as the "physics engine" of AlphaCell's Virtual Cell World Model to model perturbations as continuous flows; also used by CellFlow for single-cell trajectory modeling. Closely related to [[foundations/optimal-transport-sinkhorn]].
