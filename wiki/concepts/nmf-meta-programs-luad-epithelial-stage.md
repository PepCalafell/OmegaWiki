---
title: "NMF meta-programs of LUAD epithelial cell states (MP1–MP11)"
aliases:
  - epithelial meta-programs LUAD
  - LUAD NMF MP
  - MP2-AT2 alveolar
  - MP5-AT1
  - MP6-tumor/KAC
  - MP7-inflammatory/stress
  - epithelial NMF cell states
  - LUAD transcriptional meta-program
  - precursor MP3
  - invasive MP9
  - pan-cancer NMF meta-program lineage
  - LUAD MP landscape staging
tags:
  - lung
  - luad
  - nmf
  - meta-program
  - cell-state
  - epithelial
maturity: emerging
key_papers:
  - multimodal-spatial-omics-reveal-co-evolution
first_introduced: "2026"
date_updated: 2026-05-26
related_concepts:
  - kac-krt8-alveolar-intermediate-cells-luad-progenitors
---

## Definition

A set of robust non-negative matrix factorization (NMF) meta-programs (MPs) derived from snRNA-seq (9 epithelial MPs) and from Visium ST (11 MPs) that capture transcriptional cell states along the normal-alveolar → KAC → precursor → invasive LUAD continuum.

## Key MPs

- **MP2 (AT2 alveolar)** — decreases progressively from normal to LUAD.
- **MP5 (AT1)** — decreases progressively.
- **MP6 (tumor/KAC)** — increases progressively, defines KAC-tumor identity.
- **MP7 (inflammatory/stress)** — co-expressed in RPII with MP2/MP6.
- **MP3 (precursor)** vs **MP9 (invasive)** (ST-derived) — discriminate precursor from invasive lesion spots.
- **MP4 (lymphoid)**, **MP5 ST (myeloid)**, **MP10 (normal alveolar)**, **MP11 (plasma)** — non-epithelial niche programs.

## Comparison

Correlated with pan-cancer NMF MPs from Gavish et al. 2023 ([[papers/curated-cancer-cell-atlas-provides-comprehensive]] / 3CA) and prior pan-cancer cell-state work, supporting both lineage (ciliated, AT2) and phenotype (inflammatory/stress) axes.

## When to use

For mapping a new lung lesion sample onto a stage continuum without histology, or for cross-referencing pan-cancer cell-state atlases to identify shared LUAD-relevant programs.

## Key papers

- [[papers/multimodal-spatial-omics-reveal-co-evolution]] — defines the 9 snRNA-seq and 11 ST MPs and their stage dynamics.
- [[papers/curated-cancer-cell-atlas-provides-comprehensive]] — provides pan-cancer MP backbone used for cross-correlation.
