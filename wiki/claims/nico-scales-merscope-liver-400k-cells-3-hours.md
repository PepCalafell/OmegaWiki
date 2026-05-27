---
title: "NiCo annotates the 391,679-cell MERSCOPE mouse liver dataset in <3 hours on a 16-core workstation, whereas cell2location takes >2 days on the same data"
slug: nico-scales-merscope-liver-400k-cells-3-hours
status: supported
confidence: 0.9
tags: [spatial-transcriptomics,scalability,runtime,MERSCOPE]
domain: methods / spatial-transcriptomics
source_papers:
  - nico-identifies-extrinsic-drivers-cell-state
evidence:
  - source: nico-identifies-extrinsic-drivers-cell-state
    type: supports
    strength: strong
    detail: "Run-time benchmark on AMD Ryzen 9 5950X 16-core with 128 GiB memory; NiCo finishes in <3 hours; cell2location >2 days; SpaGCN aborted due to memory exhaustion on the same data (Fig. 2b)."
conditions: "Single hardware configuration; 391,679 cells; standard workstation, no GPU."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

NiCo annotates the 391,679-cell MERSCOPE mouse liver dataset in <3 hours on a 16-core workstation, whereas cell2location takes >2 days on the same data.

## Evidence summary

[[papers/nico-identifies-extrinsic-drivers-cell-state]] — Run-time benchmark on AMD Ryzen 9 5950X 16-core with 128 GiB memory; NiCo finishes in <3 hours; cell2location >2 days; SpaGCN aborted due to memory exhaustion on the same data (Fig. 2b).

## Conditions and scope

Single hardware configuration; 391,679 cells; standard workstation, no GPU.

## Counter-evidence

None within paper.

## Linked ideas

## Open questions

- Independent replication outside the Grün lab.
