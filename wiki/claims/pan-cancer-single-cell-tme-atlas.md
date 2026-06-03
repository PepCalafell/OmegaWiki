---
title: "Pan-cancer single-cell TME atlas spans 4.6M cells across 24 cancer types"
slug: "pan-cancer-single-cell-tme-atlas"
status: supported
confidence: 0.9
tags: [tme,atlas,scRNA-seq,pan-cancer,quantitative]
domain: oncology
source_papers:
  - pan-cancer-tumor-classification-holistic-tumor
evidence:
  - source: pan-cancer-tumor-classification-holistic-tumor
    type: supports
    strength: strong
    detail: "Core collection: 4,590,413 high-quality cells from 1,192 samples of 819 patients, 24 cancer types; 6 major compartments and 95 fine-grained subsets."
conditions: "Restricted to 10x Genomics unbiased-sorting datasets to minimize platform variation; excludes plate-based and sorted-enrichment data."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

A pan-cancer TME single-cell atlas was built from 10x scRNA-seq datasets with unbiased sorting. The core collection comprised 4,590,413 high-quality cells from 1,192 samples of 819 patients across 24 cancer types; clustering yielded six major compartments and 95 fine-grained subsets.

## Evidence summary

Core collection (n=55 datasets) of treatment-naive primary tumors plus adjacent normal and blood; 10x-only, unbiased-sorting datasets after QC. (p.3-4) Quote: "our core collection comprised a total of 4,590,413 high-quality cells from 1,192 samples of 819 patients, representing 24 cancer types".

## Conditions and scope

Restricted to 10x Genomics unbiased-sorting datasets to minimize platform variation; excludes plate-based and sorted-enrichment data.

## Counter-evidence

None recorded at ingest.

## Linked ideas

None yet.

## Open questions

How does coverage of rarer cancer types affect cluster stability for those types?
