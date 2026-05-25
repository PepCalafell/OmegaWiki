---
title: "EPIC and CIBERSORT deconvolution perform poorly on bulk proteome data; Tamborero signature ssGSEA is preferred"
slug: cibersort-epic-fail-bulk-proteome-tamborero-preferred
status: supported
confidence: 0.75
tags: [deconvolution, cibersort, epic, tamborero, proteome, immune-infiltration]
domain: methods
source_papers:
  - pan-cancer-proteome-atlas-mass-spectrometry
evidence:
  - source: pan-cancer-proteome-atlas-mass-spectrometry
    type: supports
    strength: moderate
    detail: "Authors report that EPIC and CIBERSORT deconvolution did not yield meaningful results on solid tumor bulk protein expression (data not shown); Tamborero ssGSEA signatures were selected as the preferred approach for immune subtyping, with superior separation of non-solid vs solid tumors."
conditions: "Bulk protein expression input; solid tumor cohort."
date_proposed: 2026-05-25
date_updated: 2026-05-25
---

## Statement
On bulk-tissue TPCPA proteomes, transcriptome-trained deconvolution tools (EPIC, CIBERSORT) failed to produce meaningful immune-cell estimates. Marker-set ssGSEA against Tamborero immune signatures gave the most coherent separation of solid vs non-solid tumors and was therefore used for downstream CRC immune subtyping.

## Evidence summary
- Knol et al. 2025 — text after Figures 4B–4D; "data not shown" claim regarding EPIC/CIBERSORT failure on bulk proteome.
- Supporting Figure S4D shows MS-derived hematopoietic signatures clustering individual cancer samples.

## Conditions and scope
- Bulk tissue only; deconvolution tools were not retrained on protein-level reference profiles.

## Counter-evidence
- The authors note that EPIC/CIBERSORT also performed poorly on RNA-seq for bulk tumors (ref 72), so this may be a bulk-tissue limitation rather than a proteome-specific one.

## Linked ideas

## Open questions
- Could a protein-level deconvolution reference (akin to CIBERSORTx for RNA) restore EPIC/CIBERSORT-style accuracy on bulk proteomes?
