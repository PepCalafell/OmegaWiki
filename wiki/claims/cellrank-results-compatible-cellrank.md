---
title: "CellRank 1 results are compatible with CellRank 2 (same RNA-velocity inference, modulo API changes)"
slug: cellrank-results-compatible-cellrank
status: supported
confidence: 0.85
tags:
  - trajectory-inference
  - cellrank
  - software-versioning
  - reproducibility
domain: "methods / single-cell trajectory inference"
source_papers:
  - cellrank-consistent-data-view-agnostic-fate
evidence:
  - source: papers/cellrank-consistent-data-view-agnostic-fate
    type: supports
    strength: strong
    detail: "Methodological concepts for RNA-velocity-based fate inference are unchanged between v1 and v2; the two yield identical results given unchanged dependencies, but API/field-name changes may be required."
conditions: "Identical results require all other Python packages to remain unchanged; AnnData field/variable names may need updating."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

CellRank 1 analyses are **compatible with CellRank 2**: the methodological concepts for inferring cellular fate from RNA velocity are unchanged, so the two versions yield the same results as long as all other Python packages are held constant; only API-related variable/field-name changes in the AnnData object may be required.

## Evidence summary

- [[papers/cellrank-consistent-data-view-agnostic-fate]] (p.4): "the methodological concepts for inferring cellular fate from RNA velocity estimates with CellRank 1 are unchanged in CellRank 2 … the two versions will yield the same results as long as the analysis leaves all other Python packages unchanged."

## Conditions and scope

Numerical identity is conditional on a fixed dependency stack; migration requires updating API field names per the documentation.

## Counter-evidence

Upstream dependency drift (e.g. scVelo, numerics) can change results independent of CellRank itself.

## Linked ideas

(none yet)

## Open questions

- How robust is fate inference to upstream package version drift?
