---
title: "Anatomical niche predicts macrophage function in tumors"
aliases:
  - anatomical niche predicts macrophage function
  - spatial compartmentalization of macrophage function
  - niche over surface markers
tags:
  - macrophage
  - spatial-transcriptomics
  - tumor-microenvironment
  - niche
maturity: emerging
key_papers:
  - chemokine-defined-macrophage-niches-establish-spatial
first_introduced: "2026"
date_updated: 2026-06-02
related_concepts:
  - chemokine-defined-interstitial-macrophage-division-of-labor
  - cd206hi-im-bronchovascular-chemokine-tls-niche
  - tissue-resident-macrophage-tumor-niche
---

## Definition

The principle that a tumor macrophage's function is best predicted by integrating its anatomical/spatial niche with its transcriptional state, rather than by surface markers alone. In lung cancer, CD206hi IMs positioned along bronchovascular and pleural regions are protective (TLS-organizing), whereas CD206lo IMs and recMacs positioned within tumor-dense cores/margins are protumorigenic.

## Intuition

Spatial transcriptomics (10x Xenium) shows macrophage subsets occupy non-overlapping compartments — airways/vessels (CD206hi IMs), tumor cores/margins (CD206lo IMs, recMacs), airspaces (AMs, largely excluded from tumor). The chemokine each subset produces is read out locally, so where a macrophage sits dictates which immune circuit (lymphoid recruitment vs myeloid amplification) it drives.

## Formal notation

function ≈ f(transcriptional state, anatomical niche) ≫ f(surface marker).

## Variants

- Bronchovascular/pleural protective niche vs intratumoral suppressive niche.
- Generalizes the niche-composition logic seen in spatial atlases to macrophage function specifically.

## Comparison

Extends marker-based ("M2-like CD206") and purely transcriptomic classifications by making spatial position a first-class predictor. Complementary to niche-composition and neighborhood-enrichment spatial methods.

## When to use

When reconciling conflicting reports of a macrophage marker (e.g. CD206, Trem2) being pro- or antitumor — position likely explains the discrepancy.

## Known limitations

- Demonstrated in mouse lung cancer; targeted Xenium panel rather than whole-transcriptome.
- Causality between position and function is inferred from depletion/chimera experiments, not from spatial perturbation.

## Open problems

- Spatially selective perturbation tools to test the niche→function link directly.
- Whether niche assignment is instructive (niche programs the macrophage) or selective (programmed macrophages home to niches).

## Key papers

- [[chemokine-defined-macrophage-niches-establish-spatial]]

## My understanding

The paper's headline take-home: stop classifying tumor macrophages by surface markers in isolation; combine transcriptional state with where the cell physically resides. This is both a conceptual claim and a methodological prescription for spatial profiling.
