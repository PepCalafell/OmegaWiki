---
# === Identification ===
title: "The hypoxia-driven crosstalk between tumor and tumor-associated macrophages: mechanisms and clinical treatment strategies"
slug: hypoxia-driven-crosstalk-between-tumor-tumor
arxiv: ""
doi: "10.1186/s12943-022-01645-2"
pmid: "36071472"
venue: "Molecular Cancer"
year: 2022
authors:
  - "Ruixue Bai"
  - "Yunong Li"
  - "Lingyan Jian"
  - "Yuehui Yang"
  - "Lin Zhao"
  - "Minjie Wei"
first_author: "Ruixue Bai"
corresponding_author: "Lin Zhao; Minjie Wei"

# === Source & metadata ===
source_type: pdf
s2_id: "8c48287b01eb923a937b6d943a71ffa457b2e9e7"
date_added: 2026-05-08
ingested_date: 2026-05-08
ingest_version: 1
last_reviewed: null

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - hypoxia
  - TAM
  - tumor-microenvironment
  - HIF-1α
  - HIF-2α
  - macrophage-polarization
  - exosomes
  - chemokines
  - lactate
  - succinate
  - PD-L1
  - immunotherapy
  - HIF-inhibitors
  - oncometabolites
  - clinical-trials
  - review
keywords:
  - hypoxia-inducible factor
  - tumor-associated macrophage
  - intercellular communication
  - exosomal miRNA
  - oxygen sensing
  - oncometabolite
  - HIF inhibitor
  - Belzutifan
  - PT2385
  - cancer therapy
domain: "oncology / immunology / hypoxia"

# === Biomedical domain ===
tissue:
  - multi
  - lung
  - liver
  - colon
  - stomach
  - pancreas
  - breast
  - cervix
  - ovary
  - kidney
  - brain
  - skin
  - bone_marrow
  - in_vitro_only
condition:
  - cancer
disease_specific:
  - non_small_cell_lung_cancer
  - hepatocellular_carcinoma
  - clear_cell_renal_cell_carcinoma
  - glioma
  - epithelial_ovarian_cancer
  - pancreatic_cancer
  - cervical_cancer
  - gastric_cancer
  - melanoma
  - multiple_myeloma
  - head_and_neck_squamous_cell_carcinoma
  - VHL_disease
species:
  - human
  - mouse
hypoxia_relevant: true
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques:
  - literature_review
  - clinical_trial_summary
n_samples: null
n_cells_total: null
integration_method: ""

# === Biology captured ===
key_cell_types:
  - tumor_associated_macrophage_TAM
  - tumor_cell
  - M1_macrophage
  - M2_macrophage
  - cancer_stem_cell
  - MHC-II_high_TAM
  - MHC-II_low_TAM
key_markers:
  - HIF1A
  - HIF2A
  - HIF3A
  - ARNT_HIF1B
  - PHD1
  - PHD2
  - PHD3
  - VHL
  - FIH
  - KDM6A
  - KDM5A
  - VEGF
  - VEGFA
  - CSF1
  - CCL2_MCP1
  - CCL8
  - CCL15
  - CXCL8_IL8
  - IL6
  - IL10
  - IL1B
  - OSM
  - PD-L1
  - PD-1
  - CD47
  - SIRPA
  - TLR4
  - HMGB1
  - LGALS3_GAL3
  - SEMA3A
  - NRP1
  - MYDGF
  - SPINT1
  - HGF
  - SUCNR1
  - PTEN
  - STAT3
  - NF-κB_p65
  - NF-κB_p50
  - mTORC2
  - AKT1
  - miR-1246
  - miR-21-3p
  - miR-125b-5p
  - miR-181d-5p
  - miR-301a-3p
  - miR-101
  - miR-155-3p
  - miR-223
  - let-7a
  - HMMR-AS1
  - Hsa-circ-0048117
  - PIM1
  - iASPP
  - CDK8
  - SOCS4
  - SOCS5
  - TERF2IP_RAP1
  - CREBRF
  - LOXL2
  - SPHK1
  - ROS
key_pathways:
  - HIF1α_HIF2α_HRE_transcription
  - PHD_VHL_proteasomal_degradation
  - exosomal_miRNA_macrophage_education
  - JAK_STAT3_M2_polarization
  - NF-κB_macrophage_polarization
  - mTORC2_AKT_M2_polarization
  - PI3K_AKT_PTEN_axis
  - lactate_HIF1α_PKA_CREB_M2
  - succinate_SUCNR1_PI3K_HIF1α
  - TLR4_TRIF_NF-κB_M2
  - SIRPα_CD47_phagocytosis
  - VEGF_VEGFR2_angiogenesis
  - CCL2_CCR2_macrophage_recruitment
  - CXCL8_CXCR1_2_JAK_STAT1
  - Sema3A_NRP1_PlexinA_TAM_capture
  - IL-1β_HIF1α_COX2_EMT
  - melatonin_SPHK1_ROS_HIF
  - camptothecin_HIF1α_inhibition

# === User project membership ===
projects:
  - hypoxia
  - thesis
priority: core
read_status: deep_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: included
exclusion_reason: null
data_availability: "Open access (CC BY 4.0). Review article — no primary data."

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Tumor hypoxia is a near-universal feature of solid tumors and a powerful driver of malignancy, therapy resistance, and poor prognosis. Tumor-associated macrophages (TAMs) are the most abundant immune population in the tumor microenvironment (TME) and accumulate preferentially in hypoxic regions, where they typically acquire pro-tumorigenic phenotypes and severely restrict immunotherapy efficacy. Despite the recognition that intra-tumoral hypoxia and TAM phenotype together drive aggressiveness, prior reviews had not synthesized the *molecular mechanisms* of the hypoxia-driven crosstalk between tumor cells and TAMs — i.e., how hypoxia rewires the bidirectional cell-cell communication via exosomes, cytokines, growth factors, ligand-receptor pairs, cellular debris, and oncometabolites. This review aims to fill that gap and connect mechanism to the active clinical pipeline of HIF-1α / HIF-2α inhibitors.

## Key idea

Hypoxia exerts both a *direct* effect on macrophage polarization (e.g. via the unfolded protein response and HIF-α stabilization) and a much larger *indirect* effect by altering tumor-cell-derived signals that recipient macrophages decode. The review organizes the hypoxia-driven tumor-TAM dialogue into five communication channels: (1) tumor-derived exosomes carrying miRNAs / lncRNAs / circRNAs / IL-6 that drive M2 polarization; (2) cytokines and growth factors (OSM, IL-8/CXCL8, CCL2, CCL8, VEGF, MYDGF) that recruit and polarize macrophages; (3) binding proteins and protease inhibitors (Galectin-3, HMGB1, Spint1) with mostly pro- but occasionally anti-tumor effects; (4) ligand-receptor interactions, notably the SIRPα-CD47 "don't-eat-me" axis whose hypoxic dynamics in colon cancer paradoxically *enhance* phagocytosis; (5) tumor cell debris (TLR4/TRIF/NF-κB-mediated IL-1β secretion) and oncometabolites (lactate, succinate) that reprogram macrophage metabolism and surface phenotype. The clinical translation is anchored on small-molecule HIF-2α inhibitors (Belzutifan — first FDA approval for VHL disease; PT2385; DFF332; NKT2152), HIF-1α small-molecule inhibitors (PX-478, MBM-02/Tempol), nucleic-acid drugs (RO7070179/EZN-2968 ASO; ARO-HIF2 RNAi), and drug repurposing (camptothecin/CRLX101/SN-38, melatonin, digoxin).

## Method

This is a narrative literature review. The authors synthesize ~225 primary references (2000-2022) on:
- pathophysiologic features of tumor hypoxia (chronic vs acute vs cyclic classification with H-R cycles)
- oxygen sensing mechanisms (HIF/PHD/VHL/FIH canonical axis plus newly discovered KDM6A/KDM5A direct-O₂-sensing)
- the mediators of tumor-TAM crosstalk under hypoxia (Table 1: 30 mechanism rows spanning 19 cancer types)
- clinical trials of HIF inhibitors (Table 2: 13 distinct drugs across phases I-III in 18 NCT entries)

No primary experiments. Tables 1 and 2 serve as the mechanistic and clinical anchors; Figures 1-4 are summary cartoons.

## Results

The review's "results" are the synthesis itself, summarized below in subsections:

### 1. Tumor hypoxia is heterogeneous and dynamically structured
- Solid tumors comprise normoxic (near functional vessels), hypoxic (>100 µm from vessels), and necrotic (>150 µm) regions; the hypoxic threshold is conventionally pO₂ < 10 mmHg (1.3 kPa).
- Hypoxia is classified as chronic (diffusion-limited, prolonged), acute (perfusion-limited, transient blockage), or cyclic (intermittent, hypoxia-reoxygenation H-R cycles minutes-to-days).
- The total duration, oxygen concentration, and frequency of H-R cycles are the three indicators of molecular regulation; there is no agreed standard for in vitro/in vivo hypoxia modeling.

### 2. Oxygen sensing is HIF-dependent AND HIF-independent
- Canonical: under normoxia, HIF-α is hydroxylated by PHDs (PHD1/2/3, Fe(II)/2-OG-dependent) and FIH at proline and asparagine residues; pVHL E3 ligase ubiquitinates and degrades HIF-α. Under hypoxia, HIF-α stabilizes, translocates, dimerizes with HIF-1β/ARNT, recruits p300/CBP, and binds HRE consensus.
- HIF-1α has stronger affinity for VHL than HIF-2α; the proline hydroxylation site dictates HIF-α / pVHL interaction strength.
- Non-canonical: KDM6A and KDM5A histone demethylases directly sense O₂ to regulate H3K27me3 and H3K4me3, controlling cell fate independently of HIF.
- Off-O₂ HIF activation: oleoylethanolamide (OEA) binds the HIF-3α PAS-B pocket as an endogenous ligand; PIM1 phosphorylates HIF-1α to block PHD binding regardless of O₂; iASPP binds VHL and prevents HIF-1α degradation without affecting hydroxylation.

### 3. Hypoxic exosomal miRNAs are the most-studied tumor→TAM channel
- Glioma exosomal miR-1246 → TERF2IP/RAP1 inhibition → STAT3 ON, NF-κB OFF → M2 polarization.
- Ovarian cancer hypoxic exosomal miR-21-3p / miR-125b-5p / miR-181d-5p → SOCS4/SOCS5 down → STAT3 phospho up → M2 polarization.
- Pancreatic cancer hypoxic exosomal miR-301a-3p (HIF-1α/HIF-2α regulated) → PTEN down → PI3Kγ on → M2 polarization & EMT.
- Hypoxic glioma exosomal IL-6 + miR-155-3p → CREBRF down → autophagy → M2 polarization (autophagy and STAT3 reinforcing each other).
- Melanoma hypoxic exosomal let-7a → IGF1R/INSR/IRS-1/IRS-2 down → AKT-mTOR off → glycolysis-to-OXPHOS shift → M2 polarization.
- Lung cancer hypoxia *suppresses* tumor exosomal miR-101 → CDK8 up in macrophages → IL-1A/IL-6 secretion (inflammatory).
- Hypoxic-TAM exosomal miR-223 → tumor PTEN down → PI3K/AKT activation → drug resistance & decreased apoptosis (TAM→tumor direction).
- Esophageal SCC hypoxic exosomal Hsa-circ-0048117 (ceRNA) → miR-140 sponge → TLR4 up in macrophages → M2 polarization.
- HCC exosomal HMMR-AS1 lncRNA (HIF-1α–induced) → miR-147a sponge → ARID3A up → M2 polarization.
- Intermittently hypoxic NSCLC exosomes → PD-L1 up in macrophages (relevant to OSA-cancer comorbidity).

### 4. Hypoxic cytokines and growth factors recruit and polarize TAMs
- OSM (IL-6 family) from hypoxic cancer cells → mTORC2-AKT1 (not PKCα) → CD206/CD163/Arg-1/COX-2 up → M2 polarization.
- CXCL8/IL-8 (macrophage-derived under hypoxia) → CXCR1/2 on gastric cancer → JAK/STAT1 → IL-10 transcription → reciprocal TAM M2 polarization (positive feedback).
- CCL8 (Zeb1 → CCL8 in cervical cancer hypoxia) → CCR2 → NF-κB → TAM infiltration.
- CCL2/MCP-1 (NF-κB/HIF-1α-driven in lung cancer) → macrophage accumulation.
- HNSCC: VEGF + IL-6 from tumor → M2 TAM → CCL15 (HIF-2α pathway) → CCR1-NF-κB → gefitinib resistance.
- Sema3A (hypoxia-induced) → NRP1 → captures TAMs into hypoxic niches via PlexinA1/A4 stop-signal mechanism (NRP1-independent step). Sema3A absence → M1-like TAM, reduced tumor growth.
- MYDGF (hypoxia-induced HCC) → cancer stem cell self-renewal, angiogenesis, macrophage infiltration, IL-6/TNF-α release.

### 5. Binding proteins and protease inhibitors are dual-edged
- Galectin-3 (TAM-secreted in hypoxia, ROS-NF-κB-dependent rather than HIF-1α-dependent) → tumor metastasis, angiogenesis, increased VEGFA secretion, glucose consumption.
- HMGB1 (HIF-1α-induced under prolonged hypoxia) → macrophage infiltration → IL-6 → STAT3 → tumor EMT.
- Spint1 (HIF-2α-induced in TAMs) → blocks HGFA → prevents pro-HGF cleavage → less active HGF → less c-Met activation → REDUCED tumor cell proliferation. This is a tumor-suppressing TAM mechanism.

### 6. SIRPα-CD47 axis under hypoxia: surprising direction
- HIF activates CD47 in many cancers ("don't-eat-me" up).
- BUT in colon cancer, hypoxia decreases macrophage SIRPα while increasing tumor CD47 — the net effect tilts toward enhanced phagocytosis (potentially explaining the better prognosis of M2-rich/HIF-1α-high colon cancer relative to other cancer types).

### 7. Tumor cell debris drives an IL-1β reverberation loop
- Severely hypoxic necrotic debris → TLR4/TRIF → NF-κB phospho up in macrophages → M2 polarization + IL-1β secretion.
- TAM IL-1β → tumor IL-1β/HIF-1α/COX-2 axis → enhanced tumor EMT.
- IL-1β additionally supports immune suppression (γδ T-cell IL-17, neutrophil G-CSF expansion) — TAMs are the dominant IL-1β source in many tumor models.

### 8. Oncometabolites: lactate and succinate
- Lactate → GPCR (PKA-CREB) on TAMs → M2 polarization; lactate + hypoxia synergistically induce ARG1, MAPK-driven VEGFA, HIF-1, Hedgehog, mTOR pathways. MHC-II^lo TAMs (hypoxia-enriched) shift to oxidative metabolism with lactate; MHC-II^hi TAMs do the opposite.
- Succinate → SUCNR1 on TAMs → PI3K-HIF-1 → TAM recruitment, M2 polarization, IL-6 secretion → cancer cell migration & EMT (also via SUCNR1 on tumor cells).

### 9. Clinical pipeline of HIF inhibitors
- HIF-2α small molecules (PAS-B pocket): Belzutifan/MK-6482/Welireg (first FDA approval 2021 for VHL-RCC/CNS-hemangioblastoma/pNET; expansion to Pacak-Zhuang syndrome and combinations with pembrolizumab/Lenvatinib/cabozantinib); PT2385 (first-in-class HIF-2α antagonist; ccRCC and recurrent GBM trials); DFF332; NKT2152.
- HIF-1α small molecules: PX-478 (HIF-1α/LOXL2/EMT axis; pancreatic ductal adenocarcinoma GM-CSF/PNI suppression); MBM-02/Tempol (dual HIF-1/2; ROS clearance in cycling hypoxia chemoresistance).
- Nucleic-acid drugs: RO7070179/EZN-2968 (LNA ASO targeting HIF-1α mRNA; HCC, advanced solid tumors); ARO-HIF2 (αvβ3-targeted RNAi against HIF-2α; advanced ccRCC phase I).
- Drug repurposing: Camptothecin and analogs (SN-38, topotecan, irinotecan; CRLX101 NDC); melatonin (NCT04137627 phase III in oral SCC; SPHK1-ROS-HIF-1α inhibition); digoxin (HIF-1α translation block, HIF-2α mRNA reduction).

## All claims (exhaustive)

- `[c01]` Hypoxia is a persistent and prevalent feature of solid tumors and a major driver of cancer malignancy and poor prognosis (p.1) "Given that hypoxia is a persistent physiological feature of many different solid tumors and a key driver for cancer malignancy" — confidence: high — type: correlational — links: [[concepts/tumor-hypoxia-mrna-signature]] [[foundations/hif1a]]
- `[c02]` TAMs are the most abundant immune cell population in the TME and accumulate preferentially in hypoxic tumor regions (p.1, p.2) "TAMs massively accumulate within hypoxic tumor regions" — confidence: high — type: correlational — links: [[concepts/tumor-associated-macrophage-immunosuppression]] [[concepts/tam-recruitment-hypoxic-niche-chemokines]]
- `[c03]` Tumor hypoxia is operationally classified into chronic (diffusion-limited, >24 h), acute (perfusion-blockage, <24 h), and cyclic (intermittent / IH, hypoxia-reoxygenation H-R cycles) subtypes (p.3) "tumor hypoxia can be roughly divided into chronic hypoxia and acute hypoxia... other studies have described three types of hypoxia: chronic hypoxia, acute hypoxia, and cyclic hypoxia" — confidence: high — type: methodological — links: [[concepts/tumor-hypoxia-classification-chronic-acute-cyclic]]
- `[c04]` HIF-α is hydroxylated by PHD1/2/3 and FIH under normoxia; pVHL ubiquitinates the hydroxylated HIF-α, leading to proteasomal degradation (p.4-5) "Under normoxia, HIF-α is hydroxylated by prolyl hydroxylases (PHDs) and then recognized by E3-ubiquitin ligase von Hippel-Lindau (VHL), resulting in the rapid degradation of HIF-α protein" — confidence: high — type: mechanistic — links: [[foundations/hif1a]] [[foundations/phd-prolyl-hydroxylases]] [[foundations/vhl-von-hippel-lindau]]
- `[c05]` HIF-1α has stronger pVHL affinity than HIF-2α; the specific proline-hydroxylation site differentially modulates the HIF-α / pVHL interaction (p.5) "Compared to HIF-2α, HIF-1α has a stronger affinity for VHL... different sites of proline hydroxylation play different roles in HIF-1α-pVHL interactions" — confidence: high — type: mechanistic — links: [[foundations/hif1a]] [[foundations/vhl-von-hippel-lindau]]
- `[c06]` KDM6A and KDM5A histone demethylases are direct oxygen sensors that regulate H3K27me3 and H3K4me3 in a HIF-independent manner (p.4) "Certain histone demethylases, such as KDM6A and KDM5A, directly sense oxygen to regulate gene expression by controlling chromatin structure" — confidence: high — type: mechanistic — links: [[concepts/kdm-direct-oxygen-sensing-hif-independent]]
- `[c07]` HIF-α activation can be uncoupled from O₂: PIM1 directly phosphorylates HIF-1α to prevent PHD binding regardless of O₂; iASPP binds pVHL to block HIF-1α degradation without affecting hydroxylation (p.5) "PIM1 kinase directly phosphorylated HIF-1α regardless of oxygen tension to prevent PHDs from binding... iASPP... bound directly to VHL and prevented HIF-1α from degrading" — confidence: high — type: mechanistic — links: [[foundations/hif1a]]
- `[c08]` Hypoxic glioma-derived exosomal miR-1246 targets TERF2IP (RAP1) to activate STAT3 and inhibit NF-κB, driving M2 macrophage polarization and tumor proliferation/migration/invasion (p.6) "MiR-1246 targets telomeric repeat binding factor 2 interacting protein (TERF2IP) and markedly promotes M2 macrophage polarization by activating the STAT3 pathway and inhibiting the NF-κB pathway" — confidence: high — type: mechanistic — links: [[concepts/hypoxia-exosomal-mirna-tam-polarization]]
- `[c09]` Hypoxic ovarian-cancer exosomal miR-21-3p, miR-125b-5p, miR-181d-5p bind SOCS4/SOCS5 to elevate phospho-STAT3 and induce M2 polarization (p.6, p.9) "miR-21-3p and miR-125 b-5p bind to SOCS4, whereas miR-21-3p and miR-181 d-5p bind to SOCS5, resulting in the decrease of SOCS4/5 expression and the increase of phosphorylated STAT3" — confidence: high — type: mechanistic — links: [[concepts/hypoxia-exosomal-mirna-tam-polarization]]
- `[c10]` Hypoxic pancreatic-cancer exosomal miR-301a-3p (HIF-1α/HIF-2α regulated) suppresses PTEN to activate PI3Kγ in TAMs, driving M2 polarization and tumor EMT/migration/invasion (p.9) "Tumor-derived exosomal miR-301a-3p, which is regulated by HIF-1α and HIF-2α, can be transferred to TAMs, promoting tumor cell EMT, migration, invasion, and metastatic potential. Exosomal miR-301a-3p mediates macrophages M2 polarization via downregulating PTEN expression and activating the PI3Kγ signaling pathway" — confidence: high — type: mechanistic — links: [[concepts/hypoxia-exosomal-mirna-tam-polarization]] [[foundations/pten-tumor-suppressor]]
- `[c11]` Hypoxic melanoma-derived exosomal let-7a is increased ~25-fold despite total tumor let-7a being only ~30% of normoxia, and is delivered to TAMs to suppress IGF1R/INSR/IRS-1/IRS-2, driving glycolysis-to-OXPHOS shift and M2 polarization (p.9) "total expression of let-7a miRNA... is only about 30% of that in normoxia, whereas exosomal let-7a miRNA is increased by almost 25 times" — confidence: high — type: quantitative — links: [[concepts/hypoxia-exosomal-mirna-tam-polarization]]
- `[c12]` Hypoxia *suppresses* tumor exosomal miR-101, derepressing CDK8 in macrophages and stimulating IL-1A and IL-6 secretion (lung-cancer setting) (p.9) "the tumor inhibitor miR101 is disturbed in tumor-derived exosomes under hypoxic stress, leading to the upregulation of cyclin-dependent kinase 8 (CDK8) in macrophages and the stimulation of IL1A and IL6 secretion in macrophages" — confidence: high — type: mechanistic — links: [[concepts/hypoxia-exosomal-mirna-tam-polarization]]
- `[c13]` Hypoxic-TAM-derived exosomal miR-223 lowers tumor-cell PTEN to activate PI3K/AKT, increasing tumor-cell viability and chemoresistance (TAM→tumor direction) (p.9) "Exosomal miR223 derived from hypoxic TAMs is internalized into co-cultured tumor cells, resulting in the decreased apoptosis rate, increased cell viability, and enhanced drug resistance" — confidence: high — type: mechanistic — links: [[foundations/pten-tumor-suppressor]]
- `[c14]` Intermittently hypoxic tumor cell exosomes upregulate PD-L1 on macrophages, providing biological rationale for poor cancer prognosis under obstructive sleep apnea (OSA) comorbidity (p.10) "Exosomes released from intermittently hypoxic tumor cells also promote PD-L1 expression in macrophages" — confidence: medium — type: correlational — links: [[concepts/hypoxia-pd-l1-tam-immune-evasion]]
- `[c15]` OSM (IL-6 family) from hypoxic cancer cells drives M2 polarization via mTORC2-AKT1 (not PKCα), upregulating CD206/CD163/Arg-1/COX-2 (p.10) "OSM can enhance the expression of M2 macrophage surface markers... activated mTORC2 leads to M2 polarization by relaying signals through its effector kinases Akt, particularly Akt1, rather than PKCα" — confidence: high — type: mechanistic — links: [[foundations/oncostatin-m-osm]]
- `[c16]` Hypoxia drives a CXCL8/IL-8 (macrophage) → CXCR1/2 (gastric cancer) → JAK/STAT1 → tumor IL-10 → TAM M2 (NF-κB) positive feedback loop (p.10) "Macrophage-derived CXCL8 induced by hypoxia can activate the JAK/STAT1 signaling pathway through binding to CXCR1/2 expressed on GC cells, leading to GC invasion and proliferation. The activation of STAT1 directly upregulates the expression of IL-10, stimulating M2 polarization of macrophages through the NF-κB signaling pathway" — confidence: high — type: mechanistic — links: [[foundations/cxcl8-il8]] [[foundations/nf-kb-p65-rela]]
- `[c17]` Sema3A is hypoxia-induced and captures TAMs into hypoxic niches via NRP1 followed by NRP1-independent PlexinA1/A4 stop-signaling; Sema3A loss yields M1-skewed TAMs and reduced tumor growth (p.11) "Sema3A drives TAMs toward hypoxic niches via the Sema3A–neuropilin-1 (Nrp1) pathway. Following macrophage localization in the hypoxic environment, Nrp1 is downregulated, and Sema3A captures TAMs locally via Nrp1-independent plexinA1-plexinA4-mediated stop signals" — confidence: high — type: mechanistic — links: [[concepts/tam-recruitment-hypoxic-niche-chemokines]]
- `[c18]` Galectin-3 in hypoxic TAMs is regulated by ROS-NF-κB rather than HIF-1α; HIF-1α inhibitors do NOT reduce hypoxic-TAM Gal-3 expression (p.11) "Although the expression level of HIF-1α is elevated in hypoxic TAMs, HIF-1α inhibitors have no effect on the expression of Gal-3 there, suggesting that HIF-1α may not be involved in Gal-3 expression in hypoxic TAMs" — confidence: high — type: pharmacological — links: [[foundations/galectin-3]]
- `[c19]` HIF-2α-induced Spint1 secreted by TAMs blocks HGFA-mediated HGF activation, inhibiting tumor cell proliferation — a tumor-suppressing TAM mechanism (p.11) "HIF-2α highly expressed in TAMs induces the secretion of the serine protease inhibitor Spint1. Spint1 is then released into TME to block the serine protease HGF activator (HGFA), preventing the cleavage of pro-HGF into active hepatocyte growth factor (HGF)... TAM-secreted Spint1 can reduce tumor cell proliferation" — confidence: medium — type: mechanistic
- `[c20]` In colon cancer, hypoxia decreases macrophage SIRPα while increasing tumor CD47, paradoxically *enhancing* phagocytosis and contributing to better colon-cancer prognosis (p.12) "Hypoxia can decrease SIRPα expression in macrophages while simultaneously increasing CD47 expression in colon cancer cells. The heightened signal of 'don't eat me' is countered by the reduced SIRP expression level, increasing the phagocytic capacity of macrophages" — confidence: medium — type: mechanistic — links: [[concepts/sirpa-cd47-don-t-eat-me-axis]]
- `[c21]` Severely hypoxic necrotic tumor debris activates macrophage TLR4/TRIF/NF-κB, driving M2 polarization and IL-1β secretion; macrophage IL-1β engages tumor IL-1β/HIF-1α/COX-2 to enhance EMT (p.12) "necrotic cancer cell debris can stimulate IL-1β secretion in macrophages via TLR4/TRIF/NF-κB signaling... Macrophage-derived IL-1β activates the IL-1β/HIF-1α/COX-2 axis, enhancing tumor cell EMT and promoting tumor invasion and metastasis" — confidence: high — type: mechanistic — links: [[foundations/lps-toll-like-receptor-signaling]] [[concepts/macrophage-induced-emt-tumor-invasiveness]]
- `[c22]` NF-κB exerts dual effects on TAM polarization depending on dimer composition: p50-p50 homodimers favor M2 (LPS-driven M1→M2 reprogramming); p65-p50 heterodimers favor M1 (Bufalin-driven M2→M1 transition) (p.12) "Lipopolysaccharide... promotes the overexpression of p50-p50 homodimers, allowing M1 to M2 macrophage reprogramming. In contrast, Bufalin promotes the overexpression of p65-p50 heterodimers, leading to the transition of macrophage from M2 to M1" — confidence: medium — type: mechanistic — links: [[foundations/nf-kb-p65-rela]]
- `[c23]` Lactate drives TAM M2 polarization via HIF-1α and via GPCR/PKA-CREB; lactate+hypoxia synergistically induce ARG1, VEGFA via MAPK, and M2 markers via HIF-1, Hedgehog, mTOR pathways (p.13) "lactate induces VEGF expression and M2-like polarization of TAMs, both of which are mediated by HIF-1α... Lactate targets the protein-coupled receptors on the surface of the TAMs membrane and induces M2-type polarization via the PKA/CREB pathway... When lactate is combined with hypoxia, macrophages become significantly more M2-polarized via the HIF-1, Hedgehog and mTOR pathways" — confidence: high — type: mechanistic — links: [[concepts/lactate-driven-tam-m2-polarization]]
- `[c24]` Tumor-derived succinate engages SUCNR1 on macrophages to activate PI3K-HIF-1, driving TAM recruitment, migration, and M2-skewed phenotype with IL-6 secretion that promotes cancer cell migration; succinate also acts on tumor SUCNR1 to drive EMT (p.13) "tumor-derived succinate also activates SUCNR1 on the membrane of tumor cells to induce cancer cell migration and EMT through the PI3K/HIF-1α pathway" — confidence: high — type: mechanistic — links: [[concepts/succinate-sucnr1-tam-axis]] [[foundations/sucnr1-succinate-receptor]]
- `[c25]` HIF-2α small-molecule inhibitors targeting the PAS-B pocket — Belzutifan (MK-6482) and PT2385 — are highly selective for HIF-2α/ARNT dissociation without affecting HIF-1 (p.13-14) "Despite the high sequence identity between HIF-2α and HIF-1α, these small-molecule inhibitors are highly selective in dissociating the HIF-2α/ARNT heterodimer while having no effect on HIF-1 function" — confidence: high — type: pharmacological — links: [[concepts/hif-2a-pas-b-small-molecule-inhibition]] [[foundations/belzutifan-mk-6482]] [[foundations/pt2385-hif2a-inhibitor]]
- `[c26]` Belzutifan is the first FDA-approved HIF inhibitor for VHL-disease-associated RCC, CNS hemangioblastomas, and pNET (no immediate surgery required); active trials test combinations with pembrolizumab, Lenvatinib, cabozantinib (p.13-14) "Belzutifan is the first FDA-approved treatment for Von Hippel-Lindau (VHL) disease in patients with renal cell carcinoma (RCC), central nervous system (CNS) hemangioblastomas, or pancreatic neuroendocrine tumors (pNET)" — confidence: high — type: pharmacological — links: [[foundations/belzutifan-mk-6482]]
- `[c27]` PX-478 is an HIF-1α small-molecule inhibitor that reduces HIF-1α protein, transactivation, and deubiquitination, blocks hypoxia-induced VEGF synthesis, and reduces GM-CSF/PNI in pancreatic ductal adenocarcinoma (p.14) "PX-478 can inhibit HIF-1α protein levels, transactivating activity, and deubiquitination... PX-478 can drastically reduce the expression level of granulocyte–macrophage-colony-stimulating factors (GM-CSF) and the incidence of perineural invasion (PNI) in pancreatic ductal adenocarcinoma" — confidence: high — type: pharmacological — links: [[foundations/px-478-hif1a-inhibitor]]
- `[c28]` Camptothecin (CPT) and analogs (SN-38, topotecan, irinotecan) are Topoisomerase I inhibitors that block HIF-1α expression and reduce cancer-stem-cell numbers; CRLX101 is a nanoparticle-drug conjugate of CPT for tumor delivery (p.15-16) "Camptothecin (CPT) and its analogs (including SN-38, topotecan, and irinotecan) are important Topoisomerase I inhibitors that can block HIF-1α expression... CRLX101 (NLG207) is a nanoparticle-drug conjugate (NDC) of CPT" — confidence: high — type: pharmacological

## Discussion captured

### Authors' interpretation

The authors frame hypoxia-driven tumor-TAM crosstalk as a *deadly combination* in which hypoxia indirectly amplifies its tumor-promoting effects by reprogramming TAM-tumor communication. They emphasize that the indirect effect (mediator-altered crosstalk) is at least as important as the direct effect (HIF-α stabilization in macrophages). They argue that hypoxia is a "double-edged sword" because rare hypoxic mechanisms — Spint1 secretion by HIF-2α-high TAMs, the SIRPα-CD47 paradoxical phagocytosis enhancement in colon cancer — are tumor-suppressing rather than tumor-promoting, and that this dichotomy demands further mechanistic dissection rather than a one-size-fits-all anti-hypoxia strategy.

The authors highlight that HIF-α activation can be uncoupled from O₂ (OEA endogenous PAS-B ligand of HIF-3α; PIM1 phospho-stabilization; iASPP-pVHL block), suggesting the HIF pathway is regulated by a richer set of cellular conditions than hypoxia alone, and that small-molecule allosteric ligands of the PAS-B pocket (HIF-2α antagonists like Belzutifan and PT2385) exploit the same pocket where endogenous OEA acts as a HIF-3α agonist — different molecules engaging similar pockets with opposite functional outcomes.

The authors argue that NF-κB's dual effects on TAM polarization (M1-promoting in some studies, M2-promoting in others) are best explained by *dimer composition* (p50-p50 vs p65-p50) and the source/activation route of the macrophage, rather than by a single canonical "NF-κB = pro-inflammatory" rule.

### Comparisons with prior literature (made by authors)

- The authors cite Henze & Mazzone 2016 J Clin Invest as a canonical review of hypoxia's impact on TAMs and explicitly position their review as a complement focused specifically on the molecular mediators of hypoxia-driven crosstalk, which prior reviews on tumor cell–macrophage communication (Baradaran 2022 Biomed Pharmacother; Batoon & McCauley 2021 Front Endocrinol; Sung 2021 Clin Mol Hepatol; Ge & Ding 2020 Front Oncol) had not unified.
- They cite Wei 2021 Front Cell Dev Biol (DOI 10.3389/fcell.2021.749210) as the most recent single-cell RNA-Seq evidence that hypoxia is the most important factor influencing cell communication in pan-cancer TME, motivating the review's central thesis.
- They cite Qi 2020 Front Oncol on hypoxic colorectal cancer where SIRPα-CD47 blockade may be ineffective, underscoring the colon-specific paradoxical phagocytosis enhancement mechanism.
- They cite Chakraborty 2019 *Science* (KDM6A direct O₂ sensing) and Gallipoli & Huntly 2019 *Science* (commentary) as the seminal demonstration of HIF-independent oxygen sensing.
- They cite Diao 2022 Nat Commun for OEA / HIF-3α PAS-B ligand identification.
- They cite Chakraborty 2019 Science 363:6432, Casillas 2021 Oncogene, Zhao 2022 Oncogene as exemplars of HIF activation uncoupled from oxygen.

### Mechanistic hypotheses proposed

- **Macrophage as integrator of dual signals**: "Macrophages have the ability to detect the presence of hypoxia and lactate. These signals can then be integrated with phenotypic responses by MAPK signaling" (p.13) — proposes that hypoxia and lactate are co-detected and combinatorially integrated rather than summed.
- **Subset-specific lactate metabolism**: lactate promotes oxidative metabolism in MHC-II^lo TAMs (hypoxic-region-enriched) while inhibiting it in MHC-II^hi TAMs — a position-dependent metabolic logic for TAM heterogeneity.
- **NF-κB-dimer-composition explanation**: "different homo- or heterodimers, which have opposing effects on macrophage polarization, depending on the source of macrophage populations and the way that macrophages are activated" (p.12).
- **HIF inhibitor combination strategy**: HIF-2α inhibitors plus immune checkpoint blockade (Belzutifan + pembrolizumab) and tyrosine kinase inhibitors (Belzutifan + Lenvatinib/cabozantinib) are explicitly proposed as the path to broaden HIF-targeted therapy beyond VHL-RCC.

### Caveats and self-criticism

- "Despite the fact that the importance of hypoxia in oncology is now widely recognized, understanding the many complex interactions of hypoxia and related TME stresses with cancer biology and therapy remains a work in progress" (p.3).
- "Most of the studies on the effect of lactate on macrophages were conducted under normoxic conditions, rather than hypoxic conditions" — the literature base for lactate-TAM is itself poorly hypoxia-controlled (p.13).
- "The majority of studies are still performed under normoxia, frequently ignoring the importance of hypoxia" (p.16) — the authors echo Semenza's 2017 critique.
- "There is no unambiguous and uniform classification system" for tumor hypoxia subtypes; "there is currently no agreement on the methods for studying tumor hypoxia in vitro or in vivo" (p.3).
- For TLR4 specifically: "Paradoxically, TLR4 can cause macrophage polarization towards M1 or M2" — same receptor, opposite effects — the authors acknowledge but do not resolve.
- Most exosomal miRNA→macrophage findings (miR-1305, miR-21, miR-940 in tumor exosomes) report M2 polarization but the precise mechanism is "not been thoroughly studied" — depth of mechanism varies widely across the cited body of work (p.9).

### Future directions suggested

- Standardization of in vitro and in vivo hypoxia model systems and of intratumoral hypoxia detection in clinic (p.3).
- Detailed dissection of NF-κB dimer composition in TAM polarization (p.12).
- Mapping additional non-HIF oxygen sensors beyond KDM6A/KDM5A (p.16).
- More research on Nrp-1's role in M2 TAM polarization in cancer cells (p.11).
- Mechanistic depth on MYDGF, miR-1305, miR-21, miR-940 actions in TAM (p.9, p.11).
- Combination strategies of HIF inhibitors with checkpoint blockade and TKIs (p.13-14).

## Limitations

- Narrative review without systematic search documentation; coverage of the literature is comprehensive but unaudited.
- Most of the cited mechanistic studies are 2017-2022 in vitro / co-culture, with few in vivo conditional / fate-mapping experiments — the in vivo specificity of TAM hypoxic-niche mechanisms vs systemic effects is poorly distinguished in the underlying literature.
- TAM heterogeneity beyond M1/M2 (single-cell-resolved subsets) is hardly used as an organizing principle; the review largely retains the M2 = pro-tumor framing.
- No quantitative meta-analysis: directional effects are summarized but not weighted by sample sizes, statistical strength, or replication count.
- Cancer types covered are uneven: glioma, NSCLC, HCC, ovarian, pancreatic, gastric receive deepest treatment; melanoma, esophageal, endometrial, MM, HNSCC are summarized only via single studies; rare cancers are absent.
- Clinical-trial table is current as of mid-2022; multiple Belzutifan / PT2385 / ARO-HIF2 trials have read out since.
- Spatial dimension (oxygen gradients, distance from vasculature, niche heterogeneity) is mentioned but not deeply integrated with the mechanistic mediators.

## Open questions

### Open questions raised by authors

- "How does Nrp-1, which is produced by cancer cells, promotes M2 macrophage polarization under hypoxic conditions?" (p.11)
- "The molecular mechanism of MYDGF action in tumor progression is still unclear" (p.11)
- "Mechanisms of these miRNAs [miR-1305, miR-21, miR-940] have not been thoroughly studied" (p.9)
- "TLR4 can cause macrophage polarization towards M1 or M2" — how is this paradox resolved? (p.10)
- Why do HIF-1α inhibitors (e.g. 2ME2) upregulate Gal-3 in normoxia but not in hypoxia in TAMs? (p.11)
- "Mechanisms of tumor hypoxic adaptation are more complex than currently envisaged" — what are the additional non-HIF oxygen sensors? (p.16)
- Will the HIF-2α inhibitor + checkpoint / TKI combinations show survival benefit beyond VHL-RCC?

### Open questions identified during ingest

- Are the exosomal miRNA mechanisms (miR-1246, miR-21-3p/125b/181d, miR-301a-3p, let-7a) unified by a single hypoxic exosome-loading machinery (HIF-driven nSMase / Rab27a etc.) or independently regulated per miRNA?
- Does Spint1-mediated tumor suppression by HIF-2α-high TAMs partially offset Belzutifan's intended tumor-restraining effect (i.e. blocking HIF-2α in TAMs may release pro-HGF cleavage and promote tumor cell proliferation)?
- The colon-cancer paradox of hypoxia-enhanced phagocytosis is at odds with the broader literature of hypoxia-driven CD47 upregulation. Is colon cancer's better prognosis explained primarily by this mechanism, or by independent factors (microbiome, MSI, etc.)?
- Are MHC-II^lo TAMs equivalent to a specific MoMac-VERSE cluster (e.g. cluster #4 hypoxic-inflammatory IL1B^+ Mac, or TREM2^+ LAM)?
- Is the synergy between hypoxia and lactate in driving TAM M2 explained by Hedgehog as a downstream effector, or is Hedgehog-pathway involvement a lactate-only signal?
- Does intermittent / cyclic hypoxia (vs chronic hypoxia) drive *quantitatively different* exosome cargos / mediator outputs, given the H-R cycles induce ROS bursts that re-stabilize HIF-1α/NF-κB?

## My take

For my hypoxia-NF-κB-macrophage thesis, this review is a near-perfect orientation map of the *external* (tumor-cell-derived) signals that hypoxic TAMs receive. My own work focuses on the *internal* (intrinsic, NF-κB+TET2-driven) reprogramming of macrophages under hypoxia; this review is the natural complement that anchors what those reprogrammed macrophages then do under bidirectional crosstalk in the TME. Three lines stand out for thesis use:

1. **The NF-κB dimer-composition argument** (p.12) is consonant with my finding that NF-κB cooperates with HIF-1α at chromatin under hypoxia: which dimer (p65-p50 vs p50-p50) cooperates with HIF-1α at hypoxia-NF-κB co-bound enhancers is a directly testable extension of my dataset.
2. **Sema3A → NRP1 capture** is mechanistically appealing as the stop-signal that explains *why* TAMs accumulate in hypoxic niches rather than freely diffusing — a complementary mechanism to my hypothesized HIF-1α-NF-κB-driven transcriptional locking.
3. **The Spint1 / colon-cancer paradox** are useful counter-examples for the thesis's claim that hypoxia + NF-κB activation makes TAMs *more* immunogenic — they preserve the dual-edged nature of hypoxia even in a thesis that argues for hypoxia-driven immunostimulation.

The review's biggest gap from my perspective is that it does not use single-cell taxonomies of TAMs (MoMac-VERSE etc.) — the M1/M2 axis is the dominant framing throughout. For the thesis I will integrate the mechanistic mediators here with the IL4I1/TREM2/MMAC1 cluster framework from Mulder 2021 and Calafell 2024.

## Related

- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — Bhandari 2019 *Nat Genet*. Pancancer molecular landmarks of tumor hypoxia (genome-side); the Bai review provides the immunological / mediator-side dialogue with TAMs that complements Bhandari's genomic phenotype.
- [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] — Calafell 2024. The intrinsic transcriptional and methylation program of hypoxic macrophages; this review covers what those reprogrammed macrophages then do via tumor-TAM dialogue.
- [[papers/tissue-resident-macrophages-provide-pro-tumorigenic]] — Casanova-Acebes 2021 *Nature*. NSCLC TRM-pioneered tumor-immune niche; complementary view of macrophage origin in the hypoxic-niche TAM pool.
- [[papers/cross-tissue-single-cell-landscape-human]] — Mulder 2021 *Immunity*. MoMac-VERSE atlas; gives the TAM cluster-resolved framework that this review's M1/M2-dominant framing largely lacks.
- [[papers/physiology-diseases-tissue-resident-macrophages]] — Lazarov & Geissmann 2023 *Nature*. Background on macrophage physiology that frames the SIRPα-CD47 axis discussed in this review.
- [[concepts/tumor-associated-macrophage-immunosuppression]]
- [[concepts/tam-recruitment-hypoxic-niche-chemokines]]
- [[concepts/hypoxia-exosomal-mirna-tam-polarization]]
- [[concepts/lactate-driven-tam-m2-polarization]]
- [[concepts/succinate-sucnr1-tam-axis]]
- [[concepts/hypoxia-pd-l1-tam-immune-evasion]]
- [[concepts/hif-2a-pas-b-small-molecule-inhibition]]
- [[concepts/tumor-hypoxia-classification-chronic-acute-cyclic]]
- [[concepts/kdm-direct-oxygen-sensing-hif-independent]]
- [[concepts/sirpa-cd47-don-t-eat-me-axis]]
- [[concepts/macrophage-induced-emt-tumor-invasiveness]]
- [[concepts/m1-m2-polarization-paradigm]]
- [[concepts/tumor-hypoxia-intratumoral-heterogeneity]]
- [[foundations/hif1a]]
- [[foundations/vhl-von-hippel-lindau]]
- [[foundations/phd-prolyl-hydroxylases]]
- [[foundations/belzutifan-mk-6482]]
- [[foundations/pt2385-hif2a-inhibitor]]
- [[foundations/px-478-hif1a-inhibitor]]
- [[foundations/vegf]]
- [[foundations/cxcl8-il8]]
- [[foundations/ccl2-mcp1]]
- [[foundations/oncostatin-m-osm]]
- [[foundations/galectin-3]]
- [[foundations/sucnr1-succinate-receptor]]
- [[foundations/nf-kb-p65-rela]]
- [[foundations/pten-tumor-suppressor]]
- [[foundations/lps-toll-like-receptor-signaling]]
- [[people/ruixue-bai]]
- [[people/lin-zhao]]
- [[people/minjie-wei]]
