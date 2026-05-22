---
title: "Three new label-free bio-conservation metrics (cell-cycle, HVG, trajectory conservation) distinguish methods that classical label-based metrics rank as equal"
slug: label-free-metrics-capture-trajectories-cellcycle
status: supported
confidence: 0.8
tags:
  - benchmarking
  - data-integration
  - metrics
  - label-free
domain: single-cell-methods
source_papers:
  - benchmarking-atlas-level-data-integration-single
evidence:
  - source: "[[papers/benchmarking-atlas-level-data-integration-single]]"
    type: supports
    strength: strong
    detail: "Three new metrics introduced: (i) cell-cycle variance conservation (PCA-based gene-program preservation across batches), (ii) HVG overlap (% of pre-integration HVGs retained as HVGs post-integration), (iii) trajectory conservation (diffusion-map-based pseudotime correlation pre/post). Scanorama (gene), ComBat and MNN best on cell-cycle/HVG; Scanorama, scGen, FastMNN best on trajectory."
conditions: "Metrics are particularly useful when annotation granularity is coarse. They favor full-feature input over HVG input (one of the few exceptions to the HVG advantage)."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

The scIB benchmark introduces three label-free bio-conservation metrics — cell-cycle variance conservation, HVG overlap, and trajectory conservation — that distinguish integration methods on biology beyond cell-type labels. Methods that output corrected gene matrices (Scanorama gene, ComBat, MNN) preserve cell-cycle and HVG variation best; methods optimized for biological coherence (Scanorama, scGen, FastMNN) preserve trajectories best.

## Evidence summary

Quote (p.44): "Methods that favor bio-conservation and output corrected expression matrices tended to better conserve cell state variation. Indeed, Scanorama (gene), ComBat and MNN consistently performed well at conserving cell-cycle variance and HVGs in the integrated data. Trajectory structure was slightly better conserved in the overall high-performing methods Scanorama, scGen and FastMNN."

## Conditions and scope

- Metrics are diffusion-map-based for trajectory; PCA-based for cell-cycle; set-overlap for HVG.
- They flip the HVG-vs-full-feature preference: these label-free metrics favor full-feature integration.

## Counter-evidence

- (none in this paper)

## Linked ideas

(none yet)

## Open questions

- Should these label-free metrics carry higher weight in future atlas benchmarks where annotation quality is uncertain?
