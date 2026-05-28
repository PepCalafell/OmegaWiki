---
title: "In cell-type zero-shot, AlphaCell gives 3–6x DE Overlap Accuracy improvement and 20–50% Macro-F1 increase over STATE"
slug: zero-shot-alphacell-gives-fold-de
status: supported
confidence: 0.7
tags: [AlphaCell, zero-shot, DE-overlap, Macro-F1, STATE, quantitative]
domain: methods / single-cell
source_papers:
  - towards-building-world-model-simulate-perturbation
evidence:
  - source: towards-building-world-model-simulate-perturbation
    type: supports
    strength: moderate
    detail: "Quote (p.16): 'for mechanistic accuracy, AlphaCell exhibits a 3- to 6-fold improvement in Differentially Expressed (DE) Overlap Accuracy and a 20% to 50% increase in Macro-F1 scores' over STATE in the zero-shot setting."
conditions: "Cell-type zero-shot on OTF, Sci-Plex, Tahoe."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

For mechanistic accuracy under cell-type zero-shot, AlphaCell reports a 3–6× DE Overlap Accuracy improvement and a 20–50% Macro-F1 increase over STATE, indicating it pinpoints specific regulatory genes turning on/off in a novel cellular environment rather than matching only population statistics.

## Evidence summary

Reported in [[papers/towards-building-world-model-simulate-perturbation]] (Fig. 5). Concept: [[concepts/cell-type-zero-shot-perturbation-generalization]].

## Conditions and scope

Authors attribute STATE's failure to MMD set-based distribution matching being unable to extrapolate to disjoint manifold regions.

## Counter-evidence

Self-benchmarked; absolute DE accuracy magnitudes not stated in text.

## Linked ideas

## Open questions

- How does AlphaCell compare to STATE under independent zero-shot benchmarks?
