---
title: "Spatial constraints remove scRNA-seq false-positive ligand-receptor interactions and recover missed ones"
slug: spatial-constraint-reduces-false-lr-interactions
status: supported
confidence: 0.8
tags: [cell-cell-interaction, ligand-receptor, spatial-omics, methods]
domain: methods
source_papers:
  - integrating-12-spatial-single-cell-technologies
evidence:
  - source: integrating-12-spatial-single-cell-technologies
    type: supports
    strength: strong
    detail: "stLearn SCTP on CosMx revealed interactions predicted by scRNA-seq with no colocalization (likely false positives, e.g. XCL1-XCR1) and interactions missed by scRNA-seq but detected spatially (e.g. WNT5A-ROR1); Visium/CosMx/Xenium concordantly supported pairs missed by scRNA-seq (CXCL12-CXCR4, CCL9-CCR7). (p.10, Fig S19)"
conditions: "Comparison of dissociated scRNA-seq inference vs spatially-constrained inference."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Adding spatial-neighbour constraints to ligand-receptor inference (stLearn SCTP) removes biologically implausible interactions predicted by dissociated scRNA-seq (e.g. XCL1-XCR1) and recovers genuine interactions scRNA-seq missed (e.g. WNT5A-ROR1, CXCL12-CXCR4), improving accuracy and specificity.

## Evidence summary

Direct contrast of scRNA-seq vs spatial predictions across CosMx/Visium/Xenium, with visual co-expression support for recovered pairs. (p.10)

## Conditions and scope

General methodological claim, demonstrated on skin cancer spatial data.

## Counter-evidence

Spatial co-expression remains inference, not direct binding proof.

## Linked ideas

## Open questions

Quantitative false-positive/false-negative rates vs a ground truth.
