---
# === Identification ===
title: "DECODE: deep learning-based common deconvolution framework for various omics data"
slug: decode-deep-learning-based-common-deconvolution
arxiv: ""
doi: "10.1038/s41592-026-03007-y"
pmid: "41772096"
venue: "Nature Methods"
year: 2026
authors: [Tianyi Zhao, Renjie Liu, Yuzhi Sun, Bingtian Wang, Liyuan Zhang, Qiuhao Chen, Ruibang Luo, Zhiyuan Yuan, Guohua Wang, Liang Cheng, Yadong Wang]
first_author: "Tianyi Zhao"
corresponding_author: "Liang Cheng; Yadong Wang"

# === Source & metadata ===
source_type: pdf
s2_id: "e038862b1f4f707b5955952c5a46cce59174f2d0"
date_added: 2026-05-28
ingested_date: 2026-05-28
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags: [deconvolution, multiomics, deep-learning, cell-type, cell-state, metabolomics, batch-effect]
keywords: [deconvolution, transcriptomics, proteomics, metabolomics, adversarial training, contrastive learning, cell abundance]
domain: methods

# === Biomedical domain ===
tissue: [multi, lung, breast, liver, bone_marrow, blood, colon]
condition: [healthy, cancer]
disease_specific: [MASH, breast_cancer]
species: [human, mouse]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [scRNA-seq_10x, CITE-seq, single-cell_proteomics, single-cell_metabolomics, spatial_transcriptomics, bulk_RNA-seq]
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types: [hepatocytes, Kupffer cells, endothelial cells, T cells, B cells, NK cells, myeloid cells, cancer-associated fibroblasts, PVL cells, cancer epithelial cells, monocytes, melanoma cells]
key_markers: [Ki67, HIF1a, PKM2, MITF, P-NFkB-p65]
key_pathways: []

# === User project membership ===
projects: [methods, thesis]
priority: reference
read_status: skimmed

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: ""

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Deconvolution estimates cell-type abundances from tissue-level data, enabling cellular analysis of large cohorts without single-cell profiling. But existing tools are single-omics by design: MuSiC/CIBERSORTx for bulk transcriptomics, RCTD/SPOTlight for spatial, scpDeconv for proteomics — and nothing for metabolomics, despite metabolomics correlating most strongly with clinical phenotypes. Using a different tool per omics introduces method-specific error sensitivities, so cross-omics abundance comparisons carry unquantifiable systematic biases. Three technical hurdles block a universal framework: omics heterogeneity (scale, distribution, sparsity, dimensionality), incomplete single-cell references (tissue has n+m types, reference covers only n), and severe batch effects between reference and tissue.

## Key idea

A single deep-learning framework, DECODE, that deconvolves transcriptomic, proteomic and metabolomic data — for both cell types and cell states — by combining adversarial batch-effect removal with contrastive-learning denoising. Distribution-agnostic (no Poisson/NB assumption), it works even when the single-cell reference is incomplete, and is the first method to deconvolve metabolomic data.

## Method

Four stages:
- **Stage 1 — pseudotissue generation.** Draw a random cell-type proportion vector from a uniform distribution, sample cells from single-cell reference at a preset total count, aggregate profiles into a pseudotissue; repeat to build the labelled training set ([[pseudobulk-simulation-deconvolution]]).
- **Stage 2 — adversarial batch alignment.** Train encoder, discriminator and eDeconvolver together (L1 + binary cross-entropy) so the discriminator fails to identify feature origin, removing batch effects between train- and target-tissue while preserving biological signal ([[adversarial-domain-adaptation-dann]]). Encoder is then frozen.
- **Stage 3 — contrastive denoising.** Noise (≤10%) is added to train-tissue twice; a DimExpander maps to a new latent space and an attention-based denoiser produces self-attention mask matrices that split features into noise vs. purified train-tissue features. Linear attention + deconvolver yield predicted labels, supervised by L1 loss and a contrastive strategy ([[contrastive-learning]]): co-located train/purified features are positives, noise features negatives.
- **Stage 4 — inference.** Two pathways: standard deconvolution for pure tissues; relative deconvolution (denoiser pathway) when unknown cell types are present.

## Results

- Evaluated across 15 datasets / 7 scenarios vs. 11 baselines (TAPE, CIBERSORTx, MuSiC, scpDeconv, Scaden, RCTD, Seurat, SPOTlight, Tangram, ucdselect, cell2location). Top CCC in cross-donor, cross-disease, cross-health-state, cross-dataset, spatial and multi-cell-type tasks (Fig. 2).
- First metabolomic deconvolution: mouse liver, mouse bone marrow, human colorectal cancer; beats all baselines on most metrics; only DECODE remains usable under perturbation (Fig. 3, Fig. 5e).
- Cell-state deconvolution (pseudotime, cell-cycle, drug-response) best across three omics (Fig. 4).
- Robust to incomplete references and four perturbation types (Fig. 5).
- Cross-omics consistency on PBMC CITE-seq pseudocohorts (Fig. 6a–d); cohort applications to breast cancer (238 samples) and mouse liver (285 samples) recover biologically plausible shifts (Fig. 6e–g).
- Reasonable efficiency (5th RAM, 4th runtime; Fig. 2j,k).

## All claims (exhaustive)

- `[c01]` DECODE is the first method to deconvolve metabolomic data (p.599) "dedicated deconvolution tools for metabolomic data are still lacking" — confidence: high — type: methodological — links: [[claims/decode-first-method-deconvolve-metabolomic-data]] [[concepts/metabolomics-deconvolution]]
- `[c02]` One framework deconvolves transcriptomic, proteomic and metabolomic data (p.596) "a universal deconvolution framework for both cell types and cell states that can be applied to transcriptomic, proteomic and metabolomic data" — confidence: high — type: methodological — links: [[claims/decode-deconvolves-transcriptomic-proteomic-metabolomic-data]] [[concepts/universal-multiomics-deconvolution]]
- `[c03]` DECODE outperforms SOTA in transcriptomic/proteomic deconvolution (p.600) "DECODE is currently the most effective deconvolution method for both transcriptomics and proteomics" — confidence: high — type: quantitative — links: [[claims/decode-outperforms-state-art-deconvolution-methods]] [[foundations/cibersortx-deconvolution]] [[foundations/music-deconvolution]] [[foundations/scaden-deconvolution]]
- `[c04]` Four-stage adversarial + contrastive architecture (p.597) "DECODE integrates adversarial training and contrastive learning techniques... consists of four stages" — confidence: high — type: mechanistic — links: [[claims/decode-uses-four-stage-adversarial-contrastive]] [[foundations/adversarial-domain-adaptation-dann]] [[foundations/contrastive-learning]]
- `[c05]` Stage-2 transferred adversarial training removes batch effects (p.597) "force the discriminator to fail in identifying the origin of the features, thereby effectively mitigating batch effects" — confidence: high — type: mechanistic — links: [[claims/transferred-adversarial-training-removes-batch-effects]] [[foundations/adversarial-domain-adaptation-dann]] [[concepts/batch-removal-vs-bioconservation-tradeoff]]
- `[c06]` Attention denoiser + contrastive learning separates noise for unknown-cell robustness (p.597) "an attention-based denoiser module... separates embedding features into noise features and purified train-tissue features" — confidence: high — type: mechanistic — links: [[claims/attention-denoiser-contrastive-learning-separates-noise]] [[foundations/contrastive-learning]] [[concepts/deconvolution-with-incomplete-reference]]
- `[c07]` Accurate deconvolution with incomplete single-cell reference (p.598) "accurately deconvolve known cell types even when the reference single-cell data are incomplete" — confidence: high — type: methodological — links: [[claims/decode-deconvolves-known-cell-types-accurately]] [[concepts/deconvolution-with-incomplete-reference]]
- `[c08]` Metabolomic profiles have highest cross-cell-type similarity (p.600) "metabolomic profiles exhibited the highest similarity across cell types compared to transcriptomic and proteomic profiles" — confidence: high — type: correlational — links: [[claims/metabolomic-profiles-highest-cross-cell-type]] [[concepts/metabolomics-deconvolution]]
- `[c09]` Only DECODE produces usable metabolomic deconvolution under perturbation (p.603) "all methods except DECODE exhibit unusable performance on metabolomic data" — confidence: high — type: quantitative — links: [[claims/only-decode-produces-usable-metabolomic-deconvolution]] [[concepts/metabolomics-deconvolution]]
- `[c10]` Recovers cell-state abundances across pseudotime/cell-cycle/drug-response (p.601) "DECODE consistently achieved the best performance across all datasets" — confidence: high — type: methodological — links: [[claims/decode-recovers-cell-state-abundances-across]] [[concepts/cell-state-deconvolution]]
- `[c11]` Consistent cross-omics deconvolution on PBMC CITE-seq pseudocohorts (p.604) "DECODE provides consistent, robust cell-abundance estimates for cross-omics cohort integration" — confidence: high — type: quantitative — links: [[claims/decode-gives-consistent-cross-omics-deconvolution]] [[foundations/cite-seq-citeseq]] [[concepts/universal-multiomics-deconvolution]]
- `[c12]` Breast cancer: nonmetastatic tumors higher T/PVL, lower B cells (p.604) "T cells are 1.14-fold higher than in metastatic tumors (P = 1.17 × 10−2)... B cells are 1.70-fold lower" — confidence: medium — type: quantitative — links: [[claims/nonmetastatic-breast-tumors-higher-cell-pvl]] [[concepts/universal-multiomics-deconvolution]]
- `[c13]` Kupffer cells increase in NASH/WDA, stable in HFD (p.604) "a 1.61-fold increase in the NASH group (P = 2.06 × 10−13)... while remaining stable in the HFD group" — confidence: medium — type: quantitative — links: [[claims/kupffer-cells-increase-nash-wda-stay]]
- `[c14]` Recovers consensus liver composition (~70% hepatocytes, ~15% Kupffer) (p.604) "hepatocytes account for nearly 70%... and Kupffer cells for 15% of liver cells" — confidence: high — type: correlational — links: [[claims/decode-recovers-consensus-liver-composition-70]]
- `[c15]` Hepatocyte abundance falls in NASH, rises slightly in HFD (p.604) "the NASH group showed a significant 1.12-fold reduction (P = 1.87 ×10−3). Hepatocyte abundance slightly increased in the HFD group (1.03-fold)" — confidence: medium — type: quantitative — links: [[claims/hepatocyte-abundance-falls-nash-rises-slightly]]
- `[c16]` Cell-cycle phase signatures consistent across cell types (p.601) "cell state yields highly consistent protein expression regardless of cell type" — confidence: medium — type: correlational — links: [[claims/cell-cycle-phase-signatures-consistent-across]] [[concepts/cell-state-deconvolution]]
- `[c17]` Reasonable memory/runtime efficiency (p.600) "it ranked fifth and fourth, respectively, indicating reasonable efficiency" — confidence: high — type: quantitative — links: [[claims/decode-reasonable-memory-runtime-efficiency-among]]
- `[c18]` Pseudotissue training data generated by random uniform sampling (p.597) "A random cell-type proportion vector for all target cell types is drawn from a uniform distribution" — confidence: high — type: methodological — links: [[claims/pseudotissue-training-data-generated-random-uniform]] [[foundations/pseudobulk-simulation-deconvolution]]

## Discussion captured

### Authors' interpretation

Authors frame DECODE as a milestone in multi-omics analysis: stage 2's transferred adversarial training aligns omics across platforms/health-states/sample-types, and stage 3's contrastive learning + self-attention corrects measurement bias and reconciles tissue/reference perturbations, together conferring robustness for both cell types and states even in low-specificity metabolomics. Ablation (dividing DECODE into three components) validated individual stage contributions.

### Comparisons with prior literature (made by authors)

- MuSiC (Nat Commun 2019), CIBERSORTx (Nat Biotechnol 2019) — transcriptomic baselines.
- RCTD (Nat Biotechnol 2022), SPOTlight (NAR 2021), Tangram (Nat Methods 2021), cell2location (Nat Biotechnol 2022) — spatial methods that may misattribute non-spatial variability to spatial effects.
- scpDeconv (Nat Mach Intell 2023) — proteomic domain-adversarial predecessor.
- TAPE (Nat Commun 2022), Scaden (Sci Adv 2020) — deep-learning deconvolution; Scaden examined but did not resolve unknown-cell-type effects.
- MeDuSA (cell-state pseudotime) — requires continuous-pseudotime reference, limiting it to dataset 1.
- Breast cancer immune interpretation cites prior work on T-cell prognosis, B-cell TME heterogeneity, naive-B-cell enrichment in late-stage tumors, and PVL deficiency linked to metastasis.

### Mechanistic hypotheses proposed

- Plasmablast enrichment in nonmetastatic carcinoma reflects an early protective immune role; brain-metastasis plasmablast enrichment may stem from the brain's immune "screening effect" plus tumor-driven regulation (p.604).
- Kupffer-cell increase in NASH/WDA reflects inflammation-driven recruitment; WDA (sugar+cholesterol+alcohol) provokes stronger inflammation than HFD alone (p.604–605).
- Hepatocyte decrease in NASH attributed to apoptosis; HFD increase to oxidative-stress-driven proliferation.

### Caveats and self-criticism

- Artificial-noise-cell generation incurs extra computational cost dependent on single-cell feature dimensionality (one-time per task).
- Cell-type-wise metrics unstable on small real datasets (~10–20 samples) with concentrated proportions, so overall metrics are more reliable.
- Breast-cancer plasmablast trends were inconsistent; causal relationships "require further experimental confirmation."

### Future directions suggested

- Add a dedicated spatial module to better exploit spatial transcriptomics.
- Extend to additional omics layers, e.g., DNA methylation.
- Expand single-cell metabolomics references (currently small, tissue-limited).

## Limitations

- Training requires synthesizing artificial noise cells from single-cell types, adding fixed compute cost tied to feature dimensionality.
- Single-cell metabolomics datasets are scarce and tissue-limited, preventing comprehensive robustness evaluation; blood-metabolite cohorts under-covered.
- Self-reported benchmark; a few baselines exceed DECODE on Pearson's r in some scenarios, and competitors show lower CV (better stability) in transcriptomics/proteomics.
- Cohort biological findings are deconvolution-inferred, not directly measured.

## Open questions

### Open questions raised by authors

- Can a spatial module improve spatial-transcriptomics exploitation?
- Will the framework extend cleanly to DNA methylation and other omics?
- How robust is metabolomic deconvolution once larger single-cell metabolomics references exist?

### Open questions identified during ingest

- Would independent third-party benchmarking confirm the cross-omics SOTA claims?
- How does accuracy degrade as the unknown-cell-type fraction grows large?
- Could non-uniform (Dirichlet) proportion sampling better match real tissue distributions and improve transfer?

## My take

The genuinely novel contribution is metabolomics deconvolution — a real gap, filled. The "universal" framing is methodologically appealing for cross-omics cohort comparison (error-model consistency), which matters for multi-omics thesis work, though each dataset still needs its own trained model. The architecture is a sensible composition of known parts (pseudobulk training + DANN-style alignment + contrastive denoising) rather than a new primitive. Treat the cohort biology (breast cancer, NASH) as hypothesis-generating: it is deconvolution-derived and observational.

## Related

Concepts: [[universal-multiomics-deconvolution]], [[metabolomics-deconvolution]], [[cell-state-deconvolution]], [[deconvolution-with-incomplete-reference]], [[cell-type-abundance-from-bulk-tissue-rnaseq]], [[batch-removal-vs-bioconservation-tradeoff]].

Method foundations: [[cibersortx-deconvolution]], [[music-deconvolution]], [[scaden-deconvolution]], [[rctd-deconvolution]], [[scpdeconv-proteomics-deconvolution]], [[pseudobulk-simulation-deconvolution]], [[adversarial-domain-adaptation-dann]], [[contrastive-learning]], [[cite-seq-citeseq]], [[seurat-v3-integration]], [[scrna-seq-10x-chromium]].

People: [[tianyi-zhao]], [[liang-cheng]], [[yadong-wang]].

Claims: [[claims/decode-first-method-deconvolve-metabolomic-data]], [[claims/decode-deconvolves-transcriptomic-proteomic-metabolomic-data]], [[claims/decode-outperforms-state-art-deconvolution-methods]], [[claims/decode-uses-four-stage-adversarial-contrastive]], [[claims/transferred-adversarial-training-removes-batch-effects]], [[claims/attention-denoiser-contrastive-learning-separates-noise]], [[claims/decode-deconvolves-known-cell-types-accurately]], [[claims/metabolomic-profiles-highest-cross-cell-type]], [[claims/only-decode-produces-usable-metabolomic-deconvolution]], [[claims/decode-recovers-cell-state-abundances-across]], [[claims/decode-gives-consistent-cross-omics-deconvolution]], [[claims/nonmetastatic-breast-tumors-higher-cell-pvl]], [[claims/kupffer-cells-increase-nash-wda-stay]], [[claims/decode-recovers-consensus-liver-composition-70]], [[claims/hepatocyte-abundance-falls-nash-rises-slightly]], [[claims/cell-cycle-phase-signatures-consistent-across]], [[claims/decode-reasonable-memory-runtime-efficiency-among]], [[claims/pseudotissue-training-data-generated-random-uniform]].
