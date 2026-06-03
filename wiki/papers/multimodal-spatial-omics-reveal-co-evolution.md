---
title: "Multimodal spatial-omics reveal co-evolution of alveolar progenitors and proinflammatory niches in progression of lung precursor lesions"
slug: multimodal-spatial-omics-reveal-co-evolution
arxiv: ""
doi: "10.1016/j.ccell.2025.10.004"
pmid: "41202811"
venue: "Cancer Cell"
year: 2026
authors:
  - Fuduan Peng
  - Ansam Sinjab
  - Yibo Dai
  - Warapen Treekitkarnmongkol
  - Sujuan Yang
  - Lorena I. Gomez Bolanos
  - Tieling Zhou
  - Minyue Chen
  - Alejandra G. Serrano
  - Avantika Krishna
  - Nastaran Karimi
  - Manvi Sharma
  - Akshay Basi
  - Guangsheng Pei
  - Jianlong Liao
  - Yunhe Liu
  - Jiping Feng
  - Zahraa Rahal
  - Yang Liu
  - Jiahui Jiang
  - Kai Yu
  - Tala Noun
  - Yuejiang Liu
  - Khaja Khan
  - Kyung Serk Cho
  - Jichao Chen
  - Luisa M. Solis
  - Sarah Mazzilli
  - Steven Dubinett
  - Tina Cascone
  - Avrum E. Spira
  - Stephen Swisher
  - Naoe Jimbo
  - Takuo Hayashi
  - Satsuki Kishikawa
  - Kazuya Takamochi
  - Tomoo Itoh
  - Takashi Yao
  - Kenji Suzuki
  - Neda Kalhor
  - Ignacio I. Wistuba
  - Mingyao Li
  - Seyed Javad Moghaddam
  - Junya Fujimoto
  - Jared Burks
  - Jeffrey Myers
  - Kadir Akdemir
  - Linghua Wang
  - Humam Kadara
first_author: "Fuduan Peng"
corresponding_author: "Linghua Wang; Humam Kadara"

source_type: pdf
s2_id: "1779c8cdcb2bea6c3744e75e8c05d7d123cf232b"
date_added: 2026-05-26
ingested_date: 2026-05-26
ingest_version: 1
last_reviewed:

importance: 5
tier: TIER_1
tags:
  - lung-cancer
  - luad
  - precursor-lesions
  - aah
  - ais
  - mia
  - spatial-transcriptomics
  - xenium
  - visium
  - snrna-seq
  - kac
  - rpii
  - alveolar-progenitor
  - il1b
  - il1r1
  - proinflammatory-niche
  - tam
  - canakinumab
  - precancer-interception
  - clonal-evolution
  - kras
keywords:
  - lung adenocarcinoma
  - alveolar progenitor
  - KRT8-high alveolar intermediate cell
  - reactive type II pneumocytes
  - IL1B-IL1R1 axis
  - epithelial-proinflammatory niche
  - spatial transcriptomics
  - Visium
  - Xenium
  - iStar
  - SpatialInferCNV
  - NMF meta-program
  - NF-κB
  - KRAS
  - canakinumab
  - PD-1 blockade
  - precancer interception
  - field cancerization
domain: oncology

tissue:
  - lung
condition:
  - cancer
  - inflam_precancer
disease_specific:
  - luad
  - aah
  - ais
  - mia
species:
  - human
  - mouse
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

techniques:
  - spatial_visium
  - xenium_in_situ
  - snRNA-seq
  - scRNA-seq_10x
  - WES
  - immunofluorescence
  - sequential_immunofluorescence
  - cytokine_profiling
  - organoid_culture
  - mouse_genetic_models
n_samples: 56
n_cells_total: 5400000
integration_method: ""

key_cell_types:
  - KRT8_high_alveolar_intermediate_KAC
  - RPII_reactive_type_II_pneumocyte
  - AT2
  - AT1
  - AT2_inflamed
  - alveolar_intermediate_cell_AIC
  - ciliated
  - basal
  - club
  - goblet
  - neuroendocrine
  - tumor_cell_LUAD
  - IL1B_high_macrophage_C15
  - IL1B_high_macrophage_C4
  - inflammatory_CAF_iCAF
  - cancer_associated_fibroblast_C1
  - Treg
  - CD8_T_cytotoxic
  - NK_cell
  - B_cell
  - plasma_cell
  - Tfh
  - Th17
  - alveolar_macrophage
key_markers:
  - KRT8
  - SFTPC
  - AGER
  - RTKN2
  - PGC
  - CREB3L1
  - MUC5AC
  - MUC5B
  - TFF3
  - CEACAM5
  - EGFR
  - NQO1
  - LAMP3
  - IL1B
  - IL1R1
  - RELA
  - RELB
  - NFKB1
  - CXCL2
  - NFKBIA
  - NFKBIZ
  - CCL2
  - IL18
  - CSF1
  - CCL3
  - IL33
  - IL17A
  - IL23
  - IL21
  - CXCL1
  - APOE
  - GPMNB
  - COL1A1
  - ACTA2
  - DES
  - MS4A1
  - CXCL13
  - KRAS
  - MET
  - GPRC5A
  - STAT3
key_pathways:
  - IL-1β / IL1R1 signaling
  - NF-κB (RELA / RELB / NFKB1)
  - TNFα via NF-κB
  - Interferon signaling
  - KRAS oncogenic signaling
  - PD-1 / PD-L1 checkpoint
  - alveolar AT2-to-AT1 differentiation
  - KRT8 alveolar intermediate state

projects:
  - thesis
priority: core
read_status: read

hypoxiaverse_status:
exclusion_reason:
data_availability: "GEO: GSE222901, GSE300288, GSE300293 (mouse); GSE307534, GSE308103, GSE307529 (human). Zenodo: 10.5281/zenodo.17172149 (code), 10.5281/zenodo.15670280 (processed human data)."

code_url: "https://github.com/FuduanPeng/LungPCA_Code"
cited_by:
  - mapping-inflammatory-origins-lung-cancer
---

## Problem

Lung adenocarcinoma (LUAD) is the dominant histological subtype of lung cancer and remains highly lethal once invasive. Precursor lesions — atypical adenomatous hyperplasia (AAH), adenocarcinoma in situ (AIS), and minimally invasive adenocarcinoma (MIA) — represent a window for clinical interception, but their heterogeneous progression and the cellular interactions driving early transformation are poorly understood. Bulk and imaging-only studies have not resolved how the earliest precursor cells differ from invasive LUAD, what microenvironmental cues sustain them, or how those cues differ from those of established cancer.

## Key idea

Use **multimodal spatial-omics** (Visium ST + iStar super-pixel + Xenium 5K Prime/298+100-gene + snRNA-seq + SpatialInferCNV + WES) on a 25-patient + 19-patient TMA cohort, paired with a Gprc5a−/− NNK mouse model, to (i) define the earliest precursor cell population — **KRT8-high alveolar intermediate cells (KACs / reactive pneumocytes RPII)** — and (ii) show they reside in **stage-specific epithelial-proinflammatory niches** marked by IL1B-high macrophages and IL1R1-high epithelium. The niche is dispensable in established LUAD but **drives precursor-to-LUAD progression**, providing a mechanistic and therapeutic rationale for **precancer-stage IL-1β interception** (alone or with anti-PD-1).

## Method

- **Visium ST (10x CytAssist)** on 56 tissue samples from 25 patients (11 AAH, 14 AIS, 4 MIA, 26 LUAD, 1 lesion-adjacent normal). 486,519 spots after QC.
- **snRNA-seq** on 75 samples from 23 of the 25 patients; 401,635 nuclei after QC; 139,663 epithelial.
- **Xenium in situ** with human 5K Prime panel + custom 100-gene add-on on 12 samples (6 AAH/AIS + 6 paired LUAD); 4,598,777 cells.
- **Independent validation TMA**: 188 tissue cores, 36 lesions from 19 patients, Xenium 298-gene human lung panel + 100-gene add-on; 593,334 cells.
- **iStar** super-pixel resolution enhancement of Visium ST.
- **SpatialInferCNV** for spot-level CNAs; reconstructed clonal architectures and phylogenies from paired precursor + LUAD lesions, validated against paired snRNA-seq and WES.
- **NMF meta-programs (MPs)**: 9 epithelial MPs (snRNA-seq), 11 MPs (Visium ST), correlated with pan-cancer cell-state atlases.
- **Mouse models**: Gprc5a−/− with NNK exposure (EOE, 3 mo, 7 mo); CC-LR (Kras-LSL-G12D) ± Il1r1 knockout; syngeneic LUAD transplant. Visium ST on mouse lungs; scRNA-seq of enriched epithelial cells; AT2-derived KRT8 lineage-traced organoids (Gprc5a−/−; Krt8CreER; RosatdT/+) ± recombinant IL-1β ± interstitial macrophage co-culture.
- **Antibody interventions**: anti-IL-1β, anti-PD-1, combination, control IgG, in early (prevention) and late (interception) windows. BALF cytokine profiling, scRNA-seq, sequential IF (seq-IF) on TMAs.

## Results

- **KACs / RPII are earliest LUAD precursors**: positioned between AT2 and AT1 by UMAP, pseudotime, and CytoTRACE; their MP landscape (low MP2-AT2, high MP6-tumor/KAC, high MP7-inflammatory) resembles lesions rather than normal alveolar cells.
- **Three clonal evolution patterns** across 25 patients: pattern 1a (shared clones, additional invasive subclones; KRAS absent); pattern 1b (mixed, EGFR/KRAS/MET enriched); pattern 2 (disjoint clones).
- **Earliest clones map to RPII** and are typically shared between normal-adjacent regions, precursors, and paired LUAD.
- **Meta-program trajectory**: progressive decrease in MP2-AT2 and MP5-AT1, increase in MP6-tumor/KAC across normal → AAH → AIS → MIA → LUAD.
- **IL1B-IL1R1 emerges as the top precursor-stage myeloid-epithelial LR pair**, with IL1R1 highly and uniquely expressed in KAC/precursor cells and absent in AT1/AT2.
- **NF-κB subunits (RELA, RELB, NFKB1)** and NF-κB/interferon signatures elevated in KACs and precursors; strongest in KRAS-mutant precursors (100% IL1B-IL1R1 enrichment vs absent in KRAS-WT).
- **Epithelial-proinflammatory niches are precursor-prevalent**: IL1B-high macrophages (Xenium C15; TMA C4), iCAFs, CCL2/IL18/CSF1/NFKB1 immune subsets enriched in AAH/AIS, decreasing in MIA/LUAD.
- **Mouse conservation**: Gprc5a−/− NNK KACs show top TNFα-NF-κB pathway enrichment, highest Il1r1/Rela/Relb/Nfkb1. Mouse Visium ST recapitulates RPII surrounding tumors with Il1b-Il1r1 condensed at peritumor macrophage-rich niches.
- **Functional validation**: recombinant IL-1β and IM co-culture increase number and size of AT2-derived KRT8⁺ organoids. Il1r1 KO in CC-LR mice reduces Kras-mutant tumors and LAMP3⁺/KRT8⁺ cells.
- **Therapeutic validation**: anti-IL-1β > anti-PD-1 monotherapy on lung adenoma/adenocarcinoma volume at 3 and 7 months post-NNK; combination > monotherapy especially at interception (3→7 month) window. Anti-IL-1β reduces BALF CCL3/IL33/IL17A; combo further reduces IL23/IL21/CXCL1.
- **Stage specificity**: anti-IL-1β has no effect on syngeneic established LUAD; combination uniquely counteracts anti-PD-1-associated macrophage enrichment and maximizes CD8⁺ T cell infiltration.

## All claims (exhaustive)

- `[c1]` KRT8-high alveolar intermediate cells (KACs / RPII) are the earliest precursor cells in LUAD evolution (p.327-328) "We also noted a KRT8 high alveolar intermediate cell (KAC) subset positioned between AT2 and tumor cells, and that clustered closely with cells from precursor lesions." — confidence: high — type: mechanistic — links: [[concepts/kac-krt8-alveolar-intermediate-cells-luad-progenitors]] [[claims/kac-rpii-earliest-luad-precursor-cells]]
- `[c2]` KAC meta-program landscape (low MP2-AT2, high MP6-tumor/KAC, high MP7-inflammatory) resembles precursor lesions (p.327) "the MP landscape of KACs resembled that of lesions, including reduced MP2 (alveolar) and more prevalent tumor-associated MP6." — confidence: high — type: correlational — links: [[concepts/nmf-meta-programs-luad-epithelial-stage]] [[claims/kac-mp-landscape-resembles-precursor-lesions]]
- `[c3]` Epithelial-proinflammatory niches are prevalent in lung precursor lesions but become less frequent in invasive LUAD (p.331-332) "These findings reveal epithelial-proinflammatory niches that are not only involved in LUAD pathogenesis but are also stage-specific, being prevalent in early lung precursor lesions." — confidence: high — type: correlational — links: [[concepts/epithelial-proinflammatory-niche-il1b-il1r1-luad-precursor]] [[claims/epithelial-proinflammatory-niche-prevalent-precursor-not-luad]]
- `[c4]` IL1B-IL1R1 is a top precursor-enriched myeloid-epithelial ligand-receptor pair (p.328-329) "we found that IL1B-IL1R1 was among the top ligand-receptor interactions enriched in precursors." — confidence: high — type: correlational — links: [[foundations/il-1-beta-cytokine]] [[foundations/il1r1-receptor]] [[claims/il1b-il1r1-top-ligand-receptor-precursor]]
- `[c5]` IL1R1 is highly and specifically expressed in KAC/precursor cells and absent in normal AT1/AT2 (p.329) "IL1R1 was significantly and highly expressed in KACs and precursor cells, and most evidently in precursor lesions, and absent in normal AT1 and AT2 subsets." — confidence: high — type: mechanistic — links: [[foundations/il1r1-receptor]] [[concepts/kac-krt8-alveolar-intermediate-cells-luad-progenitors]] [[claims/il1r1-expression-restricted-kac-precursor-absent-at1-at2]]
- `[c6]` IL1B-high macrophage subclusters (Xenium C15, TMA C4) are enriched in neighborhoods of KACs and AAH cells (p.330-331) "Cell neighborhoods of KACs, AAH, and inflamed AT2 cells contained significantly higher numbers of C15 cells compared to all other epithelial subsets." — confidence: high — type: correlational — links: [[concepts/epithelial-proinflammatory-niche-il1b-il1r1-luad-precursor]] [[claims/il1b-high-macrophage-subclusters-enriched-near-kac-aah]]
- `[c7]` NF-κB subunit genes (RELA, RELB, NFKB1) and NF-κB / interferon signatures are elevated in KACs and precursor lesions (p.329) "genes (RELA, RELB, and NFKB1) encoding different subunits of NF-κB... were evidently increased in KACs and precursor lesions compared to normal alveolar subsets or LUAD cells." — confidence: high — type: mechanistic — links: [[foundations/nf-kb-p65-rela]] [[claims/nfkb-rela-relb-nfkb1-elevated-kacs-precursor]]
- `[c8]` KRAS-mutant precursors show 100% IL1B-IL1R1 LR enrichment vs absent in KRAS-WT precursors (p.329) "in KRAS-mutant cases, IL1B-IL1R1 interactions were markedly more prevalent in precursor lesions (100%) than in invasive lesions." — confidence: high — type: correlational — links: [[foundations/kras-oncogene]] [[claims/kras-mutant-precursor-il1b-il1r1-enrichment]]
- `[c9]` Three spatial clonal evolution patterns (1a all-shared, 1b partially shared, 2 disjoint) define LUAD precursor-to-invasive progression (p.325-326) "We stratified cases into two broad patterns based on phylogenetic trees and shared clones between precursor and invasive lesions... In pattern 2 (n = 5), no clones were shared between preinvasive and invasive lesions." — confidence: medium — type: correlational — links: [[concepts/spatial-clonal-evolution-patterns-luad-precursor]] [[foundations/spatialinfercnv-spatial-cna]] [[claims/three-spatial-clonal-evolution-patterns-luad-precursor]]
- `[c10]` Earliest clones map to RPII regions and carry elevated KAC scores across shared and stage-specific clones (p.326, 328) "most of the clones mapping to RPII were shared across all tissues and lesions... spots located in shared clones, as well as in precursor- and invasive-specific clones, showed significantly increased levels of a KAC score." — confidence: medium — type: correlational — links: [[concepts/spatial-clonal-evolution-patterns-luad-precursor]] [[claims/rpii-clones-shared-precursor-luad-share-kac-score]]
- `[c11]` Mouse KACs in NNK Gprc5a−/− lungs express highest Il1r1, Rela, Relb, Nfkb1 relative to AT1, AT2, tumor — cross-species conservation (p.332-333) "we found that mouse KACs, compared to AT1, AT2, and even tumor cells, expressed the highest levels of Il1r1 and genes encoding different subunits of NF-κB, particularly Rela and Relb." — confidence: high — type: mechanistic — links: [[foundations/gprc5a-knockout-luad-mouse-model]] [[foundations/nnk-tobacco-carcinogen]] [[claims/mouse-kac-il1r1-nfkb-conserved-with-human]]
- `[c12]` Recombinant IL-1β or interstitial macrophage co-culture significantly increases number and size of AT2-derived KRT8⁺ organoids (p.333) "Treatment with recombinant IL-1β or coculture with lung macrophages (interstitial macrophages, IM) that were isolated from the same mice significantly increased the number and size of organoids compared to the untreated control group." — confidence: high — type: pharmacological — links: [[foundations/il-1-beta-cytokine]] [[claims/recombinant-il1b-and-im-coculture-increase-krt8-organoid-growth]]
- `[c13]` Il1r1 knockout in CC-LR Kras-LSL-G12D mice significantly reduces Kras-mutant lung tumor development and LAMP3⁺/KRT8⁺ cells (p.333) "Knockout of Il1r1 in mice with lung epithelium-driven expression of Kras LSL-G12D... significantly reduced Kras-mutant lung tumor development as well as abundance of LAMP3+/KRT8+ cells in normal alveolar regions." — confidence: high — type: pharmacological — links: [[foundations/il1r1-receptor]] [[foundations/kras-oncogene]] [[claims/il1r1-knockout-reduces-kras-luad-and-krt8-lamp3-cells]]
- `[c14]` Anti-IL-1β is more efficacious than anti-PD-1 monotherapy in reducing lung adenoma/adenocarcinoma volume at 3 and 7 months post-NNK in Gprc5a−/− mice (p.333) "anti-IL-1β was more efficacious in reducing the volume of lung adenomas and adenocarcinomas compared to anti-PD-1 monotherapy, in both early and late time points." — confidence: high — type: pharmacological — links: [[foundations/canakinumab-anti-il1b]] [[concepts/il1b-precancer-interception-luad]] [[claims/anti-il1b-reduces-lung-adenoma-luad-volume-vs-anti-pd1]]
- `[c15]` Combined anti-IL-1β + anti-PD-1 in precancerous phase achieves the greatest reduction in tumor volume, KAC fraction, BALF cytokines, and macrophage infiltration vs either monotherapy (p.333-335) "combined IL-1β and PD-1 blockade led to significantly enhanced tumor suppression relative to monotherapy especially PD-1 blockade and particularly in the interception phase." — confidence: high — type: pharmacological — links: [[concepts/il1b-precancer-interception-luad]] [[claims/anti-il1b-anti-pd1-combination-superior-precancerous-interception]]
- `[c16]` Anti-IL-1β fails to reduce growth of established mouse LUAD cells in a syngeneic transplant model — stage-specificity confirmed (p.333) "antibody-mediated neutralization of IL-1β failed to reduce the growth of mouse LUAD cells in vivo, further emphasizing that targeting anti-IL-1β is relevant in early phases in development of LUAD." — confidence: high — type: pharmacological — links: [[concepts/il1b-precancer-interception-luad]] [[claims/anti-il1b-no-effect-syngeneic-established-luad]]
- `[c17]` Anti-IL-1β reduces BALF concentrations of pro-tumor cytokines CCL3, IL33, IL17A at 7 months post-NNK; combo further reduces IL23, IL21, CXCL1 (p.335) "Anti-IL-1β significantly diminished levels of pro-tumor inflammatory cytokines, including CCL3, IL33, and IL17A, in bronchoalveolar lavage fluid (BALF) at 7 months post-NNK." — confidence: high — type: pharmacological — links: [[foundations/canakinumab-anti-il1b]] [[claims/anti-il1b-reduces-pro-tumor-cytokines-balf]]
- `[c18]` Inflammatory CAFs (iCAFs) are most abundant in AAH/AIS precursor lesions vs normal and invasive LUAD (p.330) "an inflammatory CAF (iCAF) subcluster was most abundant in lung precursor lesions (AAH, AIS) compared to normal lung and invasive cancers." — confidence: medium — type: correlational — links: [[concepts/epithelial-proinflammatory-niche-il1b-il1r1-luad-precursor]] [[claims/icaf-inflammatory-caf-most-abundant-precursor-lesions]]
- `[c19]` KACs show top enrichment of TNFα-via-NF-κB and proinflammatory pathways relative to other epithelial subsets in both human and mouse (p.328, 333) "KACs showed upregulation of various pathways including those associated with inflammation such as TNFα signaling via NF-κB." — confidence: high — type: mechanistic — links: [[foundations/nf-kb-p65-rela]] [[concepts/kac-krt8-alveolar-intermediate-cells-luad-progenitors]] [[claims/kac-pathway-enrichment-tnfa-nfkb-top-vs-other-epithelial]]
- `[c20]` MP2-AT2 and MP5-AT1 decrease progressively while MP6-tumor/KAC increases progressively across normal → AAH → AIS → MIA → LUAD (p.327) "MP2-AT2 and MP5-AT1 significantly and progressively decreased, while MP6-tumor/KAC increased by lesion stage." — confidence: high — type: quantitative — links: [[concepts/nmf-meta-programs-luad-epithelial-stage]] [[claims/mp-trajectory-mp2-at2-mp5-at1-decrease-mp6-tumor-increase]]
- `[c21]` Cohort scale: 486,519 Visium ST spots, 401,635 snRNA-seq nuclei, 4.6M Xenium cells (5K Prime), 593,334 TMA Xenium cells, across 56 + 36 lesions from 25 + 19 patients (p.322, 329-330) "486,519 spots from the Visium ST dataset were retained for downstream analyses... 188 1 mm cores... These samples comprised 593,334 cells." — confidence: high — type: quantitative — links: [[foundations/10x-visium-spatial-transcriptomics]] [[foundations/xenium-in-situ-spatial-transcriptomics]] [[foundations/snrna-seq-single-nucleus]] [[claims/spatial-multiomics-cohort-486k-spots-5m-cells]]

## Discussion captured

### Authors' interpretation

Authors frame KACs (i.e. RPII) as **ancestral to morphologically recognizable precursor lesions** — possibly representing the *true* earliest precancer state, with AAH/AIS being downstream histologically visible manifestations. They argue that "alveolar progenitors, despite exhibiting subtle morphological changes, possess robust characteristics and perhaps denote the earliest lesions in LUAD pathogenesis" (p.333). They reframe the epithelial-proinflammatory niche as a **tumor-initiating spatial field effect**, analogous to (and complementing) genomic/epithelial-intrinsic field effects such as mutant KRAS. The central thesis: **early-stage inflammation is causal for tumor initiation, but becomes dispensable by the time invasive LUAD is established** — a stage-specific niche that opens a clearly bounded therapeutic window.

### Comparisons with prior literature (made by authors)

- KAC / KRT8 alveolar intermediate concept builds on their own prior work (ref 19) and on pulmonary fibrosis literature (refs 31, 32) where similar KRT8⁺ intermediates emerge after lung injury but resolve.
- Three-pattern clonal architecture analysis is concordant with prior precursor-LUAD evolution studies (refs 11, 12, 20).
- KRAS-NF-κB driven oncogenesis literature (refs 24, 25) cited as concordant with the KRAS-mutant precursor-specific NF-κB signature.
- CANTOS atherosclerosis trial (ref 36) showed canakinumab reduced incident lung cancer; CANOPY trials (refs 37-39) failed in advanced NSCLC — authors propose stage-timing reconciles these results.
- COPD literature (ref 34) showing distinct, proinflammatory immune profile vs advanced LUAD is cited as concordant.
- Pan-cancer cell-state MP work (refs 21, 22) used as cross-validation backbone for the 9 epithelial MPs.

### Mechanistic hypotheses proposed

- "Epithelial-proinflammatory niches represent tumor-initiating spatial field effects, synonymous with genomic and epithelial-intrinsic field effects such as mutant KRAS we and others described previously" (p.334).
- IL-1β-IL1R1 signaling, possibly via NF-κB (RELA/RELB) downstream, **causes** rather than merely correlates with KAC expansion — supported by recombinant-IL-1β organoid experiments and Il1r1 KO genetics.
- "Targeting inflammation, perhaps even with immune checkpoint blockade, is more clinically effective in precancerous stages preceding LUAD development" (p.334) — explanatory hypothesis for CANTOS vs CANOPY discordance.

### Caveats and self-criticism

- "It is not clear whether epithelial-proinflammatory niches are a fork in the road between resolution of lung injury or tumor initiation" (p.334).
- Confidence in clonal phylogenies is limited by spot heterogeneity in Visium-based CNA inference; future spatial single-cell DNA-seq is needed.
- Sampling bias: only synchronously resected precursor + LUAD pairs are included; this may distort apparent evolutionary dynamics.
- Translation of mouse Gprc5a−/− NNK findings to spontaneous human LUAD evolution carries species-specific assumptions.

### Future directions suggested

- Spatial DNA-sequencing (SNV + CNA) at single-cell resolution to validate phylogenies.
- Lineage tracing and spatial perturbation in vivo to causally test epithelial-proinflammatory niche role.
- Precancer-stage clinical trials of IL-1β±PD-1 blockade in high-risk lung-cancer screening cohorts.
- Investigation of whether COPD inflammatory remodeling shares the IL1B-IL1R1 KAC axis.

## Limitations

- Visium spot heterogeneity (mixture of tumor and non-tumor cells) reduces SpatialInferCNV signal-to-noise; clonal misassignment may bias phylogenies.
- Sampling bias from synchronous precursor + LUAD resection cohorts (precursors that fully regress are never sampled).
- Mouse Gprc5a−/− NNK is a chemically driven, accelerated model; its precursor dynamics may not fully recapitulate spontaneous human LUAD evolution.
- Treatment-arm sizes are modest (e.g., n=3-4 per group at 3 months), and clinical CANOPY analogs were already negative — extrapolating mouse interception to human prevention requires careful trial design.
- iStar super-pixel resolution enhancement depends on H&E features; tissues with poor histology may degrade super-resolved maps.

## Open questions

### Open questions raised by authors

- Are epithelial-proinflammatory niches a fork between resolution of lung injury and tumor initiation, or specific to oncogenesis?
- Why are KRAS mutations absent from pattern 1a but enriched in pattern 1b?
- Can lineage tracing prove causality of niche → KAC → LUAD progression in vivo?
- Does the IL1B-IL1R1 axis underlie the COPD-LUAD risk link?

### Open questions identified during ingest

- Is the KAC state reversible by inflammation resolution agents (resolvins, anti-IL-1R agonist) prior to mutation acquisition?
- Could IL1R1 IF on CT-guided needle biopsies of indeterminate lung nodules stratify progression risk in real time?
- How do these epithelial-proinflammatory niches relate to the hypoxia-immunosuppressive niches identified in invasive NSCLC ([[papers/tumour-microenvironment-crosstalk-nsclc-progression-response]])? Are they sequential — early IL-1β niche → late hypoxic/SPP1⁺ niche?
- Does the precancer interception logic generalize to other organs' precursors (PanIN, BE, breast DCIS, colon adenoma)?
- Are pattern-2 (clonal-disjoint) precursors mechanistically driven by independent founder clones in a shared field, and does the niche pre-date all of them?

## My take

This paper is the **clearest mechanistic case to date** for a stage-specific anti-IL-1β interception window in LUAD — and likely a template for how other precancer states should be studied. Several features make it particularly important for the thesis:

1. **Stage-specific niche logic**: this reframes the standard tumor-microenvironment narrative. Most TME work emphasizes how late-stage niches (hypoxia, TAM-SPP1, CAF-COL11A1 — see [[papers/tumour-microenvironment-crosstalk-nsclc-progression-response]]) drive immune exclusion in established tumors. Peng et al. show that **early-stage** niches are mechanistically distinct: pro-inflammatory rather than immunosuppressive, IL1B-IL1R1-centered rather than SPP1/TREM2-centered, and **causally** driving KAC expansion rather than passively encasing established tumors.

2. **CANTOS vs CANOPY reconciliation**: provides the first principled mechanistic explanation — niche dissipation by the invasive stage — for why canakinumab worked for lung cancer prevention but failed in advanced NSCLC.

3. **Cross-species + multi-platform rigor**: human Visium, Xenium 5K Prime, TMA Xenium 298+100, snRNA-seq, paired WES, AND mouse Visium + scRNA-seq + organoids + Il1r1 KO + anti-IL-1β±anti-PD-1 trials. Few precancer papers achieve this level of converging evidence.

4. **Connection to existing wiki**: complements [[concepts/cancer-initiating-cell-cell-origin]] (KACs as bona fide cells-of-origin), [[concepts/field-cancerization-clonal-expansion-normal-tissue]] (niche-level field effects extending genomic field effects), and the macrophage/CAF axis from [[papers/tumour-microenvironment-crosstalk-nsclc-progression-response]] (precursor-stage IL1B+ macrophages and iCAFs precede the late SPP1⁺/COL11A1⁺ stromal regime).

5. **Open theoretical question for follow-up work**: the COPD-LUAD risk link likely runs through the same KAC niche. Worth checking whether existing COPD spatial-transcriptomics data show IL1B-IL1R1 niches at non-cancer baseline — i.e., whether the niche is risk-conferring rather than tumor-defining.

Caveats: clonal phylogenies remain noisy; the prevention-to-clinic translation is non-trivial (prophylactic anti-IL-1β in healthy high-risk cohorts has its own risk-benefit ledger); and the model is carcinogen-accelerated rather than spontaneous human-mimicking. Still, this is now the most authoritative reference for early lung TME logic in the wiki.

## Related

- [[concepts/kac-krt8-alveolar-intermediate-cells-luad-progenitors]]
- [[concepts/epithelial-proinflammatory-niche-il1b-il1r1-luad-precursor]]
- [[concepts/spatial-clonal-evolution-patterns-luad-precursor]]
- [[concepts/nmf-meta-programs-luad-epithelial-stage]]
- [[concepts/il1b-precancer-interception-luad]]
- [[concepts/cancer-initiating-cell-cell-origin]]
- [[concepts/field-cancerization-clonal-expansion-normal-tissue]]
- [[foundations/10x-visium-spatial-transcriptomics]]
- [[foundations/xenium-in-situ-spatial-transcriptomics]]
- [[foundations/istar-spatial-resolution-enhancement]]
- [[foundations/snrna-seq-single-nucleus]]
- [[foundations/spatialinfercnv-spatial-cna]]
- [[foundations/infercnv-cnv-scrna]]
- [[foundations/nmf-non-negative-matrix-factorization]]
- [[foundations/cytotrace-differentiation]]
- [[foundations/il-1-beta-cytokine]]
- [[foundations/il1r1-receptor]]
- [[foundations/nf-kb-p65-rela]]
- [[foundations/kras-oncogene]]
- [[foundations/canakinumab-anti-il1b]]
- [[foundations/gprc5a-knockout-luad-mouse-model]]
- [[foundations/nnk-tobacco-carcinogen]]
- [[papers/tumour-microenvironment-crosstalk-nsclc-progression-response]]
- [[papers/emerging-strategies-investigate-biology-early-cancer]]
- [[papers/curated-cancer-cell-atlas-provides-comprehensive]]
- [[papers/cellcharter-reveals-spatial-cell-niches-associated]]
- [[people/fuduan-peng]]
- [[people/ansam-sinjab]]
- [[people/linghua-wang]]
- [[people/humam-kadara]]
