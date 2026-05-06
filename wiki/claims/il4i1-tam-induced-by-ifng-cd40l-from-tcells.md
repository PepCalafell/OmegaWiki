---
title: "IL4I1⁺ TAMs are induced in the tumour periphery by IFNγ and CD40L from infiltrating T cells"
slug: il4i1-tam-induced-by-ifng-cd40l-from-tcells
status: supported
confidence: 0.8
tags:
  - IL4I1
  - IFNG
  - CD40L
  - T-cell
  - macrophage
  - tumor-periphery
  - NicheNet
domain: "immunology / oncology"
source_papers:
  - cross-tissue-single-cell-landscape-human
evidence:
  - source: cross-tissue-single-cell-landscape-human
    type: supports
    strength: strong
    detail: "NicheNet on liver-cancer scRNA-seq (Sharma 2020) identifies IFNG (top from CD8⁺) and CD40LG (top from CD4⁺) as the upstream ligands best explaining IL4I1_Mac and ISG_Mo programmes. IFNG-secreting CD69⁺ CD8⁺ T cells and CD40LG-expressing CD4⁺ T cells are concentrated in the tumour periphery (one-way ANOVA p<10⁻⁴), where IL4I1_Mac and ISG_Mo are also enriched. Mechanism diagram (Fig. 6H): CD40 + IFNγR signalling reprograms IFN-primed monocytes into the IL4I1_Mac state."
conditions: "Liver and colon cancer scRNA-seq with periphery-vs-core annotations; predictions inferred by NicheNet, not validated by direct perturbation."
date_proposed: 2026-05-06
date_updated: 2026-05-06
---

## Statement

The IL4I1⁺ tumour-associated macrophage state (MoMac-VERSE cluster #6) is induced in the tumour periphery in a T-cell-dependent manner: IFNγ from activated CD8⁺ T cells and CD40L from CD4⁺ T cells reprogram IFN-primed monocytes (cluster #4 ISG_Mo) into the immunosuppressive IL4I1_Mac phenotype, completing a feedback loop in which infiltrating T cells license macrophages that then suppress them.

## Evidence summary

- NicheNet ligand-target inference on liver cancer (Sharma et al. 2020): IFNG is the top predicted upstream stimulator of both ISG_Mo (#4) and IL4I1_Mac (#6); CD40LG is also among the top predicted stimulators specifically in the tumour periphery.
- IPA top upstream regulators of IL4I1_Mac: IFNA, IFNG, STAT1, NFkB complex.
- CD40LG-expressing CD4⁺ T cells most abundant in tumour periphery (Fig. 6E, 6G).
- IFNG-expressing CD69⁺ CD8⁺ T cells most abundant in tumour periphery (Fig. 6F, p<10⁻⁴).
- Three liver-cancer studies with separate normal/periphery/core annotations: ISG_Mo (#4) and IL4I1_Mac (#6) are detected at greater frequency in the tumour periphery than in tumour core.
- Tumour periphery expresses CD40 and IFNGR1/IFNGR2 in the corresponding macrophage subsets (Fig. 6E, S6B–C).
- Putative ISG_Mo → IL4I1_Mac trajectory supported by shared DEtGs and DERs and by the inferred SCENIC TF network (STAT1, STAT2, ETV7, IRF1, IRF7).

## Conditions and scope

- Validated in liver cancer scRNA-seq (Sharma) and corroborated in colon and lung cancer datasets.
- Periphery-vs-core annotations available only in liver and colon datasets within MoMac-VERSE.
- NicheNet is an inference tool — direct perturbation (anti-IFNγ or anti-CD40L) was not performed.

## Counter-evidence

- ISG_Mo (#4) → IL4I1_Mac (#6) trajectory is hypothesised, not lineage-traced.
- IFNG / CD40L are predicted from gene-expression patterns; alternative inducers (TNF, type-I IFN) are also active and may contribute redundantly.

## Linked ideas

(none yet)

## Open questions

- Direct perturbation: does in vivo anti-IFNγ or anti-CD40 antibody treatment in tumour-bearing mice prevent IL4I1_Mac accumulation?
- What is the timescale of monocyte → ISG_Mo → IL4I1_Mac transition in human tumours?
- Are there IL4I1_Mac states reachable independently of the T-cell-driven pathway (e.g. via tumour cell-intrinsic IFN signalling)?
