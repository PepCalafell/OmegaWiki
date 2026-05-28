---
title: "AlphaCell models perturbation as a continuous deterministic vector field via Optimal Transport Conditional Flow Matching"
slug: alphacell-models-perturbation-continuous-deterministic-vector
status: supported
confidence: 0.9
tags: [AlphaCell, OT-CFM, flow-matching, optimal-transport, perturbation, vector-field]
domain: methods / single-cell
source_papers:
  - towards-building-world-model-simulate-perturbation
evidence:
  - source: towards-building-world-model-simulate-perturbation
    type: supports
    strength: strong
    detail: "Quote (p.13): 'we leverage Optimal Transport Conditional Flow Matching (OT-CFM) ... allowing the model to learn a deterministic vector field v(z,t,c) that transports a cell state embedding from its control state (zctrl) to its perturbed state (zpert) along the optimal trajectory in the Virtual Cell Space.'"
conditions: "Dynamic intra-batch optimal transport matches unpaired control/perturbed populations on-the-fly."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

AlphaCell's Flow Model treats a perturbation not as a discrete jump but as a continuous deterministic vector field v(z,t,c) learned via OT-CFM, transporting a control embedding to its perturbed embedding along an optimal geodesic in the Virtual Cell Space.

## Evidence summary

Reported in [[papers/towards-building-world-model-simulate-perturbation]]. Methods: [[foundations/flow-matching-generative-modeling]], [[foundations/optimal-transport-sinkhorn]]. Embodies concept [[concepts/perturbation-continuous-flow-versus-discrete-jump]].

## Conditions and scope

Perturbation signals injected via AdaLN + Joint Attention; Shared/Routed MoE in flow backbone.

## Counter-evidence

Deterministic field cannot capture stochastic/multimodal perturbation outcomes.

## Linked ideas

## Open questions

- How does deterministic flow handle bimodal responder/non-responder populations?
