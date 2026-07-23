---
# === Identification ===
title: "Functional Genetic Screens Reveal Key Pathways Instructing the Molecular Phenotypes of Tumor-Associated Macrophages"
slug: "functional-genetic-screens-reveal-key-pathways"
arxiv: ""
doi: "10.1158/2326-6066.CIR-25-0488"
pmid: "40906823"
venue: "Cancer Immunology Research"
year: 2025
authors: ["Youxue Lu", "Ce Luo", "Lanxiang Huang", "Gengyi Wu", "Lihan Zhong", "Jieyu Chu", "Fubing Wang", "Zexian Zeng", "Deng Pan"]
first_author: "Youxue Lu"
corresponding_author: "Deng Pan; Zexian Zeng; Fubing Wang"

# === Source & metadata ===
source_type: pdf
s2_id: "3cb6bdb7d04c92080704c1d38a2b724c54141d29"
date_added: 2026-07-23
ingested_date: 2026-07-23
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - tumor-associated-macrophage
  - macrophage-polarization
  - CRISPR-screen
  - CROP-seq
  - spatial-multiomics
  - hypoxia
  - lactic-acid
  - PGE2
  - GM-CSF
  - MHC-II
  - interferon-stimulated-genes
  - cancer-immunotherapy
keywords:
  - LGP factors
  - angiogenic TAM
  - MHC-II TAM
  - ISG TAM
  - Adar
  - anti-PD-1
domain: "oncology"

# === Biomedical domain ===
tissue: [lung, breast, colon, skin, pancreas, multi]
condition: [cancer]
disease_specific: [lung_adenocarcinoma, melanoma, colorectal_cancer, breast_cancer, pancreatic_cancer]
species: [both]
hypoxia_relevant: true
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [CRISPR_screen, CROP-seq, bulk_RNA-seq, scRNA-seq, ATAC-seq, spatial_visium, spatial_metabolomics_AFADESI-MSI, flow_cytometry, immunofluorescence]
n_samples: 25
n_cells_total: 47856
integration_method: "Harmony"

# === Biology captured ===
key_cell_types:
  - tumor-associated macrophage
  - angiogenic TAM
  - MHC-II+ TAM
  - ISG+ TAM
  - lipid-associated TAM
  - bone-marrow-derived macrophage
  - tumor-educated macrophage
  - CD8+ T cell
key_markers:
  - VEGFA
  - ARG1
  - CD74
  - CIITA
  - CX3CR1
  - HIF1A
  - LDHA
  - PTGS2
  - CSF2
  - PTGER4
  - CSF2RA
  - ADAR
  - CXCL10
  - CD40
  - ISG15
  - SLC2A1
key_pathways:
  - hypoxia / HIF-1α signaling
  - glycolysis
  - MHC-II antigen presentation
  - type-I interferon / ISG response
  - GM-CSF signaling
  - PGE2 / COX2 signaling
  - fatty acid oxidation

# === User project membership ===
projects: [thesis, hypoxia]
priority: core
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: candidate
exclusion_reason:
data_availability: "GEO GSE237788, GSE269031; Zenodo 16945965; code github.com/zenglab-pku/TAM_paper"

# === Cross-references ===
code_url: "https://github.com/zenglab-pku/TAM_paper"
cited_by: []
---

## Problem

Tumor-associated macrophages (TAMs) display remarkable functional heterogeneity, and while single-cell studies have catalogued many phenotypes (angiogenic/SPP1+, MHC-II+/C1QC+, ISG+, lipid-associated), it remains unclear **which tumor-microenvironmental factors instruct which phenotype**, and whether any conserved logic governs TAM polarization across cancers. The M1/M2 paradigm is insufficient. Large-scale genetic dissection of TAMs is technically hard because primary macrophages resist screening.

## Key idea

Using an ex vivo **tumor-educated macrophage (TEM)** model amenable to CRISPR screening, the authors identify three tumor-derived factors — **lactic acid, GM-CSF, and PGE2 ("LGP")** — that combinatorially instruct TAM fate. Lactic acid + PGE2 cooperatively drive an angiogenic program and, antagonizing GM-CSF, suppress the MHC-II program at the chromatin level, producing two **mutually exclusive** TAM phenotypes that segregate into distinct metabolic spatial niches. A third, therapeutically desirable **ISG+** state can be forced by knocking out the RNA-editing enzyme **Adar**, boosting antitumor CD8+ T-cell immunity.

## Method

- **Pan-cancer scRNA-seq re-analysis**: 35,282 macrophages, 108 samples, 15 cancer types (Cheng et al. atlas), re-integrated with scVI, signature scoring by AUCell/decoupler.
- **Patient validation**: FACS of VEGFA vs MHC-II in 23 fresh breast/colon/lung tumors; TCGA survival analysis (LUAD/CESC/SKCM).
- **TEM model + ex vivo CRISPR screen**: BMDMs from Cas9 mice educated with 4T1 TCM; pooled library of ~10,200 sgRNAs / 2,245–2,425 genes; ARG1-negative sort; MAGeCK analysis.
- **Factor reconstitution**: recombinant lactate (25 mmol/L), GM-CSF (2 ng/mL), PGE2 (100 nmol/L), single/paired/triple; bulk RNA-seq + ATAC-seq (HOMER motifs); Cox2-KO / Csf2-KO / Ldha-Cox2 dKO tumor lines.
- **In vivo CROP-seq**: myeloid-Cas9 (LSL-Cas9;Lyz2-Cre) HSC transplant, LLC challenge, 47,856 TAMs, Harmony integration, genotype–phenotype mapping.
- **Spatial multiomics**: pimonidazole hypoxia staining (4T1/LLC/MC38); Visium CytAssist transcriptomics + AFADESI-MSI metabolomics in 2 human NSCLC, integrated by MultiVI + CellCharter + Cell2location.
- **ISG/Adar arm**: myeloid Adar-KO mice, LLC/B16F10 growth ± anti–PD-1, scRNA-seq, CellPhoneDB myeloid–T interaction, CD8 exhaustion/effector FACS.

## Results

The angiogenic and MHC-II programs are anticorrelated and conserved pan-cancer, and mutually exclusive at protein and chromatin levels. TCM drives the angiogenic/hypoxia program while suppressing MHC-II/IFN. The screen nominates Hif1a, Ptger4, Csf2ra, Adar, Trim28, Spi1/Rreb1/Rbpj, Lamtor1/Flcn, and SWI/SNF. Reconstitution shows only **L+G+P together** recapitulate the angiogenic phenotype; LP cooperate on glycolysis/hypoxia genes and antagonize GM-CSF's MHC-II program (closing ETS-motif chromatin). In vivo, tumor Ldha/Cox2 dKO shifts TAMs toward MHC-II; Hif1a-KO enriches MHC-II TAMs. Angiogenic TAMs are pimonidazole+ (hypoxic niche); MHC-II TAMs are normoxic with active FAO. Only the **ISG signature** correlates with effector CD8+ T cells; myeloid **Adar-KO** expands ISG+ TAMs, slows LLC/B16F10 growth, synergizes with anti–PD-1, and enhances CXCL10–CXCR3 / CD40–CD40L crosstalk while reducing CD8 exhaustion.

## All claims (exhaustive)

- `[c1]` Angiogenic and MHC-II TAM programs are mutually exclusive and conserved pan-cancer `(p.2063)` "our analysis suggests that the mutually exclusive nature of angiogenic and MHC-II programs is a widely conserved feature in TAMs" — confidence: high — type: mechanistic — links: [[claims/angiogenic-mhc-ii-tam-programs-mutually]] [[concepts/angiogenic-mhc-ii-tam-mutual-exclusivity]] [[concepts/pan-cancer-tam-atlas-23-clusters]]
- `[c2]` VEGFA and MHC-II are mutually exclusive in patient TAMs by FACS `(p.2063)` "flow cytometric validation in 23 patient-derived breast, colon, and lung cancer samples confirmed that VEGFA (angiogenic) and MHC-II were mutually exclusive in TAMs" — confidence: high — type: correlational — links: [[claims/vegfa-mhc-ii-mutually-exclusive-patient]] [[concepts/angiogenic-mhc-ii-tam-mutual-exclusivity]] [[foundations/ciita-mhc-ii-transactivator]]
- `[c3]` MHC-II TAM programs associate with better survival, angiogenic with worse (TCGA) `(p.2063)` "MHC-II programs were associated with better survival, whereas angiogenic programs showed the opposite effect" — confidence: low — type: correlational — links: [[claims/mhc-ii-tam-programs-associate-better]] [[concepts/angiogenic-mhc-ii-tam-mutual-exclusivity]]
- `[c4]` Tumor-conditioned media induce angiogenic/hypoxia genes and suppress MHC-II/IFN in macrophages `(p.2063)` "Bulk RNA-seq of these TEMs revealed significant upregulation of genes associated with hypoxia and angiogenesis ... genes involved in MHC-II ... and interferon responses ... were substantially downregulated" — confidence: high — type: mechanistic — links: [[claims/tumor-conditioned-media-induce-angiogenic-hypoxia]] [[foundations/bone-marrow-derived-macrophage-bmdm]] [[foundations/arg1-arginase-1]]
- `[c5]` Lactic acid + GM-CSF + PGE2 together are necessary and sufficient for angiogenic ARG1 polarization `(p.2064)` "when BMDMs were co-treated with the combination of lactic acid, GM-CSF, and PGE2, but not with any two factors alone, ARG1 expression reached levels comparable with those in TEMs" — confidence: high — type: mechanistic — links: [[claims/lactic-acid-gm-csf-pge2-together]] [[concepts/lgp-factor-tam-polarization-axis]] [[foundations/arg1-arginase-1]]
- `[c6]` Tumor-derived PGE2 and GM-CSF (Cox2/Csf2) are required for the angiogenic TEM phenotype `(p.2064)` "conditioned media from these KO cells failed to induce ARG1 expression in TEMs ... tumor-secreted PGE2 and GM-CSF are essential" — confidence: high — type: mechanistic — links: [[claims/tumor-derived-pge2-gm-csf-required]] [[concepts/lgp-factor-tam-polarization-axis]] [[foundations/ptgs2-cox2]] [[foundations/gm-csf-cytokine]]
- `[c7]` Lactate + PGE2 cooperatively induce glycolysis/hypoxia angiogenic genes `(p.2065)` "PGE2 and lactic acid cooperatively induced genes related to glycolysis and hypoxia pathways (e.g., Arg1, Vegfa, and Slc2a1)" — confidence: high — type: mechanistic — links: [[claims/lactate-pge2-cooperatively-induce-glycolysis-hypoxia]] [[concepts/lactate-driven-tam-m2-polarization]] [[foundations/hif1a]]
- `[c8]` Lactate + PGE2 antagonize GM-CSF to repress MHC-II genes (581/474 of 969) `(p.2065)` "among GM-CSF-induced genes (n = 969), lactic acid and PGE2 downregulated the majority (581 and 474, respectively), including MHC-II-associated genes (e.g., Cd74 and Ciita)" — confidence: high — type: quantitative — links: [[claims/lactate-pge2-antagonize-gm-csf-repress]] [[concepts/lgp-factor-tam-polarization-axis]] [[foundations/ciita-mhc-ii-transactivator]]
- `[c9]` GM-CSF + lactic acid cooperatively induce ISGs `(p.2065)` "GM-CSF and lactic acid cooperatively induced many ISGs, such as Ifi44, Ifi209, and Mx1" — confidence: medium — type: mechanistic — links: [[claims/gm-csf-lactic-acid-cooperatively-induce]] [[concepts/adar-isg-tam-reprogramming-antitumor]]
- `[c10]` CRISPR screen identifies Hif1a, Ptger4, Csf2ra, Adar, SWI/SNF etc. as angiogenic regulators `(p.2064)` "The screen revealed enriched regulators, including transcription factors ... hypoxia components (Hif1a) ... and immune modulators (Adar, Trim28, Ptger4, and Csf2ra)" — confidence: high — type: methodological — links: [[claims/crispr-screen-identifies-hif1a-ptger4-csf2ra]] [[foundations/mageck-crispr-screen-analysis]] [[foundations/hif1a]] [[foundations/spi1-pu1-master-tf]]
- `[c11]` Lactate + PGE2 close GM-CSF-induced ETS-family motif open chromatin `(p.2066)` "LP treatment strongly suppressed chromatin sites associated with ETS family ... selectively repress a subset of ETS-regulated genes that are activated by GM-CSF" — confidence: medium — type: mechanistic — links: [[claims/lactate-pge2-close-gm-csf-induced]] [[foundations/atac-seq]] [[foundations/homer-motif-enrichment-analysis]]
- `[c12]` MHC-II TAMs carry far more accessible chromatin (27,578 vs 3,979) — a permissive, plastic state `(p.2066)` "n = 27,578 were more accessible in MHC-II+ TAMs ... whereas only a limited set (n = 3,979) ... in angiogenic TAMs" — confidence: medium — type: quantitative — links: [[claims/mhc-ii-tams-carry-far-more]] [[foundations/atac-seq]] [[concepts/angiogenic-mhc-ii-tam-mutual-exclusivity]]
- `[c13]` In vivo CROP-seq: Hif1a-KO enriches MHC-II TAMs; Ppp2r3c-KO enriches proliferating TAMs `(p.2067)` "knockout of Hif1a ... enriched MHC-II TAMs in vivo ... Knockout of Ppp2r3c ... significantly enhanced proliferating macrophages" — confidence: medium — type: mechanistic — links: [[claims/vivo-crop-seq-hif1a-knockout-enriches]] [[foundations/crop-seq-crispr-droplet-sequencing]] [[foundations/hif1a]]
- `[c14]` Tumor Ldha/Cox2 double-KO increases MHC-II and decreases angiogenic TAMs in vivo `(p.2067)` "dKO tumors showed increased MHC-II+ TAMs and decreased angiogenic (CX3CR1MHC-II) TAMs ... tumor-intrinsic LP production critically dictates TAM subsets" — confidence: high — type: mechanistic — links: [[claims/tumor-ldha-cox2-double-knockout-increases]] [[concepts/lgp-factor-tam-polarization-axis]] [[foundations/ldh-lactate-dehydrogenase]] [[foundations/ptgs2-cox2]]
- `[c15]` Angiogenic TAMs reside in hypoxic (pimonidazole+) niches; MHC-II TAMs in normoxic areas `(p.2070)` "only the angiogenic (CX3CR1MHC-II) TAMs, not the MHC-II+ TAMs, stained positively with the hypoxia probe ... angiogenic TAMs reside in hypoxic niches, whereas MHC-II+ TAMs are found in normoxic areas" — confidence: high — type: mechanistic — links: [[claims/angiogenic-tams-reside-hypoxic-pimonidazole-positive]] [[concepts/metabolic-niche-partitioning-tam-phenotype]] [[foundations/pimonidazole-hypoxia-probe]]
- `[c16]` Spatial multiomics links FAO metabolites to MHC-II niches and lactate/prostaglandins to angiogenic niches `(p.2071)` "the angiogenic TAM niches also showed increased levels of glycolysis products like lactic acid and high concentrations of prostaglandins (PGA1 and PGE2)" — confidence: medium — type: correlational — links: [[claims/spatial-multiomics-links-fao-metabolites-mhc]] [[concepts/metabolic-niche-partitioning-tam-phenotype]] [[foundations/afadesi-msi-spatial-metabolomics]] [[foundations/multivi-multimodal-integration]] [[foundations/cellcharter-framework]]
- `[c17]` ISG TAM signature correlates with effector CD8+ T-cell signature across cancers `(p.2071)` "the ISG signature in TAMs consistently exhibited a high correlation with the effector signature in T cells across multiple cancer types" — confidence: medium — type: correlational — links: [[claims/isg-tam-signature-correlates-effector-cd8]] [[concepts/adar-isg-tam-reprogramming-antitumor]]
- `[c18]` Myeloid Adar-KO expands ISG+ TAMs, slows tumor growth, enhances anti–PD-1 `(p.2071)` "Adar mKO mice exhibited significantly slower tumor growth ... enhanced the efficacy of anti-PD-1 treatment" — confidence: high — type: pharmacological — links: [[claims/myeloid-adar-knockout-expands-isg-tams]] [[concepts/adar-isg-tam-reprogramming-antitumor]] [[foundations/adar-rna-editing-enzyme]]
- `[c19]` Adar-mKO enhances CXCL10–CXCR3 and CD40–CD40L crosstalk and reduces CD8 exhaustion `(p.2072)` "fewer exhausted (LAG3+ PD-1+) and more cytotoxic (GZMB+) CD8+ T cells in Adar mKO tumors compared with controls" — confidence: medium — type: mechanistic — links: [[claims/adar-myeloid-knockout-enhances-cxcl10-cxcr3]] [[foundations/adar-rna-editing-enzyme]] [[foundations/cellphonedb-ligand-receptor]]

## Discussion captured

### Authors' interpretation

The authors argue the angiogenic/MHC-II mutual exclusivity **unifies prior marker-based TAM classifications** (SPP1+/C1Q+ vs PTGS2+/C1Q+) into one conserved framework. They interpret LGP factors as a "core regulatory axis" acting at multiple levels (receptor, TF, chromatin), and read the chromatin data as showing MHC-II+ TAMs are in a more "permissive"/plastic state retaining reprogramming potential. They frame ISG+ reprogramming via Adar loss as an actionable immunotherapy strategy.

### Comparisons with prior literature (made by authors)

- Colegio et al. 2014 *Nature* (ref 28) — tumor-derived lactic acid → HIF-1α → Arg1; the authors extend this by showing lactate is necessary but not sufficient.
- Cheng et al. 2021 *Cell* (ref 7) — pan-cancer myeloid atlas used as the human signature source.
- Cortese et al. 2023 *Cancer Immunol Res* (ref 25) — independently found spatially segregated TAM subsets in colorectal cancer, supporting the model.
- Wang et al. 2022 *Nat Commun* (ref 40) — STING agonism induces a similar ISG TAM phenotype.
- Bill et al. 2023 *Science* (ref 41) — CXCL9/10+ TAMs co-localize with IFNγ+ T cells, offering a mechanism for ISG+ TAM benefit.

### Mechanistic hypotheses proposed

- LP selectively represses ETS-regulated genes activated by GM-CSF at the chromatin level (p.2066).
- Metabolic geography (hypoxia/lactate vs oxygen/FAO) supplies the LGP combinations that locally determine TAM fate (p.2071).
- A closer ISG+↔angiogenic trajectory relationship may explain why angiogenic TAMs also rose in Adar-mKO tumors (p.2072).

### Caveats and self-criticism

- Single-receptor knockouts only modestly shift the MHC-II/angiogenic ratio because lactate and PGE2 signal through multiple redundant receptors (p.2067).
- Current spatial transcriptomics could not detect GM-CSF, requiring higher-resolution methods (e.g. MERFISH) for future validation (p.2071).
- TEMs were used because large-scale CRISPR screens of TAMs are technically limited (p.2071).

### Future directions suggested

- Higher-resolution spatial validation (MERFISH) of niche boundaries and GM-CSF localization.
- ISG+ reprogramming via Adar inactivation as a TAM-targeting immunotherapy.
- Extending the LGP core to additional cytokines/metabolites (TNFα, succinate) and TAM subtypes (FOLR2+, TREM2+).

## Limitations

- Screening relied on an ex vivo TEM surrogate rather than bona fide in vivo TAMs.
- Human spatial multiomics rests on only two NSCLC patients; ~100 µm metabolomics resolution.
- Survival associations use bulk-signature proxies in modest TCGA cohorts (SKCM n=97).
- Myeloid Adar loss tested only via HSC-transplant chimeras in two mouse models; systemic ADAR inhibition is interferon-toxic.

## Open questions

### Open questions raised by authors

- How are metabolic inputs transduced to CIITA/MHC-II-locus chromatin closure?
- Is TAM phenotype commitment reversible at the single-cell level in vivo?
- Would relieving tumor hypoxia re-partition TAM phenotypes as the model predicts?

### Open questions identified during ingest

- Does myeloid ADAR inhibition have a viable therapeutic window given interferon toxicity?
- Do the LGP dose–combination rules generalize to human TAMs in situ?
- How does the ISG+ state relate mechanistically to the angiogenic state (the observed paradoxical co-increase)?

## My take

This is a genuinely integrative TAM paper: it couples loss-of-function genetics (ex vivo screen, in vivo CROP-seq, tumor-intrinsic enzyme KOs) with gain-of-function reconstitution (recombinant L+G+P) and closes the loop spatially (pimonidazole + paired spatial transcriptomics/metabolomics). For a hypoxia-and-macrophage thesis it is directly load-bearing: it gives a mechanistic, chromatin-level account of why hypoxic-niche TAMs are angiogenic/immunosuppressive and normoxic TAMs are antigen-presenting, and it upgrades the classic "lactate → M2" story into a combinatorial LGP model. The ISG/Adar arm is the most translationally provocative but also the most preliminary. Weakest links: two-patient human spatial data and bulk-proxy survival.

## Related

**Concepts**: [[concepts/lgp-factor-tam-polarization-axis]] · [[concepts/angiogenic-mhc-ii-tam-mutual-exclusivity]] · [[concepts/adar-isg-tam-reprogramming-antitumor]] · [[concepts/metabolic-niche-partitioning-tam-phenotype]] · [[concepts/lactate-driven-tam-m2-polarization]]

**Foundations (methods)**: [[foundations/mageck-crispr-screen-analysis]] · [[foundations/crop-seq-crispr-droplet-sequencing]] · [[foundations/atac-seq]] · [[foundations/homer-motif-enrichment-analysis]] · [[foundations/pimonidazole-hypoxia-probe]] · [[foundations/afadesi-msi-spatial-metabolomics]] · [[foundations/multivi-multimodal-integration]] · [[foundations/cellcharter-framework]] · [[foundations/cellphonedb-ligand-receptor]] · [[foundations/cell2location-deconvolution]] · [[foundations/aucell-gene-set-activity]] · [[foundations/decoupler-activity-inference]] · [[foundations/scanpy]] · [[foundations/harmony-integration]] · [[foundations/scvi-deep-generative-model]] · [[foundations/10x-visium-spatial-transcriptomics]] · [[foundations/msigdb-hallmark-hypoxia]] · [[foundations/bone-marrow-derived-macrophage-bmdm]]

**Foundations (biology)**: [[foundations/hif1a]] · [[foundations/arg1-arginase-1]] · [[foundations/gm-csf-cytokine]] · [[foundations/pge2-prostaglandin-e2]] · [[foundations/ptgs2-cox2]] · [[foundations/ldh-lactate-dehydrogenase]] · [[foundations/spi1-pu1-master-tf]] · [[foundations/ciita-mhc-ii-transactivator]] · [[foundations/adar-rna-editing-enzyme]]

**People**: [[people/youxue-lu]] · [[people/ce-luo]] · [[people/deng-pan]] · [[people/zexian-zeng]] · [[people/fubing-wang]]
