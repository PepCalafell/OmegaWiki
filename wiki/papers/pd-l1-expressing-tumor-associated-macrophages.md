---
# === Identification ===
title: "PD-L1-expressing tumor-associated macrophages are immunostimulatory and associate with good clinical outcome in human breast cancer"
slug: pd-l1-expressing-tumor-associated-macrophages
arxiv: ""
doi: "10.1016/j.xcrm.2024.101420"
pmid: "38382468"
venue: "Cell Reports Medicine"
year: 2024
authors:
  - "Lei Wang"
  - "Weihua Guo"
  - "Zhikun Guo"
  - "Jiangnan Yu"
  - "Jiayi Tan"
  - "Diana L. Simons"
  - "Ke Hu"
  - "Xinyu Liu"
  - "Qian Zhou"
  - "Yizi Zheng"
  - "Egelston A. Colt"
  - "John Yim"
  - "James Waisman"
  - "Peter P. Lee"
first_author: "Lei Wang"
corresponding_author: "Lei Wang; Peter P. Lee"

# === Source & metadata ===
source_type: pdf
s2_id: "cf9860a670ce2ff78a3b5c42780c9adc71af2e72"
date_added: 2026-05-12
ingested_date: 2026-05-12
ingest_version: 1
last_reviewed: null

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - PD-L1
  - tumor-associated-macrophage
  - TAM
  - breast-cancer
  - scRNA-seq
  - SIGLEC15
  - multiplex-immunofluorescence
  - mIF
  - immunotherapy
  - immune-checkpoint
  - CD8-T-cell
  - IFN-gamma
  - ERK
  - macrophage-maturation
  - METABRIC
  - TCGA
keywords:
  - PD-L1 macrophage paradox
  - PD-L1+ TAM immunostimulation
  - SIGLEC15 PD-L1 mutually exclusive
  - monocyte-macrophage maturation PD-L1
  - IFN-gamma independent PD-L1 induction
  - ERK-dependent PD-L1 monocyte
  - PD-L1+/PD-L1- TAM density ratio
  - PD-L1 TAM RFS breast cancer
  - spatial TAM T-cell interaction mIF
  - CellPhoneDB CellChat TAM T-cell
domain: "immuno-oncology / tumor immunology / single-cell genomics"

# === Biomedical domain ===
tissue:
  - breast
  - blood
  - in_vitro_only
condition:
  - cancer
disease_specific:
  - breast_cancer_luminal_ER_positive
  - breast_cancer_TNBC
species:
  - human
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques:
  - scRNA-seq_10x
  - flow_cytometry
  - phosflow_cytometry
  - multiplex_immunofluorescence
  - ELISA
  - CD8_T_cell_coculture
  - phagocytosis_assay_pHrodo
  - BiTE_blinatumomab_cytotoxicity_assay
  - CellPhoneDB
  - CellChat
  - CIBERSORT_deconvolution
  - Seurat_v3_integration
  - UMAP_clustering
  - GSEA
  - METABRIC_survival_analysis
  - TCGA_survival_analysis
  - HOMER_motif_analysis
n_samples: 5
n_cells_total: 2220
integration_method: "Seurat (in-house scRNA-seq); cluster-level dichotomization via PD-L1/SIGLEC15 mutual exclusivity"

# === Biology captured ===
key_cell_types:
  - tumor_associated_macrophage_PD-L1_pos
  - tumor_associated_macrophage_PD-L1_neg
  - peripheral_blood_monocyte
  - monocyte_derived_macrophage
  - CD8_T_cell
  - CD4_T_cell
  - cytokeratin_pos_cancer_cell
  - SIGLEC15_pos_TAM
key_markers:
  - CD274_PD-L1
  - SIGLEC15
  - CD68
  - CD83
  - HLA-DR
  - CD74
  - IL1B
  - CXCL8
  - CCL4
  - C1QA
  - C1QB
  - SPP1
  - MMP9
  - SPARC
  - FABP4
  - FN1
  - COL1A1
  - IFNGR1
  - pSTAT1
  - CD80
  - CD86
  - PD-L2
  - B7-H3
  - CSF1R
  - ICAM1
  - AREG
  - ANXA1
  - MIF
key_pathways:
  - IFN-gamma_independent_PD-L1_induction
  - ERK1_2_MAPK_signaling
  - JAK_STAT1_IFN_response
  - PD-L1_PD-1_T_cell_checkpoint
  - CellPhoneDB_AREG_ICAM1_CD162_CD62L
  - MHC_class_II_antigen_presentation
  - SPP1_VEGFA_pro_tumor_secretion
  - integrin_alphaVbeta1_alpha2beta1_ECM_binding

# === User project membership ===
projects:
  - thesis
priority: high
read_status: deep_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: included
exclusion_reason: null
data_availability: "Public scRNA-seq data: Azizi 2018 GSE114727; Pal 2021 EGAS00001004809; Bassez 2021 EGAS00001004809. In-house scRNA-seq processed counts and code likely available via corresponding author. Bulk transcriptomics: METABRIC (cBioPortal) and TCGA (PanCancerAtlas)."

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

PD-L1 expression on tumor-associated macrophages (TAMs) is a long-standing puzzle in cancer immunology. Murine tumor models and bioinformatic predictions classify PD-L1+ TAMs as immunosuppressive — extrapolating from cancer-cell PD-L1 biology. Yet clinical observations across lung, liver, and breast cancer consistently report that PD-L1 expression on macrophages correlates with *better* prognosis and stronger response to anti-PD-1/PD-L1 immune checkpoint inhibitors than tumor-cell PD-L1. Single-cell transcriptomic profiling has been limited by PD-L1 (CD274) dropout, which is a low-abundance transcript poorly captured by droplet-based scRNA-seq. The functional significance of PD-L1 expression on human TAMs — and whether the murine-derived immunosuppressive interpretation holds in human tumors — has remained unresolved.

## Key idea

PD-L1 on human breast TAMs is a *maturation/activation marker* of an immunostimulatory subset, not a checkpoint of immunosuppression. The authors operationalize a SIGLEC15-based dichotomization to circumvent PD-L1 transcript dropout (SIGLEC15 is mutually exclusive with PD-L1 in TAMs and reliably captured) and integrate four orthogonal axes of evidence: (i) scRNA-seq DEGs show PD-L1+/hi TAMs upregulate antigen-presentation/maturation (CD83, HLA-DR), pro-inflammatory cytokines (IL1B, CXCL2/3/8, CCL3/4), and complement; PD-L1−/lo TAMs upregulate pro-tumor SPP1/MMP9/ECM/FA-metabolism genes; (ii) PD-L1+/PD-L1− gene-signature ratio in METABRIC (n=1098) and TCGA (n=789) is a robust prognostic biomarker for RFS in luminal and TNBC breast cancer; (iii) multiplex immunofluorescence on n=36 fresh tumors shows PD-L1+ TAMs spatially engage T cells (<20 μm) while PD-L1− TAMs engage cancer cells; CellPhoneDB+CellChat identify AREG-ICAM1, ANXA1, MIF as TAM↔T-cell mediators; (iv) ex vivo functional assays demonstrate PD-L1+ macrophages stimulate CD8+ T cell proliferation more than PD-L1− and do not suppress BiTE-mediated killing, while PD-L1− macrophages suppress — and PD-L1 blockade does not modify either effect. Mechanistically, PD-L1 is upregulated during monocyte-to-macrophage maturation in serum-free medium under IFN-γ/IFN-γR blockade, partially blocked by ERK1/2 inhibitor SCH772984. PD-L1+ monocytes have higher IFN-γR1 and stronger ΔpSTAT1 response to IFN-γ — primed, not refractory. In two independent in-house cohorts of FFPE breast tumors (n=49 + n=93), the PD-L1+/PD-L1− TAM density ratio is an independent prognostic factor for RFS (multivariate p=0.0099). The work *reverses the paradigm* of PD-L1+ TAMs as immunosuppressive and reframes PD-L1 on myeloid cells as a marker of immune-active TIME.

## Method

In-house scRNA-seq (10x Genomics) of freshly digested untreated primary luminal breast tumors (n=4); Seurat pipeline, UMAP, sub-clustering of myeloid → TAM clusters (8 clusters, 2220 cells). PD-L1/SIGLEC15 cluster-level dichotomization. Replicated on public scRNA-seq: Pal 2021 TNBC (n=8, 4484 TAMs in 11 clusters); Bassez 2021 anti-PD1-treated BC (n=19, 12952 TAMs in 13 clusters). Flow cytometry of PD-L1 protein on CD14+HLA-DR+ TAMs and BC cell populations from matched tumors. ELISA on flow-sorted PD-L1+/− TAMs (16h supernatants) for IL1β/CCL4. Bulk-tumor survival: gene signatures from top DEGs intersecting in-house and public scRNA-seq; METABRIC (n=1098 luminal + n=269 TNBC) and TCGA (n=789); top 25% vs bottom 25%; Kaplan-Meier + log-rank. mIF on FFPE tissues (n=36 fresh + n=49 cohort 1 whole-slide + n=93 cohort 2 TMA): PD-L1, CD68, CD3, CD8, cytokeratin, DAPI; spatial cell-cell distance <20 μm. CellPhoneDB + CellChat on scRNA-seq for receptor-ligand interactions. CIBERSORT deconvolution of METABRIC bulk RNA-seq for cell composition. Ex vivo monocyte/macrophage maturation: BC patient PBMCs rested 8h in RPMI + 10% FBS (or serum-free + anti-IFN-γ/anti-IFN-γR antibodies); flow + phosflow for PD-L1, CD54/69/83, CD40/80/86, PD-L2/B7-H3/B7-H4, CD16/32/64, CSF1R/CCR5, pSTAT1/STAT3/mTOR/Akt. Small-molecule inhibitor screen (n=6 patients) with SCH772984 (ERK1/2 0.5 μM), fludarabine (STAT1 50 μM), MK-2206 (Akt 0.5 μM), LY294002 (PI3K 5 μM), QNZ (NF-κB 5 μM), rapamycin (mTOR 0.1 μM). Phagocytosis assay: pHrodo Green E. coli bioparticles + flow. CD8+ T cell proliferation assay: CellTrace-labeled autologous T cells co-cultured with flow-sorted PD-L1+/− monocytes, TCR-stimulated 4 days. BiTE-mediated cytotoxicity: CD8+ T cells + CD19+ K562 + CD3/CD19 bispecific antibody (blinatumomab) + autologous PD-L1+/− monocytes, 2 days; flow for K562 killing, CD8+ PD-1/CD137. Cox proportional hazards multivariate model on combined cohorts 1+2 (n=142) adjusting for age, tumor stage, grade, nodal status.

## Results

### 1. scRNA-seq + SIGLEC15 dichotomization reveal mature/inflammatory PD-L1+ TAMs and pro-tumor PD-L1− TAMs (Fig. 1)
- 8 TAM clusters in in-house BC scRNA-seq; PD-L1 and SIGLEC15 mutually exclusive.
- PD-L1+/hi TAMs: maturation (CD83, CD74, HLA-DRA/B), pro-inflammatory cytokines (IL1B, CXCL2/3/8, CCL3/4/18), complement C1Q, AP-1 transcriptional activators (FOS, JUNB, CEBPD).
- PD-L1−/lo TAMs: anti-inflammatory (CD9, CD52, IL1RN, CSTB), pro-tumor (SPP1, MMP9, SPARC), fatty acid metabolism (FABP4/5, LPL), ECM (FN1, COL1A1/2, COL3A1).
- Flow PD-L1+% concordant with scRNA-seq dichotomization.
- ELISA: PD-L1+ TAMs secrete more IL1β and CCL4.
- GSEA: PD-L1+/hi enriched for inflammatory response; PD-L1−/lo enriched for EMT hallmark.
- M1/M2 gene signatures common to both subsets — PD-L1 axis is orthogonal to canonical polarization.

### 2. Pattern generalizes to TNBC and anti-PD1-treated cohorts (Fig. 2)
- Pal 2021 TNBC: mutually exclusive PD-L1/SIGLEC15; DEGs reproduce maturation (HLA-DQ, IL1B, C1Q, FOSB, CEBPD) vs pro-tumor (CD9, IL1RN, SPP1, TREM2, FABP4/5, LPL, FN1).
- Bassez 2021 anti-PD1-treated TNBC: PD-L1+/hi TAM abundance higher in tumors with clonally-expanded intratumoral PD-1+ T cells — i.e., PD-L1+ TAMs do not suppress T-cell expansion.

### 3. PD-L1+ TAM gene signatures predict better RFS in METABRIC + TCGA (Fig. 3 A-C)
- METABRIC (n=1098): PD-L1+/hi top 25% vs bottom 25% — RFS p=0.001 (better); PD-L1−/lo p=0.036 (worse); ratio p<0.0001.
- TCGA (n=789): PD-L1+/hi p=0.014; PD-L1−/lo p=0.036; ratio p=0.032.
- TNBC METABRIC (n=269): PD-L1+/hi signature p significant.
- M1, M2, M1/M2 ratio signatures: no significant correlation — PD-L1 axis is the prognostically informative one.
- CIBERSORT: PD-L1+/hi-high tumors have more M1 macrophages, CD4+ memory resting T cells, CD8+ T cells.
- PD-L1+/hi correlates with CD8A expression (METABRIC r=0.52, TCGA r=0.6, p<0.0001 both).

### 4. PD-L1+/PD-L1− TAM density ratio is independent prognostic factor (Fig. 3 D-I)
- Cohort 1 (n=49 whole-slide mIF): PD-L1+ below-median → worse RFS (p=0.038); PD-L1− above-median → worse RFS (p=0.046).
- Cohort 2 (n=93 TMA): replicates (p=0.02 and p=0.01).
- Combined (n=142): PD-L1+/PD-L1− density ratio above-median → better RFS (p=0.0003), trend better OS (p=0.08).
- Multivariate (age, stage, grade, nodal): density ratio p=0.0099 — independent prognostic.
- Total CD68 TAM density: no correlation.
- PD-L1+ TAM density higher in TNBC than luminal; no association with grade, T, or N.

### 5. PD-L1+ TAMs spatially engage T cells; PD-L1− TAMs engage cancer cells (Fig. 4)
- mIF n=36 fresh tumors: within 20 μm, PD-L1+ TAMs have more CD8+ and CD4+ T cells; PD-L1− TAMs have more cancer cells.
- PD-L1− TAMs (not PD-L1+) self-cluster.
- CellPhoneDB+CellChat: PD-L1+ TAMs preferentially interact with T cells via AREG-ICAM1, CD162-CD62L (contact), ANXA1, MIF (secreted); PD-L1− TAMs interact with cancer cells via FN1-integrin αVβ1, COL6A2-integrin α2β1, SPP1, VEGFA.

### 6. PD-L1 is upregulated during monocyte-macrophage maturation IFN-γ-independently, partly via ERK (Fig. 5)
- Fresh monocytes PD-L1-low; 8h ex vivo resting → significant upregulation.
- Adherent > suspension monocytes for PD-L1.
- M-CSF differentiation → uniformly PD-L1+ macrophages.
- Serum-free + anti-IFN-γ + anti-IFN-γR: PD-L1 still upregulates (n=5, p<0.05) — IFN-γ-independent.
- PD-L1+ monocytes co-upregulate maturation/MHC-II/co-stim/co-inh/Fcγ/chemokine receptor markers, pSTAT1/STAT3/mTOR/Akt.
- ERK inhibitor SCH772984 (0.5 μM) significantly blocks PD-L1 upregulation; STAT1, Akt, PI3K, NF-κB, mTOR inhibitors do not.

### 7. PD-L1+ TAMs are primed for IFN-γ response — opposite to cancer cells (Fig. 6)
- PD-L1+ monocytes (n=28): higher ΔpSTAT1+% after IFN-γ stimulation (p<0.01); higher IFN-γR1 surface MFI (n=20, p<0.001).
- IFN-γ dose-response: simultaneous PD-L1↑ and IFN-γR1↓ on monocytes (n=6).
- Replicated in TAMs from fresh primary tumors (n=8); confirmed by mIF.
- Cancer cells: opposite — PD-L1−/lo BC cells have higher ΔpSTAT1+% (n=8, p<0.0001).

### 8. PD-L1+ macrophages stimulate; PD-L1− macrophages suppress — PD-L1:PD-1-independent (Fig. 7)
- pHrodo phagocytosis (n=16): PD-L1+ > PD-L1− monocytes.
- CD8+ T cell proliferation (CellTrace, n=6): PD-L1+ macrophages stimulate; PD-L1− do not. CD4+ stimulation similar between subsets.
- BiTE cytotoxicity (CD3/CD19, K562-CD19+, n=6): PD-L1− macrophages suppress CD8+ T cell killing; PD-L1+ do not.
- Anti-PD-L1 blocking antibody: does not change either readout — function is PD-L1:PD-1-independent.

## All claims (exhaustive)

- `[c01]` PD-L1 and SIGLEC15 are mutually exclusively expressed in human breast TAMs, enabling cluster-level dichotomization in scRNA-seq (p.2-3, Fig. 1B-E, S1F, S4A-C, S6G) "PD-L1+SIGLEC15− (range from 39.4% to 73.5%) vs. PD-L1−SIGLEC15+ (range from 26.5% to 60.6%) populations" — confidence: high — type: methodological — links: [[concepts/siglec15-pd-l1-mutually-exclusive-tam-dichotomization]] [[foundations/siglec15-checkpoint-ligand]] [[foundations/pd-l1-cd274]] [[claims/pd-l1-siglec15-mutually-exclusive-tam-scrnaseq]]
- `[c02]` PD-L1+/hi TAMs upregulate maturation markers (CD83, HLA-DRA/B), pro-inflammatory cytokines (IL1B, CXCL2/3/8, CCL3/4), and complement (C1QA/B/C) (p.3, Fig. 1G-J, S4D) "PD-L1+/hi TAMs had higher levels of macrophage maturation marker genes (e.g., CD83, CD74, HLA-DRA/B, and HLA-DQA/B), pro-inflammatory genes... cytokines/chemokines (e.g., IL1B, CXCL2/3/8, and CCL3/4/18) and complement components (e.g., C1QA/B/C)" — confidence: high — type: correlational — links: [[concepts/pd-l1-immunostimulatory-tam-phenotype]] [[foundations/pd-l1-cd274]] [[claims/pd-l1-pos-tams-upregulate-maturation-proinflammatory-genes]]
- `[c03]` PD-L1−/lo TAMs upregulate pro-tumor genes (SPP1, MMP9, SPARC), fatty acid metabolism (FABP4/5, LPL), and ECM organization (FN1, COL1A1/2, COL3A1) (p.3, Fig. 1G,I, S4D-E) "PD-L1−/lo TAMs had higher expression of anti-inflammatory genes... genes with pro-tumor functions (e.g., osteopontin [SPP1], MMP9, and SPARC), genes involved in fatty acid metabolism (e.g., FABP4/5 and LPL), and genes involved in extracellular matrix organization (e.g., fibronectin 1 [FN1], COL1A1/2, and COL3A1)" — confidence: high — type: correlational — links: [[concepts/pd-l1-immunostimulatory-tam-phenotype]] [[concepts/tumor-associated-macrophage-immunosuppression]] [[claims/pd-l1-neg-tams-upregulate-pro-tumor-ecm-fa-genes]]
- `[c04]` PD-L1+/hi vs PD-L1−/lo TAM dichotomy is orthogonal to the canonical M1/M2 polarization scheme (p.3, Fig. 1F, S2B, S7, 3C) "PD-L1+/hi vs. PD-L1−/lo TAMs do not fit within this simple canonical M1 vs. M2 dichotomy" — confidence: high — type: methodological — links: [[concepts/m1-m2-polarization-paradigm]] [[concepts/pd-l1-immunostimulatory-tam-phenotype]] [[claims/pd-l1-tam-dichotomy-orthogonal-to-m1-m2]]
- `[c05]` High PD-L1+/hi TAM gene signature correlates with better relapse-free survival in METABRIC (p=0.001, n=1098) and TCGA (p=0.014, n=789) luminal breast cancer; PD-L1+/PD-L1− ratio is the strongest signal (p.4, Fig. 3A-B, S8A) "patients with high gene signature of PD-L1+/hi TAMs (top 25%) had better relapse-free survival (RFS) (log rank test, p = 0.001)... the gene signature ratio of PD-L1+/PD-L1− TAMs showed favorable prognostic significance in METABRIC (p < 0.0001) and in TCGA (p = 0.032)" — confidence: high — type: quantitative — links: [[foundations/tcga-the-cancer-genome-atlas]] [[concepts/pd-l1-immunostimulatory-tam-phenotype]] [[claims/pd-l1-pos-tam-signature-correlates-better-rfs-breast-cancer]]
- `[c06]` PD-L1+ TAMs spatially co-localize with CD8+/CD4+ T cells within 20 μm while PD-L1− TAMs co-localize with cancer cells; PD-L1− TAMs also self-cluster (p.7-8, Fig. 4A-F, S9A) "the number of CD8+ or CD4+ T cells within 20 mm of PD-L1+ TAMs was significantly higher than to PD-L1− TAMs, while the number of cancer cells within 20 mm of PD-L1+TAMs was significantly lower" — confidence: high — type: methodological — links: [[concepts/pd-l1-immunostimulatory-tam-phenotype]] [[foundations/multiplex-immunofluorescence]] [[foundations/cellphonedb-ligand-receptor]] [[foundations/cellchat-cell-cell-communication]] [[claims/pd-l1-tam-spatial-colocalization-with-t-cells-mif]]
- `[c07]` PD-L1 is upregulated during monocyte-to-macrophage maturation independent of IFN-γ (p.9, Fig. 5A-F, S9C) "PD-L1 was still significantly upregulated on monocytes after resting (Figures 5E and 5F), indicating that PD-L1 on monocytes/macrophages could be upregulated during maturation/differentiation independent of IFN-γ" — confidence: high — type: mechanistic — links: [[concepts/monocyte-macrophage-maturation-pd-l1-induction]] [[foundations/pd-l1-cd274]] [[claims/pd-l1-upregulated-monocyte-maturation-ifng-independent]]
- `[c08]` ERK1/2 inhibition (SCH772984) suppresses PD-L1 upregulation during monocyte-to-macrophage maturation; STAT1, Akt, PI3K, NF-κB, mTOR inhibitors do not (p.9, Fig. 5I) "ERK inhibitor significantly suppressed the PD-L1 upregulation, which indicates that the observed PD-L1 upregulation during monocyte-to-macrophage differentiation is partially dependent on ERK signaling pathway" — confidence: medium — type: pharmacological — links: [[concepts/monocyte-macrophage-maturation-pd-l1-induction]] [[claims/erk-inhibition-blocks-pd-l1-monocyte-maturation]]
- `[c09]` PD-L1+ monocytes/macrophages have higher IFN-γR1 surface levels and respond more strongly to IFN-γ (higher ΔpSTAT1+%) than PD-L1− cells — opposite to cancer cells (p.10, Fig. 6A-M, S11A-D) "the percentage of PD-L1+ monocytes responded to IFN-γ stimulation (determined by ΔpSTAT1+% after IFN-γ stimulation) was significantly higher than PD-L1− monocytes... levels of IFN-γ receptor (IFN-γR1) were significantly higher on PD-L1+ than on PD-L1− monocytes" — confidence: high — type: quantitative — links: [[concepts/monocyte-macrophage-maturation-pd-l1-induction]] [[claims/pd-l1-pos-monocytes-higher-ifngr1-primed-pstat1]]
- `[c10]` PD-L1+/hi macrophages stimulate CD8+ T cell proliferation more than PD-L1−/lo macrophages in autologous co-culture; phagocytosis capacity also higher (p.11, Fig. 7A-D, S11G-I) "PD-L1+/hi macrophages had significantly higher stimulatory effects on CD8+ T cell proliferation than PD-L1−/lo macrophages" — confidence: high — type: methodological — links: [[concepts/pd-l1-immunostimulatory-tam-phenotype]] [[claims/pd-l1-pos-macs-stimulate-cd8-proliferation-cytotoxicity]]
- `[c11]` PD-L1−/lo macrophages — not PD-L1+/hi — suppress antigen-specific CD8+ T cell killing in a BiTE-mediated cytotoxicity assay (p.11, Fig. 7E-H) "PD-L1−/lo macrophages but not PD-L1+/hi macrophages significantly suppressed CD8+ T cell killing" — confidence: high — type: methodological — links: [[concepts/pd-l1-immunostimulatory-tam-phenotype]] [[concepts/tumor-associated-macrophage-immunosuppression]] [[claims/pd-l1-neg-macs-suppress-cd8-bite-killing]]
- `[c12]` PD-L1+ macrophage immunostimulatory function is PD-L1:PD-1-independent — anti-PD-L1 blockade does not abolish CD8+ T cell stimulation or BiTE-mediated killing (p.11, Fig. 7D, 7G-H, S11I) "PD-L1 blocking antibody did not suppress the stimulatory of PD-L1+ monocyte/macrophages on T cell proliferation (Figure 7D) despite PD1 expression on T cells... the stimulatory effects of PD-L1+/hi macrophages on T cell proliferation may not be mediated via PD-L1:PD1 interaction" — confidence: medium — type: pharmacological — links: [[foundations/pd-l1-cd274]] [[claims/pd-l1-tam-stimulatory-function-pdl1-pd1-independent]]
- `[c13]` Density ratio of PD-L1+/PD-L1− TAMs is an independent prognostic factor for RFS in luminal breast cancer (multivariate p=0.0099, n=142) (p.5, Fig. 3D-I) "the density ratio of PD-L1+/− TAMs retained highly prognostic significance for RFS (p = 0.0099)" — confidence: high — type: quantitative — links: [[concepts/pd-l1-immunostimulatory-tam-phenotype]] [[foundations/multiplex-immunofluorescence]] [[claims/pd-l1-pos-tam-density-ratio-multivariate-prognostic]]

## Discussion captured

### Authors' interpretation

The authors interpret the data as a paradigm reversal. PD-L1 on TAMs has been historically misclassified as immunosuppressive — an over-extrapolation from cancer cell PD-L1 biology and from murine PD-L1-KO-in-myeloid models that may reflect species-specific or model-specific effects. In human breast cancer, PD-L1 marks the mature/activated end of the TAM continuum: PD-L1+ TAMs upregulate MHC class II antigen presentation, pro-inflammatory cytokines/chemokines, and AP-1 / CEBPD transcriptional activators; functionally they engage T cells (CD8+ proliferation, no suppression of BiTE killing) and reside spatially near T cells in the TIME. PD-L1− TAMs, conversely, are the suppressive/pro-tumor subset, engaging cancer cells and producing SPP1/VEGFA/ECM components. The PD-L1+/PD-L1− density ratio is an independent prognostic factor, supporting clinical utility. The authors propose that PD-L1 expression may protect mature antigen-presenting TAMs from PD-1+ T cell killing (analogous to PD-L1 protection of DCs reported in ref 38, 43) rather than serving as a checkpoint of T-cell suppression. The PD-L1:CD80 cis-heterodimer mechanism (ref 41, 42) is invoked to explain how PD-L1+ TAMs may preserve CD28 co-stimulation while blocking CTLA-4 inhibition.

### Comparisons with prior literature (made by authors)

- **Murine TAM PD-L1 KO models (refs 5–7, Lau 2017; Tang 2018; Lin 2018)**: PD-L1 KO in myeloid lineage abolishes tumor growth — apparently contradictory. Authors argue this reflects PD-L1's protective role on PD-L1+ TAMs rather than its suppressive function.
- **Wang J 2019 Nat Med (SIGLEC15, ref 24)**: provides the mutual-exclusivity foundation for the dichotomization strategy.
- **Pal 2021 (TNBC scRNA-seq, ref 27) and Bassez 2021 (anti-PD1, ref 28)**: independent validation datasets.
- **Ahmed 2020 (TNBC durvalumab, ref 13) and Gross 2022 (lung, ref 8)**: clinical observations that PD-L1+ TAMs predict better outcome — now mechanistically rationalized.
- **Muenst 2014 (intratumoral PD-L1 BC, ref 29)**: total PD-L1 = poor prognosis (likely tumor-cell-dominant) is reconciled by separating tumor-cell vs TAM PD-L1.
- **Wang J 2021 Sci Rep (TNBC mIF, ref 10)**: PD-L1+ TAMs as predictor of improved survival in TNBC — directly extended here with multi-omics and functional analyses.
- **Cheng 2021 pan-cancer myeloid atlas (ref 19)**: TAM heterogeneity broader than M1/M2 — Wang 2024 adds the PD-L1 axis.
- **Mantovani 2022 (TAM targeting review, ref 2)**: framework for TAM-directed therapy that Wang 2024 informs by clarifying the PD-L1+/PD-L1− functional axis.

### Mechanistic hypotheses proposed

- PD-L1 on TAMs is upregulated as a maturation marker (ERK-MAPK-driven) rather than as an inducible inflammatory response gene.
- PD-L1's functional purpose on TAMs may be to *protect* the antigen-presenting cell from PD-1+ T cell killing (akin to PD-L1 on DCs).
- PD-L1+ TAMs may exert their immunostimulatory effect via PD-L1:CD80 cis-heterodimerization, blocking CTLA-4 but preserving CD28 co-stimulation.
- Anti-PD-L1 immunotherapy may not directly block the immunostimulatory function of PD-L1+ TAMs — predicting that ICI response correlates with PD-L1+ TAM enrichment as a biomarker of immune-active TIME rather than as a direct mechanistic target.

### Caveats and self-criticism

- Ex vivo functional assays cannot fully recapitulate the TIME's complexity.
- Longitudinal pre/post-ICI tumor samples are not analyzed — the in vivo dynamics under PD-L1 blockade are unresolved.
- Generalization beyond breast cancer is not tested in this study.
- Primary vs metastatic comparison is not performed.

### Future directions suggested

- Longitudinal sampling pre/post-ICI to map PD-L1+ TAM dynamics in immunotherapy.
- Extension to lung, HCC, urothelial, and other tumor types with reported PD-L1+ TAM-prognosis associations.
- Primary vs metastatic site characterization.

## Limitations

- Ex vivo assays do not fully recapitulate the TIME.
- ICI-treated cohort longitudinal sampling absent — Bassez 2021 reanalysis provides post-treatment snapshots but no within-patient longitudinal data.
- Generalization to non-breast tumors not demonstrated in this paper.
- Primary vs metastatic comparison absent.
- ERK inhibition only partially blocks PD-L1 upregulation — full pathway not delineated.
- Pharmacological inhibitor screen lacks genetic-knockout validation.
- Cluster-level dichotomization assigns ambiguous mid-PD-L1/SIGLEC15 cells based on dominant cluster identity, possibly mis-classifying intermediate states.
- PD-L1:CD80 cis-heterodimerization is invoked as mechanism but not directly tested in this paper.

## Open questions

### Open questions raised by authors

- What is the impact of anti-PD-1/PD-L1 immunotherapy on PD-L1+ TAM function and abundance in vivo?
- Are PD-L1+/− TAMs functionally equivalent in non-breast tumors (lung, HCC, urothelial)?
- Do PD-L1+/− TAM functional differences hold in primary vs metastatic disease?
- Is the PD-L1+/PD-L1− density ratio a viable clinical biomarker for ICI patient selection?

### Open questions identified during ingest

- What is the dominant PD-L1+ TAM → CD8+ T cell co-stimulatory signal (CD80:CD28? AREG-ICAM1? MIF? ANXA1?)?
- Does ERK inhibition affect TAM function in vivo, and does it perturb the prognostic axis?
- How does the PD-L1 axis interact with the hypoxia-driven PD-L1+ M2 TAM phenotype reported in HGSOC (Bai 2022, Noman 2014) — are these distinct PD-L1+ TAM states in different niches?
- Is the SIGLEC15+ subset itself a therapeutic target (anti-SIGLEC15 NC318)?
- Does the PD-L1+ TAM signature change after anti-PD-L1 blockade — i.e., is PD-L1 a stable maturation marker or does its expression depend on the ICI-modulated environment?
- Can PD-L1+ TAM enrichment be therapeutically induced (e.g., M-CSF + ERK pathway tuning) to convert immunosuppressive into immunostimulatory TIME?

## My take

This paper is the foundational human-tumor reference for reconceptualizing PD-L1 on TAMs as a *maturation marker* rather than an immune checkpoint. Several aspects are directly relevant to the HypoxiaVERSE thesis:

1. **Paradigm reversal in a domain (TAM PD-L1) parallel to ours (hypoxic TAM immunogenicity)**: the same intellectual move — distinguishing co-occurring markers from causal mechanisms — applies here as to the NF-κB/TET2 hypoxic-MAC story. The authors' finding that PD-L1 blockade does not abolish PD-L1+ TAM stimulatory function (PD-L1:PD-1-independent) directly parallels our argument that hypoxia is not monolithically immunosuppressive.
2. **Methodological complementarity**: the SIGLEC15-PD-L1 mutual exclusivity dichotomization is a clean trick for circumventing low-abundance transcript dropout that could be applied elsewhere in the wiki (e.g., when analyzing PD-L1 expression on mMAC1 or IL4I1+ TAMs in our datasets).
3. **Cross-axis integration with [[concepts/hypoxia-pd-l1-tam-immune-evasion]]**: the Wang 2024 PD-L1+ TAM phenotype (mature, immunostimulatory, peripheral monocyte-derived) sits at the *opposite* pole from the hypoxia-driven PD-L1 M2 TAM phenotype (Bai 2022). Two different PD-L1+ TAM populations co-exist in the TME — one mature/activated (Wang), one hypoxia/lactate-driven on suppressive M2-like cells (Bai/Noman). This dichotomy deserves explicit treatment in the wiki and likely in the thesis introduction.
4. **Clinical translation**: the PD-L1+/PD-L1− density ratio as multivariate-adjusted prognostic biomarker is an immediately actionable clinical biomarker. The mIF panel is simple (PD-L1, CD68, DAPI) and could be added to existing TIL/PD-L1 IHC workflows.
5. **ERK-MAPK as PD-L1 driver in monocytes**: a candidate mechanism to integrate with our ERK/AP-1 findings on hypoxic macrophage activation (FOS, JUNB, CEBPD upregulated in PD-L1+ TAMs match AP-1 family activated in mMAC1 / hypoxic LPS-activated MACs).

Caveats: the ex vivo system is built from peripheral blood monocytes, leaving the in-tumor maturation context as an inferred extrapolation. The PD-L1:CD80 cis-heterodimer mechanism is invoked but not tested. The mIF cohort sizes (n=49, n=93) are clinically meaningful but not large.

## Related

- [[concepts/pd-l1-immunostimulatory-tam-phenotype]] — core concept introduced by this paper
- [[concepts/siglec15-pd-l1-mutually-exclusive-tam-dichotomization]] — methodological concept introduced by this paper
- [[concepts/monocyte-macrophage-maturation-pd-l1-induction]] — mechanism introduced by this paper
- [[concepts/tumor-associated-macrophage-immunosuppression]] — paradigm this paper challenges
- [[concepts/hypoxia-pd-l1-tam-immune-evasion]] — complementary axis: hypoxia-driven PD-L1 on M2 TAMs (Bai 2022); Wang 2024 establishes a distinct, maturation-driven PD-L1+ TAM phenotype
- [[concepts/m1-m2-polarization-paradigm]] — orthogonal to the PD-L1 axis
- [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]] — Wang 2024 system is monocyte-derived
- [[concepts/mmac1-hypoxic-inflammatory-macrophage]] — independent paradigm reversal for hypoxic MAC immunogenicity; parallel intellectual move
- [[concepts/il4i1-tumor-associated-macrophage]] — likely in vivo correlate of the PD-L1+ mature TAM
- [[concepts/trem2-tumor-associated-macrophage]] — partial overlap with PD-L1−/lo SPP1+ TAM signature
- [[foundations/pd-l1-cd274]] — central marker
- [[foundations/siglec15-checkpoint-ligand]] — dichotomization tool
- [[foundations/multiplex-immunofluorescence]] — spatial method
- [[foundations/cellphonedb-ligand-receptor]] — interaction analysis
- [[foundations/cellchat-cell-cell-communication]] — interaction analysis
- [[foundations/cibersortx-deconvolution]] — bulk tumor deconvolution
- [[foundations/scrna-seq-10x-chromium]] — sequencing platform
- [[foundations/seurat-v3-integration]] — analysis pipeline
- [[foundations/tcga-the-cancer-genome-atlas]] — survival cohort
- [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] — parallel paradigm-reversal in hypoxic MAC immunogenicity (Calafell 2024)
- [[papers/tissue-resident-macrophages-provide-pro-tumorigenic]] — counterpoint: tissue-resident MACs (not MoDMs) drive immunosuppression in NSCLC
