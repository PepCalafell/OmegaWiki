---
title: "HIF-α activation can be uncoupled from O₂: PIM1 phosphorylates HIF-1α to block PHD binding; iASPP binds pVHL to block HIF-1α degradation"
slug: hif-uncoupled-from-oxygen-pim1-iaspp
status: supported
confidence: 0.80
tags:
  - HIF1A
  - PIM1
  - iASPP
  - VHL
  - oxygen-independent-HIF
  - kinase
  - post-translational-modification
  - cancer
domain: "molecular-biology / hypoxia / kinase-signaling"
source_papers:
  - hypoxia-driven-crosstalk-between-tumor-tumor
evidence:
  - source: hypoxia-driven-crosstalk-between-tumor-tumor
    type: supports
    strength: strong
    detail: "Bai 2022 (DOI 10.1186/s12943-022-01645-2, p.5) summarizes two oxygen-independent HIF-α activation mechanisms: (1) PIM1 kinase directly phosphorylates HIF-1α regardless of oxygen tension, preventing PHDs from binding (Casillas 2021 Oncogene); (2) iASPP (PPP1R13L) binds pVHL and prevents HIF-1α degradation without affecting hydroxylation (Zhao 2022 Oncogene). Both are oncogenic HIF-α activation routes operating under normoxia."
conditions: "Cancer-cell contexts; both mechanisms documented in vitro and in xenograft tumor models."
date_proposed: 2026-05-11
date_updated: 2026-05-11
---

## Statement

The canonical PHD/VHL axis treats HIF-α stability as an O₂-sensitive switch — but oncogenic conditions can uncouple HIF-α stabilization from O₂ availability through two distinct mechanisms documented in 2021-2022:

1. **PIM1 phospho-stabilization**: The PIM1 serine/threonine kinase directly phosphorylates HIF-1α at residue(s) that prevent PHD binding, regardless of oxygen tension. PIM1 is overexpressed in multiple cancers (AML, prostate, breast, oral SCC) and constitutively stabilizes HIF-1α under normoxia.

2. **iASPP-pVHL block**: iASPP (PPP1R13L, an inhibitor of the apoptotic-stimulating-protein-family) binds directly to pVHL and blocks HIF-1α degradation without affecting hydroxylation. iASPP overexpression in tumors causes pseudo-hypoxia: HIF-1α accumulates and drives target genes under normoxia.

These mechanisms (and the OEA endogenous ligand of HIF-3α PAS-B, Diao 2022 Nat Commun) widen the cellular contexts in which the HIF pathway is active beyond strict hypoxia, complicating the assumption that HIF-α stabilization is a clean marker of low pO₂.

## Evidence summary

- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — Bai 2022 *Molecular Cancer*.
- Foundations: [[foundations/hif1a]].
- Primary literature: Casillas 2021 Oncogene (PIM1); Zhao 2022 Oncogene (iASPP); Diao 2022 Nat Commun (OEA-HIF3α).

## Conditions and scope

- PIM1: cancers with high PIM1 expression (AML, prostate, breast, OSCC).
- iASPP: cancers with high iASPP expression.
- The mechanisms are mostly tumor-cell-intrinsic; whether they operate in TAMs is less explored.

## Counter-evidence

- Quantitative dominance: under genuine hypoxia, canonical PHD/VHL inactivation drives most HIF-α stabilization; PIM1 / iASPP contribute fractionally.
- iASPP also has p53-related apoptotic-modulator functions that may indirectly affect tumor biology.

## Linked ideas

(none yet)

## Open questions

- Are HIF-2α phospho-stabilization mechanisms analogous to PIM1-HIF-1α documented in any cancer setting?
- Does PIM1 inhibition (e.g. SGI-1776) sensitize PIM1-high tumors to HIF-1α-targeted therapies?
- Can iASPP-pVHL be drugged as a PPI to restore pVHL function in iASPP-overexpressing tumors?
