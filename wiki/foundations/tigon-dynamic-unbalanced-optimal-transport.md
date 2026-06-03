---
title: "TIGON"
slug: tigon-dynamic-unbalanced-optimal-transport
domain: "methods / single-cell trajectory / dynamic optimal transport"
status: mainstream
aliases:
  - TIGON
  - trajectory inference via dynamic unbalanced optimal transport
first_introduced: "Sha, Qiu, Zhou et al. 2024 *Nature Machine Intelligence* — Reconstructing growth and dynamic trajectories from single-cell transcriptomics data (TIGON)"
date_updated: 2026-06-03
source_url: "https://doi.org/10.1038/s42256-024-00794-x"
---

## Definition

TIGON (Trajectory Inference with Growth via Optimal-transport Networks) reconstructs continuous cell trajectories, growth rates, and velocity fields from time-series scRNA-seq by solving a dynamic unbalanced optimal-transport problem with neural networks, jointly inferring the velocity field and per-cell growth/death from snapshot distributions.

## Intuition

By solving the continuity (dynamic OT) equation describing how cellular density flows and changes mass over time, TIGON learns both where cells move and how the population grows — a continuous, mass-varying generalization of static OT couplings.

## Key variants

- Includes a Gaussian-mixture density estimator used internally.
- Reversible dimensionality reduction for gene-level interpretation.

## Known limitations

- Optimizes for reconstructing density change rather than predicting individual cell state, which can hurt fate-prediction accuracy.
- Internal GMM density estimator may miss localized mass accumulation/transition.
- Does not anchor to externally measured total tissue population size.

## Open problems

- Population-aware dynamics constrained by measured tissue size.

## Relevance to active research

- A benchmark baseline and density-estimator comparator in [[papers/pseudodynamics-reconstructing-population-dynamics-time-resolved]]: its GMM estimator achieved high correlation but missed Day-3 stem accumulation / Day-7 progenitor transition, and as a dynamic-OT method it underperformed at fate prediction. Related to [[foundations/optimal-transport-sinkhorn]] and [[foundations/waddington-ot]].
