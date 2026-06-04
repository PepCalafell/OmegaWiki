---
# === Identification ===
title: "Chinese Immune Multi-Omics Atlas"
slug: chinese-immune-multi-omics-atlas
arxiv: ""
doi: "10.1126/science.adt3130"
pmid: ""
venue: "Science"
year: 2026
authors:
  - Jianhua Yin
  - Yuhui Zheng
  - Zhuoli Huang
  - Wenwen Zhou
  - Yue Yuan
  - Pengfei Cai
  - Yong Bai
  - Miguel A. Esteban
  - Yanan Cao
  - Xun Xu
  - Longqi Liu
  - Xin Jin
  - Chuanyu Liu
first_author: "Jianhua Yin"
corresponding_author: "Yanan Cao; Xun Xu; Longqi Liu; Xin Jin; Chuanyu Liu"

# === Source & metadata ===
source_type: pdf
s2_id: ""
date_added: 2026-06-04
ingested_date: 2026-06-04
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 5
tier: TIER_1
tags: [immune-atlas, multi-omics, xqtl, single-cell, gene-regulatory-network, population-genomics, chromatin-accessibility, cell-language-model]
keywords: [CIMA, eQTL, caQTL, SMR, scATAC-seq, scRNA-seq, eRegulon, GWAS, Chinese cohort, noncoding variants]
domain: "genomics"

# === Biomedical domain ===
tissue: [blood]
condition: [healthy]
disease_specific: [asthma, rheumatoid_arthritis, type_2_diabetes]
species: [human]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [scRNA-seq_10x, scATAC-seq, WGS, lipidomics, metabolomics]
n_samples: 428
n_cells_total: 10247216
integration_method: "scGLUE"

# === Biology captured ===
key_cell_types: [CD4 Treg-FOXP3, cMono-CD14, CD8 CTL-GZMK, ncMono-FCGR3A, NK cells, B cells, dendritic cells, HSPC]
key_markers: [IKZF4, PADI2, IL-12B, FOXP3, CCR6, NPAS2, NR1D1, SLC16A11, S100A12]
key_pathways: [enhancer-driven gene regulatory networks, cis-regulation, chromatin accessibility, circadian regulation, T cell-mediated immunity]

# === User project membership ===
projects: [thesis, methods]
priority: reference
read_status: not_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "CIMA Portal https://db.cngb.org/trueblood/cima"

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

A mechanistic understanding of human immune variation and immune-mediated disease requires linking genetic variants to gene regulation at cell type resolution. Progress has been impeded by (i) the scarcity of large-scale single-cell ATAC-seq from PBMCs and (ii) the bias of existing regulatory/QTL resources toward individuals of European ancestry. Genetic factors account for only ~20–40% of interindividual immune variation, and bulk approaches cannot resolve closely related cell states.

## Key idea

Build a population-scale, multi-omics, cell type–resolved atlas of circulating immune cells in a Chinese cohort (CIMA) that integrates scRNA-seq, scATAC-seq, and WGS to (1) construct enhancer-driven gene regulatory networks, (2) map cell type–resolved eQTLs and caQTLs and integrate them with GWAS via SMR to find pleiotropic disease mechanisms, and (3) train a cell language model (CIMA-CLM) that predicts chromatin accessibility and scores noncoding variants from sequence + single-cell expression.

## Method

- **Cohort & data**: 428 Chinese adults (189 M / 239 F, ages 20–77, no active disease); 10,247,216 PBMCs profiled (6,484,974 scRNA-seq + 3,762,242 scATAC-seq), plus plasma lipidomics (1228 species), metabolomics (321 species), blood biochemistry, and WGS from plasma cell-free DNA.
- **Annotation**: iterative clustering into a 4-level hierarchy ending in 73 L4 immune cell types; cross-validated with Azimuth and CellTypist; RNA↔ATAC label transfer via scGLUE.
- **Regulatory elements & GRNs**: MACS3/SnapATAC2 peak calling → 338,036 cCREs (501-bp); HOMER annotation; eRegulon inference → 404 eRegulons (237 high-quality).
- **xQTL**: pseudobulk per cell type; TensorQTL cis-mapping (±1 Mb) with age/sex/genotype-PC/PEER covariates; trans-eQTL scan; scPME dynamic-eQTL modeling in B cells and monocytes.
- **Integration**: SMR (with HEIDI) across 154 traits (in-house lipid/metabolite GWAS + 91 inflammatory proteins + immune-disease GWAS).
- **Model**: CIMA-CLM fuses pretrained HyenaDNA (DNA) and scGPT (cell) embeddings via cross-attention to predict accessibility; in silico single-nucleotide mutagenesis for variant effects.

## Results

- 73 transcriptionally distinct immune cell types; rare types resolved below 0.1% frequency.
- MOFA recovered a sex-associated factor (e.g. 2,3-diphosphoglyceric acid, CD8 CTL-GZMB in males) and age-associated factors (e.g. factor 7 in DC2-CD1C; CX3CR1/CCR2 up, SERTAD1/IER3 down with age).
- 9600 eGenes and 52,361 caPeaks; mean π1 0.69/0.62 and rb 0.82/0.79 (eQTL/caQTL).
- 1196 SMR pleiotropic associations across 68 cell types; 73.2% single-cell-type. Headline mechanisms: rs34415530→IKZF4 (Treg)→IL-12B/asthma; rs2235922→PADI2 (monocyte)→RA; rs312457→SLC16A11 (CD4 T)→T2D.
- CIMA-CLM: mean PCC 0.8951, AUROC 0.9560 across 32 cell types; outperforms scOpen/scBasset/Epiformer/DeepSEA; in silico mutagenesis matches SMR/GWAS for VASH1 and SYNGR1 (RA) variants.

## All claims (exhaustive)

- `[c1]` Immune xQTL effects are largely cell type–specific (p.7-8) "2769 (28.84%) eGenes and 28,898 (55.19%) caPeaks were specific to a single cell type" — confidence: high — type: correlational — links: [[claims/immune-xqtl-effects-largely-cell-type]] [[concepts/cell-type-specific-genetic-regulation-immune]]
- `[c2]` Most SMR pleiotropic associations act in a single cell type (p.8-9) "73.2% of these associations were significant in only a single cell type" — confidence: high — type: quantitative — links: [[claims/majority-smr-pleiotropic-associations-single-cell]] [[foundations/summary-data-based-mendelian-randomization-smr]]
- `[c3]` rs34415530 lowers Treg IKZF4, affecting IL-12B and asthma (p.9) "the T allele at rs34415530 reduced the expression of IKZF4 in CD4 Treg-FOXP3 ... possibly promoting IL-12B secretion" — confidence: medium — type: mechanistic — links: [[claims/rs34415530-regulates-ikzf4-treg-affecting-il]] [[foundations/ikzf4-eos-transcription-factor]] [[foundations/il-12b-interleukin-12b-subunit]]
- `[c4]` rs2235922 up-regulates monocyte PADI2, linked to RA (p.9) "the A allele of rs2235922 enhances RA risk by up-regulating PADI2 in monocytes" — confidence: medium — type: mechanistic — links: [[claims/rs2235922-upregulates-padi2-monocytes-increasing-rheumatoid]] [[foundations/padi2-peptidylarginine-deiminase]]
- `[c5]` CIMA-CLM accurately predicts cell type accessibility (p.11-12) "median PCC values ranging from 0.7661 to 0.9612 (overall mean = 0.8951)" — confidence: high — type: methodological — links: [[claims/cima-clm-accurately-predicts-cell-type]] [[concepts/cima-clm-chromatin-accessibility-cell-language]]
- `[c6]` CIMA-CLM outperforms existing accessibility models (p.12) "superior performance ... over several existing sequence-free and sequence-based models, including scOpen, scBasset, Epiformer, and DeepSEA" — confidence: medium — type: methodological — links: [[claims/cima-clm-outperforms-existing-chromatin-accessibility]] [[concepts/cima-clm-chromatin-accessibility-cell-language]]
- `[c7]` CIMA profiles >10M PBMCs from 428 adults into 73 cell types (p.1-2) "profiling 10,247,216 PBMCs from 428 Chinese adults ... defined 73 transcriptionally distinct immune cell types" — confidence: high — type: methodological — links: [[claims/cima-profiles-ten-million-pbmcs-428]] [[foundations/scrna-seq-10x-chromium]] [[foundations/atac-seq]]
- `[c8]` Immune cCREs are predominantly distal noncoding elements (p.6) "Only 6.9% of the cCREs were located in promoter regions, whereas the majority were in intronic (31.2%) and intergenic (20.7%) regions or overlapped with transposable elements (32.9%)" — confidence: high — type: quantitative — links: [[claims/immune-ccres-predominantly-distal-noncoding-regulatory]] [[foundations/snapatac2-single-cell-atac-workflow]]
- `[c9]` CIMA-specific cCREs are predominantly cell type restricted (p.6) "the nonoverlapping, CIMA-specific elements were predominantly restricted to a single cell type (>50%)" — confidence: high — type: correlational — links: [[claims/cima-specific-ccres-predominantly-cell-type]] [[concepts/cell-type-specific-genetic-regulation-immune]]
- `[c10]` Enhancer-driven GRN links 84,625 regions to 13,645 genes via eRegulons (p.4-6) "404 enhancer-linked regulatory units (eRegulons), comprising 84,625 regulatory regions and 13,645 target genes" — confidence: high — type: methodological — links: [[claims/enhancer-driven-grn-links-regulatory-regions]] [[concepts/enhancer-driven-gene-regulatory-network-eregulon]] [[foundations/glue-multiomics-integration]]
- `[c11]` CIMA identifies 9600 eGenes and 52,361 caPeaks (p.7) "We identified 9600 eGenes and 52,361 caPeaks across the cell types analyzed" — confidence: high — type: quantitative — links: [[claims/cima-identifies-9600-egenes-52361-capeaks]] [[foundations/tensorqtl]]
- `[c12]` xQTL effects show substantial but variable cross-cell-type sharing (p.7-8) "mean π1 values were 0.69 for eQTLs and 0.62 for caQTLs, whereas the mean rb values were 0.82 and 0.79" — confidence: high — type: quantitative — links: [[claims/immune-xqtl-genetic-effects-show-substantial]] [[concepts/cell-type-specific-genetic-regulation-immune]]
- `[c13]` A subset of xQTLs reflects ancestry-specific effects (p.8) "10.4% had a MAF of <0.01 in European, African, or the overall ALFA populations, which suggests that a subset of xQTLs may reflect ancestry-specific regulatory effects" — confidence: medium — type: correlational — links: [[claims/subset-immune-xqtls-reflects-ancestry-specific]] [[concepts/ancestry-specific-immune-regulatory-variation]]
- `[c14]` Higher cells-per-sample drives greater cis-eGene discovery (p.8) "the higher average number of cells per sample in CIMA largely explains the greater number of cis-eGenes detected compared with OneK1K" — confidence: medium — type: methodological — links: [[claims/higher-cells-per-sample-increases-cis]] [[foundations/tensorqtl]]
- `[c15]` Many lead cis-eQTLs are dynamic along pseudotime (p.8) "32% of lead cis-eQTLs in B cells and 46.9% of lead cis-eQTLs in monocytes exhibited dynamic effects" — confidence: medium — type: quantitative — links: [[claims/many-lead-cis-eqtls-exhibit-dynamic]] [[concepts/dynamic-eqtl-along-differentiation-pseudotime]]
- `[c16]` rs11886530 acts as cis-eQTL on NPAS2 and trans-eQTL on NR1D1 (p.7) "Variant chr2:100809622 (rs11886530) exerts a cis effect on NPAS2 expression ... also mediated a trans effect on NR1D1 expression" — confidence: medium — type: mechanistic — links: [[claims/rs11886530-exerts-cis-eqtl-npas2-trans]] [[concepts/cell-type-specific-genetic-regulation-immune]]
- `[c17]` Cytotoxic T cell GRN TF activity increases with age (p.6) "TFs such as EOMES, RUNX3, and TBX21 showed significant positive correlations with age" — confidence: medium — type: correlational — links: [[claims/cytotoxic-cell-grn-transcription-factor-activity]] [[concepts/enhancer-driven-gene-regulatory-network-eregulon]]
- `[c18]` Immune TF activity shows sex-biased differences (p.6) "TFs including HIF1A, NFKB1, and STAT5B showed higher activity in females, whereas BHLHE40 was more active in males" — confidence: medium — type: correlational — links: [[claims/immune-transcription-factor-activity-shows-sex]] [[foundations/stat1-tf]]
- `[c19]` rs312457 regulates SLC16A11 in CD4 T, linked to T2D (p.9-10) "it may contribute to T2D susceptibility by modulating SLC16A11 expression in T cells" — confidence: medium — type: mechanistic — links: [[claims/rs312457-regulates-slc16a11-cells-linked-type]] [[concepts/ancestry-specific-immune-regulatory-variation]]
- `[c20]` CIMA-CLM in silico mutagenesis predicts noncoding variant effects (p.12) "in silico mutagenesis ... the variant rs2069235 ... would enhance chromatin accessibility ... aligned well with SMR findings" — confidence: medium — type: methodological — links: [[claims/cima-clm-silico-mutagenesis-predicts-noncoding]] [[concepts/cima-clm-chromatin-accessibility-cell-language]]

## Discussion captured

### Authors' interpretation

The authors frame CIMA as addressing a key gap in large-scale single-cell multi-omics profiling in the Chinese population. They emphasize that both the characteristics of circulating immune cells and the regulatory mechanisms governing them are cell type–specific, underscoring the complexity of cellular molecular networks and the need for high-resolution technologies. They enumerate five resource contributions: per-individual biomolecular indicators; expression + accessibility matrices with ENCODE-compatible annotations; cell type–specific marker/DEG catalogs; cell type–specific GRNs; and cell type–resolution eQTL/caQTL + SMR statistics.

### Comparisons with prior literature (made by authors)

- Among the 10 largest PBMC studies by cell count, most used single-cell transcriptomics alone or with genomics; CIMA adds scATAC-seq + WGS (refs 9, 14, 15, 79–85).
- Cross-validated cis-eQTLs against OneK1K (European, ref 14; 43.79% eGene overlap) and ImmuNexUT (East Asian, ref 5; 93.28% overlap).
- SMR methodology from Zhu et al. (refs 19, 20); GWAS resources (ref 21); circulating inflammatory protein GWAS (ref 53).
- Refined a prior whole-blood PADI2 eQTL (ref 66) to a monocyte-specific effect.

### Mechanistic hypotheses proposed

- "The T allele at rs34415530 reduced the expression of IKZF4 in CD4 Treg-FOXP3, potentially impairing their suppression of DC function and, in turn, possibly promoting IL-12B secretion" (p.9).
- "By modulating IKZF4 expression, the rs34415530 variant may induce Treg cell dysfunction, thereby contributing to an increased risk of asthma susceptibility" (p.9).
- "The A allele of rs2235922 enhances RA risk by up-regulating PADI2 in monocytes" (p.9).

### Caveats and self-criticism

- scRNA-seq and scATAC-seq came from separate cellular aliquots of the same blood sample (not the same cells), which "may have introduced complexity and minor inaccuracies in regulatory inference."
- Genome-wide xQTL mapping relied on pseudobulk for computational efficiency rather than single-cell models.
- The number of significant SMR associations is bounded by the number of significant GWAS loci (e.g. fewer for T1D than T2D).

### Future directions suggested

- Validation using true multiome (paired) platforms.
- More efficient single-cell QTL models for refined single-cell QTL analysis.

## Limitations

- Unpaired RNA/ATAC aliquots; integration bias mitigated but not eliminated.
- Pseudobulk QTL mapping; sample size per cell type bounds discovery power and apparent specificity.
- Common-variant focus (MAF > 0.1); rare-variant regulatory effects not assessed.
- Single Chinese cohort (95% Han); cross-ancestry transferability inferred, not directly tested in other cohorts.
- Mechanistic disease models (IKZF4, PADI2, SLC16A11) are SMR/literature-based, not experimentally validated here.

## Open questions

### Open questions raised by authors

- How to perform refined genome-wide single-cell (non-pseudobulk) QTL mapping efficiently.
- Whether true multiome platforms confirm the inferred enhancer-driven GRNs.

### Open questions identified during ingest

- How much does an ancestry-matched, cell type–resolved reference improve disease-risk portability versus European-centric resources?
- Can CIMA-CLM generalize to cell states and ancestries outside the training cohort, and are predicted variant-effect magnitudes calibrated to functional assays?
- Do dynamic (pseudotime) eQTLs explain disease loci missed by static cell-type mapping?

## My take

A landmark population-scale immune multi-omics resource. Its two durable contributions for this wiki are (1) the methodological template for cell type–resolved xQTL→SMR→GWAS integration and the strong empirical case that immune regulatory genetics is overwhelmingly cell type–specific, and (2) CIMA-CLM as a concrete multimodal foundation-model fusion (sequence + cell state) for regulatory genomics. The Chinese-cohort framing also makes a substantive ancestry-equity point. Most disease mechanisms are association-grade and await functional validation.

## Related

### Concepts
- [[concepts/cell-type-specific-genetic-regulation-immune]]
- [[concepts/cima-clm-chromatin-accessibility-cell-language]]
- [[concepts/enhancer-driven-gene-regulatory-network-eregulon]]
- [[concepts/ancestry-specific-immune-regulatory-variation]]
- [[concepts/dynamic-eqtl-along-differentiation-pseudotime]]

### Foundations (methods)
- [[foundations/summary-data-based-mendelian-randomization-smr]]
- [[foundations/multi-omics-factor-analysis-mofa]]
- [[foundations/tensorqtl]]
- [[foundations/hyenadna-genomic-sequence-model]]
- [[foundations/snapatac2-single-cell-atac-workflow]]
- [[foundations/scrna-seq-10x-chromium]]
- [[foundations/atac-seq]]
- [[foundations/glue-multiomics-integration]]
- [[foundations/scgpt-single-cell-foundation-model]]
- [[foundations/homer-motif-enrichment-analysis]]
- [[foundations/azimuth-reference-mapping]]
- [[foundations/celltypist]]

### Foundations (biological)
- [[foundations/ikzf4-eos-transcription-factor]]
- [[foundations/padi2-peptidylarginine-deiminase]]
- [[foundations/il-12b-interleukin-12b-subunit]]
- [[foundations/foxp3-tf]]
- [[foundations/cd14-receptor]]
- [[foundations/stat1-tf]]
- [[foundations/atf3-activating-transcription-factor]]

### People
- [[people/jianhua-yin]]
- [[people/yanan-cao]]
- [[people/xun-xu]]
- [[people/longqi-liu]]
- [[people/xin-jin]]
- [[people/chuanyu-liu]]
