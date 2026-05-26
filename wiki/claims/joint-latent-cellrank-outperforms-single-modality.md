---
title: "cellRank on the GLUE joint latent space outperforms single-modality cellRank for CLP/pre-pDC/MDP/pre-mDC lineage assignment"
slug: joint-latent-cellrank-outperforms-single-modality
status: supported
confidence: 0.9
tags: [cellRank, multi-omics, integration, lineage-assignment, quantitative, GLUE]
domain: single-cell methods / trajectory inference
source_papers:
  - mapping-early-human-blood-cell-differentiation
evidence:
  - source: mapping-early-human-blood-cell-differentiation
    type: supports
    strength: strong
    detail: "Quote (p.5): 'correct lineage assignments of CLP, pre-pDC, MDP, and pre-mDC improved from 86% to 91% on the RNA cells and from 65% to 95% on the protein cells (fig. S12D). Taken together, our results indicated that the cellRank model based on the joint latent space outperformed the models based on CITE-seq or scp-MS alone.'"
conditions: "cellRank with pseudotime kernel; comparison across CITE-seq-only, scp-MS-only, and joint-latent-space configurations."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Quantitative gain from multi-omics integration: lineage assignment for the dendritic-cell branch (CLP/pre-pDC/MDP/pre-mDC) improves from 86% (RNA-only) and 65% (protein-only) to 91% / 95% (joint) — a substantial improvement, particularly on the protein cells.

## Evidence summary

Direct comparison of cellRank fits across three configurations. Reported in [[papers/mapping-early-human-blood-cell-differentiation]] (fig. S12D).

## Conditions and scope

Healthy adult human BM CD34+ HSPC dendritic-cell branch.

## Counter-evidence

None within scope.

## Linked ideas

## Open questions

- Generality of the joint-latent-space advantage across other lineages and disease states.
