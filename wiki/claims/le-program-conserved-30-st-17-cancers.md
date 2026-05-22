---
title: "The LE transcriptional program is conserved across 30 ST samples from 17 cancer types; TC programs are tissue-specific"
slug: le-program-conserved-30-st-17-cancers
status: supported
confidence: 0.85
tags: [pan-cancer, leading-edge, conservation, ST, mechanistic]
domain: oncology/pan-cancer
source_papers:
  - spatial-transcriptomics-reveals-distinct-conserved-tumor
evidence:
  - source: spatial-transcriptomics-reveals-distinct-conserved-tumor
    type: supports
    strength: strong
    detail: "scPred classifier trained on OSCC identifies spatially segregated LE spots in all 30 tested ST samples across 17 cancer types; spatially segregated TC spots are identified in only 15/30 sections, well in cSCC, melanoma, CESC, COAD; lowest LE proportion (1%) in pediatric medulloblastoma and HCC."
conditions: "scPred classification on 30 publicly available ST samples (Abalo et al. 2021 + others)"
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement
The OSCC-derived LE program is identifiable across 30 ST samples spanning 17 cancer types, whereas TC programs transfer well only to cancers with similar (keratinising) tissue origins.

## Evidence summary
Fig. 4d–h and Supplementary Fig. 4a; classifier results per cancer type.

## Conditions and scope
HPV-negative OSCC training; pan-cancer ST evaluation; cross-platform variability not formally controlled.

## Counter-evidence
Medulloblastoma and HCC show only 1% LE spots, indicating limits to LE conservation in highly distinct tissue origins.

## Linked ideas

## Open questions
Whether retraining on a broader pan-cancer ST atlas changes the apparent universality.
