---
title: "CosMx spatial transcriptomics on NSCLC shows TAMs co-expressing CD68 + COL1A1/COL1A2/COL3A1, validating 18_ECMMac in situ"
slug: 18-ecmmac-spatial-cd68-collagen-coexpression
status: supported
confidence: 0.85
tags: [18_ECMMac,CosMx,spatial-transcriptomics,CD68,collagen,validation,NSCLC]
domain: immuno-oncology
source_papers:
  - using-pan-cancer-atlas-investigate-tumour
evidence:
  - source: using-pan-cancer-atlas-investigate-tumour
    type: supports
    strength: medium
    detail: "Quote (p.7, Fig. 4d): 'Analysis of the transcript expression revealed cells co-expressing CD68, COL1A1, COL1A2, and COL3A1'."
conditions: "NanoString CosMx SMI FFPE dataset, 5 NSCLC samples, 960 genes × 771,236 cells; UCell scoring with thresholds >0.8 (in-cluster) and <0.4 (out-of-cluster). Some CD68+ fibroblasts identified — possible intermediate state."
date_proposed: 2026-05-13
date_updated: 2026-05-13
---

## Statement

Spatial-transcriptomic validation of 18_ECMMac in lung tumour tissue: CosMx data identify cells co-expressing the macrophage marker CD68 with collagen transcripts (COL1A1, COL1A2, COL3A1), supporting that the collagen signature is at least partially produced by TAMs rather than only by fibroblasts.

## Evidence summary

Reported in [[papers/using-pan-cancer-atlas-investigate-tumour]] (Coulton et al., *Nat Commun* 2024, Fig. 4d).

## Conditions and scope

5 NSCLC samples; CD68/collagen co-expression is at the transcript level; protein-level validation is absent. Some "fibroblasts" co-express CD68 — possible intermediate state.

## Counter-evidence

Ambient/contaminating transcripts on spatial platforms can yield apparent co-expression without single-cell isolation.

## Linked ideas

## Open questions

- Protein-level (multiplex IHC) confirmation of CD68+ COL1A1+ cells.
- Lineage tracing of macrophage-fibroblast intermediate states.
