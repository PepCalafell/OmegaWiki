---
title: "Population size confounds single-cell snapshot flux"
aliases: []
tags: []
maturity: active
key_papers:
  - pseudodynamics-reconstructing-population-dynamics-time-resolved
first_introduced: "Articulated for single-cell flux by Fischer et al. 2019; emphasized in Zheng et al. 2025"
date_updated: 2026-06-03
related_concepts:
  - population-aware-single-cell-flux-modeling
  - time-dependent-flux-parameters-long-timecourse
---

## Definition

The principle that single-cell snapshots taken at successive timepoints cannot, on their own, separate genuine cell-state movement (differentiation/migration) from changes in overall population size. Because sequencing captures relative composition rather than absolute cell numbers, an apparent flux between states can reflect proliferation or death rather than directed transition — so trajectory methods that ignore total population size can systematically misattribute the cause of density change.

## Intuition

If a progenitor compartment shrinks in a UMAP between two timepoints, that could mean cells differentiated away (migration) *or* that the compartment stopped dividing while others expanded (a population-size effect). Without knowing absolute cell counts, the two are indistinguishable.

## Formal notation

Observed snapshots give a normalized density `û(s,t)` (sums to 1); the true unnormalized density is `u(s,t) = Nt·û(s,t)`. Inferring flux from `û` alone conflates `∂Nt/∂t` (growth/death) with `∇s·(v·u)` (drift).

## Variants

- Acute form in rapidly growing systems (embryonic development, regeneration), where population size changes fastest.

## Comparison

- Resolved by population-aware modelling ([[concepts/population-aware-single-cell-flux-modeling]]), which anchors density to measured `Nt`.

## When to use

- As the motivating rationale whenever absolute proliferation/death rates are inferred from snapshot scRNA-seq.

## Known limitations

- The confound only matters when population size genuinely changes; for near-stationary populations it is minor.

## Open problems

- Population-size measurement is itself noisy/indirect (flow cytometry, tissue counts), propagating uncertainty into flux estimates.

## Key papers

- [[papers/pseudodynamics-reconstructing-population-dynamics-time-resolved]] — frames this confound as the core motivation.

## My understanding

This is the conceptual crux: it is *why* population-aware modelling exists, not just a technical detail. Misreading proliferation as migration is a real failure mode of OT/velocity/flow-matching trajectory methods.
