---
title: "CITE-seq — cellular indexing of transcriptomes and epitopes by sequencing"
slug: cite-seq-citeseq
domain: "single-cell-genomics / methods"
status: mainstream
aliases:
  - "CITE-seq"
  - "CITEseq"
  - "cellular indexing of transcriptomes and epitopes by sequencing"
  - "REAP-seq"
first_introduced: "Stoeckius et al. 2017 Nat Methods"
date_updated: 2026-05-27
source_url: "https://cite-seq.com/"
---

## Definition

CITE-seq is a droplet-based single-cell technique that simultaneously profiles mRNA and a panel of surface proteins by tagging antibody clones with DNA barcodes (ADTs, antibody-derived tags) that are co-captured and sequenced with cellular mRNA. Output: a paired transcriptome + surface-protein matrix per cell.

## Intuition

CITE-seq lets you see what a cell expresses (mRNA) and what it presents (surface markers) simultaneously — bridging classical flow-cytometry cell-type definitions with unbiased scRNA-seq atlasing.

## Key variants

- Standard CITE-seq with ADT-labeled antibody panels
- TotalSeq A/B/C reagent families
- 5'-CITE-seq compatibility for TCR/BCR coupling
- 146-marker CITE-seq panels (von Locquenghien et al. 2025) for deep immune phenotyping in PDTFs

## Known limitations

- Antibody panel pre-selection bias; not unbiased like full-proteomics
- Background staining and unspecific ADT binding require careful denoising (DSB, totalVI)
- Cost per cell roughly doubles vs scRNA-seq alone

## Relevance to active research

Used in [[macrophage-targeted-immunocytokine-leverages-myeloid-nk]] with a 146-marker panel on 93,087 cells from five RCC PDTFs to integrate transcriptomic and proteomic readouts of MiTE-144 treatment effects (analysed with [[totalvi-cite-seq-modeling]]).
