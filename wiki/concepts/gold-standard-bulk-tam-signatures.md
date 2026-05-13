---
title: "Gold-standard TAM signatures for bulk-RNAseq deconvolution"
aliases:
  - "gold-standard TAM signatures"
  - "gold-standard macrophage cluster signatures"
  - "bulk-RNAseq deployable TAM signatures"
  - "UCell-validated TAM signatures"
  - "cell-type-specific TAM signatures"
  - "Coulton 2024 gold-standard signatures"
  - "bulk-deconvolution TAM signature set"
  - "Metric1 Metric2 TAM signature criterion"
  - "cluster-specific TAM signatures"
  - "TAM signatures for ICI bulk biomarkers"
tags:
  - TAM
  - signature
  - bulk-RNAseq
  - deconvolution
  - UCell
  - biomarker
  - methodological
maturity: emerging
key_papers:
  - using-pan-cancer-atlas-investigate-tumour
first_introduced: "Coulton et al. 2024 *Nature Communications*"
date_updated: 2026-05-13
related_concepts:
  - pan-cancer-tam-atlas-23-clusters
  - ifng-mac-cxcl9-tam-ici-responder
  - ecm-mac-collagen-producing-tam
related_foundations:
  - ucell-signature-scoring
  - cibersortx-deconvolution
---

## Definition

The "gold-standard" TAM signatures are a curated subset of seven cluster-defining 10-gene signatures from the Coulton 2024 pan-cancer TAM atlas that retain cluster-specific detection in an all-cell-type atlas (i.e., they do not bleed into non-macrophage compartments) and consistently identify their cluster across multiple cancer types. They are recommended for bulk-RNAseq deconvolution and biomarker analysis.

## The seven signatures

1. `5_StressMac` — heat-shock protein-enriched.
2. `6_SPP1AREGMac` — SPP1/AREG/EREG/CCL20.
3. `8_IFNGMac` — CXCL9/CXCL10/MMP9/VAMP5 (responder-associated).
4. `11_MetalloMac` — metallothioneins.
5. `17_IFNMac3` — ISG15/CXCL10/CCL8 (responder-associated).
6. `21_HemeMac` — CD163/HMOX1 heme-clearance.
7. `22_IFNMac4` — IFITM2/LST1 (interferon-exposed).

## Selection criteria (Coulton 2024)

1. Re-cluster a separate all-cell-type atlas of 482,677 cells from refs 30, 31, 39 (breast/CRC/OV/lung + ccRCC + lung).
2. Compute mean UCell score per signature per cluster.
3. **Metric1** = best-hit mean UCell − second-best mean UCell > **0.1** (signature must clearly mark its top cluster).
4. **Metric2** = best-hit cluster matches the originating cluster in **≥ 3 of 5** cancer types (signature must generalize).
5. Apply both thresholds simultaneously.

## Validity / limitations

- Conservative criterion (Metric1 > 0.1; 3/5 cancer types) means several other useful signatures (e.g., 18_ECMMac) are excluded — they may still be informative in specific deployments.
- "Gold-standard" applies to bulk-RNAseq deployment, not necessarily to single-cell cluster annotation.
- Performance against established deconvolution tools (CIBERSORTx, BayesPrism) is not benchmarked in the paper.

## When to use

- Bulk-RNAseq ICI cohort stratification (e.g., CPI1000+ analyses in Coulton 2024).
- Pan-cancer TCGA-style cohort deconvolution where TAM-specific resolution beyond M1/M2 is desired.
- Reanalysis of historical bulk datasets to add TAM-state context.

## Key papers

- [[papers/using-pan-cancer-atlas-investigate-tumour]] — Coulton et al. 2024. Definition + selection criteria + CPI1000+ application.
