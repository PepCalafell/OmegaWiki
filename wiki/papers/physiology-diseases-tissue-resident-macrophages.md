---
# === Identification ===
title: "Physiology and diseases of tissue-resident macrophages"
slug: physiology-diseases-tissue-resident-macrophages
arxiv: ""
doi: "10.1038/s41586-023-06002-x"
pmid: "37344646"
venue: "Nature"
year: 2023
authors:
  - "Tomi Lazarov"
  - "Sergio Juarez-Carreño"
  - "Nehemiah Cox"
  - "Frederic Geissmann"
first_author: "Tomi Lazarov"
corresponding_author: "Frederic Geissmann"

# === Source & metadata ===
source_type: pdf
s2_id: "a3274c9f33139edd6e7b31f68348c0fa93443274"
date_added: 2026-05-06
ingested_date: 2026-05-08
ingest_version: 2
last_reviewed: null

# === Classification ===
importance: 5
tier: TIER_1
tags:
  - macrophage
  - tissue-resident-macrophage
  - immunology
  - developmental-biology
  - haematopoiesis
  - microglia
  - kupffer-cell
  - alveolar-macrophage
  - osteoclast
  - efferocytosis
  - macrophage-niche
  - dementia
  - alzheimers
  - lysosomal-storage-disease
  - cancer
  - review
keywords:
  - tissue-resident macrophage
  - yolk-sac EMP origin
  - PreMacs
  - lineage-determining factor LDF
  - SALL1 microglia
  - PPARG alveolar
  - SPI-C red pulp
  - GATA6 peritoneal
  - ID3 Kupffer
  - CSF1R / IL-34 / CSF2 trophic axis
  - PRR pattern recognition receptor
  - efferocytosis
  - TIM4 / MERTK / TAM receptor
  - MFGE8 GAS6 protein S
  - microglia synaptic pruning
  - C1Q complement
  - BDNF microglia
  - Kupffer cell iron recycling
  - ferroportin
  - PDGF-CC adipose lipid storage
  - TREM2 Alzheimer
  - Nasu-Hakola disease
  - osteopetrosis CSF1R TREM2
  - lysosomal storage disease Gaucher
  - SIRPa-CD47 don't-eat-me
  - macrophage as ancillary cell
domain: "immunology / developmental biology / cell biology"

# === Biomedical domain ===
tissue:
  - liver
  - lung
  - bone_marrow
  - blood
  - skin
  - kidney
  - pancreas
  - multi
condition:
  - healthy
  - cancer
  - autoimmune
  - inflam_precancer
disease_specific:
  - ALSP_leukoencephalopathy
  - Nasu-Hakola_disease
  - Alzheimers_disease
  - Gaucher_disease
  - osteopetrosis
  - paediatric_onset_leukoencephalopathy
  - alveolar_proteinosis
  - systemic_lupus_erythematosus
  - obesity
  - lipodystrophy
species:
  - human
  - mouse
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques:
  - review
  - synthesis
n_samples: null
n_cells_total: null
integration_method: ""

# === Biology captured ===
key_cell_types:
  - tissue_resident_macrophage_TRM
  - microglia
  - kupffer_cell
  - alveolar_macrophage
  - large_peritoneal_macrophage
  - small_peritoneal_macrophage
  - red_pulp_macrophage
  - osteoclast
  - langerhans_cell
  - WAT_resident_macrophage
  - fat_associated_macrophage
  - kidney_macrophage
  - bone_marrow_derived_macrophage_BMDM
  - inflammatory_monocyte
  - PreMac
  - yolk_sac_EMP
  - HSC
key_markers:
  - CSF1R
  - CSF1
  - IL-34
  - CSF2
  - PU.1
  - cMAF
  - IRF8
  - SALL1
  - PPARG
  - SPI-C
  - GATA6
  - ID3
  - CCR2
  - TREM2
  - DAP12
  - TYROBP
  - TIM4
  - MERTK
  - TYRO3
  - AXL
  - MFGE8
  - GAS6
  - C1Q
  - SIRPA
  - CD47
  - HIF1A
  - HIF2A
  - PDGF-CC
  - BDNF
  - IGF1
  - TGFβ
  - VEGF-A
  - VEGF-C
  - ferroportin
  - NFATC1
  - RANKL
  - CSF1R-DAP12
  - SLC6A2
key_pathways:
  - CSF1R-signaling
  - IL-34-CSF1R
  - CSF2-CSF2R-PPARG
  - efferocytosis-PtdSer-TAM
  - complement-C1Q-synapse-pruning
  - TGFβ-niche-instruction
  - PDGF-CC-adipose-lipid-storage
  - SIRPα-CD47-don-t-eat-me
  - HIF-VEGF-angiogenesis
  - PRR-TLR-NLR-RLR-ALR-CLR
  - MERTK-TAM-receptor
  - osteoclast-NFATC1-RANKL
  - Kupffer-iron-recycling-ferroportin

# === User project membership ===
projects:
  - thesis
  - hypoxia
priority: core
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: included
exclusion_reason: null
data_availability: ""

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Decades of work have characterized macrophages as innate immune cells with phagocytic and inflammatory functions, yet a body of evidence accumulating since 2010 has reframed them as a developmentally and functionally heterogeneous set of cells. In particular, embryo-derived tissue-resident macrophages (TRMs) — distinct from haematopoietic stem cell (HSC)-derived monocytes and bone marrow-derived macrophages (BMDMs) — establish stable, life-long associations with specialized parenchymal cells in nearly every tissue. Their roles in tissue growth, remodelling, metabolism, and homeostasis remain incompletely systematized, and the connection between TRM dysfunction (genetic or environmental) and human diseases including dementias, lysosomal storage disorders, autoimmunity, metabolic disease, and cancer is only beginning to be charted. The review aims to provide a unifying conceptual outline of TRM biology so that origin, niche, function, and disease can be reasoned about together.

## Key idea

TRMs are an **ancillary cell type** — developmentally and functionally distinct from HSC-derived monocytes/BMDMs — that arise from yolk-sac erythro-myeloid progenitors (EMPs), colonize tissues during organogenesis, and persist by local self-renewal. Their identity is jointly encoded by core macrophage transcription factors (PU.1, cMAF, IRF8) and tissue-specific lineage-determining factors (LDFs, e.g. SALL1 microglia, ID3 Kupffer, PPARγ alveolar, SPI-C red pulp, GATA6 peritoneal), with niche signals (TGFβ, IL-34, CSF1, CSF2, retinoic acid, desmosterol/LXRα, haem) instructing the program. Once specified, TRMs sense local physiological signals (pH, osmolarity, hypoxia, mechanical stress, fatty acids, ECM, apoptotic cells, microbes) via a broad sensor repertoire (PRRs, TAM receptors, TIM4, integrins, GPCRs, ion channels) and execute *ancillary* functions for the tissue: nutrient recycling, ECM remodelling, growth-factor production, efferocytosis, and selective phagocytosis. Genetic or environmental disruption of these functions causes a spectrum of human diseases — neurodegenerative (ALSP, Nasu-Hakola, Alzheimer's), skeletal (osteopetrosis), pulmonary (alveolar proteinosis), metabolic (lipodystrophy, obesity-associated insulin resistance), autoimmune (lupus, glomerulonephritis), and oncological (organ-specific TRM tumour control vs BMDM-driven tumour promotion). The conceptual upshot: "macrophage" should not be treated as a single cell type, and disease mechanisms should be parsed at the level of specific TRM subsets and their niches.

## Method

This is a Nature *Review* article, not primary research. The authors:

- Synthesize fate-mapping, parabiosis, and lineage-tracing literature establishing the EMP yolk-sac origin of TRMs and their HSC-independence.
- Curate cell-intrinsic LDFs and niche-derived instructive signals from the past decade of macrophage transcriptomics and epigenomics (Lavin 2014, Gosselin 2014, Mass 2016, Sakai 2019, Guilliams 2022).
- Present a tissue-by-tissue catalogue of TRM identity, function, and disease (microglia, Kupffer, alveolar, kidney, peritoneal, splenic, osteoclasts, fat, gut).
- Build two synthesis figures: Fig. 1 macrophage ontogeny + tissue-specific LDFs/niche signals; Fig. 2 sensor-effector repertoire (PRRs, metabolite sensors, mechanosensors, fitness sensors); Fig. 3 physiological roles ↔ associated disease processes.
- Frame the proposed conceptual model: TRMs are *ancillary* cells, paired one-to-one with specialized parenchymal cell types.

## Results

Because this is a synthesis, "results" are the major conclusions the authors crystallize from the cited literature; the atomic claims are itemised in `## All claims (exhaustive)`. Highlights:

1. **Three haematopoietic waves** define vertebrate myelopoiesis: primitive (yolk-sac, RUNX1-independent), EMP (yolk-sac, RUNX1+ MYB- NOTCH1-), and definitive HSC (intra-embryonic AGM, RUNX1+ MYB+ NOTCH1+). EMPs give rise to nearly all adult TRMs; HSCs give rise to monocytes/BMDMs and to gut lamina-propria macrophages.
2. **Tissue specification** is jointly cell-intrinsic (stochastic LDF expression in PreMacs) and niche-instructive (TGFβ, IL-34, retinoic acid, desmosterol, haem, CSF2). The authors *favour a stochastic model with niche-mediated selection* over a purely instructive model.
3. **CSF1/IL-34/CSF2 axis** controls macrophage development and survival via CSF1R and CSF2R; tissue-specific dependencies (Langerhans cells/microglia depend on IL-34 not CSF1; alveolar macrophages depend on CSF2).
4. **TRMs self-renew locally** and persist for years (mouse parabiosis, human transplant) with negligible BMDM replacement under homeostasis. Inflammation recruits BMDMs but does not necessarily replace TRMs (microglia after EAE, Kupffer cells after stress).
5. **TRMs are ancillary support cells** — paired with specialized parenchymal cells (microglia↔neurons, osteoclasts↔osteoblasts, fat-resident macs↔white adipocytes, Kupffer↔hepatocytes, alveolar macs↔type II pneumocytes).
6. **TRM = restorative, BMDM = pro-fibrotic** dichotomy in tissue repair across liver, heart, kidney, lung; CCR2-deficient mice (lacking monocytes) have milder fibrosis.
7. **Microglia mediate developmental synaptic pruning** via complement (C1Q) and produce BDNF for motor-learning-dependent synapse formation and neuropathic pain.
8. **Kupffer cells recycle iron** from senescent erythrocytes via ferroportin-mediated export; BMDMs transiently take over under high iron-recycling demand.
9. **Adipose TRMs control lipid storage** in white adipocytes via diet-regulated PDGF-CC; loss redirects energy to brown adipose tissue (thermogenic dissipation).
10. **TRM-encoded genetic diseases** include ALSP (CSF1R hypomorph), paediatric-onset leukoencephalopathy (CSF1R bi-allelic LOF), Nasu-Hakola (TREM2/DAP12 LOF), osteopetrosis (TCIRG1/CLCN7/RANKL/TREM2/CSF1R), Gaucher and other LSDs (lysosomal hydrolase LOF), alveolar proteinosis (CSF2/CSF2R/PPARG LOF), and TREM2-polymorphism Alzheimer's risk.
11. **Cancer** — Kupffer cells limit liver-localized tumour growth; BMDM-derived TAMs in tumour niches promote growth. SIRPα-CD47 axis is a therapeutic target.
12. **PRR taxonomy** — five families (TLRs, NLRs, RLRs, ALRs, CLRs) detect pathogens; output cascades produce TNF/IL-1/IL-6/type-I IFN and trigger phagocytosis.
13. **Efferocytosis** — TIM4 and TAM receptors (TYRO3/AXL/MERTK) with bridging molecules MFGE8/GAS6/protein S/C1Q sense PtdSer; engulfment yields anti-inflammatory output (TGFβ/IL-10/PGE2). C1Q LOF predisposes to lupus and glomerulonephritis.

## All claims (exhaustive)

Atomic claims, each with page (PDF), exact quote, confidence, type, and links. TIER_1 review → 22 claims.

- `[c01]` TRMs originate primarily from yolk-sac EMPs in mammals (p.698) "Embryo-derived tissue-resident macrophages are the first representatives of the haematopoietic lineage to emerge in metazoans. In mammals, resident macrophages originate from early yolk sac progenitors and are specified into tissue-specific subsets during organogenesis" — confidence: high — type: mechanistic — links: [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]] [[claims/trms-originate-yolk-sac-emps-mammals]]
- `[c02]` EMP-derived PreMacs colonize the embryo concurrently with organogenesis and before HSC emergence (p.699) "EMP-derived macrophage precursors (PreMacs) colonize the entire embryo and differentiate into tissue-resident macrophages concurrently with the onset of organogenesis, before the emergence of HSCs" — confidence: high — type: mechanistic — links: [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]] [[claims/emp-derived-premacs-colonize-embryo-before]]
- `[c03]` HSC-derived macrophages are short-lived and depend on circulating monocytes for renewal, contrasting with self-renewing TRMs (p.699) "resident macrophages are long-lived cells that self-renew locally in tissues, whereas HSC-derived macrophages are short-lived, rely on circulating monocytes for their renewal, and can massively expand upon challenge" — confidence: high — type: mechanistic — links: [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]] [[claims/hsc-derived-macrophages-short-lived-monocyte]]
- `[c04]` Gut lamina propria is populated by HSC- and BMDM-derived macrophages (notable exception to TRM dominance) (p.699) "the gut lamina propria is populated by HSCs and bone marrow monocyte-derived macrophages (BMDMs) which may self-maintain" — confidence: high — type: mechanistic — links: [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]] [[claims/gut-lamina-propria-populated-hsc-bmdm]]
- `[c05]` PreMacs express PU.1, cMAF, and IRF8 as a core macrophage transcriptional programme (p.699) "preMacs express a core macrophage transcriptional programme that includes the transcription factors PU.1, cMAF and IRF8" — confidence: high — type: mechanistic — links: [[concepts/tissue-specific-lineage-determining-factors-macrophage]] [[foundations/spi1-pu1-master-tf]] [[claims/premacs-express-core-macrophage-tf-programme]]
- `[c06]` Tissue-specific LDFs (SALL1 microglia, ID3 Kupffer, PPARγ alveolar, SPI-C red pulp, GATA6 peritoneal) drive niche identity and their genetic deletion causes subset-specific deficiencies (p.699) "deletion of ID3 in Kupffer cells, SALL1 in microglia, PPARγ in alveolar macrophages, SPI-C in red pulp macrophages and GATA6 in large peritoneal macrophages" — confidence: high — type: mechanistic — links: [[concepts/tissue-specific-lineage-determining-factors-macrophage]] [[claims/tissue-specific-ldfs-drive-trm-identity]]
- `[c07]` Niche-derived signals (TGFβ, IL-34, retinoic acid, desmosterol/LXRα, CSF2, haem) instruct LDF expression in TRM specification (p.699) "expression of tissue-specific transcriptional regulators by tissue-resident macrophages is dependent on the niche. Such signals include cytokines such as TGFβ ... CSF2 (also known as GM-CSF) also controls PPARγ expression in alveolar macrophages and IL-34 is important for microglia and Langerhans cell identity" — confidence: high — type: mechanistic — links: [[concepts/tissue-specific-lineage-determining-factors-macrophage]] [[claims/niche-signals-instruct-trm-specification]]
- `[c08]` CSF1R and CSF2R (with CSF1, IL-34, CSF2 ligands) control TRM development and survival, with tissue-specific dependencies (microglia/Langerhans = IL-34; alveolar = CSF2) (p.701) "CSF1 and IL-34 signal to macrophages via the class III receptor tyrosine kinase CSF1R. Finally, CSF2 produced by lung epithelial cells is required for the survival of lung alveolar macrophages; this signal is mediated via CSF2R" — confidence: high — type: mechanistic — links: [[concepts/csf1r-il34-csf2-trophic-axis]] [[foundations/csf1r-receptor]] [[claims/csf1-il34-csf2-control-trm-development]]
- `[c09]` TRMs self-renew locally and persist for years independently of monocytes under homeostasis (p.701) "lineage tracing and parabiosis studies have demonstrated that resident macrophages self-renew locally and persist across the majority of tissues in adult mice independently of major contributions from BMDMs" — confidence: high — type: mechanistic — links: [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]] [[claims/trm-self-renew-locally]]
- `[c10]` Macrophages express five PRR families (TLRs, NLRs, RLRs, ALRs, CLRs) for pathogen sensing (p.704) "pattern recognition receptors (PRRs), which mediate the initial sensing of invading pathogens, can be classified into five families on the basis of their protein domain homology: Toll-like receptors, RIG-I-like receptors, NOD-like receptors, AIM2-like receptors and C-type lectin receptors" — confidence: high — type: mechanistic — links: [[concepts/pattern-recognition-receptors-macrophage]] [[claims/macrophages-express-five-prr-families-tlr]]
- `[c11]` Macrophages sense PtdSer on apoptotic cells via TIM4 and TAM receptors (TYRO3/AXL/MERTK) with bridging molecules MFGE8/GAS6/protein S/C1Q (p.704) "Macrophages sense phosphatidylserine exposed on the surface of apoptotic cells directly with TIM4 or through TAM receptors (TYRO3, AXL and MERTK), which work in conjunction with soluble bridging molecules such as MFGE8, GAS6, protein S and complement receptors" — confidence: high — type: mechanistic — links: [[concepts/efferocytosis-anti-inflammatory-clearance]] [[foundations/mertk-tam-receptors]] [[claims/efferocytosis-uses-tim4-tam-and-bridging-ligands]]
- `[c12]` Efferocytosis induces anti-inflammatory cytokines (TGFβ, IL-10, PGE2) and inhibits TNF/IL-1β/IL-6 (p.704) "This initiates the engulfment and degradation of target cells, secretion of anti-inflammatory molecules (TGFβ, IL-10 and PGE2) and inhibition of pro-inflammatory cytokine production" — confidence: high — type: mechanistic — links: [[concepts/efferocytosis-anti-inflammatory-clearance]] [[claims/efferocytosis-yields-anti-inflammatory-output]]
- `[c13]` Microglia mediate developmental synaptic pruning via complement (C1Q) (p.703) "Microglia participate in synaptic patterning by engulfing synaptic material and by the production of growth factors such as BDNF" + ref50 (Stevens 2007) "the classical complement cascade mediates CNS synapse elimination" — confidence: high — type: mechanistic — links: [[concepts/microglia-synaptic-pruning-complement]] [[claims/microglia-prune-synapses-via-c1q]]
- `[c14]` Microglial BDNF supports motor-learning-dependent synapse formation and neuropathic pain (p.703) "Microglial BDNF is important for motor learning-dependent synapse formation and neuropathic pain" — confidence: high — type: mechanistic — links: [[concepts/microglia-synaptic-pruning-complement]] [[claims/microglia-bdnf-supports-learning-synapse-formation]]
- `[c15]` Bi-allelic CSF1R LOF causes paediatric-onset leukoencephalopathy with microglia absence (p.703) "bi-allelic CSF1R loss of function results in paediatric-onset leukoencephalopathy, with a near complete absence of microglia, and death in the first year of life" — confidence: high — type: pathological — links: [[concepts/csf1r-il34-csf2-trophic-axis]] [[claims/csf1r-loss-causes-leukoencephalopathy]]
- `[c16]` TREM2/DAP12 LOF causes Nasu-Hakola disease (neurodegeneration + bone) and TREM2 polymorphisms increase Alzheimer's risk (p.703) "Inherited bi-allelic mutations in TREM2 or the gene encoding its adapter molecule DAP12 (TYROBP) causes a neurodegenerative and bone disease known as polycystic lipomembranous osteodysplasia with sclerosing leukoencephalopathy (also known as Nasu–Hakola disease). In addition, genome-wide association studies have identified TREM2 polymorphisms associated with risk of dementia and Alzheimer's disease" — confidence: high — type: correlational — links: [[concepts/trem2-microglia-dementia-axis]] [[foundations/trem2-receptor]] [[claims/trem2-loss-causes-nasu-hakola-and-alzheimer-risk]]
- `[c17]` Osteoclasts are multinucleated macrophages with EMP-derived nuclei that integrate HSC-derived nuclei via fusion in adult bone (p.701) "Embryo-derived osteoclasts carry EMP-derived nuclei and self-maintain in adult bones, but they integrate new HSC-derived nuclei by fusion, resulting in individual adult mouse osteoclasts being chimeric, containing nuclei from both EMPs and HSCs" — confidence: high — type: mechanistic — links: [[concepts/osteoclast-multinucleated-macrophage-bone]] [[claims/osteoclasts-are-chimeric-EMP-HSC-syncytia]]
- `[c18]` Osteopetrosis arises from LOF in TCIRG1, CLCN7, TNFRSF11A, TREM2, or CSF1R (p.703) "Mono- or bi-allelic loss-of-function mutations in genes that affect osteoclast survival and function, such as TCIRG1, CLCN7, TNFRSF11A, TREM2 and CSF1R, have been shown to cause osteopetrosis in humans and mice" — confidence: high — type: pathological — links: [[concepts/osteoclast-multinucleated-macrophage-bone]] [[claims/osteopetrosis-arises-lof-tcirg1-clcn7-tnfrsf11a]]
- `[c19]` Kupffer cells recycle iron from senescent erythrocytes via ferroportin (p.703) "Kupffer cells are resident macrophages in the liver that take up circulating senescent or damaged red blood cells. They have an important role in iron metabolism, as they recycle iron from haemoglobin via the ferroportin transporter" — confidence: high — type: mechanistic — links: [[concepts/kupffer-cell-iron-recycling]] [[claims/kupffer-recycle-iron-via-ferroportin]]
- `[c20]` Adipose TRMs produce diet-regulated PDGF-CC that promotes lipid storage in white adipocytes; loss redirects energy to brown adipose dissipation (p.704) "Fat tissue-resident macrophages promote lipid storage, in part via production of the growth factor PDGF-CC in response to increased dietary fat intake in mice ... Loss of energy storage in white adipose tissues of mice due to a lack of resident macrophages or PDGF-CC results in surplus unstored energy that is dissipated in the brown adipose tissue as heat" — confidence: high — type: mechanistic — links: [[concepts/adipose-macrophage-pdgf-cc-lipid-storage]] [[claims/adipose-trm-pdgf-cc-controls-lipid-storage]]
- `[c21]` CCR2-deficient mice (lacking monocytes) show reduced fibrosis across liver, heart, kidney, and lung injury models — supporting a TRM=restorative / BMDM=pro-fibrotic functional dichotomy (p.703) "Ccr2-deficient mice—which lack monocytes—exhibit substantially milder fibrosis in various injury models in the liver, heart, kidneys and lungs" — confidence: high — type: mechanistic — links: [[concepts/trm-bmdm-tissue-repair-fibrosis-dichotomy]] [[claims/ccr2-monocyte-deficiency-reduces-fibrosis]]
- `[c22]` SIRPα-CD47 axis is a 'don't-eat-me' signal that protects normal cells and tumour cells from macrophage phagocytosis; targeting it is a therapeutic strategy (p.704) "the immunoreceptor tyrosine-based inhibitory motif-containing receptor SIRPα ... protects tumoural cells, which express the SIRPα ligand CD47. Targeting the SIRPα–CD47 axis is a promising strategy for cancer treatment" — confidence: high — type: pharmacological — links: [[concepts/sirpa-cd47-don-t-eat-me-axis]] [[claims/sirpa-cd47-axis-blocks-phagocytosis]]

## Discussion captured

### Authors' interpretation

The authors interpret the converging fate-mapping, transcriptomic, and disease-genetics literature as supporting a unifying conceptual model: TRMs are an **ancillary cell type**, developmentally distinct from HSC-derived macrophages, paired one-to-one with specialized parenchymal cells across tissues. Tissue identity is **stochastically initiated** in PreMacs (LDF expression precedes niche arrival) and then **niche-selected** — environments that lack matching cues fail to retain the wrong-LDF macrophage. The authors prefer this stochastic/selection model over a purely instructive one because (i) "tissue-specific" cytokines like TGFβ and retinoic acid are in fact broadly expressed, and (ii) PreMacs already show patchy LDF expression at E10.25 before colonization. They argue this has direct consequences for engineering therapeutic macrophage subsets — engineering must target LDF expression, not just expose cells to cytokines.

For disease, the authors interpret the spectrum of TRM-linked phenotypes (neurological, skeletal, metabolic, autoimmune, oncological) as evidence that the *ancillary* model also explains pathology: when a TRM subset dysfunctions, the paired parenchymal cell loses support and the tissue fails. Thus dementia (microglia↔neurons), osteopetrosis (osteoclasts↔osteoblasts), alveolar proteinosis (alveolar macs↔type II pneumocytes), lipodystrophy (fat-resident macs↔adipocytes) all share this structure.

### Comparisons with prior literature (made by authors)

- **EMP origin foundation**: Schulz 2012 *Science* (ref 4), Hashimoto 2013 *Immunity* (ref 5), Yona 2013 *Immunity* (ref 6), Ginhoux 2010 *Science* (ref 9 — primitive yolk sac → microglia), Gomez Perdiguero 2015 *Nature* (ref 14), Mass 2016 *Science* (ref 15) — anchor the EMP yolk-sac model.
- **Niche specification**: Lavin 2014 *Cell* (ref 76), Gosselin 2014 *Cell* (ref 77 — environment-driven enhancers), Sakai 2019 *Immunity* (ref 17 — Kupffer enhancers), Okabe & Medzhitov 2014 *Cell* (ref 21 — peritoneal GATA6/RA), Guilliams 2022 *Cell* (ref 79 — hepatic niches), Dick 2022 *Sci Immunol* (ref 80 — three TRM subsets across organs), Masuda 2022 *Nature* (ref 81 — postnatal CNS macrophage subsets) are presented as the supporting transcriptomic body.
- **PDGF-CC / fat**: Cox 2021 *Science* (ref 55, by co-author Cox) — central fat-macrophage / lipid-storage finding.
- **Synaptic pruning**: Paolicelli 2011 *Science* (ref 49), Stevens 2007 *Cell* (ref 50 — complement), Parkhurst 2013 *Cell* (ref 53 — BDNF), Coull 2005 *Nature* (ref 54 — BDNF / neuropathic pain).
- **Disease genetics**: Rademakers 2012 (ref 64), Oosterhof 2019 (ref 60), Guo 2019 (ref 59) for CSF1R; Frattini 2000 (ref 67), Sobacchi 2007 (ref 68) for osteopetrosis; refs 164/165 (Nasu-Hakola TREM2/DAP12); Nott 2019 *Science* (ref 66 — disease enhancer–promoter maps in microglia).
- **TRM repair vs BMDM fibrosis**: Duffield 2005 *JCI* (ref 42), Aurora 2014 *JCI* (ref 43 — neonatal heart), Mirza 2009 (ref 69), Wynn & Vannella 2016 *Immunity* (ref 70), and CCR2-KO fibrosis studies (refs 160-163).
- **Cancer / phagocytosis**: refs 191-195 (TAM-cancer), refs 193-194 (SIRPα-CD47 immunotherapy).

### Mechanistic hypotheses proposed

- *Stochastic LDF expression hypothesis*: "differentiating preMacs that stochastically express certain sets of LDFs before they reach a given tissue preferentially survive and differentiate or settle—in other words, are selected—in microenvironments that provide suitable cues, which are not limited to growth factors." (p.700)
- *Macrophage as recycling factory hypothesis*: "Macrophages thus appear to function as recycling factories and biochemical transducers that integrate environmental inputs to direct tissue growth, remodelling and proper tissue function." (p.701)
- *LSD = nutrient-recycling failure hypothesis*: "an important function of resident macrophages may be to recycle the substantial amounts of nucleotides, proteins, lipids and sugars that result from cellular digestion to fuel cell proliferation, tissue growth, remodelling and regeneration. Lysosomal dysfunction in resident macrophages interferes with nutrient recycling, leading to cellular stress or damage and ultimately organ disfunction." (p.704)
- *Distinct TRM vs BMDM tumour roles hypothesis*: "distinct subsets of resident macrophages and monocyte-derived macrophages may have different roles in tumour growth ... the roles of macrophages in tumour growth may depend on the transcriptomes of macrophage subsets and the balance between engagement of activating and inhibitory receptors in distinct microenvironments or tumoural niches." (p.704)

### Caveats and self-criticism

- "the experimental approaches used in several of the above studies do not allow the observed phenotype to be formally attributed to resident macrophages" (p.703) — caveat that many of the TRM-vs-BMDM repair papers used non-specific depletion that cannot cleanly assign function.
- "Whether self-renewal is achieved by mitosis of differentiated macrophages or by the presence of a yet unidentified macrophage progenitor compartment within tissues remains unknown" (p.701) — open mechanistic question.
- "in the absence of further experimental evidence, a primitive haematopoietic origin of macrophages is uncertain" (p.699) — hedges on the primitive (vs EMP) origin of microglia.
- "All fate-mapping studies but one suggest that fetal HSCs do not give rise to resident macrophages" (p.699) — acknowledges one outlier study.

### Future directions suggested

- DNA barcoding to clarify EMP vs HSC contribution to adult TRM pools (p.699 ref 99).
- Identification of molecular determinants of TRM specification for therapeutic engineering (p.700).
- Investigation of fat-tissue macrophage roles in lipid/energy metabolism as therapeutic targets (p.704).
- Investigation of mechanisms underlying anti-tumour activity of Kupffer cells to identify cancer therapy targets (p.704).
- "future studies should therefore consider the contributions of individual macrophage subsets to given phenotypes" (p.704).

## Limitations

This is a *Review*, not a primary study, so the conventional methodological-limitations section does not apply. The review's interpretive limitations are:

- **Mouse-centric synthesis** — most fate-mapping evidence is murine; human TRM ontogeny is inferred indirectly from transplant chimerism studies and cross-species consistency.
- **Fate-mapping tools have limitations** — Csf1r-creER, Cx3cr1-creER, Ms4a3-cre etc. each label imperfectly; the EMP-vs-primitive vs HSC distinction depends on the specific tool used.
- **Definition of "resident"** is operational, not absolute — gut macrophages and a fraction of liver/skin macrophages have HSC contribution, blurring the dichotomy.
- **Ancillary-cell framing is conceptual** — the one-to-one TRM↔parenchyma pairing is an organizing metaphor; some tissues (e.g. spleen, gut) have multiple resident macrophage subsets with overlapping niche roles.
- **Fig. 3 disease ↔ function mapping is selective** — many TRM-related diseases (e.g. atherosclerosis, MASH, CHIP-driven myeloid disorders) are not covered.

## Open questions

### Open questions raised by authors

- Whether TRM self-renewal occurs by mitosis of differentiated cells or via an unidentified tissue macrophage progenitor (p.701).
- Whether single niche signals are sufficient to determine TRM identity, or whether unique cytokine-cocktails are required (p.700).
- The relative contribution of stochastic vs instructive specification (p.700) — authors favour stochastic/selection but acknowledge unresolved.
- The respective roles of monocytes vs resident macrophages in efferocytosis (p.704).
- Whether the primitive haematopoietic (RUNX1-independent) lineage contributes to adult mammalian microglia (p.699).
- Mechanisms underlying Kupffer-cell-mediated anti-tumour activity in liver (p.704).
- Whether BMDM contribution to fat-resident macrophage pool in obesity is clinically targetable (p.704).

### Open questions identified during ingest

- Which LDFs are *necessary* vs *sufficient* for tissue-specific TRM identity remains unmapped — most evidence is loss-of-function, not gain-of-function reprogramming.
- Quantitative parameters of "ancillary pairing" — how much TRM dysfunction is tolerated before parenchymal cell decompensates? Threshold-effect is implied by hypomorphic-vs-bi-allelic CSF1R severity gradient but not formalized.
- How does the *epigenetic* TRM state (Lavin 2014, Gosselin 2014 enhancer landscapes) interact with the LDF-instructive vs stochastic-selection mechanism? The review treats them as a single layer, but the field has pulled them apart.
- Which TRM diseases are amenable to BMT/HSC-replacement and which are not? Review notes BMT helps "some but not all" LSD patients; the predictive logic is unclear.
- For tumour immunology specifically: do early-stage Kupffer-cell-mediated tumour limitation and late-stage TAM-mediated tumour promotion involve the *same* lineage of cells switching state, or are they distinct populations?
- How does the model interface with the Casanova-Acebes 2021 finding that lung TRMs *promote* (not limit) early tumours? The Lazarov review predates that paper's TRM-pro-tumour story being fully appreciated; future syntheses need to reconcile organ-specific opposite directions.

## My take

This is the canonical 2023 Nature review on tissue-resident macrophages — by Geissmann's group, who established much of the foundational EMP-origin story. For a Ballestar-lab thesis on hypoxic NF-κB-driven macrophage reprogramming, this review is the *ontogeny anchor*: it crystallizes the developmental and tissue-specific context against which my hypoxia work happens. Two specific links to my own research:

1. **Hypoxia in TRMs** — the review notes HIF1α/HIF2α as macrophage transcriptional effectors of hypoxia (ref 32 Fang 2009) and explicitly flags VEGF-A/HIF-driven angiogenesis as a TRM repair function. My HIF1α-NF-κB cooperative-binding work (Calafell 2024) is squarely within the mechanism the review names but does not detail.
2. **TRM vs BMDM dichotomy in cancer** — Lazarov frames Kupffer cells as anti-tumour and BMDM-TAMs as pro-tumour. The Casanova-Acebes 2021 lung NSCLC TRM niche paper inverts this for early-stage lung. Reconciling these requires per-tissue, per-stage, per-genotype thinking — exactly the framing the review advocates.

For the wiki: this paper is a TIER_1 anchor for the [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]] hub and introduces the LDF / niche / ancillary-cell vocabulary that downstream papers (Mulder 2021, Casanova-Acebes 2021) build on. It will sit as a key reference for any future ingest touching macrophage development, microglia, Kupffer, alveolar macs, or osteoclasts.

Reading note for me: the *ancillary cell* framing is the single most useful conceptual gift of this review — it cleanly separates innate-immunity discourse ("macrophage = phagocyte") from tissue-physiology discourse ("macrophage = paired-helper cell"). I should adopt it when writing my own thesis chapter on macrophage diversity.

## Related

- [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]] — central concept this review anchors
- [[concepts/tissue-specific-lineage-determining-factors-macrophage]] — newly extracted concept
- [[concepts/csf1r-il34-csf2-trophic-axis]]
- [[concepts/efferocytosis-anti-inflammatory-clearance]]
- [[concepts/microglia-synaptic-pruning-complement]]
- [[concepts/kupffer-cell-iron-recycling]]
- [[concepts/adipose-macrophage-pdgf-cc-lipid-storage]]
- [[concepts/trm-bmdm-tissue-repair-fibrosis-dichotomy]]
- [[concepts/trem2-microglia-dementia-axis]]
- [[concepts/lysosomal-storage-disease-macrophage-dysfunction]]
- [[concepts/sirpa-cd47-don-t-eat-me-axis]]
- [[concepts/osteoclast-multinucleated-macrophage-bone]]
- [[concepts/pattern-recognition-receptors-macrophage]]
- [[concepts/mononuclear-phagocyte-system]]
- [[concepts/tissue-resident-macrophage-tumor-niche]]
- [[foundations/csf1r-receptor]]
- [[foundations/spi1-pu1-master-tf]]
- [[foundations/mertk-tam-receptors]]
- [[foundations/tgfb1-cytokine]]
- [[foundations/trem2-receptor]]
- [[foundations/hif1a]]
- [[people/frederic-geissmann]]
- [[people/tomi-lazarov]]
- [[papers/cross-tissue-single-cell-landscape-human]] — Mulder 2021 MoMac-VERSE — same MoMac biology, single-cell view
- [[papers/tissue-resident-macrophages-provide-pro-tumorigenic]] — Casanova-Acebes 2021 — TRM as pro-tumour niche, partly inverts the TRM-anti-tumour Kupffer story

- [[papers/aryl-hydrocarbon-receptor-rehabilitated-target-therapeutic]] — NRDD 2025 review of AHR biology and therapeutic targeting; provides pharmacological framework for the Trp-Kyn-AHR / IDO1 / IL4I1 immunosuppression axis discussed here
- [[papers/metabolism-tissue-macrophages-homeostasis-pathology]] — Wculek et al. 2022 *Cell Mol Immunol* — sibling TRM review focused on tissue-by-tissue immunometabolism; together with this paper forms the two-pillar TRM foundation (added 2026-05-26).
