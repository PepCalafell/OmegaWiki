---
title: "HIRISA is a single-cell atlas of IFN responses across 13 human immune subsets"
slug: "hirisa-single-cell-atlas-ifn-responses"
status: supported
confidence: 0.95
tags:
  - interferon
  - scRNA-seq
  - immune-atlas
  - resource
domain: immunology
source_papers:
  - dissecting-type-ii-interferon-impacts-human
evidence:
  - source: dissecting-type-ii-interferon-impacts-human
    type: supports
    strength: strong
    detail: "PBMCs from five healthy donors fractionated into CD14 monocytes, T, B, NK cells (>90% purity), stimulated 21h with IFN-α2A, IFN-β, IFN-γ, or IFN-λ1; 1,236,656 cells from 100 samples passed QC on 10x Flex, resolved into 13 L2 subsets."
conditions: "Healthy human PBMCs; enriched/fractionated stimulation; 10x Genomics Flex platform; 21h stimulation."
date_proposed: 2026-06-10
date_updated: 2026-06-10
---

## Statement

The Human Interferon Response in Immune Subsets Atlas (HIRISA) is a single-cell RNA-seq resource profiling responses to IFN-α2A, IFN-β, IFN-γ, and IFN-λ1 across 13 major human immune subsets (~1.23M cells, 5 healthy donors).

## Evidence summary

Supported by [[dissecting-type-ii-interferon-impacts-human]] (p.4): negative-selection enrichment of four lineages, 21h cytokine stimulation, 10x Flex scRNA-seq, 1,236,656 QC-passing cells resolved into 4 L1 lineages and 13 L2 subsets. See [[scrna-seq-10x-chromium]], [[hirisa-human-interferon-response-immune-subsets]].

## Conditions and scope

Circulating immune cells only; in-vitro stimulation of enriched populations from healthy donors.

## Counter-evidence

None within this paper.

## Linked ideas

## Open questions

Does the enriched-stimulation atlas generalize to tissue-resident immune populations and non-immune cells?
