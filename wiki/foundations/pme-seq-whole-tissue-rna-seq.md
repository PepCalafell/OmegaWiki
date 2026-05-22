---
title: "PME-seq — whole-tissue RNA-seq toolkit"
slug: pme-seq-whole-tissue-rna-seq
domain: genomics / bulk transcriptomics
status: mainstream
aliases:
  - PME-seq
  - PMEseq
  - whole-tissue RNA-seq
  - organism-wide RNA-seq
  - bulk tissue RNA-seq Pandey 2020
  - tissue-level transcriptomics
  - multi-organ bulk RNA-seq
  - Chevrier-lab whole-tissue protocol
first_introduced: "2020"
date_updated: 2026-05-22
source_url: "https://doi.org/10.1038/s41596-019-0286-8"
---

## Definition

PME-seq (Pandey et al., Nat Protoc 2020) is a low-input, multi-organ whole-tissue RNA-seq workflow combining mechanical homogenization, on-column poly(A) capture and bead-based library prep, optimized for parallel profiling of many tissues from each mouse.

## Intuition

PME-seq was designed for organism-wide perturbation studies in which the unit of measurement is the whole tissue, not dissociated single cells — preserving stromal and rare-cell-type transcripts that are lost in scRNA-seq, at the cost of cell-type resolution which is then recovered computationally.

## Relevance to active research

PME-seq underlies Takahama et al. 2024's organism-wide LPS/CLP time course and the cytokine-pair screen (13 organs × 6 single + 15 paired cytokine conditions), demonstrating its scalability for cross-tissue perturbation biology.
