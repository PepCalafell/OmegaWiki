---
title: "TREM2⁺ tumor-associated macrophage (TREM2 TAM)"
aliases:
  - "TREM2 TAM"
  - "TREM2 Mac"
  - "TREM2⁺ macrophage"
  - "TREM2-positive TAM"
  - "lipid-associated macrophage"
  - "LAM"
  - "TREM2 TAM cluster #3"
  - "TREM2 lipid-handling TAM"
  - "MoMac-VERSE TREM2 cluster"
  - "TREM2-APOE macrophage"
  - "Trem2 TAM (mouse)"
tags:
  - macrophage
  - tumor-microenvironment
  - TREM2
  - lipid-metabolism
  - immunosuppression
  - single-cell
maturity: active
key_papers:
  - cross-tissue-single-cell-landscape-human
  - nf-kb-tet2-promote-macrophage-reprogramming
  - tissue-resident-macrophages-provide-pro-tumorigenic
  - using-pan-cancer-atlas-investigate-tumour
first_introduced: "Multiple (Katzenelenbogen 2020 *Cell*; Sharma 2020 *Cell*; Molgora 2020 *Cell*); consolidated by Mulder et al. 2021 as MoMac-VERSE cluster #3; identified as monocyte-derived 'group II' MDM signature in NSCLC by Casanova-Acebes 2021"
date_updated: 2026-05-06
related_concepts:
  - momac-verse-mnp-verse-atlas
  - tumor-associated-macrophage-immunosuppression
  - il4i1-tumor-associated-macrophage
  - macrophage-ontogeny-resident-vs-monocyte-derived
---

## Definition

A tumor-associated macrophage state defined by high TREM2 expression together with APOE, GPNMB, SPP1, FABP5, and other lipid-metabolism genes. TREM2_Mac (MoMac-VERSE cluster #3) accumulates across multiple human cancer types and is broadly conserved between species, sharing transcriptional programmes with murine TREM2 TAM (Katzenelenbogen et al. 2020; Molgora et al. 2020) and TREM2-APOE microglia/lipid-associated macrophages (LAM) in obesity and neurodegeneration.

## Intuition

If "the M2 TAM" had a single best representative in the era of scRNA-seq, it would be the TREM2 TAM: lipid-loaded, expanded in cancer, monocyte-derived, immunosuppressive, and a frequent therapeutic target. It is one half of the immunosuppressive macrophage axis in tumours, alongside IL4I1_Mac (cluster #6).

## Formal notation

- MoMac-VERSE cluster #3
- Defining DEtGs: TREM2, APOE, SPP1, GPNMB, FABP5, MARCO, lipid-handling and phagocytic-maturation genes
- Ontogeny (Mulder et al. 2021, validated by Ms4a3 fate-mapping): predominantly monocyte-derived
- Cross-species: shares signatures with mouse TREM2 Macs (Katzenelenbogen 2020 colon; Molgora 2020 breast/sarcoma)
- Pan-cancer accumulation: increased in tumours of liver, lung, colon, breast, stomach, pancreas (all 6 cancer datasets in MoMac-VERSE)

## Variants

- TREM2 TAM in humans (this concept)
- Mouse Trem2 TAM (Katzenelenbogen, Molgora) — cross-species correlate
- LAM (lipid-associated macrophage) — adipose-tissue obesity-driven correlate, shares TREM2/APOE/SPP1 signature
- DAM (disease-associated microglia) — neurodegenerative-disease correlate, shares TREM2-driven program

## Comparison

vs IL4I1_Mac (cluster #6): both are immunosuppressive TAMs, but IL4I1 is IFN-driven, T-cell-induced, accumulates in periphery; TREM2 is lipid-driven, MERTK/efferocytosis-leaning, more uniformly distributed within tumours.
vs HES1_Mac (cluster #2): HES1 has embryonic-origin signature; TREM2 is monocyte-derived.
vs FOLR2_Mac: tissue-resident vs monocyte-derived; FOLR2 maps closer to HES1/long-term-resident, TREM2 to recruited.

## When to use

When characterising lipid-handling or efferocytic TAM populations in any cancer with available scRNA-seq; when scoring bulk RNA-seq with TREM2-Mac signature for prognostic association.

## Known limitations

- TREM2 alone is not specific (also expressed by tissue-resident microglia, alveolar Macs, osteoclasts)
- Functional immunosuppression is consistent but not uniform across tumour types
- Anti-TREM2 antibody therapy in cancer is still in early clinical evaluation; outcome differences across tumour types remain to be seen

## Open problems

- Whether targeting TREM2 unmasks compensatory immunosuppressive programmes (e.g. IL4I1)
- Spatial relationship of TREM2 TAM with tumour necrotic core vs invasive front
- Tumour-type-specific functional roles vs pan-cancer commonalities

## Key papers

- [[papers/cross-tissue-single-cell-landscape-human]] — defined MoMac-VERSE cluster #3, demonstrated pan-cancer accumulation, fate-mapped to monocyte origin
- [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] — used TREM2 TAM signature as the contrastive immunosuppressive baseline against the hypoxic mMAC1 / IL4I1 axis
- [[papers/tissue-resident-macrophages-provide-pro-tumorigenic]] — identifies TREM2/SPP1/APOE/GPNMB as the canonical monocyte-derived "group II" MDM signature in mouse and human NSCLC, ontogenically distinct from PPARG⁺/MARCO⁺ alveolar TRMs (group I); cross-species conservation reinforces the TREM2 TAM pan-cancer module

## My understanding

TREM2 TAM is the canonical "bad-side" macrophage of recent cancer single-cell biology and the natural counterpart to the IL4I1+ TAM in mechanistic studies. For HypoxiaVERSE it serves as the contrastive control: hypoxic mMAC1 maps away from TREM2_Mac and toward IL4I1_Mac, consistent with mMAC1 being a less-immunosuppressive, T-cell-recruiting state.
