---
title: "IFN-I / IFN-II activity deconvolution scoring (NMF on cell-type ISGs)"
aliases:
  - IFN-α and IFN-γ scoring algorithm
  - HIRISA scoring framework
tags:
  - interferon
  - deconvolution
  - NMF
  - methodology
maturity: emerging
key_papers:
  - dissecting-type-ii-interferon-impacts-human
first_introduced: "2025"
date_updated: 2026-06-10
related_concepts:
  - hirisa-human-interferon-response-immune-subsets
  - core-versus-subset-specific-isg-programs
---

## Definition

A quantitative framework that separates type I (IFN-α) and type II (IFN-γ) interferon activity per cell type from transcriptomic data by computing fold changes of HIRISA-derived ISGs against matched controls and applying non-negative matrix factorization to derive per-cell-type IFN-α and IFN-γ coefficients ("scores").

## Intuition

IFN-I and IFN-II share many ISGs but differ in cell-type-specific, IFN-type-specific genes (e.g., GBPs and CXCL9/IDO1 for IFN-γ; MX/IFIT/OAS for IFN-I). Using cell-type-resolved ISG references as the factorization basis lets co-induced IFN-I and IFN-II signals be disentangled where bulk signatures cannot.

## Formal notation

For each subject and cell type: FCs for ~1,174 HIRISA ISGs vs controls → NMF → IFN-α and IFN-γ scores; IFN-γ score forced to zero in NK cells (no IFNGR2). Baseline (controls) = 0.

## Variants

Deployed as an interactive web tool accepting scRNA-seq or bulk PBMC data and displaying scores against eight published disease datasets.

## Comparison

Goes beyond single ISG-signature scoring (which cannot distinguish IFN type) by jointly modeling shared and unique ISGs across cell types.

## When to use

To quantify and compare IFN-I vs IFN-II activity across diseases, timepoints, or treatment arms in a standardized, cell-type-resolved way.

## Known limitations

Requires cell-type resolution and matched controls; IFN-γ scores correlate only weakly with circulating IFN-γ; sensitive to cross-cohort batch effects.

## Open problems

Robustness on bulk-only data; validation against orthogonal IFN-pathway readouts.

## Key papers

- [[dissecting-type-ii-interferon-impacts-human]] — introduces the scoring algorithm

## My understanding

This is the practical payload of the paper: HIRISA is the reference, but the NMF deconvolution is what turns it into a reusable cross-disease measurement instrument.
