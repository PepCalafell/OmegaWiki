---
title: "SLPI+ profibrotic macrophage (Macro_SLPI) — pan-cancer ECM-remodeling TAM"
aliases:
  - SLPI+ macrophage
  - SLPI+ TAM
  - Macro_SLPI
  - profibrotic macrophage
  - profibrotic TAM
  - ECM-remodeling macrophage
  - SLPI-high tumor macrophage
  - profibrotic monocyte-derived TAM
  - wound-healing-like TAM
  - SLPI secretory leukocyte protease inhibitor TAM
tags:
  - pan-cancer
  - tam
  - macrophage
  - profibrotic
  - ecm
  - tme
  - immunosuppression
  - myeloid
maturity: emerging
key_papers:
  - spatiotemporal-analyses-pan-cancer-single-cell
first_introduced: "2025"
date_updated: 2026-05-26
related_concepts:
  - ecm-mac-collagen-producing-tam
  - cthrc1-slpi-profibrotic-spatial-ecotype
  - col11a1-spp1-fibrotic-axis-cd8-exclusion-nsclc
  - pan-cancer-tam-atlas-23-clusters
---

## Definition

A profibrotic tumor-associated macrophage subtype marked by high SLPI (secretory leukocyte protease inhibitor) expression with diminished phagocytic and inflammatory capacity but the highest EMT and focal-adhesion meta-program scores among 8 pan-cancer monocyte/macrophage subtypes. Originates from monocytes via a developmental trajectory distinct from phagocytic Macro_C1QC and anti-inflammatory Macro_THBS1.

## Intuition

Macro_SLPI is the macrophage analog of CTHRC1+ CAFs — a TAM whose dominant function is **ECM remodeling and tissue fibrosis** rather than phagocytosis or cytokine secretion. Its program is reminiscent of wound-healing macrophages in lung fibrosis and post-COVID-19 fibrotic lungs, suggesting tumors hijack a conserved fibrotic-niche macrophage state.

## Comparison

- Sister state to SPP1+ TAMs ([[concepts/col11a1-spp1-fibrotic-axis-cd8-exclusion-nsclc]]) — both are profibrotic, but SPP1+ is osteopontin-driven and stronger in NSCLC; Macro_SLPI is broader pan-cancer and lacks high SPP1.
- Likely overlaps with ECM-Mac collagen-producing TAM ([[concepts/ecm-mac-collagen-producing-tam]]) — both deposit/remodel ECM, but ECM-Mac is COL1A1+; Macro_SLPI emphasizes EMT-program and SLPI as the canonical marker.
- Distinct from C1QC+ phagocytic and THBS1+ anti-inflammatory TAMs ([[concepts/pan-cancer-tam-atlas-23-clusters]]).

## Key papers

- [[papers/spatiotemporal-analyses-pan-cancer-single-cell]] — identifies Macro_SLPI across pan-cancer scRNA-seq, demonstrates worse TCGA survival in ESCA (P=0.014) and SKCM (P=0.0001), shows colocalization with CTHRC1+ CAFs in spatial transcriptomics.

## When to use

- Annotating TAM subtypes in scRNA-seq from BCC, cholangiocarcinoma, ESCA, SKCM — where Macro_SLPI is most enriched.
- Interpreting TAM heterogeneity in spatial-omics: SLPI/CD68 dual-staining co-occurs with CTHRC1+ regions at tumor leading edges (mIHC validated in HNSC, oral, NSCLC).
- Designing TGFβ1/IL-1β interception: NicheNet inference identifies these ligands as shared upstream activators of Macro_SLPI and CTHRC1+ CAFs.

## Open problems

- Is the SLPI+ state reversible by anti-TGFβ or anti-IL-1β intervention?
- How does Macro_SLPI relate to TREM2+ hypoxic-niche TAMs ([[concepts/trem2-tumor-associated-macrophage]])? Are they competing or sequential states?
- Does AhR-mediated tryptophan metabolism intersect the Macro_SLPI program?
