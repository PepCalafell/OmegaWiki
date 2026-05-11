---
title: "Unstimulated hypoxic MACs (iMAC1) paradoxically down-regulate p65-bound genes, suggesting incomplete inflammatory differentiation in absence of LPS"
slug: imac1-paradoxical-down-p65-bound-genes
status: weakly_supported
confidence: 0.6
tags:
  - iMAC1
  - p65
  - paradox
  - inflammatory-suppression
  - macrophage-differentiation
  - context-dependency
domain: "immunology"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: moderate
    detail: "GSEA of p65-only-bound genes across MAC conditions (Calafell 2024 Fig. 4H). iMAC1 shows significant DOWN-regulation of p65-bound genes — opposite of mMAC1 (which up-regulates). Authors interpret as inflammatory suppression of unstimulated hypoxic MACs, possibly reflecting incomplete differentiation in low-O2."
conditions: "iMAC1 vs iMAC21 GSEA; p65-only peak set."
date_proposed: 2026-05-11
date_updated: 2026-05-11
---

## Statement

Unstimulated hypoxic MACs (iMAC1) show significant *down*-regulation of p65-bound genes — the opposite of the *up*-regulation seen in LPS-activated mMAC1. The authors interpret this as a paradoxical inflammatory suppression of resting hypoxic MACs, possibly stemming from incomplete differentiation in the low-O₂ environment. The implication is that hypoxia is *not uniformly* pro-inflammatory — context (activation state) flips the sign.

## Evidence summary

- GSEA on p65-only-bound gene set across conditions (Calafell 2024 Fig. 4H).
- Authors explicitly call this out as a paradox (p.8).

## Conditions and scope

- iMAC1 vs iMAC21 specifically; not generalized to other unstimulated hypoxic immune cells.
- M-CSF MACs only.

## Counter-evidence

- The interpretation (incomplete differentiation) is plausible but not directly tested — iMAC1 differentiation markers, chromatin accessibility, or single-cell heterogeneity could resolve.

## Linked ideas

- Sub-thesis for HypoxiaVERSE: hypoxia + activation = immunogenic; hypoxia alone = suppressive. Activation state is a binary co-axis.
- Reconciles competing literature on hypoxia / TAM immunology.

## Open questions

- Mechanistic basis: is iMAC1 down-regulating p65 binding, p65 cofactor binding, or downstream gene expression machinery?
- Whether re-oxygenation of iMAC1 followed by LPS recovers the mMAC1 program.
- Single-cell heterogeneity within iMAC1.
