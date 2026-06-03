---
title: "Continuous density transport (CDT)"
aliases:
  - continuous density transport
  - CDT
tags: []
maturity: emerging
key_papers:
  - pseudodynamics-reconstructing-population-dynamics-time-resolved
first_introduced: "Zheng et al. 2025 (pseudodynamics+)"
date_updated: 2026-06-03
related_concepts:
  - population-aware-single-cell-flux-modeling
  - megakaryocyte-biased-balanced-haematopoiesis-temporal-shift
---

## Definition

Continuous density transport (CDT) is a downstream analysis built on the dynamic parameters learned by population-aware flux modelling. For each cell, CDT uses the learned velocity field `v(s,t)` to simulate a state-transition trajectory, then combines the drift term with the trajectory and modulates by the state-specific growth rate `g(s,t)` to estimate, at each time interval, the density outflow to target states, the inflow from source states, and the retained density — producing a per-cell transport map of how its cell mass redistributes among progenies along the differentiation trajectory.

## Intuition

Where optimal transport gives a single coupling between two timepoints, CDT traces, step by step and in absolute density (cell-mass) units, how one cell's descendants spread across downstream fates — turning the learned dynamics into an interpretable, quantitative flux map per cell.

## Formal notation

For trajectory `[s₁,…,sₙ]` over `[t₁→tₙ]`, on each interval `[tⱼ,tⱼ₊₁]` estimate outflow `u_{i→i+1}`, inflow `u_{i−1→i}`, and retention `u_{i→i}` from the drift term, scaled by `g(s,t)`; aggregating progeny density by cell type yields the transport map / Sankey of fate output.

## Variants

- Applied at single-cell level (per MEP) and aggregated by cell type.
- Combined with CellRank velocity-kernel fate probabilities for directionality.

## Comparison

- vs optimal-transport coupling: CDT is continuous-time, per-cell, and expressed in absolute density rather than a normalized probabilistic coupling.

## When to use

- To quantify lineage output bias and its temporal evolution from learned flux parameters (e.g. MEP → Meg vs Ery output over time).

## Known limitations

- Inherits the embedding-level interpretability limits of the underlying model.
- Cell-type labels on simulated states come from nearest-neighbour transfer, which can be coarse.

## Open problems

- Quantitative benchmarking of CDT maps against ground-truth lineage-tracing flux.

## Key papers

- [[papers/pseudodynamics-reconstructing-population-dynamics-time-resolved]] — introduces CDT and applies it to MEP fate output.

## My understanding

CDT is the analysis that makes the population-aware model pay off biologically: it converts abstract `v`/`g`/`D` fields into a readable, cell-by-cell account of where cell mass flows.
