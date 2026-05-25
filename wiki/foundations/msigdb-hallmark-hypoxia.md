---
title: "MSigDB Hallmark Hypoxia — 200-gene canonical hypoxia signature"
slug: msigdb-hallmark-hypoxia
domain: "datasets / gene-set-libraries"
status: mainstream
aliases:
  - "Hallmark Hypoxia"
  - "MSigDB H Hypoxia"
  - "MSigDB hypoxia 200 genes"
  - "Liberzon Hallmark Hypoxia"
  - "Hallmark Hypoxia gene set"
  - "MSigDB cancer hallmark hypoxia"
  - "200-gene hypoxia signature"
first_introduced: "Liberzon et al. 2015 Cell Systems (MSigDB Hallmark collection)"
date_updated: 2026-05-25
source_url: "https://www.gsea-msigdb.org/gsea/msigdb/cards/HALLMARK_HYPOXIA"
---

## Definition

The 200-gene Hallmark Hypoxia gene set in the MSigDB Hallmark collection, derived by consensus filtering across multiple founder gene sets to retain genes coherently up-regulated in response to low oxygen levels.

## Intuition

A general-purpose, canonical hypoxia signature widely used as the off-the-shelf default when a tissue-specific signature is not available. Coarser than Buffa-72 or Winter-99 but more broadly validated across MSigDB-driven workflows.

## Formal notation

- 200 genes, curated for consensus hypoxia up-regulation.
- Source: MSigDB Hallmark v2024 (current).

## Key variants

- Buffa-72 ([[foundations/buffa-hypoxia-signature]]) — IHC + array-derived, prognostic in HNSCC and breast.
- Winter-99 — head and neck cancer-derived signature.
- Custom per-disease signatures.

## Known limitations

- Contains genes from canonical HIF pathway as well as broader hypoxia-stress response — heterogeneous biology.
- Single signature for all tissues / cell types.

## Open problems

- Cell-type-specific Hallmark Hypoxia refinements via single-cell data.

## Relevance to active research

The MSigDB Hallmark Hypoxia 200-gene set is the input signature for both AddModuleScore and AUCell hypoxia scoring in [[papers/development-hypoxia-responsive-macrophage-prognostic-model]], and the basis of ssGSEA tumour hypoxia microenvironment scores in TCGA-PAAD.
