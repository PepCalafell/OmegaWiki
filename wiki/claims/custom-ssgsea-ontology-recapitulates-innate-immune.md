---
title: "A custom 5-pathway ssGSEA ontology recapitulates innate immune activation by viral and bacterial stimuli"
slug: custom-ssgsea-ontology-recapitulates-innate-immune
status: supported
confidence: 0.75
tags: [ssGSEA, innate-immunity, methodological, validation]
domain: methods / immunology
source_papers:
  - genomic-investigation-innate-sensing-pathways-tumor
evidence:
  - source: genomic-investigation-innate-sensing-pathways-tumor
    type: supports
    strength: moderate
    detail: "TLR ssGSEA score rose in LPS-stimulated mouse BMDMs (4/72 h) tracking Il6/Tnf; NOD and RIG-I scores rose in RSV-infected A549 cells (24/48 h) tracking interferon genes (Fig. 1B-F)."
conditions: "Validated only on two public stimulus datasets (LPS/TLR, RSV/RIG-I-NOD); transcriptional proxy, not protein activity."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Single-sample GSEA over a manually curated gene-set ontology for the cGAS, TLR, CLR, NOD/NLR, and RIG-I cascades produces per-pathway activation scores that move in the expected direction under known innate stimuli.

## Evidence summary

LPS (a TLR4 ligand) raised TLR scores in BMDMs concordant with Il6/Tnf induction; RSV viral infection raised NOD and RIG-I scores in A549 cells concordant with type-I interferon induction.

## Conditions and scope

Methodological validation on a small number of in vitro stimulus datasets; establishes face validity of the scoring approach, not its quantitative accuracy.

## Counter-evidence

None reported in the paper; generalization beyond the tested stimuli/pathways is untested.

## Linked ideas

## Open questions

Do the scores capture signaling activation or merely receptor/effector expression? See [[concepts/innate-immune-pathway-ssgsea-immunophenotyping-pan]].
