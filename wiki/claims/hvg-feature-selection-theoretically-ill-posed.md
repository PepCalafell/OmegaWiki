---
title: "HVG feature selection is theoretically ill-posed for zero-shot perturbation prediction"
slug: hvg-feature-selection-theoretically-ill-posed
status: proposed
confidence: 0.5
tags: [HVG, zero-shot, feature-selection, theory, perturbation]
domain: methods / single-cell
source_papers:
  - towards-building-world-model-simulate-perturbation
evidence:
  - source: towards-building-world-model-simulate-perturbation
    type: supports
    strength: moderate
    detail: "Quote (p.15): 'In a zero-shot setting, the transcriptional program of the perturbed state is unknown a priori; thus, it is impossible to predict which genes will exhibit high variance upon stimulation. Relying on HVGs ... assumes that the perturbation response is confined to pre-existing axes of variance, an assumption that fails whenever a perturbation activates quiescent pathways or induces novel cell states.'"
conditions: "Argument applies to zero-shot prediction of responses in unseen contexts."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

HVG-based feature selection is logically inconsistent for zero-shot perturbation prediction because the perturbed transcriptional program — hence which genes will be highly variable — is unknown a priori; HVGs from control/training data assume responses lie on pre-existing variance axes, failing when perturbations activate quiescent pathways.

## Evidence summary

Conceptual argument in [[papers/towards-building-world-model-simulate-perturbation]]. Contrast with [[foundations/hvg-selection-scrna]]; motivates [[concepts/genome-wide-cell-representation-versus-highly]].

## Conditions and scope

Theoretical/logical claim, not an empirical measurement.

## Counter-evidence

Some perturbation responses may in practice be well-captured by control-derived HVGs; the argument is worst-case.

## Linked ideas

## Open questions

- Empirically, what fraction of zero-shot DEGs fall outside the control-HVG set?
