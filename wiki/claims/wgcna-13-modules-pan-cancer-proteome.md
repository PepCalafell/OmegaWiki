---
title: "WGCNA on TPCPA yields 13 protein co-expression modules with tissue-correlated and pan-cancer biology"
slug: wgcna-13-modules-pan-cancer-proteome
status: supported
confidence: 0.85
tags: [wgcna, co-expression, hub-proteins, drug-targets, tpcpa]
domain: oncology
source_papers:
  - pan-cancer-proteome-atlas-mass-spectrometry
evidence:
  - source: pan-cancer-proteome-atlas-mass-spectrometry
    type: supports
    strength: strong
    detail: "Weighted gene co-expression network analysis identifies 13 modules; top 5 hub proteins per module defined by eigenprotein correlation; modules link to GO biology (e.g., module 5 → cell adhesion + nucleotide sugar biosynthesis, module 6 → stress + chaperones)."
conditions: "Bulk DIA-MS protein expression; module/eigenprotein definitions per WGCNA defaults."
date_proposed: 2026-05-25
date_updated: 2026-05-25
---

## Statement
WGCNA applied to TPCPA pan-cancer proteomes resolves the proteome into 13 co-expression modules. Several modules track normal-tissue signatures; others (e.g., module 6 stress, module 11 immune/antigen presentation) recur across cancers. Hub proteins surface as candidate drug targets independent of canonical cancer-gene lists.

## Evidence summary
- Figure 3A–C; Table S3 (GO statistics).
- Module 5/6 show heatmap enrichment in colon cancer; module 12 in blood cancers.

## Conditions and scope
- Co-expression structure is bulk-tissue; cell-type-specific networks would require deconvolution or single-cell data.

## Counter-evidence
- Tissue signatures partially confound modules (e.g., module 7 mitochondrial / liver).

## Linked ideas

## Open questions
- Are module hub proteins more druggable than DE-derived markers in matched cancer models?
