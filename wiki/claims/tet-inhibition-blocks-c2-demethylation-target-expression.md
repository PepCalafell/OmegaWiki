---
title: "TET2 inhibition (4-octyl itaconate) increases C2 methylation and decreases C2-target gene expression, confirming TET2-dependent active demethylation"
slug: tet-inhibition-blocks-c2-demethylation-target-expression
status: supported
confidence: 0.85
tags:
  - 4-octyl-itaconate
  - TET2-inhibitor
  - DNA-demethylation
  - cluster-C2
  - itaconate
  - pharmacological
domain: "pharmacology / epigenetics"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: strong
    detail: "4-octyl itaconate pretreatment as positive control for TET2 inhibition (Calafell 2024 Fig. 4K-L). Result: C2 methylation rises markedly above mMAC21 levels; mRNA expression of C2 target genes (NFKB1, CCL5, IRF1, IL6) drops. Confirms TET2-mediated active demethylation is required for C2-target gene expression in mMAC1."
conditions: "4-octyl itaconate pretreatment 3h before LPS; M-CSF MACs."
date_proposed: 2026-05-11
date_updated: 2026-05-11
---

## Statement

4-octyl itaconate, a cell-permeable TET2 inhibitor, blocks C2 cluster DNA demethylation in mMAC1 and reduces mRNA expression of C2-associated target genes (NFKB1, CCL5, IRF1, IL6). This confirms that TET2-mediated active demethylation is required for the proinflammatory gene expression program of mMAC1.

## Evidence summary

- EPIC methylation array showing increased C2 methylation under 4-octyl itaconate (Calafell 2024 Fig. 4K).
- qRT-PCR of target genes showing decreased expression (Fig. 4L).

## Conditions and scope

- Single inhibitor used as positive control; 4-octyl itaconate inhibits TET2 via covalent modification of catalytic cysteine (Chen et al., Nat Metab 2022).
- TET1/3 contributions not separately tested.

## Counter-evidence

- 4-octyl itaconate has other targets (KEAP1/Nrf2 axis, GAPDH); off-target effects on gene expression possible.
- TET2 genetic KO would provide orthogonal validation.

## Linked ideas

- Direct TET2 ChIP-seq at C2 would close the loop.
- Suggests itaconate / Nrf2 axis intervention as a TAM-modulating strategy.

## Open questions

- TET isoform specificity at C2 (TET1 vs TET2 vs TET3).
- Whether p65 directly recruits TET2 or whether the relationship is indirect.
