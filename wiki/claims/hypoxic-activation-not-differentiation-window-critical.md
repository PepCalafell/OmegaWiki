---
title: "The activation step (LPS in hypoxia) — not the differentiation step — is the critical hypoxic window for the mMAC1 inflammatory program"
slug: hypoxic-activation-not-differentiation-window-critical
status: supported
confidence: 0.85
tags:
  - hypoxia
  - macrophage-differentiation
  - LPS-activation
  - swap-experiment
  - time-course
domain: "immunology"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: strong
    detail: "Swap experiments: MACs differentiated in 21% O2 transferred to 1% O2 2h before LPS recapitulate canonical hypoxic gene expression, and vice versa (Calafell 2024 fig. S2F-G). 2h is sufficient. The differentiation step's O2 environment is not required."
conditions: "Swap timing: 2h before LPS; differentiation in either O2 environment."
date_proposed: 2026-05-11
date_updated: 2026-05-11
---

## Statement

The hypoxic environment during the LPS activation step (not during the 5-day M-CSF differentiation step) is what's necessary and sufficient to drive the mMAC1 inflammatory program. A 2-hour pre-activation switch to hypoxia recapitulates the canonical hypoxic response.

## Evidence summary

- Swap design: MACs differentiated in 21% O₂ then switched to 1% O₂ 2h before LPS = "canonical hypoxia"-like response (Calafell 2024 fig. S2G).
- Mirror swap (1% → 21%) blunts the response.
- 2h before LPS is sufficient — short hypoxic window suffices.

## Conditions and scope

- Tested with 2h pre-activation swap; not tested with longer or shorter pre-activation hypoxia.

## Counter-evidence

- Earlier work (cited as ref 38 in the paper) emphasized differentiation-stage hypoxia; this paper extends and qualifies that view.

## Linked ideas

- Implies that the relevant in vivo hypoxic window is the *activation* (proximal-to-inflammation) phase — useful for in vivo modeling.
- Operationally simplifies model systems (don't need long hypoxic culture).

## Open questions

- The minimum hypoxic time before LPS that still rescues the response (<2h?).
- Whether the swap effect maps to HIF1α stabilization kinetics.
