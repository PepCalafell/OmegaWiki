---
title: "Epithelial-proinflammatory niche (IL1B-high macrophage / IL1R1-high KAC) in LUAD precursors"
aliases:
  - epithelial-proinflammatory niche
  - IL1B-IL1R1 niche
  - IL1B macrophage KAC niche
  - proinflammatory KAC niche
  - precursor lesion inflammatory niche
  - IL-1β IL-1R1 spatial niche
  - C15/C4 IL1B+ macrophage niche
  - stage-specific proinflammatory niche
  - epithelial-immune precancer niche
  - AAH-AIS proinflammatory microenvironment
  - tumor-initiating spatial field effect
  - alveolar progenitor inflammatory niche
tags:
  - lung
  - luad
  - precursor
  - tme
  - macrophage
  - inflammation
  - niche
  - spatial
maturity: emerging
key_papers:
  - multimodal-spatial-omics-reveal-co-evolution
first_introduced: "2026"
date_updated: 2026-05-26
related_concepts:
  - kac-krt8-alveolar-intermediate-cells-luad-progenitors
  - field-cancerization-clonal-expansion-normal-tissue
---

## Definition

A spatially resolved tissue niche in human and mouse lung precursor lesions (AAH, AIS) consisting of IL1R1-high epithelial KAC/RPII cells juxtaposed with IL1B-high pro-inflammatory macrophages (Xenium C15 / TMA C4 subclusters), accompanied by inflammatory CAFs (iCAFs), CCL2⁺/IL18⁺/CSF1⁺/NFKB1⁺ immune subsets, and elevated NF-κB / interferon signatures.

## Intuition

The niche is **stage-specific**: prevalent in early precursor lesions (AAH, AIS) and *decreases* as lesions progress to MIA/LUAD. This inverts the usual "more inflammation = more advanced cancer" intuition and reframes early inflammation as a tumor-initiating spatial field effect rather than a late immunosuppressive feature.

## Comparison

- Distinct from late TAM-rich immunosuppressive niches (e.g., SPP1⁺/TREM2⁺) reported in invasive NSCLC ([[papers/tumour-microenvironment-crosstalk-nsclc-progression-response]]).
- Distinct from injury-resolution KRT8⁺ intermediates in pulmonary fibrosis, although they share IL-1-driven maintenance signals.
- Stronger in KRAS-mutant precursors (100% IL1B-IL1R1 LR enrichment) than in KRAS WT.

## Key papers

- [[papers/multimodal-spatial-omics-reveal-co-evolution]] — defines the niche by Visium ST (56 lesions), Xenium 5K Prime (4.6M cells), and a 188-core TMA (593K cells), and functionally validates it via Il1r1 KO and anti-IL-1β±anti-PD-1 in NNK-exposed Gprc5a−/− mice.

## When to use

- Designing precancer interception strategies: anti-IL-1β is mechanistically active here and not in established LUAD.
- Interpreting CANTOS vs CANOPY discordance: CANTOS (atherosclerosis cohort, healthier lungs) likely intercepted precancerous niches; CANOPY trials in invasive NSCLC targeted a niche state that had already dissipated.

## Open problems

- Are these niches reversible by inflammation resolution agents (e.g., resolvins) rather than blockade?
- Which precursor lesions carry an active niche versus a resolved one, and can imaging (IL1R1 IF) stratify them?
- Does similar stage-specific niche logic apply to other organ precancers (PanIN, BE, AAH-like states elsewhere)?
