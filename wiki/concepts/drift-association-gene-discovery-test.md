---
title: "Drift-association gene discovery test"
aliases:
  - drift-association test
  - drift-associating genes test
tags: []
maturity: emerging
key_papers:
  - pseudodynamics-reconstructing-population-dynamics-time-resolved
first_introduced: "Zheng et al. 2025 (pseudodynamics+)"
date_updated: 2026-06-03
related_concepts:
  - population-aware-single-cell-flux-modeling
---

## Definition

A gene-programme discovery method that ranks genes by their association with the inferred differentiation rate (drift) along a trajectory, rather than with pseudotime or clusters alone. It identifies the pseudotime window of maximal differentiation-rate change (the "drift-variable state") via the time derivative of the projected differentiation rate, performs differential expression within that window, and combines this with correlation of gene expression along the whole trajectory.

## Intuition

The places along a trajectory where cells differentiate fastest are where lineage-deciding transcriptional programmes should switch on or off. By anchoring the gene test to the *rate of state change* (a population-flux parameter) instead of just position, the method surfaces drivers/markers tied to the dynamics of commitment.

## Formal notation

Compute projected velocity `v(t)` per lineage, its numerical derivative `dv/dt` by finite differences; slide a window (default 30 pseudotime bins) to locate the steepest-slope region; run DE within it and intersect with trajectory-wide expression correlation.

## Variants

- Per-lineage, per-timepoint application (time-dependent rates allow stage-specific TF modules).

## Comparison

- vs standard pseudotime DE / trajectory association tests: uses the model-inferred differentiation rate (a flux parameter) as the anchor, not pseudotime coordinate alone.

## When to use

- To validate inferred differentiation rates against known lineage regulators, and to nominate stage-specific transcription-factor modules.

## Known limitations

- Operates on diffusion-map projections, so genes are associations, not established causal regulators.
- Sensitive to pseudotime binning and window length.

## Open problems

- Establishing regulatory causality for drift-associated genes.

## Key papers

- [[papers/pseudodynamics-reconstructing-population-dynamics-time-resolved]] — recovers Pf4/Gata1 (Mk), Klf1/Gata1 (Ery), Cebpa/Cebpe (Neu) and stage-specific TF modules.

## My understanding

A neat reuse of the flux parameters for gene discovery — the differentiation rate becomes a feature you can correlate expression against, which is conceptually different from clustering or pseudotime DE.
