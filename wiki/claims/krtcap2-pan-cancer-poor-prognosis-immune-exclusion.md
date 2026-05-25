---
title: "KRTCAP2 expression is associated with poor pan-cancer prognosis and immune exclusion (low CD8/M1, high Treg) across most TCGA tumor types"
slug: krtcap2-pan-cancer-poor-prognosis-immune-exclusion
status: supported
confidence: 0.65
tags: [KRTCAP2,pan-cancer,prognosis,biomarker,immune-exclusion,Treg,CD8]
domain: oncology
source_papers:
  - development-hypoxia-responsive-macrophage-prognostic-model
evidence:
  - source: development-hypoxia-responsive-macrophage-prognostic-model
    type: supports
    strength: medium
    detail: "Quote (p.13, Results + Discussion): 'KRTCAP2 consistently emerged as a prognostic marker, with its expression linked to unfavorable outcomes across nearly all investigated cancer types, evidenced by a hazard ratio (HR) greater than 1'. Pan-cancer KRTCAP2 expression is elevated in tumors vs adjacent normal across most types and escalates with stage. KRTCAP2 negatively correlates with γδ T, CD8+ T, CD4+ memory-activated T cells, neutrophils, monocytes, resting mast, M1 macrophages, and activated DCs; positively correlates with Tregs (Fig 7E–G)."
conditions: "Pan-cancer survival from TCGA across multiple cohorts; immune infiltration estimated via CIBERSORT (LM22). No mechanistic validation; KRTCAP2 prior context: HCC (ref 37), gastric (ref 38), uveal melanoma (ref 39)."
date_proposed: 2026-05-25
date_updated: 2026-05-25
---

## Statement

KRTCAP2 (Keratinocyte-Associated Protein 2; N-glycosylation OST complex accessory subunit) emerges from the 13-gene PDAC hypoxia model as a pan-cancer prognostic gene: HR>1 for OS, DSS, DFS, and PFS across nearly all TCGA cancer types tested. KRTCAP2 expression is elevated in cancer vs adjacent normal tissue and rises with cancer stage. It correlates negatively with adaptive and M1-skewed immune cell infiltrates (CD8+ T, γδ T, CD4+ memory-activated T, M1 macrophages, activated DCs, neutrophils, monocytes, resting mast) and positively with immunosuppressive Tregs. Consistent with prior single-cancer reports in HCC, gastric, and uveal melanoma.

## Evidence summary

Reported in [[papers/development-hypoxia-responsive-macrophage-prognostic-model]] (Ge et al., *PLoS One* 2025, Fig 7A–G). Builds on prior reports (Sun et al. 2023 HCC; Lee et al. 2022 gastric; Liu et al. 2021 uveal melanoma) cited in the paper.

## Conditions and scope

- All analyses are TCGA-based and rely on CIBERSORT/LM22 deconvolution; no spatial or single-cell validation.
- Effect sizes (HR) are not tabulated per cancer type in the main text; the "nearly all" qualifier matters.
- No functional perturbation: no KRTCAP2 knockdown/overexpression with immune-readout to causally link expression to T-cell exclusion.

## Counter-evidence

None within paper scope. Prior literature is consistent.

## Linked ideas

## Open questions

- Does KRTCAP2 act through aberrant N-glycosylation of immune-relevant cell-surface glycoproteins (e.g. PD-L1, MHC-I, sialylated mucins)?
- Is the KRTCAP2–Treg correlation cancer-cell-intrinsic (chemokine secretion) or stromal (CAF-derived KRTCAP2)?
- Would small-molecule OST inhibitors (e.g. NGI-1) phenocopy a KRTCAP2 loss-of-function effect on tumour growth and immune infiltration?
