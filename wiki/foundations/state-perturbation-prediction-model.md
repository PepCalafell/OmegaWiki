---
title: "STATE — set-based foundation model for perturbation prediction"
slug: state-perturbation-prediction-model
domain: methods / single-cell
status: mainstream
aliases:
  - STATE
  - State model
first_introduced: "Adduri et al. 2025 bioRxiv (State)"
date_updated: 2026-05-28
source_url: "https://www.biorxiv.org/content/10.1101/2025.06.26.661135"
---

## Definition

STATE is a foundation model for predicting cellular responses to perturbations across diverse contexts. It uses set-based attention over populations of cells and a Maximum Mean Discrepancy (MMD) objective to align predicted and observed population distributions, bypassing explicit per-cell-type embedding tokens.

## Intuition

Instead of predicting one cell at a time, treat a perturbation as a transformation of a whole set/distribution of cells, and train so the predicted population statistics match the real perturbed population.

## Formal notation

Set-transformer encoder over cell populations; population-level loss via MMD between predicted and observed perturbed distributions.

## Key variants

- Context-conditioned population mapping across datasets/modalities.

## Known limitations

- MMD distribution matching produces discrete population jumps without individual continuous dynamics; reported to extrapolate poorly to disjoint manifold regions occupied by entirely unseen cell types (near-random zero-shot correlation in AlphaCell's benchmarks).

## Open problems

- Continuous per-cell dynamics; robust zero-shot transfer to unobserved lineages.

## Relevance to active research

The principal competitor in AlphaCell's zero-shot evaluation; because it is token-free it is one of the few baselines architecturally able to attempt unseen-lineage prediction, making it the key comparison for [[concepts/cell-type-zero-shot-perturbation-generalization]].
