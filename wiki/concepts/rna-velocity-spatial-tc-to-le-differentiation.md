---
title: "RNA velocity-inferred TC→LE differentiation hierarchy in solid tumors"
aliases:
  - RNA velocity TC to LE
  - scVelo cancer differentiation TC LE
  - spatial RNA velocity tumor
  - TC to LE differentiation hierarchy
  - cancer cell developmental trajectory ST
  - tumor differentiation hierarchy RNA velocity
  - spliced unspliced spatial cancer
  - tumor velocity trajectory
tags: [RNA-velocity, spatial-transcriptomics, EMT, differentiation, OSCC]
maturity: emerging
key_papers:
  - spatial-transcriptomics-reveals-distinct-conserved-tumor
first_introduced: "Arora & Cao et al. 2023 Nat Commun"
date_updated: 2026-05-22
related_concepts: []
---

## Definition
Application of scVelo (dynamical model) to spatially deconvolved cancer-cell spots reveals a reproducible developmental trajectory pointing from TC → transitory → LE, with vector-field confidence > 0.85 across spots and consistent direction at the per-patient level.

## Intuition
RNA velocity converts a snapshot transcriptome into a directional flow. The flow's direction matches the prognostic asymmetry (LE = worse) and the CSC state assignment (eCSC → mCSC), suggesting a coherent picture: cancer cells acquire LE biology by progressively shedding epithelial identity.

## Variants
- Aggregated cross-sample trajectory (most stable)
- Per-patient trajectory (qualitatively consistent)
- Driver-gene focused view (CSTA, IGHG3, etc. as top differentially spliced loci)

## Comparison
Pseudotime-only methods (Monocle3, Slingshot) give an order but not a direction; RNA velocity adds directionality. Compared to lineage tracing, velocity is short-horizon and biophysics-based, so it gives "trend" rather than "ground truth".

## When to use
- Predicting where cells in a tumour are heading short-term
- Identifying candidate driver genes whose splicing dynamics define a transition
- Hypothesising which manipulations could reverse the TC → LE flow

## Known limitations
- Velocity assumes consistent splicing kinetics across states
- Spatial spots aggregate multiple cells, blurring per-cell velocity
- Aggregating across patients risks averaging away patient-specific dynamics

## Open problems
- Calibrating short-horizon velocity against multi-day lineage tracing
- Joint spatial-temporal velocity models for ST time courses

## Key papers
- [[papers/spatial-transcriptomics-reveals-distinct-conserved-tumor]]

## My understanding
The TC → LE directionality is the linchpin that turns "TC and LE are different" into "drugs can push LE back toward TC". Once you accept the directionality, the in-silico drug-perturbation result becomes interpretable as state reversal.
