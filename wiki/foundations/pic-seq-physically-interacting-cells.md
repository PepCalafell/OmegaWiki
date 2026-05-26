---
title: "PIC-seq — physically-interacting cell sequencing"
slug: pic-seq-physically-interacting-cells
domain: "single-cell genomics / methods"
status: mainstream
aliases:
  - "PIC-seq"
  - "physically-interacting cell sequencing"
  - "PIC sequencing"
first_introduced: "Giladi et al. 2020 (Nat Biotechnol) — Amit lab, Weizmann"
date_updated: 2026-05-26
source_url: "https://www.nature.com/articles/s41587-020-0442-2"
---

## Definition

A single-cell RNA-seq workflow that preserves and selectively sorts heterotypic cell-cell doublets (physically interacting cells, PICs) from dissociated tissue, then computationally deconvolves each PIC's component cell types using reference singlet transcriptomes. Designed to identify cell-cell interactions that occur in situ but would be missed by standard scRNA-seq dissociation, which discards doublets.

## Intuition

Standard scRNA-seq filters out doublets as artefacts. PIC-seq treats them as the signal: cells that were physically engaging another cell at the moment of dissociation. By recovering MNP/T-cell doublets (or other heterotypic pairs), it reveals which cell pairs preferentially interact in vivo.

## Key variants

- Original Giladi 2020 formulation (mouse / human; gentle dissociation; FACS for doublet gating)
- Application to tumor MNP/T-cell pairs (Cohen, Giladi, Hamon, multiple studies)

## Known limitations

- Snapshot of stable interactions; transient contacts may dissociate.
- Component-cell-type deconvolution accuracy depends on singlet reference quality.
- Doublet gating is sensitive to dissociation conditions.

## Open problems

- Quantitative recovery efficiency of in situ interactions.
- Integration with spatial transcriptomics (MERFISH/Visium) for orthogonal validation.
