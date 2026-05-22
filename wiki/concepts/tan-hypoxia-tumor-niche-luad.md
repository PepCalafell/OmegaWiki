---
title: "Tumor-associated neutrophil + hypoxia spatial niche in lung adenocarcinoma"
aliases:
  - TAN-hypoxia tumor niche
  - tumor-associated neutrophil hypoxia niche
  - TAN niche LUAD
  - hypoxic tumor neutrophil niche
  - TAN-EMT hypoxia state
  - hypoxia-neutrophil tumor niche
  - NDRG1+ VEGFA+ tumor cluster
  - C0 LUAD niche
  - C23 IMC neutrophil niche
  - hypoxic tumor-state spatial niche
  - TAN response-to-hypoxia colocalization
tags:
  - spatial-transcriptomics
  - tumor-microenvironment
  - hypoxia
  - lung-adenocarcinoma
  - neutrophil
  - prognostic-signature
maturity: emerging
key_papers:
  - cellcharter-reveals-spatial-cell-niches-associated
first_introduced: "Varrone et al. 2024 *Nat. Genet.* (CellCharter)"
date_updated: 2026-05-22
related_concepts:
  - "[[concepts/hypoxia-emt-lineage-plasticity-metastasis]]"
  - "[[concepts/tam-recruitment-hypoxic-niche-chemokines]]"
  - "[[concepts/cluster-neighborhood-enrichment-spatial]]"
---

## Definition

A spatial tumour-microenvironment niche in lung adenocarcinoma in which cancer cells expressing a response-to-hypoxia and EMT transcriptional state (NDRG1, VEGFA, CA9, S100A8/9, CXCL1/2/3) directly surround dense tumour-associated neutrophils. The niche is spatially segregated from proliferative tumour-cell states (MKI67, FGFR1/2, EZH2) within the same tumour.

## Intuition

Hypoxia within growing tumour islands drives HIF1α-dependent secretion of neutrophil-recruiting chemokines (S100A8/9, CXCL1/2/3); incoming neutrophils further reinforce inflammatory and EMT-promoting signalling. The result is a spatially compact, prognostically adverse niche that is detectable across multiple platforms (CosMx, MERFISH, IMC) and patient cohorts.

## Evidence

- LUAD CosMx (5 patients, 8 sections): two coexisting tumour-enriched clusters (C0, C12). C0 is NDRG1/VEGFA/S100A8-9/CXCL1-3-high and neighbours the neutrophil/NK cluster C11; C12 is MKI67/FGFR1-2/EZH2-high.
- LUAD MERFISH (2 samples, 500 markers): three tumour-enriched clusters; one (C5) interacts with neutrophil cluster C14 and has high response-to-hypoxia signature.
- LUAD IMC tissue microarray (416 cores, 35 markers): tumour cluster C23 (MPO+/HIF1A+) surrounds neutrophil cluster C7.
- Across 9 independent LUAD bulk-transcriptomic cohorts (TCGA-LUAD, Shedden, Schabath, Okayama, Der, Chen, Mezheyeuski, Ding, Tavernari): response-to-hypoxia signature correlates with TAN signature (Sorin 2023) but not NAN; both response-to-hypoxia and TAN signatures associate with worse overall survival in multivariate Cox regression while NAN does not.

## Known limitations

- All confirmatory cohorts are bulk transcriptomics — single-cell spatial validation is restricted to a handful of tumours (5 CosMx + 2 MERFISH + IMC TMA).
- TAN gene signature has its own validation history; cross-cohort signature transfer can confound the hypoxia–TAN correlation.
- Lack of CRISPR / genetic perturbation evidence that disrupting hypoxia–TAN coupling reverses prognosis.

## Open problems

- Therapeutic targetability — does HIF1α inhibition (PX-478, belzutifan) or CXCL1/2/3 blockade collapse the niche?
- Is this niche present across LUSC, KRAS-mutant vs EGFR-mutant tumours, or restricted to specific genotypes?
- Causal direction of the positive-feedback loop between tumour hypoxia and TAN recruitment.

## My understanding

This concept formalises a recurrent observation in lung-cancer TME biology and gives it a spatial-omics-derived definition. It connects [[concepts/hypoxia-emt-lineage-plasticity-metastasis]] and [[concepts/tam-recruitment-hypoxic-niche-chemokines]] to the operationally measurable readout of TAN + hypoxia signature colocalization in patient tissue.
