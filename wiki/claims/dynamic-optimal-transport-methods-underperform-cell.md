---
title: "Dynamic optimal-transport methods underperform at cell-state fate prediction"
slug: dynamic-optimal-transport-methods-underperform-cell
status: weakly_supported
confidence: 0.55
tags:
  - benchmark
  - optimal-transport
  - fate-prediction
domain: "methods / single-cell genomics"
source_papers:
  - pseudodynamics-reconstructing-population-dynamics-time-resolved
evidence:
  - source: pseudodynamics-reconstructing-population-dynamics-time-resolved
    type: supports
    strength: weak
    detail: "On the LARRY fate-prediction task, dynamic-OT methods (TrajectoryNet, MIOFlow, TIGON) underperformed, which the authors attribute to their goal of reconstructing density change rather than predicting individual cell state."
conditions: "Specific to the LARRY fate-bias accuracy metric."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Dynamic optimal-transport methods underperform at predicting individual cell fate, plausibly because they optimize for reconstructing population density changes rather than cell-state prediction.

## Evidence summary

Empirical on one benchmark plus a mechanistic rationale; the explanation is the authors' interpretation.

## Conditions and scope

Task-specific (fate accuracy); on W2 trajectory distance MIOFlow was competitive.

## Counter-evidence

MIOFlow performed well on the W2 trajectory metric, so the underperformance is metric-dependent.

## Linked ideas

## Open questions

- Whether retuning dynamic-OT objectives closes the fate-prediction gap.
