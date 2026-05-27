---
title: "At 10 μm pixel resolution, spatial-DMT resolves telencephalon progenitors (W11, ventricular zone) from migrating GABAergic cortical interneurons (W7, mantle zone) in E11 mouse embryo forebrain"
slug: spatial-dmt-10um-resolves-telencephalic-progenitors-vs-gabaergic-cortical-interneurons-e11
status: supported
confidence: 0.85
tags: [near-single-cell, 10um-resolution, telencephalon, GABAergic-interneurons, cell-type-deconvolution]
domain: developmental neurobiology / spatial omics
source_papers:
  - spatial-joint-profiling-dna-methylome-transcriptome
evidence:
  - source: spatial-joint-profiling-dna-methylome-transcriptome
    type: supports
    strength: strong
    detail: "Quote (p.4): 'two spatially defined clusters, W7 and W11, captured key telencephalic compartments. W11 was enriched for telencephalon progenitors in the ventricular zone of the pallium, a neurogenic niche characterized by active cell division and proliferation, whereas W7 corresponded to γ-aminobutyric-acid-releasing (GABAergic) cortical interneurons localized in the mantle zone, where newborn neurons migrate, accumulate and differentiate to establish cortical architecture'. Cell-type deconvolution against Qiu 2024 scRNA-seq reference."
conditions: "E11 mouse embryo, 10 μm pixel size; cell-type deconvolution via scRNA-seq reference."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

At 10 μm pixel resolution — approaching single-cell — spatial-DMT resolves two telencephalic cell-type compartments in E11 mouse embryo forebrain: W11 = telencephalon progenitors in the ventricular zone, W7 = migrating GABAergic cortical interneurons in the mantle zone. Cell-type lineage tree from scRNA-seq reference confirms W11 are direct precursors to W7.

## Evidence summary

Reported in [[papers/spatial-joint-profiling-dna-methylome-transcriptome]], Fig. 1g–h and Extended Data Fig. 8.

## Conditions and scope

10 μm pixel chip, 1×1 mm ROI; depends on quality of external scRNA-seq reference (Qiu 2024).

## Counter-evidence

10 μm pixels still average over ≥1 cell on average; "near single-cell" is not strictly single-cell.

## Linked ideas

## Open questions

- True single-cell spatial methylome at sub-10 μm resolution.
- Methylation differences between progenitor (W11) and differentiated (W7) state at the methylome level.
