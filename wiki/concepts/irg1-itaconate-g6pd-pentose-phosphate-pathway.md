---
title: "IRG1/itaconate–G6PD–pentose phosphate pathway inhibition axis"
slug: irg1-itaconate-g6pd-pentose-phosphate-pathway
type: concept
aliases:
  - itaconate-G6PD axis
  - IRG1 itaconate G6PD PPP axis
tags:
  - immunometabolism
  - itaconate
  - pentose-phosphate-pathway
  - G6PD
  - macrophage
  - lung-cancer
maturity: emerging
key_papers:
  - irg1-itaconate-rewires-macrophage-lung-tumor
first_introduced: "2026"
date_updated: 2026-07-24
related_concepts:
  - m1-macrophage-tca-breaks-itaconate-succinate
  - succinate-itaconate-metabolic-set-point
  - warburg-effect-hif1a-glycolytic-reprogramming
  - oxphos-vs-glycolytic-tumor-metabolic-heterogeneity
---

## Definition

A metabolic control axis in which the macrophage immunometabolite itaconate (produced by IRG1/ACOD1, or delivered as 4-octyl itaconate) directly and non-covalently inhibits glucose-6-phosphate dehydrogenase (G6PD), the entry enzyme of the oxidative pentose phosphate pathway (PPP). The resulting suppression of oxidative PPP flux limits ribose-5-phosphate for nucleotide biosynthesis and NADPH for redox buffering, producing two coupled outputs: anti-proliferative pressure on cancer cells and a stress-activated, anti-tumor reprogramming of macrophages.

## Intuition

Prior itaconate biology centered on SDH inhibition and KEAP1/NRF2 alkylation. This axis adds a distinct, redox-adjacent target — G6PD — that is hit non-covalently (unlike the classic covalent cysteine chemistry). Because G6PD controls the ribose/NADPH depot that proliferating tumor cells depend on, one metabolite simultaneously (i) restrains tumor-cell division and (ii) shifts macrophages away from the anti-inflammatory, PPP-high state. The axis reframes itaconate as a metabolic brake on the PPP, not only an inflammatory signal modifier.

## Formal notation

itaconate/Octyl Ita ⊣ G6PD (↓Vmax, ~unchanged Km, no covalent adduct) → ↓ oxidative PPP flux (↓M+1 pentose phosphates, ↓R5P/Ru5P) → ↓ ribose-5-phosphate + ↓ NADPH/GSH → ↓ proliferation + G6PD–ROS–HMOX1 stress response.

## Variants

- **Cancer-cell arm**: NRF2-independent; ribose limitation is the dominant driver (TKT overexpression rescues; NAC does not).
- **Macrophage arm**: NRF2-dependent; PPP/G6PD suppression drives partial pro-inflammatory, anti-tumor reprogramming.
- **Endogenous vs pharmacologic**: IRG1-derived itaconate (autocrine + ABCG2-exported paracrine) vs exogenous 4-octyl itaconate.

## Comparison

Distinct from the SDH-inhibition/succinate ([[concepts/succinate-itaconate-metabolic-set-point]]) and KEAP1-NRF2 branches of itaconate action; complements rather than replaces them. Related to Warburg/PPP dependence in tumors ([[concepts/warburg-effect-hif1a-glycolytic-reprogramming]]) but centers on the oxidative PPP rather than glycolysis.

## When to use

Invoke when reasoning about how immunometabolites couple macrophage state to tumor-cell metabolism, or when considering G6PD/PPP as a druggable node reachable through itaconate mimetics.

## Known limitations

- Direct PPP-flux dissection was done mainly in A549 cells; generality across lung cancer genotypes is inferred from proliferation assays.
- Non-covalent G6PD inhibition is supported by kinetics/docking/chemoproteomics but lacks a co-crystal structure.

## Open problems

- Structural basis and specificity of non-covalent itaconate–G6PD binding.
- Extent of PPP/G6PD dependence across additional lung cancer subtypes.

## Key papers

- [[papers/irg1-itaconate-rewires-macrophage-lung-tumor]] — introduces the axis in lung cancer.

## My understanding

This is the load-bearing mechanistic novelty of the paper: it converts "itaconate is anti-inflammatory" into a concrete, quantitative metabolic-target story (G6PD/oxidative PPP) that unifies the tumor-cell-intrinsic and macrophage-reprogramming phenotypes under one node.
