---
title: "Population-aware single-cell flux modelling"
aliases:
  - pseudodynamics+
  - population-aware single-cell dynamics
tags: []
maturity: emerging
key_papers:
  - pseudodynamics-reconstructing-population-dynamics-time-resolved
first_introduced: "pseudodynamics-v1 (Fischer et al. 2019); high-dimensional PINN form: Zheng et al. 2025 (pseudodynamics+)"
date_updated: 2026-06-03
related_concepts:
  - population-size-confounds-snapshot-trajectory-flux
  - continuous-density-transport
  - time-dependent-flux-parameters-long-timecourse
---

## Definition

Population-aware single-cell flux modelling reconstructs tissue-scale cell dynamics by jointly fitting (i) the single-cell density landscape from time-series scRNA-seq and (ii) the measured total population size of the tissue over time. The cell density `u(s,t)` is scaled so its integral over cell-state space equals the measured `Nt`, and its temporal evolution is governed by an advection-reaction-diffusion PDE whose three behaviour functions — net proliferation `g(s,t)`, drift/differentiation velocity `v(s,t)`, and diffusion `D(s,t)` — are inferred as functions of cell state and time.

## Intuition

Standard trajectory methods describe *where* cells go but not *how many* there are, so they cannot tell proliferation/death apart from migration. Anchoring the density to an externally measured population size removes that ambiguity, letting the model attribute density change correctly to growth vs drift vs diffusion and report physiologically meaningful rates.

## Formal notation

`∂u/∂t = g(s,t)·u − ∇s(v(s,t)·u) + ∇s(D(s,t)∇s u)`, with `Nt = ∫_S u(s,t) ds`. The inverse problem estimates the behaviour functions `{g, v, D}` from disconnected density snapshots plus population sizes.

## Variants

- **pseudodynamics-v1** (Fischer 2019): 1D pseudotime axis, closed system, single lineage.
- **pseudodynamics+** ([[papers/pseudodynamics-reconstructing-population-dynamics-time-resolved]]): high-dimensional diffusion-map state space, PINN + NeuralODE, open/soft boundary, time-dependent rates, multi-lineage branching.

## Comparison

- vs optimal transport ([[foundations/waddington-ot]], [[foundations/moscot-multi-omic-optimal-transport]]): OT couples snapshots but is static and population-agnostic.
- vs flow-matching / generative dynamics ([[foundations/flow-matching-generative-modeling]], [[foundations/prescient-population-dynamics-model]]): predict state transitions but ignore absolute population size.
- vs dynamic OT ([[foundations/tigon-dynamic-unbalanced-optimal-transport]]): infers growth but targets density change, not measured tissue size.

## When to use

- When absolute tissue/population size matters (development, regeneration, in vivo homeostasis) and snapshot trajectories alone would confound proliferation with migration.

## Known limitations

- Requires an external measurement of total population size at each timepoint.
- Operates in a low-dimensional embedding, limiting per-gene interpretability of inferred rates.

## Open problems

- Linking inferred flux parameters back to gene-level regulatory programmes.
- Extending to systems dominated by influx rather than outflux.

## Key papers

- [[papers/pseudodynamics-reconstructing-population-dynamics-time-resolved]] — high-dimensional PINN formulation (pseudodynamics+).

## My understanding

The defining move is making density an *unnormalized* quantity whose integral is the measured population size — that single constraint is what turns trajectory inference into genuinely population-aware flux modelling.
