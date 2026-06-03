---
# === Identification ===
title: "Genomic investigation of innate sensing pathways in the tumor microenvironment"
slug: genomic-investigation-innate-sensing-pathways-tumor
arxiv: ""
doi: "10.1186/s12885-024-12944-w"
pmid: "39289651"
venue: "BMC Cancer"
year: 2024
authors: ["Gabriella Quinn", "Gianna Maggiore", "Bo Li"]
first_author: "Gabriella Quinn"
corresponding_author: "Bo Li"

# === Source & metadata ===
source_type: pdf
s2_id: "104c1d3d11c6a98bcfc07a891b3fad07dc137d3b"
date_added: 2026-06-03
ingested_date: 2026-06-03
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 3
tier: TIER_2
tags: [innate-immunity, cGAS-STING, TCGA, ssGSEA, tumor-microenvironment, PHF2, PHF8, intratumor-microbiome, colorectal-cancer]
keywords: [TCGA, innate immunity, cGAS-STING, tumor microenvironment, ssGSEA, pattern recognition receptors]
domain: oncology / immunology

# === Biomedical domain ===
tissue: [multi, colon, lung, bone_marrow]
condition: [cancer]
disease_specific: []
species: [human, mouse]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [bulk_RNA-seq, ssGSEA, qPCR, siRNA_knockdown, Cox_regression]
n_samples: 8554
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types: [tumor_cells, CD8_T_cells, neutrophils, dendritic_cells, bone_marrow_derived_macrophages, fibroblasts]
key_markers: [cGAS, IFNB1, IFNA2, PHF2, PHF8, TLR4, IL6, TNF, PDCD1, CTLA4, HAVCR2, LAG3, MUC16]
key_pathways: [cGAS-STING, TLR_signaling, NOD_signaling, RIG-I_signaling, CLR_signaling]

# === User project membership ===
projects: [thesis]
priority: context
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "GEO: GSE174141, GSE99298, GSE146009, GSE17538; TCGA (NCI GDC); intratumor microbe abundance from Poore et al. (ftp.microbio.me)"

# === Cross-references ===
code_url: "https://github.com/broadinstitute/ssGSEA2.0"
cited_by: []
---

## Problem

The innate immune system is the first responder to cancerous growths, priming T-cell-mediated cytotoxicity, yet it is understudied in cancer because its pattern-recognition-receptor (PRR) cascades are numerous, redundant, and intertwined. Tracking single receptors fails to capture pathway-level activation. The paper asks: can we quantify the activation of distinct innate sensing cascades genome-wide across many tumors, and use that to find clinical correlates and therapeutic targets?

## Key idea

Treat each innate cascade (cGAS, TLR, CLR, NOD/NLR, RIG-I) as a curated gene set and use single-sample GSEA (ssGSEA) to collapse its expression into a per-tumor activation score. Apply this custom 5-pathway ontology across 8,554 TCGA tumors (29 cancer types) to immunophenotype innate sensing and relate it to survival, immunogenicity, and the intratumor microbiome.

## Method

- **Data**: RSEM-normalized TCGA RNA-seq (Wang et al. 2018, hg19); copy number via TCGAbiolinks/RTCGAToolbox; intratumor microbe abundance from Poore et al. (SHOGUN on unaligned reads).
- **Custom ontology**: gene lists for cGAS/CLR/TLR/NOD/RIG-I manually curated from KEGG, GO, STRING plus reviews; deduplicated and verified against hg19 annotation; compiled to a `.gmt`.
- **Scoring**: ssGSEA (Barbie et al. single-sample extension; broadinstitute/ssGSEA2.0), raw rank metric, weight 0.75, KS statistic with 1000 permutations → normalized enrichment scores.
- **Validation**: scores tested on LPS-stimulated mouse BMDMs (TLR) and RSV-infected A549 cells (RIG-I/NOD).
- **Statistics**: partial correlations (ppcor), partial Cox regression (survival) controlling age/sex/stage/purity/infiltrate; TIMER for immune deconvolution; ANOVA/Mann-Whitney/t-tests; Benjamini-Hochberg correction.
- **Functional test**: siRNA knockdown of PHF2/PHF8 in HCT116 and wild-type vs cGAS-KO BJ fibroblasts; IFNB1/IFNA2 by RT-qPCR; cell death by LDH leakage.

## Results

- ssGSEA scores recapitulated innate activation under known viral/bacterial stimuli (validation datasets).
- Pan-cancer: cancer types differ in innate activation; innate scores predicted survival in a subset of cancers (direction varies by type).
- cGAS activation negatively associated with global transcription (834 genes down, 6 up), enriched for RNA-processing and DNA-repair downregulation.
- PHF2/PHF8 demethylases negatively associated with cGAS activation; combined copy loss elevated cGAS; MSI-H tumors had lower PHF2.
- siPHF2+siPHF8 increased IFNB1 and cell death; abolished in cGAS-KO cells → cGAS-dependent.
- In COAD, high innate activation tracked mutation burden, MUC16 mutation, immune infiltration, and exhaustion markers.
- Intratumor microbes showed weak, tissue-specific associations with innate scores (COAD-Escherichia/cGAS; LUSC-Alcanivorax/NOD).

## All claims (exhaustive)

- `[c1]` Custom 5-pathway ssGSEA ontology recapitulates innate activation by viral/bacterial stimuli (p.3-4) "by summarizing the key genes involved in the PRR pathways, we demonstrated that ssGSEA is an effective tool to generate scores that reflect innate immune activation by both viral and bacterial stimuli" — confidence: high — type: methodological — links: [[claims/custom-ssgsea-ontology-recapitulates-innate-immune]] [[concepts/innate-immune-pathway-ssgsea-immunophenotyping-pan]] [[foundations/ssgsea-single-sample-gsea]]
- `[c2]` Innate immune activation scores predict patient survival in a subset of TCGA cancers, with direction varying by type (p.5-6) "In some cancer types, high innate immune activation was hazardous and in others advantageous" — confidence: medium — type: correlational — links: [[claims/innate-immune-activation-predicts-patient-survival]] [[foundations/tcga-the-cancer-genome-atlas]]
- `[c3]` cGAS activation is negatively associated with global transcription pan-cancer (834 genes down, 6 up), enriched for RNA-processing/DNA-repair downregulation (p.6) "cGAS activation scores were negatively associated with 834 genes and positively associated with only 6 genes" — confidence: medium — type: correlational — links: [[claims/cgas-activation-negatively-associated-global-transcription]] [[foundations/cgas-cyclic-gmp-amp-synthase]]
- `[c4]` PHF2 and PHF8 are negatively associated with cGAS activation; combined copy-number loss elevates cGAS (p.6-7) "tumors that lost both copies of PHF2 and one copy of PHF8 had significantly elevated cGAS activation" — confidence: medium — type: correlational — links: [[claims/phf2-phf8-negatively-associated-cgas-activation]] [[concepts/phf-histone-demethylase-genomic-stability-cgas]] [[foundations/phf2-histone-demethylase]] [[foundations/phf8-histone-demethylase]]
- `[c5]` MSI-high tumors show significantly reduced PHF2 expression (p.6) "In tumors with high microsatellite instability, there was significantly less PHF2 expression" — confidence: medium — type: correlational — links: [[claims/microsatellite-instability-high-tumors-reduced-phf2]] [[foundations/phf2-histone-demethylase]]
- `[c6]` Combined PHF2/PHF8 knockdown increases IFNB1 and cell death in a cGAS-dependent manner (p.7) "cGAS knockout cell lines did not increase IFNB1 expression with reduction of PHF transcripts suggesting that this increase in IFNB1 expression may be cGAS-dependent" — confidence: high — type: pharmacological — links: [[claims/phf2-phf8-knockdown-increases-ifnb1-cell]] [[concepts/phf-histone-demethylase-genomic-stability-cgas]] [[foundations/type-interferon-ifna-ifnb]] [[foundations/sting-stimulator-of-interferon-genes]]
- `[c7]` In colorectal cancer, high innate activation associates with mutation burden, MUC16 mutation, and exhaustion markers (p.8-9) "Innate group 1, which had the highest innate activation, demonstrated the largest mutation burden ... also exhibited increased expression of immune cell exhaustion markers such as PDCD1 (PD1), CTLA4, HAVCR2 (TIM3), and LAG3" — confidence: medium — type: correlational — links: [[claims/colorectal-innate-activation-associated-mutation-burden]] [[concepts/innate-immune-activation-tumor-immunogenicity-immune]] [[foundations/timer-tumor-immune-deconvolution]]
- `[c8]` Intratumor microbial abundance shows weak, tissue-specific associations with innate activation (p.9) "these associations are not as strong as we expected in respect to their R values" — confidence: medium — type: correlational — links: [[claims/intratumor-microbes-weak-tissue-specific-association]] [[concepts/intratumor-microbiome-innate-immune-activation-association]]

## Discussion captured

### Authors' interpretation

The authors frame the study as a proof-of-concept that interrogating innate cascades *as whole pathways* (rather than single proteins) yields new insight: it revealed an inverse relationship between cGAS activation and both global transcription and the chromosome-stabilizing demethylases PHF2/PHF8, motivating PHF proteins as targets to boost cGAS signaling. They argue innate activation indexes tumor immunogenicity (mutation burden) and that intratumor microbes are only a weak contributor, implying additional PRR triggers (e.g., self-antigens/neoantigens).

### Comparisons with prior literature (made by authors)

- DNA damage induces global transcriptional stress by hindering RNA Pol II (Lans et al., Nat Rev Mol Cell Biol 2019).
- PHF2/PHF8 genome-stability roles (Alonso-de Vega 2020; Pappa 2019; Ma 2021, Sci Adv).
- cGAS/STING commonly downregulated in tumors despite genomic instability (Xia et al., Cell Rep 2016).
- Intratumor bacteria metabolize gemcitabine in pancreatic cancer (Geller et al., Science 2017); BCG as bladder-cancer adjuvant (Herr & Morales 2008).
- Microbiome diagnostic signatures (Poore et al., Nature 2020).

### Mechanistic hypotheses proposed

PHF2/PHF8 maintain genomic stability; their loss increases DNA damage (a cGAS ligand), de-repressing cGAS-STING and IFNB1. PRRs may help recognize self-antigens/neoantigens, contributing to immunogenicity beyond microbial sensing.

### Caveats and self-criticism

"This study is limited by its exploratory nature." Microbe associations are weak though significant; the work is positioned as a broad introduction to the scoring system and a foundation for future therapeutic-target/adjuvant work rather than definitive mechanism.

### Future directions suggested

Explore how/whether PRRs recognize self-antigens; pursue PHF proteins as adjuvant targets to boost cGAS; investigate MUC16/CA125 as a colon-cancer vaccine antigen; study microbiome-innate crosstalk for engineered-microbe therapies.

## Limitations

- Exploratory, correlational pan-cancer analysis; scores are transcriptional proxies, not protein/signaling activity.
- Functional validation limited to two cell lines (HCT116, BJ) with transient siRNA; no in vivo tumor efficacy.
- Microbiome abundance from unaligned TCGA reads carries contamination caveats; associations weak.
- Custom ontology choices influence scores; only five cascades modeled.

## Open questions

### Open questions raised by authors

- How and whether PRRs identify self-antigens/neoantigens.
- Why innate activation is protective in some cancers and hazardous in others.
- Whether MUC16 mutation-derived protein is a viable vaccine target.

### Open questions identified during ingest

- Is PHF inhibition pharmacologically tractable and tumor-selective in vivo?
- Do innate-high/exhausted CRC tumors preferentially respond to checkpoint blockade?
- Does the transcriptional suppression accompanying high cGAS reflect cause or consequence of DNA damage?

## My take

A pragmatic, hypothesis-generating framework relevant to the thesis's TME/innate-immunity interests. The standout, testable contribution is the PHF2/PHF8 → cGAS → IFNB1 axis with a clean cGAS-KO genetic control; the rest is correlative scaffolding (survival, immunogenicity, microbiome) useful for orientation. Modest venue and citation count (BMC Cancer, 2 citations at ingest), exploratory by the authors' own framing — value here is the reusable scoring concept and the PHF mechanistic hook rather than definitive results.

## Related

Concepts: [[concepts/innate-immune-pathway-ssgsea-immunophenotyping-pan]] · [[concepts/phf-histone-demethylase-genomic-stability-cgas]] · [[concepts/innate-immune-activation-tumor-immunogenicity-immune]] · [[concepts/intratumor-microbiome-innate-immune-activation-association]]

Foundations: [[foundations/ssgsea-single-sample-gsea]] · [[foundations/tcga-the-cancer-genome-atlas]] · [[foundations/cgas-cyclic-gmp-amp-synthase]] · [[foundations/sting-stimulator-of-interferon-genes]] · [[foundations/type-interferon-ifna-ifnb]] · [[foundations/phf2-histone-demethylase]] · [[foundations/phf8-histone-demethylase]] · [[foundations/timer-tumor-immune-deconvolution]]

Authors: [[people/gabriella-quinn]] · [[people/bo-li-ut-southwestern]]
