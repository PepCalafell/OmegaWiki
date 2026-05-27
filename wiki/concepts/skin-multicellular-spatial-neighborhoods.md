---
title: "Ten multicellular spatial neighborhoods as architectural units of human skin"
aliases:
  - skin spatial neighborhoods
  - multicellular skin neighborhoods
  - skin N0-N9 neighborhoods
  - DEJ-PERIVASC-STROMA-HF-ECCRINE-SEB-SUBCUTIS architecture
tags:
  - skin
  - spatial-transcriptomics
  - MERFISH
  - tissue-architecture
  - multicellular-neighborhood
maturity: emerging
key_papers:
  - single-cell-spatial-transcriptomic-analysis-human
first_introduced: "Restrepo et al. Nature Genetics 2026"
date_updated: 2026-05-27
related_concepts:
  - "[[concepts/perivascular-immune-stromal-niche-skin-salt]]"
  - "[[concepts/centrifugal-cellular-diversity-gradient-skin]]"
  - "[[concepts/age-stroma-to-perivasc-fibroblast-shift]]"
---

## Definition

A taxonomy of ten reproducible MERFISH-defined neighborhoods (N0–N9) that partition human skin into characteristic cell-coalitions: N0 dermo-epidermal junction (DEJ), N1 PERIVASC I (immune-enriched perivascular), N2 differentiated interfollicular epidermis (DIFF IFE), N3 PERIVASC II (stromal-vascular), N4 STROMA (reticular dermis), N5 UPPER HF, N6 ECCRINE, N7 SEB GLAND, N8 SUBCUTIS, N9 LOWER HF.

## Intuition

Skin's macroanatomy (epidermis / dermis / subcutis / adnexa) is shorthand for a richer cellular grammar. The ten neighborhoods are the atomic units that compose this grammar; anatomic sites differ in their *mixture* of these units, not in inventing new ones.

## Variants

- Disease-enriched neighborhoods: TLS, TLS-like, KC stress, HS tunnel, BCC tumor — appear in Visium ST mapping of AD, SCC, BCC, HS, psoriasis but not normal skin.

## Comparison

- vs Cell2location/CellCharter domains: same broad family of cluster-of-clusters spatial domains, here applied at MERFISH single-cell resolution rather than Visium spot resolution.

## When to use

When normalising spatial skin data across anatomy, donor age, or disease — to provide a shared coordinate system beyond histological compartments.

## Known limitations

- Number (k=10) is data-driven and may collapse finer hair-follicle or eccrine substructure.
- Neighborhoods are categorical; cell-state gradients within each are not modeled.

## Open problems

- Are the ten neighborhoods conserved across species (mouse skin) and across ethnicities at scale?
- How do neighborhoods reorganize during wound healing time-courses?

## Key papers

- [[papers/single-cell-spatial-transcriptomic-analysis-human]] — defines the ten-neighborhood scheme.

## My understanding

A shared neighborhood vocabulary is the most reusable contribution of this paper. Future skin spatial-omics studies can map their data onto N0-N9 to make findings comparable across labs, much the way Tabula-style atlases standardised cell-type names.
