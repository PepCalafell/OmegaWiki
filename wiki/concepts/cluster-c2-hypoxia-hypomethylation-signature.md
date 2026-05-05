---
title: "Cluster C2 hypoxia-hypomethylation signature"
aliases:
  - "C2 cluster"
  - "C2-associated CpGs"
  - "hypoxic activation hypomethylation cluster"
  - "C2 demethylation signature"
  - "NF-κB-bound hypomethylated CpGs"
  - "mMAC1-specific hypomethylation"
  - "hypoxic-LPS DNA methylation signature"
tags:
  - DNA-methylation
  - signature
  - epigenetics
  - hypoxia
  - macrophage
maturity: emerging
key_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
first_introduced: "Calafell-Segura/de la Calle-Fabregat 2024"
date_updated: 2026-05-05
related_concepts:
  - mmac1-hypoxic-inflammatory-macrophage
  - nf-kb-mediated-dna-demethylation-hypoxia
---

## Definition

A set of 403 differentially methylated CpG positions that are hypomethylated specifically in mature hypoxic LPS-activated MACs (mMAC1) compared with mature normoxic MACs (mMAC21). Identified on Illumina Infinium MethylationEPIC arrays with FDR<0.05 and |Δβ|>0.2.

## Intuition

C2 is the paper's "signature of paradox": a small island of hypomethylated CpGs in an otherwise methylation-frozen hypoxic genome. C2 sites mark NF-κB-bound enhancers of proinflammatory genes (IL6, TNF, NFKB1, CCL5, IRF1) that are *demethylated despite* the hypoxic suppression of TET activity.

## Formal notation

- 403 CpGs, hypomethylated in mMAC1 vs. mMAC21.
- Enriched in intergenic + open-sea regions; gain H3K4me1 + H3K27ac after LPS in normoxia (de novo enhancers).
- Highly enriched for NF-κB family motifs (HOMER).
- Exclusively associated with p65-specific ChIP-seq peaks (not HIF1α).
- C2-associated genes are significantly enriched in RNA-seq cluster E2 (Fisher's P=3.03×10⁻⁴⁴).
- BLCA: low-C2-methylation patients have better OS (HR=1.72, P=0.00589).

## Variants

- Sorted IL4I1 MACs from primary OC recapitulate the C2 hypomethylation pattern in vivo.
- TREM2 and FOLR2 MACs do *not* show C2 demethylation.

## Comparison

- Cluster C1 (2782 CpGs, hypomethylated in MAC differentiation, partially blocked by hypoxia) — the bulk-MAC-differentiation methylation program.
- Cluster C3 (903 CpGs, hypermethylated, RUNX/ETS motifs).
- C2 is the only one specific to hypoxic activation.

## When to use

As a methylation-based readout of hypoxic-inflammatory MAC presence. Predictive of T-cell infiltration in BLCA and likely useful as a prognostic biomarker in OC and other immune-hot tumors.

## Known limitations

- 403 CpGs is small; effect size and statistical power are modest in some downstream analyses.
- Defined on EPIC array CpG content; could miss bisulfite-untargeted regions (e.g., CpH, distal regulatory regions outside the array).
- Inferred causal mechanism (NF-κB → TET → demethylation) is supported by chemical perturbation but not by genetic loss-of-function.

## Open problems

- Whether the C2 signature persists epigenetically once hypoxia is relieved (memory / trained-immunity question).
- Tissue-of-origin specificity: does the same set of 403 CpGs apply outside MACs?
- Whether C2 expansion (more CpGs) defines a "stronger" mMAC1 phenotype or different in vivo subsets.

## Key papers

- [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] — defines and characterizes C2

## My understanding

C2 is more useful as a methylation-signature reagent than as a fundamental concept. For HypoxiaVERSE deconvolution and survival analysis, projecting C2 onto external methylation cohorts (TCGA, ovarian and bladder series) is one of the most actionable downstream uses.
