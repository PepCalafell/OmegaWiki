---
title: "CellCharter scales to millions of cells with the lowest memory among benchmarked spatial clustering tools"
slug: cellcharter-scales-millions-cells-lowest-memory
status: supported
confidence: 0.85
tags:
  - spatial-transcriptomics
  - scalability
  - benchmark
  - methodological
domain: methods
source_papers:
  - cellcharter-reveals-spatial-cell-niches-associated
evidence:
  - source: cellcharter-reveals-spatial-cell-niches-associated
    type: supports
    strength: strong
    detail: "Fig. 1c: total memory on DLPFC (12 samples) — CellCharter (GPU) 5.8 GB and (CPU) 6.1 GB vs STAGATE 80.5 GB, SOTIP 84.5 GB, SEDR 40.2 GB. Fig. 2b: on 707,466-cell CODEX mouse spleen, CellCharter total runtime ~15.9 min vs STAGATE ~698 min — ~4× faster including dimensionality reduction step."
conditions: "GPU and CPU versions both benchmarked. Memory leadership holds across all tested DLPFC sizes; runtime leadership at million-cell scale relative to STAGATE."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

CellCharter has the lowest memory consumption among benchmarked spatial-clustering tools and the runtime to handle datasets at the hundreds-of-thousands-to-millions-of-cells scale.

## Evidence summary

DLPFC runtime/memory comparison (Fig. 1c). CODEX mouse-spleen comparison (Fig. 2b): CellCharter 15.9 min vs STAGATE 698 min on 9 samples / 707,466 cells.

## Conditions and scope

Verified on Visium (DLPFC), CODEX (spleen, 707k cells), CosMx (LUAD, ~700k cells across 8 sections), MERFISH, and IMC (416 LUAD cores) datasets. UTAG remains the fastest on small datasets but does not include batch correction.

## Open questions

- Does the memory advantage hold for Visium HD's order-of-magnitude larger spot counts?
