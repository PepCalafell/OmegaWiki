---
title: "FOLR2⁺ tissue-resident-like macrophage (FOLR2 mac)"
aliases:
  - "FOLR2 mac"
  - "FOLR2+ macrophage"
  - "FOLR2-positive TAM"
  - "FOLR2 TAM"
  - "FOLR2/SEPP1/STAB1 macrophage"
tags:
  - macrophage
  - tumor-microenvironment
  - FOLR2
  - tissue-resident-like
  - mo-mac
  - onco-fetal
maturity: active
key_papers:
  - trem2-macrophages-associated-enhanced-response-pd
first_introduced: "Sharma et al. 2020 (Cell); Li et al. 2024 (onco-fetal niche); refined across pan-cancer TAM atlases"
date_updated: 2026-05-26
related_concepts:
  - trem2-tumor-associated-macrophage
  - macrophage-ontogeny-resident-vs-monocyte-derived
  - tumor-associated-macrophage-immunosuppression
  - tissue-specific-tam-function-context-dependence
---

## Definition

A tumor-associated macrophage state defined by high FOLR2 (folate receptor β / FOLR2) expression alongside SEPP1, SLC40A1, F13A1, STAB1, IGF1, GPR34, RNASE1 — broadly characteristic of a tissue-resident-like, iron-handling, scavenging mo-mac state distinct from the TREM2-mac (efferocytic / lipid-handling) state.

## Intuition

Where the TREM2 mac is the "lipid-handling, efferocytic, monocyte-derived" TAM of recent scRNA-seq biology, the FOLR2 mac is the "scavenger / homeostatic / fetal-like" counterpart — expressing surface molecules characteristic of long-lived tissue-resident macrophages despite often being monocyte-derived in cancer.

## Formal notation

- Defining markers: FOLR2 + SEPP1 + SLC40A1 + F13A1 + STAB1 + IGF1 + GPR34 + RNASE1
- Broadly maps to MoMac-VERSE cluster #2 / tissue-resident-like compartments
- Tumor-enriched in multiple cancer types (HCC, breast, NSCLC, others)

## Variants

- HCC FOLR2 mac (non-responder-associated, onco-fetal-like)
- Breast cancer FOLR2 mac (T-cell-infiltration-associated, favourable outcome)
- Onco-fetal niche FOLR2 mac (Li et al.) — paired with CAFs and a subset of endothelial cells, linked to HCC relapse

## Comparison

vs TREM2 TAM: lipid-handling, efferocytic, more uniformly distributed; FOLR2 is scavenger / tissue-resident-like, more tumor-nodule-localised.
vs Kupffer cells: KCs are bona-fide tissue-resident (MARCO/CD5L/TIMD4/LYVE1); FOLR2 macs share some scavenging signatures but accumulate where KCs are depleted.

## When to use

When characterising scavenger/iron-handling/tissue-resident-like TAM populations across pan-cancer scRNA-seq atlases; when comparing TAM functional dichotomies (FOLR2 vs TREM2 axes) in a single tumor type.

## Known limitations

- Functional role is highly tissue-context-dependent: non-responder-associated in HCC, favourable in breast cancer.
- FOLR2 alone is not specific to one ontogeny; both resident and monocyte-derived populations express it.

## Open problems

- Whether HCC FOLR2 macs are causally pro-tumorigenic or just enriched alongside other niche components (CAFs, endothelial subsets).
- Mechanism of the tissue-context-dependent functional flip.

## Key papers

- [[papers/trem2-macrophages-associated-enhanced-response-pd]] — characterises FOLR2 macs as PD-1-non-responder-enriched in HCC, paradoxical to breast-cancer favourable association
