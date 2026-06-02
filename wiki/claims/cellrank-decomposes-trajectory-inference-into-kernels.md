---
title: "CellRank decomposes fate mapping into kernels, estimators and analysis tools"
slug: cellrank-decomposes-trajectory-inference-into-kernels
status: supported
confidence: 0.85
tags:
  - trajectory-inference
  - single-cell
  - cellrank
  - software-architecture
domain: "methods / single-cell trajectory inference"
source_papers:
  - cellrank-consistent-data-view-agnostic-fate
evidence:
  - source: papers/cellrank-consistent-data-view-agnostic-fate
    type: supports
    strength: strong
    detail: "Protocol describes the framework as three modular parts; kernels and estimators are not predefined flavors, making analyses composable."
conditions: "Applies to the CellRank 2 framework; modules are interchangeable and subsets of the canonical workflow are allowed."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

CellRank divides cellular fate mapping into three modular stages: **kernels** that estimate cell–cell transition probabilities from a given data view, **estimators** that analyze the induced Markov chain, and **downstream analysis tools** (driver ranking, GEX trends, kernel/estimator comparison).

## Evidence summary

- [[papers/cellrank-consistent-data-view-agnostic-fate]] (p.2–4): "The CellRank framework naturally divides itself into three parts: kernels … estimators … and analysis tools." The specific flavors are not predefined, so analyses can use custom transition matrices or subsets of the workflow.

## Conditions and scope

Architectural claim about the software framework; the modularity is what enables data-view agnosticism.

## Counter-evidence

None known; this is a design description.

## Linked ideas

(none yet)

## Open questions

- How far can custom user kernels deviate before estimator assumptions (memorylessness) break?
