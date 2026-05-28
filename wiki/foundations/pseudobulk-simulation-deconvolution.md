---
title: "Pseudobulk / pseudotissue simulation for deconvolution training"
slug: pseudobulk-simulation-deconvolution
domain: methods
status: mainstream
aliases:
  - pseudobulk simulation
  - pseudotissue generation
first_introduced: "2020"
date_updated: 2026-05-28
source_url: ""
---

## Definition

A training-data construction technique for supervised deconvolution: cells are sampled from single-cell reference data at randomly drawn proportions and their molecular profiles aggregated to synthesize a "pseudobulk" (or "pseudotissue") sample whose ground-truth cell-type composition is known by construction. Repeating yields a labelled training set mapping aggregate profile → proportion vector.

## Intuition

Real bulk tissue lacks ground-truth proportions, so supervised models cannot be trained on it directly. Simulating mixtures from single cells provides unlimited labelled examples, turning deconvolution into a standard supervised regression.

## Formal notation

For a proportion vector p ~ Uniform over cell types and total cell count N, sample N cells per type accordingly and aggregate profiles to form one pseudobulk; (profile, p) is one training pair.

## Key variants

- Adding artificial noise / unknown-cell perturbations to pseudobulk to improve robustness (as in DECODE stage 3).
- Dirichlet vs. uniform proportion sampling.

## Known limitations

- Simulated mixtures may not reflect real batch effects or unknown cell types, motivating downstream alignment/denoising steps.

## Open problems

Closing the gap between simulated training distributions and real tissue distributions.

## Relevance to active research

The standard training paradigm for deep-learning deconvolvers (Scaden, TAPE, DECODE); the realism of the simulation directly bounds achievable accuracy.
