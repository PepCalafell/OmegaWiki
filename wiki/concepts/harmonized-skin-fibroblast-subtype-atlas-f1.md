---
title: "Harmonized human skin fibroblast subtype taxonomy (F1–F8)"
aliases:
  - F1-F8 skin fibroblast nomenclature
  - skin fibroblast subtype atlas
tags:
  - skin
  - fibroblast
  - single-cell
  - spatial-transcriptomics
  - atlas
  - nomenclature
maturity: emerging
key_papers:
  - single-cell-spatial-genomics-atlas-human
first_introduced: "Steele et al., Nature Immunology 2025"
date_updated: 2026-05-28
related_concepts:
  - "[[concepts/frc-like-fibroblast-ccl19-immunomodulatory-niche]]"
  - "[[concepts/inflammatory-myofibroblast-il11-mmp1-intermediate-state]]"
  - "[[concepts/cross-tissue-conserved-fibroblast-states]]"
---

## Definition

A consensus annotation of human skin fibroblasts integrating gene expression and spatial location into six major healthy subtypes (F1–F5, with F4 and F5 containing subclusters), two disease-adapted states (F1-like, F3-like), and three disease-specific myofibroblast states (F6, F7, F8). It harmonizes previously fragmented, study-specific fibroblast nomenclatures into one framework anchored in microanatomical niches.

## Intuition

Fibroblasts lack unique surface markers and adopt activated phenotypes in culture, so prior classifications were inconsistent. By integrating 357,276 high-quality fibroblasts (from 2.1M skin cells, 32 datasets, 251 donors) and spatially resolving them, the atlas ties each transcriptional subtype to a tissue location and function.

## Formal notation

Healthy: F1 superficial/papillary (COL13A1, APCDD1, WIF1); F2 universal/reticular (PI16, CD34, MFAP5); F2/3 perivascular (PPARG, shared F2/F3); F3 FRC-like (CCL19, CD74, HLA-DRA); F4 hair-follicle-associated (ASPN, COL11A1; DS_DPEP1+, TNN+COCH+, DP_HHIP+); F5 Schwann-like (SCN7A, NGFR; RAMP1+, NGFR+). Disease-specific: F6 inflammatory myofibroblast, F7 myofibroblast, F8 fascia-like myofibroblast.

## Variants

Disease-adapted F1-like (CRABP1+CYP26B1+, regenerative) and F3-like (CXCL9+/ADAMDEC1+, activated FRC) expand existing subtypes; disease-specific F6/F7/F8 have no healthy counterpart.

## Comparison

Harmonizes with the prior Tabib/Solé-Boldo-type skin classifications and the cross-tissue universal-fibroblast framework (Buechler et al.), reconciling differing markers/nomenclatures.

## When to use

As the reference labeling scheme when annotating human skin fibroblasts in health or disease, or mapping query datasets via reference mapping.

## Known limitations

Subtypes defined transcriptionally + spatially in snapshots; lineage relationships are inferred, not lineage-traced.

## Open problems

Functional validation of niche-specific roles; whether the taxonomy fully transfers to all skin sites and ages.

## Key papers

- [[papers/single-cell-spatial-genomics-atlas-human]] — Steele et al., Nature Immunology 2025

## My understanding

This is the organizing contribution of the paper: a niche-anchored, disease-aware fibroblast dictionary for human skin that doubles as a Rosetta stone for cross-tissue fibroblast work.
