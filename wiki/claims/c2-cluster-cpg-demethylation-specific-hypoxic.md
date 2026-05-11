---
title: "Cluster C2 (403 CpGs) shows hypoxia-specific NF-κB-motif-enriched DNA demethylation in LPS-activated macrophages"
slug: c2-cluster-cpg-demethylation-specific-hypoxic
status: supported
confidence: 0.9
tags:
  - cluster-C2
  - DNA-demethylation
  - NF-kB
  - hypoxia
  - macrophage
  - IL6
  - TNF
domain: "epigenetics"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: strong
    detail: "EPIC array, 403 CpGs hypomethylated specifically in mMAC1 vs mMAC21 (Fig. 1E). HOMER motif enrichment in C2 dominated by NF-κB family (Fig. 1F). IL6 and TNF among C2 examples (fig. S1C). C2 also enriched for H3K4me1/H3K27ac de novo enhancer marks (fig. S1E)."
conditions: "Human M-CSF MACs, EPIC array, mMAC1 vs mMAC21, FDR<0.05, |Δβ|>0.2."
date_proposed: 2026-05-05
date_updated: 2026-05-11
---

## Statement

A focal cluster of 403 CpGs (cluster C2) undergoes specific de novo DNA demethylation in hypoxic LPS-activated macrophages (mMAC1) — not in any other condition (iMAC21, iMAC1, mMAC21). C2 is strongly enriched in NF-κB family motifs and contains IL6 and TNF loci. This is the focal exception that overrides global hypoxic TET inhibition.

## Evidence summary

- EPIC methylation array, n=4 biological replicates per condition.
- 403 CpGs grouped via unsupervised clustering of differential DMPs (Calafell 2024 Fig. 1E).
- HOMER motif analysis: NF-κB top family, with AP-1 secondary (Fig. 1F).
- IL6 and TNF promoter/enhancer CpGs are members of C2 (fig. S1C), tying the methylation to cytokine output.
- C2 regions gain H3K4me1 (canonical enhancer) and H3K27ac (active enhancer) histone marks de novo upon LPS in normoxia (fig. S1E), consistent with LPS-responsive distal regulatory elements.

## Conditions and scope

- mMAC1 specifically; not present in iMAC1, mMAC21, or iMAC21.
- 1% O₂ + LPS 48h after M-CSF differentiation.

## Counter-evidence

- None directly contradicting; the paradox is explained by NF-κB recruitment overriding hypoxic TET inhibition (claim: p65-inhibition-blocks-hypoxia-specific-demethylation).

## Linked ideas

- Core concept: [[concepts/cluster-c2-hypoxia-hypomethylation-signature]].
- Mechanism: [[concepts/nf-kb-mediated-dna-demethylation-hypoxia]].

## Open questions

- TET isoform specificity (TET1/2/3) at C2 CpGs.
- Whether C2 demethylation precedes or follows NF-κB binding (sequence resolution).
- Reversibility upon re-oxygenation.
