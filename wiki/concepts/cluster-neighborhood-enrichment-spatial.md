---
title: "Cluster neighborhood enrichment (NE) and differential NE in spatial omics"
aliases:
  - cluster NE
  - cluster neighborhood enrichment
  - differential neighborhood enrichment
  - differential cluster NE
  - asymmetric neighborhood enrichment
  - cluster proximity test
  - neighborhood enrichment observed/expected
  - spatial cluster co-occurrence test
  - cluster interaction enrichment
  - permutation-free NE
  - symmetric vs asymmetric NE
tags:
  - spatial-transcriptomics
  - spatial-statistics
  - tumor-microenvironment
  - methodology
maturity: active
key_papers:
  - cellcharter-reveals-spatial-cell-niches-associated
first_introduced: "Squidpy (Palla 2022 Nat. Methods) and earlier permutation tests; analytical formulation in CellCharter (Varrone 2024)"
date_updated: 2026-05-22
related_concepts:
  - "[[concepts/spatial-domain-detection-from-svg]]"
---

## Definition

A statistical test that quantifies whether cells belonging to spatial cluster A are spatially closer to cells of cluster B than expected by chance, reported as an observed/expected ratio. Symmetric NE treats A↔B as one quantity; asymmetric NE separately measures "B is over-represented in the neighbourhood of A" vs the reverse. Differential NE tests whether NE values differ between two conditions (e.g., healthy vs disease).

## Intuition

Two clusters can be globally abundant but rarely touch; conversely, two rare clusters can be tightly co-localized. NE separates abundance from proximity. Asymmetric NE catches biologically directional contexts — e.g., a small B-PALS boundary surrounded by a much larger B-follicle.

## Use

Used to identify candidate cell–cell interactions in spatial omics: which spatial clusters co-occur (NE > 0) or repel (NE < 0); which interactions change with disease (differential NE).

## Known limitations

- Analytical NE assumes a tractable null; permutation-based variants are slower but distribution-free.
- Sensitive to the proximity-graph definition (radius, kNN, l-hop).

## Relevance to active research

CellCharter ([[papers/cellcharter-reveals-spatial-cell-niches-associated]]) introduces an analytical implementation of symmetric and asymmetric cluster NE that scales beyond permutation-based methods (Squidpy). Differential NE reveals (i) B-PALS / B-follicle / marginal-zone rewiring in MRL-lupus mouse spleen, (ii) C0 ↔ C11 (hypoxic-tumor ↔ neutrophil) interactions in LUAD CosMx, and (iii) C23 ↔ C7 interactions in LUAD IMC.
