---
title: "JAK-STAT pathway members (Jak1, Stat2, Irf9, Ifnar1, Tyk2) form a tightly co-clustered perturbation module whose knockout effects are more similar within a time point than across time points"
slug: jak-stat-pathway-members-form-co
status: supported
confidence: 0.8
tags: [jak-stat, interferon, crispr-screen, perturbation, regulon, macrophage]
domain: immunology
source_papers:
  - integrated-time-series-analysis-high-content
evidence:
  - source: integrated-time-series-analysis-high-content
    type: supports
    strength: strong
    detail: "Cross-prediction functional similarity graph: Jak1, Stat2, Irf9, Ifnar1, Tyk2 strongly co-clustered across time; their KO effects were more similar to each other at a given time point than across time points (Spearman ρ = -0.9 between within-time and within-KO similarity), i.e. they regulate different gene sets at each time point."
conditions: "RAW 264.7-Cas9 macrophages; upscaled CROP-seq; 0, 6, 24 h Listeria."
date_proposed: 2026-06-04
date_updated: 2026-06-04
---

## Statement
The interferon JAK-STAT regulators Jak1, Stat2, Irf9, Ifnar1 and Tyk2 behave as a coherent functional module: their knockout transcriptional signatures are highly similar to one another, but the specific gene sets they control shift across the time course (time-point variation exceeds regulator variation for this group).

## Evidence summary
Cross-prediction analysis and within-group similarity quantification ([[papers/integrated-time-series-analysis-high-content]], Figures 6B-D; uses [[foundations/isgf3-complex]], [[concepts/perturbation-cross-prediction-functional-similarity-graph]]).

## Conditions and scope
Macrophage cell line; Listeria time course.

## Counter-evidence
Stat1 sometimes clustered separately from the Jak1/Stat2/Irf9 group.

## Linked ideas

## Open questions
Authors propose a switch from a STAT2/IRF9-dependent homeostatic regulon to canonical STAT1/STAT2/IRF9 ISGF3 activity upon IFN-β.
