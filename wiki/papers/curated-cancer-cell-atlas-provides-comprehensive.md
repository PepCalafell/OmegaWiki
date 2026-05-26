---
# === Identification ===
title: "The Curated Cancer Cell Atlas provides a comprehensive characterization of tumors at single-cell resolution"
slug: curated-cancer-cell-atlas-provides-comprehensive
arxiv: ""
doi: "10.1038/s43018-025-00957-8"
pmid: "40341230"
venue: "Nature Cancer"
year: 2025
authors: ["Michael Tyler", "Avishai Gavish", "Chaya Barbolin", "Roi Tschernichovsky", "Rouven Hoefflin", "Michael Mints", "Sidharth V. Puram", "Itay Tirosh"]
first_author: "Michael Tyler"
corresponding_author: "Itay Tirosh"

# === Source & metadata ===
source_type: pdf
s2_id: "beed6f709c8c4efc3e5e432a352d4565e72fee8a"
date_added: 2026-05-26
ingested_date: 2026-05-26
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 5
tier: TIER_1
tags: [scrna-seq, pan-cancer, atlas, metaprograms, cell-cycle, intratumor-heterogeneity, nmf, snrna-seq, tumor-microenvironment]
keywords: [3CA, Curated Cancer Cell Atlas, metaprograms, ITH, NMF, scRNA-seq, snRNA-seq, cell cycle, G1/S, G2/M, TP53, RB1, HPV, cancer-type specificity, marker genes, pseudobulk, TCGA, Tirosh]
domain: oncology

# === Biomedical domain ===
tissue: [multi]
condition: [cancer, healthy]
disease_specific: [breast, lung_adeno, CRC, melanoma, HCC, PDAC, ovarian, MM, HNSCC, GBM, AML, ccRCC, prostate, neuroblastoma, gastric, CML, medulloblastoma, SCLC, DLBCL, skin_BCC, skin_SCC]
species: [human, mouse]
hypoxia_relevant: true
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [scRNA-seq_10x, snRNA-seq, bulk_RNA-seq, NMF, UMAP, infer_CNV]
n_samples: 2836
n_cells_total: 5658705
integration_method: "none"

# === Biology captured ===
key_cell_types: [malignant, T_cell, macrophage, fibroblast, endothelial, B_cell, plasma, dendritic, NK_cell, mast, pericyte, epithelial]
key_markers: [TPSB2, CPA3, MS4A2, KLRF1, NKG7, CD3D, IL32, CD79A, MS4A1, BANK1, MZB1, JCHAIN, C1QA, AIF1, VWF, RAMP2, DCN, COL1A2, KRT7, PIGR, PMEL, KLK3, ESR1, CDKN2A, CEACAM5, APOA2, ANKRD30A, CRYAB, LGR5, PROM1, ASCL2, MKI67, CDK1, TOP2A, CCNB1]
key_pathways: [cell_cycle_G1S, cell_cycle_G2M, hypoxia, EMT, interferon_MHC_II, EpiSen, stress, MYC, NRF2_targets, cholesterol_homeostasis, complement_coagulation, CRC_stemness]

# === User project membership ===
projects: [thesis, hypoxia]
priority: core
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: candidate
exclusion_reason:
data_availability: "https://www.weizmann.ac.il/sites/3CA/ — 124 curated datasets; Supplementary Data 1–7"

# === Cross-references ===
code_url: "https://www.weizmann.ac.il/sites/3CA/"
cited_by: []
---

## Problem

Single-cell RNA-seq has transformed cancer biology, but individual studies typically profile only 5–20 tumours, so each dataset is underpowered to detect robust, clinically meaningful expression patterns. Combining datasets across studies is blocked by batch effects, format inconsistencies, and divergent cell-type annotations. The community lacks a curated, statistically powerful, malignant-cell-centred scRNA-seq compendium analogous to TCGA, and lacks the resolution to systematically characterise context-dependent gene expression, malignant cell markers, and proliferation patterns across many cancer types.

## Key idea

Build the [[concepts/curated-cancer-cell-atlas-3ca|Curated Cancer Cell Atlas (3CA)]] — 124 scRNA/snRNA-seq datasets, 2,836 samples, 5.66 M cells, over 40 cancer types — with standardised cell-type annotations validated by [[foundations/infercnv-cnv-scrna|inferCNV]] and canonical marker genes, deliberately **without** data integration so that biological signal is preserved. From this cohort, regenerate [[concepts/recurrent-malignant-metaprograms-nmf|recurrent malignant metaprograms]] via per-sample NMF, then systematically quantify (i) cell-type marker specificity/sensitivity, (ii) pan-cancer vs cancer-type specificity per cell type, and (iii) cell-cycle proliferation rates and G1/S vs G2/M [[concepts/cell-cycle-phase-bias-malignant|phase bias]] across cell types, cancer types and driver mutations.

## Method

- **Curation**: literature search for cancer scRNA-seq studies; download from public repositories; standardise format (UMI counts or TPM); verify cell types via CNA inference and canonical markers; in 12 studies, redefine cell types de novo; in 9 studies, import annotations from [[foundations/tisch-tumor-immune-cell-atlas|TISCH2]].
- **Resource**: 3CA website (https://www.weizmann.ac.il/sites/3CA/) with per-dataset summary, MP-composition visualisations, gene-query tool, MP-gene-set query tool, and marker-gene explorer.
- **Metaprograms (MPs)**: per-sample [[foundations/nmf-non-negative-matrix-factorization|NMF]] with K=4–9 on malignant cells; retain top-50-gene programs that are robust within and across tumours; cluster by Jaccard overlap into MPs; filter MPs deriving from few studies, ribosomal/mitochondrial-dominated MPs, and likely doublet MPs. Final set: 67 malignant MPs (vs 41 previously).
- **Cell-cycle scoring**: G1/S and G2/M signatures (adapted per dataset; consensus signatures give equivalent results), with thresholds learned from score distributions; cells assigned to G1/S, G2/M, intermediate, or not-cycling.
- **Marker analysis**: per cell type, define sensitivity (fraction of cells expressing the gene) and specificity (gene's restriction to that cell type) using all cancer types with ≥2 datasets.
- **Pseudobulk cancer-type specificity**: aggregate cells of each type per tumour into pseudobulk; compare expression similarity within vs across cancer types restricted to pairs from different studies (controls for batch).
- **TCGA phase bias**: score G1/S and G2/M signatures in bulk TCGA RNA-seq across cancer types; correlate with mutation status of TP53, RB1, and other drivers from ref. 18.

## Results

- 3CA contains 124 datasets, 2,836 samples, 5,658,705 cells across >40 cancer types — nearly doubling the previous 71-dataset version.
- 67 recurrent malignant MPs are defined; **all 41 prior malignant MPs** are recovered, with new variants of EMT, interferon/MHC-II, and entirely new MPs: cholesterol homeostasis, complement and coagulation, NRF2 targets, and a CRC-specific stemness MP (LGR5/PROM1/ASCL2).
- snRNA-seq samples contribute disproportionately to a new cell-cycle MP and a second cilia MP (HYDIN, RFX3, CFAP44, DNAH7), partially overlapping their scRNA-seq counterparts.
- Cell-type markers are strongest for mast cells (TPSB2, CPA3, MS4A2); weakest for malignant cells and dendritic cells.
- Cancer-type-specific malignant markers recover known cases (PMEL/melanoma, KLK3/prostate, ESR1/breast, CDKN2A/HPV+ HNSCC) and surface novel context-dependent genes (ANKRD30A/breast, APOA2/liver).
- Pseudobulk analysis shows malignant cells (and to a lesser extent non-malignant epithelial cells) have by far the highest cancer-type specificity; immune and stromal TME cells are largely pan-cancer conserved.
- Malignant cells are the most proliferative on average (>15% cycling); non-malignant T cells and normal epithelial cells also show substantial cycling activity.
- Proliferation rates positively correlate across cell types within tumours; the strongest pairwise coupling is fibroblast ↔ endothelial (P = 1.3 × 10⁻²⁴).
- Across cancer types, ccRCC is the lowest-proliferating (~5%) and HPV+ HNSCC the highest (>45%); HPV− HNSCC is also highly proliferative (~35%).
- HPV+ and HPV− HNSCC show **opposite phase bias** (G1/S vs G2/M), consistent with HPV-driven pRb degradation.
- TCGA analysis: TP53 mutations are the genomic alteration most consistently associated with G2/M bias; RB1 mutations are most consistently associated with G1/S bias.
- Context-specific phase-bias associations: SMARCA4/EGFR in lung adeno, PIK3CA/CDH1 in breast and stomach, CTNNB1 in endometrial cancer.

## All claims (exhaustive)

- `[c01]` 3CA v2 expands to 124 datasets, 2,836 samples and 5,658,705 cells across >40 cancer types (p.1089) — "the updated version presented here consists of 124 datasets for over 40 cancer types, together comprising 2,836 samples and 5,658,705 cells" — confidence: high — type: quantitative — links: [[concepts/curated-cancer-cell-atlas-3ca]] [[claims/cca3-124-datasets-2836-samples-56m-cells]]
- `[c02]` 67 recurrent malignant metaprograms are defined in the updated 3CA, vs 41 previously (p.1091) — "We defined 67 recurrent expression programs, most of which directly corresponded to MPs that we defined previously; indeed, all 41 of the earlier malignant MPs were captured in the updated list" — confidence: high — type: quantitative — links: [[concepts/recurrent-malignant-metaprograms-nmf]] [[claims/cca3-67-malignant-metaprograms-updated]]
- `[c03]` All 41 previously-defined malignant MPs are recovered in the updated MP list, supporting model robustness (p.1091) — "all 41 of the earlier malignant MPs were captured in the updated list ... supporting the robustness of this model" — confidence: high — type: correlational — links: [[concepts/recurrent-malignant-metaprograms-nmf]] [[claims/cca3-all-41-prior-malignant-mps-recovered]]
- `[c04]` Entirely new MPs detected include cholesterol homeostasis, complement and coagulation, NRF2 targets, and a CRC stemness MP (LGR5/PROM1/ASCL2) (p.1093) — "A handful of entirely new MPs were detected, including cholesterol homeostasis, complement and coagulation and NRF2 targets. Notably, we also observed an MP capturing a 'stemness' phenotype in colorectal cancer (CRC), including genes such as LGR5, PROM1 and ASCL2" — confidence: high — type: methodological — links: [[concepts/recurrent-malignant-metaprograms-nmf]] [[concepts/crc-stemness-metaprogram]] [[claims/cca3-new-mps-cholesterol-complement-nrf2-crc-stemness]]
- `[c05]` snRNA-seq samples disproportionately contribute to a distinct cell-cycle MP and a second cilia MP (HYDIN, RFX3, CFAP44, DNAH7) (p.1091–1093) — "we detected a largely snRNA-seq-specific cell-cycle MP ... We also observed a second cilia MP mostly in snRNA-seq samples ... including HYDIN, RFX3, CFAP44 and DNAH7" — confidence: high — type: methodological — links: [[concepts/snrna-vs-scrna-metaprogram-differences]] [[claims/cca3-snrna-specific-cell-cycle-and-cilia-mps]]
- `[c06]` Mast cells have the strongest cell-type markers across cancer types (TPSB2/AB1, CPA3, MS4A2) with high specificity and sensitivity (p.1093) — "Markers were strongest for mast cells, with multiple genes scoring exceptionally highly for both specificity and sensitivity (TPSB2/AB1, CPA3 and MS4A2)" — confidence: high — type: correlational — links: [[claims/cca3-pan-cancer-mast-cell-markers-strongest]]
- `[c07]` Cancer-type-specific malignant markers recover known cases and surface novel ones (PMEL/melanoma, KLK3/prostate, ESR1/breast, CDKN2A/HPV+ HNSCC, APOA2/liver, ANKRD30A/breast) (p.1093) — "Some markers were consistent with prior knowledge, including PMEL in melanoma, CDKN2A (encoding p16) in human-papillomavirus-positive (HPV+) head and neck cancer and ESR1 in breast cancer ... Other examples of cancer-type-specific genes included APOA2 in liver cancer and ANKRD30A in breast cancer" — confidence: high — type: correlational — links: [[concepts/cancer-type-specific-malignant-markers]] [[claims/cca3-cancer-type-specific-malignant-markers]]
- `[c08]` Malignant cells have by far the highest cancer-type specificity, followed by non-malignant epithelial cells (p.1093) — "Malignant cells exhibited by far the highest cancer type specificity, followed by nonmalignant epithelial cells" — confidence: high — type: quantitative — links: [[concepts/cancer-type-specificity-tme-vs-malignant]] [[claims/cca3-malignant-and-epithelial-highest-cancer-type-specificity]]
- `[c09]` Immune and stromal TME cell types are pan-cancer conserved with minimal cancer-type effect on average expression (p.1093) — "all the other TME immune and stromal cell types appeared to have very limited cancer type specificity ... their average expression profiles are only minimally dependent on the cancer type" — confidence: high — type: correlational — links: [[concepts/cancer-type-specificity-tme-vs-malignant]] [[claims/cca3-tme-immune-stromal-pan-cancer-conserved]]
- `[c10]` Malignant cells are the most proliferative cell type with >15% typically cycling (p.1094) — "A comparison of proliferation rates across cell types confirmed malignant cells as the most proliferative on average ... with more than 15% of malignant cells typically observed cycling" — confidence: high — type: quantitative — links: [[concepts/cell-cycle-phase-bias-malignant]] [[claims/cca3-malignant-most-proliferative-15-percent]]
- `[c11]` Proliferation rates positively correlate across cell types within the same tumour (p.1094) — "we observed an overall positive correlation of proliferation rates between cell types across tumours ... This suggests that the cell cycle may be stimulated in multiple cell types at once by TME factors and intercellular communication" — confidence: high — type: correlational — links: [[claims/cca3-cell-cycle-positively-correlated-across-cell-types]]
- `[c12]` Fibroblast and endothelial proliferation are most tightly coupled across tumours (P = 1.3 × 10⁻²⁴) (p.1094, Fig. 5c) — "An especially high correlation was observed between the proliferation of fibroblasts and the proliferation of endothelial cells" — confidence: high — type: quantitative — links: [[claims/cca3-fibroblast-endothelial-proliferation-tightly-coupled]]
- `[c13]` HPV+ HNSCC is the most proliferative cancer type (>45% cycling malignant cells) (p.1095) — "HPV+ head and neck cancer was the most highly proliferative cancer type (>45% cycling cells). This may be explained by the mechanism of action of HPV, which silences p53 and pRb activity to promote progression through the cell cycle" — confidence: high — type: mechanistic — links: [[foundations/hpv-oncoprotein-e6-e7]] [[claims/cca3-hpv-pos-hnscc-most-proliferative]]
- `[c14]` ccRCC has the lowest malignant proliferation (~5% cycling), consistent with slow kidney tumour growth (p.1095) — "The proliferation of malignant cells was lowest in clear cell kidney cancer (~5% cycling cells), consistent with the slow growth of kidney tumours and their resistance to chemotherapy" — confidence: high — type: quantitative — links: [[claims/cca3-ccrcc-lowest-malignant-proliferation]]
- `[c15]` TP53 mutations are the genomic alteration most consistently associated with G2/M phase bias across cancer types (p.1095) — "an unbiased analysis of many genes commonly mutated in cancer identified TP53 mutations as the most consistently associated with G2/M bias across cancer types" — confidence: high — type: mechanistic — links: [[foundations/tp53-tumor-suppressor]] [[concepts/cell-cycle-phase-bias-malignant]] [[claims/cca3-tp53-mutation-associated-g2m-bias]]
- `[c16]` RB1 mutations are the genomic alteration most consistently associated with G1/S phase bias (p.1095) — "this analysis suggested RB1 mutations as the most consistently associated with G1/S bias" — confidence: high — type: mechanistic — links: [[foundations/rb1-tumor-suppressor]] [[concepts/cell-cycle-phase-bias-malignant]] [[claims/cca3-rb1-mutation-associated-g1s-bias]]
- `[c17]` HPV+ and HPV− HNSCC exhibit opposite cell-cycle phase bias (G1/S vs G2/M) despite both being highly proliferative (p.1095) — "HPV+ and HPV− head and neck cancers were both among the most proliferative cancer types overall, they had opposite patterns of phase bias, with HPV+ exhibiting a strong bias toward G1/S" — confidence: high — type: mechanistic — links: [[foundations/hpv-oncoprotein-e6-e7]] [[foundations/oscc-hpv-negative]] [[claims/cca3-hpv-pos-vs-neg-hnscc-opposite-phase-bias]]
- `[c18]` Avoiding data-integration methods (scANVI, Harmony, Seurat) preserves biological signal in cancer scRNA-seq compendia (p.1096) — "we avoided using data integration methods, such as those offered by scANVI, Harmony and Seurat ... they likely remove some biological signal. This is especially true in cancer, where much of the transcriptional variation between tumors arises from their unique genetic and epigenetic profiles rather than from batch effects" — confidence: medium — type: methodological — links: [[concepts/curated-cancer-cell-atlas-3ca]] [[claims/cca3-no-data-integration-preserves-biological-signal]]

## Discussion captured

### Authors' interpretation

Authors position 3CA as a single-cell counterpart to TCGA — a community resource whose statistical power grows with each contributed dataset. They argue that scale + careful curation + preserved biological heterogeneity (no integration) unlocks discoveries that individual underpowered studies miss: stable recurrent MPs, robust cancer-type-specific markers, and cell-cycle/phase-bias patterns explainable by driver mutations (TP53 → G2/M, RB1 → G1/S). The opposite phase-bias of HPV+ vs HPV− HNSCC is presented as a mechanistic vindication of the framework.

### Comparisons with prior literature (made by authors)

- Builds directly on the previous 71-dataset 3CA (ref. 7, Gavish et al. 2023 — pan-cancer ITH metaprograms).
- Compares the resource scope with TISCH2 (ref. 8) and other scRNA-seq repositories (refs 20–24), arguing 3CA uniquely prioritises malignant cells over TME.
- Cites cell-state discoveries that motivated the resource: NPC state in oligodendroglioma (ref. 2), partial EMT in HNSCC (ref. 3), antigen-presenting CAFs in PDAC (ref. 4).
- Cites integration methods (scANVI ref. 25, Harmony ref. 26, Seurat ref. 27) and the critique that integration removes biological signal (ref. 28).
- Cites prior cell-cycle scoring framework (refs 2, 15) and TCGA driver-mutation catalogue (ref. 18).
- References HPV mechanism of action on p53/pRb (refs 17, 19).

### Mechanistic hypotheses proposed

- The positive correlation of cell-cycle activity across cell types within tumours suggests TME-wide proliferation cues — "cell cycle may be stimulated in multiple cell types at once by TME factors and intercellular communication" (p.1094).
- TP53 loss disables the G1/S checkpoint, biasing cycling cells toward G2/M (p.1095).
- HPV+ tumours' G1/S bias is explained by pRb degradation downstream of HPV E7, since pRb normally restrains G1/S (p.1095).
- snRNA-seq vs scRNA-seq differences in MP recovery may reflect "biological differences in the distribution of RNA transcripts between the nucleus and cytosol" (p.1093).

### Caveats and self-criticism

- Authors note marker analysis is partially biased by the prior cell-type annotations in source datasets (p.1093).
- Acknowledge that not integrating data limits cell-to-cell comparison across samples — "there would be clear advantages to a fully integrated scRNA-seq data resource ... in which expression levels may be directly compared between any two samples" (p.1096).
- Acknowledge clinical annotations remain sparse in source datasets (p.1096).

### Future directions suggested

- Extend with larger studies (>50 samples each).
- Add underrepresented cancer types, post-treatment tumours, metastatic lesions, circulating tumour cells.
- Incorporate snRNA-seq from frozen tissue and methods for fixed tissue.
- Develop integration methods that preserve cancer-relevant biological signal.

## Limitations

- No data integration → cell-to-cell expression cannot be directly compared across samples.
- Cell-type annotations are inherited from heterogeneous source studies; some bias in marker analysis.
- Clinical annotations remain sparse in many source datasets.
- snRNA-seq vs scRNA-seq compositional differences confound some MP comparisons.
- Cell-cycle thresholding is adapted per dataset; subtle technical variation may remain.
- Driver-mutation associations with phase bias are correlational at the bulk-RNA level (TCGA), not causal.
- The atlas is malignant-cell-centred; deep TME analyses are not the focus.

## Open questions

### Open questions raised by authors

- Can robust integration methods be developed that preserve biological signal in cancer scRNA-seq?
- How will rare sample types (post-treatment, metastasis, circulating tumour cells) reshape the MP landscape?
- Will further expansion identify additional ITH hallmarks beyond the current set?

### Open questions identified during ingest

- Do the new MPs (cholesterol homeostasis, NRF2 targets, complement/coagulation) overlap with the [[concepts/cluster-c2-hypoxia-hypomethylation-signature|hypoxia signature]] in malignant cells across cancer types?
- Can the MP-by-cancer-type matrix be used to define a "transcriptional taxonomy" of tumours that competes with mutation-based subtypes?
- Is the fibroblast–endothelial proliferation coupling driven by VEGF/angiogenic crosstalk, and is it modulated by tumour hypoxia?
- Does phase bias predict response to CDK4/6 inhibitors or platinum chemotherapy in HPV+ vs HPV− HNSCC?

## My take

3CA is the obvious starting reference for any pan-cancer scRNA-seq question the thesis raises. The decision to skip integration is unconventional but defensible for malignant-cell biology — and a clean baseline against which integrated atlases can be compared. For the hypoxia thread, the explicit "hypoxia" MP and the new NRF2-targets MP are directly relevant: both should be cross-referenced against the project's hypoxia metaprogram work, and the cancer-type-resolved hypoxia MP scores from 3CA are an obvious external reference. The TP53/RB1 phase-bias mechanism is a clean example of how curated scale converts known biology into pan-cancer quantitative claims — a template for what the thesis aspires to. The fibroblast–endothelial proliferation coupling is a tantalising lead that should be cross-checked against CAF/endothelial MPs in TCGA.

## Related

- [[concepts/curated-cancer-cell-atlas-3ca]]
- [[concepts/recurrent-malignant-metaprograms-nmf]]
- [[concepts/cell-cycle-phase-bias-malignant]]
- [[concepts/cancer-type-specificity-tme-vs-malignant]]
- [[concepts/cancer-type-specific-malignant-markers]]
- [[concepts/crc-stemness-metaprogram]]
- [[concepts/snrna-vs-scrna-metaprogram-differences]]
- [[concepts/tumor-hypoxia-intratumoral-heterogeneity]]
- [[concepts/atlas-level-data-integration]]
- [[foundations/nmf-non-negative-matrix-factorization]]
- [[foundations/tp53-tumor-suppressor]]
- [[foundations/rb1-tumor-suppressor]]
- [[foundations/hpv-oncoprotein-e6-e7]]
- [[foundations/tisch-tumor-immune-cell-atlas]]
- [[foundations/tcga-the-cancer-genome-atlas]]
- [[foundations/infercnv-cnv-scrna]]
- [[foundations/oscc-hpv-negative]]
- [[people/michael-tyler]]
- [[people/itay-tirosh]]
- [[people/sidharth-v-puram]]
