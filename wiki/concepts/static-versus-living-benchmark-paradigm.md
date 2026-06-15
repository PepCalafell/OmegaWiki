---
title: "Static vs living benchmark paradigm"
aliases:
  - living benchmark paradigm
  - continuously updated benchmark
  - static benchmark snapshot
tags:
  - benchmarking
  - meta-science
  - reproducibility
maturity: active
key_papers:
  - defining-benchmarking-open-problems-single-cell
first_introduced: "Open Problems in Single-Cell Analysis (Luecken et al., Nat. Biotechnol. 2025)"
date_updated: 2026-06-15
related_concepts:
  - benchmark-self-assessment-bias
---

## Definition

The contrast between a **static benchmark** — a one-off study that freezes a snapshot of methods, datasets and metrics at publication time — and a **living benchmark**, a continuously updated platform where new methods, datasets and metrics can be added without re-publishing the benchmark.

## Intuition

Static benchmarks inevitably age: the field's state of the art moves on, but the recommendation embedded in the paper does not. A living benchmark treats evaluation as ongoing infrastructure rather than a publication event, keeping method recommendations current and reducing the proliferation of redundant, non-overlapping one-off benchmarks.

## Variants

- **Registered reports**: neutral by design but still static once published.
- **Living community platforms** (e.g. Open Problems): cloud-hosted, PR-driven, auto-evaluated, continuously re-ranked.

## Comparison

Against [[concepts/benchmark-self-assessment-bias]]: the living paradigm's main defence is independence of evaluation from method development plus continuous community participation, which counters both ageing and developer self-preferencing.

## When to use

When a field has a fast-growing tool population (e.g. >1,700 single-cell algorithms) and static benchmarks disagree because they share little data or metric overlap.

## Known limitations

- Requires sustained community and funding to stay alive.
- Maintainer-chosen metrics can implicitly favour certain method families.

## Open problems

How to govern metric quality and prevent platform-level bias as the task set grows.

## Key papers

- [[defining-benchmarking-open-problems-single-cell]] — introduces the living, community-guided Open Problems platform.

## My understanding

The genuinely reusable idea here, beyond single cell: evaluation is infrastructure, not a paper. Realised concretely by [[foundations/openproblems-benchmark]] and [[foundations/common-task-framework]].
