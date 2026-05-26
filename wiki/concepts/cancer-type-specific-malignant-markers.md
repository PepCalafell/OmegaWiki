---
title: "Cancer-type-specific malignant marker genes"
aliases:
  - cancer-type-specific malignant marker
  - tumor lineage marker
  - tissue-specific malignant marker
  - malignant cell marker gene
  - cancer-type marker scRNA-seq
  - context-dependent malignant gene
  - tumor type biomarker scRNA-seq
  - PMEL melanoma marker
  - KLK3 prostate marker
  - ESR1 breast marker
  - CDKN2A HPV HNSCC marker
  - ANKRD30A breast marker
  - APOA2 liver marker
tags: [scrna-seq, biomarkers, malignant, pan-cancer, marker-genes, oncology]
maturity: active
key_papers:
  - curated-cancer-cell-atlas-provides-comprehensive
first_introduced: "2025 (Tyler et al., 3CA v2)"
date_updated: 2026-05-26
related_concepts: [curated-cancer-cell-atlas-3ca, recurrent-malignant-metaprograms-nmf]
---

## Definition

Cancer-type-specific malignant markers are genes whose expression in malignant cells is highly enriched in a particular cancer type. Identified in 3CA v2 by ranking malignant-cell gene expression across cancer types and surfacing genes with strong cancer-type contrast.

## Examples (Tyler et al. 2025)

- **PMEL** — melanoma.
- **KLK3** (prostate-specific antigen) — prostate cancer.
- **ESR1** — breast cancer (reflecting ER+ tumour over-representation).
- **CDKN2A (p16)** — HPV+ HNSCC.
- **APOA2** — liver cancer (HCC, cholangiocarcinoma).
- **ANKRD30A** — breast cancer.
- **CHGA, ELAVL4, PCSK1N** — neuroendocrine and SCLC.
- **WT1** — Wilms tumour.
- **CLDN18** — gastric, PDAC.

## Intuition

Malignant cells differ enormously across cancer types because they retain tissue-of-origin lineage features and accumulate cancer-type-specific drivers. As a result, no pan-cancer malignant marker exists — instead, each cancer type has its own marker portfolio. This contrasts with TME cell types (T cells, macrophages, fibroblasts), where pan-cancer markers do exist.

## When to use

- Cell-of-origin annotation of clinically ambiguous tumours (Cancer-of-Unknown-Primary).
- Deconvolving mixed-cancer bulk RNA-seq.
- Building cell-type classifiers that are robust across cancer types.

## Known limitations

- Markers reflect dominant subtypes in 3CA (ER+ breast > ER−, HPV+ > HPV− HNSCC subsets), creating compositional bias.
- Some markers are co-expressed in adjacent normal epithelium → specificity to malignant cells per se can be modest.
- Cell-of-origin signal can confound malignancy-specific signal.

## Key papers

- [[curated-cancer-cell-atlas-provides-comprehensive]] — pan-cancer malignant marker catalogue with sensitivity/specificity scoring.

## My understanding

This is the malignant-cell analogue of the canonical TME-cell marker catalogues (LM22, panel-based markers) but cancer-type-resolved. The pragmatic value is in cell-type classifier training and CUP/deconvolution applications.
