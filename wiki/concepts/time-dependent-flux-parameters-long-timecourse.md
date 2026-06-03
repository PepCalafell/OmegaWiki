---
title: "Time-dependent flux parameters over long time courses"
aliases:
  - time-dependent dynamic parameters
  - time-sensitive flux rates
tags: []
maturity: emerging
key_papers:
  - pseudodynamics-reconstructing-population-dynamics-time-resolved
first_introduced: "Zheng et al. 2025 (pseudodynamics+)"
date_updated: 2026-06-03
related_concepts:
  - population-aware-single-cell-flux-modeling
  - megakaryocyte-biased-balanced-haematopoiesis-temporal-shift
---

## Definition

The principle that, over long biological time courses, the dynamic parameters governing cell flux — growth `g`, differentiation/drift `v`, and diffusion `D` — are themselves functions of time, not constants. Modelling them as time-dependent (rather than fixed) is necessary to fit systems whose behaviour evolves, e.g. a tissue transitioning from a fast expansionary phase to slow homeostasis.

## Intuition

Fixed-rate models implicitly assume the system's "physics" never changes. Over 9 months of in vivo haematopoiesis it clearly does — early proliferative bursts give way to steady-state turnover. Letting rates vary with time both fits the data and prevents anomalies at early timepoints from corrupting the whole fit.

## Formal notation

Behaviour functions are `g(s,t), v(s,t), D(s,t)` with explicit dependence on `t ∈ [1,T]`; the static special case fixes them to `g(s), v(s), D(s)`.

## Variants

- Static-rate models (pseudodynamics-v1, Kucinski 2024 compartment ODEs) as the limiting case.

## Comparison

- Static models incorrectly assign high growth to quiescent HSCs; time-dependent models predict rare HSC division, matching known quiescence and low cell-cycle scores.

## When to use

- Any long-timescale in vivo system where dynamic behaviour is expected to shift (development → homeostasis, perturbation → recovery).

## Known limitations

- More parameters/flexibility → greater risk of overfitting; needs enough timepoints.
- Early-timepoint variation may mix true biology with perturbation artefacts (e.g. tamoxifen).

## Open problems

- Distinguishing genuine temporal rate changes from measurement/perturbation artefacts.

## Key papers

- [[papers/pseudodynamics-reconstructing-population-dynamics-time-resolved]] — shows static rates fail over 9 months and time-dependent rates are required.

## My understanding

This is the practical advance that makes long in vivo time courses tractable; it also enables the biological story of an evolving (MK-biased → balanced) system, which a static model could not represent.
