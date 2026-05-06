---
title: "miR-133a-3p hypoxia-modulated tumor suppressor in prostate cancer"
aliases:
  - "miR-133a-3p in prostate cancer"
  - "hypoxia-downregulated miR-133a"
  - "miR-133a tumor suppressor"
  - "miR-133a-BIN1 axis"
  - "miR-133a-PGM5 axis"
  - "PCa hypoxia miRNA"
  - "prostate-cancer hypoxia microRNA"
  - "miR-133a-3p validated hypoxia miRNA"
  - "hypoxia-suppressed miRNA"
tags:
  - microRNA
  - hypoxia
  - prostate-cancer
  - tumor-suppressor
  - BIN1
  - PGM5
  - MYC
  - miR-133a
maturity: emerging
key_papers:
  - molecular-landmarks-tumor-hypoxia-across-cancer
first_introduced: "Bhandari et al. 2019 Nat Genet (validation in PCa); prior tumor-suppressor reports in PCa from 2010s (Kojima, Tao)"
date_updated: 2026-05-06
related_concepts: []
---

## Definition

miR-133a-3p is a hypoxia-downregulated, tumor-suppressor microRNA in localized prostate cancer. Among 784 measured miRNAs in three independent PCa cohorts, miR-133a-3p emerged as the strongest *negative* hypoxia correlate (TCGA: FDR=2.08×10⁻¹¹, ρ=−0.40; CPC-GENE: FDR=4.83×10⁻³, ρ=−0.22; Taylor: FDR=1.17×10⁻², ρ=−0.26). Validation in PC3, DU145, 22Rv1 prostate cancer cell lines shows miR-133a-3p falls under 1% O₂ for 72h, and reintroducing a miR-133a-3p mimic decreases viability and PC3 invasion (P=5.45×10⁻³).

## Intuition

While miR-210 is the canonical "hypoxia goes up" microRNA, miR-133a-3p is the cleanest example of "hypoxia goes down" — and unlike many correlative miRNA findings, this one has both pancancer correlative validation across 3 cohorts and direct in vitro mimic-based functional rescue. The mechanism likely involves loss of restraint on BIN1, PGM5, and possibly MYC-pathway targets.

## Formal notation

- TCGA PRAD: ρ_Spearman(hypoxia, miR-133a-3p) = −0.40, FDR=2.08×10⁻¹¹, n=330
- CPC-GENE: ρ=−0.22, FDR=4.83×10⁻³, n=170
- Taylor: ρ=−0.26, FDR=1.17×10⁻², n=97
- In vitro hypoxic downregulation: 22Rv1 (P=5.73×10⁻³, t=−9.26), DU145 (P=5.02×10⁻², t=−3.87), PC3 (P=3.42×10⁻², t=−3.62)
- Mimic-rescue viability: 22Rv1 (P=3.69×10⁻³), DU145 (P=5.02×10⁻²), PC3 (P=1.50×10⁻²)
- Mimic-rescue PC3 invasion: P=5.45×10⁻³, t=2.78
- Validated correlated proteins (CPC-GENE): BIN1 (FDR=5.47×10⁻², ρ=0.55), PGM5 (FDR=5.47×10⁻², ρ=0.53), WDR33, LDB3, DCAF16, VPS18, PYGM, SNRNP40, ASAP2, SDPR

## Variants

- miR-133a-3p has two genomic loci (MIR133A1 chr18q11, MIR133A2 chr20q13.33), both producing identical mature -3p
- Pan-cancer dysregulation of miR-133a-3p has been reported in bladder, esophageal, colon cancers — but the prostate hypoxia link is the most rigorously validated
- miR-1 (myomiR cluster partner) shows similar but weaker hypoxia association

## Comparison

| miRNA | Hypoxia direction | Pancancer universality | In vitro validation in PCa |
|---|---|---|---|
| miR-210 | up in 18/19 | universal | not in this paper |
| miR-133a-3p | down in PCa | PCa-specific (top hit) | mimic decreases PC3 invasion |
| miR-30a | down in PCa | similar pattern | not validated |

## When to use

- Hypoxia readout in PCa specifically (complementary to miR-210)
- Hypothesis generation for tumor-suppressor microRNA therapy in hypoxic PCa
- Bridge between hypoxia and MYC-pathway / BIN1 axis

## Known limitations

- Two genomic loci complicate locus-specific KO experiments
- Validation in only 3 PCa cell lines and 3 retrospective cohorts; prospective mimic delivery in vivo not done in this paper
- Mechanism by which hypoxia downregulates miR-133a-3p (transcriptional vs processing vs stability) is uncharacterized

## Open problems

- Therapeutic potential of miR-133a-3p mimic delivery in hypoxic PCa
- Whether the miR-133a-3p–BIN1–MYC axis is the primary functional pathway, or whether pleiotropic targets dominate
- Tissue-specificity: muscle expression is high; how the prostate-tumor pool relates to muscle baseline is unclear

## Key papers

- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — primary discovery + 3-cohort validation + in vitro functional mimic rescue

## My understanding

This is one of the few hypoxia-modulated miRNA findings with the right balance of correlative scale (3 independent cohorts) and direct in vitro validation. It deserves follow-up as a candidate therapy in hypoxic PCa and as a node in the miRNA-target interactome for HypoxiaVERSE work. The miR-133a-3p–BIN1 axis is mechanistically plausible (BIN1 is a MYC suppressor; MYC gain co-occurs with hypoxia; reducing miR-133a-3p → loss of BIN1 → MYC unbridled) but needs direct mechanistic testing.
