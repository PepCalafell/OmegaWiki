---
title: "CellRank 2 generalizes fate mapping to a data-view-agnostic, multiview framework"
slug: cellrank-generalizes-fate-mapping-data-view
status: supported
confidence: 0.85
tags:
  - trajectory-inference
  - single-cell
  - cellrank
  - multiview
domain: "methods / single-cell trajectory inference"
source_papers:
  - cellrank-consistent-data-view-agnostic-fate
evidence:
  - source: papers/cellrank-consistent-data-view-agnostic-fate
    type: supports
    strength: strong
    detail: "CellRank 1 used RNA velocity + similarity only; CellRank 2 generalizes to any prior vector field of cellular change (pseudotime, stemness, experimental time, lineage tracing)."
conditions: "Requires at least one cell–cell transition matrix; any data view that yields directed cell-state change can be incorporated."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

CellRank 2 generalizes the original RNA-velocity-based framework into a **data-view-agnostic** trajectory-inference engine that can infer cellular fate from *any* prior vector field describing cellular change and combine complementary views (pseudotime, stemness/CytoTRACE, experimental time, lineage tracing), scaling to atlas-sized datasets.

## Evidence summary

- [[papers/cellrank-consistent-data-view-agnostic-fate]] (abstract, p.2): CellRank 1 "did not enable incorporating complementary data views such as experimental time points, pseudotime or stemness potential. To facilitate these and future views, CellRank 2 generalizes CellRank's trajectory inference framework to multiview single-cell data."

## Conditions and scope

The view must be expressible as (or convertible to) a cell–cell transition matrix via a kernel.

## Counter-evidence

None; the generality is bounded only by available kernels and data quality.

## Linked ideas

(none yet)

## Open questions

- Which emerging modalities (spatial, multi-omic) still lack a suitable kernel?
