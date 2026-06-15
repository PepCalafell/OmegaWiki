---
title: "Benchmark self-assessment bias"
aliases:
  - self-assessment bias
  - self-preferencing benchmark bias
  - developer-run benchmark bias
tags:
  - benchmarking
  - meta-science
  - bias
maturity: active
key_papers:
  - defining-benchmarking-open-problems-single-cell
first_introduced: "Common task framework literature (Donoho 2017); applied to single-cell by Luecken et al. 2025"
date_updated: 2026-06-15
related_concepts:
  - static-versus-living-benchmark-paradigm
---

## Definition

The systematic tendency for benchmarks implemented by the same group that introduces a method to favour that method — through dataset and metric selection, custom hyperparameter tuning, and bespoke data processing — inflating the apparent performance of the authors' newest models.

## Intuition

A developer who both builds a method and designs its benchmark has many degrees of freedom (which datasets, which metrics, which preprocessing) that, even without intent, drift toward configurations where their tool looks best. Across a field this produces benchmarks that disagree and recommendations that cannot be trusted at face value.

## Variants

- **Dataset/metric cherry-picking**: choosing evaluation conditions that highlight a tool's strengths.
- **Hyperparameter/preprocessing inflation**: tuning the new model's pipeline more carefully than baselines.

## Comparison

The structural antidote is neutral, third-party or community-run evaluation independent of method development — see [[concepts/static-versus-living-benchmark-paradigm]] and [[foundations/openproblems-benchmark]]. Registered reports mitigate it without requiring a hosted platform.

## When to use

When interpreting a benchmark authored by the developers of one of the compared methods, or when explaining why independent benchmarks of the same task reach different conclusions.

## Known limitations

Bias is a tendency, not a certainty; many developer-run benchmarks are careful and fair. The concept should not be used to dismiss results, only to weight them.

## Open problems

How to quantify the magnitude of self-assessment inflation, and how much neutral hosting actually reduces it versus registered reports.

## Key papers

- [[defining-benchmarking-open-problems-single-cell]] — motivates the Open Problems platform by this bias.

## My understanding

This is the core "why" of neutral benchmarking infrastructure: the problem is not bad faith but degrees of freedom. Directly supported by [[claims/method-developer-run-benchmarks-inflate-performance]] and [[claims/four-independent-batch-integration-benchmarks-recommend]].
