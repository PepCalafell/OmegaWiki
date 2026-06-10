---
title: "De novo designed conformational switch (LOCKR / hinge proteins, cs221)"
slug: lockr-de-novo-conformational-switch-hinge
domain: "protein design"
status: mainstream
aliases:
  - "LOCKR"
  - "designed hinge protein"
  - "cs221"
  - "effector-responsive conformational switch"
first_introduced: "Langan et al. 2019 Nature (LOCKR); Praetorius et al. 2023 Nature (hinge proteins)"
date_updated: 2026-06-10
source_url: "https://doi.org/10.1038/s41586-019-1432-8"
---

## Definition

A family of de novo designed proteins that interconvert between two defined conformational states (closed X / open Y), with the open state Y exposing a binding cleft for a designed effector peptide. The LOCKR (Latching Orthogonal Cage–Key pRotein) and later two-domain hinge designs (e.g. cs221) allow effector ("key") binding to be allosterically coupled to a large rigid-body or register-shift conformational change.

## Intuition

These are programmable molecular switches: an input (effector peptide) binds and changes the protein's shape, which can be coupled to an output (exposing/occluding another binding site, reconstituting an enzyme, etc.). They are the chassis onto which arbitrary binders are fused in facilitated-dissociation designs.

## Formal notation

State X (closed) ⇌ State Y (open, effector-bound). Effector koff from cs221 state Y ≈ 5 × 10⁻⁶ s⁻¹ (very tight). Transition X→Y via rigid-body hinge or one-heptad register shift.

## Key variants

- LOCKR cage–key system (Langan 2019)
- Hinge proteins cs221 / 3hb21 (Praetorius 2023) — closed/open two-domain switches
- Re-engineered "always-open-cleft" switches (this paper) that retain an open effector cleft in state X to allow induced-fit binding.

## Known limitations

- Conformational-selection-limited switches are slow when the bound target blocks the X→Y transition.
- Designing single sequences compatible with two distinct backbone states is a hard multi-state design problem.

## Open problems

- Generalizing fast, driven (induced-fit) switching to arbitrary fusion geometries.

## Relevance to active research

The designed hinge switch is the modular "force-generating" module fused to arbitrary binders in [[design-facilitated-dissociation-enables-timing-cytokine]] to create effector-controlled facilitated dissociation. Prior LOCKR-based biosensors operate by slow conformational selection, which that paper's facilitated-dissociation sensors outperform by ~70×.
