---
title: "Mesenchymal-like CSCs (CD44+) localise to LE; epithelial-like CSCs (CD24+) localise to TC"
slug: ecsc-tc-mcsc-le-cd24-cd44-localization
status: supported
confidence: 0.75
tags: [CSC, EMT, CD24, CD44, OSCC, mechanistic]
domain: oncology/cancer-stem-cells
source_papers:
  - spatial-transcriptomics-reveals-distinct-conserved-tumor
evidence:
  - source: spatial-transcriptomics-reveals-distinct-conserved-tumor
    type: supports
    strength: moderate
    detail: "mCSC gene-set score higher in LE (p=2e-4); eCSC gene-set score higher in TC (p=1.5e-6). Immunofluorescence on serial tissue sections confirms CD24 in TC and CD44 in LE. Total CSC marker expression does not differ between TC and LE (p>0.05)."
conditions: "Nebulosa kernel density on Liu et al. eCSC/mCSC signatures; IF validation in serial sections"
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement
Within OSCC ST data, mesenchymal-like CSC states (CD44+) preferentially occupy the LE while epithelial-like CSC states (CD24+) preferentially occupy the TC, although the overall CSC marker density does not differ between TC and LE.

## Evidence summary
Module scoring of eCSC and mCSC gene sets; UMAP and per-spot density plots; orthogonal IF on serial sections.

## Conditions and scope
HPV-negative OSCC, Visium spots, IF on serial sections; reliance on canonical OSCC CSC markers.

## Counter-evidence
Total CSC marker expression is comparable between TC and LE, indicating CSC abundance is similar but cell-state identity differs.

## Linked ideas

## Open questions
Whether the CD24/CD44 polarity is functional (lineage tracing) or only correlative.
