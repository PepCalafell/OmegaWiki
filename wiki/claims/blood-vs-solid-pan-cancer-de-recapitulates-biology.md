---
title: "Blood-vs-solid pan-cancer DE on TPCPA recovers expected immune and adhesion biology"
slug: blood-vs-solid-pan-cancer-de-recapitulates-biology
status: supported
confidence: 0.85
tags: [pan-cancer, differential-expression, blood-cancer, solid-cancer]
domain: oncology
source_papers:
  - pan-cancer-proteome-atlas-mass-spectrometry
evidence:
  - source: pan-cancer-proteome-atlas-mass-spectrometry
    type: supports
    strength: strong
    detail: "Comparing all blood vs all solid cancers, blood-cancer-enriched DE highlights lymphocyte/leukocyte activation, antigen processing/presentation, and phagocytosis; solid-cancer-enriched DE highlights cell adhesion, cytoskeletal organisation, and migration — consistent with prior knowledge of these tumor classes."
conditions: "Bulk DIA-MS proteome; significance assessed with Volcano + clustering."
date_proposed: 2026-05-25
date_updated: 2026-05-25
---

## Statement
Pan-cancer supervised analysis comparing blood vs solid tumors at the proteome level recapitulates expected biology: immune-cell activation and antigen presentation for blood cancers, cell adhesion and migration for solid cancers — providing a sanity check on the TPCPA dataset and the underlying DIA-MS approach.

## Evidence summary
- Knol et al. 2025 Figures S5A–S5D.

## Conditions and scope
- Bulk proteome; tissue-of-origin contributes substantially to these signals.

## Counter-evidence
- Top "solid cancer" GO terms partly reflect tissue identity rather than malignancy per se.

## Linked ideas

## Open questions
- Which proteins drive solid-cancer biology after removing tissue-of-origin contributions?
