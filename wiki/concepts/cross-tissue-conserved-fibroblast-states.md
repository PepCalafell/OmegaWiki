---
title: "Cross-tissue conserved fibroblast states (skin subtypes shared across human tissues)"
aliases:
  - cross-tissue fibroblast states
  - pan-tissue fibroblast conservation
tags:
  - fibroblast
  - cross-tissue
  - atlas
  - integration
  - universal-fibroblast
maturity: emerging
key_papers:
  - single-cell-spatial-genomics-atlas-human
first_introduced: "Steele et al., Nature Immunology 2025"
date_updated: 2026-05-28
related_concepts:
  - "[[concepts/harmonized-skin-fibroblast-subtype-atlas-f1]]"
  - "[[concepts/frc-like-fibroblast-ccl19-immunomodulatory-niche]]"
  - "[[concepts/inflammatory-myofibroblast-il11-mmp1-intermediate-state]]"
---

## Definition

The finding, from integrating ~5.8 million fibroblasts across skin, lung, intestine, synovium, endometrium, heart and nasal mucosa, that several skin fibroblast subtypes are conserved across human tissues — F2 universal, F3 FRC-like, F6 inflammatory myofibroblast and F7 myofibroblast — with F2/3 perivascular and F5 NGFR+ (nerve-associated) proposed as additional cross-tissue populations.

## Intuition

Despite very different tissue biophysics, fibroblast "archetypes" recur: a universal precursor, an immune-organizing FRC-like cell, an inflammatory myofibroblast, and a terminal myofibroblast. Skin subtypes therefore generalize beyond skin.

## Formal notation

Whole-transcriptome cross-tissue integration (scVI) of ~5.8M cells; ~1M fibroblasts selected by canonical markers; reannotation maps to skin F1–F8 labels plus tissue-specific clusters.

## Variants

Marker-based assessment vs whole-transcriptome integration (the latter more comprehensively defines state similarity).

## Comparison

Reconciles differing nomenclatures of prior cross-tissue studies (Buechler et al. 2021, Korsunsky et al. 2022, Gao et al. 2024) against one skin-anchored scheme.

## When to use

When transferring fibroblast annotations between tissues or interpreting fibroblast states in non-skin disease atlases.

## Known limitations

Semi-supervised integration may underestimate tissue-specific differences; some tissues contribute few cells; gene panels differ between datasets (e.g. endometrium ~17k genes).

## Open problems

Which fibroblast states are truly universal vs convergent; functional conservation, not just transcriptional.

## Key papers

- [[papers/single-cell-spatial-genomics-atlas-human]] — Steele et al., Nature Immunology 2025

## My understanding

The cross-tissue conservation of F3 and F6 is what elevates this from a skin atlas to a general statement about immune-interacting fibroblast biology.
