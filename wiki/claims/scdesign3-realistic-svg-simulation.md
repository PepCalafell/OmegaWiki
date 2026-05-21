---
title: "scDesign3 Gaussian-process simulation enables biologically realistic SVG benchmarks beyond binary classification"
slug: scdesign3-realistic-svg-simulation
status: supported
confidence: 0.75
tags:
  - simulation
  - benchmarking
  - spatial-transcriptomics
  - methodology
domain: spatial-transcriptomics-methods
source_papers:
  - systematic-benchmarking-computational-methods-identify-spatially
evidence:
  - source: "[[papers/systematic-benchmarking-computational-methods-identify-spatially]]"
    type: supports
    strength: moderate
    detail: "Authors fit scDesign3 GP marginals (negative binomial) and Gaussian copula on 50 real ST datasets across 9 technologies. By mixing GP mean and shuffled non-spatial mean via α ∈ [0,1] with 21 grid values, they generate genes with continuous-valued ground-truth spatial variability. Evaluated by Kendall correlation rather than binary classification AUC. Authors argue this is more realistic than predefined-cluster simulations used in prior SPARK/SPARK-X/nnSVG/Spanve/scGCO papers."
conditions: "Limitations acknowledged: gene pre-selection step (high-spatial-variation genes) may bias methods that exploit similar pre-selection; Kendall correlation is computed per-gene, not across patterns; rotation invariance not tested. The simulation captures realistic spatial patterns from reference data but cannot generate patterns not present in the reference."
date_proposed: 2026-05-21
date_updated: 2026-05-21
---

## Statement

Using scDesign3 to fit GP marginals plus a Gaussian copula on real spatial transcriptomics references, then mixing the spatial and shuffled non-spatial mean components by a continuous α coefficient, generates SVG benchmarks with realistic spatial patterns and continuous ground-truth spatial variability — a substantive improvement over prior benchmarks that simulated SVGs from predefined clusters or limited pattern libraries.

## Evidence summary

Quote (p.15): "Previous studies often used simulated data by generating non-SVG profiles, which oversimplifies the distinction between SVGs and non-SVGs into a binary classification. Since spatial variability is a continuous measure, evaluating results within a binary framework is highly problematic. To address this, we proposed a novel strategy using scDesign3 and real-world spatial transcriptomics data to create biologically realistic datasets with varying degrees of spatial variation."

Method specifics (p.18): mu_formula = "s(spatial1, spatial2, bs='gp', k=500)", family_use = "nb"; copula = "gaussian"; 21 α values; 50 reference datasets across 9 technologies.

## Conditions and scope

Improves over the simulation strategies in [Edsgärd 2018, Sun 2020, Zhu 2021, Weber 2023]. Not a head-to-head with a "true" gold-standard biological ground truth (which does not exist for SVGs); the claim is about simulation realism, not external validity.

## Counter-evidence

The authors themselves acknowledge: gene pre-selection bias, per-gene Kendall correlation does not compare cross-pattern method behaviour, and rotation invariance is untested.

## Linked ideas

(none yet)

## Open questions

- Pattern-aware benchmarks that score methods separately per spatial pattern class.
- Rotation/registration-invariance benchmarks.
- Cross-technology generalisation (train on Visium reference, test on MERFISH simulated, and vice versa).
