---
title: "Single-state vs multi-state TF classification"
aliases:
  - "single-state TF"
  - "multi-state TF"
  - "state-selective TF"
  - "cell-state-specific TF"
  - "TF state selectivity"
  - "TEXterm single-state TF"
  - "TRM single-state TF"
  - "TF specificity score"
  - "state-defining TF"
tags: [methods, transcription-factor, immunology, t-cell-engineering]
maturity: emerging
key_papers: [atlas-guided-discovery-transcription-factors-cell]
first_introduced: "2025"
date_updated: 2026-05-22
related_concepts: [taiji-tf-activity-pipeline, cd8-t-cell-exhaustion-texterm, tissue-resident-memory-cd8-t-cell-trm]
---

## Definition

Classification of TFs by the breadth of cell states in which their activity is statistically enriched, as inferred by Taiji PageRank: **single-state TFs** are predominantly active in one cell state; **multi-state TFs** are active in two or more. Among CD8+ T cells, the framework yields TEXterm single-state TFs (e.g. ZSCAN20, JDP2, ZFP324), TRM single-state TFs (e.g. KLF6, FOSB, JUNB), and multi-state TFs shared by TEXterm and TRM (e.g. HIC1, GFI1, PRDM1, BHLHE40, NR4A2).

## Intuition

Two states with overlapping transcriptomes (TEXterm vs TRM) may still have **disjoint** TF activity fingerprints. Targeting a single-state TF should perturb only its host state, while targeting a multi-state TF perturbs both states.

## When to use

For designing genetic interventions that selectively shape T cell fate (e.g. CAR-T or TIL engineering) without compromising protective parallel programmes.

## Known limitations

Classification depends on the chosen statistical threshold; near-threshold TFs (e.g. Eomes, classified single-state for TEXterm despite known TEM/TCM/TRM roles) are misclassified. Cross-species generalization is partial — only 19/34 TEXterm single-state TFs in mouse retain conserved activity in human.

## Key papers

- [[atlas-guided-discovery-transcription-factors-cell]] — Chung et al. 2025: introduces the systematic single-state/multi-state framework on a 9-state CD8+ atlas.
