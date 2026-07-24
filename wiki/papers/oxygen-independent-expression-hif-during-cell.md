---
# === Identification ===
title: "Oxygen-independent expression of HIF-1α during the cell cycle in hepatocellular carcinoma cells controls essential metabolic pathways under normoxia"
slug: oxygen-independent-expression-hif-during-cell
arxiv: ""
doi: "10.1111/febs.70334"
pmid: ""
venue: "The FEBS Journal"
year: 2026
authors:
  - "Ioanna-Maria Gkotinakou"
  - "Christina Arseni"
  - "Kreon Koukoulas"
  - "Martina Samiotaki"
  - "George Panayotou"
  - "George Simos"
  - "Ilias Mylonis"
first_author: "Ioanna-Maria Gkotinakou"
corresponding_author: "Ilias Mylonis"

# === Source & metadata ===
source_type: pdf
s2_id: ""
date_added: 2026-07-24
ingested_date: 2026-07-24
ingest_version: 1
last_reviewed: null

# === Classification ===
importance: 3
tier: TIER_2
tags:
  - HIF1a
  - hypoxia
  - normoxia
  - hepatocellular-carcinoma
  - cell-cycle
  - CDK1
  - glycolysis
  - cholesterol
  - steroid-biosynthesis
  - proteomics
  - CRISPR-knockout
  - cancer-metabolism
keywords:
  - HIF-1α
  - HCC
  - Huh7
  - HeLa
  - HepG2
  - normoxia
  - cell cycle
  - CDK1
  - cyclin B1
  - glycolysis
  - cholesterol biosynthesis
  - LC-MS/MS proteomics
  - DIA-NN
  - TCGA
  - LIHC
domain: "oncology / hypoxia-signaling / cancer-metabolism"

# === Biomedical domain ===
tissue:
  - liver
  - in_vitro_only
condition:
  - cancer
disease_specific:
  - hepatocellular_carcinoma
  - cervical_carcinoma
species:
  - human
hypoxia_relevant: true
contains_immune_cells: false
contains_myeloid: false

# === Technique ===
techniques:
  - LC-MS/MS_proteomics_DIA
  - CRISPR-Cas9
  - shRNA_knockdown
  - western_blot
  - RT-qPCR
  - reporter_gene_assay
  - flow_cytometry
  - immunoprecipitation
  - cell_cycle_synchronization
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types:
  - Huh7 hepatocellular carcinoma cells
  - HepG2 hepatocellular carcinoma cells
  - HeLa cervical carcinoma cells
key_markers:
  - HIF1A
  - HIF2A
  - HK2
  - GAPDH
  - CDK1
  - Cyclin B1
  - MCM3
  - EGFR
  - CUL2
key_pathways:
  - glycolysis/gluconeogenesis
  - steroid/cholesterol biosynthesis
  - HIF-1 signaling
  - cell cycle
  - oxidative phosphorylation
  - TCA cycle

# === User project membership ===
projects:
  - thesis
  - hypoxia
priority: context
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: ""

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

The transcriptional and metabolic role of HIF-1α under hypoxia is well studied, but its function under **normoxia** — especially at the protein level, and in specific cancer types — is poorly explored. Most HIF-1 studies rely on genomic/transcriptomic data (HIF-1α chromatin occupancy or mRNA), which need not reflect protein-level changes, and proteomic studies of the direct, HIF-1α-specific proteome in a defined cancer context are rare. Hepatocellular carcinoma (HCC), where HIF-1α overexpression correlates with poor prognosis and therapeutic options are limited, is a clinically important but under-characterized setting for defining a HIF-1-dependent protein signature and its phenotypic consequences.

## Key idea

Using CRISPR/Cas9 to abolish endogenous HIF-1α in hepatoma (Huh7) and, for comparison, cervical carcinoma (HeLa) cells, the authors show that HIF-1α is essential for HCC-cell survival and metabolism **even under normoxia** — not just hypoxia. LC-MS/MS proteomics reveals that normoxic HIF-1α maintains glycolytic/gluconeogenic and steroid/cholesterol biosynthetic enzymes in Huh7 (but not HeLa). The paradox that HIF-1α is undetectable in asynchronous normoxic Huh7 cultures yet functionally required is resolved by a **transient, cell-cycle-dependent normoxic HIF-1α pulse** at G2/M (coincident with CDK1/cyclin B1), stabilized by a block in ubiquitination rather than loss of proline hydroxylation. The resulting HIF-1α-dependent protein signatures correlate with poor survival in LIHC patients.

## Method

- **Cell lines**: human hepatoma Huh7 (CVCL_0336) and HepG2 (CVCL_0027); human cervical carcinoma HeLa_S3 (CVCL_0058). Normoxia = 21% O₂; hypoxia = 1% O₂ (24 h).
- **HIF1A knockout**: CRISPR/Cas9 Double Nickase (Santa Cruz) in Huh7; sequencing-verified indel around exon 2; previously reported HeLa HIF1A⁻/⁻ used for comparison. HepG2 silenced by shRNA (pSuper-shHIF-1α).
- **Rescue / specificity**: stable pEGFP-C1-HIF-1α (GFP-HIF-1α) or GFP-only re-expression in the knockout lines; HRE-luciferase (pGL3-5xHRE-VEGF-Luc) reporter assays normalized to Renilla.
- **Phenotype**: WST-1 proliferation and LDH cytotoxicity assays over 0–48 h at 21%/1% O₂.
- **Proteomics**: SP3-based sample prep, LC-MS/MS on a Dionex Ultimate3000RSLC + Thermo Q Exactive HF-X (data-independent acquisition), analyzed with DIA-NN 1.8 (library-free, double-pass; 1% FDR; gene-level inference; MaxLFQ normalization); two biological replicates + a confirmatory third; Perseus/R downstream.
- **Pathway analysis**: KEGG enrichment; hierarchical clustering of LFQ values; validation of representative proteins (HK2, GAPDH, steroidogenic enzymes, MCM3) by western blot.
- **Cholesterol**: total cholesterol (free + esters) assay normalized to protein (n=8).
- **Cell-cycle synchronization**: 5 µM RO-3306 (CDK1 inhibitor) ~18–20 h, release, immunoblot HIF-1α / cyclin B1 / CDK1 at timepoints; PI flow-cytometry cell-cycle analysis; HIF-1α immunoprecipitation with anti-hydroxyproline / anti-ubiquitin.
- **Clinical correlation**: TCGA LIHC and CESC via GEPIA2 — signature-to-HIF1A correlation and Kaplan–Meier overall survival for HIF-1α-upregulated protein signatures.

## Results

- Both Huh7 and HeLa HIF1A⁻/⁻ cells are sensitive to hypoxia, but **only Huh7** shows increased death/reduced proliferation under normoxia; GFP-HIF-1α rescues survival (excluding CRISPR off-target effects).
- Under 21% O₂, Huh7 and GFP-HIF-1α Huh7 show measurable HIF transcriptional (HRE) activity despite undetectable HIF-1α by immunoblot; HeLa does not.
- HIF1A knockout deregulates ~26% of the identified Huh7 proteome vs ~10% of HeLa under normoxia (Huh7: 217 up + 592 down; HeLa: 428 up + 215 down by HIF-1α).
- KEGG: normoxic HIF-1α upregulates carbon metabolism, glycolysis/gluconeogenesis, and steroid biosynthesis in Huh7; downregulates oxidative phosphorylation / TCA / NAFLD-associated proteins. HeLa's normoxic HIF-1α targets differ (ferroptosis, RNA-pol transcription).
- Glycolytic cluster (incl. HK2, GAPDH) is HIF-1α-induced irrespective of O₂ in Huh7; validated in HepG2 (shHIF-1α downregulates HK2/GAPDH at 21% and 1% O₂). In HeLa the analogous cluster is HIF-1α-dependent mainly under hypoxia.
- Steroid/cholesterol biosynthetic enzymes and total cholesterol are HIF-1α-dependent under normoxia in Huh7 but not HeLa.
- Synchronized (RO-3306 release) normoxic Huh7 (and HepG2) WT cells transiently express HIF-1α at 5–8 h post-release (G2→M, tracking cyclin B1 and a CDK1 peak); HeLa never does.
- Immunoprecipitated normoxic G2/M HIF-1α is partially proline-hydroxylated but not substantially ubiquitinated → stabilization via blocked ubiquitination/degradation.
- HIF-1α downregulates DNA-replication-licensing proteins (MCM3 verified) under normoxia in Huh7 (not HeLa); WT vs KO Huh7 differ in G1 fraction (70% vs 60.1%).
- Huh7-derived normoxic (P=0.0023) and hypoxic (P=0.0081) HIF-1α signatures predict poor LIHC survival and correlate with HIF1A; HeLa-derived signatures show no CESC survival correlation (P=0.85 / P=0.4).

## All claims (exhaustive)

- `[c1]` HIF-1α is essential for HCC (Huh7) cell survival and proliferation even under normoxia (p.3140,3142) "under normoxia, only HIF1A−/− Huh7 cells showed increased death and reduced proliferation rates compared to wild-type Huh7 cells, implying that HIF-1α is essential for hepatocellular carcinoma cell survival irrespective of oxygen levels" — confidence: high — type: mechanistic — links: [[foundations/hif1a]] [[foundations/huh7-hepatoma-cell-line]] [[claims/hif1a-essential-hcc-survival-normoxia]]
- `[c2]` The normoxic growth dependency on HIF-1α is HCC-specific (Huh7) and absent in HeLa (p.3142) "under normoxia, only the hepatoma-derived Huh7 cells exhibited significant sensitivity to the absence of HIF-1α ... indicating that there is a cell-specific HIF-1α role even in the presence of abundant oxygenation" — confidence: high — type: correlational — links: [[foundations/hela-cell-line]] [[foundations/huh7-hepatoma-cell-line]] [[claims/hif1a-normoxic-growth-dependency-hcc-specific]]
- `[c3]` HIF-1α maintains glycolytic/gluconeogenic enzyme expression (HK2, GAPDH) under normoxia in HCC cells, validated in HepG2 (p.3152,3154) "Silencing of HIF-1α expression in HepG2 cells by shRNA resulted in the downregulation of two representative glycolytic enzymes (hexokinase 2 and GAPDH) under both normoxia and hypoxia, confirming the normoxic role of HIF-1α in HCC cells" — confidence: high — type: methodological — links: [[concepts/hif1a-normoxic-metabolic-dependency-hcc]] [[foundations/hk2-hexokinase-2]] [[foundations/hepg2-hepatoma-cell-line]] [[claims/hif1a-maintains-glycolytic-enzymes-normoxia-hcc]]
- `[c4]` HIF-1α maintains steroid/cholesterol biosynthetic enzymes and total cholesterol under normoxia in Huh7 but not HeLa (p.3154) "both normoxic and hypoxic cholesterol contents were strongly reduced in the absence of HIF-1α ... the absence of HIF-1α did not significantly affect cholesterol concentration under either normoxia or hypoxia [in HeLa]" — confidence: high — type: quantitative — links: [[concepts/hif1a-normoxic-metabolic-dependency-hcc]] [[claims/hif1a-maintains-cholesterol-steroid-biosynthesis-normoxia-hcc]]
- `[c5]` HIF-1α is transiently expressed in normoxic Huh7/HepG2 cells at the G2→M transition, coincident with cyclin B1/CDK1, and undetectable in asynchronous cultures (p.3154-3155) "Only the synchronized Huh7 WT cells expressed significant levels of HIF-1α at time points that coincide with the transition of cells from G2 to M (5 h and 8 h post-release) ... in HeLa WT cells, HIF-1α remained undetectable" — confidence: medium — type: mechanistic — links: [[concepts/normoxic-cell-cycle-dependent-hif1a-hcc]] [[foundations/ro-3306-cdk1-inhibitor]] [[foundations/cyclin-b1-ccnb1]] [[claims/hif1a-transient-cell-cycle-normoxic-expression-hcc]]
- `[c6]` Normoxic cell-cycle HIF-1α is stabilized by blocked ubiquitination, not loss of proline hydroxylation, coincident with a CDK1 peak (p.3155) "Although HIF-1α was shown to be, at least partially, hydroxylated, no substantial ubiquitination could be detected ... stabilization of HIF-1α at the particular cell cycle phase is not due to lack of hydroxylation but rather due to inhibition of its subsequent ubiquitination and degradation" — confidence: medium — type: mechanistic — links: [[concepts/normoxic-cell-cycle-dependent-hif1a-hcc]] [[foundations/cdk1-cyclin-dependent-kinase-1]] [[foundations/phd-prolyl-hydroxylases]] [[claims/normoxic-hif1a-stabilized-by-ubiquitination-block-not-hydroxylation]]
- `[c7]` HIF-2α (expressed in Huh7) cannot compensate for HIF-1α loss in HCC cells (p.3156) "despite the ability of Huh7 cells to express HIF-2α, they were unable to adapt (either under normoxia or hypoxia) to the knockout of HIF-1α, suggesting that, in HCC cells, HIF-2α cannot compensate for the loss of HIF-1α" — confidence: high — type: mechanistic — links: [[foundations/hif2a]] [[claims/hif2a-cannot-compensate-hif1a-loss-hcc]]
- `[c8]` ~26% of the identified Huh7 proteome vs ~10% of HeLa is HIF-1α-dependent under normoxia (p.3146) "the expression of approximately 26% of the total proteins identified in Huh7 cells and 10% of the total proteins identified in HeLa cells was affected by HIF1A knockout under normoxia" — confidence: high — type: quantitative — links: [[foundations/dia-nn-proteomics]] [[claims/hif1a-controls-26pct-huh7-proteome-normoxia]]
- `[c9]` HIF-1α downregulates DNA-replication-licensing proteins (MCM3 verified) under normoxia in Huh7 but not HeLa (p.3155-3156) "the expression of several proteins involved in the licensing of DNA replication was significantly downregulated by HIF-1α in Huh7 cells ... but not in HeLa cells. The proteomic data were verified in the case of MCM3" — confidence: medium — type: correlational — links: [[foundations/mcm3-minichromosome-maintenance-3]] [[claims/hif1a-downregulates-mcm-replication-licensing-normoxia-hcc]]
- `[c10]` Huh7-derived normoxic (P=0.0023) and hypoxic (P=0.0081) HIF-1α protein signatures correlate with poor LIHC survival, whereas HeLa-derived signatures do not predict CESC survival (p.3156-3157) "Kaplan-Meier survival analysis showed a significant correlation between higher expression of our normoxic (P = 0.0023) or hypoxic (P = 0.0081) HIF-1α-dependent signatures derived from Huh7 cells and poor outcomes for LIHC patients" — confidence: high — type: correlational — links: [[foundations/gepia2-gene-expression-profiling]] [[foundations/tcga-the-cancer-genome-atlas]] [[claims/normoxic-hif1a-signature-poor-prognosis-lihc]]

## Discussion captured

### Authors' interpretation

The authors interpret HIF-1α as a constitutive, cell-type-specific controller of HCC metabolism and growth that operates **regardless of oxygen level**. In Huh7 (but not HeLa), HIF-1α sustains glycolysis/gluconeogenesis and steroid/cholesterol biosynthesis and induces glucose/amino-acid transporters, reflecting the higher biosynthetic potential of liver cells. The apparent absence of HIF-1α in asynchronous normoxic cultures is explained by a transient, cell-cycle-restricted pulse of HIF-1α at G2/M, stabilized by CDK1-associated inhibition of ubiquitination. They argue this reframes HIF-1 as important for HCC even in well-oxygenated tumor regions and as a cell-type-specific therapeutic target.

### Comparisons with prior literature (made by authors)

- Warfel/Dang-type CDK1-Ser668 phosphorylation stabilizing normoxic HIF-1α at G2/M in colon carcinoma cells (ref [28]) — the mechanistic precedent extended here to HCC.
- Cyclin E stimulation of HIF-1α in mammary epithelial cells via E2F1 and EGLN1/PHD2 downregulation (ref [49]) — a related G1 cell-cycle route.
- A recent meta-analysis (ref [34]) linking HIF-1α inactivation to G1 arrest via CDKIs and CDK2/cyclin E.
- A recent study (ref [42]) showing transient elimination of G1-expressed HIF-1α reduces key amino acids and carbohydrates.
- Reviews correlating high HIF-1α (not HIF-2α) with poor HCC prognosis (ref [9]).
- Prior observations of small overlap in HIF-1 target expression across cell lines at the mRNA level (refs [44,45]) attributed to differing coactivator repertoires.

### Mechanistic hypotheses proposed

- **Cell-cycle pulse hypothesis**: transient normoxic HIF-1α at G2/M (a small subpopulation) is sufficient to maintain HIF-1-dependent metabolic protein expression across the asynchronous population; "the transient expression of HIF-1α in a small subpopulation of Huh7 cells can explain its apparent lack of expression in immunoblotting experiments with asynchronous cultures."
- **Ubiquitination-block hypothesis**: CDK1-coincident stabilization is due to inhibition of HIF-1α ubiquitination downstream of (retained) proline hydroxylation.
- **Liver-metabolic-potential hypothesis**: HCC-specific normoxic HIF-1 dependency reflects the intrinsically high biosynthetic/metabolic potential of liver cells.

### Caveats and self-criticism

- Small overlap of HIF-1α-upregulated proteins between Huh7 and HeLa is attributed to cell-line-specific coactivators and possible HIF-α isoform-specific functions, but not directly dissected.
- HIF-2α non-compensation is inferred from failure to rescue (endogenous levels), not from gain-of-function testing.
- The ubiquitination-block mechanism rests on a single IP timepoint and imports CDK1 causality from prior colon-carcinoma work.

### Future directions suggested

- Detailed investigation of oxygen-level-dependent HIF-1 protein signatures to identify novel, cell-type-specific therapeutic targets for high-lethality cancers such as HCC.

## Limitations

- In vitro cell-line study (Huh7, HepG2, HeLa); no in vivo tumor models or patient-derived material beyond TCGA signature correlation.
- Core proteomics based on two biological replicates (with a confirmatory third); protein levels only — no enzymatic-activity or metabolic-flux measurements (except a static cholesterol pool).
- Cell-cycle findings depend on RO-3306 synchronization, which perturbs physiology; the "transient" pulse is inferred from population immunoblots across timepoints.
- Mechanism of stabilization (ubiquitination block, CDK1 dependence) is correlative/inferred, not established by genetic perturbation of the E3/CDK1 step in HCC cells.
- Clinical correlations (GEPIA2/TCGA) are mRNA-based proxies for protein signatures and are associative, without multivariable adjustment.

## Open questions

### Open questions raised by authors

- Which coactivator/isoform differences make HCC (but not HeLa) cells normoxia-dependent on HIF-1α?
- Does HIF-1α directly regulate cell-cycle/replication-licensing genes, and how does the G2/M pulse couple to metabolite demand at G1/S?
- Can oxygen-level-dependent HIF-1 signatures define cell-type-specific intervention strategies in HCC?

### Open questions identified during ingest

- Is normoxic HIF-1α-maintained glycolysis/cholesterol reflected in measurable glucose flux, lactate output, or sterol synthesis in HCC under normoxia?
- What fraction of an asynchronous normoxic HCC population carries active HIF-1 at any instant, and is the pulse quantitatively sufficient for the observed proteome dependency?
- Is normoxic HIF-1α-dependent cholesterol supply a druggable HCC vulnerability independent of tumor oxygenation?

## My take

The value here is conceptual: HIF-1α "off under normoxia" is a population-average artifact. A cell-cycle-gated normoxic pulse makes HIF-1 a constitutive metabolic controller in HCC, with an underappreciated cholesterol/steroid arm alongside the classic glycolysis axis. For a hypoxia-focused thesis, this is a useful caution — HIF activity can be functionally present even where oxygen (and standard immunoblots) say it should be absent. The mechanistic backbone (CDK1 → ubiquitination block) is imported rather than proven here, and everything is in vitro, so it sits as a well-motivated, moderately-powered mechanistic study (importance 3) rather than a definitive result.

## Related

- Introduces [[concepts/normoxic-cell-cycle-dependent-hif1a-hcc]] — cell-cycle-dependent transient normoxic HIF-1α stabilization at G2/M.
- Introduces [[concepts/hif1a-normoxic-metabolic-dependency-hcc]] — HCC-specific normoxic HIF-1α control of glycolysis and cholesterol/steroid biosynthesis.
- Uses [[concepts/warburg-effect-hif1a-glycolytic-reprogramming]] — extends the HIF-1/glycolysis paradigm from hypoxia into normoxia.
- Foundations: [[foundations/hif1a]], [[foundations/hif2a]], [[foundations/phd-prolyl-hydroxylases]], [[foundations/vhl-von-hippel-lindau]], [[foundations/hepatocellular-carcinoma-hcc]], [[foundations/huh7-hepatoma-cell-line]], [[foundations/hepg2-hepatoma-cell-line]], [[foundations/hela-cell-line]], [[foundations/cdk1-cyclin-dependent-kinase-1]], [[foundations/cyclin-b1-ccnb1]], [[foundations/mcm3-minichromosome-maintenance-3]], [[foundations/hk2-hexokinase-2]], [[foundations/ro-3306-cdk1-inhibitor]], [[foundations/dia-nn-proteomics]], [[foundations/gepia2-gene-expression-profiling]], [[foundations/tcga-the-cancer-genome-atlas]], [[foundations/kegg-pathway-database]].
- People: [[people/ioanna-maria-gkotinakou]], [[people/christina-arseni]], [[people/george-simos]], [[people/ilias-mylonis]].
