---
title: "Pan-cancer tumor ecosystem five-subtype classification (DLP / NIHS / DHP / AILS / AIHS)"
aliases:
  - pan-cancer tumor ecosystem subtypes
  - tumor ecosystem subtypes
  - tumor ecotypes
  - DLP NIHS DHP AILS AIHS
  - TabulaTIME bulk ecotype classification
  - five tumor ecosystem groups
  - E1-E5 ecotypes
  - profibrotic ecotype subtype
  - immune-stromal ecotype classification
  - pan-cancer TME bulk subtypes
tags:
  - pan-cancer
  - ecotype
  - tcga
  - bulk
  - stromal
  - immune
  - prognosis
  - tme
maturity: emerging
key_papers:
  - spatiotemporal-analyses-pan-cancer-single-cell
  - pan-cancer-tumor-classification-holistic-tumor
first_introduced: "2025"
date_updated: 2026-05-26
related_concepts:
  - cthrc1-slpi-profibrotic-spatial-ecotype
  - cthrc1-efibro-ecm-remodeling-pan-cancer-caf
---

## Definition

A patient-level classification of 8,743 TCGA tumors across 23 cancer types into five tumor ecosystem subtypes derived by hierarchical clustering of cell-type signature scores from the TabulaTIME pan-cancer reference. The underlying five ecotypes (E1 stromal, E2 naive immune, E3 activated immune, E4 profibrotic, E5 proliferating) combine into five patient groups: **DLP** (desert-low-purity), **NIHS** (naive immune + high stromal), **DHP** (desert-high-purity), **AILS** (activated immune + low stromal), **AIHS** (activated immune + high stromal).

## Intuition

The classification stratifies tumors along two orthogonal axes — immune activation (desert vs naive vs activated) and stromal abundance (low vs high) — and identifies a clinically meaningful "profibrotic-dominated" axis (DHP / NIHS) where CTHRC1+ CAF + SLPI+ TAM ecotypes drive worst-outcome states.

## Comparison

- Complements purely immune-centric pan-cancer classifications (e.g., immunome) by adding stromal axis.
- Builds on prior TCGA molecular-subtype work (TIDE, Thorsson et al.) but uses single-cell-derived signatures rather than bulk gene-set enrichment.
- Patient subtypes are bulk-derived; single-cell validation per cancer type is incomplete.

## Key papers

- [[papers/spatiotemporal-analyses-pan-cancer-single-cell]] — derives ecotype classification from TCGA, validates survival stratification in SKCM (P=2.54×10⁻⁵, n=459) and BRCA (P=0.0229, n=1,091).

## When to use

- Stratifying TCGA patients for retrospective survival analyses by stromal-immune subtype.
- Designing patient-selection schemes for anti-CAF, anti-TGFβ, or anti-LGALS9 trials — DHP/NIHS profibrotic-dominated subtypes are the predicted responder population.
- Mapping new pan-cancer scRNA-seq cohorts onto an interpretable ecotype framework.

## Open problems

- How robust is the classification across non-TCGA cohorts and in independent ICB-treated cohorts?
- Does AIHS truly predict ICB response in trial data?
- Can the five-subtype framework be refined per cancer type (e.g., subdivide DHP in BRCA HR+ vs TNBC)?
