---
title: "Open Problems in Single-Cell Analysis — community benchmarking platform"
slug: openproblems-benchmark
domain: benchmarking-infrastructure
status: mainstream
aliases:
  - Open Problems
  - Open Problems in Single-Cell Analysis
  - openproblems.bio
  - OP single-cell benchmark
  - living benchmark platform
  - language-agnostic benchmark
first_introduced: "Luecken et al. 2024 / Open Problems consortium"
date_updated: 2026-05-21
source_url: "https://openproblems.bio/"
---

## Definition

Open Problems in Single-Cell Analysis is a community-maintained, extensible benchmarking platform that hosts reproducible, language-agnostic benchmarks for single-cell and spatial analysis tasks. Each task aggregates methods, datasets, and metrics into a continuously updated results page.

## Intuition

Standalone benchmark papers freeze a snapshot of the field. Open Problems instead provides a living benchmark — new methods, datasets, and evaluation metrics can be added without re-publishing, addressing the well-known "different benchmarks → different conclusions" reproducibility problem.

## Known limitations

- Adoption of a method into the platform requires non-trivial method-author effort to containerise their tool.
- Metrics chosen by the platform maintainers can implicitly favour certain method families.

## Relevance to active research

The Li et al. 2025 SVG benchmark deposits all 14 SVG methods, 50 simulated datasets, and 6 metrics into the Open Problems platform (`task_spatially_variable_genes`), making the benchmark continuously extensible by the community.
