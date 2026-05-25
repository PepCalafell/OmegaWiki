---
title: "Hypoxia-responsive macrophage subset (cluster 1) in PDAC scRNA-seq"
aliases:
  - "hypoxia-responsive TAM PDAC"
  - "hypoxic macrophage subcluster pancreatic cancer"
  - "macrophage cluster 1 hypoxia PDAC"
  - "hypoxia-sensitive TAM subset"
  - "HIF-active TAM subpopulation"
  - "hypoxia-imprinted macrophage subset"
  - "GSE155698 macrophage hypoxia subcluster"
  - "hypoxia hallmark high macrophage"
  - "hypoxia score high TAM"
  - "PDAC hypoxia-skewed myeloid subset"
tags:
  - hypoxia
  - macrophage
  - PDAC
  - scRNA-seq
  - tumor-associated-macrophage
  - tumor-microenvironment
  - hypoxia-signature
maturity: emerging
key_papers:
  - development-hypoxia-responsive-macrophage-prognostic-model
  - hypoxia-driven-crosstalk-between-tumor-tumor
first_introduced: "Ge et al. 2025 PLoS One; congruent with broader hypoxia-TAM literature (Bai 2022 Mol Cancer; Park 2019 Oncogene)"
date_updated: 2026-05-25
related_concepts:
  - tumor-associated-macrophage-immunosuppression
  - hypoxia-exosomal-mirna-tam-polarization
  - lactate-driven-tam-m2-polarization
  - m1-m2-polarization-paradigm
---

## Definition

A subcluster of tumour-associated macrophages, identified by subclustering single-cell RNA-seq data from PDAC and re-scoring per-cell hypoxia activity, that displays significantly elevated hypoxia-hallmark transcriptional signature compared to the remainder of TAMs. In Ge et al. 2025, this subset is termed "macrophage cluster 1"; the complementary, lower-hypoxia TAM subset is "macrophage cluster 2". The hypoxia-responsive subset is enriched in PDAC vs adjacent normal pancreas and supplies the DEGs from which the 13-gene prognostic model is constructed.

## Intuition

Bulk-tissue hypoxia signatures average over both tumour cells and stroma. At the single-cell level, hypoxia transcriptional response is unevenly distributed across cell types and within TAMs. Identifying a *macrophage-specific* hypoxia-responsive subcluster lets bulk-level signatures be re-grounded in a defined producer cell, and provides a unit of measurement (e.g. fraction of TAMs that are hypoxia-responsive) that is more biologically interpretable than a global score.

## Formal notation

- Identification pipeline: scRNA-seq → cell-type annotation → macrophage extraction → re-clustering (FindNeighbors/FindClusters in Seurat) → hypoxia score per cell (AddModuleScore + AUCell using MSigDB Hallmark Hypoxia 200 genes) → assign cluster with higher hypoxia score → "hypoxia-responsive" label.
- In Ge 2025: macrophage cluster 1 vs cluster 2 distinction; GSEA confirms Hallmark Hypoxia is activated in cluster 1.

## Variants

- Alternative scoring methods: ssGSEA, AUCell, AddModuleScore — different orderings can yield slightly different membership.
- Alternative hypoxia gene sets: Buffa-72, Winter-99, MSigDB Hallmark, custom signatures. The choice can change which TAM subset is labelled hypoxia-responsive.
- Hypoxia-responsive TAM in other tumour types (HCC, NSCLC, GBM) — analogous concept but distinct top genes.

## Comparison

- vs M1/M2 polarisation paradigm ([[concepts/m1-m2-polarization-paradigm]]): orthogonal axis — a hypoxia-responsive TAM can be M1-leaning or M2-leaning depending on context.
- vs IL4I1+ PD-L1+ TAM cluster (MoMac-VERSE): hypoxia-responsive TAMs in PDAC may overlap functionally with the immunosuppressive PD-L1+ cluster characterised in [[concepts/hypoxia-pd-l1-tam-immune-evasion]].
- vs CXCL9+ ICI-responder TAM ([[concepts/cxcl9-spp1-tam-ratio-ici-biomarker]]): the hypoxia-responsive subset is enriched in resistance contexts; CXCL9+ TAMs are the immunotherapy-favourable counterpart.

## When to use

- When deriving bulk-tissue prognostic signatures from scRNA-seq and wanting cell-type provenance for each signature gene.
- When asking whether a "hypoxia signature" actually reads out tumour-cell hypoxia or TAM-resident hypoxia response.
- For PDAC-specific reasoning about immune-resistant niches.

## Known limitations

- Cluster boundaries are inherently soft; calling a cluster "hypoxia-responsive" depends on scoring threshold.
- The identity of "responsive vs unresponsive" is descriptive, not causal — there is no proof the cluster *responds* to hypoxia rather than co-residing with hypoxic niches.
- Generality across PDAC cohorts is limited; the original cohort is Steele 2020 (GSE155698, n=16 PDAC).

## Open problems

- Spatial localisation: do hypoxia-responsive TAMs co-occupy tumour hypoxic niches (CA9+, FMISO-PET-positive regions)?
- Functional perturbation: does HIF1α / HIF2α deletion in macrophages abolish the hypoxia-responsive cluster?
- Mapping to MoMac-VERSE / Coulton 23-cluster atlas: which canonical TAM state is the hypoxia-responsive cluster?

## Key papers

- [[papers/development-hypoxia-responsive-macrophage-prognostic-model]] — defines macrophage cluster 1 in PDAC and constructs the 13-gene model from its DEGs.
- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — review establishing hypoxia-TAM crosstalk biology that this subset operationalises.

## My understanding

For my thesis, this concept matters because it offers a *single-cell-anchored* hypoxia signature that, unlike Buffa-72, has an explicit cellular producer (TAM cluster 1). When reasoning about how hypoxic-niche reprogramming maps onto bulk-RNA hypoxia scores in PDAC, this construct provides a useful intermediate level of granularity. Limitation: derived from a single PDAC cohort with standard pipeline; reproducibility across atlases is unverified.
