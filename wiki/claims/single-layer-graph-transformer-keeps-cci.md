---
title: "A single-layer graph transformer keeps GITIII's output traceable to neighbourhood features, preserving interpretability"
slug: single-layer-graph-transformer-keeps-cci
status: supported
confidence: 0.7
tags:
  - cell-cell-interaction
  - graph-transformer
  - interpretability
  - spatial-transcriptomics
domain: "spatial transcriptomics / methods"
source_papers:
  - identifying-spatial-single-cell-level-interactions
evidence:
  - source: identifying-spatial-single-cell-level-interactions
    type: supports
    strength: moderate
    detail: "Commentary stresses that the choice of a single graph-transformer layer makes the model's output directly traceable to the input features of the cell neighbourhood, preserving interpretability that is often lost in deeper networks."
conditions: "Design rationale stated by commentary authors; not an empirical interpretability benchmark."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

GITIII uses a single-layer graph transformer encoder by design: the single layer ensures that the model's output is directly traceable to the input features of the cell neighbourhood, preserving interpretability that is often lost in deeper networks.

## Evidence summary

Stated in [[papers/identifying-spatial-single-cell-level-interactions]] (p.146): "The choice of a single layer is crucial — it ensures that the model's output is directly traceable to the input features of the cell neighbourhood, preserving the interpretability that is often lost in deeper networks." This is a design-rationale claim. See [[concepts/cci-influence-tensor]] and [[foundations/gitiii-graph-transformer-cci-method]].

## Conditions and scope

Architectural-design assertion; the trade-off is reduced model depth/capacity in exchange for traceability.

## Counter-evidence

None recorded; whether a single layer sacrifices predictive accuracy is not quantified in the commentary.

## Linked ideas

None yet.

## Open questions

- Does the single-layer constraint cost predictive accuracy relative to deeper graph transformers? (requires primary paper)
</content>
