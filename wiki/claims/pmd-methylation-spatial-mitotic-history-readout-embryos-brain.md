---
title: "Partially Methylated Domain (PMD) methylation acts as a spatial mitotic-history readout: low in proliferative tissue (embryonic heart, P21 dentate gyrus), high in differentiated tissue (P21 cortex)"
slug: pmd-methylation-spatial-mitotic-history-readout-embryos-brain
status: supported
confidence: 0.85
tags: [PMD, mitotic-history, partially-methylated-domain, proliferation, spatial-omics]
domain: epigenetics / spatial omics
source_papers:
  - spatial-joint-profiling-dna-methylome-transcriptome
evidence:
  - source: spatial-joint-profiling-dna-methylome-transcriptome
    type: supports
    strength: moderate
    detail: "Quote (p.7): 'partially methylated domains (PMDs), which lose methylation over successive mitotic divisions, serve as indicators of mitotic activity. By spatially mapping PMD methylation in E11 and E13 embryos (Fig. 5c,d), we identified distinct regional patterns... embryonic heart tissue demonstrated lower PMD methylation levels, reflecting active cardiogenesis... In the P21 brain (Fig. 5e), cortical layers displayed higher PMD methylation, consistent with reduced proliferative capacity typical of differentiated neurons. By contrast, the DG has comparatively lower PMD methylation, consistent with the presence of neural stem and progenitor cells in the subgranular zone that continue to undergo mitotic division and neurogenesis'."
conditions: "Mouse E11/E13 embryos and P21 brain; PMD methylation averaged over each pixel."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

PMD methylation level — known to decline with successive mitotic divisions — varies spatially in a pattern matching tissue proliferative state. In E11/E13 embryos, heart shows low PMD methylation (active cardiogenesis) and a centre-to-periphery gradient; in P21 brain, cortex shows high PMD methylation (post-mitotic neurons) and dentate gyrus shows low PMD methylation (adult neurogenesis).

## Evidence summary

Reported in [[papers/spatial-joint-profiling-dna-methylome-transcriptome]], Fig. 5c–e.

## Conditions and scope

Mouse tissue; PMD calling depends on genome-wide methylation coverage; absolute mitotic count not quantified.

## Counter-evidence

PMD–mitotic-history coupling is indirect; alternative interpretations (lineage-specific PMD remodelling) not excluded.

## Linked ideas

## Open questions

- Quantitative mapping of PMD methylation to absolute number of past divisions.
- Cross-validation against direct proliferation markers (Ki67, Edu) at matched spatial resolution.
