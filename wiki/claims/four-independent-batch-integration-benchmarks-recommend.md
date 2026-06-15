---
title: "Four independent batch-integration benchmarks each recommend different optimal methods"
slug: four-independent-batch-integration-benchmarks-recommend
status: supported
confidence: 0.85
tags:
  - benchmarking
  - batch-integration
  - single-cell
domain: methods / benchmarking / single-cell
source_papers:
  - defining-benchmarking-open-problems-single-cell
evidence:
  - source: papers/defining-benchmarking-open-problems-single-cell
    type: supports
    strength: moderate
    detail: "Fig. 1a: four batch-integration benchmarks (Tran, Mereu, Luecken, Chazarra-Gil) span 19 methods and 18 metrics with little shared method–metric coverage."
conditions: "Specific to batch integration as of the surveyed publications (2020–2022)."
date_proposed: 2026-06-15
date_updated: 2026-06-15
---

## Statement

At least four published benchmarks of single-cell batch integration exist, each using different datasets and metrics and each suggesting a different optimal method.

## Evidence summary

"at least four benchmarks of batch integration methods exist, each of which uses different sets of datasets and metrics and suggests different optimal methods (Fig. 1a)" (p.1035). Figure 1a tabulates 19 methods × 18 metrics with mostly single-benchmark coverage of each method–metric combination.

## Conditions and scope

Batch integration specifically; the divergence is the flagship example of the broader low-overlap problem.

## Counter-evidence

The benchmarks target partly different data regimes, so divergent winners are not purely an artifact of non-standardization.

## Linked ideas

Concrete instance of [[concepts/benchmark-self-assessment-bias]]; the [[foundations/scib-benchmark-pipeline]] (Luecken 2022) is one of the four.

## Open questions

Which method wins under a single standardized batch-integration benchmark.
