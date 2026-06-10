---
title: "HIRISA — Human Interferon Response in Immune Subsets Atlas"
aliases:
  - HIRISA
  - Human Interferon Response in Immune Subsets Atlas
tags:
  - interferon
  - immune-atlas
  - scRNA-seq
  - resource
maturity: emerging
key_papers:
  - dissecting-type-ii-interferon-impacts-human
first_introduced: "2025"
date_updated: 2026-06-10
related_concepts:
  - core-versus-subset-specific-isg-programs
  - ifn-ifn-ii-activity-deconvolution-scoring
  - donor-baseline-interferon-signaling-heterogeneity
---

## Definition

HIRISA (Human Interferon Response in Immune Subsets Atlas) is a single-cell RNA-seq reference resource cataloguing the transcriptomic responses of major human circulating immune subsets to type I (IFN-α2A, IFN-β), type II (IFN-γ), and type III (IFN-λ1) interferons.

## Intuition

Existing IFN transcriptomic references aggregate mixed cell types and conflate IFN types, so upstream IFN activity cannot be inferred cleanly from disease data. HIRISA fixes this by stimulating purified lineages separately and profiling them at single-cell resolution, producing cell-type- and IFN-type-resolved ISG references.

## Formal notation

~1.23M cells from 5 healthy donors; 4 lineages (CD14 monocytes, T, B, NK) enriched to >90% purity; 21h stimulation with each IFN or unstimulated; 10x Flex; resolved into 13 L2 subsets; per-donor N-of-1 bootstrapped differential expression yields shared DEGs and mean fold changes per IFN.

## Variants

Companion interactive web explorers (ISG fold-change browser + scoring tool) at the Allen Immunology resource portal.

## Comparison

Improves on MSigDB-style aggregate ISG sets and prior single-cell-type/one-IFN datasets by spanning all major IFN types across all major immune subsets.

## When to use

As a reference to interpret IFN-driven transcriptional programs in a cell-type-specific manner, and as the ISG basis for the [[ifn-ifn-ii-activity-deconvolution-scoring]] framework.

## Known limitations

Circulating immune cells only; in-vitro stimulation; healthy donors; fixed concentrations and a single 21h timepoint.

## Open problems

Extension to tissue-resident populations (macrophages, fibroblasts, memory T cells) and additional timepoints/doses.

## Key papers

- [[dissecting-type-ii-interferon-impacts-human]] — introduces HIRISA

## My understanding

The value of HIRISA is less the atlas per se than the cell-type-resolved ISG dictionaries it yields, which make IFN-I vs IFN-II deconvolution tractable downstream.
