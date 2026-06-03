---
title: "Continuous disease-progression modeling"
aliases:
  - sample-level disease trajectory
  - continuous severity axis
first_introduced: "2025"
tags: [disease-progression, trajectory, case-control, reproducibility]
maturity: emerging
key_papers:
  - reconstructing-developmental-disease-progression-sample-level
date_updated: 2026-06-03
related_concepts: [sample-level-embedding]
---

## Definition

Continuous disease-progression modeling treats disease state as a position along one or more continuous axes inferred from molecular data, rather than as a discrete "case vs control" label. Samples are ordered along a pseudo-trajectory of progression, and downstream analyses (differential expression, abundance, cell-type prioritization) are run against the continuous coordinate.

## Intuition

Binary case/control labels assume every case is a homogeneous representative of the disease. Real cohorts are heterogeneous and the case/control threshold itself varies between studies. Modeling progression as a continuum recovers within-group structure, increases statistical power, and improves cross-study reproducibility.

## Formal notation

Embed samples (e.g. via [[sample-level-embedding]]), fit a [[principal-curve-fitting|principal curve]] or [[pseudotime-trajectory-inference|pseudotime]] over the embedding, assign each sample an arc-length progression score `τ_s`, then test gene/abundance changes as functions of `τ_s` (e.g. NB-GLM with `τ` as continuous predictor).

## Variants

- Pseudotime/diffusion-based ordering vs principal-curve ordering.
- Developmental analogue: "pseudostage" within and across nominal timepoints.

## Comparison

Contrasts directly with standard pseudobulk case-control DE ([[deseq2-differential-expression]]), which collapses continuous variation into binary groups and (in the scSLIDE Alzheimer analysis) replicated at only ~17% vs ~83% for the trajectory approach.

## When to use

Complex, heterogeneous conditions (Alzheimer's, COVID-19 severity) where a single binary label hides graded biology; development, where nominal timepoints hide within-stage progression.

## Known limitations

- Requires that a meaningful continuous axis exists and is identifiable from the data.
- Trajectory inference is a prediction needing independent validation (e.g. neuropathology scores).

## Open problems

- Distinguishing genuine progression axes from confounding technical gradients.

## Key papers

- [[reconstructing-developmental-disease-progression-sample-level]] — continuous trajectories for COVID-19, Alzheimer's, and zebrafish development.

## My understanding

The headline argument of scSLIDE: much of the irreproducibility in disease single-cell studies stems from forcing graded biology into binary labels. Validating an inferred molecular trajectory against an independent neuropathology score is the key piece of evidence that the continuum is real, not an artifact.
