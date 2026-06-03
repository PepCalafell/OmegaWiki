---
title: "Principal Curve Fitting"
slug: principal-curve-fitting
domain: statistics
status: mainstream
aliases:
  - principal curve
  - principal curves
first_introduced: "1989"
date_updated: 2026-06-03
source_url: ""
---

## Definition

A principal curve is a smooth, one-dimensional curve that passes through the "middle" of a multivariate data cloud, generalizing the first principal component to a nonlinear setting. Each data point is projected onto the curve, and its arc-length position provides a continuous ordering.

## Intuition

Where a straight principal-component line is too rigid for curved data, the principal curve bends to follow the manifold, so the arc-length coordinate becomes a natural pseudo-progression score along the dominant axis of variation.

## Formal notation

The curve `f(λ)` is fit so that each point is the conditional mean of points projecting to it (self-consistency): `f(λ) = E[X | λ_f(X) = λ]`, alternating projection and smoothing steps.

## Key variants

- Joint principal curves fit over the first few diffusion or PCA components.

## Known limitations

- Sensitive to initialization and smoothing parameters; can fail on branched or looped structure.
- Assumes a single dominant one-dimensional trajectory.

## Open problems

- Robust extension to branching trajectories.

## Relevance to active research

scSLIDE fits a joint principal curve through the first two diffusion components of its sample-level density matrix to infer a continuous disease-progression pseudo-trajectory across donors (e.g. the Alzheimer severity axis validated against neuropathology CPS scores).
