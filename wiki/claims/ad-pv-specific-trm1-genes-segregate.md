---
title: "AD- and PV-specific Trm1 genes segregate discretely in coexpression and STRING networks"
slug: ad-pv-specific-trm1-genes-segregate
status: supported
confidence: 0.8
tags: [skin, trm, network, string, atopic-dermatitis, psoriasis, methods]
domain: immunology / network biology
source_papers:
  - classification-human-chronic-inflammatory-skin-disease
evidence:
  - source: classification-human-chronic-inflammatory-skin-disease
    type: supports
    strength: strong
    detail: "Quote (p.5): 'These two groups showed significantly smaller linkages between the two groups than in multiple permutation tests that randomly assigned these genes to the AD- and PV-specific categories (P = 0.001).' 98 protein nodes, 394 interactions; normalized cut score on STRING network."
conditions: "qgraph coexpression network and STRING PPI network; 100,000-permutation null for normalized cut."
date_proposed: 2026-06-10
date_updated: 2026-06-10
---

## Statement

AD- and PV-specific Trm1 genes formed two discretely segregated modules in both a single-cell coexpression correlation network and an external STRING protein-protein interaction network, with a normalized-cut permutation test confirming significantly fewer cross-module than within-module linkages (P = 0.001), indicating coherent, biologically cooperative disease-specific pathways.

## Evidence summary

Reported in Results of [[papers/classification-human-chronic-inflammatory-skin-disease]] using [[foundations/qgraph-network-visualization]] and [[foundations/string-protein-protein-interaction-database]]. Supports [[concepts/trm1-th2-th17-molecular-classification-inflammatory]].

## Conditions and scope

Network segregation partly expected since DEGs were discovered via expression differences; STRING corroboration adds independent functional evidence.

## Counter-evidence

The authors acknowledge the transcriptional-network segregation is partly circular; STRING provides the orthogonal check.

## Linked ideas

## Open questions

- Do the two modules map to distinct druggable pathway hubs?
