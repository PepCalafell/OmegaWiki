---
# === Identification ===
title: "Targeting STING to generate therapeutic anti-tumor immunity"
slug: targeting-sting-generate-therapeutic-anti-tumor
arxiv: ""
doi: "10.1016/j.ccell.2025.12.002"
pmid: "41448179"
venue: "Cancer Cell"
year: 2026
authors:
  - "Caroline G. Fahey"
  - "Anthony F. Cordova"
  - "Patrick C. Gedeon"
  - "David A. Barbie"
first_author: "Caroline G. Fahey"
corresponding_author: "David A. Barbie"

# === Source & metadata ===
source_type: pdf
s2_id: "d4c51bf66da39051779b7d96ca439ddd0ff0d453"
date_added: 2026-05-27
ingested_date: 2026-05-27
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - cgas-sting
  - innate-immunity
  - tumor-microenvironment
  - immunotherapy
  - type-i-interferon
  - review
  - epigenetic-silencing
  - trex1
  - enpp1
  - sting-agonist
  - innate-immune-checkpoint
keywords:
  - STING agonist
  - cGAS
  - cGAMP
  - TREX1
  - ENPP1
  - tumor microenvironment
  - vascular normalization
  - tertiary lymphoid structure
  - T cell cytotoxicity
  - NK cell
  - CAR-T
  - CAR-NK
  - antibody-drug conjugate
  - DMXAA
  - ADU-S100
  - diABZI
  - MPS1 inhibitor
  - EZH2 inhibitor
  - DNMT inhibitor
domain: "immunology"

# === Biomedical domain ===
tissue: [multi]
condition: [cancer]
disease_specific: []
species: [human, mouse]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [review]
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types:
  - tumor cell
  - dendritic cell
  - macrophage
  - CD8 T cell
  - CD4 T cell
  - NK cell
  - cancer-associated fibroblast
  - endothelial cell
key_markers:
  - STING (TMEM173)
  - cGAS (MB21D1)
  - TBK1
  - IRF3
  - NF-κB
  - TREX1
  - ENPP1
  - CXCL10
  - ICAM-1
  - VCAM-1
  - SELL
  - CCL5
  - IL-6
  - STAT3
  - MHC-I
  - MTAP
  - STK11/LKB1
  - MYC
  - mutant p53
  - IDH1
  - HER2
  - CCR2
key_pathways:
  - cGAS-STING-TBK1-IRF3 type I IFN
  - STING-IKK-NF-κB non-canonical
  - STING-autophagy
  - STING-induced apoptosis / ferroptosis / pyroptosis
  - STING-IL-6-STAT3 (CIN-high tumors)
  - EZH2/DNMT-mediated STING silencing
  - MerTK-P2X7R-cGAMP-STING (macrophages)
  - JAK-STAT vascular STING
  - SASP via cGAS-STING

# === User project membership ===
projects: [thesis]
priority: context
read_status: skimmed

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: excluded
exclusion_reason: "STING/cGAS in cancer immunology; not directly hypoxia-focused (some indirect overlap via SYNB1891 hypoxia-inducible promoter and TME oxygenation)"
data_availability: ""

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

After more than a decade of clinical investment, STING agonists — despite their potent activity in mouse syngeneic tumor models — have failed to deliver clinically meaningful antitumor activity in humans. No agent has progressed past Phase 2. The review asks: why has the translational gap been so wide, and what next-generation strategies can effectively harness cGAS-STING innate immunity for durable antitumor responses in patients?

## Key idea

The clinical failures of first-generation STING agonists reflect a fundamental mismatch between the field's old "STING ON = anti-tumor immunity" mental model and the actual biology, which is **highly context- and cell-type-dependent**. Across the TME, STING signaling produces qualitatively different outputs in tumor cells (often silenced or chronically pro-tumor via non-canonical NF-κB), myeloid cells (M1 polarization, antigen presentation, TLS formation), T cells (apoptosis and impaired proliferation — the central paradox), NK cells (resistant to cytotoxicity, robust antitumor), CAFs (CXCR3 chemokine production), and endothelial cells (vascular normalization, T/NK trafficking). Effective therapy must therefore (a) match the strategy to the tumor's STING status (epigenetically silenced vs intact), (b) target delivery to the productive cell types while sparing T cells, and (c) combine STING modulation with epigenetic priming, ICB, radiation, ADCs, or adoptive NK-cell therapy.

## Method

Narrative review by the Barbie lab synthesizing: (a) canonical and non-canonical cGAS-STING signaling biochemistry; (b) cell-type-specific TME outputs across six compartments; (c) clinical-stage STING agonists and ENPP1 inhibitors (Table 1, ~25 ongoing/terminated trials); (d) emerging classes — ADCs, hydrogel-sustained release, extracellular vesicles, ENPP1/TREX1 inhibitors, MPS1 inhibitors, EZH2/DNMT priming, CAR-NK combinations; (e) predictive biomarkers (Box 2 — cGAS/STING IHC, MTAP, STK11, MYC, IDH1).

## Results

Major synthesized findings (see ## All claims for atomic statements):

- STING TME outcomes are compartmentalized and divergent — the same agonist promotes antitumor immunity in DCs/ECs/NK while killing T cells and chronically activating pro-tumor non-canonical NF-κB in tumor cells.
- Tumors most commonly silence STING/cGAS epigenetically (DNMT/EZH2/KDM5) rather than by mutation — making "STING-cold" tumors a *druggable* class via epigenetic derepression.
- TREX1 and ENPP1 function as "innate immune checkpoints" that adaptively restrain endogenous STING-IFN — inhibitors of these regulators preserve tumor-autonomous cGAMP signaling.
- T-cell-intrinsic STING cytotoxicity is the dominant unaddressed barrier to CAR-T + STING combinations; NK cells (which express low intrinsic STING) are the structurally favored adoptive-cell partner.
- Endothelial STING drives vascular normalization, upregulates ICAM/VCAM/SELL, and converts cold tumors to T-cell-infiltrated TMEs.
- STING-induced TLS formation depends on host CD11c+ DC STING activation and may underlie durable adaptive responses to intratumoral STING agonism.
- Genomic biomarkers (MYC, STK11, MTAP, IDH1) predict STING-pathway responsiveness — but no current trial enriches for them.
- Next-generation strategies: HER2-STING ADC (XMT-2056), albumin-hitchhiking diABZI, hydrogel sustained release, ENPP1 inhibitors + radiation, TREX1 inhibitors + ICB, MPS1 pulsed inhibition + decitabine, EZH2 priming + ADC.

## All claims (exhaustive)

- `[c01]` STING activation outcomes in the TME are highly context- and cell-type-dependent (p.260) "STING activation elicits highly context- and cell type-dependent outcomes, with divergent effects on tumor cells, myeloid cells, T cells, and other cell types" — confidence: high — type: mechanistic — links: [[concepts/sting-tme-context-cell-type-dependent]] [[concepts/cgas-sting-pathway-canonical-noncanonical-outputs]] [[foundations/sting-stimulator-of-interferon-genes]] [[claims/sting-tme-outcomes-context-cell-type-dependent]]
- `[c02]` STING agonists show a major translational gap between mouse and human studies (p.260) "after nearly a decade of clinical testing, clinical efficacy has been underwhelming" — confidence: high — type: pharmacological — links: [[concepts/sting-agonist-clinical-translation-gap]] [[foundations/adu-s100-sting-agonist]] [[claims/sting-agonist-clinical-translational-gap]]
- `[c03]` DMXAA fully activates only murine STING and was the prototypical translational failure (p.260) "early murine and clinical studies utilizing the agent dimethylxanthenone acetic acid (DMXAA), which was later found to fully activate only murine STING" — confidence: high — type: pharmacological — links: [[foundations/dmxaa-vadimezan]] [[claims/dmxaa-activates-only-murine-sting]]
- `[c04]` Tumors most commonly silence cGAS/STING epigenetically via DNMT/EZH2/KDM5 rather than by mutation (p.263) "Instead of directly mutating cGAS or STING, cancer cells most often utilize epigenetic silencing to suppress pathway activity. Mechanistically, this occurs through DNA methylation and histone modifications" — confidence: high — type: mechanistic — links: [[concepts/epigenetic-cgas-sting-silencing-immune-evasion]] [[foundations/ezh2-histone-methyltransferase]] [[foundations/dnmt1-maintenance-methyltransferase]] [[claims/epigenetic-sting-silencing-many-cancers]]
- `[c05]` In CIN-high tumors, chronic cGAS-STING engages non-canonical NF-κB and IL-6/STAT3 to drive metastasis (p.265) "Chronic cytosolic dsDNA present in CIN-high cells favors the activation of the noncanonical NF-κB pathway in an STING-dependent and TBK1-independent manner... with STING and downstream noncanonical NF-κB activity mediating metastasis in a tumor cell-autonomous fashion" — confidence: high — type: mechanistic — links: [[concepts/chronic-sting-noncanonical-nfkb-cin]] [[foundations/nf-kb-p65-rela]] [[claims/cin-chronic-sting-nfkb-il6-drives-metastasis]]
- `[c06]` TREX1 functions as an adaptive innate immune checkpoint restraining STING-IFN in cancer cells (p.264) "TREX1 has also been increasingly recognized as playing a major role in restraining STING-IFN signaling in cancer cells, functioning as an 'innate immune checkpoint'" — confidence: high — type: mechanistic — links: [[concepts/trex1-innate-immune-checkpoint]] [[foundations/trex1-exonuclease]] [[claims/trex1-adaptive-innate-immune-checkpoint]]
- `[c07]` ENPP1 degrades extracellular cGAMP and drives breast cancer growth and metastasis (p.264) "ENPP1, the dominant hydrolase responsible for degrading extracellular cGAMP, has been shown to drive breast cancer tumor growth and metastasis by dampening extracellular cGAMP-STING-mediated anti-tumor immunity" — confidence: high — type: mechanistic — links: [[foundations/enpp1-cgamp-hydrolase]] [[concepts/tumor-derived-cgamp-immunotransmitter]] [[claims/enpp1-degrades-cgamp-drives-breast-cancer]]
- `[c08]` T cell-intrinsic STING signaling is cytotoxic and impairs proliferation, memory, and effector function (p.265) "robust STING activation is also cytotoxic to T cells... this phenotype has now been observed across species and therapeutic STING agonists tested in humans" — confidence: high — type: mechanistic — links: [[concepts/sting-tcell-intrinsic-cytotoxicity-paradox]] [[claims/sting-tcell-intrinsic-cytotoxicity]]
- `[c09]` Human NK cells are resistant to STING-induced cytotoxicity due to low intrinsic STING expression (p.266) "unlike T cells, human NK cells express low levels of intrinsic STING, resulting in a blunted IRF3 response, a potential mechanism explaining their relative resistance to STING agonist-induced cell death" — confidence: high — type: mechanistic — links: [[concepts/sting-nk-cell-tumor-clearance]] [[claims/nk-cells-resistant-to-sting-cytotoxicity]]
- `[c10]` EC STING activation drives vascular normalization and upregulates T/NK adhesion molecules (ICAM/VCAM/SELL) (p.267) "STING activation promotes vascular normalization, characterized by improved tumor blood vessel integrity and increased expression of vascular-stabilizing factors. Importantly, it also leads to the direct upregulation of T cell adhesion molecules such as ICAM, VCAM, and SELL" — confidence: high — type: mechanistic — links: [[concepts/sting-endothelial-vascular-normalization-trafficking]] [[claims/sting-ec-vascular-normalization-icam-vcam]]
- `[c11]` Host CD11c+ DC STING activation is required for tumor-associated TLS formation (p.265) "TLS formation is entirely dependent on host STING activation, particularly within CD11c+ dendritic cells" — confidence: high — type: mechanistic — links: [[concepts/sting-tls-formation-dc-dependent]] [[concepts/tertiary-lymphoid-structure]] [[claims/sting-cd11c-dc-tls-formation]]
- `[c12]` CAF STING activation produces CXCR3 chemokines (CXCL9/10/11) that recruit T cells (p.266) "in human malignant pleural mesothelioma tumor explants treated with STING agonists, the expression of CXCR3 chemokine ligands (CXCL9, CXCL10, and CXCL11) was particularly pronounced in CAFs relative to other TME cell types" — confidence: medium — type: mechanistic — links: [[foundations/cancer-associated-fibroblast]] [[claims/caf-sting-cxcr3-chemokines-tcell-recruitment]]
- `[c13]` Tumor cell STING is a cell-intrinsic suppressor of aerobic glycolysis via HK2 (p.266) "tumor cell STING has been shown to be a cell-intrinsic suppressor of glycolysis. Indeed, treating T cells with cGAMP impairs basal glycolysis and glycolytic capacity, preventing proliferation" — confidence: medium — type: mechanistic — links: [[claims/tumor-cell-sting-suppresses-glycolysis-hk2]]
- `[c14]` Pulsed MPS1 inhibition induces micronuclei + STING activation and synergizes with decitabine in KRAS-LKB1 lung cancer (p.272) "Pulsed MPS1 inhibition leads to robust micronuclei formation and STING pathway activation in human hepatocellular carcinoma and lung cancer cell lines, and synergizes with decitabine in murine models of lung cancer" — confidence: high — type: pharmacological — links: [[foundations/mps1-mitotic-checkpoint-kinase]] [[foundations/stk11-lkb1-tumor-suppressor]] [[claims/mps1-pulsed-inhibition-derepresses-sting-with-decitabine]]
- `[c15]` MTAP deficiency confers STING-agonist resistance by destabilizing IRF3 and co-deletion of 9p IFN genes (p.270) "MTAP deficiency was shown to confer resistance to STING agonists and DNA sensing by destabilizing downstream IRF3, and type I interferon genes themselves are often co-deleted with MTAP and CDKN2A on chromosome 9p" — confidence: medium — type: mechanistic — links: [[concepts/sting-biomarkers-precision-immunotherapy]] [[foundations/irf3-interferon-regulatory-factor-3]] [[claims/mtap-deletion-destabilizes-irf3-sting-resistance]]
- `[c16]` Mutant IDH1 inhibition restores dsDNA sensing by demethylating the cGAS promoter in low-grade glioma (p.270) "IDH1-mutant tumors inactivate the pathway upstream by hypermethylating the cGAS promoter" — confidence: high — type: pharmacological — links: [[foundations/cgas-cyclic-gmp-amp-synthase]] [[concepts/epigenetic-cgas-sting-silencing-immune-evasion]] [[claims/idh1-inhibition-restores-cgas-promoter-demethylation]]
- `[c17]` STING-agonist ADCs (XMT-2056 HER2; TAK-500 CCR2) reduce systemic cytokine release vs free agonist (p.270) "XMT-2056... showed antitumor activity in multiple murine tumor models and resulted in 10-fold lower induction of systemic cytokines compared to STING agonist alone" — confidence: high — type: pharmacological — links: [[concepts/sting-agonist-adc-targeted-delivery]] [[foundations/diabzi-amidobenzimidazole]] [[claims/sting-agonist-adc-her2-reduced-systemic-toxicity]]
- `[c18]` Tumor-derived cGAMP acts as an extracellular immunotransmitter, imported by TME cells via SLC19A1/SLC46A2/LRRC8 (p.260) "cGAMP signals intracellularly and also functions as an immunotransmitter that can be exported and imported into neighboring cells" — confidence: high — type: mechanistic — links: [[concepts/tumor-derived-cgamp-immunotransmitter]] [[foundations/cgamp-cyclic-dinucleotide]] [[claims/tumor-cgamp-immunotransmitter-paracrine-tme]]
- `[c19]` The curative effect of ionizing radiation requires an intact STING/cGAS pathway (p.271) "Ionizing radiation has been shown to increase cytosolic DNA by promoting errors in chromosome segregation and the formation of micronuclei, which in turn leads to cGAS activation... The curative effect of ionizing radiation requires an intact STING pathway" — confidence: high — type: mechanistic — links: [[claims/radiation-curative-effect-requires-sting-pathway]]
- `[c20]` EZH2 and DNMT inhibition reinvigorate STING and restore MHC-I antigen presentation in melanoma, TNBC, SCLC (p.263) "inhibitors targeting methyltransferases such as EZH2 and DNMT1 can reinvigorate the cGAS-STING pathway and prime tumor immunogenicity, thereby improving therapeutic benefit" — confidence: high — type: pharmacological — links: [[concepts/epigenetic-cgas-sting-silencing-immune-evasion]] [[foundations/ezh2-histone-methyltransferase]] [[claims/ezh2-dnmt-inhibition-restores-mhci-antigen-presentation]]
- `[c21]` Mutant p53 binds TBK1 and prevents STING-TBK1-IRF3 trimer formation (p.264) "mutant p53 has been reported to promote the evasion of tumor immune surveillance by directly inhibiting STING signaling through binding to TBK1, preventing the formation of trimeric TBK1-STING-IRF3 required for IRF3 phosphorylation and nuclear translocation" — confidence: medium — type: mechanistic — links: [[foundations/tp53-tumor-suppressor]] [[foundations/tbk1-tank-binding-kinase-1]] [[claims/mut-p53-binds-tbk1-prevents-sting-irf3-trimer]]
- `[c22]` In CIN-high TNBC, cGAS-STING-IL-6-STAT3 drives survival; tocilizumab + STING activation selectively impairs growth (p.265) "blockade of IL-6 signaling with tocilizumab, together with STING activation, selectively impairs the growth of triple-negative breast cancer cells" — confidence: high — type: pharmacological — links: [[concepts/chronic-sting-noncanonical-nfkb-cin]] [[claims/tnbc-cgas-sting-il6-stat3-tocilizumab-synergy]]
- `[c23]` MerTK blockade on TAMs enhances P2X7R-dependent STING activation by tumor-derived cGAMP (p.265) "Macrophages and monocytes have also been extensively linked to STING-mediated inflammation in cancer, responding to internalized DNA from phagocytosed cancer cells while also directly importing and responding to extracellular cGAMP" — confidence: medium — type: mechanistic — links: [[foundations/mertk-tam-receptors]] [[claims/mertk-blockade-enhances-macrophage-cgamp-sting]]
- `[c24]` MET-amplified EGFR-TKI-resistant lung cancer co-induces CD73 alongside STING, suppressing signaling via adenosine (p.264) "MET amplification, the most common mechanism of resistance to EGFR tyrosine kinase inhibitors in lung adenocarcinoma, co-induces the ectonucleosidase CD73 alongside tumor cell STING, metabolizing cGAMP and suppressing signaling indirectly via the generation of immunosuppressive adenosine" — confidence: medium — type: mechanistic — links: [[claims/met-cd73-adenosine-suppresses-sting-egfr-lung]]
- `[c25]` Staggered intratumoral STING agonist before CAR-T preserves T cell function and improves antitumor control (p.273) "intratumoral administration of the murine-specific agonist DMXAA or cGAMP can improve CAR T cell control of breast cancer models when the STING agonist is used prior to CAR T cell therapy" — confidence: medium — type: pharmacological — links: [[concepts/car-t-cell-therapy]] [[concepts/sting-tcell-intrinsic-cytotoxicity-paradox]] [[claims/staggered-sting-agonist-cart-preserves-tcell-function]]

## Discussion captured

### Authors' interpretation

The authors interpret the recurrent clinical failure of STING agonists as evidence that the field's mental model is wrong, not that STING is an invalid target. They argue: (a) STING TME outputs are inherently cell-type- and context-dependent, so monotherapy direct agonism is too blunt; (b) tumors silence STING through reversible epigenetic mechanisms more often than they mutate it, so "STING-cold" tumors should be epigenetically primed first; (c) T-cell-intrinsic cytotoxicity is the dominant unaddressed barrier and motivates NK-cell-centric combination strategies and cell-type-targeted delivery; (d) negative-regulator inhibitors (TREX1, ENPP1) "innate immune checkpoint" strategies leverage the tumor's own cGAMP rather than adding exogenous agonist; (e) the future is *combinatorial* — STING modulation + epigenetic priming + DNA-damaging therapy + ICB + adoptive cell therapy.

### Comparisons with prior literature (made by authors)

- Sun, Wu, Chen 2013 Science — cGAS discovery
- Ishikawa & Barber 2008 Nature — STING discovery
- Carozza, Bohnert, Li 2020 Nat Cancer — extracellular cGAMP as immunotransmitter
- Bakhoum 2018 Nature — CIN drives metastasis via STING-NF-κB
- Hong 2022 Nature — cGAS-STING-IL-6 in CIN cancers
- Kitajima 2019/2022 — KRAS-LKB1 lung cancer STING silencing and MPS1+decitabine derepression
- Tani 2024 Cancer Discov — TREX1 innate immune checkpoint
- Knelson 2022 Cancer Immunol Res — tumor STING priming for NK cell therapy
- Wang 2023 PNAS (Carozza/Li lab) — ENPP1 cGAMP hydrolase in breast cancer
- Mahadevan 2021 Cancer Discov — SCLC EZH2-mediated STING silencing

### Mechanistic hypotheses proposed

- Engineering STING-agonist-resistant CAR/TCR T cells as a route to combine STING agonism with adoptive T-cell therapy (p.273)
- CAR-NK + STING agonism as the more structurally sound adoptive-cell approach (p.273)
- Combination of EZH1/2 inhibition with deruxtecan-based ADCs as a way to spatially restrict DNA damage to tumor cells while sparing T cells (p.272)
- TREX1 inhibition selectively timed to avoid systemic autoimmunity but unleash radiation-induced cGAS-STING (p.271)

### Caveats and self-criticism

- Most mechanistic STING-TME data come from mouse syngeneic models that do not reflect autochthonous human tumor evolution and immune editing
- DMXAA failure illustrates the limit of murine-only mechanistic work
- TAK-500 (CCR2-STING ADC) Phase 1/2 termination shows that cell-type-targeted delivery alone is not sufficient — the targeted cell type must be productive
- No clinical trial currently enriches by tumor cGAS/STING expression
- CAF-STING biology is "underexplored, again in part related to a preponderance of work in mouse syngeneic tumor models"

### Future directions suggested

- ENPP1 inhibitors + radiation
- TREX1 inhibitors + ICB or DNA-damaging therapy
- HER2-STING and other antigen-targeted STING-ADCs
- EZH2/DNMT priming + downstream STING agonism in epigenetically silenced tumors
- MPS1 pulsed inhibition + decitabine in KRAS-LKB1 NSCLC
- CAR-NK + STING-agonist combinations
- IDH1 inhibition in low-grade glioma to restore cGAS demethylation
- Albumin-hitchhiking and bispecific (albumin/PD-L1) STING-nanobody platforms
- Engineered STING-agonist-resistant CAR-T cells
- Predictive biomarker development: cGAS/STING IHC, MTAP, STK11, MYC, IDH1 stratification

## Limitations

- Narrative review without systematic search criteria; potential selection bias toward Barbie-lab work (TREX1, KRAS-LKB1, PDOTS, MPS1)
- Heavy reliance on murine mechanistic data for most cell-type-specific STING outputs
- Table 1 clinical landscape current as of late 2025/early 2026; outcomes of several ongoing trials (CRD3874-SI, GSK3745417, TAK-676, XMT-2056) are immature
- CAF and EC STING biology described as "underexplored" — claims based on a small number of preclinical studies
- Authors acknowledge that several proposed combinations (TREX1 inhibitor + ICB, MPS1 + decitabine + STING agonist) lack human data

## Open questions

### Open questions raised by authors

- Whether systemically administered STING agonists (CRD3874-SI, GSK3745417, TAK-676) can succeed where intratumoral failed
- Whether STING agonists can be combined with adoptive T-cell therapies given T-cell-intrinsic cytotoxicity, or whether engineered STING-resistant T cells are required
- Whether STING-pathway-targeting therapies require predictive biomarker enrichment (cGAS/STING IHC) to show efficacy
- How human TAM, T cell, and EC STING biology differs from mouse models in the contexts most relevant to therapy
- Whether the CIN-STING-NF-κB-IL-6 axis can be reverted to canonical IRF3-IFN by dose/schedule modulation
- Whether ENPP1 and TREX1 inhibitors will translate to humans
- Whether CAR-NK + STING agonism becomes the dominant adoptive-cell platform for STING-targeted therapy

### Open questions identified during ingest

- How tumor hypoxia interacts with STING-IFN signaling — hypoxic regions favor SYNB1891-style activation but may also drive non-canonical NF-κB output (relevance to this wiki's hypoxia-TAM line)
- Whether STING-induced CXCL9 in CAFs and ECs converges on the same CXCL9⁺ TAM ICI biomarker axis described in [[papers/macrophages-targets-next-generation-cancer-immunotherapy]] and [[papers/trem2-macrophages-associated-enhanced-response-pd]]
- Whether epigenetic STING silencing in TAMs (vs only tumor cells) would alter the read of cGAS/STING IHC as a biomarker
- Whether MerTK blockade combined with cGAMP delivery represents an exploitable phagocytosis-checkpoint × STING combination, given the broader TAM efferocytosis program (Zhou 2020)

## My take

A high-leverage synthesis from the Barbie lab that converts a noisy decade of mostly-failed STING-agonist trials into an organized framework with concrete next-generation hypotheses. The most useful contributions for this wiki are: (a) the explicit "cell-type-dependent outputs across the TME" framing that mirrors the existing wiki narrative around TAM heterogeneity and TLS biology; (b) the "innate immune checkpoint" framing for TREX1 and ENPP1, which slots cleanly alongside the wiki's existing innate-immune-checkpoint-blockade concept and the LILRB2/B4/CLEVER-1 story from Sun/Merad 2026 ([[papers/macrophages-targets-next-generation-cancer-immunotherapy]]); (c) the predictive-biomarker landscape (Box 2) — MTAP, STK11, MYC, IDH1 — which gives concrete biomarker candidates for a thesis-grade precision-immunotherapy program; (d) the unsparing analysis of T-cell-intrinsic STING cytotoxicity as the binding constraint on CAR-T + STING combinations. The weakest part is the CAF/EC sections, which acknowledge their reliance on a small handful of preclinical studies. The review will pair well with the wiki's hypoxia and TAM literature: STING-IFN-driven vascular normalization (EC arm) interacts directly with hypoxic vessel dysfunction, and CIN-driven non-canonical NF-κB-IL-6 may operate alongside the HIF1α-NF-κB cooperative axis already documented in this wiki.

## Related

- [[concepts/cgas-sting-pathway-canonical-noncanonical-outputs]]
- [[concepts/sting-tme-context-cell-type-dependent]]
- [[concepts/epigenetic-cgas-sting-silencing-immune-evasion]]
- [[concepts/chronic-sting-noncanonical-nfkb-cin]]
- [[concepts/trex1-innate-immune-checkpoint]]
- [[concepts/sting-tcell-intrinsic-cytotoxicity-paradox]]
- [[concepts/sting-nk-cell-tumor-clearance]]
- [[concepts/sting-endothelial-vascular-normalization-trafficking]]
- [[concepts/sting-tls-formation-dc-dependent]]
- [[concepts/sting-agonist-clinical-translation-gap]]
- [[concepts/sting-agonist-adc-targeted-delivery]]
- [[concepts/sting-biomarkers-precision-immunotherapy]]
- [[concepts/tumor-derived-cgamp-immunotransmitter]]
- [[concepts/tertiary-lymphoid-structure]]
- [[concepts/innate-immune-checkpoint-blockade]]
- [[concepts/immune-checkpoint-blockade]]
- [[concepts/pattern-recognition-receptors-macrophage]]
- [[concepts/car-t-cell-therapy]]
- [[foundations/cgas-cyclic-gmp-amp-synthase]]
- [[foundations/sting-stimulator-of-interferon-genes]]
- [[foundations/cgamp-cyclic-dinucleotide]]
- [[foundations/tbk1-tank-binding-kinase-1]]
- [[foundations/irf3-interferon-regulatory-factor-3]]
- [[foundations/trex1-exonuclease]]
- [[foundations/enpp1-cgamp-hydrolase]]
- [[foundations/ezh2-histone-methyltransferase]]
- [[foundations/dmxaa-vadimezan]]
- [[foundations/adu-s100-sting-agonist]]
- [[foundations/diabzi-amidobenzimidazole]]
- [[foundations/mps1-mitotic-checkpoint-kinase]]
- [[foundations/stk11-lkb1-tumor-suppressor]]
- [[foundations/type-interferon-ifna-ifnb]]
- [[foundations/nf-kb-p65-rela]]
- [[foundations/mertk-tam-receptors]]
- [[foundations/cancer-associated-fibroblast]]
- [[foundations/tp53-tumor-suppressor]]
- [[papers/macrophages-targets-next-generation-cancer-immunotherapy]] — adjacent TAM-immunotherapy review with overlapping innate-checkpoint and CAR-T/NK framing
