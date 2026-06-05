---
title: "Cell-state deconvolution"
aliases:
  - cell state abundance estimation
tags: [deconvolution, cell-state, methods]
maturity: emerging
key_papers:
  - decode-deep-learning-based-common-deconvolution
  - multiomics-analysis-cxcl9-macrophages-immunotherapy-response
first_introduced: "2026"
date_updated: 2026-05-28
related_concepts: [universal-multiomics-deconvolution, intrinsic-vs-extrinsic-cell-state-determinants]
---

## Definition

Estimating the abundance of cell *states* (e.g., pseudotime positions, cell-cycle phases, drug-response time points) — rather than discrete cell *types* — within tissue-level data, by treating each state as a deconvolution target with its own reference signature.

## Intuition

Cell type answers "what cell is this"; cell state answers "what condition is it in." Many biological questions (differentiation, activation, division, apoptosis) are about shifting state distributions within a fixed type. Deconvolving states requires distinguishing signatures that differ along a continuum, often subtler than type differences.

## Formal notation

Discretize a continuous state variable (e.g., pseudotime ∈ [0,1] → k bins) and estimate the proportion vector over states from the tissue profile, using a single-cell reference annotated by state.

## Variants

- Pseudotime-state deconvolution (continuous trajectory binned into temporal labels).
- Cell-cycle-phase deconvolution (G1/S/G2).
- Drug-response time-point deconvolution.

## Comparison

MeDuSA recovers pseudotime-state abundances but requires a continuous-pseudotime reference, so it only applies to continuous (not discrete) states; a universal framework like DECODE handles both discrete and continuous state labels and works across omics.

## When to use

When the biological signal of interest is a shift in state distribution (activation, differentiation, treatment response) within tissue cohorts rather than a change in cell-type composition.

## Known limitations

State signatures can be highly consistent across cell types (cell-cycle phase signatures are shared between monocytes and melanoma), helping cross-type transfer but blurring type-specific state effects.

## Open problems

Resolving overlapping state continua; combining type and state deconvolution jointly.

## Key papers

- [[decode-deep-learning-based-common-deconvolution]] — demonstrates cell-state deconvolution across three omics.

## My understanding

State deconvolution is the more ambitious of DECODE's targets; the finding that cell-cycle signatures transfer across cell types is the mechanistically interesting part.
