---
title: "Surface plasmon resonance (SPR)"
slug: surface-plasmon-resonance-spr
domain: "biophysics / methods"
status: mainstream
aliases:
  - "SPR"
  - "surface plasmon resonance"
first_introduced: "BIAcore commercialization, early 1990s"
date_updated: 2026-06-10
source_url: "https://en.wikipedia.org/wiki/Surface_plasmon_resonance"
---

## Definition

A label-free optical biosensing method that measures binding of molecules to a ligand immobilized on a metal (gold) sensor surface by detecting refractive-index changes near the surface as analyte accumulates. SPR yields real-time association and dissociation traces from which kinetic rate constants (kon, koff) and equilibrium affinity (Kd) are extracted.

## Intuition

You stick one binding partner on a chip, flow the other over it, and watch a real-time mass-accumulation signal. Because dissociation can be tracked under continuous buffer (or effector) flow, SPR directly measures off-rates — the central observable for facilitated dissociation.

## Formal notation

Response ∝ bound mass. Single-exponential dissociation: R(t) = R₀·e^(−koff·t). Association: dR/dt = kon·C·(Rmax−R) − koff·R. Kd = koff/kon.

## Key variants

- Single-cycle vs multi-cycle kinetics
- Bio-layer interferometry (BLI) as a related label-free alternative

## Known limitations

- Mass-transport limitation can distort fast kon measurements.
- Surface immobilization may perturb native binding; avidity artifacts with multivalent analytes.

## Open problems

- Accurately resolving very fast off-rates and transient ternary intermediates.

## Relevance to active research

SPR is the primary kinetic assay in [[design-facilitated-dissociation-enables-timing-cytokine]]: target immobilized on the chip, host then effector flowed over it to measure effector-induced acceleration of target off-rate (koff,T:H vs koff,T:HE) and to demonstrate the ternary complex as a kinetic intermediate.
