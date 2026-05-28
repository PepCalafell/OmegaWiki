---
title: "Compositional perturbation generalization"
aliases:
  - compositional generalization
  - compositional perturbation response prediction
tags: [perturbation, generalization, benchmark, cell-type, single-cell]
maturity: emerging
key_papers:
  - towards-building-world-model-simulate-perturbation
first_introduced: "Chuai et al. 2026 bioRxiv (AlphaCell)"
date_updated: 2026-05-28
related_concepts: []
---

## Definition

The task of predicting the response of a known cell type to a known perturbation in a novel, previously unobserved "cell type × perturbation" pairing. Both the cell type and the perturbation appear in training, but not together. It is the first of two generalization levels in cellular state-transition modeling (the second being cell-type zero-shot).

## Intuition

If a model has truly abstracted a perturbation into a generalized dynamic law, it should be able to apply that law to a different (but seen) cellular starting state. Failure indicates the model memorized specific cell–perturbation pairs.

## Formal notation

Train on pairs (c_i, p_j); test on held-out pairs (c_a, p_b) where c_a and p_b were each seen but the pair (c_a, p_b) was not.

## Variants

- Genetic-modality (OTF TF overexpression).
- Chemical-modality (Sci-Plex, Tahoe drug perturbations).

## Comparison

A weaker generalization demand than [[concepts/cell-type-zero-shot-perturbation-generalization]] (where the cell type itself is unseen). Both probe [[concepts/virtual-cell-world-model]] transferability.

## When to use

- Benchmarking whether a model abstracts perturbation mechanisms vs memorizes pairs.

## Known limitations

- Easier than true zero-shot; strong compositional scores do not guarantee unseen-lineage generalization.

## Open problems

- Standardized, independent compositional benchmarks across modalities.

## Key papers

- [[papers/towards-building-world-model-simulate-perturbation]]

## My understanding

A reasonable first-rung evaluation. AlphaCell's reported sweep of all baselines here ([[claims/alphacell-surpasses-all-baselines-compositional-generalization]]) is encouraging but self-benchmarked; the more interesting test is the zero-shot rung.
