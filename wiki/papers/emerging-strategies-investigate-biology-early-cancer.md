---
title: "Emerging strategies to investigate the biology of early cancer"
slug: emerging-strategies-investigate-biology-early-cancer
arxiv: ""
doi: "10.1038/s41568-024-00754-y"
pmid: ""
venue: "Nature Reviews Cancer"
year: 2024
authors:
  - "Ran Zhou"
  - "Xiwen Tang"
  - "Yuan Wang"
first_author: "Ran Zhou"
corresponding_author: "Yuan Wang"
source_type: pdf
s2_id: ""
date_added: 2026-05-25
ingested_date: 2026-05-25
ingest_version: 1
last_reviewed:
importance: 4
tier: TIER_1
tags: [early-cancer, precancer, lineage-tracing, organoid, autochthonous-mouse-model, single-cell-omics, spatial-omics, ai-cancer-detection, review]
keywords: [early cancer, precancerous lesions, cell of origin, lineage tracing, milestone reporter, ecDNA, pre-CAF, immune evasion, organoid, GEMM, AI cancer detection]
domain: "oncology"

tissue: [oesophagus, colon, pancreas, lung, breast, prostate, skin, cervix, stomach, liver, brain, bone_marrow]
condition: [cancer, inflam_precancer]
disease_specific: [PDAC, oesophageal_SCC, EAC, colorectal_cancer, lung_adenocarcinoma, breast_cancer, prostate_cancer, glioblastoma, multiple_myeloma, cervical_cancer]
species: [human, mouse]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

techniques: [scRNA-seq_10x, scATAC-seq, spatial_visium, WGS, WES, ChIP-seq, lineage_tracing, intravital_microscopy, light_sheet_microscopy, bioluminescence_imaging, CRISPR-Cas9, organoid_culture]
n_samples:
n_cells_total:
integration_method: ""

key_cell_types: [tissue_stem_cell, cancer_initiating_cell, precancerous_epithelial_cell, pre-CAF, Treg, CD8_T_cell, NK_cell, senescent_macrophage, monocyte, fibroblast]
key_markers: [TP53, KRAS, APC, MYC, ERBB2, CDKN2A, PTEN, SOX9, ARID1A, LGR5, OLFM4, ASCL2, AXIN2, RNF43, EPHB2, Tff2, MSI2, EGFR, PDGFB, NF1, CIITA, SOCS1, p16, Cox2, ERK]
key_pathways: [WNT, KRAS-RAF-MEK-ERK, PI3K-AKT, TP53, EMT, immune_evasion, metabolic_reprogramming, senescence]

projects: [thesis]
priority: context
read_status: skimmed

hypoxiaverse_status:
exclusion_reason:
data_availability: ""

code_url: ""
cited_by: []
---

## Problem
Despite extensive understanding of advanced-stage cancer, the biology of early cancer — the multistage transformation cascade from cell of origin through clonal expansion in normal tissue, precancerous state, and finally invasive cancer — remains poorly characterized. Early-stage clinical samples are scarce; widely used cancer models (cell lines, PDX) derive from fully developed tumours and are unsuitable for studying initiation. The central unanswered question is when and how a mutant cell crosses the "tipping point" of irreversible commitment to malignancy, and how to distinguish it from the much larger pool of driver-mutant cells in normal tissue that never become cancer.

## Key idea
The review argues that a coordinated arsenal of new tools — clinical sample atlases (HTAN PreCancer), event-based milestone-reporter lineage tracing in GEMMs, organoid and stem-cell-derived ex vivo systems, single-cell and spatial multi-omics, advanced imaging (intravital multiphoton, tissue clearing + light sheet, Akaluc bioluminescence), and AI models — is converging to make the early-cancer trajectory experimentally tractable. Pairing these techniques across clinical and preclinical models, with explicit attention to clonal competition and microenvironmental crosstalk, is the path to mechanism-based early-detection and prevention strategies.

## Method
This is a Nature Reviews Cancer narrative review (no new primary data). The authors structure the synthesis around four pillars:
1. Clinical samples — what can be learned from human precancerous lesions (Tables 1, 2) with single-cell, spatial omics, metabolomics, microbiome profiling and AI models trained on multimodal data.
2. Autochthonous mouse models (Table 3) — GEMMs and carcinogen-induced models, dissected with direct imaging, lineage tracing, scRNA/scATAC-seq.
3. Organoid and stem-cell-derived models (Table 4) — genetic and viral cancer induction, mutant-organoid orthotopic transplantation (Table 5), longitudinal sampling.
4. Translational outlook — implications for early detection, biomarker discovery, and cancer interception.

## Results
The review crystallizes several field-level observations:
- Driver-mutation burden in normal tissue (e.g. TP53 in oesophagus) vastly exceeds lifetime cancer risk, so additional events are required.
- Precancerous lesions across tumour types share emergent features: stem-like cell populations, metabolic reprogramming, CNV accumulation (cancer-specific), pre-CAF stromal priming, and a CD4→Treg + CD8/NK depletion immune-evasion programme.
- ecDNA appears already in Barrett's oesophagus and strongly predicts EAC progression.
- Event-based lineage tracing (p53 LOH, mutant p53 stabilization, sustained ERK, RAC, p16) enriches the rare cells destined for cancer and aligns independent carcinogenic trajectories across mice.
- Most driver-mutant cells in early lesions never become cancer; mutant clones can even outcompete carcinogen-induced precancerous lesions in adjacent normal epithelium.
- Senescent macrophages and Cox2+ senescent PanIN cells promote tumorigenesis; clearance ameliorates lung cancer.
- AI models (CancerRiskNet, DeepTrace, AI-MRI, PhylogicNDT) are entering clinical validation, with AI-MRI four-fold more efficient than density screening for breast.

## All claims (exhaustive)
- `[c01]` Cancer driver mutations are necessary but not sufficient for cancer (p.851) "We now realize that driver mutations are usually necessary but not sufficient to drive early cancer progression" — confidence: high — type: mechanistic — links: [[concepts/precancerous-lesion-malignant-transformation]] [[concepts/field-cancerization-clonal-expansion-normal-tissue]] [[claims/driver-mutations-necessary-sufficient-cancer]]
- `[c02]` TP53-mutant clones occupy 5-10% of normal oesophagus by middle age and 15-30% by age 70 (p.851) "the mutation burden of TP53 in the normal oesophagus can reach 5–10% of the cells by middle age and rise up to 15–30% in individuals of 70 years or older" — confidence: high — type: quantitative — links: [[foundations/tp53-tumor-suppressor]] [[concepts/field-cancerization-clonal-expansion-normal-tissue]] [[claims/tp53-mutation-burden-normal-oesophagus-reaches]]
- `[c03]` Lifetime oesophageal cancer risk is <1% despite this burden (p.851) "the lifetime risk of oesophageal cancer is less than 1%, indicating the requirement of additional events" — confidence: high — type: quantitative — links: [[concepts/field-cancerization-clonal-expansion-normal-tissue]] [[claims/lifetime-oesophageal-cancer-risk-less-than]]
- `[c04]` Stem-like cell populations are present in precancerous lesions of colon, gastric, lung adenocarcinoma and cervical cancer (p.851-852) "Such stem-like cell populations are identified in precancerous lesions of gastric cancer, lung adenocarcinoma and cervical cancer" — confidence: high — type: correlational — links: [[concepts/stem-like-cells-precancerous-lesions]] [[claims/precancerous-lesions-contain-stem-like-cell]]
- `[c05]` Metabolic reprogramming (TCA down in adenomas, energy metabolism up in AAH) occurs already at precancer (p.853) "the tricarboxylic acid cycle pathway was initially downregulated in precancerous adenomas... energy metabolism pathways have been upregulated in atypical adenomatous hyperplasia" — confidence: medium — type: correlational — links: [[claims/metabolic-reprogramming-occurs-already-precancerous-stage]]
- `[c06]` CNVs accumulate cancer-specifically: present in oesophageal SCC, head-and-neck, PDAC precancers but absent in colorectal adenomas (p.853) "Cells with CNVs have been identified in precancerous lesions of oesophageal SCC, head and neck cancer and pancreatic ductal adenocarcinoma, but not in colorectal adenomas" — confidence: medium — type: correlational — links: [[foundations/infercnv-cnv-scrna]] [[claims/copy-number-variations-accumulate-cancer-specifically]]
- `[c07]` ecDNA in Barrett's oesophagus is strongly associated with EAC progression and amplifies ERBB2, KRAS, MYC, CIITA, SOCS1 (p.853) "Detection of ecDNAs in Barrett's oesophagus biopsies are strongly associated with the development of oesophageal adenocarcinoma (EAC)" — confidence: high — type: correlational — links: [[concepts/ecdna-precancer-malignant-progression]] [[foundations/ecdna-extrachromosomal-dna]] [[foundations/barretts-oesophagus]] [[claims/ecdna-barrett-oesophagus-predicts-eac-progression]]
- `[c08]` A shift from immune surveillance to evasion underlies the onset of malignant transformation (p.853) "These studies together reveal a shift from immune surveillance to immune evasion, which underlies the onset of malignant transformation" — confidence: high — type: mechanistic — links: [[concepts/immune-surveillance-evasion-precancer-transition]] [[claims/immune-surveillance-evasion-transition-precancer-hallmark]]
- `[c09]` Pre-CAFs that suppress cytotoxic immunity are present in PanIN, gastric, oesophageal and oral precancers (p.853) "pre-CAFs that promote malignant progression have been found in pancreatic intraepithelial neoplasia (PanIN) and precancerous lesions of gastric, oesophageal and oral cancers" — confidence: high — type: mechanistic — links: [[concepts/pre-cafs-cancer-associated-fibroblasts-premalignant]] [[foundations/panin-pancreatic-intraepithelial-neoplasia]] [[claims/pre-cafs-promote-malignant-progression-panin]]
- `[c10]` Microbiome-derived cobalamin and succinyl-CoA in HSIL are early biomarkers for anal cancer (p.853) "increased levels of microbiome-derived cobalamin and succinyl-CoA in high-grade squamous intraepithelial lesions as early-stage biomarkers for anal cancer" — confidence: medium — type: correlational — links: [[claims/microbiome-derived-cobalamin-succinyl-coa-early]]
- `[c11]` AI-supplemented MRI is four-fold more efficient than breast-density screening for early breast cancer detection (p.854) "an AI model for supplemental MRI is four times more efficient for early breast cancer detection than traditional breast density measures" — confidence: high — type: quantitative — links: [[claims/ai-mri-four-times-more-efficient]]
- `[c12]` PhylogicNDT reconstructs cancer mutational history from advanced samples lacking precancer (p.854) "PhylogicNDT could analyse the exome sequencing data of advanced-stage head and neck SCCs, using whole-genome amplifications as milestone events" — confidence: medium — type: methodological — links: [[claims/phylogicndt-reconstructs-cancer-mutational-history-without]]
- `[c13]` KrasLSL-G12D/+;PDX-Cre or p48-Cre mice spontaneously develop PanINs that progress to PDAC at low frequency (p.857) "pancreas-specific Kras mutation in KrasLSL-G12D/+;PDX-Cre or KrasLSL-G12D/+;p48-Cre mice spontaneously develop early PanINs" — confidence: high — type: methodological — links: [[foundations/kras-oncogene]] [[foundations/cre-loxp-recombinase-system]] [[foundations/gemm-genetically-engineered-mouse-model]] [[foundations/panin-pancreatic-intraepithelial-neoplasia]] [[claims/kraslsl-g12d-pdx-cre-spontaneously-develops]]
- `[c14]` Additional Trp53 or Cdkn2a loss in KrasG12D background drives PDAC penetrance to near 100% (p.857) "Additional mutations or loss of Trp53 or Cdkn2a increases PDAC penetrance to near 100%" — confidence: high — type: quantitative — links: [[foundations/tp53-tumor-suppressor]] [[foundations/cdkn2a-tumor-suppressor]] [[foundations/kras-oncogene]] [[claims/trp53-cdkn2a-loss-kras-drives-pdac]]
- `[c15]` DEN-induced oesophageal SCC mouse models develop mutational landscapes similar to aged humans (p.857) "DEN-induced models for oesophageal SCC develop a mutational landscape similar to that of aged humans" — confidence: medium — type: methodological — links: [[foundations/den-diethylnitrosamine-carcinogen]] [[claims/den-induced-oesophageal-scc-mutational-landscape]]
- `[c16]` Akaluc/AkaLumine and NanoLuc/CFz detect 10-1000 cells in deep organs like lung and brain (p.858) "Akaluc and AkaLumine and NanoLuc and CFz, which can detect as low as 10 to 1,000 cells in deep organs such as the lung and the brain" — confidence: high — type: quantitative — links: [[foundations/akaluc-akalumine-bioluminescent-system]] [[claims/akaluc-akalumine-detects-10-1000-cells]]
- `[c17]` Carcinogen-induced precancerous lesions in oesophagus can be outcompeted by adjacent normal-tissue mutant clones (p.858) "Surprisingly, carcinogen-induced precancerous lesions are outcompeted by mutant clones in the adjacent normal oesophagus" — confidence: medium — type: correlational — links: [[concepts/field-cancerization-clonal-expansion-normal-tissue]] [[claims/mutant-clones-outcompete-carcinogen-induced-precancerous]]
- `[c18]` Tff2+ pancreatic transit-amplifying progenitors are resistant and protective against KRAS-driven carcinogenesis (p.858) "a trefoil factor 2 (Tff2)-positive transit-amplifying progenitor population in the pancreas is resistant to and protective against KRAS-driven carcinogenesis" — confidence: medium — type: mechanistic — links: [[concepts/cancer-initiating-cell-cell-origin]] [[claims/tff2-positive-pancreatic-progenitors-resistant-protective]]
- `[c19]` Senescent macrophages promote early lung tumorigenesis by suppressing cytotoxic T cells; senescent-cell clearance ameliorates lung cancer (p.858) "senescent macrophages promote early-stage tumorigenesis by suppressing cytotoxic T cell responses, and their clearance ameliorates lung cancer development" — confidence: medium — type: mechanistic — links: [[concepts/senescent-cells-promote-early-tumorigenesis]] [[claims/senescent-macrophages-promote-early-lung-tumorigenesis]]
- `[c20]` The majority of driver-mutant cells in early tissue lesions do not progress to cancer (p.859) "the majority of mutant cells will not give rise to cancer and that additional genetic and transcriptional events in specific lineages are required to promote malignant progression" — confidence: high — type: mechanistic — links: [[concepts/cancer-initiating-cell-cell-origin]] [[concepts/carcinogenesis-tipping-point-irreversibility]] [[claims/most-driver-mutant-cells-early-lesions]]
- `[c21]` Pancreatic epithelial cells gain a unique chromatin state distinguishing transformation from regeneration upon inflammation (p.859) "pancreatic epithelial cells increase epigenetic plasticity upon inflammation, entering into a unique chromatin state distinguishing transformation from regeneration" — confidence: medium — type: mechanistic — links: [[foundations/atac-seq]] [[claims/pancreatic-epithelial-cells-gain-unique-chromatin]]
- `[c22]` TP53-mutant human gastric organoids cultured >2 years recapitulate clonal evolution and CNV accumulation of preneoplasia (p.860) "genomic analysis and lineage tracing have revealed the clonal evolution and selection during preneoplasia in TP53-mutant human gastric organoids that were cultured over 2 years" — confidence: medium — type: methodological — links: [[concepts/organoid-cancer-initiation-3d-model]] [[foundations/organoid-3d-tissue-culture]] [[claims/tp53-mutant-human-gastric-organoids-show]]

## Discussion captured

### Authors' interpretation
The authors frame their synthesis around a central conceptual gap: identifying the "tipping point" at which a driver-mutant cell becomes irreversibly committed to a cancer trajectory. They argue that the convergence of (i) milestone-reporter lineage tracing, (ii) single-cell/spatial multi-omics, (iii) 3D imaging and bioluminescence-based deep-tissue sensing, and (iv) AI-driven multimodal integration is what finally makes this question experimentally tractable. They emphasize that microenvironmental remodelling (pre-CAFs, immune evasion, senescent cells) is not a late event of advanced disease but a defining feature of the precancer-to-cancer transition.

### Comparisons with prior literature (made by authors)
The review cites the HTAN PreCancer Atlas (NCI) as the principal large-scale infrastructure effort. It contrasts the strengths and limitations of cell-line/PDX models (unsuitable for initiation) with autochthonous GEMMs (gold standard, expensive) and human organoid systems (cost-effective, lack full microenvironment unless transplanted). It positions PhylogicNDT, CancerRiskNet, DeepTrace and various imaging-based AI screens as state-of-the-art examples of AI translation.

### Mechanistic hypotheses proposed
- "The dynamics of these factors determine the tipping point at which the lesions progress irreversibly towards malignancy." (Fig.1 legend)
- Event-based milestone reporters (p53 LOH, mutant-p53 stabilization, sustained ERK, RAC, p16) are proposed as the right experimental handle for the tipping point.

### Caveats and self-criticism
- Mouse-human differences in immunity, metabolism, and tissue architecture limit the translation of GEMM findings to patients.
- GEMMs introduce alterations into entire lineages, unlike sparse somatic mutation in humans.
- Snapshot sampling of human precancers cannot directly answer which lesions will progress.
- Many AI models are 'black box' with single-centre training data → bias and overfitting risk.

### Future directions suggested
- Combining milestone reporters with other lineage-tracing systems for higher precision.
- Scaling longitudinal human sampling (HTAN-style) for cancers currently lacking precursor lesions.
- Developing interception therapies targeting pre-CAFs, senescent cells and stem-like states.
- Improving interpretability and external validation of AI models.

## Limitations
- Single-author-group review with potential thematic bias toward lineage tracing and event-based reporters (the senior author's own toolset).
- No new primary data; conclusions rely on consensus across the cited literature.
- Tables 1-5 are select examples, not systematic; bias toward 2018-2024 publications.

## Open questions

### Open questions raised by authors
- When and how does a mutant cell reach the tipping point of irreversible commitment to cancer?
- Why does the same driver mutation produce vastly different outcomes across mice or patients?
- Can early-detection strategies validated in models translate to humans?
- How can AI black-box models be made interpretable enough for clinical validation?

### Open questions identified during ingest
- For solid tumours without clinically defined precursor lesions, what minimal molecular signature can mark "precancerous cells" in single-cell atlases?
- Is the immune surveillance-to-evasion switch reversible by current ICI or by pre-CAF/senescent-cell-targeted interception?
- Does ecDNA emergence have an analogue in cancers other than EAC?

## My take
This is the canonical 2024 synthesis to anchor any early-cancer / cancer-interception thread in the wiki. It is most useful as a methodology map: it crisply lays out which tools (GEMMs vs organoids vs human samples vs AI), which markers (TP53/KRAS/APC/MYC and milestone reporters), and which microenvironmental axes (pre-CAFs, Treg conversion, senescent macrophages) one must consider. For the thesis it provides framing for any work on the precancer-to-cancer transition and for milestone-reporter strategies. The "tipping point" framing is conceptually appealing but operationally fuzzy — the milestone-reporter list is currently an empirical zoo rather than a coherent theory.

## Related
- [[concepts/precancerous-lesion-malignant-transformation]]
- [[concepts/cancer-initiating-cell-cell-origin]]
- [[concepts/field-cancerization-clonal-expansion-normal-tissue]]
- [[concepts/event-based-lineage-tracing-milestone-reporters]]
- [[concepts/ecdna-precancer-malignant-progression]]
- [[concepts/pre-cafs-cancer-associated-fibroblasts-premalignant]]
- [[concepts/immune-surveillance-evasion-precancer-transition]]
- [[concepts/carcinogenesis-tipping-point-irreversibility]]
- [[concepts/organoid-cancer-initiation-3d-model]]
- [[concepts/autochthonous-mouse-models-early-cancer]]
- [[concepts/stem-like-cells-precancerous-lesions]]
- [[concepts/senescent-cells-promote-early-tumorigenesis]]
- [[foundations/kras-oncogene]]
- [[foundations/apc-tumor-suppressor]]
- [[foundations/tp53-tumor-suppressor]]
- [[foundations/cdkn2a-tumor-suppressor]]
- [[foundations/myc-oncogene]]
- [[foundations/pten-tumor-suppressor]]
- [[foundations/brca1-tumor-suppressor]]
- [[foundations/brca2-tumor-suppressor]]
- [[foundations/gemm-genetically-engineered-mouse-model]]
- [[foundations/organoid-3d-tissue-culture]]
- [[foundations/panin-pancreatic-intraepithelial-neoplasia]]
- [[foundations/ecdna-extrachromosomal-dna]]
- [[foundations/akaluc-akalumine-bioluminescent-system]]
- [[foundations/cre-loxp-recombinase-system]]
- [[foundations/4nqo-carcinogen]]
- [[foundations/den-diethylnitrosamine-carcinogen]]
- [[foundations/dmba-carcinogen]]
- [[foundations/infercnv-cnv-scrna]]
- [[foundations/red2onco-multicolour-reporter]]
- [[foundations/intravital-microscopy-multiphoton]]
- [[foundations/barretts-oesophagus]]
- [[foundations/atac-seq]]
- [[foundations/chip-seq]]
- [[foundations/scrna-seq-10x-chromium]]
- [[people/ran-zhou]]
- [[people/xiwen-tang]]
- [[people/yuan-wang]]
