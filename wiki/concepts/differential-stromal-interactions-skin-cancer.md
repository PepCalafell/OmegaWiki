---
title: "Differential stromal cell-cell interactions across skin cancer subtypes"
aliases: ["fibroblast interaction divergence skin cancer", "melanocyte-fibroblast-T-cell community"]
tags: [skin-cancer, tumour-microenvironment, cell-cell-interaction, fibroblast]
maturity: emerging
key_papers:
  - integrating-12-spatial-single-cell-technologies
first_introduced: "2025"
date_updated: 2026-06-03
related_concepts: [cd44-ecm-axis-melanoma-invasion, cross-platform-spatial-meta-community]
---

## Definition

The observation that the three major skin cancers (cSCC, BCC, melanoma) differ systematically in their stromal cell-cell interaction wiring: fibroblasts are the dominant interacting partner in all three, but fibroblast→T-cell interactions are stronger in keratinocyte cancers (cSCC, BCC) whereas fibroblast→melanocyte interactions are stronger in melanoma, with melanocyte–fibroblast–T-cell colocalization defining a melanoma-enriched community.

## Intuition

If different cancers arise and progress differently despite shared risk factors, part of the explanation is how malignant cells wire into the stroma. Keratinocyte cancers and melanoma share fibroblast centrality but route fibroblast signalling to different partners, which may relate to their differing invasiveness and metastatic potential.

## Formal notation

Not applicable. Operationalised as differential interaction scores (MMCCI) at cell-type-pair level and co-occurrence probabilities in spatial communities.

## Variants

- Cell-type-network-level differences (fibroblast-T vs fibroblast-melanocyte)
- L-R-level differences (collagen-CD44/integrin in melanoma; SPP1-integrin in cSCC; WNT in BCC)

## Comparison

Specialises the general theme of cancer-associated-fibroblast centrality to a *comparative*, subtype-resolved interactome rather than a single tumour type.

## When to use

When comparing TMEs across related cancers to explain divergent initiation/progression, or to nominate subtype-specific interaction targets.

## Known limitations

- Small patient cohort (24 donors)
- Interaction inference, requiring experimental validation
- Fibroblast subtype resolution limited by panels

## Open problems

- Whether differential fibroblast wiring is causal for metastatic potential
- Mapping fibroblast subtypes (CAF, EMT-fibroblast) to the differential interactions

## Key papers

- [[integrating-12-spatial-single-cell-technologies]] — finds fibroblast-T-cell interactions stronger in cSCC/BCC and fibroblast-melanocyte stronger in melanoma, with a melanocyte–fibroblast–T-cell colocalized community.

## My understanding

A comparative-TME concept: the same dominant cell (fibroblast) is rewired differently per cancer type, a candidate explanation for their distinct biology.
