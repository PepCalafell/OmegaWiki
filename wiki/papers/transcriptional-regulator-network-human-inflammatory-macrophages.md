---
# === Identification ===
title: "The transcriptional regulator network of human inflammatory macrophages is defined by open chromatin"
slug: "transcriptional-regulator-network-human-inflammatory-macrophages"
arxiv: ""
doi: "10.1038/cr.2016.1"
pmid: "26846308"
venue: "Cell Research"
year: 2016
authors:
  - Susanne V. Schmidt
  - Wolfgang Krebs
  - Thomas Ulas
  - Jia Xue
  - Kevin Baßler
  - Patrick Günther
  - Anna-Lena Hardt
  - Hartmut Schultze
  - Jil Sander
  - Kathrin Klee
  - Heidi Theis
  - Michael Kraut
  - Marc Beyer
  - Joachim L. Schultze
first_author: "Susanne V. Schmidt"
corresponding_author: "Joachim L. Schultze"

# === Source & metadata ===
source_type: pdf
s2_id: "ce21f14eb12300c77ae49e74b3f7ce5d78be579a"
date_added: 2026-06-03
ingested_date: 2026-06-03
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - macrophage
  - epigenetics
  - transcription-factors
  - chromatin
  - inflammation
  - network-biology
keywords:
  - inflammatory macrophages
  - open chromatin
  - transcriptional regulators
  - histone modifications
  - super-enhancers
  - PU.1
domain: "epigenetics"

# === Biomedical domain ===
tissue:
  - blood
  - in_vitro_only
  - multi
condition:
  - healthy
disease_specific: []
species:
  - human
  - mouse
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques:
  - ChIP-seq
  - bulk_RNA-seq
  - flow_cytometry
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types:
  - monocyte-derived macrophage
  - inflammatory macrophage
  - tissue-resident macrophage
key_markers:
  - PU.1
  - IRF1
  - STAT1
  - IRF4
  - STAT4
  - FOSL2
  - H3K4me3
  - H3K27ac
  - H3K4me1
  - H3K27me3
key_pathways:
  - macrophage activation
  - IFNγ signaling
  - IL-4 alternative activation
  - super-enhancer formation
  - transcriptional regulatory network

# === User project membership ===
projects:
  - thesis
priority: context
read_status: not_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "GEO: GSE36952, GSE66593, GSE66594, GSE16256, GSE63341, GSE47188, GSE63339"

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem
How is gene expression during human macrophage activation coordinated by epigenetic and transcriptional mechanisms? The general model holds that accessible chromatin predicts expression and repressive chromatin predicts silencing. Whether this integrated rule governs the *network of transcriptional/epigenetic regulators (TRs)* that drives inflammatory macrophage activation in humans had not been established.

## Key idea
By profiling four histone modifications during human macrophage activation and integrating them with transcriptomes from many activation conditions, the authors define a network of TRs whose promoters are **constitutively accessible regardless of activating signal**. Expression of these network TRs is nonetheless stimulus-specific — implying that inflammatory activation is gated transcriptionally on a pre-set open-chromatin landscape, in contrast to tissue/identity programs that are epigenetically integrated.

## Method
Monocytes purified from human peripheral blood were differentiated with GM-CSF into baseline macrophages (M_b) and activated for 72 h with IFNγ (M_IFNγ, acute inflammation), IL-4 (M_IL4, alternative), or TNF + PGE2 + Pam3Cys (M_TPP, chronic inflammation). Activation states were validated by surface markers (CD14/CD86/CD23/CD25). H3K4me1, H3K4me3, H3K27ac and H3K27me3 ChIP-seq defined five chromatin states (active/poised promoters Pa/Pp; strong/weak/poised enhancers Es/Ew/Ep). Motif enrichment (HOMER), super-enhancer calling (clustered H3K27ac), and TR-network construction were integrated with the Xue et al. 2014 multidimensional transcriptome resource. Human tissue (Roadmap, 5 tissues) and murine tissue-macrophage (Amit et al., 7 populations) datasets provided contrast networks.

## Results
- Common macrophage promoters are overwhelmingly accessible (7 427 Pa vs 1 247 Pp loci), with PU.1 motifs dominating common active promoters and strong enhancers.
- Activation reshapes the enhancer landscape in a stimulus-specific way (far more activation-specific enhancers than promoters); enhancer strength tracks expression (Es > Ew > Ep).
- Activation-specific elements are bound by signal-appropriate TFs (IRF1/MIFNγ, STAT6/MIL4, FOSL2/MTPP); a PU.1-independent subset resembles latent enhancers.
- Super-enhancers act in an activation-specific manner (up to 820/condition; 200 common).
- The macrophage activation TR network shows uniformly accessible promoters (>92% Pa) across all states, yet stimulus-specific TR expression — a second, transcriptional layer of control.
- TRs not expressed in any condition, CNS/random genes, and tissue networks instead show chromatin state tracking expression, making open-chromatin TR loci a macrophage-specific feature and defining a dichotomy between activation and identity programs.

## All claims (exhaustive)
- `[c1]` Common macrophage promoters are predominantly accessible across activation conditions `(p.153)` "A total of 7 427 common loci with histone marks matching the criteria of Pa … were observed while 1 247 loci … matched the HM characteristics for Pp" — confidence: high — type: quantitative — links: [[claims/common-macrophage-promoters-predominantly-accessible-across]] [[foundations/h3k4me3-histone-trimethylation-mark]] [[foundations/h3k27ac-histone-acetylation-mark]]
- `[c2]` PU.1 motif is enriched at common active promoters and strong enhancers `(p.155)` "PU.1 was the top expressed TF predicted to bind at common strong enhancers … the PU.1 motif was again highly enriched by bioinformatic prediction (P-value 1E−832)" — confidence: high — type: correlational — links: [[claims/pu-motif-enriched-common-active-promoters]] [[foundations/spi1-pu1-master-tf]] [[foundations/homer-motif-enrichment-analysis]]
- `[c3]` Macrophage activation hub genes are marked by active promoters not enhancers `(p.155)` "among the 869 most highly connected genes 94% were marked by a Pa but only 27% by an Es or Ew" — confidence: high — type: quantitative — links: [[claims/macrophage-activation-hub-genes-marked-active]] [[concepts/macrophage-activation-core-regulatory-hubs]]
- `[c4]` Macrophage activation induces stimulus-specific enhancer remodeling `(p.157)` "we identified more activation-specific strong (up to 763 Es in M_IFNγ), weak (from 2 855 Ew in M_TPP to 5 246 Ew in M_IL4) and poised enhancers … compared with promoters" — confidence: high — type: mechanistic — links: [[claims/macrophage-activation-induces-stimulus-specific-enhancer]] [[foundations/h3k4me1-histone-monomethylation-mark]]
- `[c5]` Strong enhancers associate with higher gene expression than weak or poised enhancers `(p.158)` "The highest average expression levels were observed for genes marked by strong enhancers followed by weak and poised enhancers for all macrophage activation states" — confidence: high — type: correlational — links: [[claims/strong-enhancers-associate-higher-gene-expression]] [[foundations/h3k27ac-histone-acetylation-mark]]
- `[c6]` Activation-specific regulatory elements are bound by stimulus-specific transcription factors `(p.158)` "TFs like IRF1 in M_IFNγ, STAT6 in M_IL4 and FOSL2 in M_TPP were predicted to bind to activation-specific accessible enhancers" — confidence: high — type: mechanistic — links: [[claims/activation-specific-regulatory-elements-bound-stimulus]] [[foundations/irf1]] [[foundations/stat1-tf]]
- `[c7]` A subset of activation-specific enhancers are PU.1-independent, resembling latent enhancers `(p.166)` "only a fraction of activation-specific sites bound PU.1. We presume that these sites are the human equivalent of what has been recently defined as latent enhancers in murine macrophages … and are not dependent on PU-1 binding" — confidence: medium — type: mechanistic — links: [[claims/subset-activation-specific-enhancers-pu-independent]] [[foundations/latent-enhancer]] [[foundations/spi1-pu1-master-tf]]
- `[c8]` Super-enhancers act in an activation-specific manner `(p.158)` "Up to 820 SEs were identified in each of the four different macrophage conditions … with 200 SEs common to all 4 macrophage conditions" — confidence: high — type: quantitative — links: [[claims/super-enhancers-act-activation-specific-manner]] [[foundations/super-enhancer]]
- `[c9]` The macrophage activation TR network has constitutively accessible promoters regardless of stimulus `(p.160)` "the large majority of the specific TRs showed accessible promoters (>92% …) in all investigated activation states" — confidence: high — type: mechanistic — links: [[claims/macrophage-activation-tr-network-constitutively-accessible]] [[concepts/open-chromatin-predefined-macrophage-activation-tr]]
- `[c10]` TR network gene expression is stimulus-specific despite uniform open chromatin `(p.160)` "M_IFNγ, M_IL4, and M_TPP were characterized by a distinct and specific pattern of differentially regulated TRs … while the patterns for accessible promoter and enhancer marks within the network were uniform" — confidence: high — type: mechanistic — links: [[claims/tr-network-gene-expression-stimulus-specific]] [[concepts/open-chromatin-predefined-macrophage-activation-tr]]
- `[c11]` Master regulators of human macrophage activation are stimulus-specific TFs `(p.161)` "Prominent examples of such TFs were STAT1 and IRF1 for M_IFNγ, IRF4 for M_IL4 and STAT4 and ETS2 for M_TPP" — confidence: medium — type: mechanistic — links: [[claims/master-regulators-human-macrophage-activation-stimulus]] [[foundations/stat1-tf]] [[foundations/irf4-transcription-factor]] [[foundations/stat4-transcription-factor]]
- `[c12]` Open chromatin at TR loci is specific to expressed network regulators `(p.160)` "When analyzing TRs not expressed in any of the 29 stimulation conditions only a minority showed accessible promoters (12%-15%) or strong enhancers (12%-17%)" — confidence: high — type: quantitative — links: [[claims/open-chromatin-tr-loci-specific-expressed]] [[concepts/open-chromatin-predefined-macrophage-activation-tr]]
- `[c13]` The open promoter landscape of the TR network is a macrophage-specific feature `(p.160)` "we assessed genes related to the central nervous system or randomly chosen genes, which both showed fewer accessible promoters … the accessibility of TR loci is a special feature of macrophages" — confidence: medium — type: correlational — links: [[claims/open-promoter-landscape-tr-network-macrophage]]
- `[c14]` Human tissue TR networks follow integrated epigenetic and transcriptional regulation `(p.162)` "expressed TRs being defined by accessible promoters, while TR genes not expressed were characterized by absence of accessible promoters" — confidence: high — type: mechanistic — links: [[claims/human-tissue-tr-networks-follow-integrated]] [[concepts/dichotomous-epigenetic-versus-transcriptional-regulation-tr]]
- `[c15]` Murine tissue-macrophage TR network is epigenetically and transcriptionally integrated `(p.162-166)` "we analyzed the data previously described by Amit et al. … developed the TR network of seven murine tissue macrophage populations … TRs not being expressed … lack the respective histone marks for permissive chromatin" — confidence: medium — type: mechanistic — links: [[claims/murine-tissue-macrophage-tr-network-epigenetically]] [[concepts/dichotomous-epigenetic-versus-transcriptional-regulation-tr]]
- `[c16]` Inflammatory macrophage activation is regulated transcriptionally by a pre-defined open-chromatin TR network `(p.151,166)` "these results support that macrophage activation during inflammation in contrast to lineage determination is mainly regulated transcriptionally by a pre-defined TR network" — confidence: high — type: mechanistic — links: [[claims/inflammatory-macrophage-activation-regulated-transcriptionally-pre]] [[concepts/open-chromatin-predefined-macrophage-activation-tr]] [[concepts/dichotomous-epigenetic-versus-transcriptional-regulation-tr]]

## Discussion captured

### Authors' interpretation
The authors interpret the open-chromatin TR network as an "exception to the rule": although inflammatory macrophages broadly follow the general integrated model (Figures 1–3), the activation TR network is pre-defined by open chromatin, so its output is governed solely by transcriptional control (input-specific master TRs). They postulate that the plasticity of macrophage activation observed in their earlier multidimensional model is a direct consequence of expression-dependent regulation within this specialized open network.

### Comparisons with prior literature (made by authors)
- Ostuni & Natoli — three-step hierarchical TR-network model and latent enhancers in murine macrophages (refs [15,16]).
- Xue et al. 2014 — their own multidimensional/spectrum model of human macrophage activation (ref [8]); hub genes reused here.
- Amit et al. — murine tissue-macrophage transcriptome/epigenome data used to build the contrast network (ref [27]).
- Roadmap Epigenomics consortium — human tissue RNA-seq/ChIP-seq (ref [41]).
- Whyte/Hnisz et al. — super-enhancer concept (refs [38,39]).

### Mechanistic hypotheses proposed
- Open TR loci are a prerequisite for rapid macrophage adaptation, with transcription (TF binding, co-regulators, ncRNAs) deciding output at already-open loci (p.161).
- PU.1-independent activation-specific enhancers are the human equivalent of murine latent enhancers (p.166).
- Other functionally plastic cell types may contain analogous cell-type-associated activation TR networks, whereas non-plastic cells regulate TRs epigenetically (p.164, Discussion).

### Caveats and self-criticism
- The exception "could be cell-type intrinsic for macrophages or might be associated with cell activation itself" (acknowledged uncertainty, p.166).
- Sufficient human tissue-macrophage epigenome data were not available, forcing reliance on murine data for the tissue-macrophage contrast.

### Future directions suggested
- Test whether M-CSF differentiation yields a comparable TR network.
- Acquire human tissue-macrophage epigenomic data to replace the murine surrogate.

## Limitations
- In-vitro, GM-CSF-differentiated, monocyte-derived macrophages only; no in-vivo human macrophage validation.
- Master regulators and TF occupancy are bioinformatic predictions (HOMER motifs), not ChIP-validated in this dataset.
- Tissue-macrophage contrast relies on murine reanalysis; some consortium datasets are n = 1.
- 72 h single timepoint; dynamics not captured.

## Open questions

### Open questions raised by authors
- Does M-CSF-driven differentiation produce a comparable open-chromatin TR network?
- Is the open-chromatin exception intrinsic to macrophage identity or to activation per se?

### Open questions identified during ingest
- What molecular machinery maintains constitutive promoter accessibility at network TR loci?
- Do human tissue-resident macrophages confirm the integrated (identity-type) regulation seen in mouse?
- Can the dichotomy be generalized to other plastic cell types (e.g. fibroblasts, T cells)?

## My take
A conceptually clean separation of two regulatory regimes: inducible activation networks gated transcriptionally on pre-opened chromatin versus identity networks gated epigenetically. The decoupling of accessibility from expression for regulator loci is the durable contribution and remains relevant to interpreting ATAC/ChIP data over TFs that do not track transcription. The reliance on motif prediction and murine surrogates tempers the strength of the mechanistic claims.

## Related
- Builds on [[transcriptome-based-network-analysis-reveals-spectrum]] (same lab; multidimensional/spectrum model and hub genes)
- Concepts: [[open-chromatin-predefined-macrophage-activation-tr]] · [[dichotomous-epigenetic-versus-transcriptional-regulation-tr]] · [[macrophage-activation-core-regulatory-hubs]] · [[spectrum-model-macrophage-activation]] · [[tpp-chronic-inflammation-macrophage-program]]
- Foundations: [[spi1-pu1-master-tf]] · [[chip-seq]] · [[homer-motif-enrichment-analysis]] · [[gm-csf-cytokine]] · [[h3k4me1-histone-monomethylation-mark]] · [[h3k4me3-histone-trimethylation-mark]] · [[h3k27ac-histone-acetylation-mark]] · [[h3k27me3-histone-trimethylation-mark]] · [[super-enhancer]] · [[latent-enhancer]] · [[irf1]] · [[stat1-tf]] · [[stat4-transcription-factor]] · [[irf4-transcription-factor]] · [[c-ebp-beta]]
