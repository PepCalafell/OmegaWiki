---
# === Identification ===
title: "An integrative epigenome-based strategy for unbiased functional profiling of clinical kinase inhibitors"
slug: integrative-epigenome-based-strategy-unbiased-functional
arxiv: ""
doi: "10.1038/s44320-024-00040-x"
pmid: "38724853"
venue: "Molecular Systems Biology"
year: 2024
authors:
  - Francesco Gualdrini
  - Stefano Rizzieri
  - Sara Polletti
  - Francesco Pileri
  - Yinxiu Zhan
  - Alessandro Cuomo
  - Gioacchino Natoli
first_author: "Francesco Gualdrini"
corresponding_author: "Francesco Gualdrini; Gioacchino Natoli"

# === Source & metadata ===
source_type: pdf
s2_id: "018c4b90052f847d44d5ca85986dc0fe37a9278f"
date_added: 2026-06-03
ingested_date: 2026-06-03
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 3
tier: TIER_2
tags:
  - kinase-inhibitors
  - polypharmacology
  - H3K27ac
  - epigenomics
  - macrophages
  - inflammation
  - TLR4
  - IL-4
  - JAK-inhibitors
  - TBK1
  - IRF3
  - interferon
  - drug-repurposing
  - machine-learning
  - kinobeads
  - viral-mimicry
keywords:
  - clinical kinase inhibitors
  - chromatin modifications
  - Multiple Factor Analysis
  - macrophage activation
  - drug profiling
domain: "methods / immunology / epigenetics"

# === Biomedical domain ===
tissue: [in_vitro_only]
condition: [healthy]
disease_specific: []
species: [mouse, human]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [ChIP-seq, ATAC-seq, bulk_RNA-seq, flow_cytometry]
n_samples: 600
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types:
  - bone-marrow-derived macrophage (BMDM)
  - THP-1 macrophage-like cell
  - classical inflammatory macrophage
key_markers:
  - H3K27ac
  - Ifnb1
  - STAT1
  - IRF3
  - TBK1
  - NF-kB
  - STAT2
  - IRF1
key_pathways:
  - TLR4 signaling
  - IL-4R signaling
  - JAK-STAT
  - TBK1-IRF3
  - type I IFN

# === User project membership ===
projects: [thesis, methods]
priority: context
read_status: not_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "GEO: GSE219239 (H3K27ac ChIP-seq); ATAC-seq and RNA-seq datasets deposited in GEO; computer code available per the paper's Data availability statement."

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

More than 500 human kinases control nearly all cellular processes, and 80 clinical kinase inhibitors (CKIs) are approved with hundreds more in development. But CKIs are polypharmacological — they inhibit many kinases beyond the intended target — so their composite cellular effects (driving both efficacy and side effects) are only partially predictable from in-vitro selectivity profiling (kinase assays, kinobeads, phosphoproteomics). These binding/activity methods report what a drug *binds*, not the functional consequence in living cells. A complementary, high-content, interpretable functional readout was needed.

## Key idea

Use signal-induced changes in a dynamic chromatin modification — H3K27ac at cis-regulatory elements — as an unbiased, information-rich readout of the functional effects of CKIs on macrophage activation. Because kinases relay signals to transcription factors that shape enhancer acetylation, the genome-wide pattern of H3K27ac change a CKI induces fingerprints which signaling pathways and downstream TFs it actually perturbs in cells. See [[concepts/epigenome-based-functional-profiling-kinase-inhibitors]].

## Method

- 58 CKIs selected from kinobeads/CATDS data ([[foundations/kinobeads-chemoproteomic-selectivity-profiling]]; Klaeger et al. 2017), used at the kinobeads EC50 of the intended target, deliberately retaining target overlap/redundancy.
- Primary mouse [[foundations/bone-marrow-derived-macrophage-bmdm]] pre-treated 1 h with each CKI (or DMSO), then stimulated with LPS ([[foundations/lps-toll-like-receptor-signaling]]) or IL-4 ([[foundations/il4-cytokine]]) for 0/0.5/1/2/4 h.
- ~600 H3K27ac ([[foundations/h3k27ac-histone-acetylation-mark]]) [[foundations/chip-seq]] samples; CREs centered on [[foundations/atac-seq]]-defined accessible regions (~16,500 LPS- and ~5,000 IL-4-regulated CREs).
- [[foundations/multiple-factor-analysis]] deconvolves the 59-table dataset (58 CKIs + DMSO) into a compromise space; per-CRE perturbation likelihood derived from CKI-vs-DMSO distances; KNN network of CKI similarity.
- ~200 TF ChIP-seq datasets (34 TFs) + 58 per-CKI [[foundations/xgboost-gradient-boosting]] classifiers; interpreted with [[foundations/shap-feature-attribution]].
- Validation: RNA-seq ([[foundations/deseq2-differential-expression]]), p-STAT1 flow cytometry, [[foundations/cetsa-cellular-thermal-shift-assay]] for TBK1 engagement, transposable-element analysis, and human THP-1 confirmation.

## Results

CKIs perturbed H3K27ac at ~85% of LPS- and ~89% of IL-4-regulated CREs, predominantly downregulating signal-induced acetylation. CKIs with identical designated targets diverged sharply at the epigenome level; kinobeads target assignment improved (but did not fully explain) functional grouping. H3K27ac separated CKIs at higher resolution than RNA-seq. Per-CKI ML models predicted downregulatory effects via IRF/STAT and NF-κB/AP-1/IRF3 features. Case studies: the six JAK inhibitors each had unique spectra dominated by off-target activity; Momelotinib uniquely lowered Ifnb1 (via TBK1); several CKIs unexpectedly upregulated Ifnb1, linked to ERV/transposable-element induction (viral mimicry); Midostaurin suppressed Ifnb1 via TBK1 (CETSA-confirmed) and behaved like Momelotinib despite different designated targets. Effects translated to human THP-1 cells.

## All claims (exhaustive)

- `[c1]` H3K27ac + MFA is an unbiased functional readout of CKI effects on macrophages (p.629) "we devised an approach grounded on the use of histone acetylation and an integrated analytical pipeline" — confidence: high — type: methodological — links: [[concepts/epigenome-based-functional-profiling-kinase-inhibitors]] [[foundations/multiple-factor-analysis]] [[claims/h3k27ac-chip-seq-mfa-deconvolution-unbiased]]
- `[c2]` H3K27ac perturbed by ≥1 CKI at ~85% LPS / ~89% IL-4 CREs (p.630) "H3K27ac was perturbed by at least one CKI at ~85% of the LPS-regulated CREs and at ~89% of the IL-4-controlled CREs" — confidence: high — type: quantitative — links: [[foundations/h3k27ac-histone-acetylation-mark]] [[claims/h3k27ac-perturbed-least-one-cki-most]]
- `[c3]` CKIs with identical designated targets give divergent epigenomic effects (p.630) "CKIs with similar designated targets generated largely different effects at the epigenome level" — confidence: high — type: mechanistic — links: [[concepts/polypharmacology-clinical-kinase-inhibitors]] [[concepts/discordance-between-vitro-kinase-inhibitor-selectivity]] [[claims/ckis-identical-designated-targets-produce-divergent]]
- `[c4]` H3K27ac captures CKI similarity at higher resolution than RNA-seq (p.632) "H3K27ac changes can capture similarities among CKIs with higher resolution than transcriptional data" — confidence: medium — type: methodological — links: [[concepts/h3k27ac-functional-readout-signaling-perturbation]] [[claims/h3k27ac-captures-cki-functional-similarity-higher]]
- `[c5]` Kinobeads assignment improves selectivity profiling but effects reflect on+off-target combinations (p.631) "kinobeads assays significantly improve specificity profiling of CKIs compared to the annotations reported in clinical labels" — confidence: high — type: correlational — links: [[foundations/kinobeads-chemoproteomic-selectivity-profiling]] [[claims/kinobeads-target-assignment-improves-cki-selectivity]]
- `[c6]` Per-CKI XGBoost predicts downregulatory H3K27ac better than upregulatory; SHAP shows IRF/STAT vs NF-κB/AP-1/IRF3 (p.635) "we trained 58 independent supervised classification models ... models performed better at predicting down-regulatory than up-regulatory effects" — confidence: medium — type: methodological — links: [[foundations/xgboost-gradient-boosting]] [[foundations/shap-feature-attribution]] [[claims/per-cki-xgboost-classifiers-predict-downregulatory]]
- `[c7]` Each JAK inhibitor induces a unique spectrum dominated by off-target activity (p.638) "each JAKi induced highly specific epigenomic and transcriptional effects ... off-target effects played a prominent role" — confidence: high — type: mechanistic — links: [[foundations/tyk2-kinase]] [[foundations/jak2-kinase]] [[claims/each-jak-inhibitor-induces-unique-spectrum]]
- `[c8]` Only Filgotinib and Momelotinib reduce LPS-induced p-STAT1 at kinobeads EC50 (p.637) "only Filgotinib and Momelotinib caused a clear and significant reduction in p-STAT1 ... At a 4-fold higher concentration we observed inhibitory effects for all" — confidence: high — type: pharmacological — links: [[foundations/filgotinib]] [[foundations/momelotinib]] [[foundations/stat1-tf]] [[claims/only-filgotinib-momelotinib-reduce-lps-induced]]
- `[c9]` Filgotinib and Tofacitinib inhibit IFN signaling despite no kinobeads JAK binding (p.635) "Filgotinib, Tofacitinib, and BMS-911543 were not found to be associated with JAKs ... yet it was not reported to bind any JAK family member" — confidence: medium — type: pharmacological — links: [[concepts/discordance-between-vitro-kinase-inhibitor-selectivity]] [[foundations/filgotinib]] [[claims/filgotinib-tofacitinib-inhibit-ifn-signaling-despite]]
- `[c10]` Momelotinib uniquely reduces Ifnb1 among JAKi via TBK1 (p.637) "Momelotinib was the only one able to reduce Ifnb1 gene expression ... Momelotinib was found to bind also to TBK1" — confidence: high — type: mechanistic — links: [[foundations/momelotinib]] [[foundations/tbk1-tank-binding-kinase-1]] [[claims/momelotinib-uniquely-reduces-ifnb1-expression-among]]
- `[c11]` Several CKIs unexpectedly upregulate Ifnb1, some via IRF3-bound CRE hyperactivation (p.638) "several inhibitors led to the upregulation of Ifnb1 ... IRF3 was found to bind CREs at which H3K27ac was induced by BGT-226, Lapatinib and Tofacitinib" — confidence: high — type: pharmacological — links: [[foundations/irf3-interferon-regulatory-factor-3]] [[foundations/type-interferon-ifna-ifnb]] [[claims/several-ckis-unexpectedly-upregulate-ifnb1-gene]]
- `[c12]` Ifnb1-upregulating CKIs induce transposable elements (ERVs), suggesting viral mimicry (p.638) "Treatment of mouse macrophages with any of the seven inhibitors resulted in the induction of numerous TEs ... and in particular ERVs, which can generate double-stranded RNAs" — confidence: low — type: mechanistic — links: [[foundations/endogenous-retrovirus-viral-mimicry]] [[concepts/cki-induced-retroelement-activation-drives-interferon]] [[claims/ckis-upregulate-ifnb1-induce-transposable-element]]
- `[c13]` Midostaurin inhibits Ifnb1 via TBK1, confirmed by CETSA (p.641) "Midostaurin was able to increase TBK1 thermal stability at the EC50 for TBK1" — confidence: high — type: mechanistic — links: [[foundations/midostaurin]] [[foundations/tbk1-tank-binding-kinase-1]] [[foundations/cetsa-cellular-thermal-shift-assay]] [[claims/midostaurin-inhibits-ifnb1-induction-binding-stabilizing]]
- `[c14]` Midostaurin and Momelotinib produce near-identical epigenomic effects via TBK1/IKBKE paralogs (p.638) "their effects on H3K27ac were extremely similar and no obvious specificities for subsets of CREs were observed" — confidence: high — type: mechanistic — links: [[foundations/ikbke-ikk-epsilon-kinase]] [[foundations/tbk1-tank-binding-kinase-1]] [[claims/midostaurin-momelotinib-produce-near-identical-epigenomic]]
- `[c15]` CKI effects on IFNB1 translate to human THP-1 cells (p.642) "Midostaurin significantly reduced IFNB1 gene expression after both LPS and dsDNA stimulation ... Filgotinib did not reduce IFNB1 gene expression at any concentration" — confidence: medium — type: methodological — links: [[foundations/filgotinib]] [[foundations/midostaurin]] [[claims/cki-effects-ifnb1-induction-translate-mouse]]

## Discussion captured

### Authors' interpretation

The authors argue that an epigenome-centered approach provides far higher granularity and resolution than gene-expression profiling because it measures many more individual elements (promoters/enhancers ≫ genes) in dynamic conditions and excludes confounders such as RNA stability and post-transcriptional regulation. Combined with knowledge of CRE "grammar" (TF binding motifs), this enabled machine-learning identification of CKI similarities based on the terminal effectors (TFs) each CKI regulates in a given signaling context. They emphasize that off-target effects generally exceeded those assignable to the intended target — to the point that each molecule's effect spectrum was unique.

### Comparisons with prior literature (made by authors)

- Kinobeads/CATDS selectivity framework — Bantscheff et al. 2007; Klaeger et al. 2017 (Science).
- Clinical CKIs no more selective than preclinical compounds — Klaeger et al. 2017.
- Phosphoproteomics maps of CKI responses — Lee et al. 2024; signaling-network reconstruction — Hijazi et al. 2020.
- Thermal-stability/CETSA complexity — Seashore-Ludlow et al. 2020; Martinez Molina et al. 2013.
- Trametinib-induced retroelement activation and IFNB1 in pancreatic cancer — Cortesi et al. 2024.
- MFA methodology — Abdi et al. 2013; Escofier and Pagès 2008.

### Mechanistic hypotheses proposed

- "the increased induction of the Ifnb1 gene by these CKIs may relate to TBK1 hyper-activation" (BGT-226, Lapatinib, Tofacitinib) (p.638).
- "deregulated expression [of repeat elements] may underlie Ifnb1 induction in response to specific CKIs" (viral mimicry) (p.639).
- Momelotinib's STAT1 effect attributed to "both direct effects on JAKs and to reduced Ifnb1 expression caused by TBK1 inhibition" (p.637).

### Caveats and self-criticism

- "we cannot fully disentangle which combination of inhibited kinases leads to a set of H3K27ac changes ... we can only correlate H3K27ac alterations with sets of TFs but not directly link specific kinases to TFs" (p.635).
- "the CKI space we explored was somehow limited" — more inhibitors/kinases would refine the analysis (p.642).
- The TE analysis "does not pinpoint the specific mediators responsible for the upregulation of the repeat elements" (p.639).
- Reliance on a single kinobeads dataset can introduce measurement bias; kinobeads cover only ~253/518 kinases.

### Future directions suggested

- Expand epigenomic datasets across more CKIs, cell types, and signaling contexts; integrate with preclinical/clinical efficacy and side-effect data to predict clinical outcomes and prioritize molecules for trials.
- Combine with genetic approaches (measuring CKI effects upon ablation of the intended target) to separate on- vs off-target effects.

## Limitations

- Correlative: cannot directly assign inhibited kinases to specific TFs/H3K27ac changes.
- Restricted to mouse BMDM with two stimuli (plus THP-1 validation); generalization untested.
- CKIs used at kinobeads EC50, an indirect potency measure that may differ from cell-based EC50.
- Not suitable for primary high-throughput library screening.
- Partial kinome coverage of kinobeads underlies binding-vs-function discordances.

## Open questions

### Open questions raised by authors

- Can the approach, expanded across cell types/contexts and integrated with clinical data, predict clinical outcomes of CKIs?
- Which specific repeat elements and mediators drive CKI-induced Ifnb1 upregulation?

### Open questions identified during ingest

- How well does the H3K27ac resolution advantage over RNA-seq hold across timepoints and slower-kinetic systems?
- Could a functional epigenomic readout be used to re-annotate CKI targets beyond binding assays?
- Is dsRNA sensing (RIG-I/MDA5) required for the proposed viral-mimicry Ifnb1 induction?

## My take

A methodologically inventive paper from the [[people/gioacchino-natoli]] lab (first/co-corresponding author [[people/francesco-gualdrini]]) that reframes the macrophage epigenome as a polypharmacology sensor. The strongest contributions are conceptual: H3K27ac as a higher-resolution functional readout than the transcriptome, and the demonstration that off-target effects dominate the cellular action of CKIs even at sub-inhibitory doses. Highly relevant to macrophage/inflammation epigenetics work — the same enhancer/TF-occupancy machinery used here for drug profiling is the substrate of signal-dependent macrophage activation. The TBK1/IKBKE and viral-mimicry case studies are elegant but the TE mechanism remains correlative.

## Related

- Concepts introduced: [[concepts/epigenome-based-functional-profiling-kinase-inhibitors]], [[concepts/polypharmacology-clinical-kinase-inhibitors]], [[concepts/h3k27ac-functional-readout-signaling-perturbation]], [[concepts/discordance-between-vitro-kinase-inhibitor-selectivity]], [[concepts/cki-induced-retroelement-activation-drives-interferon]], [[concepts/drug-repurposing-kinase-inhibitors-control-inflammation]]
- Method foundations: [[foundations/multiple-factor-analysis]], [[foundations/kinobeads-chemoproteomic-selectivity-profiling]], [[foundations/xgboost-gradient-boosting]], [[foundations/shap-feature-attribution]], [[foundations/cetsa-cellular-thermal-shift-assay]], [[foundations/h3k27ac-histone-acetylation-mark]], [[foundations/chip-seq]], [[foundations/atac-seq]], [[foundations/homer-motif-enrichment-analysis]]
- Biological foundations: [[foundations/midostaurin]], [[foundations/momelotinib]], [[foundations/filgotinib]], [[foundations/ikbke-ikk-epsilon-kinase]], [[foundations/endogenous-retrovirus-viral-mimicry]], [[foundations/tbk1-tank-binding-kinase-1]], [[foundations/irf3-interferon-regulatory-factor-3]], [[foundations/stat1-tf]], [[foundations/stat2-tf]], [[foundations/nf-kb-p65-rela]], [[foundations/lps-toll-like-receptor-signaling]], [[foundations/il4-cytokine]], [[foundations/bone-marrow-derived-macrophage-bmdm]], [[foundations/type-interferon-ifna-ifnb]]
- People: [[people/francesco-gualdrini]], [[people/gioacchino-natoli]]
