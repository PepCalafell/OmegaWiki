---
title: "Milo (differential abundance testing)"
slug: milo-differential-abundance-testing
domain: single-cell genomics
status: mainstream
aliases:
  - Milo
  - Milo DA
  - neighbourhood differential abundance
first_introduced: "2021"
date_updated: 2026-06-03
source_url: ""
---

## Definition

Milo is a method for differential abundance (DA) testing in single-cell data. It assigns cells to overlapping neighbourhoods on a k-nearest-neighbour graph and tests, neighbourhood by neighbourhood, whether cell abundance differs between conditions using a negative-binomial generalized linear model.

## Intuition

Rather than relying on discrete cluster labels, Milo asks "are there regions of the cell-state manifold that are over- or under-represented in one condition versus another?", giving cluster-free, fine-grained detection of compositional shifts.

## Formal notation

For each neighbourhood it models cell counts per sample with a NB-GLM `~ condition`, then applies spatial FDR correction across overlapping neighbourhoods.

## Key variants

- MiloDE extends the neighbourhood framework to differential expression.

## Known limitations

- Designed for binary/grouped condition contrasts (differential abundance *between* conditions), not for summarizing the full distribution of each sample.
- Does not produce a per-sample representation usable for sample-level clustering or trajectory inference.

## Open problems

- Integrating abundance and expression shifts in a single test.

## Relevance to active research

Milo is the canonical density-based DA tool and a conceptual point of contrast for scSLIDE: both exploit local density, but Milo performs binary differential-abundance testing across conditions, whereas scSLIDE summarizes each sample's entire state distribution to enable sample-level embedding.
