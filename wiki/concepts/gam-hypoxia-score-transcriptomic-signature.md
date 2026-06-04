---
title: "GAM hypoxia score — cell-type-specific hypoxic TAM signature"
aliases: []
tags: [hypoxia-signature, glioma-associated-macrophages, scRNA-seq, gene-signature, tumor-microenvironment]
maturity: emerging
key_papers:
  - hypoxic-stress-dysregulates-functions-glioma-associated
first_introduced: "2025"
date_updated: 2026-06-04
related_concepts: [tumor-hypoxia-mrna-signature, hypoxia-confounds-gam-subtype-marker-classification, tam-recruitment-hypoxic-niche-chemokines]
---

## Definition

A myeloid-cell-specific hypoxia gene signature ("hypoxia score") built by combining the top genes of hypoxic TAM clusters from two independent GBM scRNA-seq datasets (Wang et al. and Antunes et al.). Applied to single cells, the score quantifies hypoxic stress within GAM/TAM populations and is used to correlate hypoxia with marker-gene expression (e.g. positively with Lgals3, negatively with P2ry12/Tmem119).

## Intuition

Generic bulk hypoxia signatures (Buffa, MSigDB hallmark) are tuned to whole tumors. To measure hypoxia *inside myeloid cells* at single-cell resolution, the authors distill a signature from hypoxic TAM clusters specifically — so it tracks myeloid hypoxic state rather than tumor-cell hypoxia.

## Formal notation

- Construction: intersection of top hypoxic-TAM cluster genes across Wang and Antunes datasets (Table S1).
- Application: per-cell module score in scRNA-seq; correlated with marker genes across GAM subclusters and species.

## Variants

- Distinct from bulk/tumor-level signatures such as [[concepts/tumor-hypoxia-mrna-signature]] and the Buffa metagene.

## Comparison

Cell-type-specific and myeloid-focused, versus tissue/bulk hypoxia metagenes; narrower scope but better suited to single-cell GAM analysis.

## When to use

Invoke when scoring hypoxic stress in tumor myeloid populations from scRNA-seq, or when correlating myeloid marker expression with hypoxia at single-cell resolution.

## Known limitations

- Derived from two GBM datasets; the authors note it "requires further development and validation across additional single-cell GAM datasets."
- Built from cluster top-genes, so partly circular when used to define hypoxic clusters.

## Open problems

- Cross-dataset/cross-cancer validation and refinement of the gene set.
- Whether a myeloid hypoxia score generalizes beyond glioma.

## Key papers

- [[papers/hypoxic-stress-dysregulates-functions-glioma-associated]]

## My understanding

A pragmatic, reusable tool for measuring myeloid-intrinsic hypoxia in scRNA-seq — directly applicable to HypoxiaVERSE-style scoring, with the caveat that it is GBM-derived and still preliminary.
