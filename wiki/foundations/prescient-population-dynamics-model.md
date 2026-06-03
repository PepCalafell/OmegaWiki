---
title: "PRESCIENT"
slug: prescient-population-dynamics-model
domain: "methods / single-cell trajectory / generative dynamics"
status: mainstream
aliases:
  - PRESCIENT
  - potential-energy population dynamics
first_introduced: "Yeo, Saksena & Gifford 2021 *Nature Communications* — Generative modeling of single-cell time series with PRESCIENT enables prediction of cell trajectories with interpretable uncertainty"
date_updated: 2026-06-03
source_url: "https://doi.org/10.1038/s41467-021-23518-w"
---

## Definition

PRESCIENT models single-cell differentiation as diffusion in a learned potential-energy landscape, fitting a generative stochastic dynamical system to time-series scRNA-seq with cell proliferation weighting. Given an initial cell, it simulates forward trajectories (drift down the potential plus noise) to predict future states and fate distributions with uncertainty.

## Intuition

Waddington's epigenetic landscape is made quantitative: cells roll downhill in a learned potential while diffusing, so simulating many walkers yields probabilistic fate predictions and trajectory ensembles.

## Key variants

- Proliferation-weighted training to account for growth.
- Recurrent / neural drift parameterizations.

## Known limitations

- Trajectories are stochastic and can diverge into undefined regions of the embedding.
- Potential-landscape assumption may not hold for all systems.

## Open problems

- Coupling the learned dynamics to absolute tissue population sizes.

## Relevance to active research

- A benchmark baseline in [[papers/pseudodynamics-reconstructing-population-dynamics-time-resolved]]: PRESCIENT produced accurate but inherently stochastic LARRY trajectories (strong on W2 distance) while some cells diverged into undefined regions; pseudodynamics+ matched flow-matching methods on fate accuracy.
