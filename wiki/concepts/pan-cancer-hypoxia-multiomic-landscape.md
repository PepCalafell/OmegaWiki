---
title: "Pan-cancer multidimensional hypoxia-associated molecular landscape"
aliases:
  - "hypoxia-associated molecular features"
  - "multidimensional hypoxia molecular signatures"
tags:
  - hypoxia
  - pancancer
  - multi-omics
  - TCGA
  - cancer-genomics
maturity: emerging
key_papers:
  - characterization-hypoxia-associated-molecular-features-aid
first_introduced: "Ye et al. 2019, Nature Metabolism"
date_updated: 2026-06-02
related_concepts: []
---

## Definition

The pan-cancer multidimensional hypoxia-associated molecular landscape is the systematic catalogue of molecular alterations — across mRNA, miRNA, and protein expression, DNA methylation, somatic mutations, and somatic copy number alterations (SCNAs) — that distinguish hypoxia score-high from hypoxia score-low tumours within and across cancer types. It treats tumour hypoxia status (inferred from an mRNA signature) as the comparison axis and quantifies, per cancer type and per omic layer, which features are significantly biased by hypoxia after confounder adjustment.

## Intuition

Hypoxia is one of the most pervasive tumour microenvironmental stresses, touching metabolism, angiogenesis, apoptosis, EMT, and immune evasion. Rather than studying one layer at a time, this concept integrates six molecular layers over a large pan-cancer cohort (TCGA), producing a "map" of how the hypoxic state remodels the cancer genome, epigenome, transcriptome, and proteome. The map is explicitly *relative and cancer-type-aware*: the same hypoxic state produces very different alteration burdens in different tumours.

## Formal notation

For each cancer type *c* and molecular feature *f*, compute a confounder-balanced differential statistic between hypoxia score-high and score-low groups; *f* is "hypoxia-associated in *c*" if it passes layer-specific FDR thresholds and permutation control.

## Variants

- Single-layer hypoxia signatures (mRNA-only) — a degenerate case of this multi-layer landscape.
- Genomic-instability-centred pan-cancer hypoxia maps (e.g. [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]]).

## Comparison

Complements [[concepts/tumor-hypoxia-mrna-signature]] (which provides the classification axis) by adding the downstream multi-omic consequences and their drug-response links.

## When to use

When the goal is to understand the breadth of molecular reprogramming under hypoxia across many cancer types, or to nominate hypoxia-associated, therapeutically relevant features.

## Known limitations

- Bulk-tissue resolution; does not capture intratumoral or stromal/immune heterogeneity.
- Association-level; direct causal attribution to hypoxia is limited.

## Open problems

- Single-cell / spatial extension of the landscape.
- Distinguishing hypoxia-driven from hypoxia-correlated alterations.

## Key papers

- [[papers/characterization-hypoxia-associated-molecular-features-aid]] — defines the six-layer pan-cancer landscape across 21 cancer types.

## My understanding

This is the organising contribution of Ye et al.: not a single biomarker but a confounder-controlled, multi-omic atlas of what hypoxia does to tumours, framed to inform combination and hypoxia-targeted therapy.
