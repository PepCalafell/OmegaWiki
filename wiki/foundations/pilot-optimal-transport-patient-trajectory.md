---
title: "PILOT (optimal-transport patient trajectory)"
slug: pilot-optimal-transport-patient-trajectory
domain: single-cell genomics
status: mainstream
aliases:
  - PILOT
first_introduced: "2024"
date_updated: 2026-06-03
source_url: ""
---

## Definition

PILOT is a method that computes sample-level (patient-level) distances from single-cell data using optimal transport (Wasserstein distance) between the cell-type composition distributions of samples, then derives patient trajectories and disease pseudotime from those distances.

## Intuition

Two patients are "close" if little mass must be moved to turn one's cellular distribution into the other's. Optimal transport makes this notion of distributional distance precise and feeds it into trajectory inference at the sample level.

## Formal notation

For samples i, j it computes the Wasserstein distance `W(P_i, P_j)` between their cell distributions over a ground metric on cell states, producing a sample-by-sample distance matrix.

## Key variants

- Compositional vs full-distribution ground costs.

## Known limitations

- Typically operates on predefined cell-type proportions or an unsupervised embedding, so subtle phenotype-linked state variation can be missed.
- Unsupervised distances may not surface weak disease-severity gradients.

## Open problems

- Incorporating phenotype supervision into the transport cost.

## Relevance to active research

PILOT is one of the existing sample-level embedding methods benchmarked against scSLIDE. On the SEA-AD severity task it failed to recover the continuous severity trajectory that scSLIDE's semi-supervised embedding captured.
