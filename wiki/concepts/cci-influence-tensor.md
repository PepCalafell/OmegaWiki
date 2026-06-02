---
title: "CCI influence tensor"
aliases:
  - cell–cell interaction influence tensor
tags:
  - cell-cell-interaction
  - spatial-transcriptomics
  - interpretability
  - methods
maturity: emerging
key_papers:
  - identifying-spatial-single-cell-level-interactions
first_introduced: "2026"
date_updated: 2026-06-02
related_concepts:
  - ligand-receptor-free-cell-cell-interaction
  - subgraph-local-microenvironment-encoding
---

## Definition

The structured output of [[foundations/gitiii-graph-transformer-cci-method]]: a tensor that quantifies the impact of every neighbouring (sender) cell on the gene-expression state of a central (receiver) cell, indexed over central cells × neighbouring cells × genes. It is the single-cell-resolution, gene-resolved representation of inferred cell–cell interactions.

## Intuition

Rather than emitting a single scalar "interaction strength" per cell-type pair, the influence tensor records, for each individual receiver cell, how much each individual neighbour shifts each gene's expression. Because GITIII uses a single-layer graph transformer, every entry of the tensor is directly traceable back to the input neighbourhood features that produced it — preserving interpretability that deeper architectures lose.

## Formal notation

Conceptually, an entry `T[c, n, g]` ≈ the contribution of neighbour cell `n` to the expression of gene `g` in central cell `c`, learned by predicting `c`'s state from its neighbourhood subgraph ([[concepts/subgraph-local-microenvironment-encoding]]).

## Variants

Downstream reductions of the tensor power distinct analyses: aggregating over genes/cells gives CCI networks (sender→receiver matrices); per-cell influence vectors enable CCI-informed clustering; condition-wise comparison gives differential CCI strength.

## Comparison

Contrast with cell-type-level CCI scores ([[foundations/cellchat-cell-cell-communication]], [[foundations/cellphonedb-ligand-receptor]]), which collapse heterogeneity within a population to a single per-pair value. The influence tensor retains intracell-type variability and spatial specificity.

## When to use

When intracell-type interaction heterogeneity matters, when CCI-informed clustering is desired, or when comparing interaction strength across conditions at single-cell resolution.

## Known limitations

Entries are correlational influences, not causal effect sizes; the tensor inherits the small gene panel of the underlying imaging assay.

## Open problems

Calibrating the tensor against perturbation ground truth; integrating multi-omics so influence is resolved beyond transcriptomics.

## Key papers

- [[papers/identifying-spatial-single-cell-level-interactions]] — News & Views describing the influence tensor as GITIII's central output.

## My understanding

The influence tensor is the engineering payoff of the single-layer design: keeping the network shallow trades modelling capacity for a directly interpretable, fully resolved interaction object — useful precisely because the downstream value of CCI inference is interpretation, not prediction accuracy per se.
</content>
