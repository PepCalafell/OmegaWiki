---
title: "Parse Biosciences split-pool barcoding (SPLiT-seq)"
slug: parse-biosciences-split-pool-barcoding
domain: "methods"
status: mainstream
aliases:
  - "SPLiT-seq"
  - "split-pool barcoding"
  - "combinatorial barcoding scRNA-seq"
  - "Parse Biosciences Evercode"
  - "Parse GigaLab"
first_introduced: "Rosenberg et al. 2018 (Science) — SPLiT-seq; commercialized by Parse Biosciences"
date_updated: 2026-05-28
source_url: "https://doi.org/10.1126/science.aam8999"
---

## Definition

A combinatorial-indexing single-cell RNA sequencing method that labels each cell's transcripts with a unique barcode combination generated through successive rounds of split-pool ligation, without physically isolating individual cells into droplets or wells. Fixed cells/nuclei act as their own reaction compartments, enabling very large numbers of cells and samples to be multiplexed in one experiment. Commercialized by Parse Biosciences (Evercode / GigaLab).

## Intuition

Instead of one cell per droplet ([[scrna-seq-10x-chromium]]), split-pool barcoding repeatedly distributes fixed cells across wells, ligates a well-specific barcode, then pools and re-splits. After several rounds, the probability that two cells share the full barcode sequence is negligible, so each cell gets a unique combinatorial label. This decouples throughput from instrument partitioning and makes million-cell, many-sample screens (like the 90-cytokine × 12-donor Dictionary) practical.

## Key variants

- SPLiT-seq (original, Rosenberg 2018)
- Parse Evercode WT (whole transcriptome)
- Parse GigaLab (ultra-high-throughput, used for the Human Cytokine Dictionary)

## Known limitations

- Requires cell/nucleus fixation (potential RNA degradation / capture bias)
- Barcode collision risk if cell input exceeds design capacity
- Different gene-capture characteristics than droplet 10x — cross-platform comparison needs care

## Open problems

- Standardization against droplet platforms for atlas integration
- Multimodal extensions (protein, ATAC) at split-pool scale

## Relevance to active research

The assay enabling the [[human-cytokine-dictionary-dataset]] at ~9.7M cells across 1,000+ cytokine × cell-type conditions. Co-author Alexander B. Rosenberg co-invented SPLiT-seq and co-founded Parse Biosciences. Relevant to any large-scale single-cell perturbation screen.
