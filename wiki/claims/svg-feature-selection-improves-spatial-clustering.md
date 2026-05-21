---
title: "SVG-based feature selection generally improves spatial-domain clustering over HVG-based selection"
slug: svg-feature-selection-improves-spatial-clustering
status: supported
confidence: 0.8
tags:
  - spatial-transcriptomics
  - clustering
  - feature-selection
  - benchmarking
domain: spatial-transcriptomics-methods
source_papers:
  - systematic-benchmarking-computational-methods-identify-spatially
evidence:
  - source: "[[papers/systematic-benchmarking-computational-methods-identify-spatially]]"
    type: supports
    strength: strong
    detail: "On DLPFC (12 samples, manually annotated 6 cortical layers + WM), OSCC (12 samples, HPV-negative oral squamous cell carcinoma), and HER2 (8 samples, HER2-positive breast tumours), top-2000 SVGs from most methods beat top-2000 scanpy HVGs as input features for Leiden, BayesSpace, and Banksy clustering measured by ARI. Only SpaGCN, scGCO, BOOST-GP, SOMDE, and Sepal failed to outperform HVGs."
conditions: "Holds for 10x Visium data with available expert pathologist or layer annotation. Number of features fixed at 2000. Three clustering algorithms tested. Result is per-sample rank-based; absolute ARI gain varies."
date_proposed: 2026-05-21
date_updated: 2026-05-21
---

## Statement

For spatial-domain detection on 32 Visium samples (DLPFC, OSCC, HER2), top-2000 SVGs selected by most SVG methods produce higher clustering ARI than top-2000 HVGs selected by scanpy across Leiden, BayesSpace, and Banksy clustering algorithms.

## Evidence summary

Quote (p.12): "we observed that most SVG detection methods consistently improved spatial clustering accuracy relative to HVG-based feature selection, underlying the value of incorporating spatial information to gene selection for this specific analysis. Only a few methods (SpaGCN, scGCO, BOOST-GP, SOMDE, and Sepal) failed to outperform HVGs in this benchmarking."

Best three SVG methods for this task: Moran's I (mean rank 6.5), SpatialDE2 (6.6), nnSVG (6.8).

## Conditions and scope

Holds on Visium data with manual ground-truth annotation. The 5 methods that fail to beat HVGs do so for distinct reasons — sensitivity gaps in tissue architecture coverage. The number of features (2000) and choice of clustering algorithm partly determine the gain.

## Counter-evidence

5 of 14 SVG methods do not improve over HVGs, indicating method choice matters. The gain over HVGs is modest in absolute ARI for some methods.

## Linked ideas

(none yet)

## Open questions

- Does the SVG-over-HVG advantage hold on imaging-based ST data (MERFISH, Xenium, CosMx) where panels are gene-selected upstream?
- Does combining SVG and HVG feature sets via union or weighted score outperform either alone?
