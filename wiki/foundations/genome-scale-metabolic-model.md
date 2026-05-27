---
title: "Genome-scale metabolic model (GEM)"
slug: genome-scale-metabolic-model
domain: "systems biology / metabolism"
status: mainstream
aliases:
  - GEM
  - genome-scale metabolic model
  - Human1
  - Mouse1
  - Recon3D
  - metabolic reconstruction
first_introduced: "2003"
date_updated: 2026-05-27
source_url: "https://www.metabolicatlas.org/"
---

## Definition

A **genome-scale metabolic model (GEM)** is a mathematical reconstruction of all biochemical reactions known to occur in an organism, linked back to the genes encoding the enzymes that catalyze them through gene–protein–reaction (GPR) rules. Modern human GEMs such as Human1 and Recon3D encode thousands of reactions, metabolites, and gene associations across compartments.

## Intuition

A GEM is a stoichiometry-aware parts-list of metabolism. Combined with a constraint (e.g. mass balance, optimization objective), it enables flux balance analysis (FBA) of feasible metabolite flows. Combined with omics data, it serves as a prior-knowledge scaffold for inferring pathway or task-level activity from transcriptomics (CellFie, [[sccellfie-metabolic-task-inference]]) and proteomics.

## Formal notation

For metabolites m and reactions r, the stoichiometric matrix S (m × r) satisfies S · v = 0 at steady state (v: flux vector). GPR rules map gene expression g to reaction availability via AND (protein subunits) / OR (isoenzymes) logic.

## Key variants

- **Human1** (Robinson et al. 2020) — consensus human GEM merging Recon3D and HMR2.
- **Mouse1** — mouse counterpart of Human1.
- **Recon3D** — earlier human reconstruction.
- **KEGG / Reactome** — pathway databases, less stoichiometric but widely used as priors.
- **Tissue-specific GEMs** — context-specific reconstructions pruned with bulk/RNA-seq.

## Known limitations

GEMs encode known biochemistry only; novel reactions and post-translational regulation are absent. FBA requires biologically meaningful objective functions (often biomass maximization) that may not fit every cellular context. mRNA-to-flux mapping via GPR rules ignores enzyme kinetics and metabolite levels.

## Open problems

Integrating GEMs with metabolomics at single-cell resolution; learning context-specific objective functions; coupling GEMs to spatial transcriptomics for tissue-architecture-aware flux.

## Relevance to active research

GEMs underpin most transcriptomics-based metabolic inference tools, including CellFie and [[sccellfie-metabolic-task-inference]]. They are the backbone of the [[atlas-scale-metabolic-activities-inferred-single]] atlas of metabolic activities across the [[czi-cellxgene-atlas]].
