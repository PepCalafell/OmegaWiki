---
title: "Organism-wide multi-tissue perturbation profiling"
aliases:
  - organism-wide profiling
  - multi-tissue perturbation RNA-seq
  - whole-organism RNA-seq screen
  - 13-tissue profiling sepsis
  - cross-organ perturbation atlas
  - systemic perturbation profiling
  - mouse-wide tissue transcriptomics
  - organism-level perturbation screen
  - multi-organ time-series RNA-seq
tags:
  - organism-wide
  - multi-tissue
  - perturbation
  - bulk-RNA-seq
  - sepsis
maturity: active
key_papers:
  - pairwise-cytokine-code-explains-organism-wide
first_introduced: "2017"
date_updated: 2026-05-22
related_concepts:
  - pairwise-cytokine-code-sepsis
  - cell-type-abundance-from-bulk-tissue-rnaseq
---

## Definition

An experimental design that profiles many tissues (≥10) per mouse across many perturbation conditions and time points, using a scalable bulk-RNA-seq protocol (PME-seq), to map systemic effects of disease, vaccination or cytokine perturbations at organ resolution.

## Intuition

Single-tissue or single-cell deep dives miss inter-organ coordination. Organism-wide bulk profiling captures the systemic structure that defines diseases such as sepsis, vaccination response, or cytokine storms, and provides a denominator against which mechanistic single-cell experiments can be sited.

## When to use

Use when the biological question is fundamentally systemic (sepsis, vaccination, fasting, infection) and when local mechanism is secondary to mapping cross-organ structure first.

## Key papers

- [[papers/pairwise-cytokine-code-explains-organism-wide]]

## My understanding

The methodological foundation enabling the pairwise-cytokine result: without 13-tissue × 6-timepoint × 21-cytokine-condition coverage, the pairwise code would not have been discoverable.
