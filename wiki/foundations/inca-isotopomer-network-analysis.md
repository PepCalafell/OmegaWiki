---
title: "INCA — Isotopomer Network Compartmental Analysis"
slug: inca-isotopomer-network-analysis
domain: metabolic flux analysis / mass spectrometry
status: mainstream
aliases:
  - "INCA"
  - "INCA 2"
  - "INCA 2.3"
  - "Isotopomer Network Compartmental Analysis"
first_introduced: "Young et al. 2008 (INCA 1); Rahim et al. 2022 (INCA 2)"
date_updated: 2026-05-27
source_url: ""
---

## Definition

INCA is a software framework for 13C metabolic flux analysis (13C-MFA): given a defined network of reactions with their atom-transition (carbon-mapping) matrices and an experimentally measured mass-isotopomer distribution vector (MDV) of metabolites, INCA estimates intracellular fluxes by least-squares regression that minimises the sum of squared residuals between simulated and measured MDVs.

## Intuition

Without a flux model, isotopologue distributions are descriptive — "more M+3 means PC is active." INCA turns this into quantitative pathway flux: given a network and measured MDVs across multiple metabolites, it back-calculates the consistent set of reaction fluxes (including PC, PDH, glutamine anaplerosis, TCA segment fluxes) with uncertainty quantification by Monte Carlo simulation.

## Formal notation

- Inputs: network reactions with atom-transition mappings; tracer composition (e.g., U-13C6 glucose); measured MDVs.
- Output: flux estimates (per reaction) with 95% confidence intervals (Monte Carlo simulation).
- Goodness-of-fit: χ² test.
- Normalisation: a reference flux (often citrate synthase V12) set to a fixed value (e.g., 100).
- Algorithmic core: nonlinear least-squares regression with elementary-metabolite-unit (EMU) framework.

## Key variants

- INCA 1 vs INCA 2 (extended dynamic / non-stationary capabilities, NMR + MS support).
- INST-MFA (non-stationary): for short-time-window tracer experiments where steady-state assumption is violated.
- IsoCor: complementary tool for natural-13C correction of raw MS data (used upstream of INCA).

## Known limitations

- Network model is user-defined — incorrect topology produces wrong flux estimates.
- Steady-state assumption may be violated in disease conditions (rapid metabolic shifts during sampling).
- Citrate-synthase normalisation hides absolute-flux changes when CS itself is differentially expressed.

## Open problems

- Cell-type-specific flux modelling — current INCA pipelines are bulk-tissue.
- Integration with single-cell mass spec data.

## Relevance to active research

Used in [[papers/multi-omics-profiling-cachexia-targeted-tissues]] to model GC muscle TCA cycle fluxes from 13C6-glucose tracer data across Ctrl / Pre-cax / Cax groups; revealed elevated PC (V9), PDH (V10), 2-OGDH (V18) and glutamine anaplerosis (V16-V17) fluxes in cachectic muscle.
