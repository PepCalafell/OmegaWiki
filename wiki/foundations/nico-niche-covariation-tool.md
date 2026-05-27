---
title: "NiCo — Niche Covariation analysis tool"
slug: nico-niche-covariation-tool
domain: "methods / spatial-transcriptomics / single-cell-integration"
status: mainstream
aliases:
  - "NiCo"
  - "niche covariation"
  - "NiCo pipeline"
  - "NiCo framework"
first_introduced: "Agrawal, Thomann, Basu & Grün, Nat Commun 2024"
date_updated: 2026-05-27
source_url: "https://github.com/gruenlab/NiCo"
---

## Definition

NiCo is a Python framework that integrates imaging-based single-cell-resolution spatial transcriptomics (MERFISH, seqFISH, STARmap, MERSCOPE, 10x Xenium, Nanostring CosMx) with matched scRNA-seq reference data to infer how the cellular microenvironment modulates cell state. It runs three sequential modules: (1) Annotations — cell-type label transfer via soft mutual nearest neighbors with iterative anchor propagation; (2) Interactions — per-cell-type regularized logistic regression classifier that predicts central cell identity from local niche composition, exposing predictive neighbor cell types via signed coefficients; (3) Covariations — integrative or ordinary NMF to derive a small set of latent factors per cell type, followed by ridge regression of each central-cell factor on neighbor factors to detect cell-state covariation across co-localized pairs.

## Intuition

Available spatial methods either localize ligand-receptor pairs (COMMOT, SpaOTsc), detect spatially variable genes (SpatialDE), or infer tissue domains (Stagate, CellCharter). None directly answer "does the state of cell A change as a function of which cell B sits next to it?" NiCo answers exactly that, using cell-type-specific latent factors as the unit of covariation and not requiring single-cell mapping of scRNA-seq onto the spatial slide. The latent-factor design lets the model interrogate genome-wide gene programs even when the spatial panel only measures 200–500 genes.

## Formal notation

- Input: cell-by-gene spatial matrix + 2D coordinates; cell-by-gene scRNA-seq matrix + cell-type labels.
- Annotation: soft MNN anchors → pruning by Leiden clusters of spatial modality → kNN majority vote on non-anchors.
- Interaction: per central cell type CC, regularized logistic regression β(CC, niche-type, R) on neighborhood composition within radius R (default R=0, juxtacrine).
- Covariation: per CC and per niche-type NC, ridge regression of CC factor h_i on all NC factors {h_j}; significant β_{ij} indicates positive or negative covariation. Multivariate p-value from two-tailed t-statistics on regression coefficients.
- Latent factors: K=3 by default per cell type; integrative NMF on shared genes if cell segmentation is clean, else ordinary NMF on scRNA-seq only with cell loadings transferred to spatial modality.

## Key variants

- iNMF mode (clean segmentation) vs scRNA-only-NMF mode (when spillover dominates).
- Variable neighborhood radius R (R=0 juxtacrine; R≥1 paraview / higher-order interactions).
- Cutoff c on regression coefficients controls neighborhood-graph sparsity (defaults to 0.01–0.1).

## Known limitations

- Cannot run on sequencing-based spatial transcriptomics that aggregate transcripts across multiple cells per spot; needs single-cell segmentation.
- Covariation predictions are correlational; do not isolate signaling from biomechanical or metabolic competition.
- Cell-type annotation quality depends on having a matched scRNA-seq reference covering all spatial cell types.
- Latent factor count K=3 is a heuristic; sensitivity to K not fully characterized in the original paper.

## Open problems

- Causal disentanglement of signaling vs metabolic vs biomechanical drivers of covariation.
- Extension to full transcriptome imaging assays without requiring scRNA-seq reference.
- Principled K and R selection.

## Relevance to active research

NiCo is one of the first methods to push spatial transcriptomics analysis past tissue-domain / ligand-receptor descriptions into mechanistic statements about cell-state interdependence in local niches. Closest peers: NCEM (intra-cell-type variance explained by niche composition), MISTy (random-forest-based predictor of local gene interactions), COMMOT/SpaOTsc (optimal-transport ligand-receptor inference).
