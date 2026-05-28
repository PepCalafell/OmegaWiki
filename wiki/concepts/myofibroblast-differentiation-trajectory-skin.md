---
title: "Myofibroblast differentiation trajectory in human skin (F1/F2 → F6 → F7)"
aliases:
  - skin myofibroblast trajectory
  - fibroblast-to-myofibroblast transition
tags:
  - skin
  - myofibroblast
  - trajectory
  - rna-velocity
  - wound-healing
  - fibrosis
maturity: emerging
key_papers:
  - single-cell-spatial-genomics-atlas-human
first_introduced: "Steele et al., Nature Immunology 2025"
date_updated: 2026-05-28
related_concepts:
  - "[[concepts/inflammatory-myofibroblast-il11-mmp1-intermediate-state]]"
  - "[[concepts/harmonized-skin-fibroblast-subtype-atlas-f1]]"
---

## Definition

A predicted differentiation scheme in which terminal F7 myofibroblasts arise via two trajectories: directly from the F2 universal lineage, and from F1 superficial fibroblasts transitioning through an intermediate F6 inflammatory-myofibroblast state. The scheme is supported by PAGA/RNA-velocity/CellRank2 trajectory inference and a time-resolved human wound dataset.

## Intuition

Myofibroblasts are not a single endpoint reached one way: skin fibroblasts can converge on the terminal F7 state from different origins, with F6 acting as a transient inflammatory waypoint along one route.

## Formal notation

Trajectory 1: F2 universal → F7. Trajectory 2: F1 superficial → F6 inflammatory myofibroblast → F7 myofibroblast. Wound time-course: baseline (no myofibroblasts) → day 1 (rare F6) → day 7 (F6 predominant) → day 30 (F7 predominant).

## Variants

Consistent with mouse in vivo lineage-tracing showing both universal and tissue-specific fibroblast origins of myofibroblasts.

## Comparison

Extends mouse skin/lung myofibroblast-origin findings to human skin with temporal wound validation.

## When to use

When reasoning about how fibrosis/scarring stroma develops over time, or selecting candidate intermediate states for anti-fibrotic intervention.

## Known limitations

Trajectory inference cannot resolve multiple states converging to one phenotype; lineage plasticity makes single-trajectory claims tentative; no direct human lineage tracing.

## Open problems

Validating the F1→F6→F7 route in human tissue with orthogonal lineage methods; whether F6 is obligatory for F7.

## Key papers

- [[papers/single-cell-spatial-genomics-atlas-human]] — Steele et al., Nature Immunology 2025

## My understanding

The temporal human-wound data (F6 peaks at day 7, F7 by day 30) is the strongest line of evidence that F6 is a real intermediate, not just a parallel state.
