---
# === Identification ===
title: "TREM2 macrophages are associated with enhanced response to PD-1 blockade in human hepatocellular carcinoma"
slug: trem2-macrophages-associated-enhanced-response-pd
arxiv: ""
doi: "10.1101/2025.09.09.675071"
pmid: ""
venue: "bioRxiv"
year: 2025
authors:
  - "Pauline Hamon"
  - "Matthew D. Park"
  - "Jessica Le Berichel"
  - "Merav Cohen"
  - "Brian Y. Soong"
  - "Mark Buckup"
  - "Clotilde Hennequin"
  - "Katherine E. Lindblad"
  - "Raphaël Mattiuz"
  - "Igor Figueiredo"
  - "Alexandra Tabachnikova"
  - "Travis Dawson"
  - "Darwin D'souza"
  - "Leanna Troncoso"
  - "Giorgio Ioannou"
  - "Colles Price"
  - "Nicolas Fernandez"
  - "Amir Giladi"
  - "Oren Barboy"
  - "Zhen Zhao"
  - "Sinem Ozbey"
  - "Sarah Cappuyns"
  - "Amanda Reid"
  - "Steven Hamel"
  - "Joel Kim"
  - "Romain Donne"
  - "Christie Chang"
  - "Robert Marvin"
  - "Hiyab Stefanos"
  - "Grace Chung"
  - "Raphaël Merand"
  - "Laszlo Halasz"
  - "Samarth Hegde"
  - "Lou M. Guerin"
  - "Min Ni"
  - "Yi Wei"
  - "Gurinder Atwal"
  - "Alona Lansky"
  - "Hajra Jamal"
  - "Nancy Yi"
  - "Theodore Chin"
  - "Nicola James"
  - "Nausicaa Malissen"
  - "Fiona Desland"
  - "Yonit Lavin"
  - "Stephen C. Ward"
  - "Maria Isabel Fiel"
  - "Rachel Brody"
  - "Jeroen Dekervel"
  - "Diether Lambrechts"
  - "Ephraim Kenigsberg"
  - "Edgar Gonzalez-Kozlova"
  - "Vladimir Roudko"
  - "Alice O. Kamphorst"
  - "Jiang He"
  - "Marco Colonna"
  - "Seunghee Kim-Schulze"
  - "Sacha Gnjatic"
  - "John C. Lin"
  - "Gavin Thurston"
  - "Amaia Lujambio"
  - "Myron Schwartz"
  - "Ido Amit"
  - "Thomas U. Marron"
  - "Miriam Merad"
first_author: "Pauline Hamon"
corresponding_author: "Pauline Hamon; Thomas U. Marron; Miriam Merad"

# === Source & metadata ===
source_type: pdf
s2_id: "1a875e173b695e4941d2c694a29f1c54f3c239bd"
date_added: 2026-05-26
ingested_date: 2026-05-26
ingest_version: 1
last_reviewed: null

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - TREM2
  - tumor-associated-macrophage
  - hepatocellular-carcinoma
  - PD-1-blockade
  - immune-checkpoint-blockade
  - neoadjuvant
  - cemiplimab
  - FOLR2-macrophage
  - soluble-TREM2
  - biomarker
  - IMbrave150
  - POPLAR
  - MERFISH
  - PIC-seq
  - mregDC
  - tissue-specific-TAM
  - scRNA-seq
  - spatial-transcriptomics
keywords:
  - TREM2 macrophages HCC
  - PD-1 blockade response biomarker
  - soluble TREM2 sTREM2
  - neoadjuvant cemiplimab hepatocellular carcinoma
  - hepatic TREM2 program metallothionein calreticulin
  - tissue-specific TREM2 mac function
  - TREM2-PD1hi-CD8 spatial proximity
  - CXCL13 PD-1hi T-cell mregDC TREM2 quartet
  - IMbrave150 atezolizumab bevacizumab TREM2 score
  - FOLR2 macrophage non-responders HCC
domain: "tumor immunology / hepatocellular carcinoma / single-cell genomics"

# === Biomedical domain ===
tissue:
  - liver
  - blood
condition:
  - cancer
disease_specific:
  - hepatocellular_carcinoma
  - resectable_HCC
  - advanced_HCC
species:
  - human
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques:
  - scRNA-seq_10x
  - MERFISH
  - PIC-seq
  - MICSSS_multiplex_IHC
  - bulk_RNA-seq
  - flow_cytometry
  - ELISA
  - Cellpose_segmentation
  - Seurat
  - Scanpy
  - scvi-tools
  - Cell_Ranger
n_samples: null
n_cells_total: null
integration_method: "batch-aware multinomial mixture (Cohen 2018)"

# === Biology captured ===
key_cell_types:
  - TREM2_macrophage
  - FOLR2_macrophage
  - FCN1_CXCL9_macrophage
  - FCGR2B_macrophage
  - Kupffer_cell
  - SPP1_CCL2_IL4I1_monocyte
  - CD14_classical_monocyte
  - CD16_non_classical_monocyte
  - PD1hi_CD8_effector_T_cell
  - TCF1_PD1hi_CD8_T_cell
  - CXCL13_PD1hi_CD4_helper_T_cell
  - LAG3_PD1hi_CD8_T_cell
  - mregDC
  - Treg
  - NK_cell
  - hepatic_stellate_cell
key_markers:
  - TREM2
  - GPNMB
  - SPP1
  - APOE
  - FABP5
  - CD9
  - CALR
  - MT1G
  - MT1H
  - CCL20
  - S100A10
  - FOLR2
  - SEPP1
  - SLC40A1
  - F13A1
  - STAB1
  - MARCO
  - CD5L
  - TIMD4
  - LYVE1
  - CXCL13
  - PDCD1
  - TCF7
  - LAG3
  - HAVCR2
  - TOX
  - TIGIT
  - KLRK1
  - EOMES
  - HLA-DQA1
  - HLA-DRA
  - CD86
  - IFNGR1
  - CXCR6
  - GZMK
key_pathways:
  - PD-1_PD-L1_immune_checkpoint
  - TREM2_DAP12_signaling
  - efferocytosis_apoptotic_cell_clearance
  - SIRPa_CD47_don_t_eat_me
  - ferroptosis_lipid_peroxidation
  - MHC_class_II_antigen_presentation
  - T_cell_co-stimulation
  - tertiary_lymphoid_structure_formation

# === User project membership ===
projects:
  - thesis
priority: useful
read_status: deep_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: not_included
exclusion_reason: "not hypoxia-focused — included for thesis TAM and ICB-biomarker context"
data_availability: "bioRxiv preprint 2025; raw scRNA-seq and MERFISH expected in GEO/EGA upon peer-reviewed publication; IMbrave150 / POPLAR bulk data via Roche/Genentech under data-access requests"

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

In human hepatocellular carcinoma (HCC), only a minority of patients respond to PD-1 blockade, and cellular determinants of response are poorly defined. Macrophages dominate the HCC tumor microenvironment and have historically been framed as immunosuppressive — yet which macrophage subsets (if any) gate or enable immune checkpoint blockade (ICB) success has not been identified. The TREM2⁺ tumor-associated macrophage state, well documented as pro-tumorigenic in NSCLC, breast, and ovarian cancers, has an unclear function in liver cancer. The paper asks: which mac states associate with pathological response to neoadjuvant PD-1 blockade in HCC, and is there a tissue-specific reversal of the TREM2-mac immunosuppression paradigm?

## Key idea

Across two neoadjuvant cohorts (cemiplimab; cemiplimab+SBRT) and the IMbrave150 phase III trial (atezolizumab+bevacizumab), intratumoral TREM2 macrophages and circulating soluble TREM2 (sTREM2) are *positively* associated with response to PD-1/PD-L1 blockade and with overall survival in HCC — opposite to the TREM2-mac immunosuppression observed in NSCLC. The TREM2 mac core program is conserved across tumor types (48 conserved genes between HCC and NSCLC), but tissue-specific imprints (209 liver-specific genes, 89 lung-specific) — including hepatic metallothioneins (MT1G, MT1H) for oxidative-stress / anti-ferroptotic protection and calreticulin (CALR) for pro-phagocytic anti-CD47 activity — distinguish hepatic TREM2 macs and likely underlie their protective role. Spatially (MERFISH) and by direct physical interaction (PIC-seq), TREM2 macs are uniquely enriched at MNP/T-cell contacts and proximal to the PD-1hi CD8 + CXCL13⁺ CD4 + mregDC immune-niche the authors previously linked to ICB response. Direct TREM2-mac/PD-1hi-CD8 contacts correlate with elevated T-cell activation/cytotoxicity programs (EOMES, GZMA/H/K, KLRK1, CXCR6) and elevated TREM2-mac MHC-II/co-stimulation (HLA-DQ/DR, CD86, IFNGR1), while distal T cells upregulate exhaustion (HAVCR2, TOX, TIGIT). The TREM2 program stratifies IMbrave150 patients by OS but fails to stratify POPLAR NSCLC atezolizumab patients, confirming tissue-dependent function. Baseline serum sTREM2 emerges as an accessible, blood-based predictive biomarker for PD-1 blockade response in HCC.

## Method

Two prospective neoadjuvant cohorts of resectable HCC were enrolled:
- **Discovery cohort (NCT03916627 Cohort B)**: 20 patients treated with two cycles of cemiplimab pre-resection (Marron et al.) plus 9 nivolumab off-label and 8 treatment-naïve controls.
- **Validation cohort (NCT03916627 Cohort B2)**: 21 patients treated with cemiplimab + stereotactic body radiotherapy (SBRT); scRNAseq on 16 patients.

Tumor and adjacent normal liver were dissociated and profiled by 10x Genomics scRNA-seq; reads were aligned with Cell Ranger v2.2.0 against GRCh38. Batch-aware unsupervised clustering used a multinomial mixture model with batch-specific noise (Cohen 2018; Casanova-Acebes 2021). Mo-mac states (FOLR2, TREM2, FCN1/CXCL9, FCGR2B) plus Kupffer cells were annotated by gene-signature consensus.

Cell-cell physical interactions were measured with PIC-seq (physically-interacting cell sequencing; Giladi/Cohen) capturing MNP/T-cell heterotypic doublets. Spatial localization was measured with MERFISH (Vizgen MERSCOPE custom panel) on FFPE and fresh-frozen liver sections; segmentation used Cellpose v1.0.2 in the Vizgen post-processing tool with masks shrunk by 20% to reduce peripheral transcript misassignment; downstream analyses used Scanpy v1.9.1 and scvi-tools v1.0.4. Tumor, immune-aggregate, and stromal regions were defined from B-cell, fibroblast, and HSC marker expression. Proximity-conditional differential expression compared TREM2 macs and PD-1hi CD8 T cells in direct contact vs distal.

Cross-cancer comparison projected the HCC-derived TREM2 program onto published advanced HCC, NSCLC, pancreatic, and triple-negative breast scRNA-seq datasets (EGAS00001007547, GSE155698, GSE154826), identifying 48 conserved, 209 liver-specific, and 89 lung-specific genes via differential expression of TREM2hi vs TREM2lo mo-macs in each tissue.

External validation: bulk RNA-seq from IMbrave150 (atezo+bev, HCC, n=358) and POPLAR (atezo, NSCLC) phase trials was scored with the top-10 TREM2 mac genes; patients stratified into TREM2hi (top quartile) and TREM2lo (bottom quartile), Kaplan-Meier OS analysis. Baseline serum sTREM2 was quantified by ELISA in 17 additional NCT04123379 patients.

Multiplexed IHC (MICSSS / MARQO) on QuPath-annotated tissue sections corroborated TREM2-mac / PD-1hi-CD8 / mregDC co-localization.

## Results

### 1. Mo-mac heterogeneity in the HCC TME (Fig. 1)
Four mo-mac states (FOLR2, TREM2, FCN1/CXCL9, FCGR2B) plus resident Kupffer cells (KC) were defined; KCs were depleted from tumor vs adjacent normal; FOLR2 and TREM2 macs were enriched in tumor. A novel tissue-infiltrating SPP1⁺CCL2⁺FN1⁺IL4I1⁺ monocyte subset, distinct from circulating CD14/CD16 monocytes and pro-inflammatory (NLRP3, IL1B, CCL3/4, CXCL8), was enriched specifically in responders.

### 2. TREM2 macs physically and spatially engage the PD-1hi T-cell / mregDC niche (Fig. 2)
PIC-seq sequencing of MNP/T-cell physically-interacting doublets showed that TREM2 macs are the only mac subset uniquely enriched in PICs versus singlets. MERFISH placed TREM2 macs in close proximity to Tregs and NK cells inside tumor nodules, and — in immune aggregates — adjacent to CXCL13⁺ PD-1hi CD4 helper T cells, TCF1⁺ PD-1hi CD8 T cells, LAG3⁺ PD-1hi CD8 T cells, and mregDCs. FOLR2 macs in aggregates instead clustered with PD-1hi effector CD8 T cells; in stroma, with hepatic stellate cells. Proximity-conditional DE showed that PD-1hi CD8 cells in direct contact with TREM2 macs upregulated KLRK1, CD69, CD27, CXCR6, CXCR4, CD2, EOMES, GZMA/K/H, CXCL16, while distal PD-1hi CD8 upregulated HAVCR2, TOX, TIGIT. TREM2 macs in contact with PD-1hi CD8 upregulated MHC-II (HLA-DQA1/B1, DRA/B1), IFNGR1, and CD86.

### 3. Conserved core vs tissue-specific TREM2 programs (Fig. 3)
The HCC-defined TREM2 program identified TREM2 macs in advanced HCC, NSCLC, PDAC, and TNBC datasets. Cross-comparison of HCC vs NSCLC TREM2 mac DEGs yielded a 48-gene core conserved program plus 209 liver-specific and 89 lung-specific genes. NSCLC TREM2 macs uniquely upregulated CCL20, S100A10, and SPP1 (tissue-remodelling matricellular). Hepatic TREM2 macs uniquely upregulated metallothioneins (MT1G, MT1H — protection against oxidative stress / ferroptosis-linked lipid peroxidation) and CALR (calreticulin — pro-phagocytic, counteracts CD47 don't-eat-me).

### 4. TREM2 program predicts ICB response and OS in HCC but not NSCLC (Fig. 4)
The validation cohort (cemiplimab+SBRT) reproduced TREM2-mac enrichment in responders. Responders (including partial responders) had lower recurrence rates than non-responders across both cohorts. Top-10 TREM2-program genes scored on IMbrave150 (n=358 atezo+bev HCC) stratified patients into TREM2hi (top quartile) with significantly improved OS vs TREM2lo (bottom quartile). The same score failed to stratify POPLAR NSCLC atezolizumab patients — confirming tissue-dependent TREM2 function.

### 5. Soluble TREM2 (sTREM2) as a blood-based predictive biomarker
Baseline serum sTREM2 was significantly elevated in responders vs non-responders in the discovery cohort; the result was reproduced in the validation cohort. sTREM2 is therefore proposed as an accessible, easily measured biomarker for stratifying HCC patients for PD-1 blockade.

## All claims (exhaustive)

- `[c01]` Intratumoral TREM2 macrophages are enriched in HCC patients responding to neoadjuvant PD-1 blockade compared with non-responders (p.4, Fig. 1) "we determined that the intratumoral abundance of TREM2-expressing macrophages... are elevated in patients who responded to PD-1 blockade, compared to non-responders" — confidence: high — type: correlational — links: [[concepts/trem2-tumor-associated-macrophage]] [[concepts/hepatic-trem2-protective-tam-program]] [[claims/trem2-macs-enriched-hcc-pd1-responders]]
- `[c02]` Baseline serum soluble TREM2 (sTREM2) is significantly elevated in HCC patients who respond to PD-1 blockade compared with non-responders, in both discovery and validation cohorts (p.6-7, Fig. 3d-e, Fig. S4a-b) "we discovered that responders exhibited significantly higher sTREM2 levels compared to non-responders... this trend was also seen in our independent validation cohort" — confidence: high — type: correlational — links: [[concepts/soluble-trem2-icb-response-biomarker]] [[foundations/trem2-receptor]] [[claims/strem2-serum-elevated-pd1-responders-hcc]]
- `[c03]` Top-10 TREM2 program genes stratify IMbrave150 phase III HCC patients (n=358, atezolizumab + bevacizumab) into a TREM2hi top-quartile with significantly improved overall survival vs TREM2lo bottom-quartile (p.6, Fig. 4c top) "TREM2hi patients exhibited a significant survival benefit, compared to their TREM2lo counterparts" — confidence: high — type: correlational — links: [[concepts/hepatic-trem2-protective-tam-program]] [[foundations/imbrave150-trial]] [[claims/trem2-program-stratifies-imbrave150-overall-survival]]
- `[c04]` The same TREM2 program score fails to stratify POPLAR phase II NSCLC atezolizumab patients for response or overall survival — demonstrating tissue-dependent TREM2-mac function (p.6, Fig. 4c bottom) "the TREM2 program failed to stratify patients with significant differences in response to PD-L1 blockade and overall survival... reinforcing the principle that the immunological function of TREM2 macs is tissue-dependent" — confidence: high — type: correlational — links: [[concepts/tissue-specific-tam-function-context-dependence]] [[claims/trem2-program-fails-stratify-poplar-nsclc-atezo]]
- `[c05]` Four monocyte-derived macrophage transcriptional states (FOLR2, TREM2, FCN1/CXCL9, FCGR2B) plus resident Kupffer cells were identified in the HCC tumor microenvironment by scRNA-seq (p.4, Fig. 1c, Fig. S1i, Fig. S2a-b) "we identified four major transcriptional states, apart from the cells bearing the resident Kupffer cell (KC) mRNA signature... (1) FOLR2 macs, (2) TREM2 macs, (3) FCN1/CXCL9 macs, and (4) FCGR2B macs" — confidence: high — type: methodological — links: [[concepts/trem2-tumor-associated-macrophage]] [[concepts/folr2-tissue-resident-macrophage]] [[claims/four-momac-states-hcc-tme-folr2-trem2-fcn1-fcgr2b]]
- `[c06]` Resident Kupffer cells (MARCO⁺CD5L⁺TIMD4⁺LYVE1⁺) are significantly depleted from HCC tumor lesions compared with adjacent tumor-free liver, paralleling alveolar macrophage depletion in NSCLC (p.4, Fig. S1j) "KCs were significantly reduced in tumors, compared to adjacent, tumor-free tissue" — confidence: high — type: correlational — links: [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]] [[claims/kupffer-cells-depleted-hcc-tumor-vs-adjacent]]
- `[c07]` FOLR2 and TREM2 macrophages are both enriched in HCC tumor lesions relative to adjacent tumor-free liver (p.4, Fig. S1j) "FOLR2 and TREM2 macs were all enriched in tumor lesions" — confidence: high — type: correlational — links: [[concepts/trem2-tumor-associated-macrophage]] [[concepts/folr2-tissue-resident-macrophage]] [[claims/folr2-trem2-macs-enriched-hcc-tumor-vs-adjacent]]
- `[c08]` Among all mac subsets, only TREM2 macs are uniquely enriched in MNP/T-cell physically-interacting cell (PIC) doublets vs singlets, indicating preferential direct interaction with tumor-infiltrating T cells (p.4-5, Fig. 2a-b) "only TREM2 macs were found to be enriched in PICs compared to singlets" — confidence: high — type: methodological — links: [[foundations/pic-seq-physically-interacting-cells]] [[concepts/trem2-tumor-associated-macrophage]] [[claims/trem2-macs-uniquely-enriched-mnp-tcell-pics]]
- `[c09]` By MERFISH spatial transcriptomics, TREM2 macs in tumor nodules are spatially proximal to Tregs and NK cells (also to monocytes and FOLR2 macs) (p.5, Fig. 2d left) "In tumor nodules, TREM2 macs were most proximal to Tregs and NK cells, as well as monocytes and FOLR2 macs" — confidence: high — type: methodological — links: [[foundations/merfish-imaging-spatial]] [[claims/trem2-macs-spatial-proximity-tregs-nk-tumor-nodules]]
- `[c10]` Within immune aggregates, TREM2 macs are spatially proximal to CXCL13⁺ PD-1hi CD4 helper T cells, TCF1⁺ PD-1hi CD8 T cells, and LAG3⁺ PD-1hi CD8 T cells (p.5, Fig. 2d middle, Fig. S3c) "TREM2 macs were spatially organized near multiple subsets of PD-1hi T cells, including CXCL13+ PD-1hi CD4 T cells, TCF1+ PD-1hi CD8 T cells, and LAG3+ PD-1hi CD8 T cells" — confidence: high — type: methodological — links: [[concepts/trem2-mac-pd1-immune-niche-quartet]] [[concepts/cxcl13-cxcr5-tls-recruitment]] [[claims/trem2-macs-proximal-pd1hi-cd8-tcf1-cxcl13-aggregates]]
- `[c11]` mregDCs (mature DCs enriched in regulatory molecules) are spatially proximal to TREM2 macs in HCC immune aggregates, consistent with the prior TCF1⁺/CXCL13⁺/mregDC ICB-response triad now extended to a TREM2-mac-inclusive quartet (p.5, Fig. 2d) "mature DCs (mregDCs) were also found proximal to TREM2 macs in immune aggregates" — confidence: high — type: methodological — links: [[concepts/trem2-mac-pd1-immune-niche-quartet]] [[claims/trem2-macs-proximal-mregdcs-immune-aggregates]]
- `[c12]` PD-1hi CD8 T cells in direct spatial contact with TREM2 macs upregulate activation/cytotoxicity markers (KLRK1, CD69, CD27, CXCR6, CXCR4, CD2, EOMES, CXCL16, GZMA, GZMK, GZMH) compared with PD-1hi CD8 T cells distal from TREM2 macs (p.5, Fig. S3d) "PD-1hi CD8 T cells in direct contact with TREM2 macs exhibited elevated levels of activation and cytotoxicity markers (KLRK1, CD69, CD27, CXCR6, CXCR4, CD2), as well as the transcription factor EOMES and cytotoxic cytokines (CXCL16, GZMA, GZMK, GZMH)" — confidence: high — type: correlational — links: [[claims/pd1hi-cd8-contact-trem2-upregulate-activation-cytotoxicity]]
- `[c13]` PD-1hi CD8 T cells distal from TREM2 macs upregulate exhaustion markers (HAVCR2, TOX, TIGIT) relative to PD-1hi CD8 T cells in TREM2-mac contact (p.5, Fig. S3d) "those distal to TREM2 macs showed increased expression of exhaustion markers (HAVCR2, TOX, TIGIT)" — confidence: high — type: correlational — links: [[claims/pd1hi-cd8-distal-trem2-upregulate-exhaustion-markers]]
- `[c14]` TREM2 macs in direct contact with PD-1hi CD8 T cells upregulate MHC-II antigen-presentation molecules (HLA-DQA1, -DQB1, -DRB1, -DRA), IFNGR1, and the T-cell costimulatory molecule CD86 (p.5, Fig. S3e) "TREM2 macs engaged in direct interactions with PD-1hi CD8 T cells exhibited enhanced antigen-presenting capacity, marked by increased expression of MHC-II molecules (HLA-DQA1, -DQB1, -DRB1, -DRA), cytokine receptors, and T cell co-stimulatory molecules (IFNGR1, CD86)" — confidence: high — type: correlational — links: [[claims/trem2-macs-contact-pd1hi-cd8-upregulate-mhcii-costim]]
- `[c15]` 48 genes are shared between HCC and NSCLC TREM2 mac DEGs, constituting a conserved core TREM2 program preserved across tumor types (p.6, Fig. 3b) "48 conserved genes constituting a core TREM2 program" — confidence: high — type: quantitative — links: [[concepts/trem2-tumor-associated-macrophage]] [[claims/trem2-program-48-conserved-genes-hcc-nsclc-core]]
- `[c16]` Tissue-specific TREM2 mac DEGs comprise 209 liver-specific and 89 lung-specific genes, accounting for organ-specific specialisation on top of the conserved core (p.6, Fig. 3b) "209 liver-specific genes and 89 lung-specific genes" — confidence: high — type: quantitative — links: [[concepts/hepatic-trem2-protective-tam-program]] [[concepts/tissue-specific-tam-function-context-dependence]] [[claims/trem2-program-tissue-specific-209-liver-89-lung-genes]]
- `[c17]` Hepatic TREM2 macs uniquely express high levels of metallothioneins (MT1G, MT1H), proposed to protect against oxidative stress and ferroptotic lipid peroxidation in liver TME (p.6, Fig. 3h) "hepatic TREM2 macs expressed highest levels of metallothionens (i.e., MT1G, MT1H), which are essential for protecting against oxidative stress and inhibiting ferroptosis-related lipid peroxidation" — confidence: medium — type: mechanistic — links: [[concepts/hepatic-trem2-protective-tam-program]] [[claims/hepatic-trem2-macs-metallothionein-mt1g-mt1h-ferroptosis-protection]]
- `[c18]` Hepatic TREM2 macs uniquely express high levels of CALR (calreticulin), a pro-phagocytic surface molecule that counteracts CD47-mediated 'don't-eat-me' signaling — proposed as a hepatic-specific cell-debris-clearance feature (p.6, Fig. 3h) "TREM2 macs in HCC also expressed uniquely high levels of CALR, which encodes calreticulin... This molecule on the cell surface has been to facilitate clearance of cell debris, counteracting the effects of CD47 and its anti-phagocytic function" — confidence: medium — type: mechanistic — links: [[concepts/hepatic-trem2-protective-tam-program]] [[concepts/sirpa-cd47-don-t-eat-me-axis]] [[foundations/calreticulin-calr]] [[claims/hepatic-trem2-macs-calr-counters-cd47-pro-phagocytic]]
- `[c19]` In the independent validation cohort (n=21 cemiplimab + SBRT; scRNAseq on 16), TREM2 macs are again specifically enriched in responders, replicating the discovery-cohort finding (p.6, Fig. 4a) "Consistent with our findings from the exploratory cohort, we observed an enrichment of mo-macs and an exclusion of KCs from tumor samples. Among mo-macs, TREM2 macs were specifically enriched in responders" — confidence: high — type: correlational — links: [[concepts/hepatic-trem2-protective-tam-program]] [[foundations/sbrt-stereotactic-body-radiotherapy]] [[claims/validation-cohort-trem2-enriched-cemiplimab-sbrt-hcc-responders]]
- `[c20]` Responders (complete + partial) across discovery and validation cohorts exhibit lower HCC recurrence rates than non-responders post-surgical resection (p.6, Fig. 4b) "across both the exploratory and validation cohorts, responders, including partial responders, exhibited a lower recurrence rate, compared to non-responders" — confidence: high — type: correlational — links: [[claims/pd1-responders-lower-hcc-recurrence-rate-cross-cohort]]
- `[c21]` TREM2-mac immunological function is tissue-dependent: protective in HCC but immunosuppressive in NSCLC, breast, ovarian — likely driven by tissue-specific DEGs on top of the conserved 48-gene core (p.5-6, Discussion) "the opposing roles of TREM2 macs in anti-tumor immunity – and, in this case, response to PD-1 blockade – between HCC and NSCLC, for example, is likely determined by the tissue-specific DEGs" — confidence: high — type: mechanistic — links: [[concepts/tissue-specific-tam-function-context-dependence]] [[claims/trem2-mac-function-tissue-dependent-hcc-vs-nsclc]]
- `[c22]` A distinct tissue-infiltrating monocyte subset expressing SPP1, CCL2, FN1, IL4I1 (pro-inflammatory: NLRP3, IL1B, CCL3, CCL4, CXCL8) is significantly enriched in tumor lesions of responders relative to non-responders (p.4, Fig. S1e-h) "we also detected a distinct subset of tissue-infiltrating monocytes expressing SPP1, CCL2, FN1, and IL4I1, which were significantly enriched in tumor lesions of responders... high expression of NLRP3, IL1B, CCL3, CCL4, and CXCL8" — confidence: high — type: correlational — links: [[concepts/il4i1-tumor-associated-macrophage]] [[claims/spp1-ccl2-il4i1-monocyte-subset-enriched-hcc-responders]]
- `[c23]` FOLR2 macrophages accumulate in HCC tumor nodules and are enriched in non-responders to PD-1 blockade — paradoxical to breast cancer where FOLR2 macs are linked to enhanced T-cell infiltration and improved survival (p.7, Discussion) "we found that these cells accumulate within tumor nodules and are enriched in non-responders to PD-1 blockade... a similar group of FOLR2 macs was identified in breast cancer, where these cells were instead linked to enhanced T cell infiltration and improved survival" — confidence: medium — type: correlational — links: [[concepts/folr2-tissue-resident-macrophage]] [[concepts/tissue-specific-tam-function-context-dependence]] [[claims/folr2-macs-enriched-hcc-non-responders-paradox]]

## Discussion captured

### Authors' interpretation

The authors interpret their findings as the first evidence that myeloid TREM2 is a major determinant of response to PD-1 blockade in HCC and as a paradigm reversal of the TREM2-mac-as-immunosuppressor model established in NSCLC, breast, and ovarian cancer. They propose that TREM2 expression is induced uniformly across tissues by apoptotic-cell-derived ligands engaging the TREM2 receptor on infiltrating mo-macs, generating a conserved 48-gene core; tissue-specific homeostatic cues (hepatocyte-derived in liver vs alveolar-epithelial in lung) then layer organ-specific programs (ferroptotic protection, calreticulin-mediated clearance in liver) that flip the net immunological output. Spatially, TREM2 macs are positioned as fourth members of a previously described CXCL13⁺-Th / TCF1⁺-PD-1hi-CD8 / mregDC immune-response triad — refined here into a quartet — and direct TREM2-mac/PD-1hi-CD8 contacts correlate with effector activation rather than exhaustion. sTREM2 is positioned as an accessible, blood-based biomarker derived from this biology, with translational utility in stratifying neoadjuvant ICB candidates.

### Comparisons with prior literature (made by authors)

- **Marron et al. (NCT03916627 Cohort B, ref 11)** — established the 30% pathologic-response rate in cemiplimab-treated neoadjuvant HCC; this paper extends to mechanism.
- **Casanova-Acebes 2021, Mulder 2021, Park 2024 (refs 24–26)** — established alveolar-mac depletion and FOLR2/TREM2/IL4I1 mo-mac states in NSCLC; this paper applies the same framework to HCC.
- **Molgora 2020, Katzenelenbogen 2020 (refs 14, 16)** — defined TREM2 mac as pro-tumorigenic in mouse models of sarcoma, colon, breast cancer; this paper contradicts that for HCC.
- **Author group's prior NSCLC paper (ref 13)** — TREM2 macs inhibit NK infiltration in lung cancer and anti-TREM2 rescues anti-tumor immunity; this paper notes the opposite role in HCC.
- **Li et al. (ref 53)** — onco-fetal FOLR2/CAF/endothelial niche associated with HCC relapse; consistent with the FOLR2-mac/non-responder finding here.
- **Hamon et al. prior (ref 12)** — defined CXCL13⁺-Th / TCF1⁺-PD-1hi-CD8 / mregDC ICB-response triad in HCC; this paper extends to a quartet including TREM2 macs.
- **Trem2-/- HCC mouse studies (refs 20, 45-48)** — Trem2 knockout in carcinogen-induced HCC mice increases tumor burden, consistent with a protective hepatic TREM2-mac role.

### Mechanistic hypotheses proposed

- Hepatic homeostatic cues (hepatocyte-derived) program a metallothionein-rich, ferroptosis-resistant TREM2-mac state, whereas alveolar-epithelial-derived cues program a SPP1-rich, tissue-remodelling TREM2-mac state in lung.
- TREM2-mac CALR expression promotes pro-phagocytic clearance of tumor cell debris, counteracting CD47 anti-phagocytic signaling — proposed as a hepatic-specific feature.
- Direct TREM2-mac/PD-1hi-CD8 contacts physically transduce activation/MHC-II/co-stimulation signals; distal PD-1hi-CD8 cells drift toward exhaustion in their absence.
- TREM2 macs may participate in the formation/stabilisation of CXCL13/TCF1/mregDC immune aggregates, not just colocalize.

### Caveats and self-criticism

- The mechanistic basis of tissue-specific TREM2-mac function (protective vs immunosuppressive) is correlational; no in vivo causal manipulation in human tissue.
- TREM2hi vs TREM2lo IMbrave150 stratification is a quartile-cut on top-10 genes — not validated prospectively.
- sTREM2 biomarker validation rests on relatively small cohorts; requires prospective testing.
- Direct ligand-receptor pairs mediating TREM2-mac/PD-1hi-CD8 communication remain unidentified.
- Whether TREM2 macs *cause* immune-aggregate formation or merely co-occupy them is not resolved.

### Future directions suggested

- Ligand-receptor / metabolite screening of TREM2-mac/T-cell interactions.
- Determine pre-treatment TREM2-mac infiltration thresholds usable for patient selection.
- Test whether TREM2 blockade is harmful in HCC (opposite of NSCLC strategy).
- Mechanistic dissection of metallothionein / CALR axes in hepatic TREM2 macs.
- Whether the quartet (TREM2-mac + CXCL13-Th + TCF1-CD8 + mregDC) is causally required for ICB response.

## Limitations

- All cohorts are limited in size (n=20–21 per neoadjuvant arm; n=17 baseline-serum cohort).
- Cross-tumor comparison relies on previously published external datasets — batch effects, platform differences, and sample-handling heterogeneity could bias core-vs-tissue-specific gene partitioning.
- TREM2 program score is a top-10-gene quartile cut; an optimised signature would likely improve performance.
- MERFISH proximity analysis relies on Cellpose-derived segmentation with 20% mask shrinkage — peripheral transcript loss is an acknowledged source of bias.
- IMbrave150 and POPLAR bulk-RNA stratifications cannot distinguish TREM2-mac abundance from intrinsic tumor TREM2 expression — deconvolution would clarify.
- No mouse perturbation in HCC: anti-TREM2 effects are inferred from prior cirrhosis / DEN models, not tested in HCC under PD-1 blockade.
- sTREM2 measured at baseline only — kinetics during/after treatment, and contribution from non-tumor sources, are not assessed.

## Open questions

### Open questions raised by authors

- Through what receptors / cytokines / metabolites do TREM2 macs physically modulate PD-1hi T cells?
- Does pre-treatment TREM2-mac infiltration determine response prospectively?
- What hepatic-specific signals (homeostatic, ferroptotic, NASH-related, chronic inflammation) program the protective TREM2-mac state?
- Does TREM2 blockade harm anti-tumor immunity in HCC (opposite of NSCLC)?
- Do TREM2 macs causally drive the formation/stabilisation of CXCL13/TCF1/mregDC immune aggregates?

### Open questions identified during ingest

- Whether the CALR-high hepatic-TREM2 program is induced by tumor-cell-derived apoptotic debris or by intrinsic hepatic cues (hepatocyte-derived ligands).
- Whether the metallothionein program reflects iron / oxidative-stress conditioning unique to liver TME, or a more general damage-response.
- Whether sTREM2 in serum is shed predominantly by intratumoral macs or systemically (Kupffer, microglia, bone marrow) — limits biomarker specificity.
- Whether TREM2-mac protective programs co-occur with the mMAC1/IL4I1 hypoxic-inflammatory program defined elsewhere (relevant to HypoxiaVERSE / thesis bridging).
- Whether the FOLR2-mac/non-responder enrichment in HCC reflects an onco-fetal niche replay (Li et al.) or a distinct immune-exclusion mechanism.

## My take

This paper is a high-value translational ingest for the thesis for several reasons:

1. **Tissue-specific TAM function**: The cleanest demonstration to date that a "canonical immunosuppressive" mac state (TREM2 TAM) can flip sign with tissue context. For pan-cancer TAM modelling (HypoxiaVERSE and beyond), it forces an organ-aware design rather than a one-program-fits-all view.
2. **Quartet expansion of the ICB-response niche**: The TREM2-mac + CXCL13-Th + TCF1-CD8 + mregDC quartet is a cleanly testable hypothesis that ties macrophage spatial biology directly to T-cell-centric ICB-response models.
3. **sTREM2 as a translational biomarker**: One of the few accessible blood biomarkers for HCC ICB response; if it generalises, it would inform neoadjuvant patient selection.
4. **Hepatic CALR / metallothionein program**: The CALR aspect (counter-CD47, pro-phagocytic) is mechanistically interesting and points toward a tumor-debris-clearance program that may distinguish hepatic mo-macs from lung mo-macs. Worth following up.
5. **Paradigm-aware framing**: Echoes the broader literature trend that TAM functional class (immunosuppressive vs immunostimulatory) is not gene-program-monomorphic but is shaped by activation context (cf. mMAC1 hypoxia paradigm) and tissue context (here).

Caveats: cohorts are small; mechanism is correlational; the quartet is observed not perturbed. The single-cell findings would benefit greatly from in situ perturbation (anti-TREM2 in a hepatic preclinical PD-1 model under chronic-inflammation conditioning).

## Related

- [[papers/tissue-resident-macrophages-provide-pro-tumorigenic]] — defines TREM2-mac / FOLR2-mac / Group-II MDM ontogeny in NSCLC; provides the comparator tissue for the HCC vs NSCLC TREM2-mac contrast central to this paper
- [[papers/cross-tissue-single-cell-landscape-human]] — MoMac-VERSE atlas; provides the pan-cancer TREM2-mac cluster #3 definition that this paper refines with HCC-specific 209-gene program
- [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] — companion lens: hypoxic-activation paradigm reversal for IL4I1-mac immunogenicity, complementary to this paper's tissue-context paradigm reversal for TREM2-mac
- [[papers/pd-l1-expressing-tumor-associated-macrophages]] — analogous functional-reversal narrative for PD-L1⁺ TAM in breast cancer
- [[concepts/trem2-tumor-associated-macrophage]] — pan-cancer concept now extended with hepatic protective variant
- [[concepts/hepatic-trem2-protective-tam-program]] — hepatic-specific protective program defined here
- [[concepts/folr2-tissue-resident-macrophage]] — paired non-responder-associated mac state
- [[concepts/soluble-trem2-icb-response-biomarker]] — blood-based predictive biomarker introduced here
- [[concepts/trem2-mac-pd1-immune-niche-quartet]] — quartet refinement of the prior CXCL13/TCF1/mregDC triad
- [[concepts/tissue-specific-tam-function-context-dependence]] — generalisation principle motivated by this paper
- [[concepts/cxcl13-cxcr5-tls-recruitment]] — companion T-cell niche concept
- [[concepts/sirpa-cd47-don-t-eat-me-axis]] — counterpart to CALR pro-phagocytic axis
- [[foundations/trem2-receptor]] — central receptor
- [[foundations/merfish-imaging-spatial]] — spatial transcriptomics method
- [[claims/trem2-tam-hcc-better-pd1-response]] — multi-source claim; this paper is a corroborating source
- [[foundations/pic-seq-physically-interacting-cells]] — physical-contact sequencing method
- [[foundations/cellpose-cell-segmentation]] — segmentation pipeline
- [[foundations/imbrave150-trial]] — phase III HCC ICB cohort
- [[foundations/cemiplimab]] — anti-PD-1 used in discovery and validation cohorts
- [[foundations/pd-1-receptor-pdcd1]] — checkpoint receptor
- [[foundations/calreticulin-calr]] — hepatic-specific pro-phagocytic marker
- [[foundations/sbrt-stereotactic-body-radiotherapy]] — validation-cohort modality
- [[foundations/hepatocellular-carcinoma-hcc]] — disease foundation
- [[foundations/folr2-receptor]] — FOLR2-mac defining marker
- [[foundations/gpnmb-protein]] — TREM2-mac defining marker
