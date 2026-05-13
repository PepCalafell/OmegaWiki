---
title: "MoMac-VERSE / MNP-VERSE — pan-tissue MNP scRNA-seq compendium"
aliases:
  - "MoMac-VERSE"
  - "MNP-VERSE"
  - "Mononuclear Phagocyte Verse"
  - "human MNP atlas"
  - "human monocyte and macrophage atlas"
  - "pan-tissue MNP single-cell atlas"
  - "consensus MNP annotation"
  - "MoMac single-cell reference"
  - "Mulder MoMac atlas"
  - "MNP single-cell compendium"
  - "Phenograph MNP clusters"
  - "macrophage scRNA-seq reference"
tags:
  - macrophage
  - monocyte
  - single-cell
  - atlas
  - reference-mapping
  - immunology
maturity: active
key_papers:
  - cross-tissue-single-cell-landscape-human
  - nf-kb-tet2-promote-macrophage-reprogramming
  - using-pan-cancer-atlas-investigate-tumour
first_introduced: "Mulder et al. 2021 *Immunity*"
date_updated: 2026-05-06
related_concepts:
  - mononuclear-phagocyte-system
  - trem2-tumor-associated-macrophage
  - il4i1-tumor-associated-macrophage
  - macrophage-ontogeny-resident-vs-monocyte-derived
  - mmac1-hypoxic-inflammatory-macrophage
  - tumor-associated-macrophage-immunosuppression
---

## Definition

The MNP-VERSE is an integrated single-cell RNA-seq atlas of 178,651 human mononuclear phagocytes (MNPs) drawn from 41 datasets across 13 tissues (spleen, lung, liver, skin, blood, lymph node, kidney, head and neck, tonsil, colon, stomach, breast, pancreas), constructed by Seurat V3 anchor integration. The MoMac-VERSE is the monocyte- and macrophage-only re-integration of the MNP-VERSE, defining 18 conserved Phenograph clusters with cluster-specific gene signatures (e.g. #2 HES1_Mac, #3 TREM2_Mac, #4 ISG_Mo, #6 IL4I1_Mac, #15 IL1B_Mo, #16 C1Qhi_Mac, #17 FTL_Mac).

## Intuition

Before this work, every paper that profiled human macrophages by scRNA-seq invented its own cell-type vocabulary: TREM2-Macs in liver tumours, LAMs in adipose, FOLR2 in liver, IL4I1+ in melanoma, and so on. The MoMac-VERSE provides a *shared coordinate system* — any new MNP scRNA-seq dataset can be projected onto its Phenograph clusters via Azimuth, giving a uniform name and signature regardless of tissue or disease context.

## Formal notation

- 41 datasets × 13 tissues × 178,651 MNPs
- Major MNP subsets: cMo (#1, #5, #8), CD16⁺ Mo (#15), Macs (heterogeneous), cDC1, cDC2/DC3, mregDC, pre-DC, T-doublets, Proliferating
- MoMac-VERSE clusters of interest:
  - #2 HES1_Mac — embryonic-origin-leaning, FOLR2/FTL+
  - #3 TREM2_Mac — monocyte-derived, lipid-handling, immunosuppressive
  - #4 ISG_Mo — IFN-stimulated monocyte, candidate IL4I1_Mac precursor
  - #6 IL4I1_Mac — IL4I1⁺PD-L1⁺IDO1⁺ immunosuppressive TAM, accumulates in tumour periphery
  - #15 IL1B_Mo — inflammatory monocyte (NFKB1/NFKB2-driven)
  - #16 C1Qhi_Mac — liver-tumour-specific
  - #17 FTL_Mac — ferritin light chain–high, iron-handling
- Validation: in-house indexed-SMARTseq2 protein expression confirms major subsets; SCENIC regulons and pathway analyses define functional differences
- Reference-mapping interface: Azimuth + the MoMac-VERSE Seurat object (publicly hosted on https://gustaveroussy.github.io/FG-Lab/)

## Variants

- MNP-VERSE (broad, includes DCs)
- MoMac-VERSE (Mo + Mac only)
- "Transformed matrix" (transf.matrix) — cells × genes-common-to-all-datasets, used for cross-cluster DEtG analysis
- Tissue-specific subspaces revealed by overlay (cancer-only, COVID-19-only, RA-only)

## Comparison

vs single-organ atlases (e.g. lung MNP, liver TAM): MoMac-VERSE preserves cluster identity across tissues, allowing cross-tissue comparison.
vs M1/M2 polarisation paradigm: 18-cluster decomposition supersedes the binary axis and exposes states (mregDC, ISG_Mo, IL4I1_Mac) the M1/M2 dichotomy cannot represent.
vs Tabula Sapiens / Human Cell Atlas: complementary; MoMac-VERSE focuses depth on MNP, while the Human Cell Atlas focuses breadth.

## When to use

- Annotating any new human MNP scRNA-seq dataset with consistent labels
- Locating in-vitro-derived populations (e.g. mMAC1) on the in-vivo cluster landscape
- Identifying tumour-, inflammation-, or infection-expanded MNP states
- Cross-study meta-analysis of macrophage signatures

## Known limitations

- Cells lost during transformed-matrix step due to gene-set intersection across datasets
- Periphery vs tumour-core annotations available only for liver and colon; lung/breast tumour zonation not captured
- Reference is human only; mouse mapping requires orthologue-based projection
- Disease-specific cell types absent from the reference (e.g. some severe-COVID-19 macrophages) may be mis-mapped

## Open problems

- Updating the atlas with newer datasets (single-cell multi-omics, spatial)
- Standardising tumour-core / periphery annotations across cancers
- Bridging MoMac-VERSE clusters to murine populations across more tissues than liver

## Key papers

- [[papers/cross-tissue-single-cell-landscape-human]] — original definition
- [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] — uses MoMac-VERSE to map mMAC1 in vitro signatures onto in vivo IL4I1_Mac, ISG_Mo, IL1B_Mo clusters

## My understanding

For the HypoxiaVERSE project, the MoMac-VERSE is the canonical in-vivo coordinate system for projecting in-vitro hypoxic-MAC signatures. Cluster #6 (IL4I1_Mac), #4 (ISG_Mo), and #15 (IL1B_Mo) are the primary anchors for the mMAC1 / hypoxic-inflammatory phenotype. Cluster #3 (TREM2_Mac) is the contrastive immunosuppressive baseline. Any new dataset entering the thesis should be Azimuth-mapped onto MoMac-VERSE before downstream comparisons.
