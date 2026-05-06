---
title: "IL4I1⁺ TAMs degrade tryptophan via the AHR pathway and exert immunosuppression"
slug: il4i1-tam-degrade-tryptophan-via-ahr-immunosuppression
status: supported
confidence: 0.85
tags:
  - IL4I1
  - AHR
  - tryptophan
  - immunosuppression
  - tumor-microenvironment
  - macrophage
domain: "immunology / oncology"
source_papers:
  - cross-tissue-single-cell-landscape-human
evidence:
  - source: cross-tissue-single-cell-landscape-human
    type: supports
    strength: strong
    detail: "MoMac-VERSE cluster #6 (IL4I1_Mac) co-expresses IL4I1, IDO1, PD-L1, PD-L2 at protein level (CITE-seq + flow cytometry on lung adenocarcinoma and HCC). Authors cite Sadik et al. 2020 *Cell* for IL4I1 acting as a more potent AHR activator than IDO1 via tryptophan/phenylalanine catabolism. NicheNet predicts IFNG (top upstream regulator) drives IDO1 + IL4I1 expression; the result is a tryptophan-degrading immunosuppressive niche in the tumour periphery."
conditions: "Human tumours across 6 cancer types in MoMac-VERSE (liver, lung, colon, breast, stomach, pancreas); validated by flow cytometry on LUAD and HCC patient samples."
date_proposed: 2026-05-06
date_updated: 2026-05-06
---

## Statement

IL4I1⁺PD-L1⁺IDO1⁺ tumour-associated macrophages (MoMac-VERSE cluster #6) catabolise tryptophan to AHR-activating metabolites and, together with surface PD-L1/PD-L2 display, suppress effector T-cell function in the tumour periphery.

## Evidence summary

- IL4I1_Mac (#6) scRNA-seq DEtGs include IL4I1, IDO1, CD274 (PD-L1), PDCD1LG2 (PD-L2), CD40, CD80, CD86, CCR7, CXCL9, CXCL10, CXCL11.
- Protein validation: CITE-seq breast cancer (Wu et al.) shows IL4I1_Mac significantly higher PD-L1, PD-L2, MHC-II, CD80, CD86 vs other Mo/Mac (p<0.0001 each).
- Flow cytometry on healthy human lung detects PD-L1^hi PD-L2^hi HLA-DP^hi HLA-DQ^hi CD40^hi CD86^hi cells corresponding to IL4I1_Mac.
- IDO1 and IL4I1 expression is higher in tumour vs matched normal-adjacent tissue.
- Authors cite Sadik et al. 2020 *Cell* showing IL4I1 is a more potent AHR activator than IDO1 via L-amino-acid oxidase activity producing indole-3-pyruvate.
- IPA top upstream regulators of IL4I1_Mac: IFNG, IFNA, STAT1, NFkB complex — consistent with IFNγ-driven induction by adjacent T cells.
- IL4I1_Mac concentrated in tumour periphery (vs core), where IFNG-secreting CD69⁺ CD8⁺ T cells and CD40LG-expressing CD4⁺ T cells co-localise.

## Conditions and scope

- Direct functional T-cell suppression assays not performed in the paper for IL4I1_Mac specifically; immunosuppressive function inferred from gene programme + protein markers + spatial localisation + Sadik 2020 prior work.
- Validated in 6 cancer types (liver, lung, colon, breast, stomach, pancreas).

## Counter-evidence

- IL4I1_Mac also expresses M1 / pro-inflammatory markers (CXCL9/10/11, CD40, MHC-II), so the cluster is not "purely immunosuppressive" — it may be a recently activated state that is in the process of being licensed into immunosuppression.
- Pharmacological targeting of IL4I1 alone has not been shown to reverse the tumour-suppressive phenotype.

## Linked ideas

(none yet)

## Open questions

- Whether IL4I1 inhibitor + IDO1 inhibitor combination outperforms either alone clinically.
- Whether the AHR-driven Treg recruitment via CXCR3 ligands (CXCL9/10/11) is the dominant immunosuppressive output of IL4I1_Mac, or whether tryptophan depletion of effector T cells is the primary mechanism.
- Single-cell perturbation of AHR in IL4I1_Mac to dissect contribution.
