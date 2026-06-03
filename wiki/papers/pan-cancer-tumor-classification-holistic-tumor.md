---
# === Identification ===
title: "Pan-cancer tumor classification by a holistic tumor microenvironment atlas"
slug: "pan-cancer-tumor-classification-holistic-tumor"
arxiv: ""
doi: "10.64898/2025.12.27.696641"
pmid: ""
venue: "bioRxiv"
year: 2025
authors: [Shishang Qin, Xiao Du, Jinhu Li, Nan Jiang, Tian Diao, Yufei Bo, Qinhang Gao, Liangtao Zheng, Xinnan Ling, Qianqian Gao, Xiangjie Li, Sen Gao, Fei Tang, Wenjie Zhang, Chenwei Li, Peihong Fang, Linnan Zhu, Dongfang Wang, Zemin Zhang]
first_author: "Shishang Qin"
corresponding_author: "Zemin Zhang"

# === Source & metadata ===
source_type: pdf
s2_id: ""
date_added: 2026-06-03
ingested_date: 2026-06-03
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags: [pan-cancer, tumor-microenvironment, single-cell, tumor-classification, macrophage, interferon, ICB, CAF]
keywords: [TME heterogeneity, IFIT1+ TAM, type I interferon, multicellular module, TME groups, immune checkpoint blockade, holistic classification]
domain: "oncology"

# === Biomedical domain ===
tissue: [multi]
condition: [cancer]
disease_specific: []
species: [human]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [scRNA-seq_10x, spatial_visium, scATAC-seq, bulk_RNA-seq, mIHC]
n_samples: 1864
n_cells_total: 6762219
integration_method: "Harmony"

# === Biology captured ===
key_cell_types: [tumor-associated macrophages, cancer-associated fibroblasts, T cells, B cells, endothelial cells, perivascular cells, malignant cells]
key_markers: [IFIT1, CXCL9, SPP1, LRRC15, CXCL13, IRF1, IRF2, MT1X, VCAN, PI16]
key_pathways: [type I interferon signaling, IFN-gamma signaling, ECM remodeling, angiogenesis, TGFB signaling, EMT]

# === User project membership ===
projects: [thesis]
priority: reference
read_status: not_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "Public scRNA-seq datasets (GEO and others); bioRxiv preprint"

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Tumor microenvironment (TME) heterogeneity is a major bottleneck to effective cancer immunotherapy. Prior pan-cancer single-cell studies focused on individual or a few cell types, so they could not capture the TME as an integrated system or identify the dominant cellular components that collectively define distinct tumor phenotypes. The paper asks how to classify tumors across cancer types from a *holistic* view of all TME cellular components, and whether such a classification informs immunotherapy stratification and treatment selection.

## Key idea

Build a pan-cancer single-cell TME atlas, identify recurrent cell states and co-occurring multicellular modules, and use the holistic fine-grained TME composition to stratify all tumors into a small number of stable groups. These groups map onto a T/myeloid/stromal trichotomy, differ in ICB response, and each can be matched to a rationally selected cytokine-targeting therapy that specifically perturbs its expression signature.

## Method

- **Atlas construction**: 94 10x scRNA-seq datasets with unbiased sorting across 26 solid cancer types, split into a core collection (55 datasets; 4,590,413 cells from 1,192 samples / 819 patients / 24 cancer types) and a validation set (39 datasets; 2,171,806 cells from 672 samples / 452 patients / 16 cancer types). QC via [[foundations/scanpy]]; malignant cells removed before TME integration.
- **Integration**: benchmarked Harmony, scVI, Scanorama, BBKNN with [[foundations/scib-benchmark-pipeline]] (labels by [[foundations/celltypist]]); [[foundations/harmony-integration]] selected. [[foundations/leiden-clustering]] gave 6 compartments and 95 fine-grained subsets; validated with scAnnotatR and CellTypist.
- **Macrophage / interferon analysis**: functional-signature comparison, [[foundations/cytosig]] for interferon-type activity, [[foundations/scenic-tf-regulon-inference]] for TF activity (IRF1/IRF2), in vitro [[foundations/bone-marrow-derived-macrophage-bmdm]] IFN stimulation, [[foundations/atac-seq]] (scATAC) and spatial validation.
- **Multicellular modules**: cellular co-occurrence network from frequency correlations; spatial colocalization via [[foundations/cell2location-deconvolution]] on 303 Visium samples ([[foundations/10x-visium-spatial-transcriptomics]]).
- **Classification**: clustering on fine-grained TME composition → 10 groups (G01–G10); robustness by perturbation. Validation-set label transfer via [[foundations/tosica]].
- **Genetics & therapy**: malignant-cell refinement via [[foundations/cancer-finder]] + [[foundations/infercnv-cnv-scrna]]; CNV–TME association; random-forest ICB gene panel; CytoSig + public perturbation datasets ([[foundations/csf1r-receptor]], [[foundations/tgfb1-cytokine]], [[foundations/vegf]] pathways); [[foundations/cellchat-cell-cell-communication]] for collagen crosstalk; [[foundations/tcga-the-cancer-genome-atlas]] validation.

## Results

- A six-compartment, 95-subset pan-cancer TME atlas resolving rare populations (MYH11+ fibroblast-like cells, CCL19+ stromal populations, apCAFs).
- Two distinct IFN-related TAM states: IFN-γ-driven CXCL9+ TAMs (c68) and IFN-I-driven IFIT1+ TAMs (c69), with antagonistic IRF1/IRF2 programs, validated in vitro, by scATAC, and spatially.
- A type I interferon multicellular module (M-IFN1) of cross-lineage IFIT1+ cells linked to immune-permissive features, but with a duality (also co-occurs with SPP1+ TAMs and LRRC15+ CAFs).
- 10 stable TME groups (G01–G10) along a T/M/S trichotomy, distributing across (not within) cancer types, validated on an independent set with TOSICA (0.94 mean probability).
- G09 stromal tumors associate with chr1q CNV tracking LRRC15+ myCAF abundance (TCGA-validated).
- A 36-gene panel predicts ICB response (superior AUC across 11 cohorts); matched CSF1R/VEGFR/TGFB inhibition specifically perturbs the corresponding group's signature.

## All claims (exhaustive)

- `[c1]` Pan-cancer single-cell TME atlas spans ~4.6M core cells across 24 cancer types (p.3) "our core collection comprised a total of 4,590,413 high-quality cells from 1,192 samples of 819 patients, representing 24 cancer types" — confidence: high — type: methodological — links: [[claims/pan-cancer-single-cell-tme-atlas]] [[concepts/holistic-tme-based-pan-cancer-tumor]] [[foundations/scanpy]]
- `[c2]` Harmony was the best batch-integration method by scIB benchmark (p.3) "Harmony17 demonstrating superior performance and being selected for our study" — confidence: high — type: methodological — links: [[claims/harmony-selected-best-batch-integration-method]] [[foundations/harmony-integration]] [[foundations/scib-benchmark-pipeline]]
- `[c3]` Adaptive-immune clusters track favorable prognosis; ECM/vascular clusters track poor prognosis (p.3) "six clusters linked to poor prognosis were involved in extracellular matrix (ECM) organization, vascular development, and wound healing" — confidence: medium — type: correlational — links: [[claims/immune-activation-tme-clusters-positive-survival]] [[concepts/holistic-tme-based-pan-cancer-tumor]]
- `[c4]` IFIT1+ and CXCL9+ TAMs are distinct IFN-I- vs IFN-γ-induced states (p.4) "IFIT1+ and CXCL9+ TAMs represented two distinct cellular states in tumors, likely induced by IFN-I and IFN-γ, respectively" — confidence: high — type: mechanistic — links: [[claims/ifit1-cxcl9-tams-distinct-ifn-ifn]] [[concepts/ifit1-tam-type-interferon-induced-state]] [[foundations/ifit1]] [[foundations/cxcl9-chemokine]] [[foundations/cytosig]]
- `[c5]` IRF1 and IRF2 are antagonistic TFs preferentially active in CXCL9+ vs IFIT1+ TAMs (p.4) "two functionally antagonistic TFs, IRF1 and IRF230, were preferentially harbored by c68 and c69, respectively" — confidence: medium — type: mechanistic — links: [[claims/irf1-irf2-antagonistic-transcription-factors-control]] [[foundations/irf1]] [[foundations/irf2]] [[foundations/scenic-tf-regulon-inference]]
- `[c6]` IFN-γ induces CXCL9 and IFN-I induces IFIT1 in human BMDMs (p.4) "in vitro assays confirmed the specific high expression of CXCL9 and IFIT1 in human bone marrow-derived macrophages (BMDMs) upon the stimulation of IFN-γ and IFN-I, respectively" — confidence: high — type: methodological — links: [[claims/vitro-bmdm-ifn-gamma-induces-cxcl9]] [[foundations/bone-marrow-derived-macrophage-bmdm]] [[foundations/ifn-gamma-cytokine]] [[foundations/type-interferon-ifna-ifnb]]
- `[c7]` CXCL9+ and IFIT1+ macrophages are spatially segregated with distinct chromatin accessibility (p.4) "CXCL9⁺ and IFIT1⁺ macrophages were spatially segregated across multiple tumor samples" — confidence: medium — type: correlational — links: [[claims/cxcl9-ifit1-macrophages-spatially-segregated-distinct]] [[foundations/atac-seq]] [[concepts/ifit1-tam-type-interferon-induced-state]]
- `[c8]` IFIT1-high status alone does not equal an immune-hot phenotype (p.5) "IFIT1high status alone does not equal to the immune \"hot\" phenotype" — confidence: medium — type: mechanistic — links: [[claims/ifit1-high-status-alone-does-equal]] [[concepts/ifit1-tam-type-interferon-induced-state]] [[foundations/type-interferon-ifna-ifnb]] [[foundations/lrrc15-leucine-rich-repeat-containing-15]]
- `[c9]` IFIT1-low tumors are enriched for MT1X+ populations and low-activation T cells (immune-cold) (p.5) "low-activation T cells, such as CD8+LEF1+ and IL7R+ T cells, were overrepresented in these tumors" — confidence: medium — type: correlational — links: [[claims/ifit1-low-tumors-enriched-mt1x-low]] [[concepts/ifit1-tam-type-interferon-induced-state]]
- `[c10]` The type I interferon multicellular module (M-IFN1) promotes an immune-permissive TME (p.6) "M-IFN1 showed potential to facilitate the formation of an immune-hot TME" — confidence: medium — type: mechanistic — links: [[claims/ifn-multicellular-module-promotes-immune-permissive]] [[concepts/type-interferon-multicellular-module-ifn1]] [[concepts/tme-cellular-co-occurrence-multicellular-modules]]
- `[c11]` Holistic TME composition stratifies tumors into 10 stable groups along a T/M/S trichotomy (p.6) "we further stratify all tumors into 10 stable groups" — confidence: high — type: methodological — links: [[claims/holistic-tme-composition-stratifies-tumors-into]] [[concepts/holistic-tme-based-pan-cancer-tumor]]
- `[c12]` The 10 TME groups have distinct cellular compositions mapping to T-, M-, S-centric phenotypes (p.6-7) "G08-G10 exhibited low immune-cell infiltration but high proportions of stromal cells ... indicative of immune \"cold\" or stroma (S)-centric tumors" — confidence: medium — type: correlational — links: [[claims/tme-groups-g01-g10-distinct-cellular]] [[concepts/holistic-tme-based-pan-cancer-tumor]] [[foundations/lrrc15-leucine-rich-repeat-containing-15]]
- `[c13]` Most cancer types distribute across multiple TME groups rather than mapping to tissue of origin (p.7) "apart from G03 and G05, other TME groups exhibited a mixture of various cancer types" — confidence: medium — type: correlational — links: [[claims/cancer-types-distribute-across-tme-groups]] [[concepts/holistic-tme-based-pan-cancer-tumor]] [[concepts/cancer-type-specificity-tme-vs-malignant]]
- `[c14]` TOSICA transfers atlas labels to the validation set with 0.94 mean probability (p.8) "an averaged prediction probability of 0.94 was achieved" — confidence: high — type: methodological — links: [[claims/tosica-transfers-atlas-labels-validation-set]] [[foundations/tosica]] [[concepts/scrna-atlas-as-reference-projection]]
- `[c15]` G09 tumors associate with chr1q CNV tracking LRRC15+ myCAF abundance (p.9) "G09 exhibited significant correlations with CNVs on chromosome 1q" — confidence: medium — type: correlational — links: [[claims/g09-chromosome-1q-cnv-associates-lrrc15]] [[foundations/infercnv-cnv-scrna]] [[foundations/lrrc15-leucine-rich-repeat-containing-15]] [[foundations/tcga-the-cancer-genome-atlas]]
- `[c16]` A 36-gene TME panel predicts ICB response with superior AUC across cohorts (p.10) "our panel achieved superior AUCs, demonstrating robust predictive power" — confidence: high — type: quantitative — links: [[claims/36-gene-tme-panel-predicts-icb]] [[concepts/immune-checkpoint-blockade]] [[concepts/holistic-tme-based-pan-cancer-tumor]]
- `[c17]` Matched cytokine-pathway inhibition specifically perturbs each group's signature (p.10) "CSF1R inhibitor-treated tumor-bearing mice showed robust decreases in G05/G07 signatures relative to controls" — confidence: medium — type: pharmacological — links: [[claims/matched-cytokine-pathway-inhibition-perturbs-group]] [[concepts/tme-group-matched-cytokine-targeting-therapy]] [[foundations/csf1r-receptor]] [[foundations/tgfb1-cytokine]] [[foundations/vegf]]
- `[c18]` SPP1+ TAMs express M2 pro-tumoral programs (hypoxia, ECM, angiogenesis) (p.4) "SPP1+ TAMs (c66) exhibited an elevated expression of multiple M2-related pathways, including response to hypoxia" — confidence: high — type: mechanistic — links: [[claims/spp1-tams-express-m2-pro-tumoral]] [[foundations/spp1-secreted-phosphoprotein-1]] [[concepts/cxcl9-spp1-tam-ratio-ici-biomarker]]

## Discussion captured

### Authors' interpretation

The authors frame the work as a conceptual advance: rather than dissecting individual cell types, they treat the TME as an integrated system whose holistic cellular composition defines tumor phenotypes. They argue the 10-group classification links biological patterns (dominant cellular/cytokine programs) to therapeutic outcomes and can guide patient stratification and treatment selection.

### Comparisons with prior literature (made by authors)

- Build on their own and others' pan-cancer single-cell analyses of immune and non-immune cell types (refs 7–15), which they say could not capture the TME as an integrated system.
- SPP1+ vs CXCL9+ TAM polarity from a recent study (ref 27); add IFIT1+ TAMs as a distinct IFN-I state.
- Clinical support cited in discussion: CSF1R and TGFB inhibition with ICB in GM and PAAD (refs 54,55), with failures for mismatched approaches (TGFB blockade in GM, TAM depletion in PAAD; refs 56,57); ICB + TGFB inhibition in ESCA achieving 62.5% response (ref 58); ICB + VEGFR inhibition in RCC and LIHC (refs 59,60).

### Mechanistic hypotheses proposed

- IFN-I stimulation is linked to establishing an immune-permissive condition (M-IFN1 recruits lymphocytes via chemokines and supports B cells via TNFSF13B), p.6.
- Cancer-cell CNVs on chr1q (ADAM15, EFNA1) may shape the G09 fibrotic TME, p.9.
- Therapies aligned with a group's dominant TME features tend to succeed while mismatched approaches do not, p.11.

### Caveats and self-criticism

- "IFIT1high status alone does not equal to the immune 'hot' phenotype" — IFN-I has both pro- and anti-tumor effects (p.5).
- Upstream drivers of immune-inactivation tumor characteristics "remain unresolved" (p.5); causal mechanisms left to future work (p.11).

### Future directions suggested

- Elucidate causal mechanisms linking IFN-I-related TAMs to immunosuppressive TME features and cancer-cell plasticity.
- Prospectively test group-matched cytokine-targeting interventions combined with ICB.

## Limitations

- Atlas restricted to 10x unbiased-sorting datasets, excluding other platforms/enrichment strategies.
- Many associations (CNV–CAF, cytokine–group, prognosis) are correlational, not causally validated.
- Therapeutic perturbation evidence is signature-level from public/mouse datasets, not prospective patient-matched trials.
- Marker-state induction inferred from in vitro stimulation and signaling-activity inference rather than in vivo lineage tracing.

## Open questions

### Open questions raised by authors

- What are the causal drivers of the immune-inactivation TME and the IFN-I duality?
- Can group-matched cytokine therapies improve ICB outcomes prospectively?

### Open questions identified during ingest

- How stable is the 10-group scheme as new cancer types/platforms are added?
- Are IFIT1+/CXCL9+/SPP1+ TAM states terminal or interconvertible in vivo?
- Do chr1q genes (ADAM15, EFNA1) causally drive LRRC15+ myCAF accumulation?

## My take

A high-resolution, integrative reframing of pan-cancer tumor classification around whole-TME cellular composition from the Zemin Zhang lab. Its strongest contributions are the IFIT1+ (IFN-I) vs CXCL9+ (IFN-γ) TAM dichotomy and a clean translational loop from a 10-group classification to group-matched cytokine therapy. The duality of IFN-I signaling and the largely associative therapeutic evidence are the main places where causal follow-up is needed.

## Related

- [[concepts/holistic-tme-based-pan-cancer-tumor]]
- [[concepts/ifit1-tam-type-interferon-induced-state]]
- [[concepts/type-interferon-multicellular-module-ifn1]]
- [[concepts/tme-cellular-co-occurrence-multicellular-modules]]
- [[concepts/tme-group-matched-cytokine-targeting-therapy]]
- [[concepts/cxcl9-spp1-tam-ratio-ici-biomarker]]
- [[concepts/pan-cancer-tumor-ecosystem-five-subtypes]]
- [[concepts/cancer-type-specificity-tme-vs-malignant]]
- [[concepts/immune-checkpoint-blockade]]
- [[people/shishang-qin]] · [[people/zemin-zhang]] · [[people/linnan-zhu]] · [[people/dongfang-wang]]
