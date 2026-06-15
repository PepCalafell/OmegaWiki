---
title: "Independent single-cell benchmarks share less than 10% of datasets and metrics"
slug: single-cell-benchmarks-overlap-less-than
status: supported
confidence: 0.85
tags:
  - benchmarking
  - reproducibility
  - single-cell
domain: methods / benchmarking / single-cell
source_papers:
  - defining-benchmarking-open-problems-single-cell
evidence:
  - source: papers/defining-benchmarking-open-problems-single-cell
    type: supports
    strength: moderate
    detail: "Reported across single-cell topics as evidence that non-standardized benchmarks cannot give consistent guidance."
conditions: "Across single-cell topics surveyed; figure is an aggregate, not a single measurement."
date_proposed: 2026-06-15
date_updated: 2026-06-15
---

## Statement

Independent benchmarks of the same single-cell task typically overlap in less than 10% of their datasets and metrics, producing inconsistent method recommendations.

## Evidence summary

"datasets and metrics typically have less than 10% overlap between benchmarks" (p.1035), illustrated by four batch-integration benchmarks each suggesting different optimal methods (Fig. 1a). Low overlap is the concrete diagnosis behind the platform's standardization motivation.

## Conditions and scope

Aggregate observation across single-cell topics; magnitude varies by task. Low overlap reflects both legitimate scope differences and a lack of shared standards.

## Counter-evidence

Some overlap differences are intentional (benchmarks targeting different data regimes), so not all non-overlap is a reproducibility failure.

## Linked ideas

Supports [[concepts/benchmark-self-assessment-bias]] as a structural cause of divergent conclusions.

## Open questions

Whether a shared dataset/metric core would actually reconcile the divergent rankings.
