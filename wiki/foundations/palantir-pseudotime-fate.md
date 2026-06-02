---
title: "Palantir (pseudotime and fate probabilities)"
slug: palantir-pseudotime-fate
domain: "methods / single-cell trajectory inference"
status: mainstream
aliases:
  - Palantir
first_introduced: "Setty et al. 2019 *Nat Biotechnol* — Characterization of cell fate probabilities in single-cell data with Palantir"
date_updated: 2026-06-02
source_url: "https://doi.org/10.1038/s41587-019-0068-4"
---

## Definition

Palantir models differentiation as a Markov chain over a diffusion-map representation of the cell–cell similarity graph, computing a pseudotime and per-cell branch (fate) probabilities toward terminal states. Terminal states are defined as the intersection of extrema of the stationary distribution and the diffusion components.

## Intuition

Starting from a chosen early cell, Palantir treats progression as an absorbing random walk; the probability of being absorbed into each terminal region gives a continuous fate-probability profile, capturing lineage priming before overt commitment.

## Formal notation

Pseudotime is shortest-path / absorption distance on the diffusion-space graph; fate probabilities are absorption probabilities of the Markov chain into automatically detected terminal states.

## Key variants

- Used as a pseudotime source for downstream tools (e.g. it provides the pseudotime in CellRank's bone-marrow example).

## Known limitations

- Requires a user-specified start cell.
- Terminal-state detection assumes they lie at manifold extrema.

## Open problems

- Robustness on non-tree-like or convergent trajectories.

## Relevance to active research

- Contrasted with CellRank's GPCCA-based fate inference (CellRank decouples fate inference from the pseudotime source, whereas Palantir couples them); Palantir supplies the precomputed pseudotime in CellRank's CD34+ bone-marrow demo. See [[papers/cellrank-consistent-data-view-agnostic-fate]].
