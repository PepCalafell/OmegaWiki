---
title: "Tumour hypoxia in driving genomic instability and tumour evolution"
slug: tumour-hypoxia-driving-genomic-instability-tumour
arxiv: ""
doi: "10.1038/s41568-024-00781-9"
pmid: "39875616"
venue: "Nature Reviews Cancer"
year: 2025
authors:
  - "Alexandru Suvac"
  - "Jack Ashton"
  - "Robert G. Bristow"
first_author: "Alexandru Suvac"
corresponding_author: "Robert G. Bristow"
source_type: tex
s2_id: "13edecae9b7bef7cd629efeb486e0288bd13530b"
date_added: 2026-05-13
ingested_date: 2026-05-13
ingest_version: 1
last_reviewed:
importance: 5
tier: TIER_1
tags:
  - hypoxia
  - genomic-instability
  - DNA-repair
  - tumour-evolution
  - clonal-evolution
  - CIN
  - aneuploidy
  - immune-evasion
  - metastasis
  - review
keywords:
  - tumour hypoxia
  - HIF1α
  - HIF2α
  - PERK-UPR
  - homologous recombination
  - mismatch repair
  - centrosome amplification
  - PCAWG
  - PGA
  - mutational signatures
  - clonal evolution
  - peri-necrotic
  - pseudohypoxia
domain: oncology
tissue:
  - multi
  - in_vitro_only
condition:
  - cancer
disease_specific:
  - prostate_cancer
  - hepatocellular_carcinoma
  - clear_cell_renal_cell_carcinoma
  - triple_negative_breast_cancer
  - head_and_neck_squamous_cell_carcinoma
species:
  - human
  - mouse
hypoxia_relevant: true
contains_immune_cells: true
contains_myeloid: true
techniques:
  - WGS
  - bulk_RNA-seq
  - mutational_signatures
  - spatial_transcriptomics
  - laser-capture_microdissection
  - cell-line_xenografts
  - immunohistochemistry
n_samples:
n_cells_total:
integration_method: ""
key_cell_types:
  - hypoxic tumour cells
  - MDSCs
  - TAMs
  - Tregs
  - exhausted CD8 T cells
key_markers:
  - HIF1A
  - HIF2A
  - VHL
  - PHD1
  - BRCA1
  - BRCA2
  - RAD51
  - MLH1
  - MSH2
  - MSH6
  - ATR
  - ATM
  - CHK1
  - CHK2
  - MRE11
  - RRM1
  - RRM2
  - PERK
  - eIF2alpha
  - ATF4
  - CA9
  - GLUT1
  - miR-210
  - PLK4
  - CDC20
  - BUB1
  - PLK1
  - KIF4A
  - AURKA
  - CEP192
  - TP53
  - PTEN
  - MYC
  - BCL2
  - KRAS
  - PD-L1
  - CD47
  - E-cadherin
  - SNAIL
  - TWIST
  - vimentin
  - JAGGED2
  - ONECUT2
  - MAFF
key_pathways:
  - HIF axis
  - PERK-UPR
  - HR repair
  - MMR repair
  - BER repair
  - ATR-CHK1 replication stress
  - ATM-CHK2 DSB response
  - ROS-ATM-MRE11 mutator axis
  - translesion synthesis
  - APOBEC mutagenesis
  - EMT
  - immune evasion (PD-L1/CD47, adenosine, lactate)
projects:
  - thesis
  - hypoxia
priority: core
read_status: read
hypoxiaverse_status: included
exclusion_reason:
data_availability: ""
code_url: ""
cited_by: []
---

## Problem

Why are hypoxic tumours so aggressive — radioresistant, chemoresistant, ICB-refractory, metastatic — across cancer types? The paper argues that hypoxia is not just a passive consequence of disorganized vasculature but an active **microenvironmental cofactor** that, alongside driver mutations in MYC, BCL2, TP53 and PTEN, generates and selects for unstable tumour clones. The framing problem: missing causal chain linking low pO2 to defective DNA repair, chromosomal instability (CIN), driver-gene-cooperating clonal evolution and immune escape — across both preclinical models and large-scale human WGS data.

## Key idea

Hypoxia generates genomic instability through two coupled axes:

1. **Hypoxia inhibits DNA repair** (HR via BRCA1/2/RAD51 suppression; MMR via HIF1α-dependent MLH1/MSH2/MSH6 silencing; BER via translational repression) and replication-fork stability (via RRM1/RRM2 inhibition → dNTP depletion → ATR-CHK1 activation; ROS–ATM–MRE11 axis degrading nascent DNA).
2. **Hypoxia rewires the mitotic machinery** (PLK4, PLK1, CDC20, BUB1, AURKA, miR-210), generating centrosome amplification, multipolar mitoses, lagging chromosomes and aneuploidy.

Mutator hypoxic cells then **survive and clonally expand** because: (a) co-existing driver mutations (TP53, PTEN, BCL2, MYC) provide apoptosis resistance under hypoxia; (b) hypoxic niches actively suppress immune surveillance via PD-L1/CD47 upregulation, MDSC/TAM/Treg recruitment, adenosine/lactate accumulation, type-I IFN inhibition and T-cell exhaustion. The result: peri-necrotic / hypoxic tumour centres seed polyclonal, aggressive, metastatic disease resistant to therapy.

## Method

Narrative review integrating: preclinical cell-line and xenograft hypoxic-stress experiments (chronic vs cycling hypoxia, isogenic competition assays for TP53/BCL2); large-scale human WGS analyses (PCAWG of 1,188 tumours across 27 cancer types; CIN signature work across 33 types); spatial-genomics studies (TRACERx Renal, HCC polyclonal-metastasis cohorts); mutational-signature analyses (SBS, ID, CN signatures); and mechanistic DDR / mitotic / immune-evasion molecular data.

## Results

- PCAWG: hypoxic tumours have elevated SNV/megabase, more chromosomal deletions/translocations/SVs, and elevated SBS6/ID6/SBS21/ID2 signatures (HRD/MMR-deficient) **in the absence of germline DDR mutations**.
- A positive correlation exists between hypoxia signatures and copy-number signature CN17 (HRD/aneuploidy) across 33 cancer types.
- Combined high hypoxia + high PGA produces a synergistic adverse prognosis in prostate cancer (biochemical relapse-free survival) and sarcoma (metastasis-free survival).
- Chronic hypoxia downregulates BRCA1/BRCA2/RAD51 and silences MLH1/MSH2/MSH6 (HIF1α-dependent).
- Cycling hypoxia drives APOBEC mutations correlating with hypoxia scores in patient tumours.
- Hypoxia induces low-fidelity TLS polymerases (HIF1-dependent), miR-210-driven centrosome amplification, and CDC20/BUB1/PLK1/KIF4A dysregulation in TNBC.
- TP53-null and BCL2-overexpressing cells outcompete WT under hypoxia (apoptosis evasion); PTEN loss × hypoxia produces polyclonal aggressive phenotypes in prostate.
- TRACERx Renal: aggressive subclonal growth localizes to peri-necrotic centres with elevated CNAs.
- HCC polyclonal metastases associate with HIF1α activation rather than discrete genomic alterations.
- Hypoxic tumours, despite elevated TMB/neoantigens, are refractory to ICB — explained by PD-L1/CD47 upregulation, MDSC/TAM/Treg recruitment, adenosine/lactate suppression, type-I IFN inhibition, T-cell exhaustion.

## All claims (exhaustive)

- `[c01]` Chronic hypoxia downregulates BRCA1/BRCA2/RAD51 (p.171, Box 2) "chronic, but not cycling, hypoxia results in transcriptional and translational downregulation of BRCA2 and RAD51, two fundamental homologous recombination (HR) repair proteins" — confidence: high — type: mechanistic — links: [[concepts/hypoxia-inhibits-dna-repair-pathways-hr]] [[foundations/brca1-tumor-suppressor]] [[foundations/brca2-tumor-suppressor]] [[foundations/rad51-recombinase]] [[claims/chronic-hypoxia-transcriptionally-translationally-downregulates-brca1]]
- `[c02]` Hypoxia HIF1α-dependently silences MMR core (p.171, Box 2) "hypoxia causes epigenetic silencing at promoter regions of key mismatch repair (MMR) genes, namely MutS homologue 2 (MSH2), MSH6 and MutL homologue 1 (MLH1) ... promotes an increase in frameshift mutations and microsatellite instability in a HIF1α-dependent manner" — confidence: high — type: mechanistic — links: [[concepts/hypoxia-inhibits-dna-repair-pathways-hr]] [[foundations/mlh1-msh2-mismatch-repair]] [[foundations/hif1a]] [[claims/hypoxia-hif1a-dependently-silences-mlh1-msh2]]
- `[c03]` PCAWG: high hypoxia tracks with HRD/MMR mutational signatures (p.171) "specific SBS and ID signatures in hypoxic tumours without DDR mutations were associated with defective HR (that is, SBS6 and ID6) or mismatch repair (MMR; that is, SBS6, SBS21 and ID2)" — confidence: high — type: correlational — links: [[foundations/pcawg-consortium]] [[concepts/hypoxia-inhibits-dna-repair-pathways-hr]] [[claims/pcawg-high-hypoxia-tracks-hrd-mmr]]
- `[c04]` Hypoxia correlates with copy-number signature CN17 (p.172) "a positive correlation between hypoxia and the copy number signature CN17, which is associated with HR deficiency (HRD) and with signatures of aneuploidy" — confidence: high — type: correlational — links: [[concepts/hypoxia-genomic-instability-pga]] [[claims/hypoxia-tracks-copy-number-signature-cn17]]
- `[c05]` Hypoxia inhibits RNR (RRM1/RRM2) → dNTP depletion → fork stalling (p.170) "DNA synthesis is stalled owing to impaired functioning of the enzyme ribonucleotide reductase (RNR; composed of ribonucleoside-diphosphate reductase subunit M1 (RRM1) and RRM2 dimers), which leads to reduced production of deoxynucleotide triphosphates during S phase" — confidence: high — type: mechanistic — links: [[foundations/ribonucleotide-reductase-rrm1-rrm2]] [[foundations/atr-kinase]] [[claims/hypoxia-inhibits-ribonucleotide-reductase-depleting-dntps]]
- `[c06]` Hypoxia HIF1-dependently induces low-fidelity TLS polymerases (p.170) "hypoxia was found to increase expression of low-fidelity translesion synthesis DNA polymerases in a HIF1-dependent manner, which leads to bypass of lesions at or before a DNA replication fork, enabling continued DNA replication with increasing mutation" — confidence: medium — type: mechanistic — links: [[concepts/hypoxia-induced-mutator-phenotype]] [[foundations/hif1a]] [[claims/hypoxia-hif1-dependently-induces-low-fidelity]]
- `[c07]` Cycling hypoxia correlates with APOBEC-mediated mutations in patient tumours (p.170) "Cycling hypoxia and replication stress can also induce accumulation of apolipoprotein B mRNA-editing enzyme and catalytic polypeptide-like (APOBEC)-mediated mutations ... the frequency of APOBEC-mediated mutations correlated with an elevated hypoxia signature score" — confidence: medium — type: correlational — links: [[foundations/apobec-mutagenesis]] [[concepts/hypoxia-induced-mutator-phenotype]] [[claims/cycling-hypoxia-correlates-apobec-mediated-mutations]]
- `[c08]` ROS–ATM–MRE11 degrades nascent DNA under hypoxia, forcing error-prone repair (p.170) "redox-sensitive activation of the ATM kinase and MRE11 nuclease, which degrades stalled replication forks in a homologous recombination (HR)-dependent manner. As hypoxia attenuates HR ... this attracts error-prone DNA polymerases leading to increased mutation rates" — confidence: high — type: mechanistic — links: [[foundations/atm-kinase]] [[concepts/hypoxia-induced-mutator-phenotype]] [[claims/ros-atm-mre11-complex-degrades-nascent]]
- `[c09]` High hypoxia + high PGA → synergistic adverse prognosis (p.171–172, Fig. 3a) "Tumours with elevated levels of hypoxia and an increased percent genome alteration (PGA) are associated with rapid relapse or decreased metastasis-free survival when compared to tumours that have only one or neither of these two features" — confidence: high — type: correlational — links: [[concepts/hypoxia-genomic-instability-pga]] [[claims/combination-high-hypoxia-high-pga-synergistically]]
- `[c10]` miR-210 induction under hypoxia drives centrosome amplification and multipolar spindles (p.173) "upregulation of the canonical hypoxia-associated microRNA, miR-210, can result in centrosome amplification accompanied by multipolar spindles and polyploid cells" — confidence: medium — type: mechanistic — links: [[concepts/hypoxia-centrosome-amplification-mitotic-cin]] [[foundations/mir-210-mirna]] [[claims/mir-210-induction-under-hypoxia-causes]]
- `[c11]` Hypoxia upregulates mitotic genes CDC20/BUB1/PLK1/KIF4A in TNBC, independent of CN/mutation (p.173) "hypoxia altered the expression of cell division cycle 20 (CDC20), BUB1, polo-like kinase 1 (PLK1) and KIF4A genes that are involved in anaphase onset, spindle assembly checkpoint (SAC) function, centrosome function and chromosome segregation. This effect was independent of gene copy number status or gene mutation" — confidence: medium — type: mechanistic — links: [[concepts/hypoxia-centrosome-amplification-mitotic-cin]] [[claims/hypoxia-upregulates-mitotic-genes-cdc20-bub1]]
- `[c12]` Cycling hypoxia HIF1α-dependently induces aberrant mitoses and aneuploidy (p.173) "increased multipolar mitotic cells, lagging chromosomes and DNA bridges have been observed in tumour cells placed under hypoxia ... cycling hypoxia might be responsible for inducing such centrosome aberrations with HIF1α-dependency" — confidence: medium — type: mechanistic — links: [[concepts/hypoxia-centrosome-amplification-mitotic-cin]] [[foundations/hif1a]] [[claims/cycling-hypoxia-hif1a-dependently-induces-aberrant]]
- `[c13]` TP53-null cells outcompete WT under hypoxia via reduced apoptosis (p.174) "tumour cells isogenic for TP53 ... or BCL2 ... cells with mutant genotypes were preferentially selected and outcompeted the wild-type cells under hypoxic conditions. Selection was attributed to decreased apoptosis under hypoxia" — confidence: high — type: mechanistic — links: [[concepts/hypoxia-co-driver-tumour-evolution-cancer]] [[foundations/tp53-tumor-suppressor]] [[claims/tp53-null-cells-outcompete-wild-type]]
- `[c14]` PTEN loss facilitates HIF1 and correlates with hypoxia-driven polyclonality and poor prognosis (p.174) "loss of PTEN facilitates HIF1-mediated gene expression and can contribute to tumour clone expansion through the deregulation of AKT activity ... the observed polyclonality of hypoxic tumour cells is associated with loss of PTEN copy number and gene expression and this correlates with poor prognosis" — confidence: high — type: correlational — links: [[concepts/hypoxia-co-driver-tumour-evolution-cancer]] [[foundations/pten-tumor-suppressor]] [[claims/pten-loss-facilitates-hif1-activity-correlates]]
- `[c15]` Hypoxic tumours are clinically refractory to ICB despite elevated TMB/neoantigens (p.174) "Although this would suggest that hypoxic tumours should be sensitive to immune checkpoint inhibition, accumulating evidence in the clinic suggests that the opposite is true as hypoxic tumours are usually refractory to immune checkpoint inhibition" — confidence: high — type: correlational — links: [[concepts/hypoxia-immune-evasion-clonal-selection]] [[claims/hypoxic-tumours-clinically-refractory-immune-checkpoint]]
- `[c16]` Hypoxia upregulates PD-L1 and CD47 in tumour cells (p.175) "upregulation of immune checkpoint molecules such as programmed cell death protein 1 ligand 1 (PDL1) and CD47" — confidence: high — type: mechanistic — links: [[concepts/hypoxia-pd-l1-tam-immune-evasion]] [[concepts/hypoxia-immune-evasion-clonal-selection]] [[claims/hypoxia-upregulates-immune-checkpoint-molecules-pd]]
- `[c17]` Hypoxia pretreatment increases experimental metastatic potential in vivo (p.175) "pre-treatment of tumour cells with hypoxia increases experimental metastatic potential leading to an increased ability to colonize the lung and other organs" — confidence: high — type: correlational — links: [[concepts/hypoxia-emt-lineage-plasticity-metastasis]] [[claims/hypoxia-pretreatment-increases-experimental-metastatic-potential]]
- `[c18]` Hypoxia coordinates EMT marker switch (E-cadherin↓; SNAIL/TWIST/N-cadherin/vimentin/JAGGED2↑) (p.175) "hypoxia can potentiate lineage plasticity and invasion phenotypes in the form of EMT by modulating the expression of EMT genes, including the downregulation of E-cadherin ... and increased expression of N-cadherin, SNAIL, vimentin, TWIST and JAGGED2" — confidence: high — type: mechanistic — links: [[concepts/hypoxia-emt-lineage-plasticity-metastasis]] [[claims/hypoxia-downregulates-cadherin-induces-snail-twist]]
- `[c19]` HCC polyclonal metastases associate with HIF1α transcriptional activation, not genomic alterations (p.177) "primary tumours that developed polyclonal metastases were not associated with genomic alterations but rather with transcriptional activation of hypoxia signalling and increased HIF1α staining" — confidence: medium — type: correlational — links: [[concepts/hypoxia-emt-lineage-plasticity-metastasis]] [[foundations/hif1a]] [[claims/hcc-polyclonal-metastases-associate-hif1a-transcriptional]]
- `[c20]` TRACERx Renal: aggressive subclonal growth in peri-necrotic centres with elevated CNAs (p.177) "aggressive subclonal growth occurred in the peri-necrotic tumour centre, and cells from within these regions had elevated somatic CNAs, proliferation rates and tumour grade" — confidence: high — type: correlational — links: [[concepts/tumor-subclonal-evolution-architecture]] [[concepts/hypoxia-emt-lineage-plasticity-metastasis]] [[claims/tracerx-renal-aggressive-subclonal-growth-occurs]]
- `[c21]` Hypoxia-associated mutations/CNAs are predominantly clonal/early (99% of PCa hypoxia-CNAs are early) (p.176) "in prostate cancer, of all of the copy number associations associated with hypoxia, 99% were altered early during tumour evolution" — confidence: high — type: correlational — links: [[concepts/tumor-subclonal-evolution-architecture]] [[concepts/hypoxia-co-driver-tumour-evolution-cancer]] [[claims/hypoxia-associated-mutations-cnas-predominantly-clonal]]
- `[c22]` Severe hypoxia activates PERK–eIF2α, arresting global translation (p.169–170, Box 1) "activated PERK phosphorylates eIF2A, leading to global translation inhibition ... ER stress-regulated translation increases tolerance to extreme hypoxia and promotes tumour growth" — confidence: high — type: mechanistic — links: [[foundations/perk-upr-pathway]] [[claims/severe-hypoxia-activates-perk-eif2a-arresting]]

## Discussion captured

### Authors' interpretation

The authors argue hypoxia is a **microenvironmental cofactor** — not a passive bystander — that cooperates with driver mutations (MYC, BCL2, TP53, PTEN) to drive clonal and subclonal evolution. They emphasize that hypoxia-induced "contextual" HR/MMR deficiency in tumours genotypically wild-type for DDR genes is conceptually disruptive: it means mutational signatures usually attributed to germline DDR loss can arise transiently from the microenvironment. They propose hypoxic subregions act as evolutionary incubators: low O2 generates instability, driver mutations enable survival, and the immune-protective niche shields nascent mutator clones from elimination.

### Comparisons with prior literature (made by authors)

- Bristow & Hill 2008 *Nat Rev Cancer* (canonical prior review): cited as conceptual ancestor of the "hypoxia → DNA repair deficit → genetic instability" axis.
- Bhandari et al. 2019 / 2020 *Nat Genet* / PCAWG: human-tumour validation of preclinical HR/MMR-deficiency observations.
- TRACERx Renal Consortium: spatial mapping confirming peri-necrotic aggressive subclonal growth.
- Multiple cell-line studies (HCT116 vs HeLa) on MMR suppression: cited to flag cell-line dependence.

### Mechanistic hypotheses proposed

- "Mutator cell selection" model: under chronic hypoxia, continued proliferation in DDR-compromised cells permits selection of mutator phenotypes (p.170).
- "Cycling acquisition" model: under cycling hypoxia, mutations are acquired during reoxygenation-driven replication restart with decreased repair capacity (p.170).
- Hypoxic tumour microenvironment "selects for unstable tumour clones which survive, propagate and metastasize under reduced immune surveillance" (abstract).

### Caveats and self-criticism

The authors are explicit: "These data pertaining to centrosome and mitotic gene expression are controversial, and we do not yet have direct evidence that hypoxia drives the amplification of centrosomes and postmitotic chromosomal mis-segregation" (p.174). The PHD1–CEP192 mechanism was proposed and then rebutted. NHEJ and NER effects of hypoxia "remain inconclusive". MMR suppression is cell-line dependent.

### Future directions suggested

- Live-cell-microscopy of cells isogenic for key mitotic regulators under hypoxia (cycling vs chronic).
- Spatial transcriptomics + single-cell centrosome imaging to validate in situ.
- Hypoxic cell fate-mapping in syngeneic mouse models varying immune competence.
- Isogenic systems decoupling HIF1 activity from O2 to disentangle pseudohypoxia vs true hypoxia.
- Hypoxia-targeting therapies combined with DDR-targeted or immune-modulating agents.

## Limitations

- Review (no new primary data) — relies on harmonization across heterogeneous models, tumour types and signature definitions.
- Bulk WGS dominates the human-tumour evidence; subclonal/spatial conclusions await single-cell and spatial-WGS validation.
- Centrosome/mitotic mechanism remains mechanistically unsettled; PHD1–CEP192 proposed and rebutted.
- NHEJ, NER and BER effects of hypoxia are pathway- and context-dependent and not yet consensus.
- Cell-line dependence (HCT116 vs HeLa) limits generalizability of MMR-suppression mechanisms.
- Pseudohypoxia confounder for any pure mRNA-signature-based hypoxia scoring.

## Open questions

### Open questions raised by authors

- Whether hypoxia "niches" with intratumoural genetic heterogeneity for specific mutations recapitulate the global hypoxia-CN association at sub-tumour scale.
- Whether the centrosome/mitotic effects of hypoxia are causal vs correlational.
- Whether reversing hypoxia in situ sensitizes hypoxic tumours to ICB.
- How to disentangle pseudohypoxic HIF1 activation from true low-O2 hypoxia in patient analyses.
- Whether hypoxic "creeping" cells in tumour niches are primed metastatic seeds.

### Open questions identified during ingest

- What quantitative pO2/duration thresholds switch the hypoxic response from adaptive to mutagenic?
- Can transient hypoxia-induced HRD be therapeutically weaponized (PARPi window) in non-BRCA-mutant tumours?
- Does targeting the ROS–ATM–MRE11 axis under cycling hypoxia abolish APOBEC mutagenesis?
- How do TAMs in hypoxic niches (cf. [[concepts/hypoxia-pd-l1-tam-immune-evasion]], [[concepts/tam-recruitment-hypoxic-niche-chemokines]]) mechanistically protect mutator clones — is the protection at the antigen-presentation, killing or trafficking step?

## My take

This is the canonical 2025 statement of the hypoxia-genomic-instability-evolution framework and the most important conceptual review in the HypoxiaVERSE thesis area. It cleanly stitches together the three legs of the argument — repair deficit, mitotic chaos, immune-protected expansion — at a level of mechanistic depth that prior reviews lacked. The PCAWG signature evidence is the load-bearing human-tumour observation; the TRACERx Renal peri-necrotic finding is the load-bearing spatial observation. For my work, this paper is the conceptual scaffold to anchor all other hypoxia ingests against. Two practical implications: (i) any biomarker analysis stratifying by hypoxia score MUST also stratify by DDR mutational signatures and driver-gene status to avoid confounding; (ii) the ICB-refractoriness mystery sits at the intersection of mutator phenotype + immune evasion and is the most clinically actionable gap.

## Related

- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — Bhandari 2019; the pancancer WGS empirical backbone that this review interprets and extends.
- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — complementary view of hypoxia-driven tumour-immune crosstalk.
- [[papers/pd-l1-expressing-tumor-associated-macrophages]] — TAM checkpoint axis underlying the hypoxic immune-evasion observations.
- [[concepts/hypoxia-genomic-instability-pga]], [[concepts/hypoxia-inhibits-dna-repair-pathways-hr]], [[concepts/hypoxia-induced-mutator-phenotype]], [[concepts/hypoxia-centrosome-amplification-mitotic-cin]], [[concepts/hypoxia-immune-evasion-clonal-selection]], [[concepts/hypoxia-emt-lineage-plasticity-metastasis]], [[concepts/hypoxia-co-driver-tumour-evolution-cancer]], [[concepts/pseudohypoxia-oncogene-induced-hif-activation]] — primary concept anchors.
- [[papers/hypoxia-signaling-human-health-diseases-implications]] — Luo et al. 2022 STTT comprehensive review of HIF cross-talk and disease landscape (added 2026-05-21).
