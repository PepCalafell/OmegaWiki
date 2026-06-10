---
title: "CD8+ T cell exhaustion and the TEXterm state"
aliases:
  - "T cell exhaustion"
  - "TEX cells"
  - "TEXterm"
  - "terminally exhausted T cells"
  - "TEX terminal differentiation"
  - "exhausted CD8 T cells"
  - "PD1+ TIM3+ exhausted T cells"
  - "CD101+ exhausted T cells"
  - "chronic-stimulation T cell dysfunction"
  - "TEXprog progenitor exhausted T cells"
  - "TEXeff effector-like exhausted T cells"
  - "exhaustion trajectory"
tags: [immunology, cd8-t-cells, exhaustion, cancer-immunotherapy, chronic-infection]
maturity: active
key_papers: [atlas-guided-discovery-transcription-factors-cell, classification-human-chronic-inflammatory-skin-disease]
first_introduced: ""
date_updated: 2026-05-22
related_concepts: [tissue-resident-memory-cd8-t-cell-trm]
---

## Definition

CD8+ T cell exhaustion is the progressive loss of effector function and memory potential that occurs under persistent antigenic stimulation (chronic viral infection or solid tumours). The trajectory comprises three canonical states: TEXprog (TCF7+ SLAMF6+ progenitor), TEXeff (CX3CR1+ effector-like), and TEXterm (TIM3+ CD101+ CD39+ terminally exhausted). TEXterm cells express high inhibitory receptors, lack proliferative capacity, and respond poorly to immune checkpoint blockade.

## Intuition

Exhaustion is the cell-fate counterpart of memory: same antigen receptors, opposite functional destination. TEXterm cells share a tissue-resident topology and many TFs with TRM cells, but their TF networks reroute pathways from protective ones (TGFβ response, cell adhesion) to dysfunctional ones (proteasome catabolism, intrinsic apoptosis).

## Variants

- **TEXprog** — PD1+SLAMF6+CX3CR1− TCF7+: progenitor-like, multipotent, sustains the TEX pool and responds to PD1 blockade.
- **TEXeff** — PD1+CX3CR1+: transient effector-like state.
- **TEXterm** — PD1+SLAMF6−CX3CR1− TIM3+ CD101+ CD39+: terminal dysfunctional state.

## When to use

Apply this framework when modelling chronic antigen exposure (chronic LCMV, HIV, HBV, tumour TILs) and when interpreting ICB response heterogeneity.

## Known limitations

TF activity overlaps strongly with the protective TRM state, so transcriptional signatures alone cannot distinguish them — TF activity inference (Taiji/PageRank) on paired RNA-seq + ATAC-seq is required.

## Key papers

- [[atlas-guided-discovery-transcription-factors-cell]] — Chung et al. 2025: TEXterm-selective TFs (ZSCAN20, JDP2, ZFP324) identified by atlas-guided in vivo Perturb-seq.

## Open problems

- Which TEXterm-selective TFs are druggable in CAR-T or TIL therapy?
- Can KO of TEXterm-selective TFs preserve TRM formation in solid tumours, not only in viral models?
