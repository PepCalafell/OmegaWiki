---
title: "Spatiotemporal analyses of the pan-cancer single-cell landscape reveal widespread profibrotic ecotypes associated with tumor immunity"
slug: spatiotemporal-analyses-pan-cancer-single-cell
arxiv: ""
doi: "10.1038/s43018-025-01039-5"
pmid: ""
venue: "Nature Cancer"
year: 2025
authors:
  - Ya Han
  - Lele Zhang
  - Dongqing Sun
  - Guangxu Cao
  - Yuting Wang
  - Jiali Yue
  - Junjie Hu
  - Zhonghua Dong
  - Fang Li
  - Taiwen Li
  - Peng Zhang
  - Qiu Wu
  - Chenfei Wang
first_author: "Ya Han"
corresponding_author: "Qiu Wu; Chenfei Wang"

source_type: pdf
s2_id: ""
date_added: 2026-05-26
ingested_date: 2026-05-26
ingest_version: 1
last_reviewed:

importance: 4
tier: TIER_1
tags:
  - pan-cancer
  - tme
  - scrna-seq
  - spatial-transcriptomics
  - caf
  - tam
  - cthrc1
  - slpi
  - profibrotic-ecotype
  - tumor-ecosystem
  - metacell
  - tabulatime
  - ecm-remodeling
  - immune-exclusion
  - nichenet
keywords:
  - TabulaTIME
  - MetaCell
  - pan-cancer scRNA-seq
  - CTHRC1+ CAF
  - eFibro_CTHRC1
  - SLPI+ macrophage
  - Macro_SLPI
  - profibrotic ecotype
  - tumor ecosystem subtype
  - ECM remodeling
  - leading-edge fibroblast
  - LGALS9-CD44
  - TGFβ1
  - IL-1β
  - NicheNet
  - 36 cancer types
domain: oncology

tissue:
  - pan-cancer
  - lung
  - liver
  - pancreas
  - skin
  - breast
  - colon
  - kidney
  - bladder
  - esophagus
  - head-neck
  - ovary
  - prostate
condition:
  - cancer
disease_specific:
  - nsclc
  - hnsc
  - skcm
  - paad
  - lihc
  - brca
  - crc
  - blca
  - kirc
  - esca
  - prad
species:
  - human
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

techniques:
  - scRNA-seq_10x
  - spatial_visium
  - mIHC
  - immunofluorescence
  - bulk_RNA_seq
  - TCGA_analysis
  - NicheNet
  - NMF_meta_programs
  - CCA_integration
  - CellChat
  - Cell_Ranger
  - MAESTRO
  - inferCNV
  - QUANTISEQ
n_samples: 103
n_cells_total: 4483367
integration_method: "MetaCell + CCA"

key_cell_types:
  - eFibro_CTHRC1
  - eFibro_SFRP1
  - MyFibro_RGS5
  - MyFibro_MYH11
  - iFibro_IL6
  - apFibro_CCL5
  - qFibro_GPX1
  - Macro_SLPI
  - Macro_C1QC
  - Macro_THBS1
  - Macro_SPP1
  - Macro_IL32
  - Macro_CDC20
  - Mono_FCN1
  - Mono_CD16
  - cDC1_CLEC9A
  - cDC2_CD1C
  - pDC_LILRA4
  - CD8Tex_HAVCR2
  - CD8Tex_CXCL13
  - CD8Tem_GZMK
  - CD8Tn_CCR7
  - capEndo_RGCC
  - venEndo_NR2F2
  - lymEndo_PROX1
key_markers:
  - CTHRC1
  - SLPI
  - FAP
  - LRRC15
  - POSTN
  - COL1A1
  - ACTA2
  - SFRP1
  - IL6
  - GPX1
  - C1QC
  - SPP1
  - THBS1
  - LGALS9
  - CD44
  - HAVCR2
  - ITGA6
  - TGFB1
  - IL1B
  - RGCC
  - VEGFA
key_pathways:
  - ECM receptor interaction
  - Focal adhesion
  - EMT
  - Glycosaminoglycan biosynthesis (chondroitin/dermatan sulfate)
  - TGFβ signaling (SMAD)
  - IL-1β / NF-κB
  - LGALS9-CD44 / LGALS9-HAVCR2
  - TNF signaling via NF-κB
  - VEGFA / ANGPT1 angiogenesis

projects:
  - thesis
priority: high
read_status: read

hypoxiaverse_status:
exclusion_reason:
data_availability: "TabulaTIME data portal and pretrained model released by the authors. TCGA, 103 published scRNA-seq studies, and 62 spatial transcriptomics slides used as input."

code_url: ""
cited_by: []
---

## Problem

The tumor microenvironment (TME) is highly heterogeneous across cancer types, evolves during initiation/progression/metastasis, and is shaped by interactions between immune and stromal compartments. Prior pan-cancer atlases focused on individual lineages (myeloid, T cells) or single cancer types, leaving open: (i) which TME cell subtypes are universally enriched across cancers, (ii) how those subtypes are spatially organized, and (iii) which cell-cell ecotypes recur and predict outcome. Existing single-dataset analyses are also limited by batch effects and cell-number constraints that obscure rare stromal subpopulations.

## Key idea

Build **TabulaTIME**, the largest tumor-associated scRNA-seq integration to date — 4,483,367 cells from 103 studies, 36 cancer types, 746 donors — using a **MetaCell aggregation strategy** (≈30 cells/MetaCell) plus **CCA integration**. Then layer pan-cancer spatial transcriptomics (62 slides, 6 cancer types) and TCGA bulk on the resulting blueprint to identify two recurrent profibrotic populations — **CTHRC1+ ECM-remodeling fibroblasts (eFibro_CTHRC1)** and **SLPI+ profibrotic macrophages (Macro_SLPI)** — show they **colocalize at the tumor leading edge** to form a **profibrotic ecotype** that excludes immune cells, and define a five-class pan-cancer **tumor ecosystem subtype** classification (DLP / NIHS / DHP / AIHS / AILS) on 8,743 TCGA patients with prognostic stratification.

## Method

- **TabulaTIME framework** (5 modules): tumor scRNA-seq collection (103 studies, 36 cancer types, 4,483,367 cells, 746 donors); preprocessing via **MAESTRO** (QC, doublet removal, batch correction); **MetaCell** identification (~30 cells/MetaCell, 140,072 MetaCells total) to reduce technical noise; all-lineage integration via **canonical correlation analysis (CCA)** then lineage-specific integration; characterization of 56 cell subtypes across 6 major lineages.
- **Clustering**: optimal resolution selected by ASW + Clustree; subtype purity scored with **ROGUE**.
- **Pathway / program inference**: KEGG/GSVA enrichment; **NMF** on monocytes/macrophages (3,751 robust programs → meta-programs grouped into MP families: TNFA, lysosome, immune-related, cell-cycle/stress, cytokine, metabolism, EMT/ECM).
- **Spatial transcriptomics analysis**: 62 published ST slides across 6 cancer types; signature score / distance correlations to map eFibro_CTHRC1 leading-edge localization; **inferCNV** for malignant spot annotation.
- **Cell-cell communication**: **CellChat** + **NicheNet** for ligand-receptor and upstream-ligand inference.
- **Bulk integration**: TCGA across 23 cancer types (8,743 patients); cell-type signature scoring; survival analysis via Cox model / Kaplan-Meier (Stouffer-aggregated pan-cancer z scores); CD8+ T infiltration via **QUANTISEQ**.
- **Tumor ecosystem clustering**: hierarchical clustering on cell-type signature scores → 5 ecotypes (E1 stromal, E2 naive immune, E3 activated immune, E4 profibrotic, E5 proliferating) → 5 patient subtypes (DLP, NIHS, DHP, AIHS, AILS).
- **Experimental validation**: multiplex IHC and immunofluorescence (CTHRC1, SLPI, CD68, SPP1, PanCK, DAPI) on in-house HNSC, oral cancer, and NSCLC samples.
- **Pretrained transfer-learning model**: TabulaTIME used as reference for automated cell-type annotation on independent BRCA / NSCLC scRNA-seq datasets.

## Results

- **TabulaTIME scale**: 4,483,367 cells / 746 donors / 36 cancer types / 103 studies → 140,072 MetaCells → 6 major lineages × 56 subtypes; MetaCell+CCA outperforms single-cell-level batch correction.
- **Lymphocytes**: 10 cytotoxic subtypes; CD8Tem_GZMK uniquely enriched in precancerous samples (stronger T-mediated antitumor response signature); CD8Tn_CCR7 enriched in blood/normal.
- **Myeloid**: 12 subtypes; classical M1/M2 does not segregate TAM phenotypes. Identified **Macro_SLPI** (profibrotic TAM): low phagocytic/inflammatory scores, highest EMT + focal-adhesion MP scores; distinct monocyte-derived developmental branch from Macro_C1QC / Macro_THBS1 (pseudotime). High Macro_SLPI signature predicts worse survival in ESCA (P=0.014) and SKCM (P=0.0001).
- **Fibroblasts**: 7 subtypes in 5 groups (eFibro, myFibro, iFibro, apFibro, qFibro). **eFibro_CTHRC1** is tumor-enriched (vs eFibro_SFRP1 normal-enriched; iFibro_IL6 precancerous-enriched), co-expresses canonical CAF markers FAP / LRRC15 / POSTN, top-enriched for EMT, ECM receptor interaction, glycosaminoglycan biosynthesis (chondroitin/dermatan sulfate). High eFibro_CTHRC1 signature → worse outcomes in KIRC (P=0.00523) and BLCA (P=0.00568).
- **Spatial leading edge**: eFibro_CTHRC1 signature negatively correlates with distance to tumor cells in 32/41 (78%) ST slides; mIHC in oral cancer confirms localization at malignant–normal boundary; **ITGA6** in malignant cells correlates with CTHRC1+ fibroblast induction (mechanosensitive TGFβ activator hypothesis).
- **Immune exclusion**: immune-cell scores are higher on the normal side than the tumor side of CTHRC1+ boundaries; TCGA CD8+ T infiltration negatively correlates with eFibro_CTHRC1 signature in nearly all cancer types; eFibro_CTHRC1 preferentially interacts with CD8+ T via **LGALS9–CD44 / LGALS9–CD45** (and LGALS9-HAVCR2).
- **Profibrotic ecotype**: in ST data, eFibro_CTHRC1 and Macro_SLPI signature scores correlate at R>0.5 spot-level (across BRCA, CRC, OV, PAAD, PLC, SCC); mIHC confirms colocalization (CTHRC1+CD68+SLPI+) in HNSC/oral and NSCLC samples. NicheNet identifies **TGFβ1** and **IL-1β** as shared upstream inducers of both Macro_SLPI and eFibro_CTHRC1, implicating SMAD/NF-κB activation.
- **Endothelial heterogeneity**: 7 subtypes; angiogenic **capEndo_RGCC** is tumor-enriched, top NicheNet-inferred ligands include VEGFA, ANGPT1, FGF2, TGFB1, TGFA, TNF.
- **Pan-cancer ecotypes (TCGA, n=8,743)**: 5 ecotypes (E1 stromal / E2 naive immune / E3 activated immune / E4 profibrotic / E5 proliferating) → 5 patient subtypes:
  - **DLP** (desert-low-purity): low immune & stromal
  - **NIHS** (naive immune + high stromal)
  - **DHP** (desert-high-purity)
  - **AILS** (activated immune + low stromal)
  - **AIHS** (activated immune + high stromal) — best outcome
  - The **profibrotic-dominated DHP / NIHS group** has the worst survival in SKCM (P=2.54×10⁻⁵) and BRCA (P=0.0229).
- **TabulaTIME pretrained transfer model**: achieves 0.762 accuracy on BRCA_GSE176078 and 0.723 on NSCLC_GSE146100 query datasets, outperforming single-cancer references (NSCLC_GSE131907 0.644; BRCA_EMTAB8107 0.493).

## All claims (exhaustive)

- `[c1]` TabulaTIME integrates the largest pan-cancer tumor scRNA-seq dataset to date — 4,483,367 cells from 103 studies, 36 cancer types, 746 donors (p.1, Fig. 1b) "we collected 4,483,367 cells across 36 cancer types and constructed a pan-cancer resource named TabulaTIME" — confidence: high — type: quantitative — links: [[foundations/tabulatime-pan-cancer-resource]] [[foundations/metacell-aggregation]] [[claims/tabulatime-largest-pan-cancer-scrna-resource]]
- `[c2]` MetaCell aggregation (~30 cells/MetaCell) followed by CCA integration reduces batch effects more effectively than single-cell-level integration while preserving cell-type-specific biological variation (Extended Data Fig. 2e,f) "the integration using MetaCells demonstrates superior performance, significantly reducing batch effects while preserving cell-type-specific biological variation" — confidence: high — type: methodological — links: [[foundations/metacell-aggregation]] [[claims/metacell-cca-integration-outperforms-single-cell-batch-correction]]
- `[c3]` TabulaTIME resolves 56 cell subtypes across 6 major TME cell lineages (cytotoxic lymphocytes, conventional/regulatory lymphocytes, B lymphocytes, myeloid cells, fibroblasts, endothelial cells) — pan-cancer reference taxonomy (Fig. 1c,d) "We have defined 6 major cell lineages and 56 cell subtypes within the TME using an integrated approach" — confidence: high — type: methodological — links: [[foundations/tabulatime-pan-cancer-resource]] [[claims/tabulatime-defines-56-tme-subtypes-six-lineages]]
- `[c4]` CD8Tem_GZMK effector memory CD8+ T cells are significantly enriched in precancerous samples relative to normal/tumor/metastatic samples and more prevalent than cytotoxic NK cells (Fig. 2c) "GZMK+ effector memory CD8+ T cells (CD8Tem_GZMK) were significantly enriched in precancerous tumor samples and were more prevalent than cytotoxic NK cells" — confidence: high — type: correlational — links: [[claims/cd8tem-gzmk-enriched-precancerous]]
- `[c5]` Traditional M1/M2 signatures cannot clearly distinguish macrophage subtypes within the TME (Fig. 2e) "traditional M1/M2 signatures cannot clearly distinguish the macrophage subtypes within the TME, indicating a high level of plasticity and heterogeneity among macrophages" — confidence: high — type: methodological — links: [[claims/m1-m2-signatures-fail-distinguish-tme-macrophages]]
- `[c6]` Macro_SLPI is a profibrotic TAM subtype with diminished phagocytic/inflammatory capacity and the highest EMT + focal-adhesion meta-program scores (Fig. 2e,i) "the Macro_SLPI signature evinces a diminished phagocytic and inflammatory capacity, yet exhibits a markedly elevated ECM remodeling capability" — confidence: high — type: mechanistic — links: [[concepts/slpi-macrophage-profibrotic-tam]] [[foundations/nmf-non-negative-matrix-factorization]] [[claims/macro-slpi-profibrotic-tam-high-emt-focal-adhesion]]
- `[c7]` Macro_SLPI follows a developmental branch distinct from phagocytic Macro_C1QC and anti-inflammatory Macro_THBS1 although they share a monocyte origin (Fig. 2j) "although they both originate from monocytes, the profibrotic Macro_SLPI signature follows a distinct developmental branch compared to the phagocytic Macro_C1QC or the anti-inflammatory Macro_THBS1 signature" — confidence: medium — type: mechanistic — links: [[concepts/slpi-macrophage-profibrotic-tam]] [[claims/macro-slpi-distinct-developmental-branch-from-c1qc-thbs1]]
- `[c8]` High Macro_SLPI signature predicts worse overall survival in TCGA ESCA (P=0.014, n=184) and SKCM (P=0.0001, n=459) (Fig. 2k) "Higher Macro_SLPI signature scores were strongly associated with an increased risk of death in various cancer types, such as esophageal carcinoma (log-rank test, P = 0.014) and skin cutaneous melanoma (log-rank test, P = 0.0001)" — confidence: high — type: quantitative — links: [[concepts/slpi-macrophage-profibrotic-tam]] [[claims/macro-slpi-high-signature-worse-survival-esca-skcm]]
- `[c9]` eFibro_CTHRC1 cells are predominantly tumor-derived and co-express canonical CAF markers FAP, LRRC15, POSTN across nearly all cancer types but not healthy samples (Fig. 3b,d,e) "eFibro_CTHRC1 cells also expressed canonical CAF markers, including FAP, LRRC15 and POSTN, which are prevalent in nearly all cancer types but not in healthy samples" — confidence: high — type: correlational — links: [[concepts/cthrc1-efibro-ecm-remodeling-pan-cancer-caf]] [[foundations/cancer-associated-fibroblast]] [[claims/efibro-cthrc1-pan-cancer-tumor-enriched-fap-lrrc15-postn]]
- `[c10]` eFibro_CTHRC1 cells are top-enriched for EMT, ECM receptor interaction, and glycosaminoglycan biosynthesis (chondroitin/dermatan sulfate) pathways (Fig. 3f,g) "eFibro_CTHRC1 cells were enriched for EMT and ECM receptor interaction pathways... the glycosaminoglycan biosynthesis–chondroitin sulfate/dermatan sulfate pathway... was notably upregulated in eFibro_CTHRC1 cells" — confidence: high — type: mechanistic — links: [[concepts/cthrc1-efibro-ecm-remodeling-pan-cancer-caf]] [[claims/efibro-cthrc1-emt-ecm-glycosaminoglycan-enriched]]
- `[c11]` High eFibro_CTHRC1 signature predicts worse overall survival in TCGA KIRC (P=0.00523, n=533) and BLCA (P=0.00568, n=405) (Fig. 3h) "Higher expression of eFibro_CTHRC1 signature genes was correlated with worse clinical outcomes in multiple cancer types, including kidney renal clear cell carcinoma (log-rank test, P = 0.00523) and bladder urothelial carcinoma (log-rank test, P = 0.00568)" — confidence: high — type: quantitative — links: [[concepts/cthrc1-efibro-ecm-remodeling-pan-cancer-caf]] [[claims/efibro-cthrc1-high-signature-worse-survival-kirc-blca]]
- `[c12]` eFibro_CTHRC1 cells are spatially localized at the leading edge between malignant and normal regions — negative correlation between CTHRC1 signature score and distance-to-tumor in 32/41 (78%) of ST slides (Fig. 4a–d) "the eFibro_CTHRC1 fractions showed a negative correlation with the distance to tumors in the majority of ST slides (total ST slides, 32/41, 78%)" — confidence: high — type: correlational — links: [[concepts/cthrc1-efibro-ecm-remodeling-pan-cancer-caf]] [[foundations/10x-visium-spatial-transcriptomics]] [[claims/efibro-cthrc1-leading-edge-localization-78pct-st-slides]]
- `[c13]` ITGA6 expression in malignant cells positively correlates with the eFibro_CTHRC1 signature — proposed as a matrix-stiffness mechanosensor inducing CTHRC1+ CAF activation and TGFβ release (Fig. 4e) "Our analysis identified several integrins, such as ITGA6, which encodes a matrix stiffness-regulated mechanosensitive molecule that can induce invasive fibroblast phenotypes and mediate activation of transforming growth factor-β (TGFβ) in lung fibrosis" — confidence: medium — type: mechanistic — links: [[concepts/cthrc1-efibro-ecm-remodeling-pan-cancer-caf]] [[foundations/tgfb1-cytokine]] [[claims/itga6-malignant-cells-induces-cthrc1-caf-via-tgfb]]
- `[c14]` eFibro_CTHRC1 forms a physical and signaling barrier that reduces immune-cell infiltration — TCGA CD8+ T infiltration anti-correlates with eFibro_CTHRC1 signature in nearly all cancer types; preferential LGALS9–CD44 and LGALS9–CD45 interactions with CD8+ T cells (Fig. 4f,g,h) "the estimated infiltration of CD8+ T cells was notably higher in tumor samples with a lower eFibro_CTHRC1 signature score in the TCGA cohort in almost all cancer types... eFibro_CTHRC1 fibroblasts were more likely to interact with CD8+ T cells via LGALS9–CD44 and LGALS9–CD45 interactions" — confidence: high — type: mechanistic — links: [[concepts/cthrc1-efibro-ecm-remodeling-pan-cancer-caf]] [[foundations/lgals9-galectin-9]] [[claims/efibro-cthrc1-immune-exclusion-lgals9-cd44-cd8]]
- `[c15]` eFibro_CTHRC1 and Macro_SLPI colocalize in tumor regions, forming a profibrotic ecotype — spot-level signature correlation R>0.5 across ST slides; mIHC validation (CTHRC1+CD68+SLPI+) in HNSC/oral and NSCLC samples (Fig. 5a–d) "eFibro_CTHRC1 and Macro_SLPI cells showed a high correlation at the spot level (R > 0.5)... mIHC staining of CTHRC1, SLPI, CD68 and SPP1 in oral cancer and NSCLC samples further verified the colocalization of eFibro_CTHRC1 and Macro_SLPI cells" — confidence: high — type: correlational — links: [[concepts/cthrc1-slpi-profibrotic-spatial-ecotype]] [[claims/cthrc1-slpi-colocalize-profibrotic-ecotype]]
- `[c16]` NicheNet identifies TGFβ1 and IL-1β as shared upstream ligands that activate both eFibro_CTHRC1 and Macro_SLPI phenotypes (Fig. 5e) "we conducted NicheNet analyses, which indicated a tight connection between the activity of TGFβ1 and interleukin-1β (IL-1β) ligands and the eFibro_CTHRC1 phenotype... TGFβ1 and IL-1β could also stimulate the Macro_SLPI phenotype" — confidence: high — type: mechanistic — links: [[concepts/cthrc1-slpi-profibrotic-spatial-ecotype]] [[foundations/tgfb1-cytokine]] [[foundations/il-1-beta-cytokine]] [[foundations/nichenet-ligand-target-inference]] [[claims/tgfb1-il1b-shared-upstream-cthrc1-slpi-ecotype]]
- `[c17]` capEndo_RGCC angiogenic capillary endothelial subtype is tumor-enriched; NicheNet-inferred top regulators include VEGFA, ANGPT1, FGF2, TGFB1, TGFA, TNF (Fig. 6a–g) "Genes encoding the top 20 ligands inferred to regulate RGCC+ endothelial cells according to NicheNet" — confidence: medium — type: mechanistic — links: [[foundations/nichenet-ligand-target-inference]] [[claims/capendo-rgcc-tumor-enriched-vegfa-angpt1-regulated]]
- `[c18]` Pan-cancer ecotype clustering on TCGA (n=8,743, 23 cancer types) yields five tumor ecosystem subtypes (DLP, NIHS, DHP, AILS, AIHS) with distinct CD8+ T infiltration and tumor purity profiles (Fig. 7d–h) "8,743 individuals from TCGA classified into four distinct TME subtypes based on clustering of the signature of all cell types" — confidence: high — type: methodological — links: [[concepts/pan-cancer-tumor-ecosystem-five-subtypes]] [[claims/pan-cancer-five-tumor-ecosystem-subtypes-tcga]]
- `[c19]` Tumor ecosystem subtype stratification predicts overall survival — significant separation across SKCM (P=2.54×10⁻⁵, n=459) and BRCA (P=0.0229, n=1,091) (Fig. 7i) "Statistical significance was assessed via the log-rank test, with P values of 2.54 × 10−5 for SKCM and 0.0229 for BRCA" — confidence: high — type: quantitative — links: [[concepts/pan-cancer-tumor-ecosystem-five-subtypes]] [[claims/tumor-ecosystem-subtype-prognostic-skcm-brca]]
- `[c20]` TabulaTIME pretrained transfer-learning model outperforms single-cancer scRNA-seq references for automated cell-type annotation (BRCA_GSE176078 0.762 vs 0.493; NSCLC_GSE146100 0.723 vs 0.462) (Fig. 8) "Accuracy 0.762 (TabulaTiME) > 0.644 (NSCLC) > 0.493 (BRCA EMTAB8107)" — confidence: medium — type: methodological — links: [[foundations/tabulatime-pan-cancer-resource]] [[claims/tabulatime-transfer-learning-outperforms-single-cancer-reference]]

## Discussion captured

### Authors' interpretation

Authors frame the **CTHRC1+ CAF / SLPI+ TAM profibrotic ecotype** as a **conserved, pan-cancer organizing principle** of the TME — a stromal "wall" at the malignant–normal interface that physically and immunologically excludes effector T cells. They argue the ecotype is **functionally analogous to wound-healing / fibrotic-niche programs** repurposed by tumors (explicitly invoking lung fibrosis and post-COVID-19 fibrotic macrophages as molecular analogs). The clinical thesis: **targeting the profibrotic ecotype** — by blocking shared upstream activators (TGFβ1, IL-1β) or downstream interactions (LGALS9–CD44) — could simultaneously dismantle CAF-mediated immune exclusion and TAM immunosuppression.

### Comparisons with prior literature (made by authors)

- CTHRC1+ CAFs build on prior FAP+ and LRRC15+ CAF reports (refs 12, 36); this study generalizes them as the pan-cancer canonical ECM-remodeling CAF and adds spatial localization.
- Pan-cancer myeloid atlas precedents (refs 7–11): TabulaTIME extends them with stromal compartments and ecotype framing.
- Macro_SLPI MP-46/47 (EMT focal adhesion) resembles **wound-healing and profibrotic macrophages in lung fibrosis and COVID-19** (refs 32–34).
- LGALS9 immunosuppression literature on Treg stabilization, T-cell apoptosis via HAVCR2 (refs 42, 43) cited as concordant.
- ITGA6 mechanosensing in lung fibrosis (refs 40, 41) provides candidate mechanism for malignant→CTHRC1+ CAF induction.

### Mechanistic hypotheses proposed

- Profibrotic ecotype is activated by a **convergent TGFβ1 / IL-1β signaling axis** that simultaneously drives SLPI+ TAM and CTHRC1+ CAF phenotypes via SMAD and NF-κB / STAT.
- CTHRC1+ CAFs act as **both physical barrier (ECM deposition) and signaling barrier (LGALS9–CD44/CD45/HAVCR2)** to T-cell infiltration.
- The five tumor ecosystem subtypes capture distinct immune-stromal trajectories that may shape immunotherapy response — AIHS likely most responsive, DHP/NIHS profibrotic-dominated may be most resistant.

### Caveats and self-criticism

- ST data are spot-level (6–10 cells/spot), not true single-cell resolution; colocalization is inferred from signature score correlations rather than direct co-occurrence.
- Cross-study integration cannot fully eliminate technical heterogeneity; some rare subtypes may be missed.
- Pretrained transfer-learning accuracy (~0.76) is far from saturated.
- Five-subtype classification was derived on TCGA bulk; single-cell validation across all cancer types is incomplete.

### Future directions suggested

- Targeting the TGFβ1 / IL-1β / LGALS9 axes as anti-stromal therapy.
- Combining anti-CAF therapies with immune checkpoint blockade specifically in DHP/NIHS-classified patients.
- Extending TabulaTIME to longitudinal pre/post-treatment cohorts and rare cancers.

## Limitations

- ST spot-level resolution prevents true single-cell colocalization claims for CTHRC1+ CAF / SLPI+ TAM ecotypes; mIHC validation is limited to selected cancer types (HNSC, oral, NSCLC).
- Cross-study technical heterogeneity (10x Genomics vs other platforms, fresh vs frozen) may bias subtype abundance estimates.
- Survival associations are correlational; the causal contribution of CTHRC1+ CAF or SLPI+ TAM to mortality is not directly tested by intervention.
- Mechanistic claims for TGFβ1 / IL-1β as shared upstream ligands rely on NicheNet inference rather than perturbation experiments.
- Tumor ecosystem subtypes (DLP/NIHS/DHP/AIHS/AILS) are derived from TCGA bulk decomposition; their validity in individual cancer types varies (n=14 NIHS in SKCM survival analysis).

## Open questions

### Open questions raised by authors

- Can the profibrotic ecotype be selectively targeted to restore immune infiltration without disrupting beneficial wound-healing?
- Which TGFβ-axis components (SMAD2/3 vs NF-κB) are dominant in the CTHRC1+/SLPI+ ecotype across cancer types?
- Will combining anti-LGALS9 or anti-TGFβ with checkpoint blockade rescue DHP/NIHS patients specifically?

### Open questions identified during ingest

- How does the CTHRC1+ CAF / SLPI+ TAM ecotype relate to the **early IL1B-IL1R1 proinflammatory niche** described in lung precursor lesions ([[papers/multimodal-spatial-omics-reveal-co-evolution]])? Is the early IL-1β niche a temporal precursor to the late TGFβ1/IL-1β profibrotic ecotype?
- Is CTHRC1+ CAF leading-edge enrichment a hypoxia-driven phenotype? Direct comparison to [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] and [[papers/tumour-microenvironment-crosstalk-nsclc-progression-response]] would clarify whether ECM-remodeling fibroblasts are downstream of tumor-edge hypoxia.
- Does the Macro_SLPI signature overlap with the COL11A1+/SPP1+ NSCLC axis ([[concepts/col11a1-spp1-fibrotic-axis-cd8-exclusion-nsclc]])? SLPI+ TAM and SPP1+ TAM may be sister profibrotic states.
- How does AhR-active tryptophan metabolism (multiple wiki papers on AhR-TAM) interact with the CTHRC1+/SLPI+ ecotype? Both converge on immunosuppression and could be combinable interception targets.
- Could the TabulaTIME pretrained model be fine-tuned for hypoxia-specific TAM/CAF inference across the user's hypoxia corpus?

## My take

This is **the canonical pan-cancer single-cell + spatial TME reference paper of 2025** — the natural pan-cancer counterpart to the lung-precursor multimodal work ([[papers/multimodal-spatial-omics-reveal-co-evolution]]) and complements the existing wiki's lineage-specific atlases ([[concepts/pan-cancer-tam-atlas-23-clusters]], [[papers/cross-tissue-single-cell-landscape-human]]).

Three things make it load-bearing for the thesis:

1. **CTHRC1+ CAF leading-edge geometry**: provides the spatial-molecular substrate for "stromal immune exclusion" — bridging old FAP+/LRRC15+ CAF literature with the COL11A1+/SPP1+ axis ([[concepts/col11a1-spp1-fibrotic-axis-cd8-exclusion-nsclc]]) and the ECM-Mac collagen-producing TAM concept ([[concepts/ecm-mac-collagen-producing-tam]]). The 78% leading-edge enrichment across cancer types is the most compelling pan-cancer geometry claim I've seen.

2. **Profibrotic ecotype as a coherent therapeutic unit**: the colocalization of CTHRC1+ CAFs and SLPI+ TAMs around a shared TGFβ1/IL-1β axis converts what used to be two separate stromal/myeloid stories into one targetable niche. The hypothesis that targeting either component disrupts both is testable and clinically actionable.

3. **TabulaTIME as transfer-learning backbone**: the 4.5M-cell pretrained reference is immediately useful as a query backbone for any future scRNA-seq ingest in the wiki — particularly for hypoxia-relevant cancer datasets where lineage annotation is currently inconsistent across studies.

Caveats: ST spot resolution limits cellular-level claims; NicheNet inference is hypothesis-generating not mechanistic; pretrained-model accuracy is still modest. The most important follow-up question for this wiki is whether the late TGFβ1/IL-1β profibrotic ecotype is **temporally downstream** of the early IL1B-IL1R1 proinflammatory niche described by Peng et al. ([[papers/multimodal-spatial-omics-reveal-co-evolution]]) — i.e., does early-stage IL-1β/RELA inflammation transition into a late-stage CTHRC1+/SLPI+ ecotype as tumors progress to invasion?

## Related

- [[concepts/cthrc1-efibro-ecm-remodeling-pan-cancer-caf]]
- [[concepts/slpi-macrophage-profibrotic-tam]]
- [[concepts/cthrc1-slpi-profibrotic-spatial-ecotype]]
- [[concepts/pan-cancer-tumor-ecosystem-five-subtypes]]
- [[foundations/tabulatime-pan-cancer-resource]]
- [[foundations/metacell-aggregation]]
- [[foundations/lgals9-galectin-9]]
- [[foundations/cancer-associated-fibroblast]]
- [[foundations/spp1-secreted-phosphoprotein-1]]
- [[foundations/nichenet-ligand-target-inference]]
- [[foundations/tgfb1-cytokine]]
- [[foundations/il-1-beta-cytokine]]
- [[foundations/nmf-non-negative-matrix-factorization]]
- [[foundations/10x-visium-spatial-transcriptomics]]
- [[concepts/col11a1-spp1-fibrotic-axis-cd8-exclusion-nsclc]]
- [[concepts/ecm-mac-collagen-producing-tam]]
- [[concepts/pan-cancer-tam-atlas-23-clusters]]
- [[concepts/pre-cafs-cancer-associated-fibroblasts-premalignant]]
- [[concepts/ecm-mycaf-leading-edge-signaling-axis]]
- [[papers/multimodal-spatial-omics-reveal-co-evolution]]
- [[papers/tumour-microenvironment-crosstalk-nsclc-progression-response]]
- [[papers/cellcharter-reveals-spatial-cell-niches-associated]]
- [[papers/cross-tissue-single-cell-landscape-human]]
- [[papers/curated-cancer-cell-atlas-provides-comprehensive]]
- [[people/ya-han]]
- [[people/qiu-wu]]
- [[people/chenfei-wang]]
