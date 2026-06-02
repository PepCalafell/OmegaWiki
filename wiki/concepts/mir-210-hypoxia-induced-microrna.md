---
title: "miR-210 hypoxia-induced microRNA"
aliases:
  - "miR-210"
  - "miR-210-3p"
  - "hypoxamir"
  - "the hypoxamir"
  - "hypoxia-induced microRNA"
  - "canonical hypoxia microRNA"
  - "HIF1A-target microRNA"
  - "hypoxia-responsive miRNA"
  - "oxygen-responsive miRNA"
  - "MIR210"
tags:
  - hypoxia
  - microRNA
  - HIF1A
  - cancer
  - mitochondria
  - non-coding-RNA
  - biomarker
maturity: stable
key_papers:
  - molecular-landmarks-tumor-hypoxia-across-cancer
  - hypoxic-microenvironment-cancer-molecular-mechanisms-therapeutic
  - characterization-hypoxia-associated-molecular-features-aid
first_introduced: "Kulshreshtha et al. 2007 Mol Cell Biol; Camps et al. 2008 Clin Cancer Res; Huang et al. 2009 Mol Cell"
date_updated: 2026-05-06
related_concepts: []
---

## Definition

miR-210 is the canonical "hypoxamir" — the most consistently and strongly induced microRNA under hypoxia across cell types and tumor types. Direct HIF1A binding at the MIR210 promoter induces miR-210 5–50× under low oxygen. Its mature -3p strand targets electron-transport-chain (ISCU, COX10, SDHD) and DNA-damage response (RAD52) transcripts, contributing to hypoxic metabolic remodelling and the Warburg-like glycolytic shift.

## Intuition

If a single molecular feature were chosen as "this cell has been in hypoxia recently," miR-210 abundance would be it. The hypoxic induction is so robust and reproducible that miR-210 is the default positive control for any hypoxia experiment, and miR-210 abundance is positively correlated with tumor hypoxia score in 18 of 19 tumor types pancancer ([[papers/molecular-landmarks-tumor-hypoxia-across-cancer]], Spearman ρ range 0.20–0.66).

## Formal notation

- Pancancer correlation: miR-210 vs hypoxia score, Spearman ρ ∈ [0.20, 0.66] across 18 of 19 TCGA tumor types
- Mechanism: HIF1A → MIR210 promoter HRE → pri-miR-210 → mature miR-210-3p
- Downstream targets: ISCU (iron-sulfur cluster scaffold), COX10 (Complex IV), SDHD (Complex II), RAD52 (DSB repair)
- Functional readout: miR-210 high → reduced electron transport, increased glycolysis (LDHA correlates: BRCA ρ=0.72)

## Variants

- miR-210-5p (passenger strand): minor expression, distinct targets
- MIR210HG (host gene): itself hypoxia-induced
- Circulating miR-210: explored as plasma biomarker for hypoxia / breast cancer

## Comparison

| Hypoxia marker | Universality | Quantitation | Throughput |
|---|---|---|---|
| miR-210 | 18/19 cancer types | qPCR, sequencing | high |
| HIF1A target signature | tumor-type specific tuning | mRNA-seq | high |
| Pimonidazole IHC | direct, gold standard | IHC scoring | low |
| Eppendorf needle | gold standard | mmHg | very low |

## When to use

- Confirmatory hypoxia readout in any RNA-seq / miRNA-seq cohort
- Cross-platform validation of mRNA hypoxia signature
- Plasma / non-invasive hypoxia surrogate (with caveats on assay variability)
- Bridge between miRNA layer and HIF1A-driven metabolic program

## Known limitations

- Bulk-tumor miR-210 mixes malignant and stromal contributions
- Direction of miR-210 effect is context-dependent (pro-survival in mild hypoxia, pro-apoptotic in severe hypoxia + reoxygenation)
- Plasma miR-210 assays vary across platforms; not yet clinical-grade

## Open problems

- Whether miR-210-mediated mitochondrial repression *causes* the Warburg shift or amplifies a HIF1A-driven program is debated.
- Therapeutic targeting of miR-210 (anti-miR strategies) has been explored preclinically with mixed results.
- Single-cell resolution of miR-210 in tumor vs stromal compartments remains underexplored.

## Key papers

- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — pancancer miR-210 hypoxia correlation in 18/19 tumor types; miR-210 ↔ LDHA protein (BRCA ρ=0.72; OV ρ=0.42)

## My understanding

miR-210 is the workhorse "you've been in hypoxia" marker. For HypoxiaVERSE, miR-210 is a useful orthogonal validator alongside the mRNA Buffa signature. Future work should examine whether miR-210 induction in immune cells (macrophages, T cells) under hypoxia is at the same magnitude as in tumor epithelium — single-cell hypoxia studies have not yet systematically resolved this.
