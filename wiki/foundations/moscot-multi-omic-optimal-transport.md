---
title: "moscot (multi-omics single-cell optimal transport)"
slug: moscot-multi-omic-optimal-transport
domain: "methods / single-cell trajectory / optimal transport"
status: mainstream
aliases:
  - moscot
  - multi-omics optimal transport
first_introduced: "Klein et al. 2025 *Nature* — Mapping cells through time and space with moscot"
date_updated: 2026-06-03
source_url: "https://doi.org/10.1038/s41586-024-08453-2"
---

## Definition

moscot is a scalable optimal-transport framework for single-cell genomics that unifies temporal, spatial, and multimodal mapping problems. Using low-rank and entropic OT solvers, it couples cells across timepoints, modalities, or spatial coordinates at atlas scale, generalizing Waddington-OT-style trajectory inference to millions of cells and multiple problem classes.

## Intuition

Many single-cell mapping tasks (lineage over time, spatial reconstruction, modality alignment) are instances of the same optimal-transport problem; moscot provides one efficient, composable toolkit for all of them.

## Key variants

- Temporal, spatial, and translation (multimodal) problems.
- Low-rank OT solvers for atlas-scale data.

## Known limitations

- Still a discrete coupling between observed states, not a continuous-time dynamical model.
- Population-size dynamics are not the primary modelling target.

## Open problems

- Integrating population-scale flux with OT couplings.

## Relevance to active research

- Cited as a modern optimal-transport trajectory method in the related-work framing of [[papers/pseudodynamics-reconstructing-population-dynamics-time-resolved]]; contrasts with the paper's continuous PDE / PINN approach. Builds on [[foundations/waddington-ot]] and [[foundations/optimal-transport-sinkhorn]].
