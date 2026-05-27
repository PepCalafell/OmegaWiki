---
title: "CT-L3 body-composition phenotyping in cancer cachexia"
aliases:
  - "L3 vertebra CT segmentation"
  - "CT-based body composition analysis"
  - "single-slice L3 SKM/SAT/VAT segmentation"
tags:
  - cachexia
  - oncology
  - body-composition
  - imaging
maturity: stable
key_papers:
  - cancer-associated-cachexia-bridging-clinical-findings
first_introduced: "Mourtzakis et al. 2008 (single-slice L3 protocol)"
date_updated: 2026-05-27
related_concepts: []
---

## Definition

A standardized imaging analysis approach that quantifies skeletal muscle (SKM), subcutaneous adipose tissue (SAT), visceral adipose tissue (VAT), and intermuscular adipose tissue from a single CT slice at the L3 vertebral level, leveraging routine oncology CT scans without additional patient burden. Modern implementations use validated AI segmentation that achieves strong concordance with manual segmentation and enables multi-vertebral analysis at scale.

## Intuition

The L3-slice cross-section correlates strongly with whole-body muscle and adipose tissue volumes, so a single CT image already routinely acquired for tumour staging can be repurposed to phenotype the patient's body composition. Tracking change across serial scans then enables longitudinal CAC monitoring at no marginal cost.

## Formal notation

- Indices: SMI (skeletal muscle index, cm²/m²); SAT and VAT areas in cm² or normalized to height² (cm²/m²); muscle attenuation (HU; lower = higher lipid infiltration, worse prognosis).
- Common change metrics: cm², cm²/m², or % change over a defined interval.
- Validated AI tools: SliceOmatic, AutoMATiCA, TotalSegmentator (multi-vertebral); manual segmentation remains the reference.

## Variants

- Multi-vertebral (T4, T12, L3, L4) analysis for whole-body extrapolation.
- Opportunistic CT analysis applied to surveillance scans collected for staging.
- Combined with PET-FDG to derive metabolic-uptake features per tissue (spleen, liver, pancreas, adipose).

## Comparison

- vs DEXA: CT discriminates SAT/VAT/SKM whereas DEXA gives whole-body lean vs fat; DEXA correlates well at single time-point but only modestly with % change.
- vs MRI: MRI avoids radiation and has higher soft-tissue resolution; CT is more available in oncology workflows.
- vs BIA: BIA cheaper and portable but cannot differentiate SAT/VAT/SKM.

## When to use

Whenever a cancer patient already has CT imaging (staging, response assessment, surveillance) and the question is whether body composition has changed in a clinically meaningful way. Especially valuable in retrospective cohort studies because data already exists.

## Known limitations

- Acquisition variability: slice thickness alters SKM area by ~1%; thinner slices increase VAT by ~3% and intermuscular adipose by ~17%; IV contrast and tube current also matter.
- Reference values are biased toward White non-Hispanic populations (Framingham; outpatient cohorts).
- Severely wasted patients or those with metal implants produce poor segmentation and need manual review or exclusion.
- No consensus on % loss thresholds for clinically significant change — reported cutoffs range from "any loss" to 14% SKM loss.

## Open problems

- Multiethnic, multinational reference values are missing.
- Precision testing for least significant change is rarely reported.
- Mapping L3-derived subtypes onto whole-body multi-tissue molecular signatures.
- Integrating CT-derived body composition into routine oncology decision-making (e.g., chemotherapy dose adjustment) — currently aspirational.

## Key papers

- [[papers/cancer-associated-cachexia-bridging-clinical-findings]] — comprehensive review of the methodology and clinical applications.

## My understanding

The most clinically tractable phenotyping tool for CAC because the data already exists in the EHR. The barrier is operational (segmentation pipeline + reference values), not technical.
