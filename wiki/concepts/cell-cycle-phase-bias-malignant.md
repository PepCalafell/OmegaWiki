---
title: "Cell-cycle phase bias (G1/S vs G2/M) in malignant cells"
aliases:
  - phase bias
  - G1/S vs G2/M bias
  - cell-cycle phase distribution
  - G2/M bias
  - G1/S bias
  - scRNA cell-cycle phase
  - cycling cell phase fraction
  - pan-cancer phase bias
  - p53-driven phase bias
  - RB1-driven phase bias
tags: [cell-cycle, proliferation, scrna-seq, pan-cancer, tp53, rb1]
maturity: emerging
key_papers:
  - curated-cancer-cell-atlas-provides-comprehensive
first_introduced: "2025 (Tyler et al., 3CA v2)"
date_updated: 2026-05-26
related_concepts: [recurrent-malignant-metaprograms-nmf, curated-cancer-cell-atlas-3ca]
---

## Definition

Cell-cycle phase bias quantifies the relative proportion of cycling malignant cells detected in G1/S versus G2/M phases in a tumour or cancer type. Computed as `(n_G1/S − n_G2/M) / n_cycling`.

## Intuition

Standard scRNA-seq cell-cycle scoring identifies cycling cells by their G1/S and G2/M signature expression. Once cycling cells are flagged, their distribution between the two phases yields a phase-bias score that is robust to overall proliferation rate. Pan-cancer comparisons surface striking patterns: AML/CML lean strongly toward G1/S; PDAC and HPV− HNSCC lean strongly toward G2/M.

## Mechanistic link to driver mutations

- **TP53 loss** disables the G1/S checkpoint, so cycling cells progress and accumulate in G2/M → G2/M bias. Tyler et al. show TP53 is the most consistently G2/M-associated driver across TCGA cancer types.
- **RB1 loss** removes the pRb gate of G1/S, accelerating G1/S entry → G1/S bias.
- **HPV+ tumours** show strong G1/S bias consistent with HPV E7 degradation of pRb.
- Context-specific drivers (SMARCA4, EGFR, PIK3CA, CDH1, CTNNB1) show cancer-type-specific phase-bias associations.

## When to use

- To detect driver-mutation effects on cell cycle from scRNA-seq or bulk RNA-seq expression alone.
- To stratify tumours for likely sensitivity to CDK4/6 inhibitors (G1/S blockers), platinum (G2/M-toxic), or radiation.
- To compare proliferation biology between subtypes that share overall proliferation rate but differ in phase distribution (e.g. HPV+ vs HPV− HNSCC).

## Known limitations

- Estimating phase bias requires sufficient cycling cells per sample, which is hard for slow-cycling tumours (e.g. ccRCC).
- Phase-bias signatures are sensitive to choice of G1/S/G2/M gene panels.
- Driver-mutation associations are correlational at the TCGA bulk level; causation requires perturbation.

## Open problems

- Does phase bias prospectively predict response to CDK4/6 inhibitors or platinum chemotherapy?
- Are TME cell-cycle phases correlated with malignant phase bias?

## Key papers

- [[curated-cancer-cell-atlas-provides-comprehensive]] — first pan-cancer quantification across 19 cancer types with TCGA driver-mutation associations.

## My understanding

Phase bias is a small but elegant operational concept: it converts cell-cycle scoring (already a routine scRNA-seq step) into a driver-mutation readout with clean mechanistic anchors (TP53 → G2/M, RB1 → G1/S). For hypoxia work, the question is whether hypoxic malignant cells (which arrest in G1) show a distinct phase-bias signature.
