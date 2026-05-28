---
title: "AlphaCell surpasses all baselines on compositional perturbation generalization across OTF, Sci-Plex and Tahoe"
slug: alphacell-surpasses-all-baselines-compositional-generalization
status: supported
confidence: 0.75
tags: [AlphaCell, compositional-generalization, benchmark, perturbation, quantitative]
domain: methods / single-cell
source_papers:
  - towards-building-world-model-simulate-perturbation
evidence:
  - source: towards-building-world-model-simulate-perturbation
    type: supports
    strength: moderate
    detail: "Quote (p.8): 'AlphaCell maintained a high performance on the genome-wise task, consistently surpassing all baselines across all metrics (Fig. 4).' Baselines include CPA, GEARS, CASCADE, scGPT, STATE, and linear models across genetic and chemical modalities."
conditions: "Compositional task = known cell type + known perturbation in a novel pairing; genome-wide eval."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

On the compositional generalization task (predicting a known perturbation's effect on a known cell type in a novel pairing), AlphaCell reportedly outperforms all benchmarked baselines (CPA, GEARS, CASCADE, scGPT, STATE, linear) across Pearson, MAE, DE Overlap Accuracy and Macro-F1 on OTF, Sci-Plex and Tahoe.

## Evidence summary

Reported in [[papers/towards-building-world-model-simulate-perturbation]] (Fig. 4). Concept: [[concepts/compositional-perturbation-generalization]]. Baselines: [[foundations/gears-perturbation-graph-neural-network]], [[foundations/scgpt-single-cell-foundation-model]], [[foundations/state-perturbation-prediction-model]], [[foundations/scgen-perturbation-integration]].

## Conditions and scope

Self-benchmarked, non-peer-reviewed preprint; baseline configs at genome scale may disadvantage competitors.

## Counter-evidence

Benchmark framed by authors as "asymmetrical challenge favoring the baselines" — independent replication absent.

## Linked ideas

## Open questions

- Do results hold under independent benchmarking (e.g., the Wei et al. 2025 generalizable-perturbation benchmark)?
