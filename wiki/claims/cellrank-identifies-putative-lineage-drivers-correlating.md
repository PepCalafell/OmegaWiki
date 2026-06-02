---
title: "CellRank ranks putative lineage drivers by correlating gene expression with fate probabilities"
slug: cellrank-identifies-putative-lineage-drivers-correlating
status: supported
confidence: 0.8
tags:
  - trajectory-inference
  - cellrank
  - lineage-drivers
  - gene-expression
domain: "methods / single-cell trajectory inference"
source_papers:
  - cellrank-consistent-data-view-agnostic-fate
evidence:
  - source: papers/cellrank-consistent-data-view-agnostic-fate
    type: supports
    strength: moderate
    detail: "Putative drivers are genes whose GEX correlates with fate probability toward a terminal state; GAMs weighted by fate probability describe lineage-specific GEX trends. The link is correlational, not causal."
conditions: "Correlation-based; identifies candidates, not validated causal regulators."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

CellRank identifies **putative lineage drivers** by ranking genes according to the correlation between their expression and the fate probability toward a given terminal state, and fits **generalized additive models** (weighting each cell by its fate probability) to describe lineage-specific gene-expression trends over pseudotime.

## Evidence summary

- [[papers/cellrank-consistent-data-view-agnostic-fate]] (p.3–4, Fig.3f,g): drivers are "genes whose GEX correlates with fate probabilities"; e.g. ITGA2B and VWF as MEP/megakaryocyte-lineage drivers in CD34+ bone marrow.

## Conditions and scope

The driver assignment is **correlational, not causal** — the authors explicitly note CellRank "identifies putative drivers on the basis of correlation but misses causal links."

## Counter-evidence

Correlation can flag confounded or downstream genes; experimental validation is required to confirm regulators.

## Linked ideas

(none yet)

## Open questions

- Can causal driver inference (vs correlation) be integrated to reduce false positives?
