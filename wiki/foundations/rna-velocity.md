---
title: "RNA velocity"
slug: rna-velocity
domain: "methods / single-cell trajectory inference"
status: mainstream
aliases:
  - RNA velocity
  - spliced unspliced velocity
  - velocyto velocity
first_introduced: "La Manno et al. 2018 *Nature* — RNA velocity of single cells"
date_updated: 2026-06-02
source_url: "https://doi.org/10.1038/s41586-018-0414-6"
---

## Definition

RNA velocity infers the instantaneous rate and direction of change of a cell's transcriptional state by relating unspliced (nascent) and spliced (mature) mRNA abundances through a dynamical model of splicing. Because common single-cell assays capture both species, the time derivative of spliced counts can be estimated per gene, yielding a per-cell velocity vector that predicts the cell's near-future state.

## Intuition

An excess of unspliced mRNA for a gene means that gene is being upregulated (future spliced counts will rise); an excess of spliced over the steady-state expectation means downregulation. Aggregated over genes, this gives each cell an arrow in expression space pointing toward where it is heading.

## Formal notation

A simple model: du/dt = α − βu, ds/dt = βu − γs, where u = unspliced, s = spliced, α = transcription, β = splicing, γ = degradation rate. Velocity is ds/dt = βu − γs; the steady-state (γ) is fit per gene, and the residual gives velocity.

## Key variants

- Steady-state / deterministic model (velocyto, La Manno 2018).
- Dynamical model with full kinetics (scVelo, Bergen 2020).
- Deep generative model (veloVI, Gayoso 2024).
- Metabolic-labeling-based velocity (Dynamo, Qiu 2022).

## Known limitations

- Gene-structure biases: polyadenylation and splicing often co-occur, so most "unspliced" counts arise from internal priming rather than true nascent transcripts.
- Constant-kinetic-rate assumptions neglect gene–gene interactions, chromatin and protein layers.
- Preprocessing choices (intron counting) materially change results.

## Open problems

- Faithful kinetic models without simplistic steady-state assumptions.
- Reconciling velocity with orthogonal data views.

## Relevance to active research

- The data view behind CellRank's VelocityKernel; see [[papers/cellrank-consistent-data-view-agnostic-fate]] and the [[cellrank-fate-mapping]] framework.
- Closely tied to [[scvelo-rna-velocity]] and [[dynamo-in-silico-perturbation]].
