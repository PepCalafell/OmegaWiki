---
title: "Single-cell snapshot trajectories confound cell flux with population-size changes"
slug: single-cell-snapshot-trajectories-confound-cell
status: supported
confidence: 0.8
tags:
  - single-cell
  - trajectory-inference
  - population-dynamics
  - conceptual
domain: "methods / single-cell genomics"
source_papers:
  - pseudodynamics-reconstructing-population-dynamics-time-resolved
evidence:
  - source: pseudodynamics-reconstructing-population-dynamics-time-resolved
    type: supports
    strength: moderate
    detail: "Paper argues observed trajectories are confounded by changes in overall population size, so proliferation/death changes can be misread as cellular migration; motivates population-aware modelling."
conditions: "Matters most in systems where total population size changes substantially over the time course."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Because single-cell sequencing reports relative composition rather than absolute cell numbers, snapshot-based trajectory inference cannot distinguish directed cell-state transition from changes in population size, risking misattribution of proliferation/death as migration.

## Evidence summary

Stated as the central motivation; consistent with prior population-dynamics literature (Fischer 2019). Conceptually sound and broadly accepted.

## Conditions and scope

General principle; negligible for near-stationary populations.

## Counter-evidence

None; the confound is a recognized limitation of OT/velocity/flow-matching methods.

## Linked ideas

## Open questions

- How much measurement noise in population size propagates into flux estimates.
