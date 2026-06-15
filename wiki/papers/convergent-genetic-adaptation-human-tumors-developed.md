---
# === Identification ===
title: "Convergent Genetic Adaptation in Human Tumors Developed Under Systemic Hypoxia and in Populations Living at High Altitudes"
slug: convergent-genetic-adaptation-human-tumors-developed
arxiv: ""
doi: "10.1158/2159-8290.CD-24-0943"
pmid: "40199338"
venue: "Cancer Discovery"
year: 2025
authors:
  - Carlota Arenillas
  - Lucía Celada
  - José Ruiz-Cantador
  - Bruna Calsina
  - Debayan Datta
  - Eduardo García-Galea
  - Roberta Fasani
  - Ana Belén Moreno-Cárdenas
  - Juan José Alba-Linares
  - Berta Miranda-Barrio
  - Mario F. Fraga
  - Anne-Paule Gimenez-Roqueplo
  - Judith Favier
  - William F. Young Jr
  - Irina Bancos
  - Donate Weghorn
  - Mercedes Robledo
  - Igor Adameyko
  - María-Dolores Chiara
  - Patricia L.M. Dahia
  - Rodrigo A. Toledo
first_author: "Carlota Arenillas"
corresponding_author: "Rodrigo A. Toledo"

# === Source & metadata ===
source_type: pdf
s2_id: "9fb7c10df0e202cb735340e16f27a752b3b7b5d8"
date_added: 2026-06-15
ingested_date: 2026-06-15
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - hypoxia
  - EPAS1
  - HIF2A
  - PPGL
  - convergent-evolution
  - tumor-evolution
  - high-altitude
keywords:
  - EPAS1
  - HIF2alpha
  - COX4I2
  - pheochromocytoma
  - paraganglioma
  - cyanotic congenital heart disease
  - positive selection
  - microsatellite instability
domain: oncology

# === Biomedical domain ===
tissue: [multi]
condition: [cancer]
disease_specific: [pheochromocytoma_paraganglioma, cyanotic_congenital_heart_disease]
species: [both]
hypoxia_relevant: true
contains_immune_cells: false
contains_myeloid: false

# === Technique ===
techniques: [bulk_RNA-seq, scRNA-seq, WES, Sanger_sequencing, IHC, comet_assay, Seahorse, metabolomics, immunofluorescence, Western_blot]
n_samples: 34
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types:
  - chromaffin cells
  - adrenal medulla
  - sympathetic paraganglia
  - carotid body glomus cells
  - neural crest cells
key_markers:
  - EPAS1
  - HIF2A
  - COX4I2
  - VHL
  - PARP1
  - gamma-H2AX
  - MLH1
  - MSH2
  - MSH6
  - PMS2
  - fumarate
  - succinate
key_pathways:
  - HIF2alpha hypoxia signaling
  - oxidative phosphorylation / electron transport chain
  - DNA mismatch repair
  - TCA cycle / oncometabolites

# === User project membership ===
projects: [thesis, hypoxia]
priority: core
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: candidate
exclusion_reason:
data_availability: ""

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

PPGLs (pheochromocytomas/paragangliomas) arising in patients with chronic systemic hypoxia — e.g. cyanotic congenital heart disease (CCHD) — frequently carry somatic EPAS1 (HIF2α) gain-of-function mutations, but the mechanism, timing, and reason these mutations arise and are selected were unknown. The paper asks whether tumor evolution under systemic hypoxia parallels the genetic adaptation of human populations living at high altitude.

## Key idea

Human tumors developed under systemic hypoxia and human populations adapted to high-altitude hypoxia **converge on the same gene, EPAS1**, as the dominant target of positive selection (~90% prevalence in both). The convergence is on the gene, not the variant: high-altitude populations carry loss-of-function EPAS1 variants, whereas tumors carry gain-of-function ODD missense mutations. Mechanistically, EPAS1 gain-of-function induces COX4I2, slowing the electron transport chain to match oxygen consumption to a low oxygen supply — an adaptive advantage under hypoxia.

## Method

- Targeted Sanger sequencing and WES of a 34-tumor / 27-patient CCHD-PPGL cohort across five countries; comparison with TCGA and other PPGL cohorts.
- Somatic positive-selection inference (dN/dS), cancer cell fraction (CCF) clonality analysis.
- IHC for mismatch-repair proteins (MSI); WES-based MSI score, copy-number and TMB analysis.
- In-vitro DNA-damage assays (γH2AX, PARP1, comet assay) in PC12 PPGL-derived cells under hypoxia.
- Metabolomics (fumarate/succinate) in 141 PPGL tumors and a HIF2α-overexpressing MPC cell model.
- Bulk RNA-seq across three cohorts; Seahorse respirometry in EPAS1-GOF HEK293 cells; scRNA-seq of the neural-crest-to-chromaffin developmental trajectory.
- Curated clinical dataset of 2,588 patients from the CCHD-PPGL International Consortium.

## Results

EPAS1 mutations were present in 88.8% of sympathetic CCHD-PPGLs vs 4.5% in normoxic TCGA PPGL (20-fold; P<0.0001), exclusively in the oxygen-degradation domain, clonal/truncal (CCF≈0.99–1.0), absent in parasympathetic tumors, and nearly absent pan-cancer. EPAS1 was the only gene under strong positive selection (dN/dS=702). Hypoxic sympathetic tumors showed MSI/MMR loss and higher mutation burden; prolonged hypoxia damaged DNA and reduced PARP1 in PC12 cells. EPAS1 activation upregulated COX4I2 and reduced oxygen consumption. Clinical data revealed time- and tissue-dependent tumorigenesis (congenital hypoxia → sympathetic PPGL; later-onset → parasympathetic), lower SatO2 and lack of early surgical repair as risk factors, and greater aggressiveness/metastatic risk in CCHD-PPGL.

## All claims (exhaustive)

- `[c01]` EPAS1 somatic mutations in most sympathetic CCHD-PPGL `(p.1040)` "EPAS1 mutations in 24/27 sympathetic CCHD-PPGLs (88.8%)" — confidence: high — type: correlational — links: [[claims/epas1-somatic-mutations-most-sympathetic-cchd]] [[concepts/epas1-gain-function-oxygen-degradation-domain]] [[foundations/pheochromocytoma-paraganglioma-ppgl]]
- `[c02]` EPAS1 mutation frequency 20-fold higher in hypoxia `(p.1040)` "20-fold increase in EPAS1 mutation frequency in patients with hypoxia vs. normoxia (88.8% vs. 4.5%; P < 0.0001)" — confidence: high — type: quantitative — links: [[claims/epas1-mutation-frequency-20-fold-higher]] [[foundations/tcga-the-cancer-genome-atlas]]
- `[c03]` EPAS1 is the only gene under strong positive selection `(p.1040)` "EPAS1 was the only gene under statistically significant and strong positive selection ... dN/dS = 702 (q = 0)" — confidence: high — type: methodological — links: [[claims/epas1-only-gene-under-strong-positive]] [[foundations/dn-ds-positive-selection-inference]]
- `[c04]` EPAS1 mutations cluster in the oxygen-degradation domain `(p.1040)` "clustered within the oxygen-dependent degradation domain of HIF2α ... L529P, A530P/T/V, P531A/R/L/S, Y532C, and L542R/P" — confidence: high — type: mechanistic — links: [[claims/epas1-mutations-cluster-oxygen-dependent-degradation]] [[concepts/epas1-gain-function-oxygen-degradation-domain]] [[foundations/hif2a]] [[foundations/vhl-von-hippel-lindau]]
- `[c05]` EPAS1 mutations are clonal trunk events `(p.1040)` "EPAS1 mutations presented extremely high CCF levels in both cohorts (median of 1 and 0.99) ... the initial genetic events" — confidence: high — type: quantitative — links: [[claims/epas1-mutations-clonal-trunk-tumor-initiating]] [[foundations/cancer-cell-fraction-ccf]]
- `[c06]` EPAS1 mutations absent in parasympathetic carotid-body PPGL `(p.1040)` "no EPAS1 mutations in seven parasympathetic carotid body PPGLs ... 0/52 ... 0/214" — confidence: high — type: correlational — links: [[claims/epas1-mutations-absent-parasympathetic-carotid-body]] [[foundations/pheochromocytoma-paraganglioma-ppgl]]
- `[c07]` EPAS1 mutations near absent across other cancers `(p.1040)` "5/69,045 tumor samples, 0.007% ... and TCGA Pancancer Atlas Studies (0/10,775 ... 0%)" — confidence: high — type: quantitative — links: [[claims/epas1-somatic-mutations-near-absent-across]]
- `[c08]` EPAS1 prevalence parallels Tibetans/Sherpas `(p.1040)` "89% sympathetic PPGL tumors ... paralleling the 90% EPAS1 variant prevalence reported in Tibetans and Sherpas" — confidence: medium — type: correlational — links: [[claims/epas1-prevalence-cchd-ppgl-parallels-tibetan]] [[concepts/convergent-epas1-adaptation-high-altitude-populations]]
- `[c09]` Sympathetic CCHD-PPGL show MSI / MMR loss `(p.1042)` "7/9 (77%) tumors ... presented evidence of MSI ... expression loss of mismatch repair proteins, such as MLH1, MSH2, MSH6, and PMS2" — confidence: medium — type: correlational — links: [[claims/sympathetic-cchd-ppgl-tumors-show-microsatellite]] [[foundations/microsatellite-instability-msi]] [[concepts/hypoxia-inhibits-dna-repair-pathways-hr]]
- `[c10]` Higher mutation burden in hypoxic sympathetic PPGL `(p.1042)` "significantly higher average MSI genomic score ... and tumor mutation (average of 15 somatic mutations vs. 9 ... P = 0.02)" — confidence: medium — type: quantitative — links: [[claims/sympathetic-cchd-ppgl-tumors-higher-mutation]] [[concepts/hypoxia-induced-mutator-phenotype]]
- `[c11]` Prolonged hypoxia increases DNA damage, reduces PARP1 `(p.1042-1044)` "significant increase in γH2AX levels after prolonged hypoxia ... PARP1 levels progressively declined" — confidence: high — type: methodological — links: [[claims/prolonged-hypoxia-increases-dna-damage-reduces]] [[foundations/gamma-h2ax-dna-damage-marker]] [[foundations/comet-assay-single-cell-gel-electrophoresis]]
- `[c12]` EPAS1-mutant PPGL show elevated fumarate, reduced succinate `(p.1042-1045)` "EPAS1-mutated (and VHL-mutated) tumors exhibited significantly elevated fumarate levels alongside reduced succinate levels" — confidence: high — type: correlational — links: [[claims/epas1-mutated-ppgl-tumors-show-elevated]]
- `[c13]` EPAS1-HIF2α activation upregulates COX4I2 across cohorts `(p.1045)` "significant overexpression of two genes that encoded mitochondrial proteins: HMGCL ... and COX4I2" — confidence: high — type: methodological — links: [[claims/epas1-hif2alpha-activation-upregulates-cox4i2-across]] [[foundations/cox4i2-cytochrome-oxidase-subunit-isoform]]
- `[c14]` EPAS1 GOF induces COX4I2 and reduces oxygen consumption `(p.1045)` "HIF2α P405A/P531A ... induced COX4I2 expression displayed reduced oxygen consumption rate ... (P < 0.0001)" — confidence: high — type: mechanistic — links: [[claims/epas1-gain-function-induces-cox4i2-reduces]] [[concepts/cox4i2-isoform-switch-balances-oxygen-consumption]] [[foundations/seahorse-extracellular-flux-analyzer]]
- `[c15]` EPAS1/COX4I2 co-expressed in immature chromaffin cells, fetal-like in tumors `(p.1045)` "EPAS1 and COX4I2 expressions were correlated in an immature pre-birth chromaffin cell population ... significant resurgence ... suggesting a fetal-like transcriptional pattern" — confidence: medium — type: mechanistic — links: [[claims/epas1-cox4i2-co-expressed-immature-chromaffin]] [[concepts/developmental-time-window-systemic-hypoxia-tumorigenesis]] [[foundations/scrna-seq-10x-chromium]]
- `[c16]` Hypoxia since birth favors sympathetic PPGL `(p.1046-1047)` "56/66 (85%) patients with hypoxia since birth developed catecholamine-secreting PPGL ... [Eisenmenger] 7/11 (64%) parasympathetic carotid body tumors" — confidence: medium — type: correlational — links: [[claims/hypoxia-since-birth-favors-sympathetic-ppgl]] [[concepts/developmental-time-window-systemic-hypoxia-tumorigenesis]] [[foundations/cyanotic-congenital-heart-disease-cchd]]
- `[c17]` Lower SatO2 associates with PPGL development `(p.1046)` "lower SatO2 than patients with CCHD without PPGLs (average ... 81.2% ... vs ... 83.2% ...; P = 0.01)" — confidence: medium — type: quantitative — links: [[claims/lower-oxygen-saturation-associates-ppgl-development]]
- `[c18]` Early heart-repair surgery associates with reduced PPGL risk `(p.1047)` "1,204/1,368 (88%) ... without PPGL underwent early complete heart repair ... only 13/75 (17%) ... who developed PPGLs ... (P < 0.001)" — confidence: medium — type: correlational — links: [[claims/early-heart-repair-surgery-restoring-normoxia]]
- `[c19]` CCHD-PPGL is younger, multifocal, more metastatic `(p.1047)` "younger at ... diagnosis (OR = 0.92 ...), ... paragangliomas (OR = 9.98 ...), multiple ... (OR = 1.99 ...), ... metastatic disease (OR = 2.34 ... P = 0.018)" — confidence: high — type: quantitative — links: [[claims/cchd-ppgl-more-aggressive-younger-multiple]]
- `[c20]` Tibetan EPAS1 variants are loss-of-function, opposite to tumor mutations `(p.1050)` "Tibetans and Sherpas are enriched in noncoding variants ... with a loss-of-function effect ... tumors ... missense mutations ... gain-of-function and oncogenic effects" — confidence: high — type: mechanistic — links: [[claims/tibetan-epas1-high-altitude-variants-loss]] [[concepts/convergent-epas1-adaptation-high-altitude-populations]] [[foundations/erythropoietin-epo]]

## Discussion captured

### Authors' interpretation

The authors interpret EPAS1 as a fundamental driver of evolutionary adaptation to systemic hypoxia, shared between high-altitude populations and hypoxia-developed tumors. They describe several correspondences: accelerated adaptability (increased mutability), gene functional plasticity (LOF in populations vs GOF in tumors), and embryological/tissue-dependence of hypoxia stress. They propose that EPAS1 gain-of-function confers increased fitness to immature sympathetic chromaffin cells, favoring tumor development.

### Comparisons with prior literature (made by authors)

They build on prior reports of somatic EPAS1 gain-of-function in hypoxic-PPGL (refs 56–59), Fukuda et al. on the COX4I1→COX4I2 switch (ref 90), Denisovan introgression of the Tibetan EPAS1 haplotype (refs 36–38), and Kaelin/Ratcliffe's view of PPGL development via defective adrenal development and developmental apoptosis (refs 112, 113). They invoke Leigh-syndrome mouse models (Ndufs4-/-, SDHC-/-) where hypoxia improves survival (refs 119, 120).

### Mechanistic hypotheses proposed

Reduced ETC activity via COX4I2 matches oxygen consumption to supply, reducing toxicity of ETC/oxygen imbalance and giving a survival edge under hypoxia. Hypoxia-driven DNA-repair impairment (MSI, reduced PARP1, oncometabolite accumulation) generates the mutation pool from which EPAS1 variants are strongly selected.

### Caveats and self-criticism

Authors note the cause of the ~6-fold PPGL risk in CCHD "remains unknown," that the process restricting tumorigenesis to sympathetic tissues occurs "for unknown reasons," and that genetic status was not always confirmed in the extended clinical cohort (EPAS1-mutant status assumed for many CCHD sympathetic PPGLs).

### Future directions suggested

Investigate whether genes selected in populations adapted to high UV (melanoma) or to dietary/mineral scarcity drive corresponding cancers; pursue HIF2α inhibitors (belzutifan, DFF332) and PARP/temozolomide combinations for hypoxia-driven PPGL.

## Limitations

- Small functional/genomic cohorts (e.g. n=9 sympathetic CCHD-PPGL for WES/IHC).
- Mechanistic OCR/COX4I2 results from engineered cell lines; in-vivo tumor contribution inferred.
- Clinical associations (SatO2, surgical status) are observational and confounded by disease severity.
- Convergence thesis demonstrated for one gene in one tumor type.

## Open questions

### Open questions raised by authors

- Why is hypoxia-driven tumorigenesis restricted to sympathetic (adrenal medulla/paraganglia) tissues?
- What is the mechanistic basis of the ~6-fold PPGL risk in CCHD beyond EPAS1?
- Do other stressor-adaptation genes (UV, diet) drive their corresponding cancers?

### Open questions identified during ingest

- Is early surgical normoxia restoration causally protective, or is the association confounded?
- What links hypoxia/HIF2α activation to acquired mismatch-repair loss mechanistically?
- Are EPAS1 ODD alleles uniformly sensitive to HIF2α inhibitors?

## My take

A high-impact, conceptually novel paper bridging evolutionary population genetics and oncology. The quantitative 90%-vs-90% convergence and the LOF/GOF functional-plasticity twist are the memorable contributions; the COX4I2 oxygen-balancing mechanism is the satisfying functional explanation. Relevant to the thesis hypoxia work — both as a model of hypoxia-driven selection and for the DNA-repair/oncometabolite axis.

## Related

- [[concepts/convergent-epas1-adaptation-high-altitude-populations]]
- [[concepts/epas1-gain-function-oxygen-degradation-domain]]
- [[concepts/cox4i2-isoform-switch-balances-oxygen-consumption]]
- [[concepts/developmental-time-window-systemic-hypoxia-tumorigenesis]]
- [[concepts/hypoxia-induced-mutator-phenotype]]
- [[concepts/hypoxia-inhibits-dna-repair-pathways-hr]]
- [[concepts/pseudohypoxia-oncogene-induced-hif-activation]]
- [[concepts/ancestry-specific-tumor-hypoxia]]
- [[foundations/hif2a]]
- [[foundations/hif1a]]
- [[foundations/vhl-von-hippel-lindau]]
- [[foundations/arnt-hif1b]]
- [[foundations/erythropoietin-epo]]
- [[foundations/belzutifan-mk-6482]]
- [[foundations/cox4i2-cytochrome-oxidase-subunit-isoform]]
- [[foundations/pheochromocytoma-paraganglioma-ppgl]]
- [[foundations/cyanotic-congenital-heart-disease-cchd]]
- [[foundations/microsatellite-instability-msi]]
- [[foundations/comet-assay-single-cell-gel-electrophoresis]]
- [[foundations/dn-ds-positive-selection-inference]]
- [[foundations/cancer-cell-fraction-ccf]]
- [[foundations/gamma-h2ax-dna-damage-marker]]
- [[foundations/seahorse-extracellular-flux-analyzer]]
- [[foundations/scrna-seq-10x-chromium]]
- [[foundations/tcga-the-cancer-genome-atlas]]
- [[people/carlota-arenillas]]
- [[people/rodrigo-toledo]]
- [[people/patricia-dahia]]
