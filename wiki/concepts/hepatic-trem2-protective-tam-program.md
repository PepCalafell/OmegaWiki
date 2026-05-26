---
title: "Hepatic TREM2 protective TAM program"
aliases:
  - "hepatic TREM2 mac program"
  - "HCC TREM2 mac program"
  - "liver-specific TREM2 program"
  - "Hamon 2025 hepatic TREM2 program"
tags:
  - TREM2
  - HCC
  - tissue-specific
  - protective-TAM
  - liver
  - metallothionein
  - calreticulin
  - immune-checkpoint-blockade
maturity: emerging
key_papers:
  - trem2-macrophages-associated-enhanced-response-pd
first_introduced: "Hamon et al. 2025 (bioRxiv preprint)"
date_updated: 2026-05-26
related_concepts:
  - trem2-tumor-associated-macrophage
  - tissue-specific-tam-function-context-dependence
  - soluble-trem2-icb-response-biomarker
  - sirpa-cd47-don-t-eat-me-axis
---

## Definition

The liver-specific transcriptional program of TREM2 macs in HCC (209 liver-specific DEGs layered on a conserved 48-gene core), including metallothionein induction (MT1G, MT1H), calreticulin (CALR), and other features that distinguish hepatic TREM2 macs from lung/breast/ovarian TREM2 macs. Functionally associated with response to PD-1/PD-L1 blockade and improved overall survival in HCC.

## Intuition

A tissue-context refinement of the canonical pan-cancer TREM2 mac state ([[concepts/trem2-tumor-associated-macrophage]]) that flips the sign of the immunological output. The core TREM2 program is conserved; the liver-specific layer (anti-ferroptotic metallothioneins, pro-phagocytic CALR) appears to produce a protective output rather than an immunosuppressive one.

## Formal notation

- 209 liver-specific DEGs over the 48-gene conserved TREM2 core
- Defining tissue-specific upregulated genes: MT1G, MT1H, CALR
- Functional association: PD-1 blockade response + improved OS in HCC (IMbrave150)
- Spatial association: proximity to PD-1hi TCF1+ CD8, CXCL13+ Th, mregDCs in immune aggregates
- Serological correlate: elevated baseline serum sTREM2 in responders

## Variants

- Discovery-cohort cemiplimab HCC variant
- Validation-cohort cemiplimab+SBRT variant
- IMbrave150 atezolizumab+bevacizumab variant (transcriptional score)

## Comparison

vs pan-cancer TREM2 TAM ([[concepts/trem2-tumor-associated-macrophage]]): shares the core TREM2/GPNMB/SPP1/APOE/FABP5 program; differs in tissue-specific layer (MT1G/H, CALR vs CCL20/S100A10/SPP1 in lung).
vs NSCLC TREM2 mac (immunosuppressive, limits NK infiltration): opposite functional output despite shared core.

## When to use

When analysing HCC scRNA-seq mac landscape, when constructing predictive ICB signatures for HCC, or when comparing tissue-specific TREM2-mac programs across organ contexts.

## Known limitations

- Mechanistic causation of MT1G/H and CALR functional reversal not demonstrated.
- 209-gene tissue-specific set may include sample/dataset-batch artefacts.
- Cohorts are modest; signature requires prospective validation.

## Open problems

- Which subset of the 209 liver-specific genes is causally responsible for the protective phenotype?
- Does the program persist outside HCC (e.g., hepatic metastases of non-liver primaries)?
- Is the program reversible by chronic-inflammation context (NASH, fibrosis)?

## Key papers

- [[papers/trem2-macrophages-associated-enhanced-response-pd]] — defines and validates the hepatic TREM2 protective program; uses it to stratify IMbrave150 OS
