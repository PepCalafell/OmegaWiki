---
title: "M1 / M2 macrophage polarisation paradigm"
aliases:
  - "M1/M2 polarisation"
  - "M1 M2 macrophage"
  - "classical activation M1"
  - "alternative activation M2"
  - "pro-inflammatory M1"
  - "anti-inflammatory M2"
  - "M1 vs M2"
  - "macrophage polarisation"
  - "M1 macrophage"
  - "M2 macrophage"
  - "Th1/Th2 macrophage paradigm"
  - "Mills 2000 M1/M2"
tags:
  - macrophage
  - immunology
  - polarisation
  - M1
  - M2
maturity: active
key_papers:
  - cross-tissue-single-cell-landscape-human
  - hypoxia-driven-crosstalk-between-tumor-tumor
  - pd-l1-expressing-tumor-associated-macrophages
  - tumor-induced-metabolic-immunosuppression-mechanisms-therapeutic
  - dictionary-immune-responses-cytokines-single-cell
  - using-pan-cancer-atlas-investigate-tumour
  - development-hypoxia-responsive-macrophage-prognostic-model
  - metabolism-tissue-macrophages-homeostasis-pathology
  - lipid-metabolism-homeostasis-disease
  - macrophages-targets-next-generation-cancer-immunotherapy
first_introduced: "Mills, Kincaid et al. 2000 *J Immunol* (M1/M2 framing); refined by Cui & Hacohen 2024 *Nature* Mac-a/b/c/d/e at scRNA-seq resolution"
date_updated: 2026-05-27
related_concepts:
  - momac-verse-mnp-verse-atlas
  - tumor-associated-macrophage-immunosuppression
  - mmac1-hypoxic-inflammatory-macrophage
---

## Definition

A binary classification of macrophage activation states inspired by the Th1/Th2 T-helper-cell dichotomy. M1 ("classically activated") macrophages are induced by IFNγ + LPS, secrete pro-inflammatory cytokines (IL-12, TNFα, IL-6), produce nitric oxide, and present antigen. M2 ("alternatively activated") macrophages are induced by IL-4 / IL-13, express CD206 / CD163 / FOLR2, secrete anti-inflammatory IL-10 / TGFβ, and support tissue repair and angiogenesis.

## Intuition

The M1/M2 axis was the standard mental model of macrophage biology from ~2000 to ~2015, until mass cytometry and single-cell RNA-seq revealed that real-tissue macrophages occupy a continuum of states with combinatorial mixtures of M1- and M2-associated genes. The axis is still useful pedagogically and for in vitro M-CSF-derived MAC experiments, but is widely acknowledged to under-describe in vivo TAM diversity.

## Formal notation

- M1 inducers: IFNγ, LPS, GM-CSF
- M1 markers: TNFα, IL-12, IL-6, CD86 high, HLA-DR high, iNOS (NOS2)
- M2 inducers: IL-4, IL-13, IL-10, glucocorticoids, M-CSF
- M2 markers: CD206 (MRC1), CD163, FOLR2, ARG1 (mouse), CCL18 (human), TGM2
- M2 sub-states (Murray 2014 nomenclature): M2a (IL-4/IL-13), M2b (immune complex + LPS), M2c (IL-10 / glucocorticoid), M2d (TLR + adenosine, "tumour-like")

## Variants

- M2a / M2b / M2c / M2d sub-classification
- M(LPS), M(IFNγ), M(IL-4), etc. — more careful "M(x)" stimulus-tagged nomenclature (Murray et al. 2014)
- "TAM as M2-like" framing (now widely seen as oversimplification)
- M1/M2 signature scores from gene sets (Martinez et al. 2006) — used to compute per-cell M1/M2 lean

## Comparison

vs single-cell-cluster-based taxonomy (MoMac-VERSE): the binary M1/M2 axis collapses to a few directions in single-cell space; clusters #2 (HES1_Mac), #6 (IL4I1_Mac), #15 (IL1B_Mo), #16 (C1Qhi_Mac) are enriched in M1 genes, while clusters #3 (TREM2_Mac), #17 (FTL_Mac) are enriched in M2 genes — but most clusters express *both* and the dichotomy is lossy.
vs ontogeny-based axis: M1/M2 is orthogonal; an embryonic-origin TRM can be M1- or M2-like depending on stimulus.

## When to use

- Pedagogical introduction to macrophage biology
- In vitro M-CSF/GM-CSF/IL-4-derived MAC experiments where the binary axis is genuinely informative
- As a *contrastive baseline* against richer single-cell taxonomies in cancer / chronic inflammation

## Known limitations

- Real tissue MACs co-express M1 and M2 signature genes, breaking the binary
- TAMs do not fit the simple "M2 = pro-tumour" rule — IL4I1_Mac scores as M1 yet is strongly immunosuppressive
- IL-12B is restricted to mregDC and cDC1 in human MoMac-VERSE; the canonical M1-cytokine is essentially absent from human tumour macrophages, undermining a key M1 marker

## Open problems

- A formal replacement nomenclature that combines stimulus, ontogeny, and tissue niche
- Quantitative scoring frameworks that encode multidimensional polarisation rather than collapsing to one axis

## Key papers

- [[papers/cross-tissue-single-cell-landscape-human]] — explicitly demonstrates that the M1/M2 dichotomy fails to embrace the diversity of human MAC populations across tissues; clusters #6 (IL4I1) and #2 (HES1) score as M1 yet are neither pro-inflammatory effectors nor IL-12 producers, and IL-12B is restricted to DC populations rather than M1 macrophages
- [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] — uses M-CSF mMAC21 vs mMAC1 axis where the M1/M2 framing is partially informative for the in vitro system but is shown to fail at predicting in vivo TAM diversity
- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — Bai 2022 *Molecular Cancer* review uses the M1/M2 axis as the dominant TAM polarization framework throughout, with tumor-derived exosomes / cytokines / oncometabolites driving M2 polarization and rare counter-mechanisms (Spint1, colon-cancer SIRPα-CD47 paradox) preserving M1-like TAMs

## My understanding

The M1/M2 paradigm is a useful ladder to climb up to single-cell taxonomies, but should never be taken as ground truth for tissue MAC biology. For thesis writing it is best invoked as the foil against which the MoMac-VERSE / hypoxic-inflammatory taxonomy demonstrates its value.
