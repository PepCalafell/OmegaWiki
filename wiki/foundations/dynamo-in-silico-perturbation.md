---
title: "Dynamo — vector-field reconstruction and in-silico genetic perturbation"
slug: dynamo-in-silico-perturbation
domain: methods/single-cell
status: mainstream
aliases:
  - Dynamo
  - dynamo-release
  - in silico perturbation single-cell
  - vector field perturbation
  - cell fate transition prediction
  - learned splicing vector field
  - dynamo cell-fate transition probability
  - in silico genetic perturbation cancer
first_introduced: "Qiu 2022 Cell"
date_updated: 2026-05-22
source_url: "https://dynamo-release.readthedocs.io"
---

## Definition
Dynamo reconstructs a continuous vector field over single-cell or spatial transcriptomic state space from RNA velocity, enabling closed-form cell-fate transition probabilities and in-silico perturbation predictions for individual genes or programs.

## Intuition
Given a learned vector field representing how cells move through transcriptional state space, knocking out or activating a gene shifts cells along the field; the resulting trajectory predicts the consequence of a real perturbation.

## Key variants
- Velocity-only vector field (no metabolic labelling)
- Metabolically-labelled RNA velocity (tscRNA-seq) for more accurate kinetics
- Spatial-aware perturbation over ST spots

## Known limitations
- Predictions are only as good as the underlying velocity estimates
- Long-range transitions extrapolate beyond observed manifold
- Requires careful interpretation of "perturbation strength" parameter

## Open problems
- Quantitative calibration of predicted vs. experimentally observed perturbation effects
- Combining perturbations across multiple genes consistently

## Relevance to active research
Used in [[papers/spatial-transcriptomics-reveals-distinct-conserved-tumor]] to identify drugs that reverse LE→TC transition probabilities in OSCC.
