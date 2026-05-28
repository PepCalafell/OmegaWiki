---
title: "Fibroblast compositional signatures predict scarring risk in skin disease"
aliases:
  - fibroblast composition scarring risk
  - scarring-risk stromal signature
tags:
  - skin
  - fibroblast
  - fibrosis
  - scarring
  - disease-endotype
  - myofibroblast
maturity: emerging
key_papers:
  - single-cell-spatial-genomics-atlas-human
first_introduced: "Steele et al., Nature Immunology 2025"
date_updated: 2026-05-28
related_concepts:
  - "[[concepts/inflammatory-myofibroblast-il11-mmp1-intermediate-state]]"
  - "[[concepts/harmonized-skin-fibroblast-subtype-atlas-f1]]"
---

## Definition

The observation that the relative composition of fibroblast subtypes distinguishes clinically defined scarring-risk categories of skin disease (low risk, scarring risk, established fibrosis). Low-risk diseases are dominated by F1 superficial and F3 FRC-like fibroblasts; scarring-risk diseases are uniquely enriched for F6 inflammatory myofibroblasts; established fibrosis is enriched for F7 (and F8 fascia-like) myofibroblasts.

## Intuition

You can read a skin disease's scarring trajectory off its stromal makeup: presence of F6 inflammatory myofibroblasts flags active scarring risk, while their relative absence in established fibrosis suggests they are a transitional, not terminal, population.

## Formal notation

23 skin diseases grouped into 3 clinical scarring categories. Random-forest classifier ranks F6 and F7 as the most important subtypes for predicting scarring category. LRRC15 protein validates myofibroblasts in inflamed (scarring-risk) hidradenitis suppurativa but not low-risk atopic dermatitis.

## Variants

Compositional signatures cross-validated by spatial transcriptomics (Xenium/Visium) in atopic dermatitis (low risk) vs melanoma (scarring risk).

## Comparison

Links inflammatory-disease stroma to cancer-associated-fibroblast biology (F6≈iCAF, F7≈myoCAF).

## When to use

When stratifying inflammatory skin disease by fibrosis risk or interpreting stromal content as a disease endotype marker.

## Known limitations

Scarring categories are clinically assigned; compositional associations are correlative; sample numbers per disease vary widely.

## Open problems

Whether F6 abundance is prospectively predictive of scarring outcome in patients.

## Key papers

- [[papers/single-cell-spatial-genomics-atlas-human]] — Steele et al., Nature Immunology 2025

## My understanding

This reframes fibroblast composition as a clinically meaningful endotype axis, with F6 inflammatory myofibroblasts as the key risk-associated population.
