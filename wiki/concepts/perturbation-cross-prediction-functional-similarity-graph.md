---
title: "Perturbation cross-prediction functional similarity graph"
aliases:
  - cross-prediction functional similarity graph
  - perturbation cross-prediction
tags:
  - crispr-screen
  - machine-learning
  - single-cell
  - perturbation
  - network-biology
maturity: emerging
key_papers:
  - integrated-time-series-analysis-high-content
first_introduced: "Traxler et al. 2025 Cell Systems"
date_updated: 2026-06-04
related_concepts: []
---

## Definition
A method for quantifying functional similarity between gene knockouts in a single-cell CRISPR screen by cross-prediction: a classifier predicts each cell's perturbation identity from its transcriptome after the cell's true knockout class has been removed from the training set. The frequency with which knockout A's cells are predicted as knockout B (and vice versa) defines an edge weight in a functional similarity graph of regulators.

## Intuition
If knocking out two different genes produces transcriptionally indistinguishable cells, the genes are functionally similar — even if they have no known physical interaction. Cross-prediction turns "confusability" between perturbation classes into a similarity measure, recovering pathway co-membership and revealing novel functional links.

## Formal notation
For knockout classes {K}, train a leave-one-group-out classifier; P(predict B | true A) averaged over cells gives directed edge weight w(A→B). Prune edges below a cutoff (e.g. 0.1). Symmetric/asymmetric structure and within-timepoint vs within-knockout similarity can be compared to separate regulator effects from temporal effects.

## Variants
Single-time-point graph (25 nodes) vs across-time-point graph (58 nodes, knockout×time as nodes); pruned trapezoid-edge visualization weighted by cross-prediction probability.

## Comparison
Complementary to STRING protein-protein interaction networks (>80% of recovered edges were STRING-supported) and to Mixscape clustering; uniquely surfaces functional similarities absent from both (e.g. Ep300-Smc1a-Myd88-Runx1).

## When to use
To organize a high-content single-cell CRISPR screen into an interpretable map of regulator relationships, especially across conditions/time points.

## Known limitations
Requires sufficient cells per knockout; inherits Mixscape's exclusion of weak-effect perturbations; novel edges need orthogonal validation.

## Open problems
Generalization to other cell types and to combinatorial perturbations.

## Key papers
- [[papers/integrated-time-series-analysis-high-content]] — introduces cross-prediction functional similarity graphs for macrophage regulator screens.

## My understanding
An elegant reuse of classifier confusion as a biological similarity signal; the within-timepoint vs within-knockout decomposition is a neat way to separate "what" from "when" in perturbation effects.
