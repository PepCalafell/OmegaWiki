---
title: "pseudodynamics+ identifies three proliferative bursts during thymocyte maturation"
slug: pseudodynamics-identifies-three-proliferative-bursts-during
status: weakly_supported
confidence: 0.65
tags:
  - thymocyte
  - T-cell-maturation
  - proliferation
  - growth-rate
domain: "haematopoiesis / immunology"
source_papers:
  - pseudodynamics-reconstructing-population-dynamics-time-resolved
evidence:
  - source: pseudodynamics-reconstructing-population-dynamics-time-resolved
    type: supports
    strength: moderate
    detail: "Applied to Kernfeld 2018 thymus scRNA-seq, pseudodynamics+ identified three waves of proliferative bursts (progenitor, Phase 2, DP), whereas pseudodynamics-v1 suggested only the first two and assigned decreasing growth toward DP."
conditions: "Mouse embryonic thymus E12.5–E19.5, ~48k cells."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

In embryonic thymocyte maturation, pseudodynamics+ resolves three distinct proliferative bursts (progenitor, Phase 2, and double-positive stages), one more than pseudodynamics-v1.

## Evidence summary

Model-inferred growth-rate profiles; the additional DP burst is independently corroborated by cell-cycle scoring (see related claim).

## Conditions and scope

Single thymus dataset; inference depends on the multi-dimensional diffusion-map model.

## Counter-evidence

pseudodynamics-v1 on the same data inferred only two waves with decreasing DP growth.

## Linked ideas

## Open questions

- Whether the three-wave pattern generalizes across thymus datasets.
