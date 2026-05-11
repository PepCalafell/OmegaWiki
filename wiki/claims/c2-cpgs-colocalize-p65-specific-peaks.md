---
title: "Cluster C2 CpGs co-localize exclusively with p65-specific ChIP-seq peaks, not HIF1α (Fisher P = 8.3×10⁻¹⁰³)"
slug: c2-cpgs-colocalize-p65-specific-peaks
status: supported
confidence: 0.95
tags:
  - cluster-C2
  - p65
  - RELA
  - ChIP-seq
  - DNA-methylation
  - colocalization
domain: "epigenetics"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: strong
    detail: "ChIP-seq signal around C2 CpG coordinates plus Fisher's exact test for overlap of peak sets with C2 (Calafell 2024 Fig. 4I-J). p65-specific peak set: enrichment for C2 with P = 8.3×10⁻¹⁰³. HIF1α peak signal is not notably enriched at C2 regions."
conditions: "Genomic coordinate overlap; peak set definitions from ChIP-seq clustering."
date_proposed: 2026-05-11
date_updated: 2026-05-11
---

## Statement

The 403 cluster C2 CpGs co-localize exclusively with the p65-specific ChIP-seq peak set (P1), not with HIF1α peaks. Fisher's exact test on coordinate overlap yields P = 8.3×10⁻¹⁰³ — among the strongest statistical anchors in the paper. This directly couples the C2 hypomethylation signature to p65 binding rather than HIF1α binding.

## Evidence summary

- ChIP-seq signal profile plot at C2 coordinates (Calafell 2024 Fig. 4I).
- Fisher's exact test on peak-set overlaps with C2 (Fig. 4J).

## Conditions and scope

- mMAC1 condition; coordinate-based overlap; does not include cobound peaks separately.

## Counter-evidence

- None directly; pharmacological dissection (p65 inhibitor) corroborates the chromatin colocalization.

## Linked ideas

- Foundation for the pharmacological dissection in claim p65-inhibition-blocks-hypoxia-specific-demethylation.

## Open questions

- Direct TET2 ChIP-seq at C2 would close the loop (NF-κB → TET2 recruitment).
