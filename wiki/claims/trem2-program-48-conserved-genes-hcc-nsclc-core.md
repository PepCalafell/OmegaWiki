---
title: "48 conserved genes form the core TREM2 mac program across HCC and NSCLC TREM2hi vs TREM2lo mo-macs"
slug: trem2-program-48-conserved-genes-hcc-nsclc-core
status: supported
confidence: 0.85
tags:
  - TREM2-program
  - HCC
  - NSCLC
  - conserved-program
  - cross-tissue
domain: "tumor immunology / comparative genomics"
source_papers:
  - trem2-macrophages-associated-enhanced-response-pd
evidence:
  - source: trem2-macrophages-associated-enhanced-response-pd
    type: supports
    strength: strong
    detail: "DEGs distinguishing TREM2hi from TREM2lo mo-macs computed separately in HCC and NSCLC scRNA-seq datasets, intersected to yield 48 conserved genes. Projection of this conserved signature onto PDAC and TNBC scRNA-seq atlases successfully identifies TREM2 macs there too (Fig. 3b, Fig. S3f)."
conditions: "Cross-dataset comparison; TREM2hi vs TREM2lo within-tissue DEGs intersected; tested in PDAC and TNBC datasets."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Cross-tissue comparison of TREM2hi-vs-TREM2lo mo-mac DEGs between HCC and NSCLC yields 48 conserved genes, defining a core TREM2 program preserved across tumor types. The same signature successfully identifies TREM2 macs in PDAC and TNBC datasets.

## Evidence summary

- Independent DEG calculation in HCC and NSCLC.
- Intersection: 48 conserved genes.
- Projection test on PDAC + TNBC validates pan-cancer applicability.

## Conditions and scope

- Cross-dataset batch effects may bias conservation estimates.
- Conservation does not imply identical function.

## Counter-evidence

- Conserved program does NOT predict response in NSCLC POPLAR ([[claims/trem2-program-fails-stratify-poplar-nsclc-atezo]]) — functional output diverges despite transcriptional core conservation.

## Linked ideas

- [[concepts/trem2-tumor-associated-macrophage]]
- [[concepts/tissue-specific-tam-function-context-dependence]]

## Open questions

- Which genes within the 48-core drive lipid handling / efferocytosis vs immunomodulation?
