---
# === Identification ===
title: "NiCo identifies extrinsic drivers of cell state modulation by niche covariation analysis"
slug: nico-identifies-extrinsic-drivers-cell-state
arxiv: ""
doi: "10.1038/s41467-024-54973-w"
pmid: "39639035"
venue: "Nature Communications"
year: 2024
authors:
  - "Ankit Agrawal"
  - "Stefan Thomann"
  - "Sukanya Basu"
  - "Dominic Grün"
first_author: "Ankit Agrawal"
corresponding_author: "Dominic Grün"

# === Source & metadata ===
source_type: pdf
s2_id: "a330dd175c406437712c3044cd06a601fe89865f"
date_added: 2026-05-27
ingested_date: 2026-05-27
ingest_version: 1
last_reviewed: null

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - spatial-transcriptomics
  - scRNA-seq-integration
  - niche-analysis
  - cell-cell-interaction
  - covariation
  - non-negative-matrix-factorization
  - MERFISH
  - seqFISH
  - MERSCOPE
  - STARmap
  - Slide-seqV2
  - mouse-embryo
  - mouse-intestine
  - mouse-liver
  - Kupffer-cell
  - hepatic-stellate-cell
  - Paneth-cell
  - intestinal-stem-cell
  - TGFbeta
  - decorin
  - Wnt3
  - methods-development
keywords:
  - niche covariation analysis
  - latent factor cell state
  - integrative NMF spatial
  - logistic regression niche prediction
  - intrinsic vs extrinsic cell state
  - Tgfb1 decorin Kupffer stellate feedback
  - Paneth progenitor Wnt3 stem niche
  - hepatocyte zonation MERSCOPE
  - cell-state covariation in tissue
domain: "spatial transcriptomics / single-cell-integration / methods / developmental biology / hepatology / intestinal biology"

# === Biomedical domain ===
tissue:
  - liver
  - multi
condition:
  - healthy
disease_specific: []
species:
  - mouse
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques:
  - MERFISH
  - seqFISH
  - STARmap
  - MERSCOPE
  - Slide-seqV2
  - scRNA-seq_10x
  - smHCR
  - qPCR
  - integrative_NMF
  - logistic_regression
  - ridge_regression
n_samples: null
n_cells_total: 391679
integration_method: "iNMF (LIGER-style) / ordinary NMF + ridge regression"

# === Biology captured ===
key_cell_types:
  - Kupffer_cell
  - hepatic_stellate_cell
  - portal_vein_endothelial_cell
  - central_vein_endothelial_cell
  - portal_hepatocyte
  - mid_zonal_hepatocyte
  - central_hepatocyte
  - sinusoidal_endothelial_cell
  - cholangiocyte
  - Lgr5_intestinal_stem_cell
  - Paneth_cell
  - goblet_cell
  - enterocyte
  - cardiomyocyte
  - pharyngeal_mesoderm
  - haematoendothelial_progenitor
  - Purkinje_neuron
  - Bergmann_glial_cell
key_markers:
  - Tgfb1
  - Tgfbr3
  - Dcn
  - Bgn
  - Clec4f
  - Wnt3
  - Fzd7
  - Fzd2
  - Wnt2
  - Lgr5
  - Olfm4
  - Hopx
  - Nkx2-5
  - Isl1
  - Mef2c
  - Fgf8
  - Tnnt2
  - Tnni3
  - Myl2
  - Myl3
  - Acta2
  - Col1a1
  - Pdgfrb
  - Reln
  - Hmgb1
key_pathways:
  - TGFbeta_signaling
  - canonical_Wnt_signaling
  - hepatic_stellate_cell_activation
  - intestinal_stem_cell_self_renewal
  - second_heart_field_specification

# === User project membership ===
projects:
  - thesis
  - methods
priority: reference
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: not_included
exclusion_reason: "not hypoxia-focused — included as methods/spatial-transcriptomics reference for niche covariation framework potentially applicable to TME and hypoxic-niche analyses"
data_availability: "GitHub https://github.com/gruenlab/NiCo; MERSCOPE liver data via Vizgen; MERFISH intestine (Petukhov 2022); MERFISH PMC (Allen Brain); seqFISH E8.5 embryo (Lohoff 2022); STARmap visual cortex (Wang 2018); Slide-seqV2 cerebellum (Stickels 2021)"

# === Cross-references ===
code_url: "https://github.com/gruenlab/NiCo"
cited_by: []
---

## Problem

Cell state within a tissue is shaped by both intrinsic (transcriptional bursting, gene-regulatory-network stochasticity) and extrinsic (cell-cell communication, biomechanical and metabolic cues) determinants, but conventional scRNA-seq cannot separate the two because it loses spatial context. Existing computational methods for spatial transcriptomics target tissue-domain detection (Stagate, CellCharter, SpaGCN, Banksy, SpatialPCA), spatially variable genes (SpatialDE), ligand-receptor flux (COMMOT, SpaOTsc), or local gene-gene dependencies (MISTy, GCNG, NCEM). None of them directly answers the mechanistic question "how does the internal state of cell A depend on which cell B sits next to it?" Imaging-based spatial transcriptomics (MERFISH, seqFISH, MERSCOPE, Xenium, CosMx, STARmap) provides the single-cell, single-molecule resolution needed to attack this question — but typically only profiles a few hundred genes, so transcriptome-wide interpretation requires integration with scRNA-seq.

## Key idea

NiCo is a Python framework that links imaging-based single-cell-resolution spatial transcriptomics to scRNA-seq references through three sequential modules: (1) **Annotations** — soft mutual-nearest-neighbor anchors, Leiden-pruned, then kNN-propagated to non-anchors, transferring cell-type labels from scRNA-seq into the spatial modality; (2) **Interactions** — per-central-cell-type regularized logistic regression on local cell-type-frequency vectors, exposing which neighbors are most predictive of the central cell's identity; (3) **Covariations** — integrative or ordinary NMF on the shared gene set produces K=3 latent factors per cell type, after which ridge regression of each central-cell factor on neighbor-cell factors detects positive and negative cell-state covariation across co-localized pairs. The scRNA-seq reference makes the latent factors interpretable transcriptome-wide via Spearman correlation, and ligand-receptor pairs co-correlating with covarying factors are proposed as candidate signaling mediators. NiCo deliberately does not bake in a ligand-receptor catalog as a constraint, so predicted covariations can also reflect biomechanical or metabolic crosstalk. See [[concepts/niche-covariation-analysis]], [[concepts/intrinsic-vs-extrinsic-cell-state-determinants]], [[concepts/niche-composition-predicts-cell-type-identity]], and the tool itself at [[foundations/nico-niche-covariation-tool]].

## Method

**Inputs**: imaging-based spatial cell-by-gene matrix + 2D cell-center coordinates (after segmentation) + matched scRNA-seq cell-by-gene matrix + cell-type labels.

**Module 1 — Annotations**: normalize both modalities; identify soft mutual nearest neighbors in shared-gene space as anchors; prune scattered anchors using Leiden clusters of the spatial modality; iteratively annotate non-anchors by majority vote across kNN anchors.

**Module 2 — Interactions**: per central cell type CC, count neighbor cell types within radius R (default R=0, juxtacrine); train an L2-regularized logistic regression with CC vs not-CC labels; classifier coefficients β(CC, NC, R) rank niche partners by signed contribution; confusion matrix surfaces cell types with similar niches. Five-fold cross-validation for error bars.

**Module 3 — Covariations**: per cell type, fit either iNMF on the shared gene set across spatial + scRNA-seq (when segmentation is clean) or ordinary NMF on scRNA-seq only with cell loadings transferred to spatial (when spillover dominates). K = 3 latent factors per cell type. Then for each (CC, NC) niche pair from Module 2, ridge regression of each h^CC_i on all h^NC_j on the set of co-localized pairs; significant signed regression coefficients indicate factor covariation; multivariate p-values from two-tailed t-statistics.

**Downstream interpretation**: top positively/negatively correlating genes per factor are computed from the scRNA-seq modality (genome-wide); pathway enrichment via ReactomePA / EnrichR-style sets; ligand-receptor co-correlation with factors flags candidate signaling mediators.

**Validation experiments (liver)**:
- smHCR for Tgfb1, Dcn, Clec4f on healthy mouse liver tissue → spatial validation of predicted Tgfb1–Dcn covariation in Kupffer–stellate pairs.
- qPCR on cultured primary mouse HSCs ± Tgf-β ± Dcn → in vitro validation of Dcn-dampened HSC activation.

**Benchmark datasets**:
- Mouse small-intestine MERFISH (Petukhov 2022).
- Mouse primary motor cortex MERFISH (Vizgen).
- Mouse E8.5 embryo seqFISH (Lohoff 2022).
- Mouse liver MERSCOPE (Vizgen, 391,679 cells, 347 genes).
- Mouse visual cortex STARmap (Wang 2018).
- Mouse cerebellum Slide-seqV2 (Stickels 2021).
- Allen brain MERFISH atlas (Yao 2023).
- Simulated 2D tissues with Lennard-Jones interaction potentials (6 cell types, 200 cells each).

## Results

### 1. Annotation benchmark (Fig. 2a–b, Supplementary Fig. 1a)
- NiCo outperforms Tangram and uniPort on all three benchmark datasets (intestine, PMC, embryo) by both ARI and Jaccard similarity.
- NiCo matches or exceeds TACCO on PMC and embryo (lower ARI on intestine, higher Jaccard).
- cell2location higher overlap on intestine; comparable on PMC; NiCo more consistent on embryo.
- On the MERSCOPE liver dataset (391,679 cells), NiCo finishes annotation in <3 hours on a 16-core CPU; cell2location takes >2 days; SpaGCN aborts due to memory exhaustion.

### 2. Simulated interaction recovery (Fig. 2c–f)
- Lennard-Jones 2D simulations with 6 cell types and varying ε pairwise potentials.
- NiCo's regression coefficients match the simulated interaction-strength ranking in both juxtacrine (R=0) and paraview (R=5) settings.
- MISTy recovers some but not all rankings; importance scores are unsigned, complicating sign attribution; misses Wnt2–Fzd2-like best-predictor relationships in some scenarios.

### 3. Tissue-domain detection benchmark (Fig. 2g–h, Supplementary Fig. 2–3)
- On Allen brain MERFISH (6 ground-truth domains, 17 cell types), NiCo interaction coefficients correlate with ground-truth domain cell-type enrichment more consistently than CellCharter, SpaGCN, Stagate, Banksy, SpatialPCA, Seurat BuildNicheAssay.
- On STARmap visual cortex, NiCo comparable to peer methods.
- NiCo does not require pre-specified cluster number or resolution parameters.

### 4. E8.5 mouse embryo seqFISH (Fig. 3)
- Niche-prediction precision (weighted avg) = 0.71.
- Cell-type interaction map (Fig. 3e) recovers ExE endoderm → definitive endoderm → gut; endothelium → haematoendothelium → blood progenitors.
- Cardiomyocyte Fa2 ↔ pharyngeal mesoderm Fa1 covariation (log10P = −3.92, 223 pairs out of 853 PM / 773 CM).
- Mature cardiac markers (Tnnt2, Tnni3, Tnnc1, Myl2/3, Acta) anti-correlated with cardiomyocyte Fa2.
- SHF progenitor markers (Nkx2-5, Isl1, Mef2c, Fgf8) anti-correlated with pharyngeal mesoderm Fa1.
- Wnt2 (cardiomyocyte) — Fzd2 (pharyngeal mesoderm) and Hmgb1 ligand predicted as candidate mediators of cardiac maturation by SHF-derived progenitors.

### 5. Mouse small-intestine MERFISH (Fig. 4)
- Stem/TA and Paneth cells localize to crypt bottom; enterocyte zonation (bottom/mid/top) recovered.
- Stem/TA cell predicted by Paneth and goblet neighbors; Paneth predicted by Paneth + stem/TA neighbors.
- Stem/TA Fa1 ↔ goblet Fa2 covariation (log10P = −4.00).
- Stem/TA Fa1 ↔ Paneth Fa1 covariation (log10P = −1.43, 217 co-localized pairs out of 1107 stem/TA / 184 Paneth).
- Stem/TA Fa1 top-correlated genes: Olfm4, Lgr5, Hopx (stem markers).
- Paneth Fa1 top-correlated genes: Paneth-cell-progenitor markers, not mature Paneth markers.
- Wnt3 (Paneth) — Fzd7/Fzd2 (stem/TA) ligand-receptor pair predicted; Wnt3 trajectory downregulates during Paneth maturation in Böttcher 2021 reference, supporting the Paneth-progenitor-as-Wnt-source model.
- Niche-DE, COMMOT, stLearn, CellNeighborEX miss this Wnt3–Fzd7 interaction because Wnt3 is not in the spatial gene panel.

### 6. Mouse liver MERSCOPE (Fig. 5–6, Supplementary Fig. 7–10)
- 375,161 / 391,679 (95.8%) cells annotated.
- Hepatocyte zones (portal / mid / central) co-localize correctly with portal / mid / central-vein endothelial cells.
- cell2location and TACCO partially resolve hepatocyte zones; Tangram and uniPort do not.
- Niche-prediction graph: portal module (portal-vein EC, lymphatic EC, cholangiocytes, portal hepatocytes) and mid/central module (mid/central hepatocytes, central-vein EC, sinusoidal EC); fibroblasts bridge both.
- Stellate cell prediction accuracy = 0.06 (niche-promiscuous) but coefficients identify sinusoidal EC, Kupffer cells, central/mid hepatocytes as positive niche partners — matches Dobie 2019.
- Stellate Fa2 ↔ Kupffer Fa1 covariation (log10P = −3.08, 7781 pairs out of 11,881 stellate / 38,932 Kupffer).
- Top stellate genes: viral defense, antigen presentation, proteoglycans Dcn, Bgn.
- Top Kupffer genes: antigen presentation, complement activation — activated KC state.
- Tgfb1 (KC) — Tgfbr3 (HSC) ligand-receptor pair predicted.
- Replicate slice and 22.7% subsample preserve the prediction.

### 7. smHCR validation in healthy mouse liver (Fig. 6f–g)
- Tgfb1 (KC) – Dcn (HSC) co-localized-pair Pearson r = 0.59.
- Clec4f – Dcn co-localized-pair Pearson r = 0.24 (baseline).
- Specificity of Tgfb1–Dcn covariation confirmed.

### 8. In vitro Dcn–HSC qPCR (Fig. 6h, Supplementary Fig. 10f)
- HSC + Tgf-β + Dcn vs HSC + Tgf-β: Col1a1 P < 0.01, Pdgfrb P < 0.04 reduced.
- Quiescent marker Reln unaffected.
- Lox and Acta2 trend reduction, not significant.

### 9. Cerebellum Slide-seqV2 (Supplementary Fig. 11)
- Recovers Purkinje–Bergmann-glia interaction.
- Detects calcium-signaling covariation from Bergmann glia to Purkinje neurons.

## All claims (exhaustive)

- `[c01]` NiCo's three-module pipeline (annotations + interactions + covariations) integrates imaging-based single-cell-resolution spatial transcriptomics with scRNA-seq references to infer extrinsic drivers of cell state (p.2, Fig. 1) "we developed NiCo with the goal to infer Niche Covariation of gene expression programs at cell type resolution on a transcriptome-wide scale by integrating imaging-based spatial transcriptomics with matched scRNA-seq reference data" — confidence: high — type: methodological — links: [[concepts/niche-covariation-analysis]] [[foundations/nico-niche-covariation-tool]] [[claims/nico-three-module-pipeline-spatial-scrna]]
- `[c02]` NiCo outperforms Tangram and uniPort and matches or exceeds TACCO and cell2location in cell-type annotation accuracy across mouse intestine MERFISH, primary motor cortex MERFISH, and mouse embryo seqFISH (p.4, Fig. 2a) "NiCo outperformed Tangram and uniPort on all three datasets and exhibited higher ground truth consistency on Primary Motor cortex and the embryo data than TACCO" — confidence: high — type: methodological — links: [[foundations/nico-niche-covariation-tool]] [[foundations/tangram-spatial-mapping]] [[foundations/cell2location-deconvolution]] [[claims/nico-outperforms-tangram-uniport-annotation-benchmark]]
- `[c03]` NiCo annotates 391,679 MERSCOPE liver cells in <3 hours on a 16-core workstation, whereas cell2location takes >2 days on the same data and SpaGCN aborts due to memory exhaustion (p.5, Fig. 2b) "on large datasets such as the MERSCOPE liver dataset with ~400k cells, cell2location took more than two days to run, while NiCo finished in less than three hours on an AMD Ryzen 9, 5950X, 16-core processor with 128 GiB memory" — confidence: high — type: quantitative — links: [[foundations/nico-niche-covariation-tool]] [[foundations/cell2location-deconvolution]] [[claims/nico-scales-merscope-liver-400k-cells-3-hours]]
- `[c04]` Regularized logistic regression on cell-type frequencies in local neighborhoods recovers ground-truth interaction strengths in Lennard-Jones-simulated tissues for both juxtacrine (R=0) and paraview (R=5) settings; MISTy's random-forest importance is unsigned and less consistent (p.5, Fig. 2c–f) "Magnitude and signs of the regression coefficients were consistent with the simulated interactions, confirming NiCo's capability for niche prediction. ... NiCo's predictions were more consistent with the ranking by simulated interaction strengths" — confidence: high — type: methodological — links: [[concepts/niche-composition-predicts-cell-type-identity]] [[foundations/misty-spatial-omics]] [[claims/logistic-regression-niche-composition-recovers-simulated-interactions]]
- `[c05]` NiCo's per-cell-type interaction coefficients correlate with ground-truth tissue-domain cell-type enrichment more consistently than CellCharter, SpaGCN, Stagate, Banksy, SpatialPCA, and Seurat BuildNicheAssay on Allen brain MERFISH atlas (p.5, Fig. 2g) "the interactions predicted by NiCo were on average more consistent with ground truths domain annotations than the domain predictions obtained from available methods" — confidence: medium — type: methodological — links: [[concepts/niche-composition-predicts-cell-type-identity]] [[foundations/cellcharter-framework]] [[foundations/stagate-graph-attention-autoencoder]] [[claims/nico-interaction-coefficients-recover-allen-brain-merfish-domains]]
- `[c06]` In E8.5 mouse embryo seqFISH, NiCo's niche classifier predicts cell-type identity from neighborhood composition with weighted-average precision 0.71 (p.6, Fig. 3c) "The majority of cell types in the E8.5 embryo were predicted well from their niche composition (Fig. 3c) with a weighted average precision of 0.71" — confidence: high — type: quantitative — links: [[foundations/seqfish-imaging-spatial]] [[claims/e85-embryo-niche-prediction-precision-071]]
- `[c07]` Cardiomyocyte Fa2 significantly covaries with pharyngeal-mesoderm Fa1 (log10P = −3.92, 223 co-localized pairs out of 853 PM / 773 CM) in E8.5 mouse embryo; mature cardiac markers (Tnnt2, Tnni3, Myl2/3, Acta) anti-correlated with cardiomyocyte Fa2 and SHF progenitor markers (Nkx2-5, Isl1, Mef2c, Fgf8) anti-correlated with pharyngeal mesoderm Fa1 (p.8, Fig. 3f–g) "Another significant covariation (log10P = −3.92) was detected between cardiomyocyte factor (Fa) 2 and pharyngeal mesoderm Fa1, supported by 223 co-localized pairs out of 853 pharyngeal mesoderm cells and 773 cardiomyocytes" — confidence: medium — type: correlational — links: [[foundations/nkx2-5-tf]] [[foundations/tbx5-tf]] [[claims/cardiomyocyte-pharyngeal-mesoderm-covariation-shf-axis]]
- `[c08]` Wnt2 (cardiomyocyte) — Fzd2 (pharyngeal mesoderm) is the predicted ligand-receptor pair underlying cardiomyocyte–pharyngeal-mesoderm covariation, consistent with WNT-dependence of SHF progenitor proliferation and differentiation (p.8, Fig. 3h) "we identified a potential interaction between Wnt2 on cardiomyocytes and Fzd2 on pharyngeal mesodermal cells, consistent with the known requirement of WNT signaling for SHF progenitor proliferation and differentiation from pharyngeal mesoderm" — confidence: medium — type: mechanistic — links: [[claims/wnt2-fzd2-cardiomyocyte-pharyngeal-mesoderm-ligand-receptor]]
- `[c09]` In mouse small-intestine MERFISH, stem/TA cell Fa1 (Olfm4/Lgr5/Hopx) significantly covaries with Paneth Fa1 (progenitor markers; log10P = −1.43, 217 co-localized pairs out of 1107 stem/TA / 184 Paneth) and goblet Fa2 (log10P = −4.00) (p.9, Fig. 4f–g) "NiCo's covariation module inferred a significant covariation of stem/TA cell Fa1 with goblet cell Fa2 (log10P = −4.00) and Paneth cell Fa1 (log10P = −1.43) supported by 217 co-localized pairs out of 1107 stem/TA cells and 184 Paneth cells" — confidence: high — type: correlational — links: [[foundations/lgr5-intestinal-stem-cells]] [[foundations/paneth-cells]] [[claims/stem-ta-paneth-covariation-mouse-intestine-merfish]]
- `[c10]` Wnt3 (Paneth) — Fzd7 (stem/TA) is the predicted ligand-receptor pair mediating the intestinal stem-cell niche, with Wnt3 downregulating during Paneth maturation — implicating nascent Paneth progenitors, not mature Paneth cells, as the dominant Wnt-source (p.9, Fig. 4h–i) "Interrogation of ligand-receptor pairs correlated to the covarying factors recovered the Wnt3 ligand correlating to Paneth cell Fa1 and Fzd2 as well as Fzd7 receptors correlating to stem/TA cell Fa1. ... Wnt3 is downregulated during Paneth cell maturation following the trend of Fa1" — confidence: medium — type: mechanistic — links: [[concepts/paneth-progenitor-wnt3-stem-niche]] [[foundations/wnt3-ligand]] [[foundations/fzd7-receptor]] [[claims/wnt3-fzd7-paneth-stem-niche-progenitor-source]]
- `[c11]` In mouse liver MERSCOPE, stellate cell Fa2 significantly covaries with Kupffer cell Fa1 (log10P = −3.08, 7,781 co-localized pairs out of 11,881 stellate and 38,932 Kupffer cells) (p.11, Fig. 6a) "The most significant covariation (log10P = −3.08) was inferred between stellate cell Fa2 and Kupffer cell Fa1, supported by 7781 co-localized pairs out of 11,881 stellate cells and 38,932 Kupffer cells" — confidence: high — type: correlational — links: [[foundations/kupffer-cells]] [[foundations/hepatic-stellate-cells]] [[foundations/merscope-vizgen]] [[claims/stellate-kupffer-covariation-mouse-liver-merscope]]
- `[c12]` Predicted Tgfb1 (Kupffer) — Tgfbr3 (stellate) ligand-receptor pair, accompanied by stellate-side upregulation of antifibrotic proteoglycans Dcn and Bgn, mediates the Kupffer–stellate covariation in mouse liver (p.11, Fig. 6b–c) "Focusing on ligand-receptor pairs correlated with the covarying factors, we detected the ligand Tgfb1 on Kupffer cells and the receptor Tgfbr3 on stellate cells. ... proteoglycans such as Dcn and Bgn were among the top correlating genes" — confidence: high — type: mechanistic — links: [[concepts/kupffer-stellate-tgfb-decorin-feedback]] [[foundations/tgfb1-cytokine]] [[foundations/dcn-decorin]] [[claims/tgfb1-tgfbr3-kupffer-stellate-ligand-receptor]]
- `[c13]` smHCR independently validates the Tgfb1–Dcn covariation: Pearson r = 0.59 in co-localized stellate–Kupffer pairs vs r = 0.24 for the Clec4f–Dcn baseline (p.13, Fig. 6f–g) "this highly sensitive assay confirmed a strong correlation (Pearson's correlation coefficient r = 0.59) between Tgfb1 and Dcn in co-localized pairs of stellate and Kupffer cells within healthy liver tissue ... correlation of Dcn in stellate cells with the general marker Clec4f in co-localized Kupffer cells was markedly reduced (Pearson's correlation coefficient r = 0.24)" — confidence: high — type: quantitative — links: [[concepts/kupffer-stellate-tgfb-decorin-feedback]] [[foundations/smhcr-hybridization-chain-reaction]] [[claims/smhcr-validates-tgfb1-kc-dcn-hsc-coexpression-r059]]
- `[c14]` In vitro co-administration of Dcn with Tgf-β significantly dampens Col1a1 (P<0.01) and Pdgfrb (P<0.04) activation-marker induction in cultured hepatic stellate cells, while quiescent marker Reln is unaffected (p.13, Fig. 6h) "HSC stimulation by Tgf-b in the presence of Dcn led to significantly lower induction of activation markers Col1a1 (P < 0.01) and Pdgfrb (P < 0.04), while the quiescent HSC marker gene Reln remained unaffected" — confidence: high — type: pharmacological — links: [[concepts/kupffer-stellate-tgfb-decorin-feedback]] [[foundations/dcn-decorin]] [[claims/dcn-dampens-tgfb-induced-hsc-activation-qpcr]]
- `[c15]` NiCo annotates 375,161/391,679 (95.8%) cells in MERSCOPE mouse liver and resolves portal/mid/central hepatocyte zonation in correct spatial juxtaposition to portal/mid/central-vein endothelial cells, where cell2location/Tangram/TACCO/uniPort show weaker hepatocyte-zone separation (p.10, Fig. 5a–c, Suppl. Fig. 7) "NiCo could annotate 375,161 out of 391,679 cells (95.8%) in the spatial modality ... A comparison with alternative state-of-the-art annotation tools such as cell2location, Tangram, TACCO and uniPort revealed that these methods struggle with the recovery of zonated hepatocyte states" — confidence: high — type: methodological — links: [[foundations/merscope-vizgen]] [[foundations/nico-niche-covariation-tool]] [[claims/nico-recovers-zonated-hepatocyte-states-merscope]]
- `[c16]` NiCo's liver cell-type interactions and the stellate–Kupffer niche prediction are preserved on a second MERSCOPE slice (technical replicate) and on a 22.7%-subsampled region (88,772 cells) (p.10, Suppl. Fig. 8–9) "Running NiCo on a second liver slice analyzed with MERSCOPE recovers liver cell type interactions in general, and the stellate cell-Kupffer cell niche composition in particular ... we repeated the analysis on a smaller sub-region containing only 88,772 (22.7%) cells. Again, NiCo recovered liver cell type interactions and the stellate-Kupffer cell niche" — confidence: high — type: methodological — links: [[foundations/nico-niche-covariation-tool]] [[claims/nico-niche-prediction-robust-to-replicate-and-sample-size]]
- `[c17]` Stellate cells in MERSCOPE liver have low niche-classification accuracy (0.06) — they are niche-promiscuous — yet the signed regression coefficients still identify sinusoidal EC, Kupffer cells, and central/mid hepatocytes as positive niche partners (matches Dobie 2019), showing that low per-class accuracy does not preclude biologically meaningful niche inference (p.11, Fig. 5e) "we focused on the stellate cell niche, which exhibited a classification accuracy of 0.06. Nonetheless, the logistic regression classifier suggested specific positive associations with sinusoidal endothelial cells, Kupffer cells, and central/mid-zonal hepatocytes ... This niche composition aligns perfectly with a recent characterization of the stellate cell niche" — confidence: medium — type: methodological — links: [[concepts/niche-composition-predicts-cell-type-identity]] [[foundations/hepatic-stellate-cells]] [[claims/stellate-niche-prediction-low-accuracy-coefficients-still-informative]]
- `[c18]` NiCo applied to Slide-seqV2 mouse cerebellum (10 µm pixels) recovers the Purkinje–Bergmann glial interaction and detects covarying calcium-signaling secretory programs from Bergmann glia to Purkinje neurons, demonstrating generalizability to sequencing-based spatial transcriptomics when per-pixel cell-type annotations are available (p.14, Suppl. Fig. 11) "we evaluated its capabilities on a mouse cerebellum dataset generated with Slide-seqV2 ... NiCo's interaction module recovered well known interactions, e.g., between Purkinje neurons and a specialized form of astrocytes called Bergmann glial cells ... Covariation analysis ... recovered covarying secretory programs, e.g., calcium signaling from Bergmann cells to Purkinje neurons" — confidence: medium — type: methodological — links: [[foundations/nico-niche-covariation-tool]] [[claims/nico-applicable-slide-seqv2-cerebellum-purkinje-bergmann]]

## Discussion captured

### Authors' interpretation

The authors frame NiCo as filling a methodological gap: existing tools either describe tissue domains, identify spatially variable genes, or score predefined ligand-receptor interactions, but none model cell-state coupling across pairs of co-localized cell types. By inferring small per-cell-type latent factor sets and regressing factors across co-localized pairs, NiCo turns spatial transcriptomics into a tool for mechanistic hypothesis generation about cell-cell crosstalk. The liver Kupffer–stellate finding is the showcase: from a fully data-driven covariation prediction, the authors derive a homeostatic-feedback hypothesis (Tgfb1 → Dcn → Tgfb1 sequestration) that they then validate orthogonally (smHCR + qPCR), showing the value of mechanistic generation even when the spatial panel doesn't measure the inferred genes directly.

### Comparisons with prior literature (made by authors)

- **SpatialDE (Svensson 2018)** — spatially variable gene detection; complementary to NiCo's per-cell-type factor approach.
- **SpaOTsc (Cang 2020), COMMOT (Cang 2023)** — optimal-transport ligand-receptor inference; cannot infer cell-state covariation across cell types.
- **MISTy (Tanevski 2022)** — closest methodological peer for interaction inference; benchmarked head-to-head in Fig. 2f.
- **GCNG (Yuan 2020)** — local gene-gene dependencies; gene-level not cell-type-level.
- **NCEM (Fischer 2023)** — niche-driven intra-cell-type variance; complementary, gene-level, not cross-cell-type.
- **cell2location (Kleshchevnikov 2022); Tangram (Biancalani 2021); TACCO (Mages 2023); uniPort (Cao 2022)** — annotation peers; benchmarked in Fig. 2a–b.
- **Stagate (Dong 2022); CellCharter (Varrone 2024); SpaGCN (Hu 2021); SpatialPCA (Shang 2024); Banksy (Singhal 2024); Seurat BuildNicheAssay (Hao 2024)** — tissue-domain detection peers; benchmarked in Fig. 2g–h.
- **Lohoff 2022** — E8.5 embryo seqFISH source.
- **Petukhov 2022** — intestine MERFISH source.
- **Yao 2023; Zhang 2023** — Allen brain MERFISH atlas + ground-truth domains.
- **Wang 2018** — STARmap visual cortex source.
- **Stickels 2021** — Slide-seqV2 cerebellum source.
- **Böttcher 2021** — direct Paneth-from-stem differentiation; used to interpret the Paneth-Fa1-as-progenitor finding.
- **Flanagan 2015** — Fzd7 as the Lgr5+ stem-cell Wnt3 receptor; supports the Wnt3–Fzd7 prediction.
- **Dobie 2019** — hepatic stellate cell niche characterization; matches NiCo's niche-coefficient prediction.
- **Cohen 2007** — WNT signaling required for SHF progenitor proliferation; supports Wnt2–Fzd2 prediction.

### Mechanistic hypotheses proposed

- **Liver homeostatic feedback (Fig. 6, p.13)**: "Sensing of low levels of viruses and other pathogens may lead to activation of Kupffer cells and induction of Tgf-β signaling, which is received by interacting stellate cells. In stellate cells, this signal could induce proteoglycans which sequester Tgf-β ligands to dampen pro-fibrogenic signaling in order to avoid stellate cell activation at low pathogen levels in the healthy liver. Upon chronic stimulation, this mechanism may be insufficient to inhibit Tgf-β signaling surpassing a critical threshold, and thus leading to full stellate cells activation and collagen production."
- **Intestinal niche (Fig. 4, p.9)**: nascent Paneth-cell progenitors emerging directly from stem cells signal Wnt3 back to sister stem cells to maintain stemness — a sibling-loop niche.
- **Cardiac maturation (Fig. 3, p.8)**: pharyngeal mesoderm — likely SHF progenitors based on Isl1/Mef2c/Fgf8 expression — drive co-localized cardiomyocyte maturation via Wnt2/Hmgb1 signaling.

### Caveats and self-criticism

- Predicted covariations may result from indirect sources (biomechanical adaptation, metabolic competition) rather than direct signaling.
- The authors deliberately do not constrain inference by a ligand-receptor catalog; this means signaling-mediator predictions are post-hoc and may miss the true mediator.
- Sequencing-based spatial transcriptomics (Slide-seqV2 included) confounds covariation inference because pixels aggregate multiple cells.

### Future directions suggested

- Application to spatial transcriptomics in disease states (cancer, fibrosis, chronic inflammation).
- Direct extension to genome-wide spatial transcriptomics (full-transcriptome imaging) without requiring scRNA-seq reference.
- Time-resolved spatial data to disentangle directionality of cell-state covariation.

## Limitations

- Requires single-cell segmentation; not applicable to low-resolution sequencing-based spatial transcriptomics (only partially applicable to Slide-seqV2 with per-pixel annotations).
- Latent-factor count K=3 is a heuristic; sensitivity to K not systematically explored.
- Signaling-mediator predictions are based on ligand-receptor co-correlation with factors, not causal perturbation.
- Mouse-only; no human-tissue validation in this paper.
- Liver validation rests on a single MERSCOPE dataset + smHCR + in vitro qPCR; no in vivo perturbation (Dcn KO, KC-specific Tgfb1 KO).
- E8.5 cardiac maturation finding is correlational; no perturbation in this paper.

## Open questions

### Open questions raised by authors

- Whether predicted covariations can be experimentally validated as direct signaling vs biomechanical/metabolic crosstalk.
- How well NiCo generalizes to full-transcriptome spatial imaging without scRNA-seq reference.
- Whether NiCo can be extended to time-resolved spatial transcriptomics to capture directionality.

### Open questions identified during ingest

- In vivo causal validation of the Tgfb1–Dcn loop (e.g. HSC-specific Dcn KO or KC-specific Tgfb1 KO with stellate-activation readout).
- Whether the Tgfb1–Dcn loop modulates MASH/NASH progression — a falsifiable prediction.
- Lineage-tracing of Wnt3-bright nascent Paneth progenitors to test the "sibling-loop niche" model.
- Sensitivity of NiCo's factor decomposition to K and to NMF initialization.
- Whether NiCo applied to TME imaging-based spatial transcriptomics recovers macrophage–cancer-cell or macrophage–stromal-cell niche covariation patterns relevant to hypoxia biology.
- Extension to multi-slice 3D spatial data with proper cell-cell-pair handling across z-stacks.
- Whether iNMF vs ordinary-NMF mode selection can be automated rather than user-specified.

## My take

The methodological contribution is real and well-targeted: NiCo asks a question — "does the state of A depend on which B sits next to it?" — that previous spatial-transcriptomics tools either ignore or answer indirectly. The latent-factor regression on co-localized pairs is the right architectural choice given typical 200–500-gene spatial panels.

Three results are convincing rather than decorative:

1. **Tgfb1–Dcn homeostatic feedback in liver**: a fully data-driven prediction validated by an orthogonal RNA-FISH assay AND an in vitro pharmacological test. This is the strongest single demonstration that NiCo-style covariation analysis can generate testable mechanistic hypotheses about cell-cell signaling that the spatial panel itself never measured.
2. **Paneth-progenitor Wnt3 source**: a non-obvious refinement of the textbook stem-cell-niche model, showing that the *progenitor* state of the niche cell — not the mature state — supplies the niche signal. Worth tracking as a general motif of asymmetric stem-cell maintenance.
3. **Recovery of zonated hepatocyte states in MERSCOPE liver where cell2location/Tangram struggle**: a real annotation advantage, not just a benchmark-shopping win.

Weaknesses to flag for any future use:
- The Wnt2–Fzd2 cardiac and Wnt3–Fzd7 intestinal predictions are not orthogonally validated in this paper; only the liver finding is. Treat non-liver mechanistic claims as hypothesis-generating, not confirmed.
- The covariation framework cannot distinguish direct signaling from metabolic/biomechanical confounders; the smHCR-validated liver finding is the only mechanistically tight case.
- K=3 latent factors per cell type and R=0 neighborhood default are both unjustified hyperparameter choices that deserve sensitivity analysis.

Thesis-relevant lens: for hypoxia / TME work, NiCo is the cleanest available tool to ask "does macrophage state in a given tumor region co-vary with the local cancer-cell state?" on MERSCOPE, Xenium, or CosMx panels. The combination of factor covariation + ligand-receptor co-correlation gives a principled hypothesis pipeline from spatial panel → candidate signaling axis → orthogonal smHCR validation — directly transferable to any TAM-cancer-cell or TAM-stromal-cell crosstalk question.

## Related

- [[foundations/nico-niche-covariation-tool]] — the tool/framework itself.
- [[concepts/niche-covariation-analysis]] — the conceptual core.
- [[concepts/intrinsic-vs-extrinsic-cell-state-determinants]] — the framing.
- [[concepts/niche-composition-predicts-cell-type-identity]] — NiCo's interaction module.
- [[concepts/kupffer-stellate-tgfb-decorin-feedback]] — liver biological finding.
- [[concepts/paneth-progenitor-wnt3-stem-niche]] — intestinal biological finding.
- [[foundations/cell2location-deconvolution]] / [[foundations/tangram-spatial-mapping]] — annotation benchmarks.
- [[foundations/misty-spatial-omics]] / [[foundations/ncem-niche-cell-effect-model]] — interaction-analysis peers.
- [[foundations/cellcharter-framework]] / [[foundations/stagate-graph-attention-autoencoder]] — tissue-domain benchmarks.
- [[foundations/merfish-imaging-spatial]] / [[foundations/seqfish-imaging-spatial]] / [[foundations/starmap-in-situ-sequencing]] / [[foundations/merscope-vizgen]] — spatial platforms used.
- [[foundations/nmf-non-negative-matrix-factorization]] / [[foundations/liger-nmf-integration]] — NMF / iNMF backbone.
- [[foundations/scrna-seq-10x-chromium]] — reference scRNA-seq modality.
- [[foundations/kupffer-cells]] / [[foundations/hepatic-stellate-cells]] / [[foundations/paneth-cells]] / [[foundations/lgr5-intestinal-stem-cells]] — biological actors.
- [[foundations/tgfb1-cytokine]] / [[foundations/dcn-decorin]] / [[foundations/wnt3-ligand]] / [[foundations/fzd7-receptor]] — signaling molecules.
- [[foundations/smhcr-hybridization-chain-reaction]] — validation assay.
- [[foundations/nkx2-5-tf]] / [[foundations/tbx5-tf]] — cardiac TFs referenced in the SHF interpretation.
- [[papers/cellcharter-reveals-spatial-cell-niches-associated]] — peer spatial-niche framework.
- [[papers/spatial-joint-profiling-dna-methylome-transcriptome]] — peer spatial-multi-omics methods paper.
- [[papers/novae-graph-based-foundation-model-spatial]] — graph-based spatial-foundation peer.
