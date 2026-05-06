---
title: "Hypoxia-driven genomic instability (PGA)"
aliases:
  - "hypoxia-driven genomic instability"
  - "PGA"
  - "percent genome altered"
  - "percentage genome altered"
  - "CNA burden"
  - "copy-number burden"
  - "chromosomal instability under hypoxia"
  - "hypoxia-CIN association"
  - "hypoxia-mutation rate link"
  - "tumor mutational burden under hypoxia"
tags:
  - hypoxia
  - genomic-instability
  - PGA
  - CNA
  - DNA-repair
  - cancer
  - prognostic
maturity: stable
key_papers:
  - molecular-landmarks-tumor-hypoxia-across-cancer
first_introduced: "Bristow & Hill 2008 Nat Rev Cancer (review); Luoto et al. 2013 Genome Integr (PCa); Bhandari 2019 (pancancer)"
date_updated: 2026-05-06
related_concepts: []
---

## Definition

Hypoxia-driven genomic instability is the empirical association between elevated tumor hypoxia and elevated genomic instability — most commonly quantified as the percentage of the genome altered by copy-number aberrations (PGA). Mechanistically supported by hypoxic downregulation of homologous recombination (RAD51), mismatch repair (MLH1, MSH2), and apoptosis-deficient subclonal selection, this association holds in 10 of 19 tumor types in pancancer analyses ([[papers/molecular-landmarks-tumor-hypoxia-across-cancer]]) and is never inverted (no tumor type shows hypoxia → reduced PGA).

## Intuition

Cells in hypoxic niches are under metabolic stress, replication stress, and oxidative damage simultaneously, while their DNA-repair machinery is partially shut down. The combination is mutagenic. Over time, hypoxic tumor regions accumulate more mutations and CNAs than normoxic ones. Selection for apoptosis-deficient subclones (mutant TP53, PTEN loss) further amplifies this, because hypoxia would normally trigger p53-mediated apoptosis and weed out unstable cells.

## Formal notation

- PGA per sample: fraction of the genome with copy-number gain or loss vs diploid baseline
- Pancancer hypoxia-PGA correlation (Spearman ρ): ranges from negligible (THCA, OV, BLCA) to strong (BRCA ρ≈0.4, PAAD ρ≈0.4, PRAD ρ≈0.3)
- Significant in 10/19 tumor types (Bonferroni-adjusted P<0.05)
- Mechanistic supporting evidence: hypoxia downregulates RAD51 (Bindra 2004), MLH1 / MSH2 (Mihaylova 2003, Koshiji 2005); HIF-1α → mismatch-repair deficit
- In localized PCa specifically: hypoxia ↔ PGA Bonferroni P=3.55×10⁻⁵, ρ=0.24

## Variants

- SNV burden under hypoxia: in PCa, total SNV burden Bonferroni P=2.52×10⁻², ρ=0.26 ([[papers/molecular-landmarks-tumor-hypoxia-across-cancer]])
- Chromothripsis under hypoxia: catastrophic SV events Bonferroni P=2.69×10⁻²
- Mitochondrial mutations under hypoxia: P=0.048 (Kruskal-Wallis)
- Pediatric tumors: hypoxia-PGA association is open (no large-scale data)

## Comparison

| Genomic-instability measure | Source | Pancancer power |
|---|---|---|
| PGA (CNA burden) | SNP6 / WGS-based copy-number | ★★★★ (TCGA-scale) |
| TMB (SNV burden) | WES / WGS | ★★★ |
| Chromothripsis events | WGS structural variants | ★★ |
| Mutational signatures (SBS) | WGS | ★★★ |
| Telomere length variability | WGS / TelSeq | ★★ |

## When to use

- Discovery: linking microenvironment (hypoxia) to genomic features
- Risk stratification: hypoxia + high PGA is a prognostic combination
- Therapeutic selection: hypoxia + genomic instability are co-criteria for hypoxia-targeting + PARP/DDR-inhibitor combinations
- NOT for absolute mechanistic causality — correlative evidence only

## Known limitations

- Bulk-tumor PGA depends on purity and ploidy estimation
- Some tumor types (THCA, OV) show no hypoxia-PGA link, indicating the mechanism is not universal
- Hypoxia signatures and PGA may be jointly driven by a third factor (e.g., MYC amplification)
- Direct causation requires longitudinal or in vivo modelling

## Open problems

- Why hypoxia-PGA fails to associate in 9/19 tumor types — tumor-type-specific DNA-repair compensations?
- Can hypoxia + genomic instability be used to select tumors most likely to benefit from PARP inhibitors?
- The role of immune editing in shaping hypoxia-PGA in vivo

## Key papers

- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — pancancer demonstration in 10/19 tumor types

## My understanding

This is the cleanest statement of "hypoxia → genomic instability" at scale. It motivates clinical trials selecting on hypoxia + DDR-deficiency, and it grounds the mechanistic link Bristow & Hill formulated. For HypoxiaVERSE, the association supports treating hypoxia as a *causal* shaper of the tumor genome (rather than a passive biomarker), which has direct implications for how we think about hypoxic tumor microenvironment evolution.
