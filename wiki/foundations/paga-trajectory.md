---
title: "PAGA — partition-based graph abstraction for trajectory inference"
slug: paga-trajectory
domain: "methods / single-cell / trajectory-inference"
status: mainstream
aliases:
  - PAGA
  - partition-based graph abstraction
  - Wolf PAGA
  - trajectory inference single-cell
  - PAGA graph
  - PAGA spatial domains
  - cluster connectivity graph
first_introduced: "Wolf et al. 2019 Genome Biology"
date_updated: 2026-05-26
source_url: ""
---

## Definition

PAGA constructs a coarse-grained graph over clusters (or spatial domains) summarising their connectivity, reconciling clustering with trajectory inference. Edge weights reflect the statistical confidence of transitions between groups based on nearest-neighbor structure.

## Strengths

- Scalable, robust to noise via cluster-level summarization.
- Provides both global topology and per-edge confidence.

## Known limitations

- Coarse — within-cluster dynamics are not represented.
- Sensitive to cluster definition.

## Relevance to active research

Applied to Novae spatial-domain assignments in [[papers/novae-graph-based-foundation-model-spatial]] to compare slide-architecture changes (e.g., nondiseased vs reactive lymph node: D500 germinal center connected to a single domain vs five domains).
