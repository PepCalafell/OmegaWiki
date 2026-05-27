---
title: "Spatial pseudotime mapping of DNA-methylation + RNA reveals migration of oligodendrocyte progenitors from subpallium to pallium during E11 oligodendrogenesis"
slug: spatial-pseudotime-oligodendrogenesis-subpallium-to-pallium-migration
status: supported
confidence: 0.85
tags: [pseudotime, oligodendrogenesis, embryonic-brain, spatial-trajectory]
domain: developmental biology / spatial omics
source_papers:
  - spatial-joint-profiling-dna-methylome-transcriptome
evidence:
  - source: spatial-joint-profiling-dna-methylome-transcriptome
    type: supports
    strength: moderate
    detail: "Quote (p.5): 'Spatial mapping of the pseudotime of each pixel revealed the organized migration of oligodendrocyte progenitor cells from the subpallium to the pallium during oligodendrogenesis (Fig. 3a and Extended Data Fig. 5c)'. Pseudotime computed jointly on spatial DNAm + RNA."
conditions: "E11 mouse embryo; label transfer from scRNA-seq reference (Qiu 2024); pseudotime mapped in space."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

Joint DNAm + RNA spatial pseudotime in E11 mouse embryo recapitulates the canonical subpallium-to-pallium migration of oligodendrocyte progenitor cells during oligodendrogenesis, with pseudotemporal ordering matching the spatial axis of migration.

## Evidence summary

Reported in [[papers/spatial-joint-profiling-dna-methylome-transcriptome]], Fig. 3a; reference scRNA-seq label transfer from Qiu et al. *Nature* 2024.

## Conditions and scope

E11 mouse embryo; single developmental stage; depends on a high-quality external scRNA-seq reference.

## Counter-evidence

None within paper.

## Linked ideas

## Open questions

- Reproduction of the trajectory at finer (10 μm) resolution.
- Comparison of DNAm-only vs joint pseudotime orderings.
