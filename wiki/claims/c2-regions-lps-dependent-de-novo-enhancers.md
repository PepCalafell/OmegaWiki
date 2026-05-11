---
title: "Cluster C2 regions are LPS-dependent de novo enhancers, gaining H3K4me1 and H3K27ac upon activation"
slug: c2-regions-lps-dependent-de-novo-enhancers
status: supported
confidence: 0.8
tags:
  - cluster-C2
  - enhancer
  - H3K4me1
  - H3K27ac
  - DNA-methylation
  - chromatin
domain: "epigenetics"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: moderate
    detail: "Reanalysis of public MAC histone ChIP-seq data shows C2 regions gain H3K4me1 (canonical enhancer) and H3K27ac (active enhancer) histone marks upon LPS activation. C2 also displays highest enrichment for human MO enhancer chromatin state. Authors propose C2 = LPS-dependent de novo enhancers (Calafell 2024 fig. S1E)."
conditions: "Public histone ChIP-seq reanalysis; ChromHMM-style chromatin state annotation."
date_proposed: 2026-05-11
date_updated: 2026-05-11
---

## Statement

The 403 CpGs of cluster C2 are predominantly located at distal regulatory elements that acquire de novo enhancer marks (H3K4me1, H3K27ac) upon LPS activation. C2 is the methylation-dynamic mark of LPS-inducible enhancers that overlap with NF-κB binding.

## Evidence summary

- Reanalysis of public histone ChIP-seq data (Calafell 2024 fig. S1E).
- C2 gains H3K4me1/H3K27ac upon LPS activation in normoxia; methylation-dynamic regions canonically co-localize with distal regulatory elements.

## Conditions and scope

- Inferred from public histone ChIP-seq + ChromHMM-style chromatin state mapping, not generated in this study.

## Counter-evidence

- Direct experimental validation (e.g., enhancer-reporter assay or perturbation) not performed here.

## Linked ideas

- LPS-inducible NF-κB enhancers are a well-described class; C2 is the methylation-dynamic subset under hypoxia.

## Open questions

- Whether C2 enhancers are functionally required (CRISPRi screen).
- Whether NF-κB binding precedes or follows H3K4me1 deposition.
