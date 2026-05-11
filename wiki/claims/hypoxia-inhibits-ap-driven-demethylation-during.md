---
title: "Hypoxia partially blocks AP-1-driven DNA demethylation that normally occurs during macrophage differentiation (cluster C1)"
slug: hypoxia-inhibits-ap-driven-demethylation-during
status: supported
confidence: 0.85
tags:
  - hypoxia
  - DNA-methylation
  - TET-inhibition
  - AP-1
  - macrophage-differentiation
  - cluster-C1
domain: "epigenetics"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: strong
    detail: "EPIC array DMPs (FDR<0.05, |Δβ|>0.2) cluster into 3 sets. C1 (2782 CpGs) is hypomethylated during normoxic MAC differentiation (vs MO), AP-1-motif-enriched. In hypoxia, the demethylation tendency is partially inhibited — consistent with hypoxic TET inhibition (Thienpont 2016). Fig. 1E-F."
conditions: "M-CSF MAC differentiation 5d, 1% vs 21% O2; EPIC array vs MO baseline; AP-1 motif by HOMER."
date_proposed: 2026-05-11
date_updated: 2026-05-11
---

## Statement

The largest DMP cluster (C1, 2782 CpGs) during normal MO→MAC differentiation is hypomethylated in normoxia and enriched in AP-1 motifs (canonically associated with MAC differentiation). Under hypoxia, this demethylation is partially inhibited — consistent with global hypoxic TET inhibition. This is the *expected* hypoxic-TET phenotype that mMAC1's NF-κB-driven C2 cluster paradoxically overrides at a focal subset of CpGs.

## Evidence summary

- EPIC array DMP clustering (Calafell 2024 Fig. 1E).
- HOMER motif analysis on cluster C1 (Fig. 1F).
- Consistent with Thienpont et al. 2016 (Nature) showing tumor hypoxia → DNA hypermethylation via TET activity reduction.

## Conditions and scope

- Comparison: differentiated MACs vs starting MOs.
- AP-1 family TFs as the canonical drivers of the C1 demethylation program.

## Counter-evidence

- The C2 cluster (NF-κB-enriched) demethylates *despite* the hypoxic environment — focal NF-κB-driven exception.

## Linked ideas

- Frames the C2 finding as a *paradoxical* exception to the global rule (Thienpont 2016).

## Open questions

- TET isoform specificity for C1 vs C2 demethylation.
- Whether AP-1 binding is itself reduced in hypoxia or whether AP-1 binds but TET cannot demethylate.
