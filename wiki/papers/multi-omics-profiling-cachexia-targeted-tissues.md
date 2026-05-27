---
# === Identification ===
title: "Multi-omics profiling of cachexia-targeted tissues reveals a spatio-temporally coordinated response to cancer"
slug: multi-omics-profiling-cachexia-targeted-tissues
arxiv: ""
doi: "10.1038/s42255-025-01434-3"
pmid: "41540255"
venue: "Nature Metabolism"
year: 2026
authors:
  - "Pauline Morigny"
  - "Michaela Vondrackova"
  - "Honglei Ji"
  - "Kristyna Brejchova"
  - "Monika Krakovkova"
  - "Konstantinos Makris"
  - "Radka Trubacova"
  - "Tuna F. Samanci"
  - "Doris Kaltenecker"
  - "Su-Ping Ng"
  - "Vignesh Karthikaisamy"
  - "Sophia E. Chrysostomou"
  - "Anna Bidovec"
  - "Mariana Ponce-de-Leon"
  - "Tanja Krauss"
  - "Claudine Seeliger"
  - "Olga Prokopchuk"
  - "Marc E. Martignoni"
  - "Melina Claussnitzer"
  - "Hans Hauner"
  - "Martina Schweiger"
  - "Laure B. Bindels"
  - "Mauricio Berriel Diaz"
  - "Stephan Herzig"
  - "Dominik Lutter"
  - "Ondrej Kuda"
  - "Maria Rohm"
first_author: "Pauline Morigny"
corresponding_author: "Ondrej Kuda; Maria Rohm"

# === Source & metadata ===
source_type: pdf
s2_id: "fd755fe11608094c8519ee73bc45c246efabb1e5"
date_added: 2026-05-27
ingested_date: 2026-05-27
ingest_version: 1
last_reviewed: null

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - cancer-cachexia
  - one-carbon-metabolism
  - methionine-cycle
  - NNMT
  - MNAM
  - sarcosine
  - IL6
  - muscle-atrophy
  - glucose-hypermetabolism
  - 13C-glucose-tracing
  - multi-omics
  - metabolomics
  - transcriptomics
  - C26-mouse-model
  - PDAC-cachexia
  - humanised-cachexia-model
  - FIDAS-5
  - MAT-inhibitor
  - sarcopenia
  - methyltransferases
  - pseudo-time-metabolite-clustering
keywords:
  - tissue-overarching one-carbon metabolism in cachexia
  - IL6-driven NNMT induction in cachectic liver
  - methionine treatment induces myotube atrophy and hypermetabolism
  - FIDAS-5 rescues IL6-induced cachexia features in C2C12
  - 13C6-glucose tracing reveals muscle TCA hypermetabolism
  - pyruvate carboxylase active in cachectic muscle
  - multi-omics IPA upstream regulator analysis IL6 LPS
  - six-model + humanised SW480 conservation of one-carbon signature
  - patient sarcopenia NNMT upregulation
domain: "metabolism / oncology / cachexia"

# === Biomedical domain ===
tissue:
  - liver
  - blood
  - adipose_eWAT
  - adipose_iWAT
  - skeletal_muscle_GC
  - skeletal_muscle_soleus
  - heart
  - tumour
  - in_vitro_only
condition:
  - cancer
disease_specific:
  - cancer_cachexia
  - colon_carcinoma_C26
  - pancreatic_ductal_adenocarcinoma_Panc02_8025
  - intestinal_polyposis_ApcMin
  - Lewis_lung_carcinoma_LLC
  - KPP_PDAC
  - SW480_humanised_cachexia
  - sarcopenia
species:
  - mouse
  - human
hypoxia_relevant: false
contains_immune_cells: false
contains_myeloid: false

# === Technique ===
techniques:
  - LC-MS_metabolomics_LIMeX
  - HILIC_MS
  - HSS_T3_MS
  - bulk_RNA-seq
  - 13C6-glucose_isotope_tracing
  - 1-13C-pyruvate_isotope_tracing
  - INCA_2_metabolic_flux_analysis
  - IsoCor_isotopologue_correction
  - MS-DIAL_processing
  - PLSDA
  - VSClust_clustering
  - KEGG_pathway_analysis
  - IPA_Qiagen_upstream_regulator
  - qRT-PCR
  - IL6_neutralising_antibody
  - tumour_cell_IL6_KO
  - C2C12_myotube_atrophy_imaging
  - 3T3-L1_adipocyte_lipolysis_assay
  - FIDAS-5_MAT_pharmacological_inhibition
  - recombinant_IL6_stimulation
n_samples: null
n_cells_total: null
integration_method: ""

# === Biology captured ===
key_cell_types:
  - C2C12_myotube
  - 3T3-L1_adipocyte
  - hepatocyte_in_vivo
  - skeletal_muscle_fibre_in_vivo
  - cardiomyocyte_in_vivo
  - adipocyte_in_vivo
  - C26_colon_carcinoma_cell
  - Panc02_PDAC_cell
  - 8025_PDAC_cell
  - SW480_human_colon_carcinoma_cell
key_markers:
  - NNMT
  - MAT1A
  - MAT2A
  - GNMT
  - KMT2A
  - KMT2B
  - SAT1
  - GPX3
  - GSTA4
  - MTHFR
  - SHMT1
  - SHMT2
  - PEMT
  - sarcosine
  - MNAM
  - dimethylglycine
  - di-methyllysine
  - tri-methyllysine
  - thymidine
  - ureidopropionic_acid
  - SAH_SAM_ratio
  - IL6
  - pyruvate_carboxylase
  - pyruvate_dehydrogenase
key_pathways:
  - one-carbon_metabolism_methionine_folate_cycle
  - polyamine_metabolism_SAT1_spermidine
  - urea_cycle_arginine_biosynthesis
  - pyrimidine_synthesis_via_folate
  - glutathione_metabolism_GPX3_GSTA4
  - TCA_cycle_PC_PDH_2OGDH_glutamine_anaplerosis
  - IL6_inflammation_driven_metabolic_reprogramming

# === User project membership ===
projects: []
priority: reference
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: excluded
exclusion_reason: "Cancer-cachexia metabolic resource; not hypoxia-focused. Useful as multi-tissue multi-omics methodology and one-carbon/IL6 mechanistic context for tumour–host metabolic crosstalk."
data_availability: "GEO GSE290937 (RNA-seq); WebApp https://m3cav.metabolomics.fgu.cas.cz/; Supplementary Tables 1-5"

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Cancer cachexia is a multifactorial wasting syndrome affecting most patients with cancer and one of the strongest predictors of mortality; it cannot be reversed by nutritional support, implying a maladaptive metabolic component. Prior work has shown a coordinated multi-tissue response and implicates tumour-secreted factors (notably IL6), but few studies have integrated metabolomics across multiple tissues, almost none have combined metabolomics with transcriptomics and 13C-tracing across the time-course of cachexia, and no tissue-overarching metabolic pathway has been nominated as a unifying mechanism of wasting.

## Key idea

By integrating polar metabolomics (~200-300 metabolites/tissue), bulk RNA-seq and in vivo 13C6-glucose tracing across eight tissues (plasma, liver, eWAT, iWAT, heart, GC muscle, soleus, tumour) at three stages of cachexia progression (control / pre-cachectic / cachectic) in the C26 mouse model — plus five additional mouse models, a humanised SW480 model, and patient liver/muscle — the authors identify **one-carbon metabolism** as the tissue-overarching pathway activated in cachexia. The pathway is controlled by IL6 (inhibition rescues), is causally connected to muscle atrophy and glucose hypermetabolism (methionine drives it; FIDAS-5 MAT inhibitor reverses it in C2C12 myotubes), is conserved across six tumour entities and translates to humans (patient sarcopenia → elevated NNMT in liver/muscle). The work proposes one-carbon metabolism as both a unifying biomarker and a candidate therapeutic node in cachexia.

## Method

In vivo C26 cachexia model: male BALB/c mice, subcutaneous C26 colon carcinoma cells; controls were PBS-injected (Ctrl) or non-cachexia-inducing NC26-injected (Non-cax). Mice were classified Pre-cax (before weight loss) or Cax (~10% weight loss). 6-h fast, intraperitoneal [13C6]-glucose injection 1 h before tissue collection. Eight tissues collected (plasma, liver, eWAT, iWAT, heart, GC muscle, soleus, tumour) — n = 4/group. Additional cachexia models: ApcMin, LLC, KPP, Panc02 (orthotopic), 8025 (orthotopic, mild & cachectic timepoints), SW480 (humanised colon-carcinoma xenograft).

Metabolomics: LIMeX pipeline (LC-MS), HILIC and HSS-T3 platforms (positive/negative ionisation), MS-DIAL processing, iterative MS/MS for annotation; ~200-300 polar metabolites/tissue retained. Isotopologue correction with IsoCor.

Tracer flux modelling: INCA 2.3 (Isotopomer Network Compartmental Analysis), citrate synthase activity (V12) used as flux normalisation reference; χ² goodness-of-fit and Monte Carlo 95% CIs.

Transcriptomics: bulk RNA-seq at Novogene (NovaSeq, 150 bp PE) — Cax vs Ctrl across 5 tissues; ~340 commonly altered genes. Pathway analysis: IPA (Qiagen) for up-/downstream and integrated -omics; KEGG for metabolite-level pathway enrichment.

Pseudo-time analysis: metabolite trajectories assigned to 8 clusters (early/late increase or decrease) using VSClust; Sankey-style attribution to tissue and metabolite class.

IL6 perturbations in vivo: (i) IL6-neutralising antibody in C26-bearing mice; (ii) CRISPR IL6 KO in C26 cells (C26-IL6-KO vs C26-scr) — both rescue weight loss without reducing tumour size.

In vitro: C2C12 myotubes treated with 0/20/100 μM L-methionine (48 h) — myotube imaging (40-60 myotubes/well, ImageJ), 13C6-glucose tracing 1 h, MS quantitation of one-carbon metabolites. FIDAS-5 (MAT inhibitor, 2-5 μM, 48 h) ± recombinant IL6 (100 ng/mL). 3T3-L1 adipocytes used as cell-type-specificity control (lipolysis & glucose consumption assays).

Patient cohort: liver and skeletal muscle from cancer patients with vs without sarcopenia; NNMT and one-carbon signature gene expression analysis (Supplementary Table 3).

## Results

### 1. Multi-tissue metabolomes are coordinately reprogrammed in C26 cachexia (Fig. 1)
- Cax mice: ~10% BW loss; tumour size identical to Non-cax (no anorexia-only effect).
- PLSDA/PCA: plasma, liver, eWAT cluster apart from controls; muscle/heart more variable.
- Non-cax tumours barely perturb host tissues — alterations are cachexia-specific.
- 5-38% of metabolites significantly altered per tissue; amino acids, nucleosides and organoheterocyclic compounds are jointly regulated.

### 2. Pseudo-time clustering reveals one-carbon metabolism as the tissue-overarching axis (Fig. 2)
- 8 metabolite clusters identified (early/late ± increase/decrease).
- Cluster #1 (late increase, 151 metabolites): methylated amino acids (sarcosine, trimethyllysine), aminoadipic acid, ureidopropionic acid, glycyl-glutamate, ornithine.
- Cluster #5 (late decrease): energy intermediates (malic acid, ATP, phosphocreatine).
- KEGG: commonly upregulated in ≥2 target tissues → one-carbon pool by folate, pyrimidine metabolism, Gly/Ser/Thr metabolism, arginine biosynthesis. Commonly downregulated → TCA, glycolysis, Ala/Asp/Glu, nitrogen metabolism.

### 3. One-carbon products and ratios elevated across plasma/liver/adipose/muscle (Fig. 3)
- Substrates of one-carbon (glycine, serine) depleted in circulation.
- Products (sarcosine, MNAM, di/tri-methyllysine, dimethylglycine, thymidine) elevated across plasma, liver, eWAT, iWAT, heart, GC muscle and tumour.
- SAH/SAM ratio trends up in Cax plasma, adipose, tumour; THF/5-methylTHF trends up in liver.
- Tissue-specific methyl-acceptor signatures: MNAM dominates liver; sarcosine + methyllysines dominate adipose & muscle.

### 4. Transcriptomes are coordinately reprogrammed; one-carbon enzymes upregulated (Fig. 4 a-f, Ext Fig. 5)
- Cax vs Ctrl: 89-100% of variance explained by cachexia (tumour effect ≤11%); ~340 commonly altered genes across tissues.
- IPA: top activated pathways are amino acid metabolism, protein synthesis/post-translational modification (including Nnmt); top inhibited are mitochondrial/energy production.
- Liver: Mat1a, Nnmt strongly induced. Muscle: Mat2a, Kmt2a, Kmt2b induced. Cross-tissue: Sat1, Gpx3, Gsta4. Pathway maps confirm coordinated remodelling.

### 5. Inflammation (LPS / IL6) is the dominant upstream driver (Fig. 4 g-k)
- IPA upstream regulator: lipopolysaccharide/inflammation, β-oestradiol, TGFB1.
- IL6 inhibition (neutralising antibody OR C26-IL6-KO): no effect on tumour size, but rescues cachexia weight loss.
- Nnmt induction in liver suppressed 77% (antibody) and 89% (KO).
- One-carbon metabolites (MNAM, thymidine in liver; di/tri-methyllysine in GC muscle) elevated in C26-scr → abolished in C26-IL6-KO.

### 6. Methionine drives myotube atrophy and glucose hypermetabolism; FIDAS-5 rescues (Fig. 5, Ext Fig. 6)
- L-methionine (0/20/100 μM, 48 h) on C2C12 myotubes: dose-dependent ↑ one-carbon metabolites (SAM, SAH, MNAM, DMG); dose-dependent myotube atrophy; ↑ glucose consumption; ↑ 13C6-glucose label into TCA intermediates.
- FIDAS-5 (MAT inhibitor): ↓ one-carbon metabolites; myotube hypertrophy; ↓ glucose consumption → opposite phenotype.
- Recombinant IL6 in C2C12 → atrophy + hypermetabolism + one-carbon induction; FIDAS-5 reverses each readout.
- 3T3-L1 adipocytes + L-methionine: no lipolysis or glucose-consumption phenotype → effect is cell-type-specific.

### 7. Cachectic muscle exhibits PC/PDH-driven TCA hypermetabolism (Fig. 6, Ext Fig. 7-8)
- 13C6-glucose 1 h post-injection: TCA intermediates (citrate, succinate, fumarate, malate) more highly labelled in Cax GC muscle, soleus, heart; higher isotopologues (M+3, M+4) particularly enriched.
- Unlabelled metabolite pools mostly unchanged/decreased → hypermetabolism only manifest upon glucose availability.
- M+3 labelling implies pyruvate-carboxylase activity; [1-13C]-pyruvate tracing in C2C12 confirms PC active in muscle cells.
- INCA flux modelling (citrate synthase = V12 normaliser): ↑ V9 (PC), ↑ V10 (PDH), ↑ V18 (2-OGDH), trends ↑ V19-21 (SDH/FH/MDH); ↓ V11 (acetyl-CoA from β-oxidation/ketogenic AA); ↑ V16-V17 (glutamine entry).
- Pre-cax mice show trends in same direction → early event.

### 8. The signature is conserved across six mouse models + humanised model (Fig. 7, Ext Fig. 9)
- Panc02 (mild cachexia, 3% BW loss), 8025 (Mild + Cax timepoints, 4-10% BW loss), ApcMin, LLC, KPP all reproduce: ↑ Nnmt, Gnmt, Kmt2a/b, Mthfr, Mat1a/Mat12a, Sat1, Gpx3, Gsta4; ↑ sarcosine, MNAM, di/tri-methyllysines, thymidine in liver/muscle/adipose.
- 13C-glucose tracing in Panc02 and 8025 GC muscle: TCA-label enrichment scaling with cachexia severity.
- Conserved across genetic backgrounds, tumour entities, laboratory environments.

### 9. Translation to patients and humanised SW480 model (Fig. 8, Ext Fig. 10)
- Patient liver + skeletal muscle (sarcopenic vs non-sarcopenic cancer patients): ↑ NNMT and overall one-carbon signature gene set in sarcopenia.
- Humanised SW480 mice: clear cachexia phenotype (BW + tissue mass loss); ↑ one-carbon enzyme expression in liver/muscle/adipose; ↑ one-carbon metabolites in plasma, liver, heart, skeletal muscles, adipose; ↑ 13C6-glucose label into TCA in cardiac & skeletal muscle, matching C26 and PDAC patterns.

## All claims (exhaustive)

- `[c01]` C26-cachectic mice show distinct, cachexia-specific metabolome clustering in plasma, liver and adipose tissue, while muscle/heart metabolomes are more variable (Fig. 1e-l) "plasma, liver and adipose tissue metabolomes of C26 cachectic animals clearly clustered apart from all other groups... Skeletal muscle and heart metabolite profiles showed a higher variability, especially in the cachectic group" — confidence: high — type: methodological — links: [[concepts/multi-omics-coordinated-host-tissue-response-cachexia]] [[foundations/cancer-cachexia]] [[foundations/c26-colon-carcinoma-cachexia-model]] [[claims/c26-cachectic-mice-distinct-metabolome-clustering-tissues]]
- `[c02]` Non-cachexia-inducing NC26 tumours do not perturb host-tissue metabolomes — perturbation requires a cachexia-inducing tumour (Fig. 1e-k, Ext Fig. 2) "Non-cachexia-inducing NC26 tumours did not cause any major alterations in the metabolite profiles of host tissues compared with Ctrl... highlighting that most metabolic alterations are associated with the presence of a cachexia-inducing tumour" — confidence: high — type: methodological — links: [[concepts/multi-omics-coordinated-host-tissue-response-cachexia]] [[foundations/cancer-cachexia]] [[claims/non-cax-tumour-no-host-metabolome-perturbation]]
- `[c03]` Pseudo-time VSClust analysis of metabolite trajectories identifies a dominant late-increase cluster (#1, 151 metabolites) enriched in methylated amino acids (sarcosine, trimethyllysine) and amino-acid derivatives, coordinated across host tissues (Fig. 2a-c) "the most prominent cluster #1 (late increase in Cax) was defined by increased levels of several methylated amino acids (for example, sarcosine/methylglycine and trimethyllysine) and derivatives of amino acid metabolism" — confidence: high — type: methodological — links: [[concepts/multi-omics-coordinated-host-tissue-response-cachexia]] [[foundations/sarcosine-metabolite]] [[foundations/vsclust-clustering]] [[claims/pseudo-time-cluster1-methylated-aa-coordinated-cachexia]]
- `[c04]` KEGG pathway analysis of metabolites altered in ≥2 cachexia target tissues identifies one-carbon pool by folate, pyrimidine synthesis and arginine biosynthesis as commonly upregulated; TCA cycle, glycolysis and Ala/Asp/Glu metabolism as commonly downregulated (Fig. 2d-e) "products of one-carbon metabolism (for example, sarcosine and dimethylglycine) and related pathways, such as pyrimidine synthesis... and arginine biosynthesis/metabolism" were elevated — confidence: high — type: methodological — links: [[concepts/one-carbon-metabolism-cachexia-tissue-overarching]] [[foundations/kegg-pathway-database]] [[claims/kegg-one-carbon-pyrimidine-arginine-upregulated-cachexia]]
- `[c05]` Products of one-carbon metabolism (sarcosine, MNAM, di/tri-methyllysine, dimethylglycine, thymidine, ureidopropionic acid) are elevated across plasma, liver, eWAT, iWAT, heart, GC muscle, soleus and tumour of cachectic mice; circulating glycine and serine (substrates) are depleted (Fig. 3 c-g) "We observed a clear increase in the levels of the vast majority of these metabolites in all tissues of Cax animals as well as in the tumour... especially in products of this pathway" — confidence: high — type: mechanistic — links: [[concepts/one-carbon-metabolism-cachexia-tissue-overarching]] [[foundations/sarcosine-metabolite]] [[foundations/mnam-1-methylnicotinamide]] [[claims/one-carbon-products-elevated-across-tissues-cachexia]]
- `[c06]` SAH/SAM ratios trend higher in cachectic plasma, adipose and tumour, and THF/5-methylTHF in liver — consistent with flux activation through the methionine and folate cycles (Ext Fig. 4p-q) "trends towards elevated SAH/SAM ratios in Cax plasma, adipose tissue and tumour and THF/5-methylTHF in liver (the only tissue in which such metabolites were detectable)" — confidence: medium — type: quantitative — links: [[concepts/one-carbon-metabolism-cachexia-tissue-overarching]] [[foundations/s-adenosylmethionine-sam]] [[claims/sah-sam-thf-5mthf-ratios-trend-up-cachexia]]
- `[c07]` Methylated-product signature is tissue-specific: MNAM dominates the liver methyl-acceptor profile, sarcosine and methyllysine dominate adipose and muscle (Fig. 3 c-g) "we observed tissue specificity in terms of methylated products, with MNAM being the main methyl acceptor in liver, sarcosine and methyllysine in adipose tissue and muscles" — confidence: high — type: correlational — links: [[concepts/nnmt-mnam-liver-cachexia-axis]] [[foundations/mnam-1-methylnicotinamide]] [[claims/tissue-specific-methylated-product-signature-cachexia]]
- `[c08]` Cax transcriptomes are massively remodelled vs Ctrl, with cachexia explaining 89-100% of gene-expression variance (tumour ≤11%); 340 genes are commonly altered across cachexia target tissues (Ext Fig. 5 a-g) "we observed a huge remodelling of tissue transcriptomes in Cax compared with Ctrl mice, with cachexia explaining 89% to near 100% of gene expression changes" — confidence: high — type: quantitative — links: [[concepts/multi-omics-coordinated-host-tissue-response-cachexia]] [[claims/cachexia-transcriptome-remodelling-dominates-tumour-effect]]
- `[c09]` One-carbon-metabolism enzymes are coordinately upregulated across tissues with isoform-specific patterns: Mat1a and Nnmt in liver; Mat2a, Kmt2a, Kmt2b in muscle; Sat1, Gpx3, Gsta4 across multiple tissues (Fig. 4 c-f) "Mat1a... and Nnmt... were strongly induced in livers of cachectic animals... regulation of Mat2a, Kmt2a and Kmt2b... was more specific to cachectic muscle... several changes were common across tissues, such as... Sat1, Gpx3 and Gsta4" — confidence: high — type: mechanistic — links: [[concepts/one-carbon-metabolism-cachexia-tissue-overarching]] [[foundations/nnmt-nicotinamide-n-methyltransferase]] [[foundations/mat1a-methionine-adenosyltransferase-1a]] [[foundations/mat2a-methionine-adenosyltransferase]] [[foundations/sat1-spermidine-spermine-acetyltransferase]] [[foundations/gnmt-glycine-n-methyltransferase]] [[claims/one-carbon-enzyme-expression-broadly-elevated-cachexia]]
- `[c10]` IPA combined-omics upstream-regulator analysis nominates LPS/inflammation as the principal driver of cachexia metabolic reprogramming, with IL6 and TGFB1 as further regulators (Fig. 4g) "lipopolysaccharide and, by extension, inflammation as the first determinant to drive the substantial metabolic reprogramming occurring in cachexia" — confidence: high — type: methodological — links: [[concepts/il6-driven-cachexia-one-carbon-reprogramming]] [[foundations/il-6-cytokine]] [[foundations/ingenuity-pathway-analysis]] [[claims/ipa-lps-il6-tgfb1-upstream-cachexia-reprogramming]]
- `[c11]` IL6 inhibition (neutralising antibody or tumour-cell IL6 KO) does not reduce tumour size but rescues cachexia-associated weight loss and suppresses induction of one-carbon enzymes — Nnmt liver induction reduced 77% (antibody) and 89% (C26-IL6-KO) (Fig. 4 h-i, Ext Fig. 5 k-u) "IL6 inhibition did not reduce tumour size but improved cachexia-associated weight loss... Nnmt induction in liver by C26 tumours was repressed by 77% with IL6-neutralising antibody, and by 89% upon IL6 KO in C26 cells" — confidence: high — type: pharmacological — links: [[concepts/il6-driven-cachexia-one-carbon-reprogramming]] [[concepts/nnmt-mnam-liver-cachexia-axis]] [[foundations/il-6-cytokine]] [[foundations/nnmt-nicotinamide-n-methyltransferase]] [[claims/il6-inhibition-rescues-cachexia-and-blocks-nnmt-induction]]
- `[c12]` Tumour-cell IL6 KO abolishes the cachexia-associated elevation of one-carbon metabolites (MNAM and thymidine in liver; di- and tri-methyllysine in GC muscle), demonstrating IL6 is necessary for the metabolic phenotype (Fig. 4 j-k) "Metabolomics confirmed the significant increase of multiple products of the one-carbon metabolism in C26 cachectic liver (for example, #10 MNAM and #18 thymidine) and GC muscle... and the near-complete absence of their enrichment upon IL6 KO" — confidence: high — type: pharmacological — links: [[concepts/il6-driven-cachexia-one-carbon-reprogramming]] [[foundations/il-6-cytokine]] [[claims/il6-ko-abolishes-one-carbon-metabolite-elevation-cax]]
- `[c13]` L-methionine treatment of C2C12 myotubes (0/20/100 μM, 48 h) induces dose-dependent myotube atrophy, replicating a key cachexia feature in vitro (Fig. 5 a-c) "L-methionine induced myotube atrophy, a classical cachexia feature in this cell culture setting, in a dose-dependent manner" — confidence: high — type: pharmacological — links: [[concepts/methionine-cycle-myotube-atrophy-hypermetabolism]] [[foundations/c2c12-myotube-model]] [[claims/l-methionine-induces-dose-dependent-myotube-atrophy-c2c12]]
- `[c14]` L-methionine treatment increases glucose consumption in C2C12 myotubes and shifts 13C6-glucose labelling toward higher TCA isotopologues — methionine drives muscle-cell hypermetabolism (Fig. 5 d-h) "L-methionine altered myotube metabolism towards higher glucose consumption... acceleration of glucose metabolism feeding into the TCA cycle" — confidence: high — type: quantitative — links: [[concepts/methionine-cycle-myotube-atrophy-hypermetabolism]] [[concepts/muscle-glucose-hypermetabolism-cachexia-tca-rewiring]] [[foundations/13c6-glucose-tracer]] [[claims/l-methionine-drives-glucose-hyperconsumption-myotube]]
- `[c15]` FIDAS-5 (MAT inhibitor) reduces one-carbon metabolites in C2C12 cells and induces a phenotype opposite to L-methionine: myotube hypertrophy with reduced glucose consumption (hypometabolism) (Ext Fig. 6 f-j) "FIDAS-5 significantly reduced one-carbon metabolite levels and led to a phenotype opposite to L-methionine-treated cells in a dose-dependent manner, characterised by myotube hypertrophy associated with reduced glucose consumption" — confidence: high — type: pharmacological — links: [[concepts/fidas-5-methionine-blockade-rescues-cachexia]] [[concepts/methionine-cycle-myotube-atrophy-hypermetabolism]] [[foundations/fidas-5-mat-inhibitor]] [[claims/fidas5-induces-myotube-hypertrophy-reduces-glucose-uptake]]
- `[c16]` FIDAS-5 rescues IL6-induced one-carbon induction, myotube atrophy and elevated glucose consumption in C2C12 cells, placing the methionine cycle downstream of IL6 in the atrophy/hypermetabolism phenotype (Ext Fig. 6 k-q) "the induction of IL6 signalling was associated with an induction of one-carbon metabolites and myotube atrophy, which was rescued upon FIDAS-5 treatment. FIDAS-5 also significantly reduced glucose consumption in IL6-treated cells" — confidence: high — type: pharmacological — links: [[concepts/fidas-5-methionine-blockade-rescues-cachexia]] [[concepts/il6-driven-cachexia-one-carbon-reprogramming]] [[foundations/fidas-5-mat-inhibitor]] [[foundations/il-6-cytokine]] [[claims/fidas5-rescues-il6-induced-atrophy-and-hypermetabolism-c2c12]]
- `[c17]` The methionine ↔ atrophy/hypermetabolism link is cell-type-specific: L-methionine treatment of 3T3-L1 adipocytes does not alter lipolysis or glucose consumption (Ext Fig. 6 r-t) "Treatment of 3T3-L1 adipocytes with different doses of L-methionine... did not affect lipolysis or glucose consumption, suggesting that the connection is indeed cell type specific" — confidence: high — type: pharmacological — links: [[concepts/methionine-cycle-myotube-atrophy-hypermetabolism]] [[claims/methionine-atrophy-link-cell-type-specific-not-adipocyte]]
- `[c18]` In vivo 13C6-glucose tracing reveals elevated incorporation of label into TCA intermediates (citrate, succinate, fumarate, malate) and enrichment of higher isotopologues (M+3, M+4) in GC muscle, soleus and heart of cachectic C26 mice, despite stable or reduced unlabelled pools (Fig. 6) "we observed an unexpected increase in the labelling of TCA metabolites in GC muscle, soleus muscle and heart upon glucose injection... the labelling of higher isotopologues (M+3 and more) of TCA cycle metabolites suggested a rewiring of glucose flux and hypermetabolism" — confidence: high — type: quantitative — links: [[concepts/muscle-glucose-hypermetabolism-cachexia-tca-rewiring]] [[foundations/13c6-glucose-tracer]] [[claims/13c6-glucose-labels-tca-elevated-cachectic-muscle-heart]]
- `[c19]` M+3 labelling of TCA intermediates from 13C6-glucose and complementary [1-13C]-pyruvate tracing in C2C12 establish that pyruvate carboxylase (PC) is active in cachectic muscle and provides anaplerotic carbon to the TCA cycle (Fig. 6, Suppl Fig. 4) "the significant increase in M + 3 labelling of these metabolites in muscles of Cax mice indicates that PC is active... [1-13C]-pyruvate tracing in C2C12 myotubes... showed M + 1 labelling of TCA intermediates, confirming that PC is active in muscle cells" — confidence: high — type: mechanistic — links: [[concepts/muscle-glucose-hypermetabolism-cachexia-tca-rewiring]] [[foundations/pyruvate-carboxylase-pc]] [[claims/pyruvate-carboxylase-active-cachectic-muscle-anaplerotic]]
- `[c20]` INCA metabolic-flux modelling normalised to citrate synthase (V12) shows increased PC (V9), PDH (V10) and 2-OGDH (V18) flux and increased glutamine entry (V16-V17) into the TCA cycle of cachectic GC muscle, with decreased β-oxidation/ketogenic-AA-derived acetyl-CoA flux (V11) (Ext Fig. 8 g-h, Suppl Table 2) "Relative flux through PC and PDH was increased in GC muscle (V9 and V10)... significantly increased flux through 2-oxoglutarate dehydrogenase (V18) in cachectic muscle... increased usage of glutamine (including also glucogenic amino acid backbones) as a substrate for the TCA cycle (V16 and V17)" — confidence: high — type: methodological — links: [[concepts/muscle-glucose-hypermetabolism-cachexia-tca-rewiring]] [[foundations/inca-isotopomer-network-analysis]] [[foundations/pyruvate-carboxylase-pc]] [[claims/inca-flux-pc-pdh-2ogdh-elevated-cachectic-muscle]]
- `[c21]` Pre-cachectic mice (no weight loss) already exhibit trends towards increased TCA flux in GC muscle, indicating muscle glucose hypermetabolism is an early event preceding wasting (Ext Fig. 8 h) "The Pre-cax state showed trends towards increased flux in all above-mentioned reactions despite unchanged body weight and composition, indicating that glucose hypermetabolism in muscle may be an early event contributing to cachexia" — confidence: medium — type: correlational — links: [[concepts/muscle-glucose-hypermetabolism-cachexia-tca-rewiring]] [[claims/pre-cachectic-muscle-tca-flux-trends-early]]
- `[c22]` The one-carbon-metabolism signature (gene + metabolite + muscle 13C-glucose TCA enrichment) is conserved across six independent mouse cachexia models (C26, Panc02, 8025, ApcMin, LLC, KPP) and a humanised SW480 model — a unifying feature of cancer cachexia (Fig. 7, Fig. 8 c-i, Ext Fig. 9-10) "the conserved alteration in gene expression and metabolites in six independent mouse models highlights the tissue-overarching activation of one-carbon metabolism as a hallmark of cachexia" — confidence: high — type: correlational — links: [[concepts/one-carbon-metabolism-cachexia-tissue-overarching]] [[foundations/panc02-pdac-cachexia-model]] [[foundations/sw480-humanised-cachexia-model]] [[foundations/c26-colon-carcinoma-cachexia-model]] [[claims/one-carbon-conserved-six-mouse-cachexia-models-and-humanised]]
- `[c23]` Cancer patients with sarcopenia show increased NNMT and increased one-carbon signature gene expression in liver and skeletal muscle compared with non-sarcopenic cancer patients — the pathway translates to human cachexia (Fig. 8 a-b, Suppl Table 3) "Sarcopenia was associated with increased gene expression of NNMT and increased expression of the signature gene set overall, in accordance with our previous observation linking this pathway to muscle wasting" — confidence: high — type: correlational — links: [[concepts/nnmt-mnam-liver-cachexia-axis]] [[foundations/sarcopenia-clinical-syndrome]] [[foundations/nnmt-nicotinamide-n-methyltransferase]] [[claims/patients-sarcopenia-show-elevated-nnmt-one-carbon-genes-liver-muscle]]

## Discussion captured

### Authors' interpretation

The authors interpret one-carbon metabolism activation as a unifying, IL6-driven metabolic adaptation in cancer cachexia. Multi-omics integration — not metabolomics alone — was required to recognise the coordinated tissue response; previous studies had identified individual hits (Nnmt, sarcosine, dimethylglycine) but missed the cross-tissue coherence. They propose that products of one-carbon metabolism support transcriptional reprogramming via methylation (DNA, RNA, histones) and supply the building blocks (purines, pyrimidines, polyamines, glutathione) for the wide tissue remodelling characteristic of cachexia. Liver MNAM induction is framed as a detoxification adjunct; muscle methyllysine accumulation is framed as an unresolved but candidate atrophy mediator. The link between methionine/one-carbon activation and muscle glucose hypermetabolism (PC/PDH-driven TCA acceleration, glutamine anaplerosis) is interpreted as an energy-consuming process that could itself drive wasting.

### Comparisons with prior literature (made by authors)

- **Mizuno et al. (ref 24)** — Remote solid cancers rewire hepatic nitrogen metabolism via host NNMT; consistent with NNMT/MNAM induction in cachectic liver in this paper.
- **Bindels et al. (ref 25), Chrysostomou et al. (ref 26 — same lab), Thibaut et al. (ref 27)** — Prior evidence that IL6 is a key tumour-secreted driver of C26 cachexia; this paper extends IL6's role to one-carbon metabolism.
- **Ducker & Rabinowitz 2017 *Cell Metab* (ref 22), Sanderson et al. 2019 *Nat Rev Cancer* (ref 23)** — One-carbon and methionine metabolism reviews; framing for canonical pathway.
- **Morigny et al. 2021 (ref 28 — first author's prior PLA2G7 paper)** — Cachexia biomarker discovery context.
- **Talbert et al. (ref 32)** — Humanised cancer-induced cachexia model precedent (SW480-type).
- **Recent methionine-cycle / DNA-methylation cachexia paper (ref 43)** — argues methionine cycle controls muscle DNA methylation in cachexia; this paper agrees mechanistically but extends to broader metabolite remodelling beyond DNA methylation.
- **Methotrexate / raltitrexed / 5-FU (ref 37, 38)** — One-carbon-targeting chemotherapeutics are known to aggravate cachexia; the authors flag this as a clinically important consideration for any therapeutic targeting of the pathway.
- **Methionine-restricted diets (refs 45-47)** — Lifespan extension; potential cachexia relevance.

### Mechanistic hypotheses proposed

- IL6 → one-carbon enzymes (Nnmt, Mat2a, Kmt2a/b, Sat1, Gpx3, Gsta4) → elevated one-carbon products → sustained methylation/translation/redox remodelling → wasting phenotype.
- Tumour-mediated reprogramming: depletion of essential metabolites required for tumour growth coupled with increased one-carbon intermediates in host tissues may serve to supply the tumour with building blocks.
- One-carbon activation may divert methyl flux away from DNA epigenetics towards more immediate processes (RNA methylation, redox, nucleotide synthesis) under metabolic stress.
- Muscle hypermetabolism via PC/PDH-driven TCA flux + glutamine anaplerosis is itself energy-consuming and may contribute to wasting.
- One-carbon upregulation may be an early response to mitochondrial dysfunction (citing refs 48-49); vice-versa, one-carbon activity influences mitochondrial metabolism (ref 50).

### Caveats and self-criticism

- Only male mice studied in this work (acknowledged); refs 10, 24 reported similar Nnmt/sarcosine/DMG changes in female C26 and 4T1 models.
- LLC and KPP cohorts were random-fed (not 6-h-fasted) — amplitude differences across models confounded by feeding status, mouse strain, tumour entity.
- The IPA "LPS" upstream regulator should be interpreted as "inflammation in general" — the authors equate it with IL6/TNF-class inflammatory drive rather than literal endotoxin exposure.
- It is "difficult to speculate on the cause or consequence" — paper does not claim that one-carbon activation directly *causes* wasting in vivo; FIDAS-5 was tested only in vitro (C2C12).
- Methionine-targeting chemotherapeutics (methotrexate, 5-FU) aggravate cachexia — therapeutic targeting needs nuance.

### Future directions suggested

- In vivo testing of one-carbon blockade (FIDAS-5, dietary methionine restriction) on cachexia phenotypes in tumour-bearing mice.
- Dissect tissue-specific roles of one-carbon products (methyllysines in muscle, MNAM in liver, sarcosine systemically).
- Determine whether one-carbon-derived methylation marks (DNA / histone / RNA) are causally required for the transcriptional reprogramming of cachexia.
- Patient-side biomarker development (sarcosine, MNAM, NNMT activity) for cachexia prediction/stratification.
- Pre-cachexia interception strategies given the early muscle hypermetabolism signal.

## Limitations

- Male mice only; sex generalisation relies on prior literature (refs 10, 24).
- FIDAS-5 rescue demonstrated only in vitro (C2C12); no in vivo MAT-inhibition phenotype tested in tumour-bearing mice.
- IL6 KO/neutralisation rescues weight loss and one-carbon induction, but the chain IL6 → specific upstream regulator → one-carbon enzyme transcription is not nailed down at the transcription-factor level.
- INCA flux modelling normalised to citrate synthase, which is itself elevated in Cax muscle — absolute flux changes are likely larger than reported relative changes.
- Patient cohort: liver and muscle biopsies from a relatively small set of sarcopenic vs non-sarcopenic patients (Suppl Table 3); n and exact cancer-type composition not visible in main text.
- Bulk RNA-seq only — single-cell resolution would clarify whether the one-carbon signature is cell-intrinsic to muscle fibres / hepatocytes / adipocytes or arises from infiltrating immune cells.
- Feeding-status heterogeneity across the six mouse models limits quantitative cross-model comparison of absolute fold-changes.
- Tumour ↔ host directionality of one-carbon flux not isotopically resolved (e.g., is liver MNAM exported to tumour, or is tumour sarcosine exported to muscle?).

## Open questions

### Open questions raised by authors

- Is one-carbon activation a cause or consequence of wasting in vivo?
- Does dietary methionine restriction or systemic MAT inhibition rescue cachexia phenotypes in tumour-bearing mice?
- What is the precise transcription-factor route from IL6 to Nnmt/Mat1a/Mat2a/Kmt2a induction?
- What is the contribution of DNA vs RNA vs histone vs small-molecule methylation in the cachectic remodelling?
- Are MNAM (liver) and methyllysines (muscle, adipose) functional drivers of organ-specific dysfunction or passive end-products?
- Can one-carbon metabolites serve as early biomarkers for pre-cachexia identification in patients?

### Open questions identified during ingest

- Whether the tissue-overarching one-carbon signature has a tissue-resident-macrophage / TAM contribution (NNMT/sarcosine biology is documented in macrophages — [[papers/macrophages-use-apoptotic-cell-derived-methionine]]).
- Whether IL6 → STAT3 → NNMT is the molecular axis (NNMT is a known STAT3 target in some contexts).
- Whether the pre-cachexia muscle glucose hypermetabolism overlaps biologically with hypoxia-driven metabolic rewiring (PC/PDH balance) documented in tumour or stromal compartments.
- Whether methionine restriction could be combined with chemotherapy that *itself* targets one-carbon (methotrexate, 5-FU) — sequencing/dosing question.
- Whether single-cell RNA-seq or spatial transcriptomics on cachectic muscle would refine the cell-type contribution (slow vs fast fibres, FAPs, satellite cells, resident macrophages).
- Whether the MNAM-rich cachectic liver state phenocopies any other liver pathology (NAFLD, hepatic regeneration) that could inform repurposing.

## My take

This is a flagship multi-omics resource paper for cancer cachexia. The conceptual novelty is the *integration* — neither metabolomics, transcriptomics nor 13C-tracing alone would have identified one-carbon metabolism as the unifying axis. Three findings stand out as load-bearing:

1. **One-carbon as a tissue-overarching signature**: products (sarcosine, MNAM, methyllysines, dimethylglycine, thymidine) consistently elevated in plasma + liver + adipose + muscle + tumour, with tissue-specific dominant methyl acceptors. Substrate depletion (glycine, serine) + product accumulation is a coherent flux signature.
2. **IL6 as upstream switch**: IL6-neutralisation and tumour-IL6-KO both abolish Nnmt induction and one-carbon metabolite elevation. This is a clean genetic + pharmacological double-dissociation.
3. **Muscle glucose hypermetabolism as an early event**: PC/PDH-driven TCA acceleration is detectable in pre-cachectic muscle. This reframes muscle wasting as an energy-leak-driven process, not only protein catabolism, and matches the methionine-driven hypermetabolic phenotype in C2C12. FIDAS-5 reversal in vitro is the most translatable handle.

Weaknesses: in vivo FIDAS-5 rescue is missing — the strongest version of the story would have shown that systemic MAT inhibition (or methionine restriction) preserves muscle mass and survival in C26 mice. The patient cohort is small and the bulk-RNA-seq design cannot dissect cell-type contributions to NNMT/methyltransferase upregulation. The IPA "LPS" upstream call is generic — the actual TF route remains open.

For the wiki: this paper is the entry point for the cachexia domain. It anchors NNMT, MAT1A, MAT2A, MNAM, sarcosine and FIDAS-5 in a cancer-host-metabolism context, complementing the existing macrophage-MAT2A-DNMT3A axis ([[papers/macrophages-use-apoptotic-cell-derived-methionine]]) and the methionine-competition T-cell biology already in the wiki. The mechanistic similarity — IL6-driven Nnmt vs efferocytosis-driven MAT2A-DNMT3A — suggests a recurring theme: methionine-cycle reprogramming as a tissue-specific commit step downstream of inflammation.

## Related

- [[papers/macrophages-use-apoptotic-cell-derived-methionine]] — Methionine-cycle / MAT2A / DNMT3A epigenetic biology in macrophages — complementary tissue context for cancer cachexia methionine axis.
- [[concepts/one-carbon-metabolism-cachexia-tissue-overarching]]
- [[concepts/il6-driven-cachexia-one-carbon-reprogramming]]
- [[concepts/methionine-cycle-myotube-atrophy-hypermetabolism]]
- [[concepts/muscle-glucose-hypermetabolism-cachexia-tca-rewiring]]
- [[concepts/nnmt-mnam-liver-cachexia-axis]]
- [[concepts/fidas-5-methionine-blockade-rescues-cachexia]]
- [[concepts/multi-omics-coordinated-host-tissue-response-cachexia]]
- [[foundations/cancer-cachexia]]
- [[foundations/sarcopenia-clinical-syndrome]]
- [[foundations/nnmt-nicotinamide-n-methyltransferase]]
- [[foundations/mat1a-methionine-adenosyltransferase-1a]]
- [[foundations/gnmt-glycine-n-methyltransferase]]
- [[foundations/sat1-spermidine-spermine-acetyltransferase]]
- [[foundations/sarcosine-metabolite]]
- [[foundations/mnam-1-methylnicotinamide]]
- [[foundations/fidas-5-mat-inhibitor]]
- [[foundations/c26-colon-carcinoma-cachexia-model]]
- [[foundations/panc02-pdac-cachexia-model]]
- [[foundations/sw480-humanised-cachexia-model]]
- [[foundations/c2c12-myotube-model]]
- [[foundations/13c6-glucose-tracer]]
- [[foundations/inca-isotopomer-network-analysis]]
- [[foundations/pyruvate-carboxylase-pc]]
- [[foundations/vsclust-clustering]]
- [[foundations/kegg-pathway-database]]
