---
title: "Development of a hypoxia-responsive macrophage prognostic model using single-cell and bulk RNA sequencing in pancreatic cancer"
slug: development-hypoxia-responsive-macrophage-prognostic-model
arxiv: ""
doi: "10.1371/journal.pone.0322618"
pmid: "40315225"
venue: "PLoS One"
year: 2025
authors:
  - Heming Ge
  - Gerrit Wolters-Eisfeld
  - Thilo Hackert
  - Yuqiang Li
  - Cenap Güngör
first_author: "Heming Ge"
corresponding_author: "Cenap Güngör"

source_type: pdf
s2_id: "a28c1f8b79257c664c811788e61bf9094e13c61d"
date_added: 2026-05-25
ingested_date: 2026-05-25
ingest_version: 1
last_reviewed:

importance: 3
tier: TIER_2
tags: [hypoxia, PDAC, pancreatic-cancer, tumor-associated-macrophage, prognostic-model, LASSO-Cox, scRNA-seq, TCGA-PAAD, KRTCAP2, chemoresistance, pan-cancer]
keywords: [hypoxia-responsive macrophage, macrophage cluster 1, LASSO Cox, 13-gene signature, KRTCAP2, TCGA-PAAD, GSE155698, PACA-CA, PACA-AU, oncoPredict, ESTIMATE, CIBERSORT, AddModuleScore, AUCell, MSigDB Hallmark Hypoxia]
domain: oncology

tissue: [pancreas, blood]
condition: [cancer]
disease_specific: [pancreatic_cancer]
species: [human]
hypoxia_relevant: true
contains_immune_cells: true
contains_myeloid: true

techniques: [scRNA-seq_10x, bulk_RNA-seq, ssGSEA, LASSO_Cox, CIBERSORT, ESTIMATE, oncoPredict, maftools, GISTIC2, AUCell, AddModuleScore, clusterProfiler_GSEA]
n_samples: 159
n_cells_total: 44334
integration_method: "Seurat v5 standard workflow (no batch-correction stated beyond default integration)"

key_cell_types: [macrophage_cluster1, macrophage_cluster2, epithelial_cells, neutrophil, T_cell, NK_cell, B_cell, plasma_cell, mast_cell, dendritic_cell, endothelial_cell, fibroblast, pericyte, acinar_cell]
key_markers: [LYZ, SCN1B, PLAU, INSIG2, DSC2, MICAL1, U2AF1, KRTCAP2, DDX60L, SATB1, SAMD9, LTC4S, IGLL5, KRAS, TP53, CDKN2A, SMAD4, TTN]
key_pathways: [hypoxia, cell_cycle, DNA_replication, E2F_targets, G2M_checkpoint, mitotic_spindle, protein_processing_ER, ribosome, nucleotide_metabolism, amino_acid_biosynthesis]

projects: [thesis, hypoxia]
priority: reference
read_status: skimmed

hypoxiaverse_status:
exclusion_reason:
data_availability: "scRNA-seq data: GEO GSE155698 (Steele et al. 2020); bulk transcriptomic and clinical data: TCGA-PAAD, ICGC PACA-CA and PACA-AU. No primary data deposited by this study."

code_url: ""
cited_by: []
---

## Problem

Pancreatic ductal adenocarcinoma (PDAC) has a 5-year survival rate ~10% and limited immunotherapy responsiveness. Hypoxia is a hallmark of the PDAC microenvironment and drives metabolic reprogramming, EMT, immune evasion and chemoresistance, yet existing bulk-tissue hypoxia signatures do not resolve *which* cell types in the PDAC TME are most affected by hypoxia and which cell-state-anchored genes carry prognostic information. The paper asks: can a single-cell-anchored hypoxia signature derived from the most hypoxia-responsive immune cell subset stratify PDAC survival and predict chemotherapy sensitivity?

## Key idea

Compute per-cell hypoxia signature scores across annotated immune cell types in PDAC scRNA-seq, identify macrophages as the most hypoxia-responsive immune cell type, subcluster macrophages into a hypoxia-high "cluster 1" and a hypoxia-low "cluster 2", take the DEGs of cluster 1 (PDAC vs normal pancreas), univariate-Cox-shortlist them against TCGA-PAAD OS, shrink to 13 genes via LASSO-Cox, and use the resulting hypoxia score for stratification, GSEA, mutation-landscape, immune-deconvolution, drug-sensitivity, and pan-cancer prognostic analyses — with KRTCAP2 surfaced as a recurrent pan-cancer prognostic biomarker.

## Method

- **scRNA-seq cohort**: GSE155698 (Steele 2020) — 16 primary PDAC + 3 non-malignant pancreas; ~37k tumour + ~7.3k normal cells after QC ([[foundations/gse155698-steele-pdac-scrnaseq]]).
- **scRNA processing**: [[foundations/seurat-v3-integration]] (v5.0.1) — QC (gene count 200–5000, mt<20%), LogNormalize, FindVariableFeatures (2000), PCA top 30, FindNeighbors / FindClusters (res 0.4), UMAP; 13 annotated cell types via top markers.
- **Hypoxia scoring per cell**: [[foundations/msigdb-hallmark-hypoxia]] 200-gene set; per-cell scores via [[foundations/addmodulescore-seurat]] and [[foundations/aucell-gene-set-activity]].
- **Bulk hypoxia score**: [[foundations/ssgsea-single-sample-gsea]] (GSVA v1.46.0, 1000 permutations) on TCGA-PAAD using the Hallmark Hypoxia 200-gene set; median dichotomisation.
- **Macrophage subclustering**: re-clustering of macrophage cells; "cluster 1" = high hypoxia score, "cluster 2" = low. GSEA between clusters via [[foundations/clusterprofiler-gsea]] (NES |>1|, FDR<0.25, p<0.05, 1000 permutations).
- **DEG → signature**: cluster 1 PDAC-vs-normal DEGs (Seurat `FindMarkers`, Wilcoxon, |log2FC|>0.25, p<0.05) → 882 DEGs → univariate Cox on TCGA-PAAD OS → 23 prognostic genes → [[foundations/lasso-cox-glmnet]] (10-fold CV, λ.min=0.0432) → 13 final genes (LYZ, SCN1B, PLAU, INSIG2, DSC2, MICAL1, U2AF1, KRTCAP2, DDX60L, SATB1, SAMD9, LTC4S, IGLL5).
- **Prognostic evaluation**: KM + log-rank, time-dependent ROC (timeROC v0.4), decision curve analysis (ggDCA v1.2); nomogram integrating clinicopathologic features and hypoxia score.
- **External validation**: [[foundations/icgc-paca-pdac-cohorts]] PACA-CA (n=142) and PACA-AU (n=76).
- **Mutation landscape**: [[foundations/maftools-mutation-analysis]] (v2.14.0) for SNV / TMB; [[foundations/gistic2-copy-number]] (thresholds ±0.2) for CNV.
- **Immune deconvolution**: [[foundations/estimate-stromal-immune-score]] (v1.0.13) for purity / immune / stromal scores; [[foundations/cibersortx-deconvolution]] (CIBERSORT, LM22) for 22 immune subsets.
- **Drug sensitivity**: [[foundations/oncopredict-drug-sensitivity]] (v0.2) against GDSC database; per-drug IC50 prediction; Wilcoxon test between high vs low hypoxia groups.
- **Pan-cancer analysis**: TCGA across cancer types for OS/DSS/DFS/PFS, KRTCAP2 expression vs adjacent normal, vs stage, and vs immune cell infiltration.

## Results

1. High tumour hypoxic microenvironment score correlates with worse OS and PFS in TCGA-PAAD (Fig 1, 2A–B).
2. Across 13 annotated PDAC cell types, macrophages have the highest per-cell hypoxia signature score (Fig 2E–F).
3. Macrophage subclustering yields a hypoxia-high "cluster 1" (Fig 2G); GSEA confirms Hallmark Hypoxia is enriched in cluster 1 vs cluster 2 (Fig 2H–J).
4. PDAC-vs-normal DEGs within macrophage cluster 1 yield 882 genes (571 up, 311 down). Univariate Cox keeps 23 genes; LASSO-Cox (λ=0.0432) collapses to 13 (Fig 3A–B).
5. Hypoxia score (13-gene signature) stratifies TCGA-PAAD into high vs low groups; high group has significantly worse OS (Fig 3C–D). Time-dependent ROC AUC: 0.774 (1y), 0.727 (2y), 0.711 (3y); decision-curve benefit exceeds clinicopathologic-feature-only model (Fig 3E–G).
6. Multivariate Cox confirms hypoxia score is independent of age, sex, T, N, AJCC stage (Fig 4A; S3). Nomogram with hypoxia+clinicopath features outperforms clinicopath alone (Fig 4D–F).
7. GSEA in TCGA-PAAD: high-hypoxia samples enriched for amino-acid biosynthesis, cell cycle, DNA replication, E2F, G2M, mitotic spindle, ribosome, protein processing in ER, hypoxia (Fig 5A–B).
8. SNV/CNV/TMB: top mutated genes (KRAS, TP53, CDKN2A, SMAD4, TTN) shared between groups. Overall mutation rate 90.28% (high) vs 78.87% (low). CNV gains enriched in high; TMB higher in high; Pearson r between hypoxia and TMB = 0.28, p<0.001 (Fig 5C–G).
9. ESTIMATE: high hypoxia → higher purity, lower immune, stromal, and ESTIMATE scores. CIBERSORT (LM22): naïve B cells reduced, M0 macrophages enriched in high hypoxia (Fig 6A–C).
10. oncoPredict / GDSC: gemcitabine, oxaliplatin, cisplatin, 5-FU and paclitaxel IC50 elevated in high hypoxia group (Fig 6D).
11. Pan-cancer (TCGA): 13 hypoxia-related genes are significantly associated with OS, DSS, DFS, PFS across multiple cancer types (Fig 7A–D). KRTCAP2 emerges as a consistent prognostic marker (HR>1 across nearly all cancers) with elevated expression in tumour vs adjacent normal and rising expression with stage (Fig 7E–F). KRTCAP2 negatively correlates with γδ T, CD8+, CD4+ memory-activated T, neutrophils, monocytes, resting mast, M1 macrophages, activated DCs; positively with Tregs (Fig 7G).

## All claims (exhaustive)

- `[c01]` Macrophages have the highest per-cell hypoxia signature scores among PDAC immune cell types in GSE155698 (p.5, Results) "macrophages exhibited the highest hypoxic microenvironment scores, significantly higher than those of other immune cell types (Fig 2E and 2F)" — confidence: high — type: correlational — links: [[concepts/hypoxia-responsive-macrophage-subset-pdac]] [[foundations/gse155698-steele-pdac-scrnaseq]] [[claims/macrophages-highest-hypoxia-score-pdac-immune-cells]]
- `[c02]` A 13-gene hypoxia-responsive macrophage signature (LYZ, SCN1B, PLAU, INSIG2, DSC2, MICAL1, U2AF1, KRTCAP2, DDX60L, SATB1, SAMD9, LTC4S, IGLL5) was constructed by LASSO-Cox (λ=0.0432) on TCGA-PAAD from macrophage cluster 1 DEGs (p.5–6, Results) "13 hypoxia-related genes were finally included in the construction of the hypoxia-related prognostic model" — confidence: high — type: methodological — links: [[concepts/scrna-derived-lasso-cox-prognostic-signature]] [[foundations/lasso-cox-glmnet]] [[foundations/krtcap2-gene]] [[foundations/plau-urokinase]] [[claims/13-gene-hypoxia-prognostic-model-pdac]]
- `[c03]` Hypoxia score time-dependent ROC AUC in TCGA-PAAD: 0.774 (1y), 0.727 (2y), 0.711 (3y), exceeding clinicopathologic features alone (p.6, Results) "AUC values were 0.774 at 1 year, 0.727 at 2 years, and 0.711 at 3 years (Fig 3E). These values were significantly superior to those derived from clinicopathologic characteristics alone" — confidence: high — type: quantitative — links: [[foundations/tcga-paad-pancreatic-cohort]] [[claims/hypoxia-model-tcga-paad-os-auc]]
- `[c04]` High hypoxia score correlates with higher TMB in TCGA-PAAD (Pearson r=0.28, p<0.001; mutation rate 90.28% high vs 78.87% low) (p.9, Results) "the hypoxia score was positively correlated with TMB, with a correlation coefficient of 0.28 and a statistically significant level (P < 0.001)" — confidence: high — type: correlational — links: [[foundations/maftools-mutation-analysis]] [[foundations/gistic2-copy-number]] [[claims/high-hypoxia-score-correlates-tmb-pdac]]
- `[c05]` KRTCAP2 is consistently associated with poor pan-cancer prognosis (HR>1 across nearly all TCGA types) and tracks immune exclusion (low CD8/M1, high Treg) (p.12–13, Results + Discussion) "KRTCAP2 consistently emerged as a prognostic marker, with its expression linked to unfavorable outcomes across nearly all investigated cancer types, evidenced by a hazard ratio (HR) greater than 1" — confidence: medium — type: correlational — links: [[concepts/krtcap2-pan-cancer-biomarker]] [[foundations/krtcap2-gene]] [[claims/krtcap2-pan-cancer-poor-prognosis-immune-exclusion]]
- `[c06]` High hypoxia score predicts reduced sensitivity (elevated IC50) to gemcitabine, oxaliplatin, cisplatin, 5-FU and paclitaxel via oncoPredict / GDSC (p.12–13, Results) "most drugs exhibited significant differential responses between the high and low hypoxia groups, including key agents such as gemcitabine, oxaliplatin, cisplatin, 5-Fluorouracil and paclitaxel (Fig 6D). The elevated half-maximal inhibitory concentrations (IC50) of these drugs in the high hypoxia group suggested a diminished chemotherapy efficacy" — confidence: medium — type: pharmacological — links: [[foundations/oncopredict-drug-sensitivity]] [[claims/high-hypoxia-score-chemotherapy-resistance-pdac]]
- `[c07]` High hypoxia in TCGA-PAAD associates with lower immune/stromal/ESTIMATE scores, reduced naïve B cells, and enriched M0 macrophages (p.9–10, Results) "the high hypoxia group exhibited higher tumor purity and lower immune, stromal, and ESTIMATE scores (Fig 6A) ... a reduced presence of anti-tumor immune cells such as naive B cells in the high hypoxia group, while macrophages M0 were predominantly enriched (Fig 6B)" — confidence: medium — type: correlational — links: [[foundations/estimate-stromal-immune-score]] [[foundations/cibersortx-deconvolution]] [[claims/high-hypoxia-immunosuppressive-microenvironment-pdac]]
- `[c08]` GSEA shows the high-hypoxia TCGA-PAAD group is enriched for cell cycle, DNA replication, E2F, G2M, ribosome and protein processing pathways (p.9, Results) "the high hypoxia group exhibited significant enrichment in several critical pathways, including biosynthesis of amino acids, cell cycle, DNA replication ... E2F targets, G2M checkpoint, hypoxia and mitotic spindle (Fig 5A and 5B)" — confidence: medium — type: correlational — links: [[foundations/clusterprofiler-gsea]] [[claims/high-hypoxia-cell-cycle-dna-replication-enrichment-pdac]]

## Discussion captured

### Authors' interpretation

The authors interpret the 13-gene model as: (i) a single-cell-anchored, cell-state-resolved prognostic signature that outperforms clinicopathologic features in TCGA-PAAD and validates externally on PACA-CA/-AU; (ii) a biological argument that macrophages are the PDAC immune compartment most affected by hypoxia, with macrophage cluster 1 as the canonical hypoxia-responsive subpopulation; and (iii) a hypothesis-generation engine for KRTCAP2 as a pan-cancer biomarker with immune-exclusion correlates.

### Comparisons with prior literature (made by authors)

- Earlier PDAC hypoxia prognostic models (Wu et al. 2023 Sci Rep; Wu et al. 2024 Technol Cancer Res Treat; Ren et al. 2023 World J Surg Oncol — refs 27–29) — share PLAU and similar approach but are bulk-only.
- Hypoxia-TAM crosstalk reviews (Bai 2022 Mol Cancer — ref 11) — provide the biological rationale.
- Steele 2020 Nat Cancer (ref 12, GSE155698) — supplies the scRNA-seq input.
- Prior KRTCAP2 reports in HCC (Sun 2023 — ref 37), gastric (Lee 2022 — ref 38) and uveal melanoma (Liu 2021 — ref 39).
- HIF-1α biology in PDAC (Qin 2014 Cancer Lett — ref 8, LSD1-HIF-1α glycolysis).

### Mechanistic hypotheses proposed

- Hypoxia drives macrophage polarisation and enrichment, with cluster 1 the most affected subset (Discussion, p.13).
- The 13-gene signature captures macrophage-cluster-1-specific transcriptional state in pancreatic cancer (Discussion, p.13).
- KRTCAP2 modulates the immune microenvironment across cancer types (Discussion, p.15).
- Hypoxia-driven TMB elevation may underlie part of the poor prognosis in the high-hypoxia group (p.9, "TMB is associated with poor prognosis, which may be the reason for the poor prognosis in the high hypoxia group").

### Caveats and self-criticism

- "Additional investigations into the protein expression levels of hypoxia-related genes are necessary" (p.15–16).
- "Our study lacks supporting cellular and animal experiments to confirm the regulatory mechanisms in pancreatic cancer" (p.15–16).

### Future directions suggested

- Protein-level validation of the 13 hypoxia-related genes.
- In vitro and in vivo functional experiments to confirm causal hypoxia → macrophage cluster 1 → prognostic-gene-set link.
- Wider pan-cancer functional validation of KRTCAP2.

## Limitations

- Single-cohort PDAC scRNA-seq input (GSE155698) — no replication of the macrophage cluster 1 finding in an independent PDAC scRNA-seq atlas.
- LASSO-Cox training and ROC reporting use the same TCGA-PAAD cohort; external validation uses model weights frozen at TCGA training.
- 13-gene signature includes myeloid markers (LYZ, PLAU), so the "hypoxia score" partially reads myeloid infiltration rather than pure tumour-cell hypoxia.
- All immune cell quantification is deconvolution-based (CIBERSORT LM22 / ESTIMATE); no IHC or spatial validation.
- Drug sensitivity is oncoPredict-imputed from GDSC — no measured patient response or PDO IC50.
- No functional perturbation of macrophage cluster 1 (no HIF1α / HIF2α KO experiments, no signature-gene knockdown).
- KRTCAP2 pan-cancer claims rely on TCGA bulk data + CIBERSORT, without mechanistic validation.
- No multivariable adjustment of pan-cancer claims for tumour purity or stage.

## Open questions

### Open questions raised by authors

- What protein-level expression patterns underlie the 13-gene transcriptional model?
- Is the regulatory mechanism in pancreatic cancer experimentally validated?
- How broadly does KRTCAP2 act as a therapeutic target across cancer types?

### Open questions identified during ingest

- Does macrophage cluster 1 reproduce in independent PDAC scRNA-seq atlases (Peng 2019, Chan-Seng-Yue 2020)?
- How does the 13-gene signature compare quantitatively (AUC, C-index) to Buffa-72, Winter-99 and prior PDAC hypoxia signatures on the same TCGA-PAAD cohort?
- Is the hypoxia-driven chemoresistance (gemcitabine, oxaliplatin, 5-FU, paclitaxel) measured ex vivo in PDAC PDOs from high-hypoxia patients?
- Which OST-pathway perturbation (e.g. NGI-1, KRTCAP2 knockdown) phenocopies the KRTCAP2-high → Treg/CD8 phenotype?
- Does the M0 macrophage enrichment in CIBERSORT/LM22 correspond to macrophage cluster 1 in scRNA-seq?
- Are hypoxic-niche-anchored TAMs (cluster 1) also the dominant PD-L1+ TAM source in PDAC, linking to the [[concepts/hypoxia-pd-l1-tam-immune-evasion]] axis?

## My take

This is a typical, well-executed instance of the scRNA-anchored LASSO-Cox prognostic-model genre, with a relevant thesis-adjacent setting (PDAC + hypoxia + macrophages). The single-cell anchoring gives the 13-gene signature a slightly better biological story than pure bulk models, but the validation strategy (frozen weights on PACA-CA/-AU rather than independent retraining), the lack of any functional perturbation, and the inclusion of myeloid markers like LYZ and PLAU mean the prognostic signal is plausibly a hybrid hypoxia + myeloid-infiltration score. Three things make the paper worth keeping: (i) the explicit identification of a "macrophage cluster 1" hypoxia-responsive subset in PDAC scRNA-seq that I can map to my own thinking about NF-κB+TET2 macrophage reprogramming; (ii) the KRTCAP2 / OST-complex pan-cancer biomarker thread, which is a less-explored mechanistic axis; (iii) the comprehensive TCGA-PAAD analytic battery (TMB, CIBERSORT, ESTIMATE, oncoPredict) on a hypoxia-stratified PDAC cohort, useful as a precedent for thesis analyses. Not a paper to cite for mechanism, but a useful methodological precedent and a source for KRTCAP2 follow-up.

## Related

- [[foundations/gse155698-steele-pdac-scrnaseq]] — scRNA-seq cohort
- [[foundations/tcga-paad-pancreatic-cohort]] — bulk training cohort
- [[foundations/icgc-paca-pdac-cohorts]] — external validation cohorts
- [[foundations/msigdb-hallmark-hypoxia]] — hypoxia gene set
- [[foundations/seurat-v3-integration]] — scRNA processing
- [[foundations/aucell-gene-set-activity]] — per-cell hypoxia scoring
- [[foundations/addmodulescore-seurat]] — per-cell hypoxia scoring
- [[foundations/ssgsea-single-sample-gsea]] — bulk hypoxia scoring
- [[foundations/lasso-cox-glmnet]] — signature shrinkage
- [[foundations/clusterprofiler-gsea]] — GSEA
- [[foundations/maftools-mutation-analysis]] — TMB / SNV
- [[foundations/gistic2-copy-number]] — CNV
- [[foundations/cibersortx-deconvolution]] — immune deconvolution
- [[foundations/estimate-stromal-immune-score]] — stromal / immune scoring
- [[foundations/oncopredict-drug-sensitivity]] — drug sensitivity
- [[foundations/krtcap2-gene]] — pan-cancer prognostic gene
- [[foundations/plau-urokinase]] — recurring hypoxia signature gene
- [[foundations/hif1a]] — hypoxia master regulator
- [[concepts/hypoxia-responsive-macrophage-subset-pdac]] — central biological concept
- [[concepts/scrna-derived-lasso-cox-prognostic-signature]] — methodological pattern
- [[concepts/krtcap2-pan-cancer-biomarker]] — secondary biological concept
- [[concepts/tumor-associated-macrophage-immunosuppression]] — TME context
- [[concepts/hypoxia-pd-l1-tam-immune-evasion]] — adjacent axis
- [[concepts/m1-m2-polarization-paradigm]] — TAM context
- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — review framing
- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — pan-cancer hypoxia priors
- [[papers/hypoxic-microenvironment-cancer-molecular-mechanisms-therapeutic]] — hypoxia mechanisms
- [[people/heming-ge]] — first author
- [[people/cenap-gungor]] — senior / corresponding author
