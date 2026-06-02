---
title: "Pseudotime (trajectory inference)"
slug: pseudotime-trajectory-inference
domain: "methods / single-cell trajectory inference"
status: mainstream
aliases:
  - pseudotime
  - diffusion pseudotime
  - DPT
  - pseudotemporal ordering
first_introduced: "Trapnell et al. 2014 *Nat Biotechnol* (Monocle); Haghverdi et al. 2016 *Nat Methods* (diffusion pseudotime)"
date_updated: 2026-06-02
source_url: "https://doi.org/10.1038/nmeth.3971"
---

## Definition

Pseudotime is a scalar coordinate assigned to each cell that orders cells along a one-dimensional latent progression (e.g. differentiation), reconstructing a dynamic process from a static snapshot. Immature cells receive a low pseudotime that increases with maturity. It typically requires a user-defined root cell marking the start of the process.

## Intuition

Cells captured at a single time point represent many asynchronous stages of the same process. By embedding them on a manifold and measuring distance from a root along that manifold, one recovers a proxy for the (unobservable) real time each cell has progressed.

## Formal notation

Diffusion pseudotime defines DPT(x,y) as a distance in diffusion-map space derived from the transition matrix of a random walk over the cell–cell similarity graph; pseudotime of a cell is its DPT distance from the root.

## Key variants

- Diffusion pseudotime (DPT, Haghverdi 2016).
- Monocle / reversed graph embedding (Qiu 2017).
- Palantir absorption-probability pseudotime ([[palantir-pseudotime-fate]]).
- Slingshot minimum-spanning-tree lineages (Street 2018).

## Known limitations

- Assumes a unidirectional less-to-more-differentiated process.
- Requires a user-specified root cell; fails when the initial state is unknown.
- Struggles on complex, cyclic or convergent topologies.

## Open problems

- Rooting and directionality without prior knowledge.
- Calibrated uncertainty on the ordering.

## Relevance to active research

- The data view behind CellRank's PseudotimeKernel; see [[papers/cellrank-consistent-data-view-agnostic-fate]] and [[cellrank-fate-mapping]].
