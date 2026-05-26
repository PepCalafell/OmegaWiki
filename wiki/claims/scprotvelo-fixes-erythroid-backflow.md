---
title: "scProtVelo recovers correct erythroid directionality where standard scVelo produces the previously reported Late→Early Eryth backflow"
slug: scprotvelo-fixes-erythroid-backflow
status: supported
confidence: 0.85
tags: [scProtVelo, scVelo, RNA-velocity, erythroid, trajectory-inference, methodological]
domain: methods / trajectory inference
source_papers:
  - mapping-early-human-blood-cell-differentiation
evidence:
  - source: mapping-early-human-blood-cell-differentiation
    type: supports
    strength: strong
    detail: "Quote (p.8): 'applying the standard RNA velocity workflow to the scRNA-seq cells of the erythroid trajectory resulted in the previously reported erroneous backflow in velocity vectors from Late to Early Erythroid progenitors (10, 11)… Also, judging individual proposed cell to cell transitions by whether they coincide with an increase in pseudotime consolidates higher accuracy in trajectory inference based on translation modeling than on RNA velocity (fig. S25, E to I).'"
conditions: "scVelo on the same erythroid scRNA-seq vs scProtVelo on integrated mRNA+protein."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

The erythroid trajectory backflow artifact that has plagued scVelo can be resolved by switching to scProtVelo with protein-aware translation dynamics — demonstrating a tangible biological win from multi-omics velocity.

## Evidence summary

Direct comparison of cell-to-cell transition accuracy via pseudotime concordance. Reported in [[papers/mapping-early-human-blood-cell-differentiation]] (fig. S25 E-I).

## Conditions and scope

Erythroid trajectory specifically; pseudotime-based ground truth.

## Counter-evidence

Pseudotime as ground truth may not be neutral — but trajectory accuracy is consistently higher across the metrics shown.

## Linked ideas

## Open questions

- Whether scProtVelo equally outperforms scVelo on trajectories without prior pseudotime / where pseudotime itself is uncertain.
