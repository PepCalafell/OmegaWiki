---
title: "Rare immune cell types produce the most cytokines (inverse abundance–production correlation)"
aliases:
  - rare cells cytokine producers
  - FRC cytokine producer
  - basophil cytokine producer
  - ILC cytokine producer
  - inverse abundance-cytokine production correlation
  - stromal cell cytokine production
  - rare cell immune networking
  - cytokine producer hubs
  - lymph node FRC cytokine hub
  - non-abundant immune cell cytokine output
maturity: emerging
tags:
  - cytokine-networks
  - rare-cell-types
  - FRC
  - ILC
  - basophil
key_papers:
  - dictionary-immune-responses-cytokines-single-cell
first_introduced: "2024"
date_updated: 2026-05-13
related_concepts:
  - cytokine-mediated-immune-cell-cell-interactome
---

## Definition

Inferring cytokine production from per-cell-type transcript expression in the Immune Dictionary, rare cell types (fibroblastic reticular cells, basophils, innate lymphoid cells, eTACs, LECs) produce the *largest* number of distinct cytokines, while abundant lymphocytes (B, CD4 T, CD8 T) produce relatively few. Pearson r = -0.71, P = 0.0065 between cell-type abundance and number of cytokines produced.

## Intuition

The cytokine "broadcast bandwidth" of a cell type is inversely correlated with its abundance. FRCs are functional hubs of cytokine production despite being rare. Loss of a rare cytokine-producing cell type has disproportionate network consequences.

## Variants

- FRC as universal lymph-node broadcaster (TGFβ1, IL-7, IL-33, BAFF…)
- Basophils as IL-4 / IL-13 producers
- ILCs as IL-13 / IL-22 / IFNγ producers
- cDC1 as IL-1β-mediated broadcaster

## When to use

Important context for any analysis that filters out rare cell types — those filtered cells may be the actual signal source in the cytokine network.

## Open problems

- Whether the same inverse relation holds in human tissue
- Whether the relation generalizes outside lymph nodes (tumours, infected tissue)

## Key papers

- [[papers/dictionary-immune-responses-cytokines-single-cell]]

## My understanding

Provides a quantitative rationale for the existence of "small-but-influential" populations in tissue immunology. Has direct implications for scRNA-seq analyses that over-filter low-abundance clusters.
