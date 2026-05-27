---
title: "IFN-γ-driven CXCL9+ TAM (8_IFNGMac) — T-cell-recruiting macrophage associated with ICI response"
aliases:
  - "8_IFNGMac"
  - "IFNGMac"
  - "IFN-gamma macrophage"
  - "CXCL9+ TAM"
  - "CXCL9-CXCL10 macrophage"
  - "T-cell-recruiting TAM"
  - "ICI-responder macrophage"
  - "IFN-γ-stimulated TAM"
  - "M1-like CXCL9+ TAM"
  - "T-cell-engaging macrophage"
  - "Coulton 8_IFNGMac cluster"
tags:
  - TAM
  - 8_IFNGMac
  - CXCL9
  - CXCL10
  - IFN-gamma
  - T-cell-recruitment
  - ICI-response
  - biomarker
maturity: emerging
key_papers:
  - using-pan-cancer-atlas-investigate-tumour
  - tumour-microenvironment-crosstalk-nsclc-progression-response
  - macrophages-targets-next-generation-cancer-immunotherapy
first_introduced: "Coulton et al. 2024 *Nature Communications* (cluster definition + ICI-response association)"
date_updated: 2026-05-27
related_concepts:
  - pan-cancer-tam-atlas-23-clusters
  - pd-l1-immunostimulatory-tam-phenotype
  - tam-recruitment-hypoxic-niche-chemokines
  - gold-standard-bulk-tam-signatures
  - mana-score-neoantigen-tcell-signature
---

## Definition

8_IFNGMac is a TAM cluster defined in the Coulton 2024 pan-cancer atlas by IFN-γ-driven gene expression: high CXCL9 (top marker), CXCL10, MMP9, and the interferon-induced gene VAMP5. Functionally, the cluster is interpreted as a T-cell-recruiting, IFN-γ-responsive TAM state and is one of the strongest *responder*-associated signatures in CPI1000+ bulk RNAseq (fgsea q≈1.4e-11). The signature meets the "gold-standard" criterion for bulk-RNAseq deconvolution.

## Distinguishing features

- **Marker genes**: CXCL9, CXCL10, MMP9, VAMP5.
- **Spatial niche**: nearest neighbours are TAMs, then CD4 memory T cells, cancer cells, CD8 memory T cells (CosMx NSCLC).
- **MANA-stratification**: 8_IFNGMac proportion enriched in high-MANA lung tumour samples (q=0.060).
- **Bulk-RNAseq deployable**: passes Metric1 > 0.1 and Metric2 ≥ 3/5 cancer-type criteria.

## Mechanistic interpretation

- IFN-γ signalling drives CXCL9/CXCL10 chemokine production, which in turn recruits CXCR3+ T cells to the tumour.
- The cluster's spatial proximity to memory T cells supports an active TAM-T cell crosstalk role.
- Enrichment in high-MANA samples suggests neoantigen-reactive T cell IFN-γ secretion feeds back to polarize TAMs toward this state.

## Validity / limitations

- Functional T-cell recruitment is inferred from gene expression + spatial proximity; no in vivo perturbation.
- Some CXCL9 expression in the atlas comes from non-8_IFNGMac clusters — gold-standard criterion mitigates but does not eliminate signal bleed.

## When to use / look for

- Bulk-RNAseq stratification: high 8_IFNGMac signature predicts ICI response.
- Combined biomarker panels with 18_ECMMac (responder/non-responder axes).
- Mechanistic studies of TAM-T cell IFN-γ feedback loops.

## Key papers

- [[papers/using-pan-cancer-atlas-investigate-tumour]] — Coulton et al. 2024. Cluster definition, ICI-response association, and MANA-score stratification.
