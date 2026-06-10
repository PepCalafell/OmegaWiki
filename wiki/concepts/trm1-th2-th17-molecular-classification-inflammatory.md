---
title: "Trm1 TH2/TH17 molecular classification of inflammatory skin disease"
aliases:
  - RashX TH2/TH17 framework
  - Trm1 disease-specific signature classification
tags: [immunology, skin, scrna-seq, classification, atopic-dermatitis, psoriasis, trm]
maturity: active
key_papers:
  - classification-human-chronic-inflammatory-skin-disease
first_introduced: "Liu et al. 2022, Science Immunology"
date_updated: 2026-06-10
related_concepts: [tissue-resident-memory-cd8-t-cell-trm, treg-trm-expansion-cd8-exhaustion-chronic, molecular-stratification-indeterminate-rash-predicts-dupilumab]
---

## Definition

A framework for classifying chronic inflammatory skin disease at the molecular level using disease-specific differentially expressed gene (DEG) signatures derived from the Trm1 skin-resident memory T cell cluster. Atopic dermatitis (AD) is characterized by a TH2-skewed signature and psoriasis vulgaris (PV) by a TH17-skewed signature; gene-set module scores along these two axes place any sample on an AD↔PV continuum.

## Intuition

Bulk profiling conflates cell types and fails to reproducibly distinguish AD from PV. By isolating the Trm1 population — which harbors the largest number of conserved disease-discriminating DEGs — and scoring AD- and PV-specific gene modules, individual patient samples segregate cleanly into TH2- vs TH17-biased classes regardless of histopathologic ambiguity.

## Formal notation

Per sample, compute aggregate gene-set scores S_AD and S_PV over Trm1 cells (Seurat AddModuleScore); samples are positioned in the (S_AD, S_PV) hyperdimensional plane and assigned by proximity (Canberra distance) to the AD or PV centroid, with significance by one-sided Mann-Whitney test.

## Variants

- Heatmap representation of avg_log2FC for AD- and PV-specific genes per sample.
- Hyperdimensionality (hull-plot) representation along the two-axis TH2/TH17 plane.

## Comparison

Unlike reference-projection atlas classifiers (e.g. [[patient-classification-reference-embedding-projection]]), this approach relies on a curated cell-type-restricted DEG signature rather than whole-transcriptome embedding similarity.

## When to use

When molecularly endotyping an adult inflammatory rash whose clinical/histopathologic diagnosis is ambiguous, especially to inform TH2- vs TH17-targeted biologic therapy.

## Known limitations

- Restricted to the Trm1 population; underpowered for APC-driven signals.
- Validated on small cohorts (this study plus the Reynolds et al. external set).

## Open problems

- Whether the two-axis TH2/TH17 model generalizes to rashes outside the AD-PV-BP-LP spectrum.

## Key papers

- [[papers/classification-human-chronic-inflammatory-skin-disease]] — introduces the Trm1 TH2/TH17 classification and the RashX portal.

## My understanding

This is a concrete, deployable instance of molecular endotyping for dermatology: the value is less in a new algorithm than in showing that a single cell-type-restricted signature recovers patient-level disease class and tracks drug response.
