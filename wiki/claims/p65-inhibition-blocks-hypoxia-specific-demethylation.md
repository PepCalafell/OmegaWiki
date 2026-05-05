---
title: "p65 inhibition (BAY11-7082) blocks hypoxia-specific C2 demethylation in mMAC1"
slug: p65-inhibition-blocks-hypoxia-specific-demethylation
status: supported
confidence: 0.85
tags:
  - pharmacology
  - NF-kB
  - DNA-methylation
  - macrophage
  - hypoxia
domain: "pharmacology / epigenetics"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: strong
    detail: "BAY11-7082 (p65 inhibitor) restores C2 methylation in mMAC1 to mMAC21 levels (Fig. 4K). PX-478 (HIF1α inhibitor) does not alter C2 methylation. 4-octyl itaconate (TET2 inhibitor) blocks demethylation and gene expression. Pharmacological triangulation supports causal role of p65 → TET-mediated C2 demethylation."
conditions: "BAY11-7082 pretreatment 3 h before LPS in 1% O2; tested in M-CSF MACs only."
date_proposed: 2026-05-05
date_updated: 2026-05-05
---

## Statement

Pretreatment with the NF-κB/IKK inhibitor BAY11-7082 prevents hypoxia-specific demethylation of cluster-C2 CpGs in LPS-activated MACs. p65 inhibition restores C2 methylation in mMAC1 to mMAC21 levels and reduces target gene expression (IL6, TNF, NFKB1, CCL5, IRF1). The HIF1α inhibitor PX-478 does NOT alter C2 methylation, indicating specificity of the NF-κB pathway in the demethylation step.

## Evidence summary

- BAY11-7082 (3 h pretreatment) before LPS activation in 1% O₂ → C2 methylation values restored to mMAC21 (Fig. 4K).
- BAY11-7082 also reduces mRNA expression of IL6, TNF, NFKB1, CCL5, IRF1 (Fig. 4L).
- PX-478 (HIF1α inhibitor) → no change in C2 methylation, partial reduction in some target genes (suggesting HIF1α regulates expression independently of demethylation in some loci).
- 4-octyl itaconate (TET2 inhibitor) → C2 methylation increased + gene expression decreased (positive control for TET dependence).

## Conditions and scope

- Human M-CSF MACs in vitro, 1% O₂, LPS 48 h.
- BAY11-7082 is not strictly p65-specific (inhibits IKK and other NF-κB pathway components); genetic loss-of-function would strengthen the claim.

## Counter-evidence

- BAY11-7082 has known off-target effects on E2/E3 ligases beyond NF-κB; some demethylation rescue could reflect non-NF-κB activities of the compound.

## Linked ideas

(none yet)

## Open questions

- Does p65-specific genetic knockdown phenocopy BAY11-7082?
- Does p65 directly recruit TET2, or does p65 binding open chromatin to allow TET2 access?
- Time course of p65 binding vs C2 demethylation.
