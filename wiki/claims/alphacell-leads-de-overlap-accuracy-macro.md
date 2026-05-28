---
title: "AlphaCell leads in DE Overlap Accuracy and Macro-F1 while baselines give flat high-precision low-recall predictions"
slug: alphacell-leads-de-overlap-accuracy-macro
status: supported
confidence: 0.75
tags: [AlphaCell, differential-expression, Macro-F1, DE-overlap, benchmark, quantitative]
domain: methods / single-cell
source_papers:
  - towards-building-world-model-simulate-perturbation
evidence:
  - source: towards-building-world-model-simulate-perturbation
    type: supports
    strength: moderate
    detail: "Quote (p.8): 'AlphaCell demonstrated a substantial lead in DE Overlap Accuracy and Macro-F1 scores, whereas competitors often produced flat predictions with high precision but limited recall. Notably, expanding baseline models to predict the genome-wise gene set generally resulted in lower DE Overlap Accuracy.'"
conditions: "DE Overlap = top-DEG retrieval; Macro-F1 = correctness of up/down directionality."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

Beyond global correlation, AlphaCell substantially leads on Differentially Expressed Gene (DEG) retrieval (DE Overlap Accuracy) and regulatory-direction correctness (Macro-F1), while baselines — especially discrete-mapping models — produce flat predictions that overfit observation noise.

## Evidence summary

Reported in [[papers/towards-building-world-model-simulate-perturbation]] (Fig. 4). Reflects [[concepts/perturbation-continuous-flow-versus-discrete-jump]].

## Conditions and scope

Compositional generalization across OTF/Sci-Plex/Tahoe.

## Counter-evidence

Self-benchmarked; DEG thresholds and gene-set definitions can shift these metrics.

## Linked ideas

## Open questions

- How robust is DE Overlap to the choice of top-k DEG cutoff?
