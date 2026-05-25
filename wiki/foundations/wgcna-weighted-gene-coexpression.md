---
title: "WGCNA — Weighted Gene Co-expression Network Analysis"
slug: wgcna-weighted-gene-coexpression
domain: methods
status: mainstream
aliases:
  - WGCNA
  - weighted gene coexpression network analysis
  - co-expression network module analysis
  - eigengene module analysis
  - protein co-expression WGCNA
  - module-eigenprotein WGCNA
first_introduced: "Langfelder & Horvath 2008 BMC Bioinformatics"
date_updated: 2026-05-25
source_url: "https://horvath.genetics.ucla.edu/html/CoexpressionNetwork/Rpackages/WGCNA/"
---

## Definition
A correlation-based network analysis framework that groups variables (genes or proteins) into modules of co-regulated entities based on a soft-thresholded adjacency matrix and topological-overlap clustering. Each module is summarised by an eigengene/eigenprotein (first principal component); within-module hub features are those most strongly correlated with the eigenfeature.

## Intuition
Rather than testing individual features, WGCNA identifies coherent programs by clustering the correlation structure of the data, then relates programs to phenotypes via module-trait correlations.

## Formal notation
- Adjacency: a_ij = |cor(x_i, x_j)|^β, β chosen for scale-free topology
- Topological overlap matrix: TOM_ij integrates direct and shared-neighbour connectivity
- Modules: hierarchical clustering on dissTOM = 1 − TOM
- Hub: max |cor(x_i, ME_module)|

## Key variants
- Signed vs unsigned networks
- Consensus WGCNA across multiple datasets
- WGCNA on proteomic data (e.g., TPCPA pan-cancer modules)

## Known limitations
- Soft-threshold β tuning is data-dependent.
- Modules track tissue / batch identity as well as biology.
- Hub identity is correlation-based, not causal.

## Open problems
- Robust WGCNA on single-cell / spatial data with high sparsity.
- Causal extensions linking module hubs to phenotype outcomes.

## Relevance to active research
WGCNA remains the default for module discovery in large bulk transcriptomics and proteomics datasets, and is increasingly applied to pan-cancer proteomics where co-expression structure surfaces unexpected hub-protein drug targets beyond canonical cancer-gene lists.
