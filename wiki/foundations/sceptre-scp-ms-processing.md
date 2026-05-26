---
title: "SCeptre — Scanpy-style processing pipeline for scp-MS"
slug: sceptre-scp-ms-processing
domain: "methods / single-cell proteomics"
status: mainstream
aliases:
  - SCeptre
  - SCeptre scp-MS processing
  - single-cell proteomics Scanpy
  - mass-spec scp-MS analysis pipeline
  - Schoof SCeptre pipeline
  - scp-MS batch correction SCeptre
  - SCeptre normalization scp-MS
first_introduced: "Schoof et al. (Furtwängler lab lineage); used in Furtwängler et al. 2025 *Science*"
date_updated: 2026-05-26
source_url: "https://github.com/schooflab/SCeptre"
---

## Definition

SCeptre is a Python pipeline for processing single-cell proteomics by mass spectrometry (scp-MS) data, extending Scanpy idioms (AnnData containers, modular processing steps) to handle the specifics of MS data: high missingness, isobaric channel batch effects, peptide-carrier normalization, and TMT reporter-ion quantification.

## Intuition

scRNA-seq and scp-MS share the same fundamental abstraction (cells × features with missingness and batch effects), so the Scanpy ecosystem can be transposed onto MS data. SCeptre handles the MS-specific preprocessing while exposing the resulting object to all downstream Scanpy / scverse tools.

## Formal notation

Pipeline steps:
1. Raw report import (peptide-level intensities from MaxQuant / FragPipe).
2. Peptide-to-protein roll-up.
3. Cell-level QC (missingness threshold, total intensity).
4. Batch correction (per-MS-run, per-plate, per-TMT-channel).
5. Median-ratio normalization (vs total-signal normalization — Furtwängler 2025 benchmark).
6. AnnData object output for downstream UMAP / clustering / differential abundance.

## Key variants

- TMT 11-plex / TMTpro 16-plex configurations.
- Peptide-carrier vs no-carrier modes.

## Known limitations

- Median-ratio normalization assumes most proteins are unchanged across cells — may underperform when global proteome shifts dominate (e.g., quiescent vs proliferating cells).
- Requires upstream MaxQuant or FragPipe processing.

## Open problems

- Imputation strategies for high-missingness regimes.
- Cross-lab batch correction standardization.

## Relevance to active research

- [[papers/mapping-early-human-blood-cell-differentiation]] uses SCeptre as its primary processing pipeline; pipeline behavior (PCA regression confirming donor/plate variance removal) is reported there.
