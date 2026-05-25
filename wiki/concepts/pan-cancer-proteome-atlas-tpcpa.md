---
title: "The Pan-Cancer Proteome Atlas (TPCPA)"
aliases:
  - TPCPA
  - Pan-Cancer Proteome Atlas
  - pan-cancer proteomics atlas
  - pan-cancer proteome landscape
  - DIA-MS pan-cancer atlas
  - cancer proteome atlas
  - multi-cancer proteome dataset
  - large-scale tumour proteomics
  - protein-level pan-cancer reference
  - pan-cancer DIA-MS dataset
  - mass-spectrometry cancer atlas
tags: [pan-cancer, proteomics, dia-ms, atlas, reference-dataset]
maturity: emerging
key_papers:
  - pan-cancer-proteome-atlas-mass-spectrometry
first_introduced: "Knol et al. 2025 Cancer Cell"
date_updated: 2026-05-25
related_concepts: []
---

## Definition
The Pan-Cancer Proteome Atlas (TPCPA) is a DIA-MS-based proteomic landscape quantifying 9,670 proteins across 999 primary tumor samples representing 22 cancer types (18 solid + 4 liquid). It serves as a protein-level analogue to large transcriptomic atlases such as TCGA and is accessed through an interactive R2-platform data portal.

## Intuition
Most prior pan-cancer protein resources (e.g., TMT-multiplexed CPTAC studies, RPPA panels) either restrict the protein set, the cancer-type coverage, or both. TPCPA uses single-shot data-independent acquisition mass spectrometry on bulk tissue to broaden coverage to >9,000 proteins on a uniform pipeline across many cancer types, enabling cross-tumour comparisons without TMT multiplexing constraints.

## Formal notation
- 999 primary tumour samples / 22 cancer types
- 11,250 protein groups identified, 9,670 quantified post-filtering
- ≥ 5 samples per cancer type, ≥ 30% data presence threshold
- HeLa QC controls anchor cross-batch comparisons

## Variants
- Standalone TPCPA dataset
- TPCPA in combination with external proteome datasets (CPTAC kidney, independent DIA breast)
- TPCPA + RNA reference cohorts (CRC CMS validation)

## Comparison
- vs **TCGA / ICGC**: TCGA is RNA/DNA; TPCPA is direct protein expression.
- vs **CPTAC**: CPTAC is multi-omic but TMT-based with per-tumour-type cohorts; TPCPA unifies many cancer types under one DIA-MS workflow.
- vs **RPPA atlases (TCPA)**: RPPA covers ~300 antibody targets; TPCPA covers ~10× more proteins.

## When to use
- Cancer-type-level protein biomarker discovery
- Validation of RNA-level pan-cancer signatures at the protein level
- Reference for cancer-of-unknown-primary (CUP) classifiers based on DIA-MS

## Known limitations
- Bulk tissue only; no cell-type resolution.
- Per-sample depth (~5,000–6,000) below modern fractionated workflows.
- Tissue-of-origin contributions confound malignancy-specific biology.

## Open problems
- Extension to metastatic and post-treatment tumours.
- Integration with single-cell / spatial proteomics.

## Key papers
- [[papers/pan-cancer-proteome-atlas-mass-spectrometry]]

## My understanding
TPCPA is the first large, uniform DIA-MS pan-cancer proteome and a likely reference dataset for protein-level cancer-type comparisons going forward. The decision to forgo TMT multiplexing trades depth for cross-cohort comparability, which is the right call for a pan-cancer resource.
