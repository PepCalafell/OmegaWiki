---
# === Identification ===
title: "Reconstructing developmental and disease progression with sample-level embeddings"
slug: reconstructing-developmental-disease-progression-sample-level
arxiv: ""
doi: "10.64898/2025.12.10.693462"
pmid: ""
venue: "bioRxiv"
year: 2025
authors: ["Longda Jiang", "Zhixin Cyrillus Tan", "Isabella N. Grabski", "Yuhan Hao", "Nathan Nakatsuka", "Sourav Sarkar", "Anagha Shenoy", "Rahul Satija"]
first_author: "Longda Jiang"
corresponding_author: "Rahul Satija"

# === Source & metadata ===
source_type: pdf
s2_id: ""
date_added: 2026-06-03
ingested_date: 2026-06-03
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags: [single-cell, sample-level-embedding, scSLIDE, disease-trajectory, methods, WNN, diffusion-map]
keywords: [sample-level embedding, density estimation, landmark cells, diffusion map, disease progression, case-control, pseudostage, semi-supervised]
domain: methods

# === Biomedical domain ===
tissue: [blood, brain, multi]
condition: [healthy]
disease_specific: [covid_19, alzheimers_disease, zebrafish_embryogenesis]
species: [human, zebrafish]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [scRNA-seq_10x, snRNA-seq, sci-RNA-seq3]
n_samples:
n_cells_total:
integration_method: "WNN"

# === Biology captured ===
key_cell_types: [CD14_monocytes, CD16_monocytes, dendritic_cells, microglia, SST_interneurons, mature_fast_muscle]
key_markers: [SNCA, APOE, LRRK2, SNX27, ttn.1, ttn.2, mylpfa, mylpfb]
key_pathways: [interferon_response, neutrophil_degranulation, Rho_GTPase, signal_transduction]

# === User project membership ===
projects: [methods]
priority: reference
read_status: skimmed

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "CZ CELLxGENE (COMBAT, Stephenson, SEA-AD); AD Knowledge Portal (Psych-AD); ZSCAPE portal (zebrafish)"

# === Cross-references ===
code_url: "https://github.com/satijalab/scSLIDE"
cited_by: []
---

## Problem

Most single-cell computational frameworks treat the **cell** as the fundamental unit of analysis. But many translational questions — patient stratification, disease trajectory, treatment-response prediction — concern the **sample** (a whole patient or specimen). The prevailing paradigm assigns cells to types/states and runs binary "case vs control" differential expression within each type. This has two failures: (1) it produces sprawling, hard-to-prioritize DE-gene lists, and (2) it assumes every sample within a group is a homogeneous representative of its condition. For heterogeneous conditions (Alzheimer's, COVID-19) with noisy or subjective labels, case-control analysis collapses continuous, multi-axis biology into binary labels, hurting power and cross-study reproducibility.

## Key idea

**scSLIDE** (single-cell Sample-Level Integration using Density Estimation) reframes analysis around the sample. It (1) embeds cells into a **semi-supervised** latent space that keeps cell-type resolution while emphasizing phenotype-linked variation, (2) summarizes each sample as a **density profile over landmark cells**, and (3) uses that per-sample representation for clustering, trajectory inference, and differential analysis — turning each sample into a point in "sample space".

## Method

1. **Cell embedding (semi-supervised).** A "type"-focused unsupervised embedding (integration/reference mapping) and a "state"-focused supervised embedding (PLS against sample metadata) are fused via the **weighted nearest neighbor (WNN)** framework into one space that retains type resolution yet prioritizes phenotype signal and can still discover unprovided axes.
2. **Landmark density quantification.** ~5,000 landmark cells are chosen via **geometric sketching** to span abundant and rare states. For each cell the k-nearest landmarks are found and aggregated per sample into a landmark-abundance matrix, then normalized with a **chi-square-style** transform (observed−expected, scaled by √expected) into a **sample-level relative density matrix**.
3. **Sample-level analysis.** Cosine distances between sample columns feed diffusion maps / t-SNE / clustering; **principal curves** infer disease/developmental pseudo-trajectories; trajectory **NB-GLM** DE and the **TRADE**-based transcriptome-wide impact (TI) score identify driver genes and prioritize cell types.

## Results

- **COVID-19 (COMBAT: 78 infected + 10 controls, >700k cells).** Diffusion components separate three *independent* axes — DC1 case/control, DC2 time-since-onset (interferon program), DC3 severity continuum (neutrophil degranulation). Myeloid cells most affected (TRADE TI). Findings reproduced on an independent cohort; prioritization beat Augur in cross-dataset reproducibility.
- **Alzheimer's (SEA-AD: 89; Psych-AD: 299; snRNA-seq).** Case-control DE replicated at only ~17% across cohorts. scSLIDE inferred a continuous severity trajectory (principal curve) that matched the independent neuropathology **CPS score (r=0.67, p=5.07e-13)** and CERAD/cognition measures. Trajectory DE recovered AD genes (SNCA, APOE, LRRK2…) with higher power, surfaced a novel microglial **Rho GTPase** enrichment, and replicated at **82.8%** across cohorts.
- **Benchmarks.** Permutation negative control yielded no spurious structure. scSLIDE beat MrVI, scPoli, PILOT, unsupervised-scSLIDE, and a proportion baseline (McFadden pseudo-r² 0.701 case-control / 0.526 CPS).
- **Zebrafish (ZSCAPE: ~528k cells, 1,025 embryos, 18 timepoints).** Embryos cluster by stage more sharply than by cell-type proportions; temperature-outlier embryos flagged automatically; a continuous **pseudostage** captures within-timepoint heterogeneity (fast-muscle markers ttn.1/2, mylpfa/b). Here unsupervised scSLIDE sufficed.

## All claims (exhaustive)

- `[c1]` scSLIDE represents each sample as a landmark relative-density profile (p.4) "we estimate the density of cells from the sample that fall within its high-dimensional WNN local neighborhood ... generating a 'landmark abundance' matrix" — confidence: high — type: methodological — links: [[claims/scslide-represents-each-sample-landmark-density]] [[concepts/sample-level-embedding]] [[concepts/landmark-based-density-estimation]]
- `[c2]` scSLIDE builds a semi-supervised cell embedding by WNN-combining unsupervised and PLS embeddings (p.4) "Combining these with WNN yields a single semi-supervised space that retains high-resolution cell type information ... and simultaneously prioritizes features associated with phenotypes" — confidence: high — type: methodological — links: [[claims/scslide-builds-semi-supervised-cell-embedding]] [[foundations/wnn-weighted-nearest-neighbor-integration]] [[foundations/partial-least-squares-pls]]
- `[c3]` Chi-square-style normalization yields the sample-level relative density matrix (p.4) "we normalize the 'landmark abundance' matrix using a chi-square style transformation ... scale the observed deviation by the square root of this expectation" — confidence: high — type: methodological — links: [[claims/chi-square-normalization-yields-sample-level]] [[concepts/landmark-based-density-estimation]]
- `[c4]` COVID-19 heterogeneity decomposes into independent infection, time, and severity axes (p.5) "DC1 separating cases from controls ... DC2 captured ... time since disease onset ... DC3 stratified patients according to disease severity" — confidence: high — type: correlational — links: [[claims/covid-19-sample-heterogeneity-decomposes-into]] [[concepts/continuous-disease-progression-modeling]] [[foundations/diffusion-map-embedding]]
- `[c5]` scSLIDE recovers the time-since-onset axis without being given that metadata (p.5) "Notably, we did not provide TSO information to the scSLIDE workflow, but it still identified this axis of variation" — confidence: medium — type: methodological — links: [[claims/scslide-recovers-time-since-onset-axis]] [[concepts/sample-level-embedding]]
- `[c6]` COVID-19 DC2 reflects an early interferon response that dampens over time (p.6) "DC2 was dominated by interferon-β–stimulated genes ... rapidly induced at disease onset ... but that subsequently dampened over time" — confidence: medium — type: correlational — links: [[claims/covid-19-dc2-reflects-early-interferon]] [[concepts/continuous-disease-progression-modeling]]
- `[c7]` The COVID-19 severity axis is enriched for neutrophil degranulation genes (p.6) "Top DC3 genes ... highlighted enrichment of genes involved in neutrophil degranulation, a pathway ... linked to myeloid responses in severe COVID-19" — confidence: medium — type: correlational — links: [[claims/covid-19-severity-axis-enriches-neutrophil]]
- `[c8]` Myeloid cells are the most transcriptionally affected populations in COVID-19 (p.6) "myeloid cells (in particular CD14 monocytes, CD16 monocytes and dendritic cells) were most strongly affected" — confidence: high — type: quantitative — links: [[claims/myeloid-cells-most-transcriptionally-affected-populations]] [[foundations/trade-transcriptome-wide-impact]]
- `[c9]` scSLIDE cell-type prioritization is more reproducible across datasets than Augur (p.7) "Augur exhibited lower reproducibility across datasets, for example, prioritizing Naive CD4 T cells above all myeloid cell types in one dataset but not the other" — confidence: high — type: methodological — links: [[claims/scslide-cell-type-prioritization-more-reproducible]] [[foundations/augur-cell-type-prioritization]]
- `[c10]` Alzheimer case-control DE replicates poorly across cohorts (p.7) "only a low number (median: 17) and percentage (median: 17.8%) of the genes successfully replicated" — confidence: high — type: quantitative — links: [[claims/alzheimer-case-control-differential-expression-replicates]] [[concepts/continuous-disease-progression-modeling]]
- `[c11]` scSLIDE infers a continuous Alzheimer severity trajectory via principal curve (p.7) "we therefore fitted a joint principal curve to these components to infer a pseudo-trajectory of disease progression across donors" — confidence: high — type: methodological — links: [[claims/scslide-infers-continuous-alzheimer-disease-severity]] [[foundations/principal-curve-fitting]] [[concepts/continuous-disease-progression-modeling]]
- `[c12]` The scSLIDE Alzheimer trajectory correlates with the independent neuropathology CPS score (p.8) "a clear association between the scSLIDE trajectory and CPS score (Pearson's r=0.67, p-value=5.07×10-13)" — confidence: high — type: quantitative — links: [[claims/scslide-alzheimer-trajectory-correlates-neuropathology-pseudoprogression]] [[concepts/continuous-disease-progression-modeling]]
- `[c13]` Inhibitory-neuron loss and microglial increase track the AD trajectory (p.8) "SST+ interneurons showed clear decreases as AD progressed ... microglia showed clear upward trends in severe AD patients" — confidence: medium — type: correlational — links: [[claims/inhibitory-neuron-loss-microglial-increase-track]]
- `[c14]` Trajectory DE recovers AD-linked genes with greater power than case-control (p.8) "non-significant upregulation of SNCA in microglia ... in binary case-control testing ... robust upregulation along the trajectory with high statistical power" — confidence: medium — type: mechanistic — links: [[claims/trajectory-differential-expression-recovers-alzheimer-linked]]
- `[c15]` Rho GTPase pathway genes rise progressively in microglia along the AD trajectory (p.9) "a specific enrichment for genes involved in Rho GTPase pathway activity ... previous scRNA-seq papers have not identified this enrichment" — confidence: medium — type: mechanistic — links: [[claims/rho-gtpase-pathway-genes-rise-microglia]]
- `[c16]` Trajectory-based DE is far more reproducible than case-control (82.8% vs 17%) (p.9) "82.8% reproducibility rate, compared to 17% for case-control DE) across all cell types" — confidence: high — type: quantitative — links: [[claims/trajectory-based-differential-expression-far-more]] [[concepts/continuous-disease-progression-modeling]]
- `[c17]` scSLIDE detects no spurious structure under sample-label permutation (p.9) "showed no separation of cases and controls ... yielded no differentially expressed genes ... indicating that scSLIDE does not overfit" — confidence: high — type: methodological — links: [[claims/scslide-detects-no-spurious-structure-under]]
- `[c18]` scSLIDE outperforms existing sample-level embedding methods (p.10) "McFadden's pseudo r2=0.701 for scSLIDE, range of 0.189-0.330 for other approaches ... CPS prediction (r2=0.526 ... range of 0.321-0.453)" — confidence: high — type: quantitative — links: [[claims/scslide-outperforms-existing-sample-level-embedding]] [[foundations/mrvi-multi-resolution-variational-inference]] [[foundations/scpoli-prototype-reference-mapping]] [[foundations/pilot-optimal-transport-patient-trajectory]]
- `[c19]` Supervised dimensional reduction is essential for subtle phenotypes but unnecessary for strong temporal signals (p.10) "the unsupervised version of scSLIDE failed to recover the same signals, confirming that the supervised dimensional reduction is essential ... for subtle phenotypes" — confidence: high — type: methodological — links: [[claims/supervised-dimensional-reduction-essential-resolving-subtle]] [[foundations/partial-least-squares-pls]]
- `[c20]` scSLIDE reconstructs zebrafish developmental pseudostage within and across timepoints (p.11) "scSLIDE's pseudostage recapitulates robust and biologically meaningful sample-level variation even within a single developmental timepoint" — confidence: high — type: correlational — links: [[claims/scslide-reconstructs-zebrafish-developmental-pseudostage-within]] [[foundations/sci-rna-seq3]] [[foundations/sci-plex-chemical-transcriptomics]]

## Discussion captured

### Authors' interpretation
The authors interpret scSLIDE as a reframing of single-cell analysis around the sample. They argue a key advantage is resolving multiple distinct axes of sample variation (infection, time, severity) rather than collapsing individuals into binary categories, and that modeling continuous trajectories boosts power and reproducibility. They emphasize that agreement between the scSLIDE AD trajectory and an independent neuropathology-derived burden score (CPS) confirms biological relevance.

### Comparisons with prior literature (made by authors)
- **Milo** (ref 32): also uses density, but for binary differential-abundance testing — contrasted as a distinct problem from scSLIDE's full-distribution summarization.
- **Augur** (ref 47): widely used cell-type prioritization; criticized as limited to binary single-variable comparisons and less reproducible across datasets.
- **WNN** (ref 10): their own prior multimodal framework, reused for the semi-supervised embedding.
- **TRADE** (ref 46): used for transcriptome-wide impact estimation.
- **MrVI, scPoli, PILOT** (refs 71-73): benchmarked sample-level methods that failed to recover the severity trajectory.

### Mechanistic hypotheses proposed
- DC2/interferon: "interferon responses that were rapidly induced at disease onset (independent of severity) but that subsequently dampened over time."
- Microglial Rho GTPase: progressive upregulation "represents an interpretable molecular consequence of the transition toward activated, disease-associated cellular states."

### Caveats and self-criticism
- "scSLIDE's trajectory represents a computational prediction that requires independent validation."
- They did not integrate datasets across studies/consortia; sample-level batch correction is unsolved.
- Scaling to tens of millions of cells "will require further algorithmic advances."

### Future directions suggested
- Replace/augment PLS with supervised deep learning.
- Sample-level batch-effect modeling for multi-cohort atlases.
- Extension beyond scRNA-seq to chromatin accessibility, spatial, and multimodal assays.

## Limitations

- Demonstrated on three datasets per use-case; no cross-study/consortium integration.
- No correction for sample-level (not cell-level) batch effects.
- Severity benchmarking relies on a single ground-truth dataset (SEA-AD CPS).
- Scaling ceiling around hundreds of samples / >1M cells.

## Open questions

### Open questions raised by authors
- How to correct sample-level batch effects from tissue handling/dissociation differences?
- How to scale sample-level embedding to tens of millions of cells?
- Can richer phenotype integration via supervised deep learning improve the embedding?

### Open questions identified during ingest
- How many samples are needed to reliably resolve N independent axes?
- Does the inferred trajectory predict *longitudinal* clinical decline, not just cross-sectional severity?
- Is the microglial Rho GTPase signal causal or a downstream marker?

## My take

A clean, well-validated methods contribution from a top single-cell group. The strongest evidence is the independent neuropathology validation of the AD trajectory (r=0.67) and the 83%-vs-17% reproducibility gap — these make the "case-control collapses real biology" argument concrete rather than rhetorical. The framework is conceptually simple (semi-supervised embedding → landmark density → sample space) and reuses well-understood components (WNN, PLS, diffusion maps, principal curves). Relevant to any multi-sample single-cell study; the sample-level-embedding concept is likely to generalize across modalities.

## Related

- [[sample-level-embedding]] — central concept introduced here.
- [[landmark-based-density-estimation]] — the density-quantification step.
- [[continuous-disease-progression-modeling]] — the analytical paradigm argued for.
- Methods: [[wnn-weighted-nearest-neighbor-integration]], [[partial-least-squares-pls]], [[geometric-sketching]], [[diffusion-map-embedding]], [[principal-curve-fitting]], [[trade-transcriptome-wide-impact]].
- Compared methods: [[milo-differential-abundance-testing]], [[augur-cell-type-prioritization]], [[mrvi-multi-resolution-variational-inference]], [[scpoli-prototype-reference-mapping]], [[pilot-optimal-transport-patient-trajectory]].
- People: [[longda-jiang]], [[rahul-satija]], [[yuhan-hao]].
