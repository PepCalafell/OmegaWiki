---
title: "MMCCI — multi-platform multi-modal cell-cell interaction integration"
slug: mmcci-multiplatform-cci
domain: spatial omics methods
status: mainstream
aliases: ["MMCCI", "multi-platform multi-sample CCI", "multimodal CCI integration"]
first_introduced: "2024"
date_updated: 2026-06-03
source_url: "https://github.com/BiomedicalMachineLearning/MMCCI"
---

## Definition

MMCCI (Multi-platform, Multi-modal Cell-Cell Interaction) is a computational framework that integrates cell-cell interaction predictions across biological replicates, platforms, and modalities to identify consistent interactions and perform differential interaction analysis. It combines per-sample interaction scores/p-values (e.g. stLearn SCTP outputs) into integrated interaction strengths for each ligand-receptor pair and each cell-type pair, then statistically compares them — at the cell-type network level (edges between interacting cell types) or at the L-R level (interaction scores).

## Intuition

Single-sample interaction predictions are noisy and platform-dependent. MMCCI asks which interactions survive integration across replicates and technologies, and which differ significantly between conditions (e.g. between cancer types) — turning many noisy per-sample networks into high-confidence, comparable interactomes.

## Formal notation

For interaction i, integrated strength = cumulative p-value combination across samples; differential tests compare integrated scores between groups at L-R or cell-type-pair resolution.

## Key variants

- Cell-type network-level differential analysis
- L-R-level differential analysis
- Cross-platform (CosMx + Visium) integration

## Known limitations

- Inherits biases of the underlying per-sample interaction caller
- Sensitive to batch/platform normalisation
- Statistical power limited by replicate count

## Open problems

- Principled weighting across heterogeneous platforms
- Handling partially overlapping gene/L-R panels

## Relevance to active research

Used to derive cancer-type-specific consistent ligand-receptor interactomes (e.g. 16 LR pairs in BCC, 17 in cSCC, 37 in melanoma) and to compare cell-cell interaction networks across skin cancer subtypes.
