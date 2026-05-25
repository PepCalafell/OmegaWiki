---
title: "High hypoxia score correlates with higher tumor mutational burden in TCGA-PAAD (Pearson r=0.28, p<0.001)"
slug: high-hypoxia-score-correlates-tmb-pdac
status: supported
confidence: 0.7
tags: [hypoxia,PDAC,TMB,mutation-rate,TCGA-PAAD,genomic-instability]
domain: oncology-hypoxia
source_papers:
  - development-hypoxia-responsive-macrophage-prognostic-model
evidence:
  - source: development-hypoxia-responsive-macrophage-prognostic-model
    type: supports
    strength: medium
    detail: "Quote (p.9, Results): 'the high hypoxia group harbored a remarkably greater tumor mutational burden (TMB) than the low hypoxia group (Fig 5F), and the hypoxia score was positively correlated with TMB, with a correlation coefficient of 0.28 and a statistically significant level (P < 0.001), as illustrated in Fig 5G'. Overall mutation rate 90.28% (high) vs 78.87% (low). Top mutated genes shared across groups: KRAS, TP53, CDKN2A, SMAD4, TTN."
conditions: "TCGA-PAAD bulk cohort, n≈159; TMB computed via maftools; CNV via GISTIC 2.0. Correlation is modest (r=0.28) — explains <10% of TMB variance."
date_proposed: 2026-05-25
date_updated: 2026-05-25
---

## Statement

In TCGA-PAAD, patients in the high-hypoxia group (defined by median-split of the 13-gene hypoxia score) show a higher overall mutation rate (90.28% vs 78.87%) and higher TMB than the low-hypoxia group. Pearson correlation between continuous hypoxia score and TMB is r=0.28 (p<0.001). The top five mutated genes (KRAS, TP53, CDKN2A, SMAD4, TTN) are shared between groups. CNV gains are also enriched in the high-hypoxia group.

## Evidence summary

Reported in [[papers/development-hypoxia-responsive-macrophage-prognostic-model]] (Ge et al., *PLoS One* 2025, Fig 5C–G).

## Conditions and scope

- Single cohort (TCGA-PAAD); no external replication of the hypoxia–TMB correlation.
- The correlation is modest (r=0.28). The 90.28% vs 78.87% mutation-rate gap is largely driven by passenger mutations in TTN and other long genes.
- Compatible with broader literature on hypoxia-induced genomic instability in other cancer types ([[concepts/hypoxia-induced-mutator-phenotype]], [[concepts/hypoxia-genomic-instability-pga]]) but does not establish causality.

## Counter-evidence

None within paper scope.

## Linked ideas

## Open questions

- Is hypoxia *causing* increased mutation accumulation in PDAC (mutator phenotype), or is high hypoxia score itself a downstream consequence of clones with higher TMB?
- Does the hypoxia–TMB correlation hold within KRAS-mutant subgroups, or is it confounded by KRAS allele identity?
