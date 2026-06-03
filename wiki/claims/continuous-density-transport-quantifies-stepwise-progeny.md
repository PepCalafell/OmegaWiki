---
title: "Continuous density transport quantifies stepwise progeny density redistribution"
slug: continuous-density-transport-quantifies-stepwise-progeny
status: weakly_supported
confidence: 0.65
tags:
  - methods
  - continuous-density-transport
  - cell-flux
domain: "methods / single-cell genomics"
source_papers:
  - pseudodynamics-reconstructing-population-dynamics-time-resolved
evidence:
  - source: pseudodynamics-reconstructing-population-dynamics-time-resolved
    type: supports
    strength: moderate
    detail: "CDT uses the learned velocity field to simulate per-cell trajectories, then combines the drift term and growth rate to estimate per-interval outflow, inflow, and retained density, yielding a per-cell transport map of cell mass redistribution among progenies."
conditions: "Requires the fitted v, g, D fields; demonstrated on the Meg–Ery bifurcation subset."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Continuous density transport (CDT) is a method, built on the learned dynamic parameters, that quantifies how each cell's density redistributes stepwise among its progenies along the differentiation trajectory in absolute cell-mass units.

## Evidence summary

Methodological contribution demonstrated by producing interpretable per-cell transport maps and Sankey-style fate-output quantification.

## Conditions and scope

Depends on the quality of the underlying fitted fields; cell-type labels via nearest-neighbour transfer.

## Counter-evidence

No quantitative benchmark of CDT against ground-truth lineage-tracing flux.

## Linked ideas

## Open questions

- Benchmarking CDT maps against clonal ground truth.
