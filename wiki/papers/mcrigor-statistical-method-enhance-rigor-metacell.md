---
# === Identification ===
title: "mcRigor: a statistical method to enhance the rigor of metacell partitioning in single-cell data analysis"
slug: mcrigor-statistical-method-enhance-rigor-metacell
arxiv: ""
doi: "10.1038/s41467-025-63626-5"
pmid: "41022768"
venue: "Nature Communications"
year: 2025
authors: ["Pan Liu", "Jingyi Jessica Li"]
first_author: "Pan Liu"
corresponding_author: "Jingyi Jessica Li"

# === Source & metadata ===
source_type: pdf
s2_id: "d5bf883923af242ef25f1a39ff2c19f50a8a2022"
date_added: 2026-06-02
ingested_date: 2026-06-02
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 3
tier: TIER_2
tags: [single-cell, metacell, statistics, benchmarking, methods, scRNA-seq, multiome]
keywords: [metacell, dubious metacell, double permutation, divergence score, granularity optimization, co-expression, gene regulatory inference, sparsity]
domain: "methods"

# === Biomedical domain ===
tissue: [blood, bone_marrow, multi]
condition: [healthy, cancer]
disease_specific: [COVID-19, glioblastoma]
species: [human, mouse]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [scRNA-seq_10x, snRNA-seq, scATAC-seq, CITE-seq, bulk_RNA-seq]
n_samples:
n_cells_total:
integration_method: "Harmony"

# === Biology captured ===
key_cell_types: [B cells, T cells, NK cells, monocytes, dendritic cells, hematopoietic stem and progenitor cells, CD4 T cells, CD8 T cells]
key_markers: [GATA2, TAL1, Lag3, Clspn, KLRG1, HMGB2, IRF7, FOXP3, CCR6]
key_pathways: [adaptive immune response, MHC class II antigen processing, type I interferon response]

# === User project membership ===
projects: [methods, thesis]
priority: reference
read_status: not_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "GSE150728 (COVID-19 PBMC); GSE200046 (scMultiome); GSE99330 (Drop-seq + smRNA FISH); GSE75748 (ESC bulk + scRNA-seq); GSE232040 (Zman-seq); GSE126906 + 10x Genomics (cell lines); Zenodo 10.5281/zenodo.16309527"

# === Cross-references ===
code_url: "https://github.com/JSB-UCLA/mcRigor"
cited_by: []
---

## Problem

Single-cell data are sparse. A common remedy is to aggregate homogeneous cells into **metacells** (averaging their profiles) to reduce technical noise while preserving within-cell-type biological variation — a middle ground between single cells and pseudobulk. But existing metacell methods (MetaCell, MetaCell2, SuperCell, SEACells) lack any check on the homogeneity assumption. They can aggregate cells from different biological states, producing **dubious metacells** whose averaged profiles bias downstream analysis and create spurious discoveries. There is no rigorous definition of a metacell and no principled way to choose the partitioning method or its granularity hyperparameter.

## Key idea

Give "metacell" a statistical definition — a group of cells sharing the same relative feature-abundance vector λ, so all within-metacell variation is technical (see [[concepts/dubious-versus-trustworthy-metacell-statistical-definition]]). Then test it: within a trustworthy metacell, features should be nearly uncorrelated, so structured feature correlation flags heterogeneity. mcRigor operationalizes this with the **divergence score (mcDiv)** and a **double permutation** null (see [[concepts/metacell-divergence-score-mcdiv-double-permutation]]), and uses the resulting dubious-rate to **optimize granularity** via a DubRate/ZeroRate **Score** (see [[concepts/metacell-granularity-optimization-dubrate-zerorate-score]]).

## Method

Built on a hierarchical observation model (expression model for biological variation + multinomial measurement model for technical variation, following Sarkar & Stephens). For dubious-metacell detection (four steps, on a Seurat-V5 LogNormalized, top-2000-HVG matrix):

1. **mcDiv** = ‖R_k − I‖_F / ‖R̃_k − I‖_F, the within-feature-permutation-normalized Frobenius deviation of the feature correlation matrix from identity.
2. **mcDiv_null** via **double permutation**: within-cell permutation (preserves library sizes, kills biological correlation) then within-feature permutation.
3. **Metacell-size-specific thresholds**: 95th percentile of mcDiv_null over similarly-sized metacells (sliding window, bandwidth h = 10).
4. Flag metacell as dubious if mcDiv > threshold.

For optimization, compute **DubRate** (fraction of cells in dubious metacells) and **ZeroRate** (fraction of zeros in the metacell matrix), then **Score = 1 − w·DubRate − (1−w)·ZeroRate** (default w = 0.5), maximized over γ ∈ {2,…,100} and over four metacell methods. Score's common [0,1] scale enables method selection. Standard tools used downstream: [[foundations/scdesign3-simulator]] (semi-synthetic data), [[foundations/cite-seq-citeseq]] (bmcite reference), [[foundations/deseq2-differential-expression]] (DGE), [[foundations/harmony-integration]] + [[foundations/lisi-local-inverse-simpson]] (integration), [[foundations/rnascope-single-molecule-fish]] (smFISH gold standard), [[foundations/atac-seq]] / [[foundations/scrna-seq-10x-chromium]] (multiome), [[foundations/seurat-v3-integration]] (normalization).

## Results

- Detection accuracy on semi-synthetic data: mcDiv ↔ purity Spearman ρ = −0.948; F-score 0.921 (MetaCell), comparable for SEACells/SuperCell/MetaQ.
- All 16 barcode multiplets correctly called trustworthy, validating the technical-variation assumption.
- COVID-19 B-cell co-expression: trustworthy-only correlation reveals adaptive-immune module enrichment (p = 7.6e-19) masked (p = 0.546) when dubious metacells are included.
- Enhancer-gene inference (HSPC multiome): GATA2 0.69→0.76, TAL1 0.83→0.87; recovered a validated GATA2 enhancer.
- Score recovers true γ* = 50 (MetaCell); SEACells γ = 13 best for DGE (bulk concordance 0.800, F-score 0.400 vs single-cell 0.204); optimized γ matches smRNA-FISH zero proportions; Zman-seq trajectory sharpened (ΔcTET 0.718 vs 0.538) with Lag3/Clspn corrected.
- Method ranking: MetaCell and SEACells > SuperCell and MetaCell2 (longer runtimes).

## All claims (exhaustive)

- `[c1]` mcDiv is strongly negatively correlated with ground-truth metacell purity (p.4) "A strong negative Spearman correlation (ρ = −0.948) was observed between mcDiv values and purity." — confidence: high — type: methodological — links: [[concepts/metacell-divergence-score-mcdiv-double-permutation]] [[claims/mcdiv-divergence-score-negatively-correlates-metacell]]
- `[c2]` Double permutation is necessary; within-feature permutation alone misclassifies >35% of trustworthy metacells (p.13) "more than 35% of ground-truth trustworthy metacells … are incorrectly classified as dubious, leading to poor overall classification performance (F-score < 0.4)" — confidence: high — type: methodological — links: [[concepts/metacell-divergence-score-mcdiv-double-permutation]] [[claims/double-permutation-necessary-accurate-dubious-metacell]]
- `[c3]` MetaCell and SEACells outperform SuperCell and MetaCell2 (p.5, p.8) "At the true granularity level γ = 50, MetaCell, SEACells, SuperCell, and MetaQ produced 0.4%, 10.1%, 28.4%, and 7.8% dubious metacells" — confidence: medium — type: quantitative — links: [[concepts/metacell-granularity-optimization-dubrate-zerorate-score]] [[foundations/metacell-aggregation]] [[claims/metacell-seacells-outperform-supercell-metacell2-metacell]]
- `[c4]` Barcode multiplets approximate trustworthy metacells; mcRigor calls all 16 trustworthy (p.4) "mcRigor successfully identified all 16 barcode multiplets as trustworthy metacells." — confidence: high — type: methodological — links: [[concepts/dubious-versus-trustworthy-metacell-statistical-definition]] [[foundations/atac-seq]] [[claims/barcode-multiplets-approximate-trustworthy-metacells-validating]]
- `[c5]` Removing dubious metacells uncovers COVID-19-enriched co-expression masked otherwise (p.6-7) "the adaptive immune response gene module (p-value = 7.6e −19) … included dubious metacells … was not enriched in COVID-19 patients (p-value = 0.54632)" — confidence: high — type: correlational — links: [[concepts/dubious-versus-trustworthy-metacell-statistical-definition]] [[claims/removing-dubious-metacells-uncovers-covid19-differential]]
- `[c6]` Removing dubious metacells improves enhancer-gene regulatory inference (p.7) "the association score between the key erythroid lineage regulator TAL1 and its most correlated peak increased from 0.8266 to 0.8703 … GATA2 … increased from 0.6904 to 0.7606" — confidence: high — type: methodological — links: [[concepts/dubious-versus-trustworthy-metacell-statistical-definition]] [[claims/mcrigor-improves-enhancer-gene-regulatory-inference]]
- `[c7]` Lowering granularity alone is insufficient; coarse + mcRigor beats naively fine partition (p.7) "simply lowering γ is insufficient and that mcRigor is essential for improving statistical power" — confidence: medium — type: methodological — links: [[concepts/metacell-granularity-optimization-dubrate-zerorate-score]] [[claims/lowering-granularity-alone-insufficient-mcrigor-essential]]
- `[c8]` Score selects optimal γ matching the true γ* (p.8) "the highest Score was achieved precisely at γ = γ*" — confidence: high — type: methodological — links: [[concepts/metacell-granularity-optimization-dubrate-zerorate-score]] [[claims/mcrigor-score-selects-optimal-granularity-matching]]
- `[c9]` mcRigor-optimized partition improves DGE concordance with bulk RNA-seq (p.8) "SEACells with γ = 13 … achieves the highest concordance (Pearson correlation ρ = 0.800) and F-score (0.400)" — confidence: medium — type: methodological — links: [[concepts/metacell-granularity-optimization-dubrate-zerorate-score]] [[foundations/deseq2-differential-expression]] [[claims/mcrigor-optimized-partition-improves-dge-concordance]]
- `[c10]` mcRigor distinguishes biological from non-biological zeros, matching smRNA-FISH (p.8) "the γ value selected by mcRigor … resulted in a proportion of zeros that closely matched the proportion of zeros in the smRNA FISH data" — confidence: medium — type: methodological — links: [[concepts/metacell-granularity-optimization-dubrate-zerorate-score]] [[foundations/rnascope-single-molecule-fish]] [[claims/mcrigor-distinguishes-biological-nonbiological-zeros-smfish]]
- `[c11]` mcRigor-optimized partition better reveals temporal immune trajectories and corrects gene patterns (p.9) "a greater cTET difference between the earliest- and latest-stage metacells (0.718 vs 0.538 in the original study)" — confidence: medium — type: methodological — links: [[concepts/metacell-granularity-optimization-dubrate-zerorate-score]] [[claims/mcrigor-optimized-partition-reveals-temporal-immune]]
- `[c12]` Metacell size does not predict trustworthiness (p.11) "no clear relationship exists between metacell size and trustworthiness (as determined by mcRigor)" — confidence: medium — type: mechanistic — links: [[concepts/dubious-versus-trustworthy-metacell-statistical-definition]] [[claims/metacell-size-does-predict-trustworthiness]]

## Discussion captured

### Authors' interpretation

The authors interpret dubious metacells as the root cause of spurious downstream findings (artifact co-expression, false enhancer-gene links, distorted temporal patterns). They frame mcRigor as both a filter (remove dubious metacells) and an optimizer/benchmarker (pick method + γ via Score), emphasizing it is task-agnostic and prior-free.

### Comparisons with prior literature (made by authors)

- Builds on Baran et al.'s original MetaCell definition (resamples of the same original cell).
- Uses the Sarkar & Stephens single-cell observation model to formalize biological vs technical variation.
- Co-expression findings consistent with CS-CORE; enhancer-gene analysis extends the SEACells multiome study (ref. 33); Zman-seq reanalysis from the glioblastoma immune-profiling study (ref. 30).
- Contrasts metacells with pseudobulk and with imputation (scImpute, SAVER, MAGIC, DCA).

### Mechanistic hypotheses proposed

Within a trustworthy metacell, feature correlations are driven only by technical noise (minimal, vanishing as p grows); structured correlation therefore implies mixed biological states. Including dubious metacells in correlation estimation is proven to induce spurious co-expression.

### Caveats and self-criticism

- Double permutation is run only once per metacell.
- mcRigor only flags/removes dubious metacells; it does not yet re-partition them (the mcRigor two-step extension is a first attempt).
- Operates on a single modality at a time.
- Imputation before metacell construction is discouraged as redundant and potentially harmful (can increase dubious metacells).

### Future directions suggested

Multiple-round double permutation; recursive re-partitioning of dubious metacells; a from-scratch trustworthy-by-construction metacell method; multi-modality integration into the statistic and Score; extension to spatial niches and other data types; mcRigor as a benchmark for doublet-removal methods.

## Limitations

- Validation of detection accuracy relies on semi-synthetic data (scDesign3) where ground truth is model-defined.
- On real data, purity is approximated from fine-grained annotations.
- Optimal-γ recovery is poor for methods that produce mostly dubious metacells (SuperCell, MetaCell2).
- Single-modality; spatial transcriptomics niches are out of scope.

## Open questions

### Open questions raised by authors

- Does multi-round double permutation improve robustness?
- Can dubious metacells be recursively re-partitioned rather than discarded?
- Can a new method generate only trustworthy metacells by construction?
- How to define reliable rigor criteria for spatial niches?

### Open questions identified during ingest

- How sensitive is mcDiv to the choice of normalization and HVG count (Seurat V5 defaults are baked in)?
- Could mcRigor's Score be biased toward methods whose dubious-metacell geometry happens to suit the mcDiv statistic?

## My take

A clean, conceptually satisfying contribution: it converts "metacell" from a clustering artifact into a testable statistical object and gives a calibrated, library-size-aware null. The double permutation is the crux — the within-cell step is what makes the test honest. For my own single-cell work (macrophage/immune states, co-expression and regulatory inference), the practical takeaway is concrete: run mcRigor's Score to pick γ and method, and filter dubious metacells before trusting any metacell-level co-expression or peak-gene link. Relevant to [[foundations/metacell-aggregation]]-based pipelines and atlas integration.

## Related

- [[foundations/metacell-aggregation]] — the family of methods mcRigor audits and optimizes.
- [[concepts/metacell-divergence-score-mcdiv-double-permutation]], [[concepts/dubious-versus-trustworthy-metacell-statistical-definition]], [[concepts/metacell-granularity-optimization-dubrate-zerorate-score]] — concepts introduced here.
- [[foundations/scdesign3-simulator]] — same lab (JSB), used for the semi-synthetic validation.
- [[people/pan-liu]], [[people/jingyi-jessica-li]] — authors.
