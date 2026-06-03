---
title: "CKIs with identical designated targets produce largely divergent epigenomic effects"
slug: ckis-identical-designated-targets-produce-divergent
status: supported
confidence: 0.85
tags:
  - mechanistic
  - correlational
  - kinase-inhibitors
  - polypharmacology
domain: pharmacology / epigenomics
source_papers:
  - integrative-epigenome-based-strategy-unbiased-functional
evidence:
  - source: integrative-epigenome-based-strategy-unbiased-functional
    type: supports
    strength: strong
    detail: "In 2D KNN network graphs, CKIs with identical/similar designated targets showed no evident correlation; relative positions and nearest neighbors differed between LPS and IL-4 contexts, attributed to polypharmacology."
conditions: "BMDM; LPS and IL-4; perturbation-likelihood network."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Clinical kinase inhibitors sharing the same designated target generate largely different epigenomic effects, so the functional scope of a CKI cannot be reliably inferred from current clinical target annotations.

## Evidence summary

KNN network graphs of CKI similarity (from H3K27ac perturbation likelihoods) showed no clustering by designated target, and nearest neighbors changed between LPS and IL-4 contexts — consistent with the [[concepts/polypharmacology-clinical-kinase-inhibitors]] and the [[concepts/discordance-between-vitro-kinase-inhibitor-selectivity]].

## Conditions and scope

Mouse BMDM; two stimuli; effects measured at the kinobeads EC50 of the intended target.

## Counter-evidence

Kinobeads-assigned (rather than designated) target families did show reduced intra-family distances — partial structure exists at the binding-assay level.

## Linked ideas

## Open questions

- How much of the divergence is attributable to specific off-targets vs concentration effects?
