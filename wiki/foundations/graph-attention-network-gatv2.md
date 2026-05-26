---
title: "Graph Attention Network / GATv2 — attention-based graph neural network"
slug: graph-attention-network-gatv2
domain: "methods / graph-neural-networks / representation-learning"
status: mainstream
aliases:
  - GAT
  - GATv2
  - graph attention network
  - graph attention network v2
  - Velickovic GAT
  - Brody GATv2
  - dynamic attention GNN
  - attention-based message passing
  - attention pooling graph neural network
  - graph attention encoder
first_introduced: "Velickovic et al. 2018 ICLR (GAT); Brody, Alon & Yahav 2022 ICLR (GATv2)"
date_updated: 2026-05-26
source_url: "https://openreview.net/forum?id=F72ximsx7C1"
---

## Definition

Graph Attention Networks compute node representations by aggregating neighbor features weighted by learned attention coefficients. GATv2 (Brody et al. 2022) corrects a static-attention limitation of the original GAT by reordering the LeakyReLU / linear projection inside the attention computation, restoring full dynamic attention expressivity.

## Workflow

1. Node features `h_i` are linearly projected.
2. Pairwise attention scores `e_ij = LeakyReLU(a^T [W h_i || W h_j])` are computed for each edge (GATv2 swaps order of operations to be dynamic).
3. Scores are softmax-normalized over each node's neighborhood.
4. New node features are the attention-weighted sum of neighbors, optionally with multi-head attention.

## Strengths

- Edge-weight learning is data-driven and unconstrained.
- Multi-head attention provides regularization.
- Operates inductively (generalizes to unseen graphs at test time).

## Known limitations

- Quadratic memory in dense neighborhoods.
- Original GAT has static attention that does not depend on the query node — fixed in GATv2.

## Relevance to active research

GATv2 is the backbone encoder of [[papers/novae-graph-based-foundation-model-spatial]], where it encodes a cell's spatial neighborhood (local subgraph) into a panel-invariant spatial-context embedding before swapped-assignment self-supervised training.
