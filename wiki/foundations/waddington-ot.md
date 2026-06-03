---
title: "Waddington-OT"
slug: waddington-ot
domain: "methods / single-cell trajectory / optimal transport"
status: mainstream
aliases:
  - Waddington-OT
  - WOT
  - optimal-transport developmental trajectories
first_introduced: "Schiebinger et al. 2019 *Cell* — Optimal-transport analysis of single-cell gene expression identifies developmental trajectories in reprogramming"
date_updated: 2026-06-03
source_url: "https://doi.org/10.1016/j.cell.2019.01.006"
---

## Definition

Waddington-OT reconstructs ancestor–descendant relationships between single-cell snapshots taken at consecutive timepoints by solving an (unbalanced) optimal-transport problem that finds the most energy-efficient coupling between the two distributions, optionally accounting for cell growth/death via local mass variation.

## Intuition

If cells move minimally in expression space between timepoints, the cheapest transport plan approximates the true flow of cells. The coupling gives, for each early cell, a distribution over likely descendants — a probabilistic lineage map from snapshots alone.

## Key variants

- Balanced vs unbalanced OT (growth-rate-aware).
- Entropic-regularized (Sinkhorn) solvers for scalability; see [[foundations/optimal-transport-sinkhorn]].
- Successors: moscot ([[foundations/moscot-multi-omic-optimal-transport]]) for large/multimodal data.

## Known limitations

- Static description: couples two timepoints but does not yield a continuous velocity field.
- Assumes minimal-cost movement; strong proliferation/death must be modelled explicitly.
- Neglects total tissue population size unless growth scores are supplied.

## Open problems

- Continuous-time, population-aware transport at single-cell resolution.

## Relevance to active research

- A foundational optimal-transport trajectory method cited as prior art by [[papers/pseudodynamics-reconstructing-population-dynamics-time-resolved]], which argues such couplings remain static and population-agnostic compared to its continuous, population-aware PDE framework.
