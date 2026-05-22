---
title: "TC and LE annotations rest on Louvain clustering plus literature HNSCC markers (CLDN4/SPRR1B for TC, LAMC2/ITGA5 for LE)"
slug: tc-le-louvain-annotation-cldn4-lamc2-markers
status: supported
confidence: 0.8
tags: [methodological, OSCC, annotation, HNSCC-markers]
domain: methods/spatial-transcriptomics
source_papers:
  - spatial-transcriptomics-reveals-distinct-conserved-tumor
evidence:
  - source: spatial-transcriptomics-reveals-distinct-conserved-tumor
    type: supports
    strength: moderate
    detail: "Phylogenetic tree of 14 Louvain clusters collapses into 3 nodal clusters; cluster 1 = TC (CLDN4, SPRR1B high), cluster 3 = LE (LAMC2, ITGA5 high), cluster 2 = transitory (mixed DEGs). Marker assignments follow Puram et al. 2017."
conditions: "Seurat v4.3.0 BuildClusterTree; resolution 1.0; ape v5.6-2 visualisation"
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement
The OSCC TC, LE and transitory clusters are defined by Louvain clustering of malignant spots followed by phylogenetic-tree-guided collapse into three nodal clusters, each annotated using literature-validated HNSCC markers.

## Evidence summary
14 Louvain clusters → 3 nodal clusters. Per-cluster DEGs and nebulosa kernel-density plots of CLDN4, SPRR1B (TC) and LAMC2, ITGA5 (LE) confirm the assignment.

## Conditions and scope
HPV-negative OSCC, Visium 10x, Seurat-based pipeline.

## Counter-evidence
None within the paper. The choice of resolution = 1.0 is not formally calibrated.

## Linked ideas

## Open questions
Robustness of the annotation to clustering resolution and to alternative marker sets.
