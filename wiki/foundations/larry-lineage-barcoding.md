---
title: "LARRY lineage barcoding"
slug: larry-lineage-barcoding
domain: "methods / lineage tracing / single-cell genomics"
status: mainstream
aliases:
  - LARRY
  - lineage and RNA recovery
  - LARRY barcodes
  - expressed lentiviral barcoding
first_introduced: "Weinreb, Rodriguez-Fraticelli, Camargo & Klein 2020 *Science* — Lineage tracing on transcriptional landscapes links state to fate during differentiation"
date_updated: 2026-06-03
source_url: "https://doi.org/10.1126/science.aaw3381"
---

## Definition

LARRY (Lineage And RNA RecoverY) is a lentiviral expressed-barcode system that stably integrates a heritable, transcribed DNA barcode into cells at the start of a time-course experiment. Because the barcode is expressed and captured by standard scRNA-seq, each cell's clonal identity is read out alongside its transcriptome, allowing direct assignment of clonal ancestry and measurement of fate outcomes across timepoints.

## Intuition

Snapshot scRNA-seq alone cannot say which early cell gave rise to which late cell. LARRY tags founder cells with unique heritable barcodes, so all descendants of a clone share a label — providing ground-truth fate bias to benchmark trajectory-inference and state→fate prediction methods.

## Key variants

- Static expressed barcodes (original LARRY) vs evolving/CRISPR-based recorders.
- Combined with cell-state profiling at multiple timepoints to define clonal fate distributions.

## Known limitations

- Barcode is set at infection; it records clonal membership, not the full branching history within a clone.
- Requires in vitro / transplantable systems amenable to lentiviral transduction.
- Sampling at each timepoint is destructive, so the same cell is never observed twice.

## Open problems

- Reconstructing intra-clone branching order from endpoint clonal labels alone.

## Relevance to active research

- The in vitro mouse haematopoiesis benchmark dataset (Days 2/4/6) used by [[papers/pseudodynamics-reconstructing-population-dynamics-time-resolved]] to evaluate fate-bias and trajectory accuracy against flow-matching and dynamic-OT baselines.
