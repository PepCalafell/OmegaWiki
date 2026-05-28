---
title: "GEARS — graph neural network for multigene perturbation prediction"
slug: gears-perturbation-graph-neural-network
domain: methods / single-cell
status: mainstream
aliases:
  - GEARS
first_introduced: "Roohani, Huang & Leskovec 2024 Nat. Biotechnol. (GEARS)"
date_updated: 2026-05-28
source_url: "https://www.nature.com/articles/s41587-023-01905-6"
---

## Definition

GEARS predicts transcriptional outcomes of single- and multi-gene perturbations by combining a gene co-expression / gene-ontology knowledge graph with a graph neural network. The prior graph lets it generalize to novel perturbation combinations, including genes not seen perturbed during training, by sharing information among related genes.

## Intuition

Genes that are related (co-expressed, same pathway) should have related perturbation effects. Encoding that relatedness as a graph lets the model infer the effect of perturbing a gene it has limited or no direct training signal for.

## Formal notation

GNN message passing over a gene knowledge graph to produce perturbation embeddings, added to a control cell embedding to predict the perturbed expression profile.

## Key variants

- GO-graph vs co-expression-graph priors.

## Known limitations

- Mechanistic constraint encodes discrete state transitions guided by the prior graph; performance bounded by graph quality; degrades when extended naively to genome-wide outputs.

## Open problems

- Reducing dependence on prior-graph quality; modeling continuous dynamics rather than discrete jumps.

## Relevance to active research

A representative knowledge-graph / mechanistic-constraint baseline in AlphaCell's compositional generalization benchmark, illustrating the "discrete jump guided by prior graph" paradigm AlphaCell contrasts against continuous flow.
