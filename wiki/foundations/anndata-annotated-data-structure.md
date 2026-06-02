---
title: "AnnData (annotated data structure)"
slug: anndata-annotated-data-structure
domain: "methods / single-cell data infrastructure"
status: mainstream
aliases:
  - AnnData
  - annotated data
  - h5ad
  - adata
first_introduced: "Wolf et al. 2018 *Genome Biology* (SCANPY / AnnData)"
date_updated: 2026-06-02
source_url: "https://anndata.readthedocs.io"
---

## Definition

AnnData is the in-memory and on-disk (`.h5ad` / `.zarr`) data structure underlying the scverse single-cell Python ecosystem. It stores an expression matrix `X` (cells × genes) together with aligned per-cell annotations (`obs`), per-gene annotations (`var`), multi-dimensional embeddings (`obsm`), pairwise graphs (`obsp`), unstructured metadata (`uns`) and alternative matrices (`layers`).

## Intuition

It is a single container that keeps the count matrix and every derived annotation (clusters, pseudotime, velocities, neighbor graphs, embeddings) in slots that stay row-aligned to the cells, so tools can read and write standardized fields without re-wrangling.

## Formal notation

Slots used by CellRank kernels: `obsp` (symmetric cell–cell similarity graph), `obs` (pseudotime, experimental time point), `obsm`/`layers` (velocity and GEX representation), passed by field name at kernel initialization.

## Key variants

- `.h5ad` (HDF5) and `.zarr` on-disk formats.
- Backed mode for out-of-core access; MuData for multimodal extension.

## Known limitations

- Single primary matrix `X`; multimodal data needs MuData or layered conventions.
- Convention drift between tool versions (field-name changes).

## Open problems

- Standardizing slot conventions across the rapidly growing tool ecosystem.

## Relevance to active research

- Every CellRank kernel reads its inputs from specific AnnData slots; see [[papers/cellrank-consistent-data-view-agnostic-fate]]. Shared substrate across [[scvelo-rna-velocity]], [[scvi-deep-generative-model]] and the scverse stack.
