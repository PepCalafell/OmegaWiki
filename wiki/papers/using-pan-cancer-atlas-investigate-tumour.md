---
# === Identification ===
title: "Using a pan-cancer atlas to investigate tumour associated macrophages as regulators of immunotherapy response"
slug: using-pan-cancer-atlas-investigate-tumour
arxiv: ""
doi: "10.1038/s41467-024-49885-8"
pmid: "38969631"
venue: "Nature Communications"
year: 2024
authors:
  - "Alexander Coulton"
  - "Jun Murai"
  - "Danwen Qian"
  - "Krupa Thakkar"
  - "Claire E. Lewis"
  - "Kevin Litchfield"
first_author: "Alexander Coulton"
corresponding_author: "Claire E. Lewis; Kevin Litchfield"

# === Source & metadata ===
source_type: pdf
s2_id: "ac24e0e7a39e90599e20a198363cbf479bb3749d"
date_added: 2026-05-13
ingested_date: 2026-05-13
ingest_version: 1
last_reviewed: null

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - tumor-associated-macrophage
  - TAM
  - pan-cancer
  - scRNA-seq
  - macrophage-atlas
  - immune-checkpoint-inhibitor
  - immunotherapy-response
  - CPI1000
  - ECM-macrophage
  - collagen-producing-TAM
  - IFNG-macrophage
  - CXCL9
  - reference-mapping
  - projection
  - macrophage-T-cell-crosstalk
  - MANA-score
  - neoantigen
  - spatial-transcriptomics
  - CosMx
  - melanoma-brain-metastasis
  - CRC-liver-metastasis
keywords:
  - pan-cancer TAM atlas 23 clusters
  - 18_ECMMac collagen-producing macrophage ICI resistance
  - 8_IFNGMac CXCL9 ICI responder TAM
  - CPI1000+ bulk RNAseq ICI cohort 1446 patients
  - gold-standard macrophage signatures bulk deconvolution
  - MANA score TAM-T cell crosstalk lung
  - reference-projection of new scRNAseq datasets
  - melanoma brain metastasis 12_MBMMac LRMDA
  - TREM2 ICIMac1/ICIMac2 melanoma-resistance recapitulation
  - macrophage-fibroblast differentiation ECM signature
domain: "immuno-oncology / tumor immunology / single-cell genomics / pan-cancer atlas / immunotherapy biomarkers"

# === Biomedical domain ===
tissue:
  - lung
  - kidney
  - colon
  - breast
  - skin
  - liver
  - brain
  - esophagus
  - thyroid
  - ovary
  - endometrium
  - pancreas
  - lymph_node
  - blood
condition:
  - cancer
disease_specific:
  - lung_adenocarcinoma
  - lung_squamous_cell_carcinoma
  - small_cell_lung_cancer
  - clear_cell_renal_cell_carcinoma
  - glioblastoma_multiforme
  - colorectal_cancer
  - breast_cancer
  - cutaneous_melanoma
  - melanoma_brain_metastasis
  - esophageal_carcinoma
  - thyroid_carcinoma
  - ovarian_cancer
  - high_grade_serous_ovarian
  - liver_hepatocellular_carcinoma
  - uterine_endometrial_carcinoma
  - basal_cell_carcinoma
  - pancreatic_adenocarcinoma
  - papillary_renal_cell_carcinoma
species:
  - human
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques:
  - scRNA-seq_10x
  - scRNA-seq_MARS-seq
  - scRNA-seq_GEXSCOPE
  - scRNA-seq_InDrop
  - scRNA-seq_SmartSeq2
  - snRNA-seq
  - Seurat_v4
  - Seurat_RPCA_integration
  - Seurat_CCA_integration
  - Harmony_integration
  - Scanorama_integration
  - SCT_normalization
  - Louvain_clustering
  - UMAP
  - hierarchical_clustering
  - SingleR_cell_typing
  - HumanPrimaryCellAtlas_reference
  - UCell_signature_scoring
  - fgsea_pathway_enrichment
  - DESeq2_differential_expression
  - Propeller_cell_composition
  - CosMx_spatial_transcriptomics
  - reference_projection_Seurat
  - iLISI_integration_benchmark
  - RANN_nearest_neighbor
n_samples: "32 studies; 17 cancer types"
n_cells_total: 363315
integration_method: "Seurat V4 RPCA integration with SCT normalization; 23 Louvain clusters on the integrated TAM-only atlas; query-to-reference projection for novel datasets"

# === Biology captured ===
key_cell_types:
  - tumor_associated_macrophage
  - alveolar_macrophage_0_AlvMac
  - metabolic_M2_macrophage_1_MetM2Mac
  - complement_macrophage_2_C3Mac
  - ICIMac1_3_TREM2_SPP1_RNASE1_NUPR1
  - ICIMac2_4_TREM2_APOE_APOC1
  - stress_macrophage_5_StressMac
  - SPP1_AREG_macrophage_6
  - IFN_macrophage_7
  - IFNG_macrophage_8_CXCL9_CXCL10
  - angiogenic_macrophage_9_VEGFA_VCAN_THBS1
  - inflammatory_macrophage_10
  - metallothionein_macrophage_11_MetalloMac
  - melanoma_brain_met_macrophage_12_MBMMac_LRMDA
  - calcium_macrophage_13
  - proliferating_macrophage_14_MKI67_CDK1
  - LYZ_macrophage_15
  - ECM_homeostasis_macrophage_16_ECMHomeoMac
  - IFN_macrophage_17_IFNMac3_ISG15
  - ECM_collagen_macrophage_18_ECMMac_COL1A1
  - classical_monocyte_19_ClassMono
  - T_macrophage_doublet_20_TDoub
  - heme_macrophage_21_HemeMac_CD163_HMOX1
  - IFN_macrophage_22_IFNMac4_IFITM2_LST1
  - CD8_T_cell_neoantigen_reactive_MANA_high
  - tumor_fibroblast
key_markers:
  - FABP4
  - MCEMP1
  - CD52
  - SELENOP
  - SLC40A1
  - PLTP
  - F13A1
  - FUCA2
  - CD163
  - HMOX1
  - C3
  - PLD4
  - HLA-DPA1
  - HLA-DPB1
  - CCL20
  - CXCL3
  - IL1B
  - CXCL2
  - CXCL8
  - CCL2
  - CCL8
  - CCL4L2
  - CCL3L3
  - SPP1
  - CXCL9
  - CXCL10
  - MMP9
  - VAMP5
  - ISG15
  - IFITM2
  - LST1
  - CCL3
  - CCL4
  - TNF
  - TREM2
  - RNASE1
  - NUPR1
  - APOE
  - APOC1
  - HSPA6
  - HSPA1B
  - HSPA1A
  - DNAJB1
  - HSPB1
  - HSPH1
  - HSPD1
  - HSP90AA1
  - BAG3
  - VEGFA
  - VCAN
  - THBS1
  - AREG
  - EREG
  - MKI67
  - CDK1
  - LYVE1
  - FOLR2
  - ARG1
  - HES1
  - LRMDA
  - COL1A1
  - COL1A2
  - COL3A1
  - CD68
  - CXCL13
  - HLA-DRA
  - HLA-DRB1
  - HLA-DRB5
  - HLA-DQA1
  - HLA-DQB1
  - HLA-DPA1
  - HLA-DPB1
  - GZMA
  - GEM
  - ENTPD1
  - TNS3
  - MIR4435-2HG
key_pathways:
  - macrophage_diversity_pan_cancer
  - IFN_gamma_T_cell_recruitment_axis
  - ECM_collagen_deposition_macrophage_fibroblast_differentiation
  - angiogenesis_VEGFA_VCAN
  - heat_shock_response_HSPA_family
  - heme_clearance_CD163_HMOX1
  - MHC_class_II_antigen_presentation_neoantigen_response
  - TREM2_lipid_associated_macrophage_axis
  - SPP1_pro_tumor_M2_axis
  - macrophage_T_cell_crosstalk_spatial
  - immune_checkpoint_inhibitor_response_bulk_RNA_signatures

# === User project membership ===
projects:
  - thesis
priority: high
read_status: deep_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: included
exclusion_reason: null
data_availability: "scRNA-seq atlas as Seurat object: Zenodo 11222158. Code: https://github.com/alexcoulton/macrophage-atlas (Zenodo 10.5281/zenodo.11221774). CPI1000+ bulk RNAseq: 1446 ICI-treated patients (552 bladder, 411 lung, 226 melanoma, 212 RCC, 45 gastric) from refs 115-124. CosMx FFPE lung cancer dataset: open-source NanoString. Oral cancer projection dataset: Luoma et al. 2022."

# === Cross-references ===
code_url: "https://github.com/alexcoulton/macrophage-atlas"
cited_by: []
---

## Problem

The M1/M2 dichotomy is an inadequate framework for tumour-associated macrophage (TAM) diversity, but a pan-cancer scRNA-seq atlas dedicated to TAMs — at sufficient resolution to define rare and previously-undescribed subsets, and at sufficient breadth to cover the major human cancer types — did not exist when this work was undertaken. Prior pan-cancer atlases (Cheng 2021, Nieto 2021, Mulder 2021) integrated broader myeloid or all-immune compartments, leaving TAM-specific resolution under-explored. In parallel, the variable response of cancer patients to immune checkpoint inhibitors (ICIs) is incompletely explained by tumour-cell-intrinsic factors and CD8⁺ T-cell infiltration alone; the contribution of TAM compositional heterogeneity to ICI response is unresolved.

## Key idea

Aggregate 32 public scRNA-seq studies covering 17 human cancer types into a TAM-only pan-cancer atlas of 363,315 cells, cluster at high resolution (23 Louvain clusters) after Seurat RPCA integration, annotate each cluster by canonical and de novo marker genes, and use the resulting cluster-defining signatures as building blocks for: (i) primary-vs-metastatic and tissue-context comparisons, (ii) bulk-RNAseq association with ICI response in an expanded CPI1000+ cohort (n=1446 patients), (iii) spatial validation in CosMx FFPE lung cancer, (iv) TAM-T-cell crosstalk analysis stratified by mutation-associated neoantigen (MANA) score on a 7-study lung secondary atlas, and (v) projection of new datasets onto the atlas as a public reference. The headline biological finding is a novel `18_ECMMac` cluster — TAMs that highly upregulate COL1A1/COL1A2/COL3A1 — enriched in ICI non-responders and likely representing a TAM→fibroblast differentiation pathway. The headline methodological contribution is a set of seven "gold-standard" cluster signatures that retain specificity in an all-cell-type atlas and are therefore suitable for bulk-RNAseq deconvolution.

## Method

Construction of the atlas: 32 published scRNA-seq studies (refs 16, 19-48) covering 17 cancer types selected by literature + GEO search; TAMs extracted using author-provided cell annotations where available, otherwise de novo clustering with a macrophage-signature filter from ref 109 (≥1 SD above dataset-wide mean). Integration: SCT normalization on raw counts; benchmark of Seurat CCA, Seurat RPCA, Harmony, Scanorama against iLISI on a 1.5 TB RAM node — RPCA selected (Seurat CCA failed; Scanorama underperformed unintegrated). Clustering: Seurat v4.2.0 RunPCA, FindNeighbors, FindClusters (resolution tuned); SingleR macrophage/monocyte verification against Human Primary Cell Atlas; UMAP. Annotation: extensive literature search on top DEGs per cluster from FindMarkers.

ICI response association: CPI1000+ bulk RNAseq cohort, 1446 patients across bladder (552), lung (411), melanoma (226), RCC (212), gastric (45), processed via the RIMA pipeline. DESeq2 v1.36.0 with tumour-type and response in the design formula. fgsea v1.22.0 with 10-gene top-DEG signatures per cluster as pathways; FDR q<0.1 significance. Gold-standard signature criterion: re-cluster a separate all-cell-type atlas (482,677 cells from refs 30, 31, 39) without cell-type filtering; compute mean UCell score per signature per cluster; require best-hit cluster to match in ≥3 of 5 cancer types and Metric1 (best - second-best mean UCell) > 0.1.

Cell composition tests: Propeller v0.99.1 with arcsin transformation, FDR-corrected. Hierarchical clustering on per-cluster mean gene expression with Euclidean distance. Spatial: CosMx SMI FFPE open-source NanoString dataset of 5 NSCLC samples (960 genes × 771,236 cells); UCell scoring of 18_ECMMac and 8_IFNGMac signatures with thresholds >0.8 (in-cluster) and <0.4 (out-of-cluster); nearest-neighbour analysis with RANN v2.6.1. MANA score: lung secondary atlas of 31,598 macrophages + 72,585 T cells from 7 lung studies; CD8 T-cell AddModuleScore on the 14-gene MANA signature from ref 98 (CXCL13, HLA-DRA/B/DQA/B/DPA/B/DRB5/DRB1, CCL3, GZMA, GEM, ENTPD1, TNS3, MIR4435-2HG); per-sample upper/lower MANA quartile comparison via Propeller.

Reference projection: Seurat native reference mapping — PCA structure of the integrated atlas projected onto a query dataset for cell-type prediction + UMAP projection for visualization. Demonstrated on the Luoma et al. 2022 oral cancer scRNAseq dataset.

## Results

### 1. Atlas construction (Fig. 1, 2)

- 363,315 TAMs/monocytes from 32 studies, 17 cancer types; 279,104 tumour, 74,982 adjacent normal, 9,229 other (blood/LN).
- 73.8% primary tumour, 18.5% metastatic.
- Lung > ccRCC > GBM the most-represented cancers.
- Mixed platforms (10x Genomics, MARS-seq, GEXSCOPE, In-Drop, Smart-Seq2) + 2 snRNAseq studies.
- Seurat RPCA + Harmony tied as best integration; RPCA chosen.
- 23 Louvain clusters; cluster identities annotated by canonical + de novo markers.

### 2. TAM cluster annotations (Fig. 2)

Major cluster identities (selection):

- `0_AlvMac` — alveolar macrophages (FABP4, MCEMP1, CD52); mostly lung.
- `1_MetM2Mac` — immunoregulatory M2 (SELENOP, SLC40A1, PLTP, F13A1, FUCA2).
- `2_C3Mac` — complement + MHC II (C3, PLD4, HLA-DPA1/DPB1).
- `3_ICIMac1` — TREM2/SPP1/RNASE1/NUPR1; recapitulates a melanoma ICI-resistance signature.
- `4_ICIMac2` — TREM2 + APOE/APOC1 (lipid-associated macrophages).
- `5_StressMac` — heat-shock signature (HSPA1A/1B/6, DNAJB1, HSPB1, HSP90AA1, BAG3).
- `6_SPP1AREGMac` — SPP1/AREG/EREG/CCL20/CXCL3.
- `7_IFNMac` — CCL2/CCL8/CCL4L2/CCL3L3/SPP1.
- `8_IFNGMac` — CXCL9/CXCL10/MMP9/VAMP5 — IFN-γ-driven, T-cell-recruiting.
- `9_AngioMac` — VEGFA/VCAN/THBS1/AREG/EREG/IL1B.
- `10_InflamMac` — CCL3L3/CCL4L2/CXCL8/IL1B/TNF.
- `11_MetalloMac` — metallothioneins.
- `12_MBMMac` — uniquely high LRMDA; melanocyte differentiation factor; melanoma brain metastasis-enriched.
- `13_CalciumMac` — calcium-signaling.
- `14_ProliMac` — MKI67/CDK1 proliferating.
- `15_LYZMac` — LYZ-marked.
- `16_ECMHomeoMac` — ECM homeostasis.
- `17_IFNMac3` — ISG15/CXCL10/CCL8 (interferon-stimulated).
- `18_ECMMac` — **novel** — high COL1A1/COL1A2/COL3A1 + CD68; ECM-modifying, possibly TAM→fibroblast differentiation.
- `19_ClassMono` — classical monocytes.
- `20_TDoub` — TAM-T cell doublets.
- `21_HemeMac` — heme-clearance (CD163, HMOX1, SLC40A1, SELENOP).
- `22_IFNMac4` — IFITM2/LST1 (interferon-exposed).

### 3. Tumour-context shapes macrophage composition (Fig. 3)

- CRC primary, CRC liver metastasis, primary LIHC differ significantly in `6_SPP1AREGMac`, `7_IFNMac`, `8_IFNGMac`, `16_ECMHomeoMac`, `18_ECMMac` proportions (Propeller, FDR-corrected; q for `18_ECMMac` = 8.7e-7).
- GBM, primary cutaneous melanoma (SKCM), SKCM brain metastases differ across `12_MBMMac`, `6_SPP1AREGMac`, `5_StressMac`, `9_AngioMac`, `10_InflamMac`, `11_MetalloMac`, `7_IFNMac`, `4_ICIMac2`, `20_TDoub`, `2_C3Mac` (q-values down to 1.03e-9 for `12_MBMMac`).
- `12_MBMMac` is enriched in melanoma brain metastases vs primary GBM, uniquely upregulating LRMDA — indicative of bidirectional interaction between melanocyte-derived cells and TAMs at the brain metastatic niche.

### 4. TAM signatures associate with ICI response in CPI1000+ (Fig. 4a)

- Responder-enriched (DESeq2 + fgsea, q<0.1): `20_TDoub` (q=1.7e-3), `8_IFNGMac` (q=1.4e-11), `17_IFNMac3` (q=1.8e-8), `14_ProliMac` (q=6.1e-12), `11_MetalloMac` (q=0.036), `4_ICIMac2` (q=2.8e-3), `3_ICIMac1` (q=0.028).
- Non-responder-enriched: `18_ECMMac` (q=3.8e-5).
- T-cell signature is *higher* (not lower) in the upper quartile of `18_ECMMac` signature in CPI1000+ (Mann-Whitney, p<0.0001; n_lower=362, n_upper=723) — ECM-associated ICI resistance is **not** mediated by T-cell exclusion.
- `18_ECMMac` cancer-type distribution: ccRCC (28.2%) > HGSOC (15.4%) > CRC (14.9%).

### 5. Spatial validation of 18_ECMMac (Fig. 4d, e)

- CosMx FFPE NSCLC: cells co-expressing CD68 + COL1A1/COL1A2/COL3A1 identified — confirms TAMs (not just fibroblasts) produce collagen in tissue.
- Some CD68+ "fibroblasts" by signature suggest an intermediate macrophage-fibroblast state.
- Nearest-neighbour: `18_ECMMac`+ TAMs neighbour other TAMs, then fibroblasts; `8_IFNGMac` TAMs neighbour other TAMs, then CD4/CD8 memory T cells, then cancer cells.

### 6. MANA-stratified TAM composition in lung (Fig. 4c)

- Lung secondary atlas: 7 studies, 31,598 macrophages + 72,585 T cells.
- `18_ECMMac` proportion higher in low-MANA samples (Propeller q=0.078).
- `8_IFNGMac` proportion higher in high-MANA samples (q=0.060).

### 7. Gold-standard bulk-RNAseq signatures (Supplementary Data 5–6)

- 7 cluster signatures retain specificity in an all-cell-type atlas (Metric2 ≥ 3/5 cancer types; Metric1 > 0.1): `5_StressMac`, `6_SPP1AREGMac`, `8_IFNGMac`, `11_MetalloMac`, `17_IFNMac3`, `21_HemeMac`, `22_IFNMac4`.

### 8. Atlas as a projection reference (Fig. 5)

- Project Luoma 2022 oral cancer TAMs onto the atlas:
  - C1QB+ TAM → `2_C3Mac`
  - CD14+ Mono → `19_ClassMono`
  - CXCL8+ TAM → `6_SPP1AREGMac`
  - SPP1+ TAM → `16_ECMHomeoMac`
- No `18_ECMMac` cells detected in oral cancer — cancer-type specificity.
- Ma et al. (2022) literature-defined TAM marker genes vary in cluster specificity: MKI67/CDK1 → `14_ProliMac`; LYVE1/FOLR2 → `1_MetM2Mac`; CXCL9 → `8_IFNGMac` (cluster-specific). APOE/APOC1/ARG1/HES1 → broadly distributed.

## All claims (exhaustive)

- `[c01]` A pan-cancer scRNA-seq atlas of 363,315 TAMs across 32 studies and 17 human cancer types yields 23 Louvain clusters after Seurat RPCA integration (p.1-2, Fig. 1, 2a-b) "The total dataset includes 363,315 TAMs or macrophage-like cells... resulting in 23 clusters in total, visualized as a 2-dimensional UMAP" — confidence: high — type: methodological — links: [[concepts/pan-cancer-tam-atlas-23-clusters]] [[foundations/seurat-v3-integration]] [[foundations/scrna-seq-10x-chromium]] [[claims/pan-cancer-tam-atlas-363k-cells-23-clusters]]
- `[c02]` Cluster 18_ECMMac is a previously-undescribed TAM subset characterized by high COL1A1/COL1A2/COL3A1 expression and likely represents a TAM→fibroblast differentiation pathway (p.4, 8, Fig. 4d, S8) "One cluster identified here that is absent from other TAM analyses is 18_ECMMac. These macrophages showed high levels of increased collagen production... This cluster most likely represents an avenue towards fibroblast differentiation" — confidence: high — type: mechanistic — links: [[concepts/ecm-mac-collagen-producing-tam]] [[claims/18-ecmmac-novel-tam-collagen-producing]]
- `[c03]` The 18_ECMMac signature is significantly enriched in non-responders to immune checkpoint inhibitors in the CPI1000+ bulk RNAseq cohort (fgsea q=3.8e-5) (p.5, Fig. 4a) "18_ECMMac was significantly enriched in non-responding patients (fgsea, q-value = 0.000038213695118505)" — confidence: high — type: quantitative — links: [[concepts/ecm-mac-collagen-producing-tam]] [[foundations/cpi1000-plus-ici-cohort]] [[foundations/fgsea-gene-set-enrichment]] [[claims/18-ecmmac-signature-enriched-ici-non-responders]]
- `[c04]` The 8_IFNGMac signature is significantly enriched in responders to ICI in CPI1000+ (fgsea q≈1.4e-11); 17_IFNMac3, 14_ProliMac, 11_MetalloMac, 4_ICIMac2, 3_ICIMac1, and 20_TDoub are also enriched in responders (p.5, Fig. 4a) "20_TDoub and 8_IFNGMac signatures were both significantly enriched in responding patients (fgsea, q-value = 0.001668273617609862 and 0.000000000013715289 respectively)" — confidence: high — type: quantitative — links: [[concepts/ifng-mac-cxcl9-tam-ici-responder]] [[foundations/cpi1000-plus-ici-cohort]] [[foundations/fgsea-gene-set-enrichment]] [[claims/8-ifngmac-signature-enriched-ici-responders]]
- `[c05]` Cluster 8_IFNGMac is defined by CXCL9/CXCL10/MMP9/VAMP5 upregulation, consistent with an IFN-γ-driven T-cell-recruiting phenotype (p.2, Fig. 2c) "Top upregulated genes in cluster 8 include CXCL9, CXCL10, MMP9... VAMP5, which is an interferon-induced gene" — confidence: high — type: mechanistic — links: [[concepts/ifng-mac-cxcl9-tam-ici-responder]] [[foundations/ifn-gamma-cytokine]] [[claims/8-ifngmac-cxcl9-cxcl10-tcell-recruiting]]
- `[c06]` 18_ECMMac proportion differs significantly between primary CRC, CRC liver metastases, and primary LIHC (Propeller q=8.7e-7) (p.4, Fig. 3a) "q-values for 6_SPP1AREGMac, 7_IFNMac, 8_IFNGMac, 16_ECMHomeoMac, 18_ECMMac were 0.0290..., 0.0864..., 0.0392..., 0.0156..., and 0.0000008703445 respectively" — confidence: high — type: quantitative — links: [[concepts/ecm-mac-collagen-producing-tam]] [[foundations/propeller-cell-composition-analysis]] [[claims/18-ecmmac-higher-crc-primary-liver-met-vs-lihc]]
- `[c07]` Cluster 12_MBMMac is enriched in melanoma brain metastases vs primary GBM (Propeller q=1.03e-9) and uniquely upregulates LRMDA, suggesting bidirectional TAM-melanocyte interaction at the brain metastatic niche (p.4, 8, Fig. 3c-d) "q-values for 12_MBMMac... were 0.000000001027255... and not glioblastomas, harboured a large proportion of 12_MBMMac macrophages, which uniquely upregulated LRMDA, a melanocyte differentiation factor" — confidence: high — type: correlational — links: [[concepts/pan-cancer-tam-atlas-23-clusters]] [[foundations/propeller-cell-composition-analysis]] [[claims/12-mbmmac-melanoma-brain-met-lrmda]]
- `[c08]` CosMx spatial transcriptomics on 5 NSCLC tumours identifies cells co-expressing CD68 + COL1A1/COL1A2/COL3A1, confirming that TAMs (not only fibroblasts) produce collagen in situ (p.7, Fig. 4d, S8) "Analysis of the transcript expression revealed cells co-expressing CD68, COL1A1, COL1A2, and COL3A1" — confidence: high — type: methodological — links: [[concepts/ecm-mac-collagen-producing-tam]] [[foundations/cosmx-spatial-transcriptomics]] [[foundations/ucell-signature-scoring]] [[claims/18-ecmmac-spatial-cd68-collagen-coexpression]]
- `[c09]` Nearest-neighbour analysis in CosMx shows 18_ECMMac+ TAMs are closest to other TAMs followed by fibroblasts, while 8_IFNGMac TAMs are closest to other TAMs followed by CD4/CD8 memory T cells and cancer cells (p.7, Fig. 4e) "the closest neighbouring cells to 18_ECMMac+ TAMs were other TAMs followed by fibroblasts... the closest neighbours to 8_IFNGMac TAMs were other TAMs, followed by CD4 memory T cells, cancer cells and CD8 memory T cells" — confidence: high — type: correlational — links: [[concepts/ecm-mac-collagen-producing-tam]] [[concepts/ifng-mac-cxcl9-tam-ici-responder]] [[foundations/cosmx-spatial-transcriptomics]] [[claims/ecmmac-fibroblast-ifngmac-tcell-spatial-neighbors]]
- `[c10]` 18_ECMMac proportion anticorrelates with MANA-score quartile in lung cancer (Propeller q=0.078), while 8_IFNGMac is enriched in high-MANA samples (q=0.060), linking TAM composition to neoantigen-reactive T-cell activation (p.7, Fig. 4c) "We observed significantly higher proportions of 18_ECMMac in samples in the lower quartile of MANA scores compared to the upper quartile... 8_IFNGMac was significantly enriched in the upper quartile" — confidence: medium — type: quantitative — links: [[concepts/mana-score-neoantigen-tcell-signature]] [[concepts/ecm-mac-collagen-producing-tam]] [[concepts/ifng-mac-cxcl9-tam-ici-responder]] [[foundations/propeller-cell-composition-analysis]] [[claims/18-ecmmac-anticorrelates-mana-score-lung]]
- `[c11]` 18_ECMMac-associated ICI resistance is not explained by T-cell exclusion: the general T-cell signature is significantly higher (not lower) in the upper quartile of 18_ECMMac signature in CPI1000+ (Mann-Whitney p<0.0001, W=74219, n_lower=362, n_upper=723) (p.5, Fig. 4b) "we observed significantly higher (Two-sided Mann-Whitney U test... p < 0.0001; W = 74219... T-cell signatures associated in the upper quartile of ECM signature samples in the CPI1000+, indicating that general T cell exclusion might not be the mechanism" — confidence: high — type: correlational — links: [[concepts/ecm-mac-collagen-producing-tam]] [[foundations/cpi1000-plus-ici-cohort]] [[claims/18-ecmmac-not-via-tcell-exclusion]]
- `[c12]` Seurat RPCA outperforms Scanorama and ties Harmony in iLISI integration benchmark on a TAM-only pan-cancer atlas; Seurat CCA failed at 1.5 TB RAM (p.10, Methods) "Seurat CCA failed to run successfully... Scanorama produced lower iLISI scores than the unintegrated data, whilst Harmony and Seurat RPCA performed similarly" — confidence: high — type: methodological — links: [[foundations/seurat-v3-integration]] [[concepts/pan-cancer-tam-atlas-23-clusters]] [[claims/seurat-rpca-best-pan-tam-integration]]
- `[c13]` Seven TAM cluster signatures (5_StressMac, 6_SPP1AREGMac, 8_IFNGMac, 11_MetalloMac, 17_IFNMac3, 21_HemeMac, 22_IFNMac4) meet "gold-standard" criteria for cluster-specific detection in an all-cell-type atlas and are recommended for bulk-RNAseq deconvolution (p.4, 10, Supplementary Data 5-6) "we defined a set of macrophage-specific 'gold-standard' signatures, which consistently identified their respective macrophage clusters when assessed via UCell scores... namely for clusters 5_StressMac, 6_SPP1AREGMac, 8_IFNGMac, 11_MetalloMac, 17_IFNMac3, 21_HemeMac and 22_IFNMac4" — confidence: high — type: methodological — links: [[concepts/gold-standard-bulk-tam-signatures]] [[foundations/ucell-signature-scoring]] [[claims/seven-gold-standard-tam-bulk-signatures]]
- `[c14]` The Luoma 2022 oral cancer scRNAseq TAMs project onto the atlas with a stable mapping: C1QB+ TAM → 2_C3Mac, CD14+ Mono → 19_ClassMono, CXCL8+ TAM → 6_SPP1AREGMac, SPP1+ TAM → 16_ECMHomeoMac; 18_ECMMac is absent in oral cancer (p.9, Fig. 5a-b) "TAMs classified as C1QB+ TAMs by the authors primarily mapped to our 2_C3Mac cluster... CXCL8+ TAM mapped to 6_SPP1AREGMac and SPP1+ TAMs mapped to 16_ECMHomeoMac... There were no 18_ECMMac TAMs detected in the oral cancer dataset" — confidence: high — type: methodological — links: [[concepts/scrna-atlas-as-reference-projection]] [[concepts/ecm-mac-collagen-producing-tam]] [[claims/oral-cancer-tam-projection-validates-atlas]]
- `[c15]` Literature-proposed TAM subset-defining markers (Ma et al. 2022) vary in atlas-level specificity: MKI67/CDK1 (proliferating), LYVE1/FOLR2 (tissue-resident M2), CXCL9 (IFNG) are cluster-specific, while APOE/APOC1/ARG1/HES1 are distributed across many clusters (p.9, Fig. 5c-d) "Markers attributed to proliferating macrophages, including MKI67 and CDK1 can be attributed to the former category... Markers distributed among a large number of clusters included APOE, APOC1, ARG1 and HES1" — confidence: high — type: mechanistic — links: [[concepts/pan-cancer-tam-atlas-23-clusters]] [[concepts/m1-m2-polarization-paradigm]] [[claims/ma-markers-vary-cluster-specificity]]
- `[c16]` A secondary lung-cancer atlas integrating 7 lung studies contains 31,598 macrophages + 72,585 T cells and is used to stratify TAM composition by per-sample MANA score quartile (p.10, Methods) "we combined a second, smaller atlas of lung cancers from 7 studies, consisting of 31598 macrophages and 72585 T cells" — confidence: high — type: methodological — links: [[concepts/mana-score-neoantigen-tcell-signature]] [[claims/lung-secondary-atlas-31k-mac-72k-tcell-mana]]
- `[c17]` The atlas is publicly distributed as a Seurat object via Zenodo (accession 11222158) with code at github.com/alexcoulton/macrophage-atlas, enabling reference-mapping of new datasets onto the 23 TAM clusters (p.11, Data availability) "The scRNAseq atlas generated in this study has been deposited in Zenodo as a Seurat object under accession code 11222158" — confidence: high — type: methodological — links: [[concepts/scrna-atlas-as-reference-projection]] [[claims/pan-cancer-tam-atlas-public-zenodo-projection-ready]]
- `[c18]` TREM2-expressing TAMs in clusters 3_ICIMac1 (SPP1/RNASE1/NUPR1) and 4_ICIMac2 (APOE/APOC1) partially recapitulate a melanoma immunotherapy-resistance gene signature; both are nonetheless enriched in CPI1000+ responders (p.3, 5, Fig. 2c, 4a) "Cluster 3 TAMs... partially recapitulated a gene signature that has been associated with immunotherapy resistance in melanoma, with high expression of SPP1, RNASE1, NUPR1 and TREM2... 4_ICIMac2 and 3_ICIMac1 were significantly enriched in responders" — confidence: medium — type: correlational — links: [[concepts/trem2-tumor-associated-macrophage]] [[foundations/trem2-receptor]] [[claims/trem2-tams-recapitulate-melanoma-ici-resistance]]

## Discussion captured

### Authors' interpretation

The atlas establishes that TAM characterization should move beyond M1/M2 to a high-resolution multi-cluster taxonomy that captures functional diversity arising from ontogeny + local stimuli. The novel 18_ECMMac cluster is the key biological finding: collagen-producing TAMs likely represent an avenue towards fibroblast differentiation, are enriched in ccRCC, HGSOC, CRC and lung tumours, and predict poor ICI response. The mechanism is not T-cell exclusion (T-cell infiltration is in fact *higher* in high-ECM tumours), implicating instead a more nuanced TAM-fibroblast-T-cell interaction. The authors connect this to a recent breast-cancer finding that collagen-producing macrophages restrict CD8 function (ref 106). On the responder side, 8_IFNGMac (CXCL9/CXCL10) and TREM2+ clusters (3_ICIMac1, 4_ICIMac2) are signatures of an ICI-permissive microenvironment. The gold-standard signature set is offered as a deployable bulk-RNAseq deconvolution tool for ICI patient stratification.

### Comparisons with prior literature (made by authors)

- **Ma et al. 2022 Trends Immunol (ref 14)**: proposed a seven-part TAM model + spectrum. This atlas validates cluster specificity of some Ma markers (CXCL9, MKI67, LYVE1) but shows others (APOE, APOC1, ARG1, HES1) are broadly distributed and not subset-defining.
- **Cheng 2021 Cell (ref 16)**: pan-cancer myeloid atlas; broader scope, lower TAM-specific resolution.
- **Mulder 2021 Immunity (ref 18)**: cross-tissue MNP atlas (MoMac-VERSE); complementary but not pan-tumour and not focused on bulk-RNAseq deconvolution. 18_ECMMac is absent from Mulder.
- **Nieto 2021 Genome Res (ref 17)**: single-cell tumour immune atlas; all-immune scope.
- **Mills 2000 J Immunol (ref 13)**: original M1/M2 paradigm — explicitly superseded.
- **Nahrendorf 2016 Circ Res (ref 15)**: network model of macrophage function — congruent with the high-resolution view here.
- **Macrophage TREM2-ICI literature (ref 71)**: experimental TREM2 inhibition potentiates ICI in mice — connects to 3_ICIMac1/4_ICIMac2 in this atlas.
- **APOC1 inhibition (ref 74)**: APOC1 inhibition reverses M2 polarization and enhances anti-PD-1 in HCC — connects to 4_ICIMac2.
- **Collagen-producing macrophages in BC (ref 106)**: restrict CD8 function — provides mechanistic precedent for the 18_ECMMac–ICI resistance link.
- **Luoma 2022 oral cancer scRNAseq (ref 100)**: used as the projection-test dataset.
- **Lung histology / driver genotype and ICI (ref 107)**: orthogonal axis the atlas does not yet integrate.

### Mechanistic hypotheses proposed

- 18_ECMMac represents an intermediate state along a TAM-to-myofibroblast differentiation trajectory; some "fibroblasts" co-expressing CD68 in CosMx may be intermediate cells.
- The 18_ECMMac–ICI resistance link is mediated by TAM-fibroblast-T-cell crosstalk and ECM remodeling, not bulk T-cell exclusion.
- 8_IFNGMac (CXCL9+) recruits and engages T cells, explaining its responder enrichment; spatial nearest-neighbour data support this.
- LRMDA upregulation in 12_MBMMac suggests cross-talk with melanocytic cells at the brain metastasis niche shapes macrophage identity.
- The breadth of cancer types harbouring 18_ECMMac (ccRCC > HGSOC > CRC) suggests tumour-type-specific environmental cues drive this differentiation, with CRC genotype influencing the differentiation pathway in the liver metastatic context.

### Caveats and self-criticism

- 18_ECMMac signature contains collagen genes also expressed by fibroblasts; bulk-RNAseq associations cannot be uniquely attributed to TAMs versus fibroblasts.
- Other non-gold-standard signatures may also be influenced by non-macrophage cell types.
- Detailed analysis of lung-cancer driver genotype × TAM composition was infeasible due to limited metadata.
- The atlas is read-only — no perturbation data are integrated.

### Future directions suggested

- Detailed lung-cancer driver-genotype × TAM-composition analysis when metadata become available.
- Study 18_ECMMac in more detail, including perturbation studies to confirm the TAM→fibroblast differentiation hypothesis.
- Expand projection use-cases: oral cancer is one example; encouraged for any new TAM dataset.
- Cross-link TAM atlas with non-TAM immune compartments to map intercellular signalling.

## Limitations

- TAM extraction is heterogeneous across the 32 input studies (some author-annotated, some de novo).
- snRNA-seq vs scRNA-seq batch effects partially mitigated by RPCA but not formally controlled.
- Cluster boundaries are partly resolution-dependent; rare populations may be merged.
- "Gold-standard" criterion is conservative (3/5 cancer types, Metric1 > 0.1) — other signatures may still be useful in specific contexts.
- 18_ECMMac causal role in ICI resistance is associative, not perturbed.
- No protein-level validation of cluster-defining markers beyond CosMx for COL1A1/COL1A2/COL3A1 + CD68.
- CPI1000+ cohort heterogeneity (5 cancer types, mixed agents) is controlled in the design formula but not stratified per agent.

## Open questions

- Is 18_ECMMac a stable terminal state or a transient transition state toward myofibroblast identity?
- Can perturbation of TAM→fibroblast differentiation reverse ICI resistance in 18_ECMMac-high tumours?
- Do collagen-producing TAMs share an ontogenetic origin (monocyte-derived vs tissue-resident) across cancer types?
- Why is 18_ECMMac absent in oral cancer? Is collagen-TAM induction tumour-type-restricted by stromal context or tumour-cell-intrinsic factors?
- How does 18_ECMMac coordinate with cancer-associated fibroblasts (CAFs) — competition, complementarity, or co-differentiation?
- Are the 8_IFNGMac and 18_ECMMac axes orthogonal predictors that can be combined into a multivariate ICI-response classifier?
- Do hypoxia-driven TAM states (relevant to the user's thesis) preferentially seed 18_ECMMac or other ECM-modifying clusters?

## My take

This is a high-utility resource paper: a TAM-specific pan-cancer atlas at 23-cluster resolution, paired with a deployable bulk-RNAseq deconvolution toolkit (7 gold-standard signatures) and an associative biomarker for ICI response. The 18_ECMMac discovery is the headline biological contribution and is corroborated by both spatial validation (CosMx) and an explicit refutation of the obvious confounder (T-cell exclusion). The TREM2/ICIMac dual response-enrichment is a counterintuitive finding worth following up — TREM2 inhibition is generally considered ICI-potentiating yet TREM2+ clusters here associate with response. For ΩmegaWiki the atlas serves three roles: (i) a reference for projecting future hypoxia-focused TAM scRNAseq onto a pan-cancer backdrop, (ii) a source of cluster-level signatures for bulk-RNAseq deconvolution in lung and ccRCC cohorts (both hypoxia-relevant), and (iii) a paradigm-shifting datapoint for the TAM-fibroblast axis in cancer ECM remodelling. The Litchfield lab's CPI1000+ cohort is also a valuable cross-paper resource. Limitations: associative, no perturbation, collagen-signature/fibroblast confound is acknowledged but not fully resolved.

## Related

- [[concepts/pan-cancer-tam-atlas-23-clusters]]
- [[concepts/ecm-mac-collagen-producing-tam]]
- [[concepts/ifng-mac-cxcl9-tam-ici-responder]]
- [[concepts/scrna-atlas-as-reference-projection]]
- [[concepts/mana-score-neoantigen-tcell-signature]]
- [[concepts/gold-standard-bulk-tam-signatures]]
- [[concepts/m1-m2-polarization-paradigm]]
- [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]]
- [[concepts/tumor-associated-macrophage-immunosuppression]]
- [[concepts/trem2-tumor-associated-macrophage]]
- [[concepts/momac-verse-mnp-verse-atlas]]
- [[concepts/mononuclear-phagocyte-system]]
- [[foundations/cpi1000-plus-ici-cohort]]
- [[foundations/ucell-signature-scoring]]
- [[foundations/propeller-cell-composition-analysis]]
- [[foundations/fgsea-gene-set-enrichment]]
- [[foundations/deseq2-differential-expression]]
- [[foundations/cosmx-spatial-transcriptomics]]
- [[foundations/singler-cell-type-annotation]]
- [[foundations/seurat-v3-integration]]
- [[foundations/ifn-gamma-cytokine]]
- [[foundations/trem2-receptor]]
- [[foundations/scrna-seq-10x-chromium]]
- [[papers/pd-l1-expressing-tumor-associated-macrophages]]
- [[papers/cross-tissue-single-cell-landscape-human]]
- [[people/alexander-coulton]]
- [[people/kevin-litchfield]]
- [[people/claire-e-lewis]]
