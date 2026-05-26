---
title: "scp-MS UMAP embedding recapitulates the human HSPC differentiation hierarchy (HSC/MPP → LMPP → GMP / CLP / MEP branches)"
slug: scp-ms-umap-recapitulates-hspc-hierarchy
status: supported
confidence: 0.9
tags: [scp-MS, HSPC, hierarchy, UMAP, correlational]
domain: single-cell proteomics / hematology
source_papers:
  - mapping-early-human-blood-cell-differentiation
evidence:
  - source: mapping-early-human-blood-cell-differentiation
    type: supports
    strength: strong
    detail: "Quote (p.2): 'Overlaying the cell identities derived from the two different cell-sorting strategies onto the UMAP embedding revealed clustering and branching of the sorted (en-riched) populations based on the HSPC differentiation hierarchy (Fig. 1D). Hematopoietic stem cells (HSCs) and multipotent progenitors (MPPs) were primarily located at the top of the hierarchy as a mixed and heterogeneous population… Downstream of HSCs/MPPs followed lymphoid-primed multipotent progenitors (LMPPs), which tended to be located upstream of granulocyte-macrophage progenitors (GMPs) and common lymphoid progenitors (CLPs) branches.'"
conditions: "FACS-gated and total-HSPC random-sampling strategies; UMAP on SCeptre-processed scp-MS data."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Protein-level scp-MS data alone recapitulates the canonical human HSPC hierarchy, validating scp-MS as a discovery-mode tool for in vivo differentiation systems.

## Evidence summary

Two independent FACS strategies map consistently onto the scp-MS UMAP. Reported in [[papers/mapping-early-human-blood-cell-differentiation]] (Fig. 1D).

## Conditions and scope

Healthy adult human bone marrow.

## Counter-evidence

CMP gate is heterogeneous and splits between BaEoMa and myeloid branches — a refinement, not a contradiction.

## Linked ideas

## Open questions

- Does the same hierarchy hold in pediatric or aged BM?
