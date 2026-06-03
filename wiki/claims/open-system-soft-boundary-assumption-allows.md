---
title: "An open-system soft-boundary assumption lets DP thymocytes keep differentiating, unlike pseudodynamics-v1"
slug: open-system-soft-boundary-assumption-allows
status: weakly_supported
confidence: 0.65
tags:
  - methods
  - boundary-condition
  - open-system
  - thymocyte
domain: "methods / single-cell genomics"
source_papers:
  - pseudodynamics-reconstructing-population-dynamics-time-resolved
evidence:
  - source: pseudodynamics-reconstructing-population-dynamics-time-resolved
    type: supports
    strength: moderate
    detail: "pseudodynamics+ applies a soft boundary (loss penalizing mass outflow, λgrowth=0 open system) instead of v1's closed system with enforced zero drift at the last pseudotime bin, allowing DP cells to transition to unobserved downstream (single-positive) states."
conditions: "Biologically motivated by DP→SP differentiation and thymic egress; optimal boundary strength determined retrospectively."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

By modelling an open system with a soft boundary penalty rather than a hard closed boundary, pseudodynamics+ allows DP thymocytes to continue differentiating toward unobserved downstream states, better matching known DP→single-positive biology.

## Evidence summary

Methodological/biological argument; the open-system choice changes the inferred differentiation rate at the trajectory terminus relative to v1.

## Conditions and scope

Boundary-strength hyperparameter must be tuned retrospectively; choice is dataset-dependent.

## Counter-evidence

The authors note the optimal boundary constraint can only be determined after the fact.

## Linked ideas

## Open questions

- Principled, data-driven selection of the boundary penalty.
