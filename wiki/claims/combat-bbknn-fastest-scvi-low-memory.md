---
title: "ComBat, BBKNN and SAUCIE are fastest; scVI, scANVI and BBKNN are most memory-efficient"
slug: combat-bbknn-fastest-scvi-low-memory
status: supported
confidence: 0.85
tags:
  - scalability
  - data-integration
  - scRNA-seq
  - benchmarking
domain: single-cell-methods
source_papers:
  - benchmarking-atlas-level-data-integration-single
evidence:
  - source: "[[papers/benchmarking-atlas-level-data-integration-single]]"
    type: supports
    strength: strong
    detail: "Under the scIB Snakemake pipeline timing/memory monitoring: ComBat, BBKNN and SAUCIE have the lowest CPU runtime. scVI, scANVI and BBKNN have the lowest peak memory. BBKNN is the unique entry in both lists."
conditions: "CPU-only timing. GPU availability changes the picture for deep-learning methods. Memory measured as peak Snakemake-reported usage."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

In CPU-only benchmark conditions, the fastest scRNA-seq integration methods are ComBat, BBKNN and SAUCIE; the most memory-efficient are scVI, scANVI and BBKNN. BBKNN appears in both lists, making it the operationally-cheapest method overall.

## Evidence summary

Quote (p.46): "ComBat, BBKNN and SAUCIE performed best in terms of runtime and scVI, scANVI and BBKNN are the most memory efficient."

## Conditions and scope

- CPU-only timing; deep-learning methods accelerate substantially on GPU.
- Memory is peak under the Snakemake pipeline; alternative monitoring may give different numbers.

## Counter-evidence

- (none)

## Linked ideas

(none yet)

## Open questions

- Has BBKNN's scaling profile held up post-2022 as datasets grew to 10M+ cells?
- Do GPU-native versions of scVI / scANVI dominate when GPU is available?
