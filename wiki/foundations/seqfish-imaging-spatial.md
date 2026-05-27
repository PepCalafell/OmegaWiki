---
title: "seqFISH — sequential fluorescence in situ hybridization"
slug: seqfish-imaging-spatial
domain: "spatial-transcriptomics / imaging-platform"
status: mainstream
aliases:
  - "seqFISH"
  - "seqFISH+"
  - "sequential FISH"
  - "sequential fluorescence in situ hybridization"
first_introduced: "Lubeck et al. Nat Methods 2014; seqFISH+ Eng et al. Nature 2019"
date_updated: 2026-05-27
source_url: "https://www.spatialresearch.org/seqfish/"
---

## Definition

seqFISH is an imaging-based spatial transcriptomics method that detects mRNA molecules via sequential rounds of fluorescent probe hybridization and imaging, encoding gene identity in a barcoded color sequence. seqFISH+ scales to >10,000 genes by combinatorial barcoding. Yields single-molecule, single-cell resolution after cell segmentation.

## Intuition

The barcoding scheme decouples the number of probed genes from the number of fluorescent channels — Y rounds × C colors encode C^Y genes. Used as the imaging modality in mouse embryo developmental atlases (Lohoff et al. 2022).

## Known limitations

- Long imaging times per slide.
- Requires high-quality cell segmentation for downstream covariation analysis.
- Limited tissue throughput compared to commercial platforms (MERSCOPE, Xenium, CosMx).

## Relevance to active research

Foundational technology for high-plex spatial transcriptomics; benchmark dataset for mouse embryo E8.5 used in NiCo (Lohoff 2022) and many other spatial method papers.
