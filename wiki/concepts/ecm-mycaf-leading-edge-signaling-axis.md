---
title: "Ecm-myCAF — leading-edge signalling axis in solid tumors"
aliases:
  - ecm-myCAF
  - ecm myCAF
  - LRRC15+ myCAF
  - matrix myCAF
  - extracellular matrix myCAF
  - ECM-producing myofibroblastic CAF
  - ecm-myCAF LE axis
  - CAF leading edge signalling
  - fibrovascular niche LE
  - CAF-tumor LE crosstalk
tags: [CAF, leading-edge, ligand-receptor, ECM, OSCC, pan-cancer]
maturity: active
key_papers:
  - spatial-transcriptomics-reveals-distinct-conserved-tumor
first_introduced: "Galbo 2022 / Kieffer 2020 (CAF taxonomy); spatial axis formalised by Arora & Cao 2023"
date_updated: 2026-05-22
related_concepts: []
---

## Definition
Ecm-myCAFs are a conserved CAF subset (LRRC15+, GJB2+, COL1A1-high, FN1-high) that signal preferentially to LE cancer cells. CellChat reconstruction shows that ecm-myCAF → LE interactions exceed both LE-LE and TC-TC cancer signalling in number and strength, suggesting that this stromal axis actively maintains LE-state biology.

## Intuition
The invasive front is not a cancer-cell-autonomous state — it is co-produced with a specific CAF niche. Disrupting that stromal partner could collapse the LE state without targeting the malignant cells directly.

## Variants
- LRRC15-high myCAF (the canonical ecm-myCAF)
- Detox-iCAF (ADH1B+, GPX3+) — alternative niche, less LE-coupled
- Intermediate fibroblasts (CXCL1+, PDPN1+) — also enriched in LE neighbourhoods

## Comparison
Earlier CAF taxonomies (Sahai 2020, Galbo 2022) defined myCAF and iCAF on inflammation vs contractility. The ecm-myCAF identifier sharpens that with spatial coupling: which CAF subset signals to which cancer-cell state.

## When to use
- Designing CAF-depletion strategies that selectively reduce invasive biology
- Interpreting ST data with mixed stromal/cancer compositions
- Identifying ligand-receptor pairs (COL1A1-SDC1, FN1-SDC1) as candidate drug targets

## Known limitations
- CellChat inference is correlational, not perturbation-validated
- Spatial resolution of Visium spots can blur CAF and cancer signals within the same spot
- Generalisability beyond OSCC to other tumour types remains to be tested explicitly

## Open problems
- Whether targeting ecm-myCAF (e.g. anti-LRRC15 ADCs) reverses LE state in vivo
- Mapping ecm-myCAF heterogeneity at higher spatial resolution (CosMx, Stereo-seq)

## Key papers
- [[papers/spatial-transcriptomics-reveals-distinct-conserved-tumor]]

## My understanding
The ecm-myCAF–LE axis is one of the most translationally interesting parts of the paper. LRRC15-targeting therapeutics are already in clinical development; if the LE-coupling holds beyond OSCC, this becomes a pan-cancer entry point.
