---
title: "CUT&RUN — cleavage under targets and release using nuclease"
slug: cut-run-cleavage-under-targets-release
domain: "epigenomics / methods"
status: mainstream
aliases:
  - "CUT&RUN"
  - "CUT and RUN"
  - "cleavage under targets and release using nuclease"
first_introduced: "Skene & Henikoff 2017 eLife"
date_updated: 2026-06-04
source_url: "https://doi.org/10.7554/eLife.21856"
---

## Definition

CUT&RUN is an antibody-targeted chromatin profiling method in which a protein-A/G–MNase fusion is tethered to a chromatin-bound factor or histone modification in situ; localized nuclease cleavage releases the bound fragments for sequencing. It maps histone modifications and TF binding with lower input and background than ChIP-seq.

## Intuition

Instead of crosslinking and shearing the whole genome (ChIP), CUT&RUN cuts only where the antibody binds, so the signal-to-noise is high and few cells are needed — well suited to scarce sorted populations such as microglia from co-cultures.

## Formal notation

- Workflow: permeabilized cells/nuclei → primary antibody → pA/pG-MNase → Ca²⁺-activated cleavage → fragment release → library prep → sequencing.

## Key variants

- CUT&Tag (Tn5-based), ChIP-seq ([[foundations/chip-seq]]), ChIP-Nexus.

## Known limitations

- Sensitive to antibody quality; not ideal for very low-abundance targets.
- Quantitative comparisons across conditions require careful spike-in normalization.

## Open problems

- Standardization of normalization for differential acetylation across treatment conditions.

## Relevance to active research

Used in [[papers/hypoxic-stress-dysregulates-functions-glioma-associated]] to quantify the global loss of H3K27ac in BV2 microglia under hypoxia.
