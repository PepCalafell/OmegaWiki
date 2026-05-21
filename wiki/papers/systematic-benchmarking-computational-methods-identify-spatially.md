---
title: "Systematic benchmarking of computational methods to identify spatially variable genes"
slug: systematic-benchmarking-computational-methods-identify-spatially
arxiv: ""
doi: "10.1186/s13059-025-03731-2"
pmid: "40968359"
venue: "Genome Biology"
year: 2025
authors:
  - "Zhijian Li"
  - "Zain M. Patel"
  - "Dongyuan Song"
  - "Sai Nirmayi Yasa"
  - "Robrecht Cannoodt"
  - "Guanao Yan"
  - "Jingyi Jessica Li"
  - "Luca Pinello"
first_author: "Zhijian Li"
corresponding_author: "Luca Pinello"
source_type: pdf
s2_id: "22f81f296713100ec8164688d7bb7d98a5576510"
date_added: 2026-05-21
ingested_date: 2026-05-21
ingest_version: 1
last_reviewed:
importance: 3
tier: TIER_2
tags:
  - spatial-transcriptomics
  - SVG
  - benchmarking
  - methods
  - simulation
  - Visium
  - MERFISH
  - spatial-ATAC-seq
  - computational-biology
keywords:
  - spatially variable genes
  - SVG
  - SVP
  - SPARK-X
  - Moran's I
  - nnSVG
  - SOMDE
  - SpatialDE
  - SpatialDE2
  - SpaGFT
  - SpaGCN
  - scGCO
  - Sepal
  - Spanve
  - BOOST-GP
  - GPcounts
  - scDesign3
  - simulation
  - benchmarking
  - 10x Visium
  - MERFISH
  - Slide-seq
  - Stereo-seq
  - Slide-tag
  - DBiT-seq
  - 10x Xenium
  - seqFISH
  - STARmap
  - spatial ATAC-seq
  - DLPFC
  - OSCC
  - HER2
  - BayesSpace
  - Banksy
  - Open Problems
  - Cauchy combination
  - K-S calibration
  - CHAOS score
  - p-value calibration
domain: methods
tissue:
  - brain
  - colon
  - in_vitro_only
  - multi
condition:
  - healthy
  - cancer
disease_specific:
  - HPV-negative oral squamous cell carcinoma
  - HER2-positive breast cancer
  - colon cancer
species:
  - human
  - mouse
hypoxia_relevant: false
contains_immune_cells: false
contains_myeloid: false
techniques:
  - spatial_visium
  - MERFISH
  - Slide-seqV2
  - Slide-tag
  - DBiT-seq
  - Stereo-seq
  - 10x_Xenium
  - seqFISH
  - STARmap
  - spatial_ATAC-seq
  - simulation_scDesign3
  - Leiden_clustering
  - BayesSpace
  - Banksy
n_samples: 96
n_cells_total:
integration_method: ""
key_cell_types:
  - cortical_layer_L1-L6
  - white_matter
  - tumor_epithelium
  - tumor_stroma
  - mouse_embryonic_tissue
key_markers: []
key_pathways: []
projects:
  - methods
  - thesis
priority: reference
read_status: skimmed
hypoxiaverse_status:
exclusion_reason:
data_availability: "Open Problems platform — https://openproblems.bio/results/spatially_variable_genes ; GitHub https://github.com/openproblems-bio/task_spatially_variable_genes"
code_url: "https://github.com/openproblems-bio/task_spatially_variable_genes"
cited_by: []
---

## Problem

Spatial transcriptomics has exploded in technology breadth (Visium, Slide-seq, Stereo-seq, MERFISH, seqFISH, Xenium, STARmap, Slide-tag, DBiT-seq) and analytical pipeline depth. A core analytical step shared by every platform is identifying genes whose expression varies non-randomly in space — spatially variable genes (SVGs). Despite > 14 SVG-detection methods now existing, no benchmark has compared more than 7 methods at a time, and prior comparisons used synthetic data with predefined clusters or a small set of hand-crafted patterns — inflating performance and offering little guidance for method selection.

## Key idea

Reframe SVG detection from binary classification (SVG vs non-SVG) to continuous gene-ranking, then benchmark 14 methods on 96 datasets across 9 ST technologies using six metrics: ranking accuracy (Kendall correlation), classification accuracy (auPRC), statistical calibration (K-S distance under spatially-shuffled null), memory and time scalability (100 → 40k spots), impact on spatial domain detection (ARI across Leiden/BayesSpace/Banksy on DLPFC/OSCC/HER2 datasets), and feasibility on spatial ATAC-seq (CHAOS clustering metric). Use scDesign3 (GP marginals + Gaussian copula) on 50 real reference datasets to generate biologically realistic synthetic data with continuous ground-truth spatial variability via an α-mixing coefficient. Host the entire benchmark on the Open Problems platform as a living, extensible community resource.

## Method

- **Methods evaluated (14)**: Moran's I (Squidpy), Spanve, scGCO, SpaGCN, SpaGFT, Sepal, SpatialDE, SpatialDE2, SPARK, SPARK-X, BOOST-GP, GPcounts, nnSVG, SOMDE.
- **Simulation framework**: scDesign3 fit_marginal with GP spline (k = 500) under NB family; fit_copula Gaussian; 21 α values mixing GP-derived spatial mean and shuffled non-spatial mean; per-gene continuous-valued ground truth.
- **Reference datasets**: 50 real-world ST datasets across 9 technologies (10x Visium n=20; Slide-seqV2 n=5; Slide-tag n=4; DBiT-seq n=6; Stereo-seq n=5; 10x Xenium n=2; MERFISH n=5; seqFISH n=1; STARmap n=2), 17 tissue types, healthy and cancer.
- **Ranking accuracy**: Kendall correlation between estimated and true per-gene spatial variability.
- **Classification accuracy**: auPRC after thresholding ground-truth α to define SVG / non-SVG labels.
- **Calibration**: shuffle spots in real Visium mouse olfactory bulb and Xenium colon-cancer data → expected uniform p-values → K-S distance to U(0,1).
- **Scalability**: 10 datasets, 100 genes, 100–40k spots; record memory and wall-clock time.
- **Downstream clustering**: 32 Visium samples (12 DLPFC + 12 OSCC + 8 HER2). Top-2000 SVGs per method; Leiden (resolution 1), BayesSpace, Banksy clustering; ARI vs expert annotation; rank within sample-clustering combination.
- **Spatial ATAC-seq**: mouse embryonic spatial ATAC at E12.5, E13.5, E15.5; cell × peak matrices; top 20k peaks; Leiden clustering; CHAOS score.
- **Aggregate overall ranking**: per-metric ranks averaged across methods.
- **Open Problems integration**: language-agnostic Nextflow pipeline.

## Results

- **Top performer overall**: SPARK-X (avg rank 4.3 across 6 metrics) — see [[claims/sparkx-best-overall-svg-benchmark]].
- **Ranking accuracy**: SPARK-X Kendall 0.88 > SpatialDE2 0.81 > nnSVG 0.80 > Moran's I 0.76.
- **Calibration**: only SPARK and SPARK-X well-calibrated; 6 over-conservative; 4 over-liberal — see [[claims/most-svg-methods-poorly-calibrated]].
- **Scalability**: SOMDE best memory + best time; SPARK-X 2nd; SPARK ~250 GB at 20k spots; BOOST-GP & GPcounts intractable — see [[claims/somde-best-scalability-svg]].
- **Spatial domain detection**: Moran's I (mean rank 6.5) > SpatialDE2 (6.6) > nnSVG (6.8); most SVG methods beat HVG baseline — see [[claims/svg-feature-selection-improves-spatial-clustering]] and [[claims/morans-i-competitive-baseline-svg]].
- **Spatial ATAC-seq**: only SpatialDE2 marginally beats the all-peaks baseline; SVP detection is an open gap — see [[claims/svg-methods-fail-spatial-atac-svp]].
- **Simulation methodology**: scDesign3 GP-based simulation argued as more realistic than prior binary/predefined-cluster simulations — see [[claims/scdesign3-realistic-svg-simulation]].

## All claims (exhaustive)

- `[c01]` SPARK-X is the best-performing SVG method overall in this 14-method, 96-dataset, 6-metric benchmark (p.13) "SPARK-X as the top-performing method, with an average ranking of 4.3. It demonstrated the best performance in correctly ranking genes based on estimated spatial variation for six out of nine ST profiling techniques" — confidence: high — type: methodological — links: [[foundations/spark-x-svg]] [[concepts/spatially-variable-gene-detection]] [[claims/sparkx-best-overall-svg-benchmark]]
- `[c02]` Only SPARK and SPARK-X produce well-calibrated p-values under a spatially-shuffled null; 6 methods are over-conservative and 4 over-liberal (p.8) "SPARK-X and SPARK produced well-calibrated p-values. In contrast, other methods showed poor calibration… six methods (SpatialDE, Spanve, SOMDE, scGCO, nnSVG, and BOOST-GP) generated over-conservative p-values… four methods (SpaGFT, GPcounts, SpaGCN, and Moran's I) generally overestimated the p-values" — confidence: high — type: quantitative — links: [[concepts/svg-pvalue-calibration]] [[foundations/spark-x-svg]] [[claims/most-svg-methods-poorly-calibrated]]
- `[c03]` Moran's I, despite simplicity, is the third-best SVG method overall and the BEST for spatial-domain detection (p.14) "Surprisingly, Moran's I, a simple method based on autocorrelation between spots and their spatial neighbors, achieved the third-best performance… notably outperforming other methods in spatial domain detection" — confidence: high — type: methodological — links: [[foundations/morans-i-spatial-autocorrelation]] [[concepts/spatial-domain-detection-from-svg]] [[claims/morans-i-competitive-baseline-svg]]
- `[c04]` Top-2000 SVGs from most methods improve Visium spatial-domain clustering ARI over top-2000 scanpy HVGs across DLPFC, OSCC, HER2 with Leiden, BayesSpace, Banksy (p.12) "most SVG detection methods consistently improved spatial clustering accuracy relative to HVG-based feature selection… Only a few methods (SpaGCN, scGCO, BOOST-GP, SOMDE, and Sepal) failed to outperform HVGs" — confidence: high — type: quantitative — links: [[concepts/spatial-domain-detection-from-svg]] [[foundations/10x-visium-spatial-transcriptomics]] [[claims/svg-feature-selection-improves-spatial-clustering]]
- `[c05]` SOMDE has the lowest memory and fastest runtime among SVG methods on 100–40k-spot scaling sweep; SPARK-X second; BOOST-GP and GPcounts intractable above 15–20k spots (p.10) "SOMDE exhibited the most efficient memory usage across all benchmarking datasets… SOMDE again achieved the best scalability, closely followed by SPARK-X and scGCO" — confidence: high — type: quantitative — links: [[foundations/somde-svg]] [[foundations/spark-x-svg]] [[claims/somde-best-scalability-svg]]
- `[c06]` On spatial ATAC-seq, only SpatialDE2 marginally beats the "use all peaks" baseline; BOOST-GP / GPcounts time out at 120 h and SPARK fails on memory — purpose-built SVP methods are needed (p.12, p.16) "SpatialDE2 outperformed other methods (mean CHAOS = 0.104)… using all peaks yielded the second-best performance (mean CHAOS = 0.105). This finding suggests that more specialized methods are required to analyze spatial chromatin accessibility data" — confidence: high — type: methodological — links: [[foundations/spatial-atac-seq]] [[foundations/spatialde-svg]] [[concepts/spatial-atac-svp-detection-gap]] [[claims/svg-methods-fail-spatial-atac-svp]]
- `[c07]` scDesign3 GP-marginals plus Gaussian copula, mixed via α ∈ [0,1] across 21 grid values, generate biologically realistic SVG benchmarks with continuous ground-truth spatial variability, improving over prior binary/predefined-cluster simulations (p.5, p.15) "we employed the recent scDesign3 framework, significantly advancing the realism and biological relevance of our simulations… we proposed a novel strategy using scDesign3 and real-world spatial transcriptomics data to create biologically realistic datasets with varying degrees of spatial variation" — confidence: medium — type: methodological — links: [[foundations/scdesign3-simulator]] [[concepts/spatially-variable-gene-detection]] [[claims/scdesign3-realistic-svg-simulation]]
- `[c08]` Different methods exhibit pattern-specific performance differences: SPARK-X / nnSVG / Moran's I / Spanve do poorly on small-spot patterns (pattern 1), while SpatialDE2 / SPARK / Sepal do well on pattern 1 but poorly on pattern 4 (p.7-8) "many methods (e.g., SPARK-X, nnSVG, Moran's I, and Spanve) exhibited low accuracy for pattern 1, where genes were highly expressed in a small area and absent elsewhere. Conversely, SpatialDE2, SPARK, and Sepal showed high performance in pattern 1 but low performance in pattern 4" — confidence: medium — type: methodological — links: [[concepts/spatially-variable-gene-detection]] [[foundations/spark-x-svg]] [[claims/sparkx-best-overall-svg-benchmark]]

## Discussion captured

### Authors' interpretation

Method choice should be tailored to specific goals: SPARK-X for comprehensive ranking, Moran's I for exploratory use or spatial-domain detection, SOMDE or SPARK-X when scalability dominates. Authors stress that p-value calibration failures imply users should select SVGs by top-N rank rather than significance threshold. Moran's I being top-3 overall is interpreted as a wake-up call for the field — a "largely overlooked" classical statistic that should be the baseline in future benchmarks.

The authors also frame their benchmark as a methodological contribution in its own right (the scDesign3-based continuous-spatial-variability simulation strategy), not only a comparison study.

### Comparisons with prior literature (made by authors)

- Prior SVG benchmarks (Charitakis 2023; Zhang 2024; Edsgärd 2018) all included ≤ 7 methods and used predefined-cluster or limited-pattern simulations.
- Authors confirm prior observations that SPARK-X and nnSVG are top performers, and that p-value miscalibration is widespread.
- Novel finding vs prior work: Moran's I emerges as top-3, a result no prior benchmark reported because Moran's I was usually excluded.
- Open Problems platform integration cited as response to Saelens et al. 2019 trajectory-inference benchmark and other "different benchmarks → different answers" reproducibility problems.

### Mechanistic hypotheses proposed

- The Cauchy combination rule (Liu & Xie 2020) is the proposed mechanism for SPARK / SPARK-X's well-calibrated p-values (p.8).
- Cubic scaling of standard GP regression is the proposed mechanism for the memory blow-up of SPARK and SpatialDE on large spot counts (p.10).
- The sparsity, near-binary signal, and high dimensionality of spatial ATAC-seq peak matrices are hypothesised to explain the failure of repurposed SVG methods on SVP detection (p.16).

### Caveats and self-criticism

- The scDesign3 simulation requires pre-selection of genes with high spatial variation, which may bias the benchmark toward methods that exploit similar features.
- Kendall correlation is computed per-gene rather than across spatial patterns, so cross-pattern comparison of methods is limited.
- Rotation-invariance of SVG methods is not evaluated — same tissue oriented differently could give different SVG sets.
- Ground truth for spatial ATAC-seq SVPs does not exist; only CHAOS-based proxy used.

### Future directions suggested

- Pattern-aware SVG benchmarks that score methods per spatial pattern class.
- Rotation/registration-invariance benchmarks.
- Purpose-built SVP-detection algorithms for binary/sparse spatial-omics data.
- Joint SVG–SVP integration toward spatially aware gene-regulatory networks.
- Extension to other spatial omics modalities (proteomics, methylation).

## Limitations

- Methodological: gene pre-selection step inside scDesign3 simulation; Kendall metric per-gene; rotation invariance untested.
- Coverage: 14 methods chosen, but methods released after 2024-Q4 are excluded; living Open Problems platform mitigates this going forward.
- Spatial ATAC-seq evaluated on only 3 timepoints from mouse embryonic data; no ground truth.
- Spot-resolution Visium data dominate (20/50 reference datasets); imaging-based platforms underrepresented.

## Open questions

### Open questions raised by authors

- How should SVP-specific algorithms model the binary, sparse, high-dimensional structure of spatial ATAC-seq?
- Can SVG and SVP integration enable spatial gene-regulatory network reconstruction?
- Do these results extend to spatial proteomics and spatial methylation?

### Open questions identified during ingest

- Does SPARK-X's dominance hold on emerging high-resolution platforms (Visium HD, Slide-Tags) not represented in the 50 reference datasets?
- Could ensemble methods (e.g., SPARK-X + Moran's I + SpatialDE2 union) outperform any single method in practice given complementary pattern-specific behaviour ([c08])?
- For thesis-relevant TME work using Visium / Xenium, does the Moran's I → SpatialDE2 → nnSVG recommendation hold on macrophage-niche spatial data, or does TAM-rich tissue introduce SVG-pattern types where SPARK-X is preferable?

## My take

A solid, well-structured benchmark. The headline result (SPARK-X wins, Moran's I is a "free" top-3 baseline) is actionable for choosing SVG methods in TME spatial work. Two pieces are particularly useful for the thesis: (i) the calibration analysis — I should use rank-based feature selection (top-2000) rather than FDR-based when running SVG on Visium TAM/T-cell colocalization studies; (ii) the SVP-detection gap on spatial ATAC-seq is real and signals that any spatial-ATAC analysis on macrophages will need a custom approach. The scDesign3 simulation framework is also worth bookmarking as a generic ST-method development tool — relevant for any future methods work.

## Related

- [[concepts/spatially-variable-gene-detection]]
- [[concepts/svg-pvalue-calibration]]
- [[concepts/spatial-domain-detection-from-svg]]
- [[concepts/spatial-atac-svp-detection-gap]]
- [[foundations/spark-x-svg]]
- [[foundations/morans-i-spatial-autocorrelation]]
- [[foundations/nnsvg-svg]]
- [[foundations/somde-svg]]
- [[foundations/spatialde-svg]]
- [[foundations/scdesign3-simulator]]
- [[foundations/10x-visium-spatial-transcriptomics]]
- [[foundations/merfish-imaging-spatial]]
- [[foundations/spatial-atac-seq]]
- [[foundations/openproblems-benchmark]]
- [[foundations/cosmx-spatial-transcriptomics]]
- [[foundations/atac-seq]]
- [[people/luca-pinello]]
- [[people/zhijian-li]]
