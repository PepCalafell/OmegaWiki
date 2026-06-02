---
title: "Proteomics-derived signatures separate proinflammatory macrophages in patient tumor scRNA-seq"
slug: proteomic-signatures-separate-proinflammatory-macrophages-patient
status: supported
confidence: 0.8
tags:
  - macrophage
  - proteomics
  - signature
  - scRNA-seq
  - TAM
domain: immunology
source_papers:
  - delineation-signaling-routes-underlie-differences-macrophage
evidence:
  - source: delineation-signaling-routes-underlie-differences-macrophage
    type: supports
    strength: strong
    detail: "Proteomics-derived M1/M2 signatures applied to HCC and brain-metastasis scRNA-seq separated proinflammatory macrophages; M1-like cells enriched in IFN-γ/TNFA-NFKB/inflammatory hallmarks; up to 89% classified M1-like depending on annotation."
conditions: "Public tumor scRNA-seq (HCC: Sharma et al.; brain metastases: Gonzalez et al.); gene-set activity / ModuleScore."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement
Protein-level signatures of in vitro M1 vs M2 macrophages transfer to single-cell RNA-seq of patient tumors and successfully separate proinflammatory from immunosuppressive macrophage populations.

## Evidence summary
- "the signature proteins defined here through the proteome characterization of in vitro macrophages were able to distinguish proinflammatory macrophages in the both analyzed clinical single cell datasets" with M1-like cells strongly enriched in inflammatory hallmark pathways (IFN-γ, TNFA-NFKB, inflammatory response; FDR < 0.05) (p.14).
- "up to 89% of the identified macrophages were classified as M1-like, proinflammatory cells" (p.14).

## Conditions and scope
Validates a coarse proinflammatory-vs-immunosuppressive axis in clinical scRNA-seq; signatures derived from in vitro monocyte-derived macrophages.

## Counter-evidence
None within the paper; this refines (does not refute) the limitation that the full M1/M2 axis under-describes in vivo TAMs.

## Linked ideas

## Open questions
Can proteomic signatures also resolve immunosuppressive sub-states (not just the proinflammatory pole) in vivo?
