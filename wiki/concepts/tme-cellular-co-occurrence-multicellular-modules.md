---
title: "TME cellular co-occurrence network and multicellular modules"
aliases:
  - multicellular modules
  - cellular co-occurrence network
  - TME cellular co-occurrence
tags:
  - tme
  - co-occurrence
  - multicellular-module
  - cellular-network
  - spatial
maturity: emerging
key_papers:
  - pan-cancer-tumor-classification-holistic-tumor
first_introduced: "2025"
date_updated: 2026-06-03
related_concepts:
  - type-interferon-multicellular-module-ifn1
  - niche-covariation-analysis
---

## Definition

A framework that builds a cellular network from positive frequency correlations among TME cell clusters and annotates connected components as multicellular modules with distinct biological meaning, validated by permutation/subsampling and spatial colocalization (e.g. via deconvolution of Visium data).

## Intuition

Cells that consistently rise and fall together across tumors likely participate in shared programs or niches. Grouping co-occurring clusters into modules summarizes multicellular organization beyond individual cell types.

## Variants

- Tissue-of-origin modules (blood, nerve, mucosa) reflecting organ context.
- Functional immune modules such as the type I interferon module (M-IFN1).

## Comparison

Frequency-correlation co-occurrence differs from spatial [[niche-covariation-analysis]], which infers cell-state coupling from spatial neighborhoods; modules here are detected compositionally and then checked for spatial coherence.

## When to use

When summarizing coordinated multicellular structure across many tumors from compositional data.

## Known limitations

- Frequency correlations can arise from co-enrichment in shared contexts without direct interaction.
- Some modules show no spatial coherence.

## Open problems

- Distinguishing causally interacting modules from co-enriched but non-interacting ones.

## Key papers

- [[pan-cancer-tumor-classification-holistic-tumor]] — constructs the co-occurrence network and annotates multicellular modules.

## My understanding

A compositional lens on multicellular organization that complements spatial and ligand-receptor methods.
