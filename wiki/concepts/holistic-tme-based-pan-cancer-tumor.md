---
title: "Holistic TME-based pan-cancer tumor classification (10 groups, T/M/S trichotomy)"
aliases:
  - holistic TME-based tumor classification
  - TME-based pan-cancer tumor classification
  - 10 TME groups G01-G10
  - TME group classification G01-G10
tags:
  - pan-cancer
  - tme
  - classification
  - single-cell
  - immune-stratification
maturity: emerging
key_papers:
  - pan-cancer-tumor-classification-holistic-tumor
first_introduced: "2025"
date_updated: 2026-06-03
related_concepts:
  - pan-cancer-tumor-ecosystem-five-subtypes
  - cancer-type-specificity-tme-vs-malignant
  - atlas-level-data-integration
---

## Definition

A single-cell-resolved pan-cancer tumor classification that stratifies tumors by their holistic tumor-microenvironment cellular composition. Coarse clustering on major-compartment abundance yields a trichotomy of T-, myeloid-, and stromal-dominant tumors; refinement on fine-grained cell-cluster frequencies defines 10 stable groups (G01–G10).

## Intuition

A tumor is an ecosystem, not a bag of cancer cells. Describing each tumor by the relative abundance of all its TME cell states captures dominant cellular programs that one-cell-type analyses miss, exposing immune-hot (T-centric), myeloid-centric, and immune-cold (stromal-centric) phenotypes and finer subdivisions within them.

## Variants

- Major-compartment trichotomy (T / myeloid / stromal).
- 10 fine-grained groups: G01–G04 T-centric, G05–G07 M-centric, G08–G10 S-centric.

## Comparison

Complements bulk-derived ecotype schemes such as the [[pan-cancer-tumor-ecosystem-five-subtypes]] classification, but is built from single-cell fine-grained TME composition rather than deconvolved bulk signatures, giving higher cellular resolution.

## When to use

When stratifying patients for immunotherapy by the cellular structure of the whole TME rather than by tissue of origin or a single biomarker.

## Known limitations

- The number of groups (10) is a chosen resolution.
- Group proportions depend on the cohorts sampled per cancer type.

## Open problems

- Stability of the scheme as new cancer types/platforms are added.

## Key papers

- [[pan-cancer-tumor-classification-holistic-tumor]] — defines the 10-group, single-cell holistic TME classification.

## My understanding

A cellular-composition coordinate system for tumors that links TME structure to ICB response and to matched therapeutic strategies.
