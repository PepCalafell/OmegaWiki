---
# === Identification ===
title: "Integrated time-series analysis and high-content CRISPR screening delineate the dynamics of macrophage immune regulation"
slug: integrated-time-series-analysis-high-content
arxiv: ""
doi: "10.1016/j.cels.2025.101346"
pmid: "40782800"
venue: "Cell Systems"
year: 2025
authors:
  - Peter Traxler
  - Stephan Reichl
  - Lukas Folkman
  - Lisa E. Shaw
  - Victoria Fife
  - Amelie Nemc
  - Djurdja Pasajlic
  - Anna Kusienicka
  - Daniele Barreca
  - Nikolaus Fortelny
  - André F. Rendeiro
  - Florian Halbritter
  - Wolfgang Weninger
  - Thomas Decker
  - Matthias Farlik
  - Christoph Bock
first_author: "Peter Traxler"
corresponding_author: "Christoph Bock"

# === Source & metadata ===
source_type: pdf
s2_id: "b345d80e3b3bc1614baa179a778c4057e53ae882"
date_added: 2026-06-04
ingested_date: 2026-06-04
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - macrophage
  - epigenetics
  - chromatin-accessibility
  - crispr-screen
  - crop-seq
  - cite-seq
  - interferon
  - jak-stat
  - innate-immunity
  - multi-omics
  - time-series
keywords:
  - epigenetic potential
  - relative transcriptional abundance
  - CROP-seq
  - CITE-seq
  - Mixscape
  - cross-prediction functional similarity
  - PU.1 / SPI1
  - EP300
  - Listeria
  - regulons
domain: immunology

# === Biomedical domain ===
tissue: [bone_marrow, in_vitro_only]
condition: [healthy]
disease_specific: []
species: [mouse]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [bulk_RNA-seq, ATAC-seq, scRNA-seq_10x, CITE-seq, flow_cytometry, qPCR]
n_samples: 142
n_cells_total: 37456
integration_method: "custom normalization + batch correction (gene-centric RNA/ATAC integration)"

# === Biology captured ===
key_cell_types: [macrophage, bone-marrow-derived macrophage, RAW 264.7]
key_markers: [Spi1, Ep300, Sfpq, Sf3b1, Smc1a, Med8, Med14, Stat1, Stat2, Irf9, Jak1, Tyk2, Ifnar1, Rela, Irf8]
key_pathways: [JAK-STAT, type-I-interferon, NF-κB, TLR, TNF, MAPK]

# === User project membership ===
projects: [thesis, methods]
priority: context
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "GEO: GSE263763 (super-series; RNA-seq GSE263759, ATAC-seq GSE263758, CROP-seq GSE263760/GSE263761)"

# === Cross-references ===
code_url: "https://github.com/epigen/macrophage-regulation"
cited_by: []
---

## Problem
How do macrophages mount swift, pathogen-specific transcriptional responses and then return to homeostasis? Dissecting this requires both (i) dense, time-resolved measurement of the regulatory landscape (transcription + chromatin) across diverse immune stimuli and (ii) functional, causal evaluation of the candidate regulators at scale — capabilities that had not previously been combined in a single study.

## Key idea
Combine dense multi-omics time series (RNA-seq + ATAC-seq, six stimuli, six time points over 24 h) of murine macrophages with high-content single-cell CRISPR screens (a combined CROP-seq + CITE-seq assay) of transcription/chromatin regulators, and integrate the two via machine-learning cross-prediction to build a functional similarity graph of regulators and connect it back to time-series "regulons." Two new quantitative concepts — **epigenetic potential** (open chromatin in excess of transcription) and **relative transcriptional abundance** (transcription in excess of promoter accessibility) — describe how macrophages stay primed for rapid responses.

## Method
- Primary murine bone-marrow-derived macrophages (BMDMs) treated with six stimuli — *Listeria monocytogenes*, LCMV, UV-irradiated *Candida albicans*, LPS, IFN-β, IFN-γ — profiled by RNA-seq and ATAC-seq at 0, 2, 4, 6, 8, 24 h (31 conditions, 2 replicates).
- Unsupervised dimensionality reduction, differential expression/accessibility, k-means temporal clustering, gene-set enrichment, and TF motif enrichment.
- Gene-centric integration of expression and promoter accessibility (normalization + batch correction) to identify "divergent" genes (epigenetic potential vs relative transcriptional abundance).
- Pooled CRISPR screens in RAW 264.7-Cas9 macrophages using a combined CROP-seq (whole-transcriptome) + CITE-seq (11 surface markers) assay; MOI 0.1, ~90% untransduced co-culture to isolate cell-intrinsic effects; Listeria time course. Proof-of-concept (15 genes, 9,153 cells) then upscaled (135 genes, 28,303 cells).
- Mixscape perturbation modeling; leave-one-group-out cross-prediction of knockout identity → functional similarity graphs; STRING comparison; enrichment of KO signatures in time-series regulons.
- EP300 validation by individual CRISPR KO and small-molecule inhibition (SGC-CBP30 reader; A-485 catalytic), qPCR readout.

## Results
- Six stimuli produced two main trajectories (interferon vs pathogen); IFN-β and IFN-γ converged at 2 h then diverged; LCMV responded late (24 h); Candida resolved within 24 h.
- Universal upregulation of immune programs and (transcription-only) downregulation of cell-cycle/metabolism, with retained chromatin accessibility — stronger cell-cycle repression for type-I IFN (IFN-β/Listeria/LPS) than IFN-γ.
- Epigenetic potential and relative transcriptional abundance identified as two complementary routes to rapid immune-gene induction; clusters transition between them over the Listeria time course.
- CRISPR screens: Spi1/PU.1 KO had dominant, time-invariant effects; JAK-STAT members (Jak1, Stat2, Irf9, Ifnar1, Tyk2) formed a tight module; Ep300 KO uniquely de-repressed ISGs; chromatin/RNA machineries (MED8/14, SMC1A, SF3B1, SFPQ) emerged as immune regulators.
- Cross-prediction functional similarity graph recovered >80% STRING-supported edges plus novel functional similarities (e.g. Ep300/Smc1a/Myd88/Runx1; Sfpq/Ep300 as IFN constrainers).
- EP300's repression of ISGs validated by both genetic KO and two mechanistically distinct small-molecule inhibitors.

## All claims (exhaustive)
- `[c01]` Macrophages shift from cell-cycle/maintenance to immune activation while retaining promoter accessibility at downregulated genes `(p.4-5)` "many downregulated genes maintained high levels of chromatin accessibility, suggesting that the downregulation was temporary" — confidence: high — type: mechanistic — links: [[concepts/epigenetic-potential-macrophage]] [[foundations/atac-seq]] [[claims/macrophages-shift-cell-cycle-immune-activation]]
- `[c02]` Type-I IFN (IFN-β, Listeria, LPS) downregulates cell-cycle genes more strongly than type II IFN (IFN-γ) `(p.5,14)` "This temporary reduction of basic cell functions ... appeared to be specific to the type-I IFN response triggered by IFN-β, Listeria, and LPS" — confidence: medium — type: correlational — links: [[foundations/type-interferon-ifna-ifnb]] [[claims/type-interferon-causes-stronger-cell-cycle]]
- `[c03]` Unrealized epigenetic potential (open chromatin > transcription) enables rapid immune-gene upregulation `(p.6,8)` "rapid transcriptional upregulation exploits a pre-established 'epigenetic potential' at certain genes" — confidence: high — type: mechanistic — links: [[concepts/epigenetic-potential-macrophage]] [[claims/unrealized-epigenetic-potential-enables-rapid-immune]]
- `[c04]` Relative transcriptional abundance is a complementary route to rapid immune-gene upregulation `(p.7-8)` "we define as transcription levels that exceed those typically seen in genes with similar promoter accessibility" — confidence: medium — type: mechanistic — links: [[concepts/relative-transcriptional-abundance]] [[claims/relative-transcriptional-abundance-complementary-route-rapid]]
- `[c05]` A combined CROP-seq + CITE-seq assay enables high-content CRISPR screening with joint transcriptome/surface-protein readout `(p.9-11)` "we established a method for high-content CRISPR screening that combines CROP-seq and CITE-seq" — confidence: high — type: methodological — links: [[foundations/crop-seq-crispr-droplet-sequencing]] [[foundations/cite-seq-citeseq]] [[claims/combined-crop-seq-cite-seq-high]]
- `[c06]` Spi1/PU.1 KO broadly downregulates macrophage-identity genes and TLR/TNF-α/JAK-STAT signaling across the time course `(p.8)` "broad downregulation of genes and cell-surface markers relevant for macrophage biology ... TLR, TNF-α, and JAK-STAT" — confidence: high — type: mechanistic — links: [[foundations/spi1-pu1-master-tf]] [[claims/spi1-pu-knockout-downregulates-macrophage-identity]]
- `[c07]` Spi1/PU.1 KO unexpectedly increases ISG expression, suggesting a repressive role `(p.8)` "Spi1 knockout cells also expressed increased levels of certain interferon response genes ... PU.1 may directly repress certain interferon response genes" — confidence: medium — type: mechanistic — links: [[foundations/spi1-pu1-master-tf]] [[claims/spi1-pu-knockout-increases-interferon-stimulated]]
- `[c08]` EP300 represses ISGs while promoting inflammatory genes in macrophages `(p.8,14)` "Ep300 regulates cell defense by promoting inflammation while restraining the interferon response" — confidence: high — type: mechanistic — links: [[foundations/ep300-histone-acetyltransferase]] [[claims/ep300-represses-interferon-stimulated-genes-while]]
- `[c09]` Small-molecule EP300 inhibition (SGC-CBP30, A-485) phenocopies Ep300 KO in upregulating ISGs `(p.11-12)` "Both knockout and inhibition resulted in the upregulation of the ISGs in cells that were treated with IFN-β for 2 h" — confidence: high — type: pharmacological — links: [[foundations/ep300-histone-acetyltransferase]] [[claims/small-molecule-ep300-inhibition-phenocopies-knockout]]
- `[c10]` JAK-STAT members form a co-clustered module; KO effects more similar within a time point than across time points `(p.12-13)` "the different JAK-STAT knockouts altered the macrophages in very similar ways, but they regulated different gene sets for each time point" — confidence: high — type: mechanistic — links: [[foundations/isgf3-complex]] [[concepts/perturbation-cross-prediction-functional-similarity-graph]] [[claims/jak-stat-pathway-members-form-co]]
- `[c11]` JAK-STAT signaling maintains tonic ISG expression in untreated macrophages `(p.13,15)` "Knockouts of JAK-STAT pathway members resulted in reduced ISG expression even in untreated macrophages (0-h time point)" — confidence: high — type: mechanistic — links: [[concepts/tonic-baseline-jak-stat-homeostasis]] [[claims/baseline-jak-stat-homeostasis-cd8-macrophage]]
- `[c12]` SFPQ and EP300 are negative regulators of the interferon response that share transcriptional effects across layers `(p.12-15)` "SFPQ helps maintain the expression of similar genes at the post-transcriptional level as EP300 does at the transcriptional level" — confidence: medium — type: mechanistic — links: [[concepts/perturbation-cross-prediction-functional-similarity-graph]] [[claims/sfpq-ep300-negative-regulators-interferon-response]]
- `[c13]` Cross-prediction between perturbation signatures yields a functional similarity graph recovering known interactions (>80% STRING) plus novel ones `(p.11-12)` "More than 80% (24 out of 29) of the edges in the functional similarity graph were supported by predicted protein-protein interactions in the STRING database" — confidence: high — type: methodological — links: [[concepts/perturbation-cross-prediction-functional-similarity-graph]] [[foundations/mixscape-crispr-perturbation-analysis]] [[claims/cross-prediction-perturbation-signatures-functional-similarity]]
- `[c14]` Mediator (MED8/14), cohesin (SMC1A) and splicing factors (SF3B1/SFPQ) function as macrophage immune regulators `(p.12-15)` "Our results highlight the immune-regulatory roles of chromatin remodeling and the mediator complex and identify Sfpq and Ep300 as modulators" — confidence: medium — type: mechanistic — links: [[claims/mediator-cohesin-splicing-factors-function-macrophage]]
- `[c15]` Gene expression and chromatin accessibility follow globally consistent trends but accessibility is not a simple correlate of expression `(p.5,7)` "underlining that chromatin accessibility is not a simple correlate of gene expression levels" — confidence: high — type: correlational — links: [[foundations/atac-seq]] [[concepts/epigenetic-potential-macrophage]] [[claims/gene-expression-chromatin-accessibility-globally-consistent]]

## Discussion captured

### Authors' interpretation
The authors argue that unrealized epigenetic potential, the ability to establish relative transcriptional abundance, and baseline (tonic) signaling through immune pathways in homeostatic macrophages all contribute to the cells' preparedness for rapid immune responses. They interpret JAK-STAT knockout effects as a switch from a STAT2/IRF9-dependent homeostatic regulon (possibly alternative ISGF3 complexes) to a canonical STAT1/STAT2/IRF9 ISGF3 program upon IFN-β. They propose EP300 balances HDAC activity (BRD4-availability model) and may act via non-histone acetylation.

### Comparisons with prior literature (made by authors)
- Contrast with a prior human PBMC-derived macrophage study reporting stronger IFN-γ effects (possible species difference).
- Consistency with their own recent JAK-STAT homeostasis study ([[papers/jak-stat-signaling-maintains-homeostasis-cells]], Nat Immunol 2024, DOI 10.1038/s41590-024-01804-1).
- EP300 results expand on a previous macrophage polarization screen; Smc1a/Myd88 similarity consistent with a prior cohesin–TLR report.
- Position relative to perturbational studies of macrophage polarization, phagocytosis, programmed cell death, RNA-binding proteins, lncRNAs, Rab GTPases, and dendritic cell regulation.

### Mechanistic hypotheses proposed
- "EP300 may counteract this effect [HDAC-mediated BRD4 sequestration], underlining the importance of regulating global histone acetylation in macrophages" (p.15).
- "SPI1/PU.1 may directly repress certain interferon response genes, in addition to its role as a lineage-determining transcription factor" (p.8).
- SFPQ maintains similar genes post-transcriptionally as EP300 does transcriptionally — simultaneous multi-layer regulation (p.15).

### Caveats and self-criticism
- Combining primary BMDMs (time series) with a cell line (RAW 264.7, CROP-seq) introduces differences, especially in dependence on differentiation factors (Spi1/PU.1, Csf1r).
- Mixscape excludes weak-effect perturbations, omitting some knockouts (e.g. Csf1r/CD115, Fcgr1/CD64) from analysis though present in raw data.

### Future directions suggested
The method should generalize to other cell types and to dissecting disease-associated gene regulation and immune-modulatory therapeutic interventions.

## Limitations
1. Time series covered only the first 24 h with two biological replicates (prioritizing dense time points).
2. Stringent CROP-seq thresholds across time points excluded many high-quality data points to enable integration.
3. Primary cells (time series) vs cell line (screens) mismatch.
4. Mixscape excludes small-effect perturbations.

## Open questions

### Open questions raised by authors
- How do regulators establish vs realize epigenetic potential, and does the framework transfer to other cell types and disease contexts?
- What is the precise mechanism (histone vs non-histone acetylation, HDAC/BRD4 balance) of EP300-mediated ISG repression?

### Open questions identified during ingest
- Are the STRING-independent functional similarities (e.g. Ep300/Smc1a) reproducible in primary macrophages and other systems?
- Does PU.1 directly bind and repress the ISG loci that increase upon its knockout?
- Which post-accessibility mechanisms (elongation, splicing, mRNA stability) drive relative transcriptional abundance?

## My take
A genuinely integrative methods + biology paper: the epigenetic-potential / relative-transcriptional-abundance framework is a clean, measurable way to think about poised chromatin, and the CROP-seq+CITE-seq cross-prediction pipeline turns perturbation-class confusability into an interpretable regulator map. The EP300 dual-validation (genetic + two domain-specific inhibitors) is a model of orthogonal confirmation. Main caveat for reuse: most causal data come from a transformed cell line, so transfer to primary/tissue macrophages is assumed, not shown.

## Related
- [[concepts/epigenetic-potential-macrophage]]
- [[concepts/relative-transcriptional-abundance]]
- [[concepts/perturbation-cross-prediction-functional-similarity-graph]]
- [[concepts/tonic-baseline-jak-stat-homeostasis]]
- [[foundations/crop-seq-crispr-droplet-sequencing]]
- [[foundations/cite-seq-citeseq]]
- [[foundations/mixscape-crispr-perturbation-analysis]]
- [[foundations/ep300-histone-acetyltransferase]]
- [[foundations/atac-seq]]
- [[foundations/spi1-pu1-master-tf]]
- [[foundations/isgf3-complex]]
- [[foundations/type-interferon-ifna-ifnb]]
- [[papers/jak-stat-signaling-maintains-homeostasis-cells]] — builds on (same group; homeostatic JAK-STAT)
- [[papers/transcriptional-regulator-network-human-inflammatory-macrophages]] — similar approach (open chromatin + transcription in macrophage activation)
