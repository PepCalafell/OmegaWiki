---
title: "Benchmarks run by method-developing groups inflate the performance of their own newest models"
slug: method-developer-run-benchmarks-inflate-performance
status: supported
confidence: 0.8
tags:
  - benchmarking
  - bias
  - reproducibility
domain: methods / benchmarking
source_papers:
  - defining-benchmarking-open-problems-single-cell
evidence:
  - source: papers/defining-benchmarking-open-problems-single-cell
    type: supports
    strength: moderate
    detail: "Authors cite historical analyses (refs 6–8) that self-run benchmarks inflate new-model performance via custom hyperparameter and data-processing choices."
conditions: "General benchmarking finding, imported from ML and bioinformatics meta-analyses, applied to single-cell."
date_proposed: 2026-06-15
date_updated: 2026-06-15
---

## Statement

When benchmarks are implemented by the same groups that introduce new methods, evaluations tend to inflate the performance of the newest models through custom hyperparameter selection and data processing.

## Evidence summary

"when benchmarks are implemented by the same groups introducing new methods, the evaluations tend to inflate performance of the newest models via custom hyperparameter selection and data processing" (p.1035). Bespoke benchmarks also tend to choose datasets and metrics that highlight the authors' own tool. This is the core motivation for neutral, community-run evaluation.

## Conditions and scope

A meta-scientific tendency, not a deterministic rule; magnitude varies by field and by author practice. The platform's defence is independence of evaluation from method development.

## Counter-evidence

Not every developer-run benchmark is biased; registered reports and pre-specified protocols can mitigate it even without third-party hosting.

## Linked ideas

Definitional support for [[concepts/benchmark-self-assessment-bias]].

## Open questions

How much the Open Problems neutral-hosting model actually reduces measured inflation versus registered reports.
