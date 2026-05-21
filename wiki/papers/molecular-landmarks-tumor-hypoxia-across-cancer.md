---
# === Identification ===
title: "Molecular landmarks of tumor hypoxia across cancer types"
slug: molecular-landmarks-tumor-hypoxia-across-cancer
arxiv: ""
doi: "10.1038/s41588-018-0318-2"
pmid: "30643250"
venue: "Nature Genetics"
year: 2019
authors:
  - "Vinayak Bhandari"
  - "Christianne Hoey"
  - "Lydia Y. Liu"
  - "Emilie Lalonde"
  - "Jessica Ray"
  - "Julie Livingstone"
  - "Robert Lesurf"
  - "Yu-Jia Shiah"
  - "Tina Vujcic"
  - "Xiaoyong Huang"
  - "Shadrielle M. G. Espiritu"
  - "Lawrence E. Heisler"
  - "Fouad Yousif"
  - "Vincent Huang"
  - "Takafumi N. Yamaguchi"
  - "Cindy Q. Yao"
  - "Veronica Y. Sabelnykova"
  - "Michael Fraser"
  - "Melvin L. K. Chua"
  - "Theodorus van der Kwast"
  - "Stanley K. Liu"
  - "Paul C. Boutros"
  - "Robert G. Bristow"
first_author: "Vinayak Bhandari"
corresponding_author: "Paul C. Boutros; Robert G. Bristow"

# === Source & metadata ===
source_type: pdf
s2_id: "e1591572826fbcc0f74fdce676e57bf75a221b4c"
date_added: 2026-05-06
ingested_date: 2026-05-11
ingest_version: 2
last_reviewed: null

# === Classification ===
importance: 5
tier: TIER_1
tags:
  - hypoxia
  - cancer
  - genomics
  - pancancer
  - prostate-cancer
  - TCGA
  - genomic-instability
  - microRNA
  - TP53
  - PTEN
  - HIF1a
  - subclonal-evolution
  - chromothripsis
  - telomere
keywords:
  - tumor hypoxia
  - mRNA hypoxia signature
  - Buffa signature
  - pancancer
  - intratumoral heterogeneity
  - TP53 mutation
  - PTEN loss
  - MYC gain
  - miR-210
  - miR-133a-3p
  - chromothripsis
  - intraductal carcinoma
  - nimbosus
  - subclonal architecture
  - telomere length
  - TERT
  - HIF1A target
domain: "oncology / genomics / hypoxia"

# === Biomedical domain ===
tissue:
  - multi
  - prostate
  - breast
  - lung
  - kidney
  - liver
  - pancreas
  - colon
  - ovary
  - bladder
  - thyroid
  - cervix
  - skin
  - brain
  - stomach
  - in_vitro_only
condition:
  - cancer
disease_specific:
  - prostate_adenocarcinoma_PRAD
  - breast_invasive_carcinoma_BRCA
  - lung_adenocarcinoma_LUAD
  - lung_squamous_cell_LUSC
  - renal_clear_cell_carcinoma_KIRC
  - renal_papillary_KIRP
  - liver_hepatocellular_LIHC
  - pancreatic_adenocarcinoma_PAAD
  - head_and_neck_squamous_HNSC
  - cervical_squamous_CESC
  - thyroid_carcinoma_THCA
  - lower_grade_glioma_LGG
  - glioblastoma_GBM
  - colorectal_COADREAD
  - bladder_urothelial_BLCA
  - ovarian_serous_OV
  - skin_cutaneous_melanoma_SKCM
  - uterine_corpus_endometrial_UCEC
  - pheochromocytoma_paraganglioma_PCPG
species:
  - human
hypoxia_relevant: true
contains_immune_cells: false
contains_myeloid: false

# === Technique ===
techniques:
  - bulk_RNA-seq
  - microarray_mRNA_expression
  - miRNA_expression
  - whole_exome_sequencing
  - whole_genome_sequencing
  - copy_number_aberration_analysis
  - SNV_calling
  - reverse_phase_protein_array_RPPA
  - cell_culture_PC3_DU145_22Rv1
  - miRNA_mimic_transfection
  - cell_invasion_assay
  - cell_viability_assay
  - Mann_Whitney_U_test
  - Kruskal_Wallis_test
  - Spearman_correlation
  - Bonferroni_correction
  - AS89_algorithm
  - consensus_clustering
  - Fisher_exact_test
  - linear_modelling
  - Cox_proportional_hazards
  - Kaplan_Meier
n_samples: 8006
n_cells_total: null
integration_method: ""

# === Biology captured ===
key_cell_types:
  - tumor_epithelial_cell
  - prostate_cancer_cell_PC3
  - prostate_cancer_cell_DU145
  - prostate_cancer_cell_22Rv1
key_markers:
  - HIF1A
  - TP53
  - PTEN
  - MYC
  - TERT
  - CDKN2A
  - APC
  - MYCN
  - PIK3CA
  - BCL6
  - SPOP
  - LDHA
  - GPI
  - PFKP
  - ERO1L
  - VEGFA
  - PDK1
  - PGK1
  - GAPDH
  - miR-210
  - miR-133a-3p
  - miR-30a-3p
  - miR-15b-5p
  - BIN1
  - PGM5
  - WDR33
  - LDB3
  - CAIX
key_pathways:
  - HIF1A_target_genes
  - hypoxia_glycolysis
  - DNA_damage_response
  - DNA_repair_RAD51_MLH1_MSH2
  - chromothripsis
  - PTEN_PI3K_AKT
  - p53_pathway
  - telomere_maintenance_TERT
  - microRNA_regulation

# === User project membership ===
projects:
  - hypoxia
  - thesis
priority: core
read_status: deep_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: included
exclusion_reason: null
data_availability: "TCGA (https://portal.gdc.cancer.gov/), CPC-GENE (ICGC PRAD-CA), Taylor cohort. Code: doi.org/10.17605/OSF.IO/XEPRY referenced; Custom CDF files at http://brainarray.mbni.med.umich.edu/Brainarray/Database/CustomCDF/CDF_download.asp"

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Tumor hypoxia — regions of low oxygen within solid tumors — is a known clinical adverse and targetable feature found in roughly half of all solid tumors, but the *molecular* hallmarks of hypoxia across tumor types remain poorly defined. Prior studies had measured hypoxia in single tumor types or with single signatures, leaving open whether hypoxia (i) shapes the somatic genome (mutations, CNAs), (ii) acts uniformly or in tumor-type-specific ways, (iii) interacts with subclonal evolutionary timing, and (iv) modulates clinical trajectory beyond its known prognostic effect. The paper aims to fill this gap with a pancancer quantification across 19 tumor types and 8,006 tumors, focusing in depth on localized prostate cancer where matched whole-genome sequencing and direct intratumoral oxygen measurements are available.

## Key idea

mRNA-based hypoxia scores can be computed across heterogeneous TCGA cancer types and consistently associate with a constellation of aggressive molecular features (genomic instability, TP53 SNVs, MYC gains, PTEN loss, miRNA dysregulation, and in localized prostate cancer chromothripsis, allelic PTEN loss, shorter telomeres, and intraductal/cribriform carcinoma). The concurrence of these features in hypoxic prostate tumors defines a new aggressive cellular phenotype the authors name "nimbosus" (Latin: gathering of stormy clouds). Hypoxia-associated copy-number aberrations preferentially occur in the trunk of tumor evolution, supporting a model in which hypoxia exerts an *early* selective pressure that fixes aggressive somatic alterations.

## Method

- **Cohorts**: 8,006 tumors across 19 TCGA tumor types plus the CPC-GENE (Canadian Prostate Cancer Genome Network) cohort with matched WGS + direct oxygen (Eppendorf needle electrode) measurements; Taylor et al. prostate cohort for orthogonal validation.
- **Hypoxia quantification**: mRNA-based Buffa metagene as primary signature; eight independent signatures (Buffa, Winter, Ragnum, West, Sorensen, Elvidge, Hu, Seigneuric) integrated via algorithm AS89; pancancer scores correlated ρ=0.42±0.21.
- **Protein-based hypoxia**: reverse-phase protein array (RPPA) signatures derived for BRCA, OV, COADREAD where data were available; correlated against mRNA scores.
- **Genomic features**: percentage of genome altered (PGA, surrogate of genomic instability), SNV calls in 253 cancer driver genes, CNAs in 112 driver genes, miRNA expression for ~784 miRNAs, chromothripsis calls, kataegis, structural variants, telomere length estimated by TelSeq.
- **Statistics**: Mann–Whitney U test (SNV vs WT comparisons), Kruskal–Wallis (multi-group), Spearman ρ for continuous correlations, Fisher's exact test for CNA enrichment, Bonferroni correction for multiple testing, AS89 algorithm for adjusted P-value computation.
- **Subclonal architecture**: 191 localized prostate tumors with reconstructed subclonal architecture (PhyloWGS-style) used to map hypoxia-associated CNAs to trunk vs branch evolutionary timing.
- **In vitro validation of miR-133a-3p**: 3 prostate cancer cell lines (22Rv1, DU145, PC3) exposed to 1% O₂ for 72h. miR-210-3p (positive control) measured. miR-133a-3p mimic transfected; viability and invasion assays performed.
- **Telomere modelling**: linear model with telomere length as outcome, hypoxia score, PTEN mRNA, TERT mRNA, and pairwise/three-way interactions as predictors, in 333 TCGA / 215 CPC-GENE PRAD samples.

## Results

- Squamous tumors of head/neck (HNSC), cervix (CESC), and lung (LUSC) are the *most* hypoxic; thyroid (THCA) and prostate (PRAD) adenocarcinomas the *least* hypoxic (Fig. 1a).
- 42% of variance in hypoxia scores lies *within* tumor types rather than between them; LUAD (IQR=38), PAAD (IQR=32), BRCA (IQR=32) show especially high intertumoral variability (Fig. 1a).
- Among breast cancers, tumors in subjects of Caucasian ancestry have lower hypoxia than tumors in Asian or African-ancestry subjects (median White=−7, Asian=11, Black=13; Bonferroni P=4.08×10⁻¹³, Fig. 1b) — this may explain higher efficacy of evofosfamide in Asian-descent subjects in MAESTRO.
- Hypoxia is associated with elevated PGA (genomic instability) in 10 of 19 tumor types (Fig. 1c).
- TP53 SNVs are recurrently associated with hypoxia in BRCA (Bonferroni P=4.38×10⁻⁶¹), LUAD (P=1.83×10⁻¹²), LIHC (P=1.64×10⁻⁵), HNSC (P=2.26×10⁻³), localized PRAD (P=8.58×10⁻²), and a subtype of BRCA both with and without TP53 SNVs (Fig. 2a).
- BRCA-specific: hypoxic tumors enriched for APC loss (P=1.25×10⁻⁴²), MYCN gain (P=2.75×10⁻³²), TP53 protein abundance increase (P=1.96×10⁻², ρ=0.28).
- LUAD-specific: BCL6 SNVs (P=3.24×10⁻⁷), PIK3CA SNVs (P=2.93×10⁻⁶) associated with hypoxia.
- KIRC-specific: loss of CDKN2A (P=1.40×10⁻⁹), gain of MYC (P=3.71×10⁻⁸) associated with hypoxia.
- Pancancer: gain of MYC associated with hypoxia in 11 tumor types; loss of PTEN in 7 tumor types (Fig. 2b).
- 51 of 85 HIF1A target genes correlate strongly with hypoxia score in either CPC-GENE or TCGA prostate (Fig. 5a).
- 658 of 784 miRNAs correlate with hypoxia in at least one tumor type. miR-210 is positively associated with hypoxia in 18 of 19 tumor types (Spearman ρ range 0.20–0.66) (Fig. 2c).
- miR-210 abundance correlates with LDHA protein abundance in BRCA (ρ=0.72, FDR=5.66×10⁻⁷) and OV (ρ=0.42, FDR=6.21×10⁻⁴), consistent with HIF1A-driven glycolytic remodelling.
- miR-133a-3p is the strongest hypoxia-associated miRNA in localized PCa (TCGA: FDR=2.08×10⁻¹¹, ρ=−0.40), validated in CPC-GENE (n=170; FDR=4.83×10⁻³, ρ=−0.22), and Taylor (n=97; FDR=1.17×10⁻², ρ=−0.26) cohorts (Fig. 3a–c).
- In vitro: miR-210-3p elevated under 1% O₂ in 22Rv1, DU145, PC3 (positive control); miR-133a-3p significantly *decreased* in DU145 and PC3 under hypoxia. Reintroducing miR-133a-3p mimic decreased viability in all three lines and decreased PC3 invasion (P=5.45×10⁻³, t=2.78, Fig. 3e–g).
- Localized PCa: hypoxia associated with chromothripsis (Bonferroni P=2.69×10⁻²), elevated SNV burden (P=2.52×10⁻², ρ=0.26), elevated PGA (P=3.55×10⁻⁵, ρ=0.24).
- Hypoxia-associated CNAs preferentially in chromosome 7 (P=7.62×10⁻²²⁴) and chromosome 10 (P=1.41×10⁻³², Supplementary Fig. 6a). 1,189 CNA-hypoxia associations identified (FDR<0.10).
- Allelic loss of PTEN in localized PCa: FDR=2.69×10⁻⁴, OR=3.50 (95% CI 2.14–5.79); validated in TCGA (P=1.26×10⁻⁵), CPC-GENE (P=9.26×10⁻¹¹), and a third cohort of n=130 (Spearman ρ=−0.41, P=9.65×10⁻⁷).
- Hypoxia + PTEN loss synergistically predict 2-year biochemical relapse (HR=4.4, 95% CI 1.7–11.0, P=1.95×10⁻³), even after controlling for T category, Gleason, PSA.
- TERT mRNA is negatively correlated with PTEN mRNA in localized PCa (CPC-GENE ρ=−0.36, P=4.01×10⁻⁸; TCGA ρ=−0.15, P=7.21×10⁻³).
- Telomere modelling: hypoxia score, PTEN, and TERT individually and their three-way interaction significantly predict telomere length (interaction Bonferroni P=4.34×10⁻², linear model P=2.17×10⁻³, Fig. 5e); lowest PTEN observed in tumors with high hypoxia + high TERT.
- 99% (660 of 667) of hypoxia-associated CNAs occur preferentially in the *trunk* of tumor evolution (observed/expected = 73, P=6.71×10⁻²⁴⁹), supporting hypoxia as an *early* selective pressure (Fig. 6b).
- Among 108 polyclonal PCa tumors: hypoxic polyclonal samples enriched for IDC-CA (OR=3.27, P=0.024), allelic PTEN loss (OR=3.41, P=6.15×10⁻³), and lower PTEN mRNA (P=3.05×10⁻⁵).
- Subjects with hypoxia + IDC-CA + PTEN deletion have HR=11.10 (95% CI 3.02–47.27, P=3.15×10⁻⁵) for poor 5-year biochemical relapse-free outcome (Fig. 6h–i). The authors name this constellation "nimbosus".
- SPOP, the most frequent SNV in localized PCa, is *not* associated with hypoxia.

## All claims (exhaustive)

- `[c01]` Hypoxia was quantified in 8,006 tumors across 19 tumor types using mRNA-based Buffa metagene with 8 independent signatures integrated via AS89 algorithm (p.308) "we evaluated tumor hypoxia in 8,006 tumors representing 19 distinct tumor types to create a pancancer quantification of this environmental cancer hallmark" — confidence: high — type: methodological — links: [[concepts/tumor-hypoxia-mrna-signature]] [[foundations/buffa-hypoxia-signature]] [[claims/hypoxia-elevates-genomic-instability-pancancer]]
- `[c02]` Pancancer hypoxia scores from 8 independent signatures are strongly correlated (ρ=0.42 ± 0.21) (p.309) "Pancancer hypoxia scores from the eight independent signatures were strongly correlated (ρ=0.42±0.21, mean±s.d.; algorithm AS89)" — confidence: high — type: quantitative — links: [[concepts/tumor-hypoxia-mrna-signature]] [[claims/hypoxia-elevates-genomic-instability-pancancer]]
- `[c03]` Squamous tumors of head/neck (HNSC), cervix (CESC), and lung (LUSC) are most hypoxic; thyroid (THCA) and prostate (PRAD) adenocarcinomas least hypoxic (p.309) "squamous cell tumors of the head and neck (HNSC), cervix (CESC) and lung (LUSC) were the most hypoxic, whereas adenocarcinomas of the thyroid (THCA) and prostate (PRAD) were the least hypoxic" — confidence: high — type: correlational — links: [[concepts/tumor-hypoxia-mrna-signature]] [[claims/hypoxia-elevates-genomic-instability-pancancer]]
- `[c04]` 42% of variance in hypoxia scores lies within tumor types rather than between them (p.309) "42% of the variance in hypoxia scores lies within individual tumor types rather than between them" — confidence: high — type: quantitative — links: [[concepts/tumor-hypoxia-intratumoral-heterogeneity]] [[claims/hypoxia-elevates-genomic-instability-pancancer]]
- `[c05]` Intertumoral hypoxia variability is particularly pronounced in LUAD (IQR=38), PAAD (IQR=32), BRCA (IQR=32) (p.309) "Intertumoral variability in hypoxia was particularly pronounced in adenocarcinomas of the lung (interquartile range (IQR)=38) and pancreas (PAAD; IQR=32) and in breast tumors (BRCA; IQR=32)" — confidence: high — type: quantitative — links: [[concepts/tumor-hypoxia-intratumoral-heterogeneity]] [[claims/hypoxia-elevates-genomic-instability-pancancer]]
- `[c06]` Tumors in subjects of Caucasian ancestry have lower hypoxia than tumors in subjects of Asian or African ancestry in BRCA (Bonferroni P=4.08×10⁻¹³) (p.309) "tumors arising in subjects of Caucasian ancestry had less hypoxia than tumors in subjects with either Asian or African ancestry (Bonferroni-adjusted P=4.08×10⁻¹³, Kruskal–Wallis test)" — confidence: high — type: quantitative — links: [[concepts/ancestry-specific-tumor-hypoxia]] [[claims/ancestry-disparity-tumor-hypoxia-brca]]
- `[c07]` Hypoxia is associated with elevated genomic instability (PGA) in 10 of 19 tumor types (p.309) "Tumor hypoxia was associated with significantly elevated genomic instability in 10 of 19 tumor types, and in no case was tumor hypoxia associated with decreased genomic instability" — confidence: high — type: correlational — links: [[concepts/hypoxia-genomic-instability-pga]] [[claims/hypoxia-elevates-genomic-instability-pancancer]]
- `[c08]` In BRCA, hypoxic tumors enriched for TP53 SNVs (Bonferroni P=4.38×10⁻⁶¹, Mann–Whitney U test) (p.309) "Hypoxic breast tumors also showed an elevated rate of TP53 point mutations (Bonferroni-adjusted P=4.38×10⁻⁶¹, Mann–Whitney U test)" — confidence: high — type: quantitative — links: [[claims/tp53-snvs-recurrently-associated-with-hypoxia]] [[foundations/tp53-tumor-suppressor]]
- `[c09]` In BRCA, hypoxic tumors more likely to harbor APC loss (Bonferroni P=1.25×10⁻⁴²) and MYCN gain (P=2.75×10⁻³²) (p.309) "hypoxic tumors were more likely to harbor loss of APC (Bonferroni-adjusted P=1.25×10⁻⁴²) and gain of MYCN (Bonferroni-adjusted P=2.75×10⁻³²)" — confidence: high — type: quantitative — links: [[claims/myc-gain-co-occurs-hypoxia-pancancer]] [[claims/hypoxia-elevates-genomic-instability-pancancer]]
- `[c10]` In LUAD, BCL6 SNVs (Bonferroni P=3.24×10⁻⁷) and PIK3CA SNVs (P=2.93×10⁻⁶) associated with hypoxia (p.309) "Hypoxic lung adenocarcinomas were additionally associated with gain of BCL6 (Bonferroni-adjusted P=3.24×10⁻⁷)" — confidence: high — type: quantitative — links: [[claims/hypoxia-elevates-genomic-instability-pancancer]]
- `[c11]` In KIRC, loss of CDKN2A (Bonferroni P=1.40×10⁻⁹) and gain of MYC (Bonferroni P=3.71×10⁻⁸) associated with hypoxia (p.309) "hypoxia was associated with loss of CDKN2A (Bonferroni-adjusted P=1.40×10⁻⁹) and gain of MYC (Bonferroni-adjusted P=3.71×10⁻⁸)" — confidence: high — type: quantitative — links: [[foundations/cdkn2a-tumor-suppressor]] [[foundations/myc-oncogene]] [[claims/myc-gain-co-occurs-hypoxia-pancancer]]
- `[c12]` Pancancer: MYC oncogene gain associated with elevated hypoxia in 11 tumor types; PTEN loss in 7 (p.309) "gain of the MYC oncogene was associated with elevated hypoxia in 11 separate tumor types, whereas loss of the tumor-suppressor gene PTEN was associated with elevated hypoxia in seven tumor types" — confidence: high — type: correlational — links: [[foundations/myc-oncogene]] [[foundations/pten-tumor-suppressor]] [[claims/myc-gain-co-occurs-hypoxia-pancancer]]
- `[c13]` miR-210 abundance is positively correlated with hypoxia score in 18 of 19 tumor types (Spearman ρ range 0.20–0.66) (p.311) "miR-210 abundance was associated with elevated hypoxia score across all 18 tumor types (Spearman's ρ range=0.20–0.66)" — confidence: high — type: quantitative — links: [[concepts/mir-210-hypoxia-induced-microrna]] [[foundations/mir-210-mirna]] [[claims/mir-210-induced-under-hypoxia-pancancer]]
- `[c14]` miR-210 abundance correlates with LDHA protein in BRCA (ρ=0.72, FDR=5.66×10⁻⁷) and OV (ρ=0.42, FDR=6.21×10⁻⁴) (p.311) "miR-210 abundance is positively correlated with the protein abundance of LDHA in breast cancer (ρ=0.72, FDR=5.66×10⁻⁷, AS89; Supplementary Fig. 4s) and ovarian cancer (ρ=0.42, FDR=6.21×10⁻⁴)" — confidence: high — type: quantitative — links: [[concepts/mir-210-hypoxia-induced-microrna]] [[claims/mir-210-induced-under-hypoxia-pancancer]]
- `[c15]` miR-133a-3p is the strongest hypoxia-associated miRNA in TCGA localized prostate cancer (FDR=2.08×10⁻¹¹, ρ=−0.40) (p.311–312) "In the TCGA data, miR-133a-3p was the strongest hypoxia-associated miRNA (FDR=2.08×10⁻¹¹, ρ=−0.40, AS89)" — confidence: high — type: quantitative — links: [[concepts/mir-133a-3p-hypoxia-prostate]] [[foundations/mir-133a-3p-mirna]] [[claims/mir-133a-3p-tumor-suppressor-prostate-hypoxia]]
- `[c16]` miR-133a-3p hypoxia association replicated in CPC-GENE (n=170, FDR=4.83×10⁻³, ρ=−0.22) and Taylor (n=97, FDR=1.17×10⁻², ρ=−0.26) prostate cohorts (p.312) "we confirmed that the abundance of miR-133a-3p was also significantly associated with hypoxia in the CPC-GENE cohort … and a third independent cohort with 97 subjects" — confidence: high — type: quantitative — links: [[concepts/mir-133a-3p-hypoxia-prostate]] [[claims/mir-133a-3p-tumor-suppressor-prostate-hypoxia]]
- `[c17]` miR-133a-3p mimic significantly decreased PC3 cell invasion (P=5.45×10⁻³, t=2.78, paired Student's t test) (p.312) "Introducing a miR-133a-3p mimic significantly decreased the invasive ability of PC3 cells (P=5.45×10⁻², t=2.78, Student's t test, Fig. 3g)" — confidence: high — type: pharmacological — links: [[concepts/mir-133a-3p-hypoxia-prostate]] [[claims/mir-133a-3p-tumor-suppressor-prostate-hypoxia]]
- `[c18]` miR-133a-3p mimic decreased viability in 22Rv1, DU145, PC3 (P_22Rv1=3.69×10⁻³, P_DU145=5.02×10⁻², P_PC3=1.50×10⁻²) (p.312) "introduction of a miR-133a-3p mimic significantly decreased cell viability in all the cell lines (P_22Rv1=3.69×10⁻³ … P_PC3=1.50×10⁻²)" — confidence: high — type: pharmacological — links: [[concepts/mir-133a-3p-hypoxia-prostate]] [[claims/mir-133a-3p-tumor-suppressor-prostate-hypoxia]]
- `[c19]` In localized PCa, hypoxia is associated with elevated rates of chromothripsis (Bonferroni P=2.69×10⁻²), elevated SNV burden (P=2.52×10⁻², ρ=0.26), and elevated PGA (Bonferroni P=3.55×10⁻⁵, ρ=0.24) (p.313) "elevated PGA was associated with higher levels of tumor hypoxia (Bonferroni-adjusted P=3.55×10⁻⁵, ρ=0.24, AS89; Fig. 4a). Additionally, catastrophic chromothriptic events (Bonferroni-adjusted P=2.69×10⁻², Mann–Whitney U test) and the total burden of somatic SNVs (Bonferroni-adjusted P=2.52×10⁻², ρ=0.26)" — confidence: high — type: quantitative — links: [[concepts/chromothripsis-hypoxia-prostate]] [[claims/hypoxia-elevates-genomic-instability-pancancer]]
- `[c20]` In localized PCa, allelic loss of PTEN strongly correlated with elevated tumor hypoxia (FDR=2.69×10⁻⁴, OR=3.50, 95% CI 2.14–5.79) (p.314) "allelic loss of the tumor suppressor PTEN, which was correlated with significantly elevated tumor hypoxia (FDR=2.69×10⁻⁴, odds ratio (OR)_loss/neutral=3.50, 95% confidence interval (CI), 2.14–5.79, Fisher's exact test)" — confidence: high — type: quantitative — links: [[foundations/pten-tumor-suppressor]] [[claims/pten-loss-co-occurs-with-hypoxia-localized-pca]]
- `[c21]` PTEN loss + hypoxia synergistically predict 2-year biochemical relapse in PCa (HR=4.4, 95% CI 1.7–11.0, P=1.95×10⁻³) (p.314) "subjects whose prostate tumors had both loss of PTEN and high hypoxia were significantly higher risk of biochemical relapse within 2 years … (hazard ratio=4.4, 95% CI 1.7–11.0, P=1.95×10⁻³, Wald test)" — confidence: high — type: quantitative — links: [[claims/pten-loss-co-occurs-with-hypoxia-localized-pca]]
- `[c22]` PTEN mRNA negatively correlates with TERT mRNA in localized PCa (CPC-GENE ρ=−0.36, P=4.01×10⁻⁸; TCGA ρ=−0.15, P=7.21×10⁻³) (p.314) "PTEN mRNA abundance was negatively correlated with the mRNA abundance of TERT, a HIF1A target, in CPC-GENE (ρ=−0.36, p=4.01×10⁻⁸, AS89)" — confidence: high — type: correlational — links: [[concepts/hypoxia-pten-tert-telomere-axis]] [[claims/hypoxia-pten-tert-three-way-telomere-interaction]]
- `[c23]` Hypoxia × TERT × PTEN three-way interaction significantly predicts telomere length (Bonferroni P=4.34×10⁻², linear model) (p.314) "a model incorporating hypoxia, PTEN and TERT mRNA abundance demonstrated a significant interaction between these features in modulating telomere length (Bonferroni-adjusted P_interaction=4.34×10⁻², linear model)" — confidence: high — type: quantitative — links: [[concepts/hypoxia-pten-tert-telomere-axis]] [[claims/hypoxia-pten-tert-three-way-telomere-interaction]]
- `[c24]` 99% (660/667) of hypoxia-associated CNAs preferentially occur early in tumor evolution (in trunk; observed/expected=73, P=6.71×10⁻²⁴⁹) (p.314) "99% (660 of 667) of the CNAs associated with hypoxia, including PTEN, that showed biased evolutionary timing preferentially occured early during tumor evolution" — confidence: high — type: quantitative — links: [[concepts/tumor-subclonal-evolution-architecture]] [[claims/hypoxia-cnas-occur-early-trunk-evolution]]
- `[c25]` Hypoxic polyclonal PCa tumors enriched for IDC-CA (OR=3.27, 95% CI 1.09–10.31, P=0.024, Fisher's exact test) (p.316) "Indeed, polyclonal samples with high hypoxia were also significantly enriched for IDC-CA (OR=3.27, 95% CI 1.09–10.31, P=0.024)" — confidence: high — type: quantitative — links: [[concepts/intraductal-cribriform-carcinoma]] [[claims/nimbosus-aggressive-pca-phenotype]]
- `[c26]` Hypoxic polyclonal PCa tumors enriched for allelic loss of PTEN (OR=3.41, 95% CI 1.32–9.34, P=6.15×10⁻³) (p.316) "Polyclonal tumors that are hypoxic are enriched for allelic loss of PTEN (n=103 independent tumors)" — confidence: high — type: quantitative — links: [[claims/nimbosus-aggressive-pca-phenotype]] [[claims/pten-loss-co-occurs-with-hypoxia-localized-pca]]
- `[c27]` Subjects with hypoxia + IDC-CA + PTEN deletion have HR=11.10 (95% CI 3.02–47.27, P=3.15×10⁻⁵) for poor 5-year biochemical relapse-free outcome (p.317) "PTEN-deleted tumors were significantly more likely to harbor both hypoxia and IDC-CA (OR=11.10, 95% CI 3.02–47.27, P=3.15×10⁻⁵, Fisher's exact test; Fig. 6g)" — confidence: high — type: quantitative — links: [[concepts/nimbosus-aggressive-prostate-phenotype]] [[claims/nimbosus-aggressive-pca-phenotype]]
- `[c28]` Constellation of hypoxia + PTEN loss + mutant TP53 + chromothripsis + shorter telomeres + IDC-CA defines the proposed "nimbosus" aggressive phenotype in localized PCa (p.317) "a constellation of co-occurring molecular features (nimbosus) are associated with aggressive disease, including hypoxia, mutant TP53, allelic loss of PTEN, chromothripsis and shorter telomeres" — confidence: high — type: mechanistic — links: [[concepts/nimbosus-aggressive-prostate-phenotype]] [[claims/nimbosus-aggressive-pca-phenotype]]
- `[c29]` SPOP (most common SNV in localized PCa) is not associated with hypoxia (p.314) "SPOP, the gene most frequently altered by somatic SNVs in localized prostate cancers, was not associated with hypoxia" — confidence: high — type: correlational — links: [[claims/hypoxia-elevates-genomic-instability-pancancer]]
- `[c30]` Mitochondrial mutations associated with elevated hypoxia in PCa (P=0.048, Kruskal–Wallis) (p.314) "Tumors with mitochondrial genome mutations previously associated with poor prognosis also had elevated hypoxia (P=0.048, Kruskal–Wallis test)" — confidence: medium — type: correlational — links: [[claims/hypoxia-elevates-genomic-instability-pancancer]]
- `[c31]` 51 of 85 HIF1A target genes correlate with hypoxia score in TCGA or CPC-GENE prostate cohorts (p.314) "We associated hypoxia scores with the mRNA abundance of HIF1A-activated genes and observed a strong correlation for 51 of 85 HIF1A targets" — confidence: high — type: methodological — links: [[foundations/hif1a]] [[claims/hypoxia-elevates-genomic-instability-pancancer]]

## Discussion captured

### Authors' interpretation

- Tissue hypoxia is "an important differentiating metabolic characteristic between normal and malignant tissues" that "leads to aggressive tumor cell phenotypes."
- Subsets of patients with a range of solid tumors with genetic instability may benefit from hypoxia-targeting therapy; clinical trials of hypoxia-targeting agents should focus on solid tumors with elevated hypoxia AND associated genetic instability — analogous to how targeted-therapy trials select on a specific mutation.
- "TP53 mutations are enriched in hypoxic tumors within each breast cancer subtype, thus supporting the idea that they are a genomic consequence of tumor hypoxia."
- HIF1A stabilization may be mediated downstream of PTEN loss (citing Zundel et al. 2000 Genes Dev), making the in vivo hypoxia-PTEN-HIF1A relationship complex.
- A model of prostate cancer aggression under hypoxia: hypoxia applies a selective pressure; surviving subclones with aggressive features (PTEN loss + mutant TP53) rapidly expand after normoxia is reestablished, culminating in poor prognosis. This is supported by Hong et al. 2015 longitudinal analysis showing TP53 mutations in primary tumors enriched in matched metastatic samples.

### Comparisons with prior literature (made by authors)

- Wilson & Hay 2011 (Nat Rev Cancer) and Harris 2002 (Nat Rev Cancer) cited as foundational reviews of hypoxia targeting and HIF biology.
- Bristow & Hill 2008 (Nat Rev Cancer) cited as prior work on hypoxia, DNA repair, and genetic instability.
- Bindra et al. 2004 (Mol Cell Biol) for RAD51 down-regulation and decreased homologous recombination in hypoxic cancer cells.
- Mihaylova 2003 (Mol Cell Biol) and Koshiji 2005 (Mol Cell) for MLH1/MSH2 down-regulation and HIF-1α-induced genetic instability via mismatch-repair downregulation.
- Buffa et al. 2010 (Br J Cancer), Winter et al. 2007, Ragnum et al. 2015 cited as the canonical mRNA hypoxia signatures used.
- Eustace et al. 2013 (Clin Cancer Res) for the laryngeal hypoxia signature predicting carbogen-nicotinamide benefit; Janssens et al. 2012 (J Clin Oncol) for the original phase III trial; Hoskin et al. 1997, 2010 (J Clin Oncol) for bladder hypoxia targeting.
- Lalonde et al. 2014 (Lancet Oncol), 2017 (Eur Urol) for prior CPC-GENE findings on tumor genomic and microenvironmental heterogeneity in localized PCa.
- Chua et al. 2017 (Eur Urol) for the prior introduction of the IDC-CA / nimbosus concept in prostate cancer.
- Fraser et al. 2017 (Nature) and Espiritu 2018 for whole-genome architecture of localized non-indolent prostate cancer.
- Zundel et al. 2000 (Genes Dev) for "Loss of PTEN facilitates HIF-1-mediated gene expression."
- Hong et al. 2015 (Nat Commun) for tracking the origins and drivers of subclonal metastatic expansion in prostate cancer.
- Sakamuro et al. 1996 (Nat Genet) for BIN1 as a MYC-interacting protein with tumor-suppressor features.
- Greijer & van der Wall 2004 (J Clin Pathol) and Graeber 1996 (Nature) cited as foundational for hypoxia-mediated apoptosis selection.

### Mechanistic hypotheses proposed

- "TP53 mutations may be a genomic consequence of tumor hypoxia" rather than independent of it.
- "Loss of PTEN may preferentially occur in hypoxic tumors, as either an adaptive or a selective effect" associated with elevated genomic instability and aggressive disease.
- The nimbosus model: hypoxia + mutant TP53 + PTEN loss + IDC-CA jointly reflect tumor evolution under hostile microenvironment selective pressure; reoxygenation after this selective bottleneck enables rapid expansion of aggressive subclones.
- Hypoxia exerts selection pressure *early* in tumor evolution (trunk timing of CNAs, monoclonal hypoxia features mirroring polyclonal ones).

### Caveats and self-criticism

- "tumor hypoxia did not vary with either of these features (sex/age at diagnosis)" — limited statistical power for ancestry except in BRCA where sample size was twice that of any other cancer type.
- "Variability in hypoxia within a tumor type was not associated with the median level of hypoxia within that tumor type" — limits inferences across tumor types.
- The hypoxia-mutation associations bridged across BRCA subtypes — generalizable but each subtype association was less than the combined.
- Limited statistical power for ancestry in non-BRCA tumor types.
- The paper is descriptive/correlational at the pancancer level; in vitro validation was limited to miR-133a-3p in PCa cell lines.

### Future directions suggested

- "this work could be further extended to further examine the somatic-mutational architecture of other cancer types, such as pediatric tumors, in relation to hypoxia in large, well-powered data sets."
- "additional work should characterize the role of these miRNAs in canonical hypoxia-response pathways."
- Validation of ancestry-specific hypoxia in independent large cohorts (impacts evofosfamide trial design).
- Prospective biomarker development integrating hypoxia, PTEN status, IDC-CA, and TP53 mutation for high-risk PCa stratification.
- "careful in vitro modeling is required to delineate the relationship between these features [PTEN loss and HIF1A]" — i.e. dedicated mechanistic work on PTEN-HIF1A axis in PCa.

## Limitations

- Hypoxia is measured by mRNA-based signature, not direct oxygen measurement — except in CPC-GENE (Eppendorf needle electrode subset).
- Pancancer analysis is on TCGA, which is biased toward primary, treatment-naive tumors; metastatic and treated samples under-represented.
- Cell-line in vitro validation only for miR-133a-3p, only in 3 PCa lines.
- The "nimbosus" framework is descriptive — directly testing causality (does hypoxia *cause* PTEN loss?) requires longitudinal patient-derived models or genetically engineered systems.
- Ancestry analysis confined to BRCA due to sample-size limits elsewhere.
- Cross-cancer comparisons of hypoxia score are valid only because all 8 signatures gave highly correlated rankings; absolute values are signature-dependent.
- Subclonal architecture analysis limited to 191 tumors with reconstructed phylogenies; trunk/branch annotation depends on phylogeny accuracy.

## Open questions

### Open questions raised by authors

- Does the ancestry-specific hypoxia signal in BRCA reflect biology or socioeconomic confounding (selection bias in TCGA)?
- Are the hypoxia-mutation co-occurrences causally linked, or co-selected by independent microenvironmental pressures?
- Can the nimbosus signature drive treatment-decision prospective trials in localized PCa?
- What is the role of hypoxia-modulated miRNAs (beyond miR-210, miR-133a-3p) in canonical HIF1A-response pathways?
- How does hypoxia drive trunk-timing of CNA fixation mechanistically?
- Does hypoxia targeting (evofosfamide, etc.) work better in non-Caucasian patients, as implied by MAESTRO post-hoc analyses?

### Open questions identified during ingest

- The paper focuses on epithelial tumor genomics; the *immune-microenvironment* coupling of hypoxia (HIF1α in macrophages, mMAC1 phenotype) is not addressed and is the topic of complementary work in this wiki ([[papers/nf-kb-tet2-promote-macrophage-reprogramming]]). Does the nimbosus signature correlate with hypoxic-macrophage infiltration?
- TCGA bulk mRNA confounds tumor-cell hypoxia with stromal hypoxia. To what extent are pancancer hypoxia scores driven by malignant epithelium vs hypoxic stromal/myeloid compartments?
- The paper proposes TP53 mutation as a *consequence* of hypoxia (selection); but mutual confounding by clonal hematopoiesis or germline modifiers is not ruled out.
- Whether hypoxia-induced miR-133a-3p downregulation affects BIN1/PGM5 protein levels in vivo (not only correlationally) is open.

## My take

This is the foundational pancancer hypoxia paper in the genomics era — the *primary citation* for "hypoxia drives genomic instability and aggressive somatic landscapes." For the user's HypoxiaVERSE thesis, this paper anchors the *tumor-cell genomic* arm: it establishes the cross-cancer hypoxia-mutation associations (TP53, MYC, PTEN, CDKN2A) and provides the first rigorous statistical framework (AS89, multiple-signature ensembling) for hypoxia quantification at scale. The nimbosus concept reframes hypoxia from "a TME feature" to "an early evolutionary selective pressure that fixes aggressive somatic state." The complementary immune-microenvironment story — how hypoxia rewires myeloid epigenetics ([[papers/nf-kb-tet2-promote-macrophage-reprogramming]]) and recruits TRM/MoMac populations — is downstream of the genomic framework this paper lays. miR-133a-3p in PCa is a concrete mechanistic finding that bridges into miRNA-target work. The PTEN-TERT-hypoxia three-way interaction is unusual and worth reexamining with current single-cell/multi-omic methods.

## Related

- [[concepts/tumor-hypoxia-mrna-signature]]
- [[concepts/nimbosus-aggressive-prostate-phenotype]]
- [[concepts/mir-210-hypoxia-induced-microrna]]
- [[concepts/mir-133a-3p-hypoxia-prostate]]
- [[concepts/tumor-subclonal-evolution-architecture]]
- [[concepts/hypoxia-genomic-instability-pga]]
- [[concepts/ancestry-specific-tumor-hypoxia]]
- [[concepts/hypoxia-pten-tert-telomere-axis]]
- [[concepts/chromothripsis-hypoxia-prostate]]
- [[concepts/intraductal-cribriform-carcinoma]]
- [[concepts/tumor-hypoxia-intratumoral-heterogeneity]]
- [[foundations/hif1a]]
- [[foundations/pten-tumor-suppressor]]
- [[foundations/tp53-tumor-suppressor]]
- [[foundations/myc-oncogene]]
- [[foundations/tert-telomerase]]
- [[foundations/cdkn2a-tumor-suppressor]]
- [[foundations/tcga-the-cancer-genome-atlas]]
- [[foundations/buffa-hypoxia-signature]]
- [[foundations/mir-210-mirna]]
- [[foundations/mir-133a-3p-mirna]]
- [[people/vinayak-bhandari]]
- [[people/paul-c-boutros]]
- [[people/robert-g-bristow]]
- [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] — complementary: hypoxic macrophage epigenetic reprogramming in tumor microenvironment

- [[papers/tumour-hypoxia-driving-genomic-instability-tumour]] — Suvac, Ashton & Bristow 2025 *Nat Rev Cancer* review consolidating the hypoxia → genomic-instability → clonal-evolution → immune-evasion framework.
- [[papers/hypoxia-signaling-human-health-diseases-implications]] — Luo et al. 2022 STTT comprehensive review of HIF cross-talk and disease landscape (added 2026-05-21).
