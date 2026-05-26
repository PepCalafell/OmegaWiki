---
title: "Optimal transport (Sinkhorn-Knopp) — entropic-regularized OT for representation learning"
slug: optimal-transport-sinkhorn
domain: "methods / optimization / representation-learning"
status: mainstream
aliases:
  - Optimal transport
  - Sinkhorn-Knopp algorithm
  - entropic optimal transport
  - Sinkhorn distance
  - Cuturi optimal transport
  - Peyre Cuturi computational OT
  - earth mover distance
  - balanced optimal transport
  - unbalanced optimal transport
  - regularized OT
first_introduced: "Cuturi 2013 NeurIPS; Peyré & Cuturi 2019 (Computational Optimal Transport)"
date_updated: 2026-05-26
source_url: ""
---

## Definition

Optimal transport (OT) computes the minimum-cost coupling between two probability distributions given a ground-cost matrix. The Sinkhorn-Knopp algorithm solves an entropic-regularized variant in `O(n^2)` per iteration via alternating row/column normalization, producing differentiable transport plans suitable for end-to-end deep learning.

## Workflow

1. Define source and target marginals (e.g., uniform over batch cells and uniform over prototypes).
2. Compute a cost matrix (typically negative similarity between features and prototypes).
3. Apply Sinkhorn-Knopp iterations to project onto the equipartition polytope.
4. Use the resulting transport plan as soft cluster assignments.

## Strengths

- Differentiable, GPU-friendly.
- Enforces equipartition that prevents trivial cluster-collapse solutions.
- Unbalanced variants tolerate distribution mismatch.

## Known limitations

- Sinkhorn convergence sensitive to entropic regularization parameter `epsilon`.
- Standard balanced formulation can be too rigid when batch composition is uneven; relaxation is required for spatial domains that are slide-specific.

## Relevance to active research

OT/Sinkhorn-Knopp is the assignment mechanism inside SwAV-style self-supervision, including [[papers/novae-graph-based-foundation-model-spatial]] where a relaxed (unbalanced) variant enables native batch-effect correction across slides while permitting prototypes to remain unused on slides that genuinely lack a domain.
