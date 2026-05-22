---
title: "scVelo — RNA velocity inference accounting for gene-specific dynamics"
slug: scvelo-rna-velocity
domain: methods/single-cell
status: mainstream
aliases:
  - scVelo
  - RNA velocity scVelo
  - generalized RNA velocity
  - spliced/unspliced ratio cell-fate inference
  - scVelo dynamical model
  - splicing kinetics single-cell
  - cell-fate transition vector field
  - cell trajectory RNA velocity
first_introduced: "Bergen 2020 Nat Biotechnol"
date_updated: 2026-05-22
source_url: "https://scvelo.readthedocs.io"
---

## Definition
scVelo extends La Manno et al.'s RNA velocity framework by modelling gene-specific transcription, splicing and degradation rates with a dynamical EM model, allowing recovery of latent time and future-state estimation for individual cells from spliced/unspliced mRNA ratios.

## Intuition
Newly transcribed mRNA appears in unspliced form first; the ratio of unspliced to spliced reads encodes the direction in which a cell's transcriptome is moving. Aggregating across thousands of cells reveals differentiation hierarchies.

## Key variants
- Stochastic model (steady-state assumption)
- Dynamical model (full generative kinetics, recommended)
- spatial-aware extensions used when ST spots replace single cells

## Known limitations
- Assumes consistent kinetic parameters per gene across cell states
- Mitochondrial and ambient-RNA contamination can flip velocity direction
- Performs poorly when the steady-state assumption is grossly violated (e.g. cycling-only populations)

## Open problems
- Joint velocity inference across spatial spots and time series
- Reliable confidence quantification beyond cosine-similarity proxies

## Relevance to active research
Used in cancer ST work (e.g. [[papers/spatial-transcriptomics-reveals-distinct-conserved-tumor]]) to infer TC→LE differentiation hierarchies in solid tumors.
