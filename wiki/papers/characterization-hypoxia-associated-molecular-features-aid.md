---
# === Identification ===
title: "Characterization of hypoxia-associated molecular features to aid hypoxia-targeted therapy"
slug: characterization-hypoxia-associated-molecular-features-aid
arxiv: ""
doi: "10.1038/s42255-019-0045-8"
pmid: "31984309"
venue: "Nature Metabolism"
year: 2019
authors:
  - "Youqiong Ye"
  - "Qingsong Hu"
  - "Hu Chen"
  - "Ke Liang"
  - "Yuan Yuan"
  - "Yu Xiang"
  - "Hong Ruan"
  - "Zhao Zhang"
  - "Anren Song"
  - "Huiwen Zhang"
  - "Lingxiang Liu"
  - "Lixia Diao"
  - "Yanyan Lou"
  - "Bingying Zhou"
  - "Li Wang"
  - "Shengtao Zhou"
  - "Jianjun Gao"
  - "Eric Jonasch"
  - "Steven H. Lin"
  - "Yang Xia"
  - "Chunru Lin"
  - "Liuqing Yang"
  - "Gordon B. Mills"
  - "Han Liang"
  - "Leng Han"
first_author: "Youqiong Ye"
corresponding_author: "Liuqing Yang; Gordon B. Mills; Han Liang; Leng Han"

# === Source & metadata ===
source_type: pdf
s2_id: "839ef2206060b500dc35e3fadc8f0fc929c06dcb"
date_added: 2026-06-02
ingested_date: 2026-06-02
ingest_version: 1
last_reviewed: null

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - hypoxia
  - cancer
  - pancancer
  - TCGA
  - multi-omics
  - drug-response
  - precision-oncology
  - genomics
  - epigenetics
  - proteomics
keywords:
  - tumour hypoxia
  - 15-gene hypoxia signature
  - pan-cancer
  - propensity score
  - drug response
  - clinically actionable genes
  - hypoxia-targeted therapy
  - TP53
  - EGFR
  - miR-210
domain: "oncology"

# === Biomedical domain ===
tissue: [multi]
condition: [cancer]
disease_specific: []
species: [human]
hypoxia_relevant: true
contains_immune_cells: false
contains_myeloid: false

# === Technique ===
techniques: [bulk_RNA-seq, miRNA-seq, RPPA, EPIC_array, WES, SCNA_GISTIC2, GSVA, propensity_score_matching, cell_viability_assay]
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types: []
key_markers: [HIF1A, VEGFA, NDRG1, LDHA, SLC2A1, TP53, PTEN, EGFR, YAP1, miR-210, fibronectin]
key_pathways: [glycolysis, PI3K-Akt, RTK-signalling, HIF-1-signalling, p53, EMT, angiogenesis, apoptosis]

# === User project membership ===
projects: [thesis, hypoxia]
priority: core
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: candidate
exclusion_reason:
data_availability: "TCGA (portal.gdc.cancer.gov); GDSC; CPTAC; GEO GSE33072 (BATTLE). Code: https://github.com/youqiongye/HAMFA"

# === Cross-references ===
code_url: "https://github.com/youqiongye/HAMFA"
cited_by:
  - tumour-hypoxia-driving-genomic-instability-tumour
---

## Problem

Tumour hypoxia drives resistance to chemotherapy, radiotherapy, targeted therapy, and immunotherapy, making hypoxia-targeted therapy attractive — yet clinical trials of hypoxia-targeted agents have largely disappointed, and there is no reliable predictive biomarker. The molecular consequences of hypoxia across cancer types, and how they shape drug response, were not characterised comprehensively. This study asks: across many cancer types and molecular layers, which features are associated with tumour hypoxia status, and how do they relate to anticancer drug response?

## Key idea

Use a validated 15-gene mRNA signature to classify TCGA tumours into hypoxia score-high / -intermediate / -low groups within each cancer type, then — after balancing clinical confounders with a propensity-score algorithm — systematically compare six molecular layers (mRNA, miRNA, protein, DNA methylation, somatic mutation, SCNA) between hypoxia-high and -low groups. Integrate the resulting hypoxia-associated features with drug-sensitivity data (GDSC cell lines, imputed TCGA patient response, FDA-approved drug targets) to identify both drug-resistant and drug-sensitive associations, and validate selected predictions experimentally.

## Method

- **Classification**: 15-gene signature (ACOT7, ADM, ALDOA, CDKN3, ENO1, LDHA, MIF, MRPS17, NDRG1, P4HA1, PGAM1, SLC2A1, TPI1, TUBB6, VEGFA); hypoxia score via GSVA; unsupervised hierarchical clustering per cancer type. 24 cancer types (n≥100); KIRC/COAD VHL-mutant (≥5%) samples excluded (pseudohypoxia); 21 cancer types retained with ≥30 samples per group.
- **Validation of signature**: ten independent hypoxia/normoxia datasets; concordance with Winter and Hu signatures; CPTAC protein-level enrichment (BRCA NES=1.92, OV NES=2.15).
- **Confounder control**: propensity-score matching weights (logistic regression) balancing sex, age, ethnicity, smoking, stage, histology, tumour purity; standardized difference <10%; 100× permutation testing.
- **Drug response**: Spearman correlation of gene/protein/methylation/miRNA with GDSC cell-line drug AUC (252 drugs, 1,074 lines) and imputed TCGA patient drug response (138 drugs); FDA-approved drug-target (clinically actionable gene) mapping.
- **Experimental validation**: A549 and H1299 lung cancer lines, CellTiter 96 proliferation assay under 1% O2 vs 21% O2.

## Results

- The 15-gene signature robustly classifies hypoxia status; hypoxia score-high tumours have worse overall survival across cancer types (pan-cohort P=1.8×10⁻¹²).
- Hypoxia-associated alteration burden varies enormously across cancer types (e.g. STAD alterations in all six layers; OV only 399 mRNAs).
- 143 hypoxia-associated genes correlate with sensitivity to ≥3 anticancer drugs in cell lines; YAP1 links to resistance to 49 drugs.
- miR-210-3p up in 16 cancer types; hypoxia-associated miRNA networks enrich PI3K/Akt, Hippo, Ras, p53, EGFR, HIF-1 pathways.
- TP53 mutation enriched in hypoxia score-high tumours (e.g. 62.3% vs 8.0% in BRCA); IDH1 mutation enriched in hypoxia score-low LGG.
- Hypoxia-associated SCNAs harbour actionable genes (EGFR 7p11.2, PDCD1 2q37.3 deletion).
- 90.9% (110/121) of clinically actionable genes are hypoxia-biased in ≥1 layer.
- Hypoxia bidirectionally modulates drug response (resistance: erlotinib/LIHC, lapatinib/KIRP; sensitivity: thapsigargin/PAAD, imatinib/HNSC), confirmed in A549/H1299, and high hypoxia score predicts worse sorafenib outcome in the BATTLE NSCLC trial.

## All claims (exhaustive)

- `[c01]` 15-gene mRNA signature robustly classifies hypoxia status across cancer types (p.432) "These results demonstrate the robustness of the 15-gene signature to define hypoxia status in different cancer types." — confidence: high — type: methodological — links: [[claims/15-gene-hypoxia-signature-robust-pancancer-classification]] [[concepts/tumor-hypoxia-mrna-signature]] [[foundations/buffa-hypoxia-signature]] [[foundations/tcga-the-cancer-genome-atlas]]
- `[c02]` Hypoxia score-high tumours are associated with worse overall survival across cancer types (p.434) "hypoxia score-high tumours were consistently associated with worse prognosis across cancer types in univariate or multivariate survival analysis." — confidence: high — type: correlational — links: [[claims/hypoxia-score-high-worse-survival-pancancer]]
- `[c03]` A propensity-score algorithm balances clinical confounders to isolate hypoxia-associated molecular features (p.442) "we identified hypoxia-biased molecular signatures that are largely independent from the potential confounders across 21 cancer types." — confidence: high — type: methodological — links: [[claims/propensity-score-confounder-balanced-hypoxia-features]] [[concepts/propensity-score-confounder-balanced-omics]]
- `[c04]` The burden of hypoxia-associated multi-omic alterations varies markedly across cancer types and layers (p.434) "STAD had many hypoxia-associated features in six molecular layers... while glioblastoma multiforme (GBM) had hypoxia-associated features in 629 mRNAs and 5 proteins." — confidence: high — type: correlational — links: [[claims/hypoxia-molecular-alteration-burden-varies-by-cancer]] [[concepts/pan-cancer-hypoxia-multiomic-landscape]]
- `[c05]` 143 hypoxia-associated genes correlate with anticancer drug sensitivity across cancer cell lines (p.434) "its mRNA expression is linked to drug resistance to 49 anticancer drugs (for example, navitoclax, rs=0.52, FDR<1.0×10⁻⁵⁵)." — confidence: medium — type: correlational — links: [[claims/hypoxia-genes-correlate-anticancer-drug-sensitivity]] [[foundations/oncopredict-drug-sensitivity]]
- `[c06]` Hypoxia-induced miR-210-3p is upregulated in hypoxia score-high tumours in 16 cancer types (p.436) "The hypoxia-induced miRNA, miR-210-3p, was upregulated in hypoxia score-high tumours in 16 cancer types." — confidence: high — type: correlational — links: [[claims/mir-210-induced-under-hypoxia-pancancer]] [[concepts/mir-210-hypoxia-induced-microrna]] [[foundations/mir-210-mirna]]
- `[c07]` Hypoxia-associated miRNAs regulate target genes enriched in cancer signalling pathways (p.436) "Genes targeted by these miRNAs are significantly enriched in cancer-related pathways, including the PI3K/Akt, Hippo, Ras, p53, EGFR, and HIF-1 signalling pathways." — confidence: medium — type: mechanistic — links: [[claims/hypoxia-mirna-target-network-cancer-pathways]]
- `[c08]` Hypoxia-biased mRNA expression changes are inversely related to DNA methylation changes (p.436) "the hypoxia-biased mRNA expression level of a gene tended to be the opposite of its DNA methylation level." — confidence: medium — type: mechanistic — links: [[claims/hypoxia-mrna-expression-inverse-dna-methylation]] [[foundations/tet-mediated-dna-demethylation]]
- `[c09]` Hypoxia score-high tumours show recurrent protein alterations including PTEN loss and fibronectin gain (p.436) "PTEN, which negatively regulates the PI3K/Akt signalling pathway, was significantly downregulated in hypoxia score-high samples in five cancer types." — confidence: medium — type: correlational — links: [[claims/hypoxia-protein-alterations-pten-loss-fibronectin-gain]] [[foundations/pten-tumor-suppressor]]
- `[c10]` Integrative multi-omic regulation converges on drug-response genes such as EGFR in hypoxic tumours (p.436) "EGFR was upregulated in hypoxia score-high tumours (fold change=2.65, FDR=3.2×10⁻⁵)... EGFR showed hypomethylation in the promoter region." — confidence: medium — type: mechanistic — links: [[claims/hypoxia-integrative-multiomic-egfr-drug-response-network]] [[foundations/egfr-mutation-luad]]
- `[c11]` TP53 mutation frequency is higher in hypoxia score-high tumours across multiple cancer types (p.439) "62.3% (137 out of 220) and 73.5% (83 out of 113) of samples had TP53 mutations in hypoxia score-high BRCA and LUAD, while only 8.0%... and 34.6%... in hypoxia score-low." — confidence: high — type: correlational — links: [[claims/tp53-mutation-enriched-hypoxia-score-high]] [[foundations/tp53-tumor-suppressor]]
- `[c12]` Hypoxia-associated SCNAs harbour clinically actionable genes (p.440) "The 7p11.2 amplicon, which harbours EGFR, occurred more frequently in hypoxia score-high LGG samples (FDR=6.5×10⁻⁵)." — confidence: medium — type: correlational — links: [[claims/hypoxia-scna-harbour-actionable-genes]] [[foundations/gistic2-copy-number]]
- `[c13]` 90.9% of clinically actionable genes are biased by hypoxia status in at least one molecular layer (p.440) "90.9% (110 out of 121) of clinically actionable genes were associated with at least 1 type of hypoxia-associated molecular signature in at least 1 cancer type." — confidence: high — type: quantitative — links: [[claims/hypoxia-biases-clinically-actionable-genes-pancancer]]
- `[c14]` Tumour hypoxia bidirectionally modulates anticancer drug response (resistance and sensitivity) (p.440) "some tumours may become sensitive to several drugs under hypoxic conditions, such as thapsigargin in PAAD (rs=−0.66)... which suggests that patients with these cancers may not benefit from hypoxia-targeted therapy." — confidence: high — type: mechanistic — links: [[claims/hypoxia-bidirectional-anticancer-drug-response]] [[concepts/hypoxia-bidirectional-drug-response-modulation]]
- `[c15]` Lung cancer cell-line experiments confirm hypoxia-dependent drug resistance and sensitivity (p.440) "camptothecin and bexarotene showed greater drug resistance under the hypoxic condition, whereas... Akt inhibitor VIII and PHA-665752 showed greater sensitivity under the hypoxic condition for both A549 and H1299 cell lines." — confidence: high — type: pharmacological — links: [[claims/hypoxia-drug-response-lung-cell-line-validation]]
- `[c16]` High hypoxia score predicts worse prognosis after sorafenib in advanced NSCLC (BATTLE trial) (p.440) "patients with advanced NSCLC with high hypoxia scores were associated with worse prognosis after sorafenib treatment (log-rank test, P=8.6×10⁻³)." — confidence: medium — type: correlational — links: [[claims/high-hypoxia-score-worse-sorafenib-prognosis-nsclc]]

## Discussion captured

### Authors' interpretation

The authors argue that hypoxia remodels tumour molecular signatures at multi-omic levels through gene regulatory networks, and that this remodelling impacts a broad range of biological processes (metabolic reprogramming, angiogenesis, apoptosis, multiple signalling pathways) and ultimately drug response. They emphasise that 90.9% of clinically actionable genes are hypoxia-biased, confirming hypoxia-targeted therapy as attractive — most plausibly as a component of rational combination therapy.

### Comparisons with prior literature (made by authors)

- DNA hypermethylation under hypoxia via reduced TET activity (Thienpont et al. 2016, *Nature*).
- Hypoxia drives transient site-specific copy gain and drug-resistant expression (Black et al. 2015, *Genes Dev*).
- p53 mutation diminishes oxygen consumption; p53–HIF interplay (Amelio & Melino 2015).
- 15-gene signature best-performer (Fox et al. 2014; Buffa et al. 2010).
- Metformin-induced hypoxia reduction potentiates PD-1 blockade (prior immunotherapy work).

### Mechanistic hypotheses proposed

- Hypoxia-biased mRNA changes are partly driven by opposite-direction DNA methylation changes (p.436).
- IDH1 mutation promotes HIF-1α degradation, reducing hypoxic effect and improving survival in LGG (p.440).

### Caveats and self-criticism

- Hypoxia status is *inferred* (relative signature), not directly measured (no O2 levels in TCGA).
- Bulk data conflate cell types; single-cell resolution needed for tumour heterogeneity.
- Catalogue is largely associative; which alterations are *directly* hypoxia-caused remains open.
- Few clinical trials record tumour hypoxia status, limiting clinical validation.

### Future directions suggested

- Incorporate tumour hypoxia status into future clinical trial design.
- Apply single-cell profiling to resolve hypoxia heterogeneity.

## Limitations

- Indirect, relative hypoxia inference from an mRNA signature.
- Bulk-tissue resolution; no stromal/immune decomposition.
- Drug-response associations rely heavily on cell-line and imputed (not measured) patient data.
- Only a single clinical trial (BATTLE) available for outcome validation.

## Open questions

### Open questions raised by authors

- Which hypoxia-associated alterations are directly caused by hypoxia vs. merely correlated?
- How does intratumoral hypoxia heterogeneity (single-cell) modify these pan-cancer patterns?

### Open questions identified during ingest

- Can hypoxia status prospectively stratify patients into benefit/no-benefit arms for hypoxia-targeted or combination therapy?
- How do these bulk pan-cancer associations compare to single-cell/spatial hypoxia maps now available?

## My take

This is a foundational pan-cancer resource for the thesis's hypoxia axis: it reframes hypoxia from a uniform resistance driver to a bidirectional modulator of drug response, and provides a confounder-controlled multi-omic atlas (HAMFA) linking hypoxia status to clinically actionable genes. The propensity-score framework is a reusable method for any TCGA two-group molecular comparison. Complementary to [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]], which attacks the same pan-cancer hypoxia problem from a genomic-instability angle.

## Related

- [[concepts/pan-cancer-hypoxia-multiomic-landscape]]
- [[concepts/propensity-score-confounder-balanced-omics]]
- [[concepts/hypoxia-bidirectional-drug-response-modulation]]
- [[concepts/tumor-hypoxia-mrna-signature]]
- [[concepts/mir-210-hypoxia-induced-microrna]]
- [[concepts/warburg-effect-hif1a-glycolytic-reprogramming]]
- [[concepts/hypoxia-emt-lineage-plasticity-metastasis]]
- [[foundations/tcga-the-cancer-genome-atlas]]
- [[foundations/buffa-hypoxia-signature]]
- [[foundations/gistic2-copy-number]]
- [[foundations/oncopredict-drug-sensitivity]]
- [[foundations/tp53-tumor-suppressor]]
- [[foundations/pten-tumor-suppressor]]
- [[foundations/egfr-mutation-luad]]
- [[foundations/vhl-von-hippel-lindau]]
- [[foundations/hif1a]]
- [[foundations/mir-210-mirna]]
- [[foundations/vegf]]
- [[foundations/ndrg1]]
- [[foundations/ldh-lactate-dehydrogenase]]
- [[foundations/phd-prolyl-hydroxylases]]
- [[foundations/tet-mediated-dna-demethylation]]
- [[foundations/evofosfamide-th-302]]
- [[foundations/braf-kinase]]
- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]]
- [[people/youqiong-ye]]
- [[people/qingsong-hu]]
- [[people/liuqing-yang]]
- [[people/gordon-mills]]
- [[people/han-liang]]
- [[people/leng-han]]
