---
title: "MoMac-VERSE defines conserved monocyte and macrophage gene signatures across human tissues and disease states"
slug: momac-verse-conserved-mnp-signatures-cross-tissue
status: supported
confidence: 0.9
tags:
  - MoMac-VERSE
  - MNP-VERSE
  - scRNA-seq
  - integration
  - atlas
  - macrophage
  - monocyte
domain: "immunology / single-cell"
source_papers:
  - cross-tissue-single-cell-landscape-human
evidence:
  - source: cross-tissue-single-cell-landscape-human
    type: supports
    strength: strong
    detail: "Seurat V3 integration of 178,651 MNPs from 41 datasets across 13 tissues yields 18 Phenograph clusters with conserved DEtG and SCENIC regulon signatures across colon, liver, lung. In-house indexed-SMARTseq2 protein-expression data (1830 cells, 5 tissues) validates the major MNP subsets (Mo/Mac, pre-DC, cDC2, cDC1) at protein level. Azimuth re-projection of three independent query datasets (rheumatoid arthritis Kuo 2019, COVID-19 PBMC Silvin 2020, COVID-19 BAL Liao 2020) recapitulates each study's main reported populations within the MoMac-VERSE clusters."
conditions: "Healthy and pathologic human MNP scRNA-seq across 13 tissues and 41 datasets; published platform: https://gustaveroussy.github.io/FG-Lab/."
date_proposed: 2026-05-06
date_updated: 2026-05-06
---

## Statement

A Seurat-V3-integrated atlas of 178,651 human mononuclear phagocytes from 41 datasets across 13 tissues defines a conserved set of MNP populations (cMo, CD16⁺ Mo, multiple Mac states, cDC1, cDC2/DC3, pre-DC, mregDC, proliferating) with stable gene-expression and TF-regulon signatures across tissues, validated at protein level and reusable for de novo annotation of new query datasets via Azimuth.

## Evidence summary

- 41 datasets × 13 tissues × 178,651 MNPs successfully integrated into a common UMAP space.
- 18 Phenograph clusters with cluster-specific DEtGs (Fig. 1E) and SCENIC DERs (Fig. 2B) across colon, liver, lung — the three datasets with sufficient depth for independent SCENIC replication.
- Indexed-SMARTseq2 data (1830 cells, 5 tissues) confirms surface protein expression of CD88, CD16, CD14, CD11b, CD206 (Mo/Mac), CD123, CD5, CD169 (pre-DC), CD1c, FcεRIα (cDC2/DC3), CD141 (cDC1) — protein-level validation.
- Azimuth re-projection of three new query datasets recovers each study's main reported populations: HBEGF⁺/MERTK⁺/IFN-STAT clusters from Kuo 2019 (RA synovial); HLA-DRB1^hi, NFKBIA^hi, C5AR1^hi clusters from Silvin 2020 (COVID-19 blood); TREM2_Mac, ISG_Mo, IL4I1_Mac frequencies from Liao 2020 (COVID-19 BAL).
- MNP-VERSE / MoMac-VERSE atlas published online at https://gustaveroussy.github.io/FG-Lab/.

## Conditions and scope

- Human only; mouse mapping requires orthologue projection.
- 13 tissues — not exhaustive (e.g. brain microglia, bone marrow not included).
- Cross-disease validation limited to RA and COVID-19; other inflammatory diseases inferred by analogy.

## Counter-evidence

- Some genes are lost during the transformed-matrix step due to gene-set intersection across datasets.
- Cells from disease-specific contexts not represented in the reference may be mis-mapped.
- Cluster #14 corresponds to contaminating CXCL9, CXCL10, IL11-expressing cells; cluster #9 to MNP/T doublets — illustrating residual integration artefacts.

## Linked ideas

(none yet)

## Open questions

- Updating the atlas with newer single-cell multi-omics and spatial datasets.
- Standardised periphery / core / metastasis tumour zonation across more cancer types.
- Validation of MoMac-VERSE-derived signatures as bulk RNA-seq prognostic markers across clinical cohorts.
