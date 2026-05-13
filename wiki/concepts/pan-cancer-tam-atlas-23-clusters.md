---
title: "Pan-cancer TAM atlas — 23-cluster Louvain taxonomy from 363,315 cells"
aliases:
  - "Coulton 2024 TAM atlas"
  - "pan-cancer macrophage atlas"
  - "23-cluster TAM taxonomy"
  - "TAM-only pan-tumour scRNAseq atlas"
  - "scRNAseq TAM atlas 17 cancer types"
  - "macrophage-atlas Litchfield"
  - "high-resolution TAM Louvain clustering"
  - "tumour-associated macrophage reference atlas"
  - "0_AlvMac to 22_IFNMac4 TAM clusters"
  - "TAM cluster taxonomy human pan-cancer"
  - "macrophage atlas Zenodo 11222158"
tags:
  - TAM
  - atlas
  - scRNA-seq
  - pan-cancer
  - Louvain
  - reference-mapping
maturity: established
key_papers:
  - using-pan-cancer-atlas-investigate-tumour
first_introduced: "Coulton, Murai, Qian, Thakkar, Lewis & Litchfield 2024 *Nat Commun*"
date_updated: 2026-05-13
related_concepts:
  - momac-verse-mnp-verse-atlas
  - m1-m2-polarization-paradigm
  - macrophage-ontogeny-resident-vs-monocyte-derived
  - tumor-associated-macrophage-immunosuppression
  - ecm-mac-collagen-producing-tam
  - ifng-mac-cxcl9-tam-ici-responder
  - scrna-atlas-as-reference-projection
  - gold-standard-bulk-tam-signatures
---

## Definition

A pan-cancer human tumour-associated macrophage (TAM) atlas constructed by Coulton et al. (2024, *Nature Communications*) from 32 published scRNA-seq studies covering 17 cancer types. After Seurat RPCA integration of 363,315 cells, Louvain clustering yields 23 clusters spanning canonical (alveolar, IFN-stimulated, proliferating, M2-like) and previously-undescribed (ECM-modifying, melanoma-brain-met-specific) TAM states.

## Cluster identity (selection)

- `0_AlvMac` — alveolar (FABP4/MCEMP1/CD52); lung-dominant.
- `1_MetM2Mac` — immunoregulatory M2 (SELENOP/SLC40A1/PLTP/F13A1/FUCA2).
- `2_C3Mac` — complement + MHC II (C3/PLD4/HLA-DPA1/HLA-DPB1).
- `3_ICIMac1` — TREM2/SPP1/RNASE1/NUPR1 (melanoma-ICI signature recapitulation).
- `4_ICIMac2` — TREM2/APOE/APOC1 (lipid-associated).
- `5_StressMac` — heat-shock proteins.
- `6_SPP1AREGMac` — SPP1/AREG/EREG/CCL20/CXCL3 — gold-standard signature.
- `7_IFNMac` — cytokine-rich (CCL2/8, SPP1).
- `8_IFNGMac` — CXCL9/CXCL10/MMP9/VAMP5 — IFN-γ, T-cell-recruiting, gold-standard.
- `9_AngioMac` — VEGFA/VCAN/THBS1.
- `10_InflamMac` — cytokine-rich pro-inflammatory.
- `11_MetalloMac` — metallothioneins (gold-standard).
- `12_MBMMac` — LRMDA-high, melanoma brain-metastasis-enriched.
- `13_CalciumMac` — calcium signalling.
- `14_ProliMac` — MKI67/CDK1 proliferating.
- `15_LYZMac` — LYZ-marked.
- `16_ECMHomeoMac` — ECM-homeostatic.
- `17_IFNMac3` — ISG15/CXCL10/CCL8 (gold-standard).
- `18_ECMMac` — **novel**: COL1A1/COL1A2/COL3A1 collagen-producing TAMs.
- `19_ClassMono` — classical monocytes.
- `20_TDoub` — TAM-T cell doublets.
- `21_HemeMac` — CD163/HMOX1 heme-clearance (gold-standard).
- `22_IFNMac4` — IFITM2/LST1 (gold-standard).

## Workflow (Coulton 2024)

1. Aggregate 32 published scRNAseq studies; extract TAMs via author annotations or de novo macrophage-signature filter.
2. SCT-normalize raw counts; benchmark Seurat CCA/RPCA, Harmony, Scanorama against iLISI on a 1.5 TB RAM node — pick RPCA.
3. Cluster at tuned resolution; verify macrophage/monocyte identity with SingleR vs Human Primary Cell Atlas.
4. Annotate clusters via top DEGs + literature.
5. Distribute as a Seurat object via Zenodo (11222158) for query-to-reference projection.

## Strengths and limitations

- **Strength**: TAM-specific resolution (vs broader myeloid atlases like Cheng 2021, Mulder 2021) reveals previously-undescribed states (18_ECMMac, 12_MBMMac).
- **Strength**: paired with ICI-response biomarker analysis and seven "gold-standard" bulk-RNAseq deconvolution signatures.
- **Limitation**: TAM extraction heterogeneity across 32 source studies (some author-annotated, some de novo).
- **Limitation**: snRNA-seq batch effects partially controlled but not formally adjusted.
- **Limitation**: 23 clusters depend on Louvain resolution; rare states may be merged.

## When to use

- Reference for projecting new TAM scRNAseq datasets to a standardized 23-cluster taxonomy.
- Source of cluster-level signatures for bulk-RNAseq deconvolution (especially the 7 gold-standard signatures).
- Hypothesis generator for cancer-type-specific TAM differentiation states.

## Key papers

- [[papers/using-pan-cancer-atlas-investigate-tumour]] — Coulton et al. 2024. Original atlas construction.
