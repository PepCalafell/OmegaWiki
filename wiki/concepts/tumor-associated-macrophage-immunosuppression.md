---
title: "Tumor-associated macrophage immunosuppression"
aliases:
  - "TAM immunosuppression"
  - "tumor MAC reprogramming"
  - "immunosuppressive TAM"
  - "M2-like TAM polarization"
  - "TME-induced macrophage suppression"
  - "anti-inflammatory TAM phenotype"
  - "tumor-associated macrophages"
  - "TAM"
tags:
  - tumor-microenvironment
  - macrophage
  - immunosuppression
  - cancer-immunology
maturity: stable
key_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
  - cross-tissue-single-cell-landscape-human
first_introduced: "(field-standard concept; refined here)"
date_updated: 2026-05-06
related_concepts:
  - mmac1-hypoxic-inflammatory-macrophage
  - momac-verse-mnp-verse-atlas
  - trem2-tumor-associated-macrophage
  - il4i1-tumor-associated-macrophage
---

## Definition

The dominant TME framing of macrophages: monocyte-derived MACs entering the tumor are reprogrammed by TME cues (hypoxia, lactate, IL-10, TGF-β, apoptotic bodies, growth factors) into immunosuppressive cells that dampen T-cell responses, support angiogenesis, and correlate with poor patient prognosis.

## Intuition

TAMs are the "wrong-side" macrophage of cancer immunology — they suppress immune responses and predict bad outcomes. Markers commonly associated with this state include CD163, CD206, FOLR2, TREM2, and high IL-10 production. Hypoxia is one of the canonical TME signals invoked to explain this immunosuppression.

## Formal notation

- Markers: CD14^hi, CD163^hi, CD206^hi, FOLR2 (tissue-resident), TREM2 (lipid-associated, immunosuppressive)
- Function: suppress CD8⁺ T-cell proliferation, secrete IL-10 / TGF-β
- Clinical: high TAM infiltration → poor OS in many cancer types
- TCGA in this paper: TREM2 signature → poor prognosis in 7/12 cancers; FOLR2 in 6/12; mMAC21 in 10/12

## Variants

- TREM2⁺ TAM: lipid-handling, strongly immunosuppressive
- FOLR2⁺ TAM: tissue-resident, context-dependent
- mMAC21 (in vitro normoxic activated MAC): correlates with mMAC21 transcriptomic signature in IL1B Mo cluster

## Comparison

This paper challenges the universal-immunosuppression framing by demonstrating a *hypoxic* MAC subset (mMAC1 / IL4I1) that is *anti*-suppressive and correlates with *better* prognosis. Hypoxia is not monolithically pro-suppressive in MAC biology.

## When to use

When framing TME-driven MAC reprogramming, especially as the null hypothesis against which to compare hypoxic-inflammatory exceptions.

## Known limitations

- Heterogeneity of TAMs is large; markers like CD163/CD206 are not specific.
- Bulk-deconvolution-based TAM scoring conflates several MAC subsets.
- The "M1/M2" dichotomy under-describes in vivo TAM diversity.

## Open problems

- Single-cell-resolved markers and signatures across cancers (atlas-scale).
- Causal vs correlational role of TAM presence in outcomes.
- Therapeutic targeting strategies (TREM2 antibodies, CSF1R inhibitors, reprogramming agonists).

## Key papers

- [[papers/cross-tissue-single-cell-landscape-human]] — pan-tissue scRNA-seq decomposition of TAM heterogeneity into MoMac-VERSE clusters; defines TREM2_Mac and IL4I1_Mac as the two principal pan-cancer immunosuppressive TAM populations and shows that the binary M1/M2 framing under-describes this diversity.
- [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] — provides a hypoxic exception to the universal-immunosuppression framing

## My understanding

TAM immunosuppression is the field-standard framing this paper *partially refutes*. Important for HypoxiaVERSE as the contrastive baseline against which mMAC1 / IL4I1 macrophages stand out.
