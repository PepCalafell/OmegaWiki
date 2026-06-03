---
title: "pseudodynamics+ solves the single-cell advection-reaction-diffusion PDE without pseudotime discretization via a PINN"
slug: pseudodynamics-solves-single-cell-advection-reaction
status: weakly_supported
confidence: 0.7
tags:
  - methods
  - PINN
  - PDE
  - single-cell
  - population-dynamics
domain: "methods / single-cell genomics"
source_papers:
  - pseudodynamics-reconstructing-population-dynamics-time-resolved
evidence:
  - source: pseudodynamics-reconstructing-population-dynamics-time-resolved
    type: supports
    strength: strong
    detail: "PINN surrogate network + three behaviour networks parameterize g, v, D and solve the governing advection-reaction-diffusion PDE in high-dimensional diffusion-map space, integrated by NeuralODE; no pseudotime discretization needed."
conditions: "Requires a low-dimensional cell-state embedding and measured population size; demonstrated on mouse thymus, LARRY, and in vivo haematopoiesis datasets."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

pseudodynamics+ approximates the single-cell density with a physics-informed neural network and parameterizes growth, drift, and diffusion as neural behaviour functions, solving the advection-reaction-diffusion PDE on complex branching landscapes without reducing cell state to a 1D pseudotime axis.

## Evidence summary

Demonstrated across three datasets; the PINN+NeuralODE formulation (Eqs. 1–8) replaces the pseudotime discretization of pseudodynamics-v1, enabling multi-lineage modelling.

## Conditions and scope

Methodological capability claim; validated computationally, not against new ground-truth flux measurements.

## Counter-evidence

None within the paper; interpretability of rates is limited because input is an embedding, not gene expression.

## Linked ideas

## Open questions

- Robustness to embedding choice and density-estimator quality.
