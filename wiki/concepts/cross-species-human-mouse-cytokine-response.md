---
title: "Cross-species divergence of human and mouse cytokine responses"
aliases:
  - human-mouse cytokine response divergence
  - cross-species cytokine response comparison
maturity: emerging
tags:
  - cross-species
  - cytokines
  - translation
  - mouse-human
key_papers:
  - single-cell-cytokine-dictionary-human-peripheral
first_introduced: "2025"
date_updated: 2026-05-28
related_concepts:
  - cytokine-cell-type-specific-response-pleiotropy
  - donor-baseline-interferon-signaling-heterogeneity
---

## Definition

The finding that cell-type-matched cytokine responses correlate only weakly between human PBMCs (this Dictionary) and mouse lymph-node immune cells (Cui et al. 2024) — median gene-wise Pearson r ≈ 0.19 across 81 shared cytokines, with only ~11.3% of strongly regulated genes concordant and ~6.9% strongly discordant. Within-human (r ≈ 0.61) and within-mouse correlations substantially exceed cross-species ones; restricting to genes strongly regulated in both species raises agreement (within-human ~0.77 vs across-species ~0.57–0.59).

## Intuition

Mouse cytokine biology does not directly read out human cytokine biology at the gene level. But the gap is not purely "species divergence": experimental design differs too (in vitro 24 h human vs in vivo 4 h mouse, dose, tissue). Comparing to a time-matched human IFN-β dataset (Kang et al., 6 h) still shows within-human > cross-species, indicating both species and design contribute. Some cytokines (e.g. IL-32) have no mouse ortholog at all.

## Variants

- Concordant vs discordant strongly regulated genes
- Database-anchored comparison (ImmunoGlobe + immuneXpresso): better-studied cell–cytokine pairs diverge less
- Monocytes as the least cross-species-correlated lineage

## Comparison

Reframes the mouse [[immune-dictionary-dataset]] as a partial, not direct, proxy for human cytokine responses; motivates a dedicated human reference.

## When to use

When translating mouse cytokine-perturbation findings to human, or when deciding whether a human or mouse reference signature is appropriate for a given dataset.

## Known limitations

- Confounded by design differences (in vitro/in vivo, time, dose, tissue)
- DE-based comparisons sensitive to statistical power / cell numbers
- Single mouse dataset as comparator

## Open problems

- Isolating genuine species divergence from experimental confounders
- Which cytokine modules are conserved vs human-specific
- Implications for preclinical-to-clinical cytokine-therapy translation

## Key papers

- [[papers/single-cell-cytokine-dictionary-human-peripheral]]

## My understanding

A sobering translational result: well-studied, strong responses are reasonably conserved, but the long tail of cytokine × cell-type effects diverges, and human-specific cytokines (IL-32) sit entirely outside mouse models. Argues for human-native reference atlases in immunotherapy work.
