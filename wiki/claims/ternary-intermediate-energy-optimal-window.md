---
title: "The ternary-intermediate energy must lie within an optimal window for fast facilitated dissociation"
slug: ternary-intermediate-energy-optimal-window
status: supported
confidence: 0.8
tags: [protein-design, strain-energy, kinetics, excited-states]
domain: protein design
source_papers:
  - design-facilitated-dissociation-enables-timing-cytokine
evidence:
  - source: design-facilitated-dissociation-enables-timing-cytokine
    type: supports
    strength: moderate
    detail: "The energy of the ternary intermediate must be neither too high (otherwise the facilitated pathway would not be faster) nor too low (otherwise the target would not dissociate); strain is tuned by switch–binder fusion geometry."
conditions: "Design reasoning supported by variant sampling and AF2-predicted deformations."
date_proposed: 2026-06-10
date_updated: 2026-06-10
---

## Statement

For facilitated dissociation to be fast, the energy of the strained ternary intermediate must fall within an optimal window — high enough to drive target release, but not so high that the facilitated pathway is no longer faster than spontaneous dissociation.

## Evidence summary

"the energy of this ternary intermediate must be neither too high (otherwise the facilitated dissociation pathway would not be faster) nor too low (otherwise the target would not dissociate)" (p.2). Strain was controlled by varying switch–binder fusion geometry; acceleration was maximized by moderately increasing ternary energy without making effector association rate-limiting.

## Conditions and scope

Designed AS1-derived systems; strain estimated via a spring model and AlphaFold2 deformation predictions.

## Counter-evidence

The optimal window is found empirically by sampling geometries rather than predicted a priori.

## Linked ideas

None yet.

## Open questions

Can the optimal-energy window be predicted quantitatively from structure? Linked: [[designed-protein-excited-states-kinetic-control]].
