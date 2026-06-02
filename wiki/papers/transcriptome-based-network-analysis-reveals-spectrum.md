---
# === Identification ===
title: "Transcriptome-Based Network Analysis Reveals a Spectrum Model of Human Macrophage Activation"
slug: transcriptome-based-network-analysis-reveals-spectrum
arxiv: ""
doi: "10.1016/j.immuni.2014.01.006"
pmid: "24530056"
venue: "Immunity"
year: 2014
authors:
  - Jia Xue
  - Susanne V. Schmidt
  - Jil Sander
  - Astrid Draffehn
  - Wolfgang Krebs
  - Inga Quester
  - Dominic De Nardo
  - Trupti D. Gohel
  - Martina Emde
  - Lisa Schmidleithner
  - Hariharasudan Ganesan
  - Andrea Niño-Castro
  - Michael R. Mallmann
  - Larisa Labzin
  - Heidi Theis
  - Michael Kraut
  - Marc Beyer
  - Eicke Latz
  - Tom C. Freeman
  - Thomas Ulas
  - Joachim L. Schultze
first_author: "Jia Xue"
corresponding_author: "Joachim L. Schultze"

# === Source & metadata ===
source_type: pdf
s2_id: "28535d644612f0877a615c9b0d0b270e4f01310a"
date_added: 2026-06-02
ingested_date: 2026-06-02
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 5
tier: TIER_1
tags:
  - macrophage
  - activation
  - transcriptomics
  - network-analysis
  - immunology
  - WGCNA
keywords:
  - spectrum model
  - macrophage polarization
  - M1 M2
  - WGCNA
  - reverse network engineering
  - core macrophage signature
domain: immunology

# === Biomedical domain ===
tissue:
  - blood
  - lung
condition:
  - healthy
disease_specific:
  - COPD
species:
  - human
  - mouse
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques:
  - microarray
  - ChIP-seq
  - miRNA-seq
  - flow_cytometry
  - bulk_RNA-seq
n_samples: 384
n_cells_total:
integration_method:

# === Biology captured ===
key_cell_types:
  - monocyte-derived macrophages
  - alveolar macrophages
  - dendritic cells
  - monocytes
key_markers:
  - STAT1
  - STAT6
  - STAT4
  - NFKB1
  - JUNB
  - CREB1
  - HIF1A
  - PU.1
  - CD14
  - MERTK
key_pathways:
  - M1/M2 macrophage activation
  - chronic inflammation (TPP)
  - interferon signaling
  - NF-κB signaling

# === User project membership ===
projects:
  - thesis
priority: context
read_status: not_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "GSE47189"

# === Cross-references ===
code_url: ""
cited_by: [delineation-signaling-routes-underlie-differences-macrophage]
---

## Problem
Macrophage activation involves profound transcriptional reprogramming, but the classical M1-versus-M2 polarization model — two poles inspired by the Th1/Th2 dichotomy — fails to describe the broad transcriptional repertoire macrophages display in chronic inflammation, chronic infection, and cancer. No prior study had reconciled the many genomic observations of macrophage activation into an integrative model, and no large, standardised human macrophage activation resource existed.

## Key idea
Generate a large, highly standardised resource of human macrophage transcriptomes across diverse stimuli on a single platform, then apply network modeling to (1) extend M1/M2 to a multidimensional **spectrum model** of activation, (2) identify both stimulus-specific and activation-independent transcriptional regulators, (3) map in-vitro programs onto in-vivo tissue (alveolar) macrophages, and (4) refine a cross-species core macrophage signature using ImmGen murine data.

## Method
- **Resource:** 299 macrophage transcriptomes (29 conditions, 28 stimuli) from GM-CSF/M-CSF-derived human monocyte macrophages on Illumina BeadChips (384 arrays total); 9,498 genes expressed in ≥1 condition. Data: GSE47189.
- **Structure analysis:** coregulation analysis (CRA, BioLayout Express3D), SOM clustering, correlation coefficient matrices (CCM), 3D spectrum reconstruction (Mb = origin).
- **Module analysis:** [[foundations/wgcna-weighted-gene-coexpression]] → 49 modules; module eigengenes correlated to conditions; GO enrichment (BiNGO/EnrichmentMap), TF networks (Genomatix).
- **Functional validation of TPP:** flow cytometry, ELISA (CXCL5, IL-1α), allogeneic MLR / CFSE, miRNA-Seq, STAT4 immunoblot.
- **In-vivo mapping:** [[foundations/clusterprofiler-gsea]]-style GSEA of WGCNA modules on public alveolar macrophage cohorts (GSE13896, GSE2125; 39 nonsmokers, 49 smokers, 12 COPD).
- **Core network:** [[foundations/aracne-reverse-network-engineering]] (and TINGe) reverse engineering; PWM binding prediction; PU.1 / H3K4me3 ChIP-seq.
- **Cross-species core:** overlay of human orthologs onto [[foundations/immgen-immunological-genome-project]] murine macrophage/DC core signatures.

## Results
- A spectrum of ≥9 macrophage activation programs replaces the bipolar axis; non-canonical stimuli (fatty acids, HDL, TPP) drive off-axis states.
- WGCNA yields 49 condition-linked modules (M1=module 8, M2=module 15; TPP=30/32/33).
- TF hubs: STAT1 (IFN-γ), STAT6 (IL-4), STAT4 (TPP, novel in macrophages).
- TPP macrophages are phenotypically, secretomically, and functionally distinct (51 surface markers, CXCL5/IL-1α, T-cell suppression).
- COPD alveolar macrophages unexpectedly lose inflammatory signatures (depleted IFN-γ module 8).
- ARACNe network (66,744 interactions); core hub TFs JUNB, NFKB1, HIVEP1, CREB1, HBP1; PU.1/H3K4me3 enriched at hubs.
- A refined cross-species core signature + surface panel (CD14, CD32, MERTK, CD64, CD13) separates macrophages from DCs and monocytes.

## All claims (exhaustive)
- `[c01]` Macrophage activation forms a spectrum of ≥9 programs beyond M1/M2 (p.275) "Network modeling of this data set led us to extend the current M1 versus M2 polarization model to a 'spectrum model' with at least nine distinct macrophage activation programs" — confidence: high — type: mechanistic — links: [[claims/human-macrophage-activation-forms-spectrum-least]] [[concepts/spectrum-model-macrophage-activation]] [[concepts/m1-m2-polarization-paradigm]]
- `[c02]` Resource of 299 human macrophage transcriptomes across 28 stimuli (p.274) "we stimulated human macrophages with diverse activation signals, acquiring a data set of 299 macrophage transcriptomes" — confidence: high — type: methodological — links: [[claims/resource-299-human-macrophage-transcriptomes-across]]
- `[c03]` Non-polarizing stimuli reveal off-axis activation states (p.275) "when adding stimuli not linked to either M1 or M2 polarization, such as free fatty acids, high-density lipoprotein (HDL) ... a spectrum of macrophage-activation signatures beyond the initial bipolar axis became apparent" — confidence: high — type: correlational — links: [[claims/non-polarizing-stimuli-reveal-activation-states]] [[concepts/spectrum-model-macrophage-activation]]
- `[c04]` SOM clustering and CCM validate the spectrum model (p.275) "we did not identify a bipolar structure within the CCM, but rather a condition-specific spectrum of correlation coefficients in 10 major clusters" — confidence: high — type: methodological — links: [[claims/som-clustering-correlation-matrices-validate-macrophage]]
- `[c05]` Selective single marker genes per stimulus, but combinations usually needed (p.276) "IFN-β selectively induced ZNF77, while IFN-γ selectively induced FEM1C ... gene combinations are necessary to distinguish complex input signals" — confidence: medium — type: correlational — links: [[claims/single-selective-marker-genes-induced-specific]]
- `[c06]` WGCNA defines 49 coexpression modules linked to conditions (p.278) "We identified 49 distinct coexpression modules containing 27 to 884 genes per module" — confidence: high — type: methodological — links: [[claims/wgcna-defines-49-macrophage-coexpression-modules]] [[foundations/wgcna-weighted-gene-coexpression]]
- `[c07]` TPP induces modules absent in M1/M2 (p.278) "TNF, PGE2, and P3C (TPP, MTPP) induced a strong signal in modules 30, 32, and 33, which were not present in IFN-γ or IL-4 stimulated cells" — confidence: high — type: correlational — links: [[claims/tpp-stimulation-induces-macrophage-modules-absent]] [[concepts/tpp-chronic-inflammation-macrophage-program]]
- `[c08]` STAT1 and STAT6 are central hubs of IFN-γ and IL-4 networks (p.278) "revealed STAT1 as a central hub in the IFN-γ-condition and STAT6 as a hub in the IL-4-condition" — confidence: high — type: mechanistic — links: [[claims/stat1-stat6-central-hubs-ifn-gamma]] [[foundations/stat1-tf]] [[foundations/stat6-tf]]
- `[c09]` STAT4 is selectively induced in TPP macrophages (p.279) "STAT4 protein expression clearly confirmed that STAT4 is only induced in MTPP" — confidence: high — type: mechanistic — links: [[claims/stat4-selectively-induced-tpp-activated-macrophages]] [[foundations/stat4-transcription-factor]] [[concepts/tpp-chronic-inflammation-macrophage-program]]
- `[c10]` TPP macrophages express a distinct surface marker set (p.279) "A total of 51 cell surface markers were elevated in MTPP but not M1, M2, or Mb ... CD14, CD23, CD25, CXCR7, and CD197 on MTPP (p value < 0.05)" — confidence: high — type: quantitative — links: [[claims/tpp-macrophages-express-distinct-cell-surface]]
- `[c11]` TPP macrophages are functionally distinct and inhibit T cell proliferation (p.279) "MTPP showed a strong inhibitory effect, clearly demonstrating that macrophage activation by TPP induced an effector program distinct from M1 and M2" — confidence: high — type: correlational — links: [[claims/tpp-macrophages-functionally-distinct-inhibit-cell]]
- `[c12]` COPD alveolar macrophages lose inflammatory signatures (p.281) "In contrast to previous literature, we did not see an enrichment of IL-4-IL-13-associated signatures in COPD patients ... the most significantly depleted ... module in COPD patients was module 8 (linked to IFN-γ stimulation)" — confidence: medium — type: correlational — links: [[claims/copd-alveolar-macrophages-lose-inflammatory-gene]] [[foundations/tissue-resident-alveolar-macrophage]]
- `[c13]` ARACNe yields a dense macrophage interaction network (p.282) "We identified 66,744 interactions resulting in an average degree of connectivity of 14.7" — confidence: high — type: methodological — links: [[claims/aracne-reverse-engineering-yields-dense-macrophage]] [[foundations/aracne-reverse-network-engineering]]
- `[c14]` JUNB, NFKB1, CREB1 are common transcriptional denominators (p.283) "we ... generated a network of the top five TFs (JUNB, NFKB1, HIVEP1, CREB1, and HBP1)" — confidence: high — type: mechanistic — links: [[claims/junb-nfkb1-creb1-common-transcriptional-denominators]] [[concepts/macrophage-activation-core-regulatory-hubs]] [[foundations/nf-kb-p65-rela]] [[foundations/creb1-transcription-factor]]
- `[c15]` PU.1 binding and H3K4me3 enriched at hub gene loci (p.283) "a strong enrichment of PU.1 binding and permissive histone marks H3K4me3 at the loci of the 869 major hub genes" — confidence: high — type: correlational — links: [[claims/pu1-binding-h3k4me3-enriched-macrophage-hub]] [[foundations/spi1-pu1-master-tf]]
- `[c16]` A refined cross-species core macrophage signature distinguishes macrophages from DCs (p.284) "identified cell surface markers (CD14, FCGR2A [CD32], MERTK, FCGR1A [CD64], CD13 [ANPEP]) that distinguish human macrophages from both DCs and CD14+ blood monocytes" — confidence: high — type: mechanistic — links: [[claims/refined-cross-species-core-macrophage-signature]] [[concepts/cross-species-core-macrophage-signature]] [[foundations/immgen-immunological-genome-project]]

## Discussion captured

### Authors' interpretation
The authors interpret the data set as evidence that macrophages "integrate and compute signals from their local microenvironment," and that extending M1/M2 to a spectrum model "opens new avenues to study macrophage activation in the context of human diseases." Network-based, signal-specific transcriptional programming is proposed as a basis for linking defined activation programs to in-vivo human macrophage biology.

### Comparisons with prior literature (made by authors)
- M1/M2 framework: Biswas and Mantovani 2010; Chinetti-Gbaguidi and Staels 2011.
- ImmGen core signatures: Gautier et al. 2012; Miller et al. 2012.
- ARACNe / reverse network engineering: Margolin et al. 2006; Basso et al. 2005 (B cells); TINGe Aluru et al. 2013.
- WGCNA: Langfelder and Horvath 2008.
- COPD prior reports (IL-4/IL-13 enrichment): Shaykhiev et al. 2009 — explicitly contradicted by this study.
- COPD anti-inflammatory treatment inefficiency: Barnes 2013.

### Mechanistic hypotheses proposed
- Host factors TNF, PGE2, and TLR2-ligand jointly "shape the transcriptional program during chronic inflammation" (p.278).
- The loss of inflammatory signatures in COPD alveolar macrophages may "reflect clinical observations demonstrating inefficiency of anti-inflammatory treatment regimens in COPD" (p.284).

### Caveats and self-criticism
- Little is known about most of the highly interconnected hub genes (HIVEP1 and others) in macrophage activation — RNE reveals "unknown aspects."
- Saturated vs unsaturated fatty acids induce distinct responses (S.V.S., data not shown) — not fully developed here.
- Cross-species comparison needs same-tissue, in-vivo follow-up; some human-specific regulation will require non-animal methodology.

### Future directions suggested
- Link defined activation programs to in-vivo human macrophage biology.
- Compare macrophages from the same tissues across species in homeostasis and pathophysiology.
- Develop new mathematical models for signal integration and new therapeutic strategies targeting specific macrophage subsets.

## Limitations
- Built from in-vitro monocyte-derived macrophages on a single microarray platform; no tissue-resident ontogeny or single-cell resolution.
- Bulk transcriptomes average over cellular heterogeneity.
- Network edges (ARACNe/WGCNA) are associative, not causal.
- "At least nine" programs is data-set dependent.
- COPD/alveolar conclusions rely on re-analysis of two small public cohorts.

## Open questions

### Open questions raised by authors
- How are defined in-vitro activation programs realised in vivo in human tissue macrophages?
- What is the role of macrophage STAT4 and of unstudied hub TFs (e.g. HIVEP1) in activation?
- Why do COPD alveolar macrophages lose inflammatory signatures, and what are the therapeutic implications?

### Open questions identified during ingest
- How does the bulk spectrum model map onto modern single-cell macrophage taxonomies (MoMac-VERSE)?
- Can a quantitative scoring framework place arbitrary samples within the spectrum?

## My take
This is the seminal bulk-transcriptomic argument that macrophage activation is multidimensional — the historical hinge between [[concepts/m1-m2-polarization-paradigm]] and single-cell taxonomies. For thesis framing it is best cited as the origin of the [[concepts/spectrum-model-macrophage-activation]], the concrete TPP/STAT4 example of a non-M1/M2 program, and the identification of a shared activation backbone ([[concepts/macrophage-activation-core-regulatory-hubs]]).

## Related
- Concepts: [[concepts/spectrum-model-macrophage-activation]], [[concepts/tpp-chronic-inflammation-macrophage-program]], [[concepts/macrophage-activation-core-regulatory-hubs]], [[concepts/cross-species-core-macrophage-signature]], [[concepts/m1-m2-polarization-paradigm]]
- Foundations: [[foundations/wgcna-weighted-gene-coexpression]], [[foundations/aracne-reverse-network-engineering]], [[foundations/immgen-immunological-genome-project]], [[foundations/stat1-tf]], [[foundations/stat6-tf]], [[foundations/stat4-transcription-factor]], [[foundations/nf-kb-p65-rela]], [[foundations/creb1-transcription-factor]], [[foundations/spi1-pu1-master-tf]], [[foundations/tissue-resident-alveolar-macrophage]], [[foundations/clusterprofiler-gsea]]
- People: [[people/jia-xue]], [[people/joachim-schultze]], [[people/eicke-latz]], [[people/thomas-ulas]]
