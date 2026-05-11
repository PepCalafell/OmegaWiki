---
title: "DoRothEA TF activity inference shows HIF1A, RELA, STAT2, IRF1 co-active in mMAC1 with RELA NES rising from 3.8 to 5 along the hypoxia axis"
slug: dorothea-hif1a-rela-irf-stat-co-active-mmac1
status: supported
confidence: 0.85
tags:
  - DoRothEA
  - TF-regulon
  - HIF1A
  - RELA
  - STAT2
  - IRF1
  - NES
domain: "methods / epigenetics"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: strong
    detail: "DoRothEA inference on bulk RNA-seq (Calafell 2024 Fig. 2F). Hypoxia axis: HIF1A is top TF in iMAC21 vs iMAC1. In mMAC21 vs mMAC1: STAT2 and IRF1 overtake HIF1A; RELA regulon NES increases from 3.8 (iMAC21 vs iMAC1) to 5 (mMAC21 vs mMAC1)."
conditions: "DoRothEA v2 TF regulon database, bulk RNA-seq normalized counts, default scoring."
date_proposed: 2026-05-11
date_updated: 2026-05-11
---

## Statement

Discriminant regulon expression analysis (DoRothEA) shows that on the hypoxia axis, HIF1A is the dominant TF regulon in unstimulated MACs (iMAC21 vs iMAC1), but in activated MACs (mMAC21 vs mMAC1), STAT2 and IRF1 overtake HIF1A while RELA regulon activity rises (NES 3.8 → 5). This indicates that hypoxia + LPS co-activates an IFN/STAT/IRF/NF-κB axis on top of the HIF1A hypoxic baseline.

## Evidence summary

- DoRothEA TF regulon analysis (Calafell 2024 Fig. 2F).
- Top 8 positive regulons per comparison, ranked by NES.
- RELA NES quantification: 3.8 (iMAC21 vs iMAC1) → 5 (mMAC21 vs mMAC1).

## Conditions and scope

- TF regulon inference is correlation-based and depends on the curated regulon database.
- Cannot disambiguate direct vs indirect TF activity.

## Counter-evidence

- DoRothEA's RELA regulon may overlap with NFKB1; the paper reports both as co-active.

## Linked ideas

- Multi-regulon hypoxic+inflammatory program; useful for HypoxiaVERSE atlas regulon scoring.

## Open questions

- Whether STAT2/IRF1 are autocrine type-I-IFN-driven (sterile inflammation) or LPS/NF-κB-induced.
