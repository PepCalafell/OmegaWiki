---
title: "The burden of hypoxia-associated multi-omic alterations varies markedly across cancer types and molecular layers"
slug: hypoxia-molecular-alteration-burden-varies-by-cancer
status: supported
confidence: 0.85
tags:
  - hypoxia
  - multi-omics
  - pancancer
  - heterogeneity
  - TCGA
domain: "oncology / cancer-genomics / hypoxia"
source_papers:
  - characterization-hypoxia-associated-molecular-features-aid
evidence:
  - source: characterization-hypoxia-associated-molecular-features-aid
    type: supports
    strength: strong
    detail: "Hypoxia-associated mRNA alterations ranged from 399 genes (OV) to 4,795 (TGCT); miRNA from 2 (SKCM) to 213 (THYM). Quote (p.434): 'STAD had many hypoxia-associated features in six molecular layers, including 4,169 mRNAs, 186 miRNAs, 91 proteins, 294 methylation probes, 1 gene mutation and 10 SCNAs, while glioblastoma multiforme (GBM) had hypoxia-associated features in 629 mRNAs and 5 proteins.'"
conditions: "Six molecular layers compared: mRNA (~20,000 genes), protein (~200), miRNA (~2,000), DNA methylation (~16,000 genes), highly mutated genes (>5% frequency), and SCNAs (GISTIC2.0). FDR<0.05."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

The number and distribution of hypoxia-associated molecular features differ dramatically between cancer types and between omic layers — from hundreds to thousands of mRNA changes, and from a handful to hundreds of miRNA changes — implying that hypoxia-targeted therapy response will be cancer-type specific.

## Evidence summary

- [[papers/characterization-hypoxia-associated-molecular-features-aid]] — six-layer feature counts per cancer type (Fig. 3b).

## Conditions and scope

- Counts depend on per-layer significance thresholds and propensity-score balancing.

## Counter-evidence

- Feature counts partly reflect data availability and sample size per cancer type.

## Linked ideas

(none yet)

## Open questions

- How much of the cross-cancer variation reflects biology vs. statistical power?
