---
title: "Literature-proposed TAM subset markers (Ma et al. 2022) vary in atlas-level cluster specificity; APOE/APOC1/ARG1/HES1 are broadly distributed"
slug: ma-markers-vary-cluster-specificity
status: supported
confidence: 0.85
tags: [TAM-markers,Ma-2022,MKI67,LYVE1,CXCL9,APOE,ARG1,specificity]
domain: immuno-oncology
source_papers:
  - using-pan-cancer-atlas-investigate-tumour
evidence:
  - source: using-pan-cancer-atlas-investigate-tumour
    type: supports
    strength: strong
    detail: "Quote (p.9, Fig. 5c-d): 'Markers attributed to proliferating macrophages, including MKI67 and CDK1 can be attributed to the former category, the majority of cells expressing these genes belonging to cluster 14_ProliMac. Similarly, cells expressing LYVE1 and FOLR2 primarily belonged to cluster 1_MetM2Mac, whilst cells expressing CXCL9 mainly belonged to cluster 8_IFNGMac. Markers distributed among a large number of clusters included APOE, APOC1, ARG1 and HES1'."
conditions: "Per-cluster proportion of positive cells along expression percentile of each Ma marker."
date_proposed: 2026-05-13
date_updated: 2026-05-13
---

## Statement

When assessed against a high-resolution 23-cluster pan-cancer TAM atlas, the literature-curated TAM subset markers proposed by Ma et al. (2022, Trends Immunol) vary in specificity: MKI67/CDK1 → 14_ProliMac, LYVE1/FOLR2 → 1_MetM2Mac, and CXCL9 → 8_IFNGMac are cluster-specific, whereas APOE, APOC1, ARG1, and HES1 are widely distributed across many clusters and therefore not subset-defining.

## Evidence summary

Reported in [[papers/using-pan-cancer-atlas-investigate-tumour]] (Coulton et al., *Nat Commun* 2024, Fig. 5c-d).

## Conditions and scope

Specificity is a property of the 23-cluster atlas at its chosen resolution; different resolutions or atlases could change the spread.

## Counter-evidence

Broadly-distributed markers (APOE, APOC1) may still distinguish broader functional axes (e.g., lipid-associated state) even if not single-cluster-defining.

## Linked ideas

## Open questions

- Build a hierarchical taxonomy that explicitly separates "subset-defining" from "broad functional state" markers.
