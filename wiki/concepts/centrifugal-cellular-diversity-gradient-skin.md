---
title: "Centrifugal cellular diversity and density gradient across the human body plan"
aliases:
  - centrifugal diversity gradient
  - centrifugal density axis
  - trunk-to-extremity skin diversity
tags:
  - skin
  - body-plan
  - cellular-diversity
  - spatial-transcriptomics
maturity: emerging
key_papers:
  - single-cell-spatial-transcriptomic-analysis-human
first_introduced: "Restrepo et al. Nature Genetics 2026"
date_updated: 2026-05-27
related_concepts:
  - "[[concepts/skin-multicellular-spatial-neighborhoods]]"
---

## Definition

The observation that cellular diversity (Shannon) and cell density (cells per 100 µm²) in adult human skin both increase centrifugally — from low-diversity central body sites (buttocks, abdomen, back) toward higher-diversity peripheral sites (face, scalp, sole, flexural fossae) — independently of hair-follicle density.

## Intuition

The body plan imprints a coarse axis on skin composition: extremities recruit more immune and vascular populations, while the trunk is comparatively immune-quiet. This frames "site-matched" controls as essential for any skin disease study, and explains some long-standing biopsy-site biases.

## Variants

- Anterior-posterior and craniocaudal sub-gradients ride on top of the centrifugal axis.
- Flexural sites (antecubital, popliteal) are diversity-enriched relative to neighboring extensor sites (elbow, knee).

## Comparison

- Distinct from skin-microbiome diversity gradients which follow moisture/sebum.

## When to use

When interpreting between-site differences in scRNA-seq / spatial cohorts; when designing biopsy-matched studies; when comparing AD/psoriasis lesional vs non-lesional that involve different anatomic sites.

## Known limitations

- Demographic confounding (age, sex, ancestry) partially deconvolved by variance partitioning but not exhausted.
- Centrifugal pattern is based on 15 sites; not all body coordinates sampled.

## Open problems

- Is the centrifugal gradient genetically programmed or environmentally maintained (UV, mechanical stress)?
- Does the gradient shift with age?

## Key papers

- [[papers/single-cell-spatial-transcriptomic-analysis-human]]

## My understanding

Important constraint for any skin study: lesional/non-lesional comparisons that mix anatomic sites will confound disease signal with the centrifugal axis. Adds rigour requirements for skin biopsy design.
