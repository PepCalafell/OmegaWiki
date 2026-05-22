---
title: "Spatial transcriptomics reveals distinct and conserved tumor core and edge architectures that predict survival and targeted therapy response"
slug: spatial-transcriptomics-reveals-distinct-conserved-tumor
arxiv: ""
doi: "10.1038/s41467-023-40271-4"
pmid: "37596273"
venue: "Nature Communications"
year: 2023
authors:
  - Rohit Arora
  - Christian Cao
  - Mehul Kumar
  - Sarthak Sinha
  - Ayan Chanda
  - Reid McNeil
  - Divya Samuel
  - Rahul K. Arora
  - T. Wayne Matthews
  - Shamir Chandarana
  - Robert Hart
  - Joseph C. Dort
  - Jeff Biernaskie
  - Paola Neri
  - Martin D. Hyrcza
  - Pinaki Bose
first_author: "Rohit Arora"
corresponding_author: "Pinaki Bose"

source_type: pdf
s2_id: "e9ff812d4ac6b6b7eaf82fa2c61aea8da0b652db"
date_added: 2026-05-22
ingested_date: 2026-05-22
ingest_version: 1
last_reviewed:

importance: 4
tier: TIER_1
tags: [spatial-transcriptomics, OSCC, leading-edge, tumor-core, pan-cancer, RNA-velocity, Dynamo, scPred, prognostic-signature]
keywords: [spatial transcriptomics, OSCC, leading edge, tumor core, scVelo, Dynamo, scPred, CellChat, SCENIC, TCGA]
domain: oncology

tissue: [oral_cavity, head_and_neck, multi]
condition: [cancer]
disease_specific: [OSCC_HPV_negative, HNSCC]
species: [human]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

techniques: [spatial_visium, scRNA-seq_10x, bulk_RNA-seq, immunofluorescence]
n_samples: 12
n_cells_total: 24876
integration_method: "Seurat SCTransform + CCA"

key_cell_types: [malignant_OSCC_cells, ecm-myCAF, detox-iCAF, intermediate_fibroblast, macrophage, cytotoxic_CD8_T, mast_cell, dendritic_cell]
key_markers: [CLDN4, SPRR1B, LAMC2, ITGA5, COL1A1, COL1A2, FN1, SPRR2D, CD24, CD44, CSTA, IGHG3, LRRC15, GJB2]
key_pathways: [keratinization, EMT, ECM_remodeling, MIF-CD74_CD44, COL1A1-SDC1, FN1-SDC1, GP6_signaling, EIF2_signaling, p38_MAPK]

projects: [thesis, skin]
priority: context
read_status: deep_read

hypoxiaverse_status:
exclusion_reason:
data_availability: "Spatial atlases at http://www.pboselab.ca/spatial_OSCC and http://www.pboselab.ca/dynamo_OSCC; HNSCC scRNA-seq reference GSE103322; OSCC validation cohort GSE41613"

code_url: ""
cited_by: []
---

## Problem
Intratumoral heterogeneity drives treatment failure and poor outcomes in solid tumors, but the spatial transcriptional architecture of the tumor microenvironment — particularly the tumor core (TC) and leading edge (LE) — remains poorly characterised. Prior IHC/ISH studies have been low-throughput; prior scRNA-seq studies lack spatial information. HPV-negative OSCC has stagnant 5-year survival (<50%) and few effective targeted therapies; a spatial framework for OSCC biology could expose new drug targets.

## Key idea
Use integrative single-cell + 10x Visium spatial transcriptomics on 12 HPV-negative OSCC samples to characterise the TC and LE as distinct transcriptional architectures, then ask whether those architectures are conserved across cancers (via an ML classifier), predict outcomes (via TCGA), and can be reversed therapeutically (via RNA velocity + Dynamo in-silico perturbation).

## Method
- **Spatial profiling**: 12 fresh-frozen HPV-negative OSCC samples (10 patients) on 10x Visium; 24,876 spots; 43,648 mean reads/spot.
- **Malignancy calling**: spots with [[foundations/card-spatial-deconvolution]] deconvolution >0.99 OR [[foundations/numbat-cnv-inference]] p_cnv >0.99, intersected with pathologist SCC annotation; 13,950 malignant + 10,852 nonmalignant spots.
- **Integration & clustering**: Seurat v4.3.0 with [[foundations/sctransform-normalization]] per sample, batch correction, Louvain clustering at resolution 1.0; phylogenetic tree (BuildClusterTree, ape) collapses 14 clusters into 3 nodal clusters annotated as TC, transitory, LE via literature HNSCC markers (CLDN4/SPRR1B for TC; LAMC2/ITGA5 for LE).
- **Pathway and regulon inference**: [[foundations/ingenuity-pathway-analysis]] for canonical pathways and upstream regulators; [[foundations/scenic-tf-regulon-inference]] for TF activity; SCPA + Seurat AddModuleScore for hallmark gene-set comparison.
- **Cell-cell communication**: [[foundations/cellchat-cell-cell-communication]] on ST spots, with ecm-myCAFs (LRRC15+, GJB2+) and detox-iCAFs (ADH1B+, GPX3+) annotated from a published HNSCC scRNA-seq reference (GSE103322).
- **Pan-cancer transfer**: [[foundations/scpred-classifier]] trained on TC/LE/transitory/other spots; applied to 30 ST samples across 17 cancer types.
- **Survival analysis**: single-sample gene-set enrichment scores on [[foundations/tcga-the-cancer-genome-atlas]] HPV-negative OSCC (n=275, TCGA) and a validation cohort (GSE41613, n=93); Cox PH across 20 TCGA pan-cancer cohorts.
- **RNA velocity & perturbation**: [[foundations/scvelo-rna-velocity]] (dynamical model) on spatially deconvolved cancer cells; [[foundations/dynamo-in-silico-perturbation]] for cell-fate transition probabilities under genetic perturbation; [[foundations/pharmacodb-drug-response]] for AAC stratification of 417 drugs across ≥25 HPV-negative HNSCC cell lines; [[foundations/dgidb-drug-gene-interactions]] for drug-gene effect annotation (140/417 retained, 70 with significant perturbations).

## Results
1. Three reproducible nodal clusters annotated as TC, transitory, LE (Fig. 2a–d). TC enriched for keratinization (SPRR2D/E/A); LE enriched for ECM (COL1A1, COL1A2, FN1) and EMT initiation (MT2A, NME2, IFITM3). Inter-patient correlation: high within TC and within LE, low between TC and LE for the same patient (Fig. 2e).
2. LE shows higher cell cycle, EMT, angiogenesis (Supp. Fig. 2n); SCENIC identifies TC TFs (EGR3, DLX5, MXI1, GRHL3, PITX1) and LE TFs (TP63, HOXB2, CREB3L1, TCF4, NFATC4).
3. CSC states are spatially organised: mCSC (CD44+) in LE; eCSC (CD24+) in TC; total CSC marker expression does not differ (Fig. 3a–d). HNSCC molecular subtypes mix within tumours; subclonal CNV lineages do not explain TC vs LE difference.
4. CellChat: TC-exclusive ANGPTL/GRN/NECTIN/EPHB; LE-exclusive CSPG4; LE-enriched ECM and inflammatory pathways. Ecm-myCAF → LE interactions exceed LE-LE and TC-TC (Supp. Fig. 3g) via COL1A1-SDC1, FN1-SDC1. LE has more neighbouring CD8+ T, ecm-myCAF, intermediate fibroblast, macrophage spots than TC (Fig. 3i).
5. scPred classifier achieves CV ROC 0.991/0.922/0.943/0.958. Applied to 30 ST samples across 17 cancers: LE identified in all 30; TC only in 15/30 (best in cSCC, COAD, CESC, melanoma). LE proportion lowest in medulloblastoma and HCC (Fig. 4d–h).
6. TCGA OSCC (n=275): high LE → worse DSS (HR 0.60, p<0.05), PFI (HR 0.67, p<0.05); high TC → better OS/DSS/PFI (HR 1.51 / 1.93 / 1.82, p<0.05). Pan-cancer (20 TCGA cohorts): LE prognostic across most cancers (exceptions: BRCA OS, LUSC DSS, SKCM/LUSC PFI). Low TC associates with high N stage, LVI, grade III, +margins, ECS; LE associates with no clinicopath covariate.
7. scVelo: TC → transitory → LE differentiation hierarchy with velocity field confidence >0.85, conserved per patient. CSTA (TC) and IGHG3 (LE) are top dynamic-splicing drivers (Fig. 6c–d).
8. Dynamo perturbation: high-AAC drugs increase outgoing-LE transition probability vs low-AAC (p<0.05) (Fig. 6h); anti-PD-1, anti-CTLA-4, Alvocidib (CDK inhibitor) recapitulate the high-AAC pattern.

## All claims (exhaustive)
- `[c01]` OSCC TC and LE are spatially distinct transcriptional compartments conserved across 12 samples / 10 patients (p.2–4) "the TC and LE are characterized by unique transcriptional profiles, neighboring cellular compositions, and ligand-receptor interactions" — confidence: high — type: mechanistic — links: [[concepts/tumor-core-vs-leading-edge-spatial-architecture]] [[claims/oscc-tc-le-spatial-architectures-conserved]]
- `[c02]` TC is enriched for keratinization genes (SPRR2D/E/A, DEFB4A, LCN2) while LE is enriched for ECM (COL1A1, FN1, COL1A2, TIMP1) and EMT initiation (MT2A, NME2, IFITM3) (p.4–5) "Top differentially expressed genes in the TC included genes involved in keratinization SPRR2E, CRCT1, SPRR2D, CNFN, and SPRR1A, while top genes in the LE included collagens (COL1A1, COL1A2), and genes involved in EMT initiation and regulation MT2A, NME2, IFITM3" — confidence: high — type: correlational — links: [[concepts/tumor-core-vs-leading-edge-spatial-architecture]] [[foundations/oscc-hpv-negative]] [[claims/tc-keratinization-le-ecm-emt-degs]]
- `[c03]` ST of 12 OSCC samples (10 patients) yields 24,876 spots, 43,648 mean reads/spot, 13,950 malignant + 10,852 nonmalignant spots after CARD/Numbat thresholding (p.2) "All 12 samples were identified to have both spatially deconvolved or CNV-inferred cancer cells based on the applied cutoff with high confidence, resulting in 13950 malignant and 10852 nonmalignant spots" — confidence: high — type: quantitative — links: [[foundations/10x-visium-spatial-transcriptomics]] [[foundations/card-spatial-deconvolution]] [[foundations/numbat-cnv-inference]] [[claims/oscc-st-12-samples-24876-spots]]
- `[c04]` TC/LE annotation rests on Louvain → 3 nodal clusters using HNSCC TC markers CLDN4/SPRR1B and LE markers LAMC2/ITGA5 (p.4) "the expression of CLDN4 and SPRR1B HNSCC TC markers, and LAMC2 and ITGA5 HNSCC LE markers corresponded to clusters 1 and 3, respectively" — confidence: high — type: methodological — links: [[foundations/sctransform-normalization]] [[claims/tc-le-louvain-annotation-cldn4-lamc2-markers]]
- `[c05]` SCENIC identifies TC TFs (EGR3, DLX5, MXI1, GRHL3, PITX1) and LE TFs (TP63, HOXB2, CREB3L1, TCF4, NFATC4) (p.5) "SCENIC analysis identified the upregulation of several proto-oncogenic TFs EGR3 and DLX5, and tumor suppressor TFs MXI1, GRHL3, and PITX1 in the TC. ... TP63 and HOXB2, and EMT regulatory genes CREB3L1, TCF4, and NFATC4 were observed in the LE" — confidence: medium — type: methodological — links: [[foundations/scenic-tf-regulon-inference]] [[claims/tc-le-scenic-tf-regulons]]
- `[c06]` LE shows significantly higher cell-cycle (p-adj<0.001), EMT (p-adj<0.05), angiogenesis (p-adj<0.001) hallmark scores than TC (p.5) "LE spots displayed higher expression of genes associated with cell cycle (p-adj < 0.001), epithelial-mesenchymal transition (EMT) (p-adj < 0.05), and angiogenesis (p-adj < 0.001)" — confidence: high — type: quantitative — links: [[claims/le-cell-cycle-emt-angiogenesis-elevated]]
- `[c07]` Mesenchymal-like CSCs (CD44+) localise to LE and epithelial-like CSCs (CD24+) localise to TC, validated by IF on serial sections (p.7) "our results corroborated the existence of higher expression of the mesenchymal-like CSC state in the LE (p < 0.001) and epithelial-like CSC state in the TC (p < 0.001) ... revealed localization of the CD24 marker at the TC, and the CD44 marker at the LE" — confidence: medium — type: mechanistic — links: [[concepts/spatially-regulated-cancer-cell-states]] [[claims/ecsc-tc-mcsc-le-cd24-cd44-localization]]
- `[c08]` CellChat shows TC-exclusive ANGPTL/GRN/NECTIN/EPHB signalling and LE-enriched ECM and inflammatory pathways (Collagen, Laminin, Tenascin, FN1, MIF, CD99, Notch) (p.7) "ANGPTL, GRN, NECTIN, and EPHB signaling pathways were exclusively seen in the TC, and CSPG4 in the LE" — confidence: medium — type: methodological — links: [[foundations/cellchat-cell-cell-communication]] [[claims/tc-le-cellchat-distinct-signaling-pathways]]
- `[c09]` Ecm-myCAFs exhibit more numerous and stronger interactions with LE cancer cells than LE-LE or TC-TC cancer signalling, via COL1A1-SDC1 and FN1-SDC1 (p.7) "ecm-myCAFs exhibited prominent cellular signaling, with many more interactions to neighboring LE cancer cells compared to TC-TC and LE-LE signaling" — confidence: medium — type: mechanistic — links: [[concepts/ecm-mycaf-leading-edge-signaling-axis]] [[claims/ecm-mycaf-strong-le-signaling-interaction]]
- `[c10]` LE spots are surrounded by significantly more cytotoxic CD8+ T (p=0.003), ecm-myCAF (p=2.2e-4), intermediate fibroblast (p=0.002) and macrophage (p=0.008) spots than TC (p.7) "significantly higher numbers of neighboring spots enriched for cytotoxic CD8(+) T cell (p-adj < 0.01), ecm.myCAF (p-adj < 0.001), intermediate fibroblast (p-adj < 0.01), and macrophage cells (p-adj < 0.01), neighboring LE spots" — confidence: high — type: correlational — links: [[claims/le-neighbored-cd8-cafs-fibroblasts-macrophages]]
- `[c11]` scPred TC/LE/transitory/other classifier achieves 10-fold CV ROC 0.991/0.922/0.943/0.958 (p.8) "Model 10-fold cross validation revealed robust performance in all models (ROC: TC = 0.991, LE = 0.922, transitory = 0.943, other remaining spots = 0.958)" — confidence: high — type: methodological — links: [[foundations/scpred-classifier]] [[claims/scpred-tc-le-classifier-high-roc]]
- `[c12]` LE transcriptional program is conserved across 30 ST samples in 17 cancers; TC programs are tissue-specific (cSCC, COAD, CESC, melanoma) (p.8) "LE-associated expression states are conserved across multiple cancer contexts, while expression profiles associated with the TC are more tissue-specific" — confidence: high — type: mechanistic — links: [[concepts/pan-cancer-conserved-leading-edge-signature]] [[claims/le-program-conserved-30-st-17-cancers]]
- `[c13]` TCGA HPV-negative OSCC (n=275): high LE → worse DSS HR 0.60 (p<0.05), PFI HR 0.67 (p<0.05); high TC → improved OS/DSS/PFI HR 1.51/1.93/1.82 (all p<0.05); replicated in GSE41613 (p.9) "High expression of the LE signature was associated with worse DSS (HR 0.60 [0.38–0.96 95% CI]; p < 0.05) and PFI (HR 0.67 [0.45–0.98 95% CI]; p < 0.05)" — confidence: high — type: correlational — links: [[concepts/pan-cancer-conserved-leading-edge-signature]] [[foundations/tcga-the-cancer-genome-atlas]] [[claims/tcga-oscc-le-worse-tc-better-survival]]
- `[c14]` Across 20 TCGA pan-cancer cohorts, high LE → worse OS in 19/20 and worse DSS in 19/20, with exceptions BRCA (OS) and LUSC (DSS) (p.9) "a high LE score was consistently associated with worse OS and DSS across multiple cancers, with the exception of breast cancer (BRCA) in OS and lung squamous cell carcinoma (LUSC) in DSS" — confidence: high — type: correlational — links: [[claims/pan-cancer-tcga-le-worse-survival-20-cancers]]
- `[c15]` Low TC score correlates with adverse clinicopath features (N stage, LVI, grade III, +margins, ECS); LE score does not significantly associate with any clinical covariate (p.9) "Lower TC signature scores were associated with higher nodal stage (p-adj < 0.05), presence of lymphovascular invasion (p-adj < 0.01), higher tumor grade (p-adj < 0.001), positive margins (p-adj < 0.05), and presence of extracapsular spread (p-adj < 0.01); while higher LE signature scores were not associated with any clinical characteristics (p-adj > 0.05)" — confidence: medium — type: correlational — links: [[claims/tc-low-clinicopath-correlates-le-independent]]
- `[c16]` scVelo dynamical model shows a TC → transitory → LE differentiation hierarchy with velocity field confidence >0.85 across spots (p.10) "we observed a differentiation hierarchy originating from TC extending towards LE ... high spot velocity vector field confidence of greater than 0.85 in all spots" — confidence: medium — type: methodological — links: [[concepts/rna-velocity-spatial-tc-to-le-differentiation]] [[foundations/scvelo-rna-velocity]] [[claims/scvelo-tc-to-le-differentiation-hierarchy]]
- `[c17]` CSTA and IGHG3 are top dynamic-splicing driver genes for TC and LE states respectively (p.10) "Top putative TC and LE state driver genes included CSTA and IGHG3 genes, respectively" — confidence: medium — type: mechanistic — links: [[claims/csta-ighg3-top-tc-le-velocity-drivers]]
- `[c18]` Dynamo in-silico perturbation across 70 PharmacoDB+DGIdb drugs shows high-AAC drugs significantly increase outgoing-LE transition probability vs low-AAC (p<0.05) (p.11) "a significant increase in the quantitative measure of net outgoing LE transition probabilities in high AAC drugs relative to low AAC drugs (p < 0.05)" — confidence: medium — type: pharmacological — links: [[concepts/in-silico-perturbation-le-state-reversal]] [[foundations/dynamo-in-silico-perturbation]] [[foundations/pharmacodb-drug-response]] [[foundations/dgidb-drug-gene-interactions]] [[claims/dynamo-effective-drugs-induce-le-state-reversal]]
- `[c19]` Anti-PD-1, anti-CTLA-4 and Alvocidib (CDK inhibitor) in-silico perturbations recapitulate the effective-drug LE-outgoing pattern (p.11) "dynamo based in-silico perturbations of common immunotherapy targets (anti-PD-1, anti-CTLA-4) displayed similar results to effective drugs (high AAC), with a predominance in outgoing LE transition signaling. ... Alvocidib ... may be a promising candidate for further research" — confidence: low — type: pharmacological — links: [[claims/anti-pd1-ctla4-alvocidib-le-outgoing-pattern]]
- `[c20]` IPA predicts LE-exclusive activation of GP6, EIF2 and HOTAIR canonical signalling and TC-specific MSP-RON-in-macrophages, IL-33, p38 MAPK signalling (p.5) "IPA predicted the activation of GP6, EIF2, and HOTAIR regulatory canonical signaling pathways exclusively in the LE across patients ... In the TC, we observed the activation of MSP-RON signaling in macrophages, IL-33, and p38 MAPK canonical signaling pathways" — confidence: medium — type: methodological — links: [[foundations/ingenuity-pathway-analysis]] [[claims/ipa-tc-le-canonical-pathways]]

## Discussion captured

### Authors' interpretation
The authors interpret the TC and LE as spatially regulated cancer cell states rather than fixed molecular subtypes or genetic lineages. They argue that the LE represents a conserved, pan-cancer invasive program associated with worse prognosis, while the TC represents a more differentiated, tissue-specific compartment with protective prognostic value. RNA velocity supports a TC → LE differentiation flow, and Dynamo perturbation reframes effective anticancer drugs as state reversers.

### Comparisons with prior literature (made by authors)
- Puram et al. 2017 HNSCC scRNA-seq (TC/LE markers, p-EMT) — partial overlap with the present DEG lists; the authors emphasise novelty of the broader ST-derived signatures.
- Galbo 2022 / Kieffer 2020 CAF taxonomy (LRRC15+ ecm-myCAFs, ADH1B+ detox-iCAFs) — adopted directly for CAF annotation.
- Liu et al. 2014 eCSC/mCSC framework — the present spatial data corroborates the CD24/CD44 polarity.
- Conventional HNSCC TCGA subtypes (Basal/Atypical/Mesenchymal/Classical) — argued to be inadequate because multiple subtypes coexist within a tumour.
- Bryne et al. and earlier IHC-based LE definitions — superseded by ST-wide LE/TC profiling.

### Mechanistic hypotheses proposed
- "The transcriptomic differences in the TC and LE are driven by the existence of spatially unique cancer cell states" (p.12).
- "Cancer cells from the TC state can transition into LE state by gradually acquiring a more aggressive EMT-like phenotype that promotes cancer invasion and dissemination" (p.13).
- "Effective anticancer drugs direct the transition from a LE-like cancer cell state to a TC-like cancer cell state" (p.13).

### Caveats and self-criticism
- TC/LE molecular states are derived from limited HPV-negative OSCC cohort; TC programs do not generalise to all cancer types.
- CSC marker abundance does not differ between TC and LE — the polarity is in CSC *state*, not CSC frequency.
- Dynamo perturbations are in-silico; underpowered drug classes were observed; outliers persist.
- LE signature is independent of standard clinicopath covariates — its prognostic value comes from a different axis but multivariate validation is not shown.

### Future directions suggested
- Mechanistic dissection of conserved invasion / metastasis features at the LE.
- Pan-cancer targeted-therapy strategies aimed at the LE state.
- Experimental validation of top in-silico hits (e.g. Alvocidib, ICB) in OSCC models.

## Limitations
- 10 unique patients, 12 samples is a modest cohort.
- Visium spot resolution (~55 µm) aggregates multiple cells.
- TC programs do not generalise across tissues of differing origin (HCC, medulloblastoma).
- All cell-cell interaction inferences are correlative.
- Dynamo perturbation findings are in-silico and unvalidated.
- LE classifier sensitivity (0.694) is the lowest among classes.
- LE score does not associate with classical clinicopath covariates — independent prognostic axis but the mechanism is unclear.

## Open questions

### Open questions raised by authors
- Which mechanisms drive the conserved features of LE biology across diverse cancers?
- Which actionable targets at the LE are clinically tractable?
- Can effective anticancer drugs be selected by in-silico LE-state reversal prospectively?

### Open questions identified during ingest
- Does LE score add information over AJCC stage in multivariate Cox models?
- Does the TC → LE flow reverse during neoadjuvant therapy in vivo?
- Are ecm-myCAF-targeting therapies (anti-LRRC15 ADCs) effective at reversing LE biology?
- How well does the scPred classifier transfer to non-Visium ST platforms (CosMx, Stereo-seq, MERFISH)?

## My take
This is one of the cleaner formalisations of "spatially regulated cancer cell states" in solid tumors, and the pan-cancer conservation of LE makes it more than an OSCC paper. The TCGA prognostic claims are strong; the Dynamo drug-perturbation framing is the most speculative but also the most actionable for follow-up. The ecm-myCAF–LE axis is particularly interesting given that LRRC15-targeting therapeutics are already in clinical development. For my thesis context (skin, hypoxia, single-cell biology), the relevance is in (i) ST analytic playbook (CARD + Numbat + Louvain + literature-marker collapse), (ii) the LE program as a candidate axis to test in cSCC and other epithelial cancers, and (iii) the cross-modality TCGA-validation pattern.

## Related
- [[foundations/10x-visium-spatial-transcriptomics]] — ST platform
- [[foundations/cellchat-cell-cell-communication]] — used for ligand-receptor inference
- [[foundations/scenic-tf-regulon-inference]] — used for TF activity
- [[foundations/tcga-the-cancer-genome-atlas]] — used for survival cohorts
- [[concepts/tumor-core-vs-leading-edge-spatial-architecture]]
- [[concepts/pan-cancer-conserved-leading-edge-signature]]
- [[concepts/spatially-regulated-cancer-cell-states]]
- [[concepts/ecm-mycaf-leading-edge-signaling-axis]]
- [[concepts/rna-velocity-spatial-tc-to-le-differentiation]]
- [[concepts/in-silico-perturbation-le-state-reversal]]
- [[papers/cellcharter-reveals-spatial-cell-niches-associated]]
- [[papers/systematic-benchmarking-computational-methods-identify-spatially]]
