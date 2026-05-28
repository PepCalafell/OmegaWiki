---
title: "Discrete learnable cell-type embeddings structurally preclude zero-shot prediction on unseen lineages"
slug: discrete-cell-type-embeddings-structurally-preclude
status: proposed
confidence: 0.5
tags: [zero-shot, cell-type-embedding, STATE, architecture, perturbation]
domain: methods / single-cell
source_papers:
  - towards-building-world-model-simulate-perturbation
evidence:
  - source: towards-building-world-model-simulate-perturbation
    type: supports
    strength: moderate
    detail: "Quote (p.15): 'most traditional perturbation models rely on learnable, discrete cell-type embeddings, a design choice that structurally precludes them from performing true zero-shot predictions on unobserved lineages without retraining. Only set-based foundation architectures like STATE, which bypass explicit cell-type tokens, are mathematically equipped to attempt this task.'"
conditions: "Applies to models with explicit per-cell-type embedding tokens."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

Models that encode cell identity via discrete learnable cell-type embeddings cannot perform true zero-shot prediction on unseen lineages without retraining; only token-free set-based architectures (e.g., STATE) or universal continuous embeddings (AlphaCell's Virtual Cell Space) can attempt it.

## Evidence summary

Argument in [[papers/towards-building-world-model-simulate-perturbation]]. Motivates [[concepts/cell-type-zero-shot-perturbation-generalization]] and the universal-manifold design [[concepts/virtual-cell-world-model]]. Competitor: [[foundations/state-perturbation-prediction-model]].

## Conditions and scope

Architectural argument about embedding design.

## Counter-evidence

None within paper.

## Linked ideas

## Open questions

- Could discrete-embedding models be retrofitted with a continuous cell-state encoder to enable zero-shot?
