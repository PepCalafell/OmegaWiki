---
# === Identification ===
title: "Interpretable inflammation landscape of circulating immune cells"
slug: "interpretable-inflammation-landscape-circulating-immune-cells"
arxiv: ""
doi: "10.1038/s41591-025-04126-3"
pmid: "41526507"
venue: "Nature Medicine"
year: 2026
authors:
  - Laura Jiménez-Gracia
  - Davide Maspero
  - Sergio Aguilar-Fernández
  - Francesco Craighero
  - Maria Boulougouri
  - Max Ruiz
  - Domenica Marchese
  - Ginevra Caratù
  - Jose Liñares-Blanco
  - Miren Berasategi
  - Ricardo O. Ramirez Flores
  - Angela Sanzo-Machuca
  - Ana M. Corraliza
  - Hoang A. Tran
  - Rachelly Normand
  - Jacquelyn Nestor
  - Yourae Hong
  - Tessa Kole
  - Petra van der Velde
  - Frederique Alleblas
  - Flaminia Pedretti
  - Adrià Aterido
  - Martin Banchero
  - German Soriano
  - Eva Román
  - Maarten van den Berge
  - Azucena Salas
  - Jose Manuel Carrascosa
  - Antonio Fernández Nebro
  - Eugeni Domènech
  - Juan D. Cañete
  - Jesús Tornero
  - Javier P. Gisbert
  - Ernest Choy
  - Giampiero Girolomoni
  - Britta Siegmund
  - Antonio Julià
  - Violeta Serra
  - Roberto Elosua
  - Sabine Tejpar
  - Silvia Vidal
  - Martijn C. Nawijn
  - Ivo Gut
  - Julio Saez-Rodriguez
  - Sara Marsal
  - Alexandra-Chloé Villani
  - Juan C. Nieto
  - Holger Heyn
first_author: "Laura Jiménez-Gracia"
corresponding_author: "Juan C. Nieto, Holger Heyn"

# === Source & metadata ===
source_type: pdf
s2_id: "b64a88b64e1acc67ba4ed8b86611e9b6197ecf74"
date_added: 2026-06-04
ingested_date: 2026-06-04
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - scRNA-seq
  - atlas
  - inflammation
  - PBMC
  - immunology
  - interpretable-ML
  - diagnostics
  - batch-effect
keywords:
  - Inflammation Atlas
  - circulating immune cells
  - PBMC single-cell
  - disease classifier
  - SHAP interpretability
  - reference mapping
domain: "immunology"

# === Biomedical domain ===
tissue:
  - blood
condition:
  - healthy
  - autoimmune
  - cancer
disease_specific:
  - SLE
  - rheumatoid_arthritis
  - psoriatic_arthritis
  - psoriasis
  - ulcerative_colitis
  - Crohns_disease
  - multiple_sclerosis
  - sepsis
  - COPD
  - asthma
  - cirrhosis
  - influenza
  - COVID-19
  - HBV
  - HIV
  - breast_cancer
  - colorectal_cancer
  - nasopharyngeal_carcinoma
  - HNSCC
species:
  - human
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques:
  - scRNA-seq_10x
n_samples: 1047
n_cells_total: 6340934
integration_method: "scANVI"

# === Biology captured ===
key_cell_types:
  - classical monocyte
  - non-classical monocyte
  - effector-memory CD8 T cell
  - naive CD4 T cell
  - non-naive CD4 T cell
  - NK cell
  - dendritic cell
  - B cell
  - ILC
  - plasma cell
key_markers:
  - STAT1
  - SP1
  - CYBA
  - IFITM1
  - GZMB
  - FGFBP2
  - STAT3
key_pathways:
  - interferon signaling
  - TNF via NFκB
  - antigen presentation
  - cytotoxicity
  - chemokine signaling

# === User project membership ===
projects:
  - thesis
  - skin
priority: context
read_status: not_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "GEO GSE248688 SuperSeries (SCGT01 GSE248689, SCGT02 GSE248695, SCGT03 GSE248685, SCGT04 GSE248693, SCGT06 GSE270165); Zenodo https://doi.org/10.5281/zenodo.14851901; CELLxGENE / 10x Genomics portals"

# === Cross-references ===
code_url: "https://github.com/Single-Cell-Genomics-Group-CNAG-CRG/Inflammation-PBMCs-Atlas"
cited_by: []
---

## Problem

Inflammation underlies nearly every disease, yet it is studied disease-by-disease, producing incompatible cell-state definitions and no global, holistic view. The authors ask whether a single integrated single-cell atlas of *circulating* immune cells across many inflammatory conditions can (1) reveal shared vs disease-specific inflammatory programs, (2) yield interpretable, batch-robust disease-discriminative genes, and (3) be turned into a patient-level diagnostic — i.e. treat blood immune cells as "living biomarkers".

## Key idea

Build the Inflammation Atlas: ~6.3M PBMCs from 1,047 patients across 19 diseases, integrated with scVI/scANVI. Characterize it three ways — (i) signature/GRN activity to find disease-driving mechanisms, (ii) interpretable machine learning (gradient-boosted trees + SHAP, with a study-classifier control) to extract disease-discriminative genes, and (iii) reference-embedding projection + per-cell-type majority voting to classify patients. A deliberately honest stress test (unseen patients vs unseen studies) exposes batch effects, not biology, as the barrier to clinical generalization, partly recovered on a centralized single-chemistry dataset.

## Method

PBMC scRNA-seq (10x 3′ and 5′) from in-house and public studies were quality-controlled and integrated with scVI then scANVI (30 latent dimensions), conditioning on diagnosis, sex and age. Cells were annotated by recursive top-down clustering into Level 1 lineages and 64 Level 2 states. Inflammatory molecules were grouped into 21 signatures, refined with Spectra into 119 cell-type-specific factors, and scored with decoupleR's univariate linear model (ULM) on scANVI-corrected pseudobulks; disease-vs-healthy effects were estimated with linear mixed-effect models. DEGs were called with edgeR quasi-likelihood on per-patient/cell-type pseudobulks (correcting chemistry, sex, age). GRN/TF activity used CollecTRI regulons (≥10 targets) with decoupleR. Disease-discriminative genes were obtained with per-cell-type XGBoost classifiers plus SHAP (d-SHAP), with a parallel study classifier (s-SHAP) to disentangle batch-confounded genes. Patient classification projected query cells into the scANVI reference, formed per-cell-type embedding pseudobulks, trained one classifier per cell type, and resolved diagnosis by majority voting, evaluated in three scenarios (cross-validation, unseen patients, unseen studies) and on a centralized dataset; scANVI was compared against Harmony/Symphony, scGen and scPoli.

## Results

- The atlas spans 6,340,934 PBMCs, 1,047 patients, 19 diseases (five groups), with 338 healthy controls; recursive clustering yields 64 immune populations.
- Most immune-relevant signatures increase across diseases vs healthy (>50%); IMIDs upregulate adhesion, TNF-via-NFκB and antigen-presentation programs, while IFN type 1/2 signatures are mostly downregulated in IMIDs except in non-naive CD8 T cells.
- FGFBP2/GZMB rise in specific effector-memory CD8 subsets (strongest in UC); STAT1 and SP1 are identified as the regulators of the IFN-induced signature, with cell-type-/disease-/flare-specific activity in SLE.
- XGBoost on scANVI-corrected expression classifies disease at BAS 0.87 / WF1 0.90 (vs 0.65/0.78 uncorrected); d-SHAP beats random genes and recovers known (STAT3, IFN genes) and novel markers (CYBA, IFITM1).
- The reference-embedding patient classifier reaches WF1 0.90 in CV and BAS 0.95 on unseen patients, but collapses on unseen studies (BAS 0.12); a centralized single-chemistry dataset recovers it (WF1 0.56), implicating batch effects; Harmony generalizes best on unseen studies.

## All claims (exhaustive)

- `[c1]` Atlas comprises ~6.3M PBMCs from 1,047 patients across 19 diseases `(p.634)` "6,340,934 after filtering, representing 1,047 patients and 19 diseases" — confidence: high — type: quantitative — links: [[claims/inflammation-atlas-comprises-million-pbmcs-1047]] [[concepts/inflammation-atlas-circulating-immune-cells]] [[foundations/scrna-seq-10x-chromium]]
- `[c2]` Generative probabilistic integration (scVI/scANVI) outperforms alternatives for annotated atlas integration `(p.634)` "Generative probabilistic models proved superior performances in integrating complex datasets compared to other approaches, particularly if cell annotations are available" — confidence: medium — type: methodological — links: [[claims/scanvi-generative-integration-outperforms-alternatives-annotated]] [[concepts/atlas-level-data-integration]] [[foundations/scvi-deep-generative-model]] [[foundations/scanvi-semi-supervised]]
- `[c3]` Recursive top-down clustering resolves 64 circulating immune populations `(p.634)` "we obtained a total of 64 immune populations (Level 2)" — confidence: high — type: methodological — links: [[claims/recursive-top-down-clustering-resolves-64]] [[concepts/inflammation-atlas-circulating-immune-cells]]
- `[c4]` Most immune-relevant signatures show increased activity across diseases vs healthy `(p.634)` ">50% increased average signature scores" — confidence: high — type: correlational — links: [[claims/most-immune-signatures-show-increased-activity]] [[foundations/spectra-factor-analysis-gene-programs]] [[foundations/decoupler-activity-inference]]
- `[c5]` IMIDs upregulate adhesion, TNF-via-NFκB and antigen-presentation signatures `(p.634)` "characteristic upregulation of adhesion molecule signatures, TNF via NFκB signaling, antigen cross-presentation and antigen-presenting signatures" — confidence: high — type: correlational — links: [[claims/imids-upregulate-adhesion-tnf-nfkb-antigen]] [[foundations/tnf-tumor-necrosis-factor]] [[foundations/nf-kb-p65-rela]]
- `[c6]` IFN type 1 and 2 signatures are downregulated in most IMIDs except non-naive CD8 T cells `(p.634)` "Interferon (IFN) type 1 and type 2 signatures were significantly downregulated in most IMIDs and cell types, except for non-naive CD8 T cells" — confidence: medium — type: correlational — links: [[claims/ifn-type-signatures-downregulated-imids-except]] [[foundations/type-interferon-ifna-ifnb]] [[foundations/ifn-gamma-cytokine]]
- `[c7]` FGFBP2 and GZMB are upregulated in effector-memory CD8 T cells in barrier IMIDs `(p.637)` "FGFBP2 and GZMB showed increased expression levels, with restriction to specific effector memory (EM) CD8 T cell subtypes … with a marked increase observed in UC" — confidence: high — type: correlational — links: [[claims/fgfbp2-gzmb-upregulated-effector-memory-cd8]] [[foundations/fgfbp2-fibroblast-growth-factor-binding-protein]] [[foundations/gzmb-granzyme]]
- `[c8]` STAT1 and SP1 are the primary transcriptional regulators of the IFN-induced signature `(p.637)` "STAT1 and SP1 were identified as the primary regulators of the IFN-induced signature" — confidence: medium — type: mechanistic — links: [[claims/stat1-sp1-primary-transcriptional-regulators-ifn]] [[foundations/stat1-tf]] [[foundations/sp1-transcription-factor]] [[foundations/collectri-tf-regulon-network]]
- `[c9]` SLE shows opposing STAT1 and SP1 activity in monocytes and non-naive CD8 T cells `(p.637)` "patients with SLE exhibited opposing STAT1 and SP1 activities in monocytes and non-naive CD8 T cells" — confidence: medium — type: correlational — links: [[claims/sle-shows-opposing-stat1-sp1-activity]] [[foundations/stat1-tf]] [[foundations/sp1-transcription-factor]]
- `[c10]` STAT1 activity rises during SLE flares while SP1 dominates myeloid cells in non-flare `(p.637)` "STAT1 activity was elevated during flares, particularly within CD8 T cells, whereas SP1 activity was more prominent in myeloid populations in the absence of flares" — confidence: medium — type: correlational — links: [[claims/stat1-activity-rises-during-sle-flares]] [[foundations/stat1-tf]] [[foundations/sp1-transcription-factor]]
- `[c11]` Gradient-boosted trees on batch-corrected expression classify disease at BAS 0.87 / WF1 0.90 `(p.637)` "achieving a balanced accuracy score (BAS) of 0.87 and a weighted F1 (WF1) score of 0.90 on held-out samples" — confidence: high — type: quantitative — links: [[claims/gradient-boosted-trees-batch-corrected-expression]] [[concepts/interpretable-ml-disease-discriminative-gene-discovery]] [[foundations/xgboost-gradient-boosting]]
- `[c12]` Batch correction (scANVI) improves disease classification over uncorrected counts `(p.637)` "uncorrected log-normalized counts led to a reduced performance … (BAS: 0.65 and WF1: 0.78)" — confidence: high — type: methodological — links: [[claims/batch-correction-improves-disease-classification-over]] [[concepts/batch-removal-vs-bioconservation-tradeoff]] [[foundations/scanvi-semi-supervised]]
- `[c13]` d-SHAP gene selection outperforms random gene sets on unseen studies `(p.637)` "On unseen studies, d-SHAP genes consistently yielded more accurate predictions" — confidence: high — type: methodological — links: [[claims/shap-gene-selection-outperforms-random-genes]] [[concepts/interpretable-ml-disease-discriminative-gene-discovery]] [[foundations/shap-feature-attribution]]
- `[c14]` A study classifier (s-SHAP) disentangles disease-specific from batch-confounded genes `(p.638)` "trained separate classifiers to predict the study identity (BAS: 0.97 … ) and to identify study-associated genes via SHAP values (s-SHAP) … allowed us to prioritize bona fide disease-discriminative genes" — confidence: medium — type: methodological — links: [[claims/study-classifier-shap-disentangles-disease-specific]] [[concepts/interpretable-ml-disease-discriminative-gene-discovery]] [[foundations/shap-feature-attribution]]
- `[c15]` CYBA discriminates intestinal from skin barrier IMIDs (high→UC/CD, low→PS/PSA) `(p.639)` "high expression of CYBA drove the model to classify intestinal inflammatory diseases (UC and CD), whereas reduced levels were relevant to classify skin-related diseases (PS and PSA)" — confidence: medium — type: mechanistic — links: [[claims/cyba-discriminative-marker-separating-intestinal-skin]] [[foundations/cyba-cytochrome-b245-light-chain]] [[foundations/inflammatory-bowel-disease]] [[foundations/psoriasis-disease]]
- `[c16]` IFITM1 discriminates COPD from asthma in lymphoid cells (high→COPD, low→asthma) `(p.639)` "higher IFITM1 expression drives the model toward classifying COPD, whereas lower expression shifts the classification toward asthma" — confidence: medium — type: correlational — links: [[claims/ifitm1-discriminates-copd-asthma-lymphoid-cells]] [[foundations/ifitm1-interferon-induced-transmembrane-protein]]
- `[c17]` Reference-embedding patient classifier reaches WF1 0.90 / BAS 0.85 in cross-validation `(p.639)` "resulting in 0.90 ± 0.03 WF1 and 0.85 ± 0.07 BAS" — confidence: high — type: quantitative — links: [[claims/reference-embedding-patient-classifier-reaches-wf1]] [[concepts/patient-classification-reference-embedding-projection]] [[concepts/scrna-atlas-as-reference-projection]]
- `[c18]` Patient classifier generalizes to unseen patients (BAS 0.95) but fails on unseen studies (BAS 0.12) `(p.639)` "Scenario 2 … BAS of 0.95 and a WF1 of 0.98. However … unseen studies (Scenario 3) resulted in a strongly decreased BAS of 0.12 and a WF1 of 0.23" — confidence: high — type: quantitative — links: [[claims/patient-classifier-generalizes-unseen-patients-fails]] [[concepts/patient-classification-reference-embedding-projection]] [[concepts/batch-removal-vs-bioconservation-tradeoff]]
- `[c19]` A centralized single-chemistry dataset restores patient-classifier generalization `(p.639)` "WF1 and BAS increased to 0.56 and 0.53 … pointing to a highly improved generalization performance … as compared to Scenario 3" — confidence: high — type: mechanistic — links: [[claims/centralized-single-chemistry-dataset-restores-patient]] [[concepts/patient-classification-reference-embedding-projection]]
- `[c20]` HIV is best classified by naive lymphoid cells, consistent with CD4 T-cell tropism `(p.639)` "HIV was best classified by naive lymphoid cells … in line with the tropism of the virus infecting mainly CD4 T cells" — confidence: medium — type: correlational — links: [[claims/hiv-best-classified-naive-lymphoid-cells]] [[foundations/hiv-virus]]
- `[c21]` Severe influenza patients molecularly resemble severe COVID-19 cases `(p.637)` "identified patients with severe Flu to closely resemble severe COVID cases … supporting common inflammatory signatures of patients suffering from these severe respiratory infections" — confidence: medium — type: correlational — links: [[claims/severe-influenza-patients-molecularly-resemble-severe]] [[foundations/influenza-virus]] [[foundations/sars-cov-2-coronavirus]]
- `[c22]` Harmony generalizes best among integration methods on unseen studies `(p.641)` "Harmony performed best with a BAS of 0.24 and a WF1 of 0.47" — confidence: medium — type: methodological — links: [[claims/harmony-generalizes-best-among-integration-methods]] [[foundations/harmony-integration]] [[foundations/symphony-reference-mapping]]

## Discussion captured

### Authors' interpretation
The authors interpret the atlas as a holistic, cross-disease map of circulating inflammation that recapitulates known disease biology and surfaces interpretable, disease-discriminative genes. They frame circulating immune cells as "living biomarkers" and propose the reference-embedding classifier as a step toward a universal liquid-biopsy diagnostic for inflammatory disease. They emphasize that the GBDT+SHAP approach yields explainable (not black-box) gene rankings, a key requirement for clinical biomarker discovery.

### Comparisons with prior literature (made by authors)
- Existing patient classifiers (scPoli, MultiMIL) evaluated settings akin to Scenarios 1–2 but not unseen studies (Scenario 3).
- scANVI selected for top performance on atlas-level integration benchmarks (scIB); compared here against Harmony/Symphony, scGen, scPoli.
- Confirm prior disease alterations: low UTC/ILC/naive CD4 and high B/monocyte in SLE; UTC/ILC reduction in IBD; sepsis lymphopenia; HIV lymphocytosis; STAT3 in RA CD4 T cells; IFN genes in SLE.
- FGFBP2/GZMB recently described in CD8 T cells at sites of epithelial damage.

### Mechanistic hypotheses proposed
- Reduced monocyte CYBA in skin IMIDs (PS/PSA) impairs immune barrier function, causing localized flares; upregulated CYBA in IBD drives ROS accumulation (p.639).
- Chronic inflammation raises lymphoid IFITM1, facilitating lymphoid-cell accumulation in COPD (p.639, validation needed).
- Circulating effector CD8 activation (FGFBP2/GZMB) may precede tissue infiltration (p.637).

### Caveats and self-criticism
- Most samples are of European ancestry; broader ancestry needed for global generalizability.
- The classifier requires prospective, independent, multicenter validation.
- The relationship between circulating and tissue-resident immune cells is unresolved and key for diagnostic translation.
- d-SHAP/s-SHAP disentanglement is limited when disease and study are collinear.

### Future directions suggested
- Generate large, single-chemistry, multi-center training datasets and define QC/best-practice standards to reduce batch effects.
- Build a foundation model from a heterogeneous, controlled atlas for a universal, batch-robust disease classifier.
- Validate that circulating molecular programs reflect tissue-resident inflammation across organs.

## Limitations
- Predominantly European-ancestry cohort.
- Cross-study generalization fails without single-chemistry centralization (batch effects dominate).
- TF/marker findings (STAT1/SP1, CYBA, IFITM1) are correlative classifier-importance/activity-inference results, not functionally validated.
- Mixed chemistries and study designs introduce nested confounders.
- Some rare cell types (plasma, UTC) classify poorly individually.

## Open questions

### Open questions raised by authors
- How faithfully do circulating immune states reflect tissue-resident inflammation?
- Can a generalizable, batch-robust universal classifier be built without single-chemistry centralization?
- What ancestry-diverse data are needed to capture global immune variability?

### Open questions identified during ingest
- Is SP1's role in the IFN-induced program causal or correlative?
- Could circulating CD8 STAT1 activity or monocyte CYBA serve as prospective flare/subtype biomarkers?
- Would a VAE with stronger regularization match Harmony's cross-study robustness?

## My take

A landmark resource that is unusually honest about its own ceiling: the Scenario-2-vs-Scenario-3 collapse and its partial recovery on a centralized dataset turn "batch effects" from a hand-wave into a quantified, isolated barrier. The transferable methodological contribution is the s-SHAP study-classifier control for batch-robust interpretable biomarker discovery, and the embedding-pseudobulk + majority-voting patient classifier. For thesis relevance, the monocyte/CYBA and skin-IMID (PS/PSA) findings and the STAT1/SP1 IFN regulation in myeloid cells connect to macrophage/monocyte inflammatory biology, even though the data are blood-restricted and correlative.

## Related
- Concepts: [[concepts/inflammation-atlas-circulating-immune-cells]] · [[concepts/circulating-immune-cells-living-biomarkers]] · [[concepts/interpretable-ml-disease-discriminative-gene-discovery]] · [[concepts/patient-classification-reference-embedding-projection]] · [[concepts/atlas-level-data-integration]] · [[concepts/batch-removal-vs-bioconservation-tradeoff]] · [[concepts/scrna-atlas-as-reference-projection]]
- Foundations: [[foundations/scrna-seq-10x-chromium]] · [[foundations/scvi-deep-generative-model]] · [[foundations/scanvi-semi-supervised]] · [[foundations/harmony-integration]] · [[foundations/symphony-reference-mapping]] · [[foundations/scgen-perturbation-integration]] · [[foundations/scpoli-prototype-reference-mapping]] · [[foundations/spectra-factor-analysis-gene-programs]] · [[foundations/decoupler-activity-inference]] · [[foundations/collectri-tf-regulon-network]] · [[foundations/edger-differential-expression]] · [[foundations/xgboost-gradient-boosting]] · [[foundations/shap-feature-attribution]] · [[foundations/scib-benchmark-pipeline]] · [[foundations/czi-cellxgene-atlas]] · [[foundations/benjamini-hochberg-fdr]] · [[foundations/stat1-tf]] · [[foundations/sp1-transcription-factor]] · [[foundations/cyba-cytochrome-b245-light-chain]] · [[foundations/ifitm1-interferon-induced-transmembrane-protein]] · [[foundations/gzmb-granzyme]] · [[foundations/fgfbp2-fibroblast-growth-factor-binding-protein]] · [[foundations/type-interferon-ifna-ifnb]] · [[foundations/ifn-gamma-cytokine]] · [[foundations/tnf-tumor-necrosis-factor]] · [[foundations/nf-kb-p65-rela]] · [[foundations/inflammatory-bowel-disease]] · [[foundations/psoriasis-disease]] · [[foundations/hiv-virus]] · [[foundations/influenza-virus]] · [[foundations/sars-cov-2-coronavirus]]
- People: [[people/laura-jimenez-gracia]] · [[people/juan-c-nieto]] · [[people/holger-heyn]] · [[people/julio-saez-rodriguez]] · [[people/alexandra-chloe-villani]]
- Builds on [[papers/benchmarking-atlas-level-data-integration-single]] — selects scANVI as the integration backbone on the strength of this scIB benchmark's atlas-integration ranking
