---
title: "CellPhoneDB — ligand-receptor interaction inference from scRNA-seq"
slug: cellphonedb-ligand-receptor
domain: "bioinformatics / cell-cell-communication"
status: established
aliases:
  - "CellPhoneDB"
  - "CPDB"
  - "CellPhoneDB v2"
  - "CellPhoneDB v3"
  - "CellPhoneDB v4"
  - "ligand-receptor inference"
  - "cell-cell communication database"
  - "receptor-ligand database"
  - "L-R interaction analysis"
tags:
  - scRNA-seq
  - cell-cell-communication
  - ligand-receptor
  - bioinformatics
  - immunology
maturity: established
date_updated: 2026-05-12
---

## Definition

CellPhoneDB is a publicly available curated repository of ligand-receptor pairs (including heteromeric complexes) together with a statistical framework for inferring putative cell-cell communication events from single-cell RNA-seq data. It scores ligand-receptor interactions between cell-type pairs by permutation testing on cluster-mean expression, retaining interactions with both members expressed above threshold in their respective clusters.

## Workflow

1. Annotate scRNA-seq clusters by cell type.
2. Provide normalized expression matrix and cluster labels.
3. Permutation testing assigns p-values to each ligand-receptor pair per cluster-cluster combination.
4. Significant interactions are visualized as dot plots, networks, or chord diagrams.

## Strengths and limitations

- Curated heteromeric complexes (e.g., integrin heterodimers, cytokine receptor subunits) improve interpretability over flat ligand-receptor lists.
- Expression-based inference does not establish spatial proximity — pairing with spatial transcriptomics or mIF is recommended.
- Subject to dropout in scRNA-seq; low-expression ligands or receptors may be missed.
- Often used alongside CellChat for cross-validation; the two tools agree on the most robust interactions but differ on lower-confidence calls.
