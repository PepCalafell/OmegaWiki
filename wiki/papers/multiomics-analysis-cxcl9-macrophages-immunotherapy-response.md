---
# === Identification ===
title: "Multiomics analysis of CXCL9+ macrophages in the immunotherapy response of bladder cancer"
slug: "multiomics-analysis-cxcl9-macrophages-immunotherapy-response"
arxiv: ""
doi: "10.21203/rs.3.rs-5587651/v1"
pmid: ""
venue: "Research Square (preprint)"
year: 2024
authors: ["Lin Zhou", "Guopeng Yu", "Zhongpeng Zheng", "Yushan Liu", "Bin Xu"]
first_author: "Lin Zhou"
corresponding_author: "Bin Xu"

# === Source & metadata ===
source_type: pdf
s2_id: ""
date_added: 2026-06-05
ingested_date: 2026-06-05
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 3
tier: TIER_2
tags: [bladder-cancer, CXCL9, macrophages, immunotherapy, ICB, biomarker, scRNA-seq, spatial-transcriptomics, multiomics, Mscore, TAM]
keywords: [bladder cancer, CXCL9, macrophages, immunotherapy, IMvigor210, CIBERSORTx, Mscore]
domain: "oncology / immunology"

# === Biomedical domain ===
tissue: [bladder]
condition: [cancer]
disease_specific: [bladder_cancer, urothelial_carcinoma]
species: [human]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [scRNA-seq_10x, spatial_visium, bulk_RNA-seq, methylation_array]
n_samples: 16
n_cells_total: 113905
integration_method: "Harmony"

# === Biology captured ===
key_cell_types: [Macro-CXCL9, Macro-SPP1, Macro-FOLR2, Macro-CCL4, CD8-CXCL13 T cells, CXCL14+ fibroblasts, endothelial cells]
key_markers: [CXCL9, CXCL10, SPP1, FOLR2, CCL4, PDCD1, CD274, FGFR3, LAG3, ACKR1, C3, CTSC, CAPG, CTSB]
key_pathways: [CXCR3-CXCL9/10/11 axis, IFN-gamma signaling, immune checkpoint blockade]

# === User project membership ===
projects: [thesis]
priority: reference
read_status: not_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "scRNA-seq in-house on request; PRJNA662018; stRNA GSE171351; IMvigor210 (IMvigor210CoreBiologies R package); TCGA via UCSC Xena; RCC SCP1288; BC biokey.lambrechtslab.org"

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Immune checkpoint inhibitors (anti-PD-1/PD-L1) benefit only a minority of bladder cancer patients (≈6% complete, 17% partial response in metastatic monotherapy), and no biomarker reliably stratifies responders. Macrophages are a dominant TME component whose functional subsets may explain differential ICB response, but the relevant macrophage states and their predictive value in bladder cancer were undefined.

## Key idea

Use integrated single-cell, spatial, and bulk multiomics to resolve tumour macrophage subsets in bladder cancer, identify a CXCL9⁺ macrophage state (Macro-CXCL9) associated with ICB response, and distil its marker genes into a clinically usable risk score (Mscore) for patient stratification.

## Method

- Integrated scRNA-seq of 16 bladder cancer patients (public PRJNA662018 n=11 + in-house n=5); 113,905 cells; Seurat v4.3.0 + Harmony batch correction; myeloid sub-clustering.
- Trajectory/RNA-velocity (scVelo, velocyto, PAGA) and TF regulon inference (pySCENIC).
- Spatial transcriptomics (Visium, GSE171351) mapped with CellTrek; cell-cell interactions with LIANA.
- CIBERSORTx deconvolution of IMvigor210 and TCGA bulk cohorts; pan-cancer TCGAplot analysis.
- ConsensusClusterPlus immune subtyping; AIC-selected multivariate Cox regression to build the five-gene Mscore; ROC/Kaplan-Meier validation.

## Results

Four macrophage subsets (Macro-CCL4, -CXCL9, -FOLR2, -SPP1) were resolved; Macro-CXCL9 sits at the inferred differentiation origin, carries distinct TF activity, and is enriched in ICB responders across IMvigor210 and re-analysed breast/RCC cohorts. Five immune subtypes (A–E) were defined, with the Macro-CXCL9-high class (E in IMvigor210, B in TCGA) showing distinct mutations; FGFR3 mutation marked immune-cold tumours. A five-gene Mscore predicted worse OS and ICB response (14% vs 44%), was an independent prognostic factor (HR=1.92), and combined with TMB/TNB reached AUC 0.7758.

## All claims (exhaustive)

- `[c1]` Macro-CXCL9 occupies the early node of the tumour macrophage differentiation trajectory (p.4) "Macro-CXCL9 subpopulation is situated at the initial differentiation site of macrophages. We identified differentiation pathways from Macro-CXCL9 to Macro-SPP1 and Macro-FOLR2." — confidence: low — type: mechanistic — links: [[concepts/macro-cxcl9-progenitor-node-tumor-macrophage]] [[foundations/scvelo-rna-velocity]] [[foundations/paga-trajectory]] [[claims/macro-cxcl9-occupies-early-node-tumor]]
- `[c2]` Bladder cancer TME contains four macrophage subpopulations (Macro-CCL4/-CXCL9/-FOLR2/-SPP1) (p.3-4) "we discerned four primary macrophage populations: Macro-CCL4 (CCL4), Macro-CXCL9 (CXCL9), Macro-FOLR2 (FOLR2), and Macro-SPP1 (SPP1)." — confidence: high — type: methodological — links: [[concepts/cxcl9-spp1-tam-ratio-ici-biomarker]] [[foundations/scrna-seq-10x-chromium]] [[foundations/harmony-integration]] [[foundations/spp1-secreted-phosphoprotein-1]] [[foundations/folr2-receptor]] [[claims/bladder-cancer-tme-contains-four-macrophage]]
- `[c3]` Macro-CXCL9 abundance is higher in immunotherapy responders across cohorts (p.4) "The responder (R) group in this cohort showed a significantly higher proportion of Macro-CXCL9 (P < 0.001) ... Tumors responsive to treatment after therapy exhibited higher levels of Macro-CXCL9." — confidence: medium — type: correlational — links: [[concepts/ifng-mac-cxcl9-tam-ici-responder]] [[concepts/cell-state-deconvolution]] [[foundations/cibersortx-deconvolution]] [[foundations/cxcl9-chemokine]] [[claims/macro-cxcl9-abundance-higher-immunotherapy-responders]]
- `[c4]` Macro-CXCL9 is governed by distinct TFs (LYL1, NRF1, SMARCC2, CCNT2, TCF3) (p.4) "The specific transcription factors for Macro-CXCL9 include LYL1, NRF1, SMARCC2, CCNT2, and TCF3." — confidence: low — type: mechanistic — links: [[foundations/scenic-tf-regulon-inference]] [[concepts/macro-cxcl9-progenitor-node-tumor-macrophage]] [[claims/macro-cxcl9-governed-distinct-transcription-factors]]
- `[c5]` Macro-CXCL9 engages ACKR1⁺ endothelium and LAG3⁺ CD8-CXCL13 cells via distinct ligand-receptor axes (p.4-5) "CXCL9 and CXCL10 secreted by Macro-CXCL9 can interact with ACKR1 ... Macro-CXCL9 also produces HLA-DRB1, HLA-DQB1, and HLA-DQA1, which bind to the LAG3 receptor on CD8-CXCL13 cells." — confidence: low — type: mechanistic — links: [[foundations/liana-cell-cell-interaction-inference]] [[foundations/cxcl10-chemokine]] [[concepts/tam-t-cell-spatial-proximity-tme]] [[claims/macro-cxcl9-ligand-receptor-interactions-ackr1]]
- `[c6]` Bladder cancer stratifies into five immune subtypes (A-E) with the Macro-CXCL9-high class (E in IMvigor210, B in TCGA) (p.5) "we identified five stable bladder cancer subtypes ... labeled A through E ... Class E patients had significantly more Macro-CXCL9 than other classes (all P < 0.001)." — confidence: medium — type: methodological — links: [[concepts/macrophage-abundance-immune-subtypes-bladder-cancer]] [[foundations/consensusclusterplus-consensus-clustering]] [[foundations/tcga-the-cancer-genome-atlas]] [[claims/five-immune-subtypes-bladder-cancer-class]]
- `[c7]` FGFR3 mutation is associated with reduced CXCL9, CXCL10, PDCD1, and CD274 expression (p.5) "FGFR3 mutations were linked to lower levels of CXCL9, CXCL10, PDCD1, and CD274 expression." — confidence: medium — type: correlational — links: [[foundations/pd-1-receptor-pdcd1]] [[foundations/pd-l1-cd274]] [[claims/fgfr3-mutation-associated-reduced-cxcl9-cxcl10]]
- `[c8]` A five-gene Mscore (CXCL9, C3, CTSC, CAPG, CTSB) predicts ICB efficacy in bladder cancer (p.6) "Mscore = -0.1463152×Exp.CXCL9 + 0.1018251×Exp.C3 + 0.1316632×Exp.CTSC − 0.1869480×Exp.CAPG + 0.1556237×Exp.CTSB." — confidence: medium — type: methodological — links: [[concepts/mscore-cxcl9-macrophage-marker-gene-icb]] [[claims/five-gene-mscore-predicts-immune-checkpoint]]
- `[c9]` High Mscore correlates with worse OS and reduced ICB response (14% vs 44%) (p.6) "Patients with elevated Mscores exhibited significantly worse overall survival ... and showed a reduced response to treatment compared to those with lower Mscores (14% vs. 44%, P < 0.001)." — confidence: medium — type: quantitative — links: [[concepts/mscore-cxcl9-macrophage-marker-gene-icb]] [[concepts/immune-checkpoint-blockade]] [[claims/high-mscore-correlates-worse-survival-reduced]]
- `[c10]` Mscore is an independent prognostic indicator (HR=1.92) inversely correlated with TMB (r=-0.28) and TNB (r=-0.36); Mscore+TMB+TNB AUC=0.7758 (p.6) "Multivariate Cox regression analysis identified Mscores (Cox P-value = 0.01, Hazard Ratio = 1.92) ... inverse correlations between Mscore and both TMB (P < 0.001, r = − 0.28) and TNB (P < 0.001, r = − 0.36) ... AUC value of 0.7758." — confidence: medium — type: quantitative — links: [[concepts/mscore-cxcl9-macrophage-marker-gene-icb]] [[claims/mscore-independent-prognostic-indicator-inversely-correlated]]

## Discussion captured

### Authors' interpretation

The authors interpret Macro-CXCL9 as a pivotal early-differentiation macrophage whose distinct TF profile and positive correlations with CXCL13⁺CD4⁺ T cells, NR4A2⁺ B cells, CXCL14⁺ fibroblasts and germinal-centre B cells reflect a complex network promoting anti-tumour immunity. They position Macro-CXCL9 abundance and the derived Mscore as predictors of ICB efficacy and a basis for patient stratification.

### Comparisons with prior literature (made by authors)

- Bill et al. *Science* 2023 — CXCL9:SPP1 macrophage polarity controlling human cancers [ref 7].
- Marcovecchio et al. *J Immunother Cancer* 2021 — CXCL9-expressing TAMs as anti-cancer players [ref 8].
- Cappuyns et al. *Nat Commun* 2023 — CXCL10⁺ macrophages and effector-memory CD8 T cells in atezo/bev responders (HCC) [ref 9].
- Hoch et al. *Sci Immunol* 2022 — IMC of chemokine milieus; CXCL9/CXCL10 co-localise with LAG3⁺ T cells [ref 10].
- House et al. *Clin Cancer Res* 2020 — macrophage-derived CXCL9/CXCL10 required for antitumour responses after ICB [ref 21].
- Zhang et al. *J Clin Invest* 2024 — CXCL9⁺ macrophages induce TWIST1 in FAP⁺ fibroblasts via IL-1β/TGF-β [ref 13].

### Mechanistic hypotheses proposed

- "Macrophage-expressed CXCL9 regulates the recruitment and localization of stem-like CD8 T cells expressing CXCR3, contributing to clinical responses to anti-PD-1 or PD-L1 therapies" (p.3).
- Atezo/bev may enhance activation of PD-L1-expressing CXCL10⁺ macrophages, releasing CXCL9/10/11 into the TME (p.4).

### Caveats and self-criticism

- Datasets gathered retrospectively, which "may inevitably introduce some degree of bias" (p.8).
- No phase-3 RCT validates Mscore-based prognosis/response (p.8).
- Marker-gene biology not explored in bladder cancer cells; needs experimental validation (p.8).

### Future directions suggested

- Prospective clinical-trial validation of Macro-CXCL9 / Mscore as predictive biomarkers; experimental dissection of marker-gene function in bladder cancer cells.

## Limitations

- Retrospective bulk/single-cell cohorts; modest sample size for in-house scRNA-seq (n=5).
- Trajectory, TF, and cell-cell interaction findings are computational inferences without lineage tracing, perturbation, or spatial-contact validation.
- Mscore developed and tested on the same retrospective cohorts; cohort-specific class labels (E vs B); moderate AUC (0.7758).

## Open questions

### Open questions raised by authors

- Which TAM subsets exert antitumour effects and the optimal timing for intervention remain challenges across tumour types (p.7).
- Precise mechanisms of TIL recruitment under ICIs are "not yet fully understood" (p.7).

### Open questions identified during ingest

- Is the Macro-CXCL9 differentiation origin a true hierarchy or an IFN-γ activation continuum?
- Does Mscore add predictive value beyond CXCL9:SPP1 ratio, CXCL9 alone, PD-L1, or TMB?
- Do the five immune subtypes replicate prospectively and guide subtype-specific therapy?

## My take

A competent but largely re-analysis-driven preprint that repackages the well-established CXCL9⁺ (IFN-γ-driven) vs SPP1⁺ TAM polarity story into a bladder-cancer-specific Mscore. The biomarker is plausible and the multiomics integration is thorough, but everything rests on retrospective deconvolution and computational inference; the developmental and ligand-receptor claims are weak, and clinical value awaits prospective validation. Useful mainly as a bladder-cancer instance of [[concepts/cxcl9-spp1-tam-ratio-ici-biomarker]].

## Related

- [[concepts/cxcl9-spp1-tam-ratio-ici-biomarker]]
- [[concepts/ifng-mac-cxcl9-tam-ici-responder]]
- [[concepts/macro-cxcl9-progenitor-node-tumor-macrophage]]
- [[concepts/mscore-cxcl9-macrophage-marker-gene-icb]]
- [[concepts/macrophage-abundance-immune-subtypes-bladder-cancer]]
- [[people/lin-zhou]]
- [[people/bin-xu]]
