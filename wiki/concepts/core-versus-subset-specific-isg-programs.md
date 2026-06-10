---
title: "Core versus cell-type-specific ISG programs"
aliases:
  - shared versus subset-specific ISG modules
tags:
  - interferon
  - ISG
  - cell-type-specificity
maturity: emerging
key_papers:
  - dissecting-type-ii-interferon-impacts-human
first_introduced: "2025"
date_updated: 2026-06-10
related_concepts:
  - hirisa-human-interferon-response-immune-subsets
  - ifn-ifn-ii-activity-deconvolution-scoring
---

## Definition

The decomposition of an interferon-stimulated gene (ISG) response into a conserved "core" program shared broadly across cell types (high fold change) and "subset-specific" programs unique to individual immune lineages (typically lower fold change).

## Intuition

Canonical ISG markers (OAS3, IFI44L, ISG15) are high-magnitude and shared, so they dominate aggregate signatures and mask lineage-specific biology. Resolving responses per cell type exposes lower-FC but functionally distinct subset programs — e.g., monocyte leukocyte-trafficking and pyroptosis genes — that aggregate analyses miss.

## Formal notation

Per subset: DEGs partitioned into shared (across lineages) vs unique; shared antiviral genes (MX1, ISG15, IFI6, IFI44L) show greater FCs than subset-specific genes; overlap quantified by Jaccard index across subsets.

## Variants

Applies separately to each IFN type (IFN-I core vs subset-specific; IFN-γ shared GBP/STAT1/IRF1 vs monocyte-unique CXCL9/IDO1).

## Comparison

Contrasts with single-aggregate ISG-signature scoring, which collapses this structure.

## When to use

When interpreting IFN responses in heterogeneous tissues/disease, to avoid attributing a monocyte- or B-cell-specific program to "global" IFN activity.

## Known limitations

Subset-specific genes have lower FCs and are easier to miss; definitions depend on the reference atlas used.

## Open problems

Whether subset-specific programs are conserved between blood and tissue.

## Key papers

- [[dissecting-type-ii-interferon-impacts-human]] — defines core and subset-specific ISG programs across 13 subsets

## My understanding

This is the conceptual justification for the whole atlas: the interesting IFN biology lives in the low-FC, subset-specific tail that aggregate signatures discard.
