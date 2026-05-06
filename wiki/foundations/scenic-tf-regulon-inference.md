---
title: "SCENIC — single-cell regulatory network inference and clustering"
slug: scenic-tf-regulon-inference
domain: "computational-biology / methods"
status: mainstream
aliases:
  - "SCENIC"
  - "single-cell regulatory network inference"
  - "scenic regulon analysis"
  - "GRN inference scRNA-seq"
  - "TF regulon scoring (SCENIC)"
  - "AUCell regulon activity"
  - "pyscenic"
  - "Aibar 2017 SCENIC"
  - "GRNBoost / GENIE3 + cisTarget pipeline"
first_introduced: "Aibar et al. 2017 *Nature Methods*"
date_updated: 2026-05-06
source_url: "https://scenic.aertslab.org/"
---

## Definition

SCENIC is a three-step pipeline for inferring transcription-factor (TF) → target-gene regulons from scRNA-seq and scoring their activity per cell. (1) GENIE3 / GRNBoost2 builds gene co-expression modules anchored on TFs. (2) cisTarget filters those modules to motif-supported targets, producing regulons. (3) AUCell computes a per-cell ranking-based activity score for each regulon.

## Intuition

Whereas DoRothEA uses a curated TF-target database, SCENIC builds a data-driven, cell-population-specific gene regulatory network. It is the standard tool for asking "which TFs are active in which clusters of an scRNA-seq dataset" with motif evidence backing each regulon.

## Formal notation

- Input: cell × gene expression matrix
- Step 1: co-expression modules around each TF (GENIE3 / GRNBoost2)
- Step 2: motif enrichment (cisTarget) → motif-supported regulons
- Step 3: per-cell AUCell area-under-recovery-curve → regulon activity score
- Output: cell × regulon activity matrix + per-regulon DEG sets (DERs)

## Key variants

- SCENIC (R, original)
- pySCENIC (Python, faster, Dask/Distributed-friendly)
- SCENIC+ — adds chromatin accessibility (multi-omic GRN)
- DoRothEA + VIPER — curated alternative (no de novo GRN learning)

## Known limitations

- Heavy compute for large atlases (millions of cells)
- Sensitive to dataset depth and gene dropout
- Motif enrichment is human/mouse-centric

## Open problems

- Cross-dataset regulon stability is not well characterized
- Integration with scATAC and spatial data is still maturing

## Relevance to active research

[[papers/cross-tissue-single-cell-landscape-human]] applies SCENIC to colon, liver, and lung MNP datasets to define differentially expressed regulons (DERs) per Phenograph cluster, identifying NFKB1/NFKB2 as defining the IL1B_Mo cluster and STAT1/STAT2/IRF1/IRF7/ETV7 as common upstream regulators of IL4I1_Mac and ISG_Mo.
