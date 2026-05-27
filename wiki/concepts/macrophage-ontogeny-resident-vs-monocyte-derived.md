---
title: "Tissue-resident vs monocyte-derived macrophage ontogeny"
aliases:
  - "macrophage ontogeny"
  - "tissue-resident macrophage"
  - "TRM"
  - "long-term resident macrophage"
  - "monocyte-derived macrophage"
  - "MoMac"
  - "embryonic-origin macrophage"
  - "yolk-sac-derived macrophage"
  - "fetal-liver-derived macrophage"
  - "Ms4a3 fate mapping"
  - "macrophage origin scRNA-seq"
  - "self-renewing tissue macrophage"
  - "EMP-derived macrophage"
  - "erythro-myeloid progenitor origin"
  - "PreMac"
  - "BMDM vs TRM"
  - "ancillary macrophage"
  - "self-renewal local proliferation"
  - "parabiosis TRM independence"
tags:
  - macrophage
  - ontogeny
  - lineage-tracing
  - immunology
  - development
maturity: active
key_papers:
  - cross-tissue-single-cell-landscape-human
  - tissue-resident-macrophages-provide-pro-tumorigenic
  - physiology-diseases-tissue-resident-macrophages
  - using-pan-cancer-atlas-investigate-tumour
  - metabolism-tissue-macrophages-homeostasis-pathology
  - macrophages-targets-next-generation-cancer-immunotherapy
first_introduced: "Ginhoux 2010, Hashimoto 2013, Mass 2016, Liu (Ms4a3) 2019; applied to NSCLC TRM vs MDM in Casanova-Acebes 2021; canonical 2023 review by Lazarov & Geissmann"
date_updated: 2026-05-27
related_concepts:
  - mononuclear-phagocyte-system
  - momac-verse-mnp-verse-atlas
  - trem2-tumor-associated-macrophage
  - il4i1-tumor-associated-macrophage
---

## Definition

The two-compartment model of macrophage origin in adult tissues. Tissue-resident macrophages (TRMs / "long-term resident") are seeded during embryonic development from yolk-sac and fetal-liver progenitors and self-renew locally. Monocyte-derived macrophages (MoMacs) arise from circulating bone-marrow-derived classical monocytes recruited from blood, and become the dominant macrophage population during inflammation, infection, and tumour growth.

## Intuition

The classical view that all tissue macrophages are "renewed from blood monocytes" was overturned by murine fate-mapping in the early 2010s. In most adult tissues at homeostasis, TRMs are predominantly embryonic in origin and self-renew locally with little contribution from monocytes. During pathology (inflammation, cancer), monocyte-derived macrophages flood the tissue and accumulate. The ratio of TRM-like to MoMac-like cells encodes pathological state.

## Formal notation

- Embryonic ancestors: yolk-sac primitive macrophages → fetal-liver erythro-myeloid progenitors → tissue seeding before birth
- Adult ancestors: bone marrow → circulating Ly6C⁺ monocytes (mouse) / CD14⁺ classical monocytes (human) → tissue recruitment
- Lineage-tracing tools (mouse): Ms4a3-Cre (monocyte-restricted, Liu 2019), CX3CR1-CreER, Cdh5-CreER, Csf1r-CreER
- Tissue-by-tissue ratios at homeostasis: brain microglia ≈ 100% embryonic; liver Kupffer ≈ 80% embryonic; lung alveolar Mac ≈ 100% fetal liver; gut LP Mac ≈ 100% monocyte-derived after weaning
- Cancer / inflammation: MoMac fraction rises sharply, displacing TRMs

## Variants

- LYVE1⁺ tissue-resident MAC (Chakarov et al. 2019)
- Classical Kupffer cell (embryonic)
- Microglia (yolk-sac primitive)
- Alveolar macrophage (fetal liver)
- Langerhans cell (fetal liver, classical example of self-renewing TRM)
- Monocyte-derived TAM (e.g. TREM2_Mac, IL4I1_Mac in MoMac-VERSE)

## Comparison

vs M1/M2 polarisation: M1/M2 is a state descriptor, ontogeny is a lineage descriptor; the two are orthogonal.
vs MoMac-VERSE clusters: HES1_Mac (#2) and FTL_Mac (#17) lean embryonic-resident; TREM2_Mac (#3), IL4I1_Mac (#6), proliferating_Mac (#10), C1Qhi_Mac (#16) lean monocyte-derived.

## When to use

- Interpreting why some macrophage subsets self-renew under perturbation while others depend on monocyte recruitment
- Designing CSF1R / CCR2 inhibition strategies (target MoMac without depleting TRMs)
- Mapping mouse fate-mapping data onto human scRNA-seq populations

## Known limitations

- Most direct evidence is from mouse; human ontogeny is inferred via signature similarity, not lineage tracing
- Some tissues (skin, colon) replace TRMs partially with MoMacs over time, blurring the dichotomy
- Plasticity: MoMacs can adopt TRM-like programmes given long enough residency

## Open problems

- Whether monocyte-derived TAMs in tumours acquire long-term-resident properties or remain transient
- Cross-species mapping of murine fate-mapping data to specific MoMac-VERSE clusters at scale
- Functional consequences of mixed-origin macrophage populations in human disease

## Key papers

- [[papers/cross-tissue-single-cell-landscape-human]] — uses Ms4a3-Cre mouse liver scRNA-seq and the LYVE1⁻ conserved monocyte signature to assign embryonic vs monocyte-derived origin to MoMac-VERSE clusters: HES1_Mac and FTL_Mac map to embryonic; TREM2_Mac, IL4I1_Mac, proliferating_Mac, C1Qhi_Mac map to monocyte-derived
- [[papers/tissue-resident-macrophages-provide-pro-tumorigenic]] — applies Map17(Pdzk1ip1)-creER and Cx3cr1-creER fate mapping in mouse NSCLC to assign group I (PPARG⁺/MARCO⁺/SIGLEC1⁺) to TRM lineage and group II (TREM2⁺/SPP1⁺/APOE⁺/GPNMB⁺) to MDM lineage; cross-species signatures conserved between human and mouse
- [[papers/physiology-diseases-tissue-resident-macrophages]] — Lazarov & Geissmann 2023 *Nature* canonical review; consolidates the EMP yolk-sac origin, three haematopoietic waves (primitive / EMP / HSC), local self-renewal, niche-mediated specification (LDFs SALL1/PPARG/SPI-C/GATA6/ID3), and the ancillary-cell framing of TRMs as paired-helper cells for parenchymal cell types

## My understanding

For HypoxiaVERSE, this ontogeny axis matters because hypoxic mMAC1 is generated in vitro from monocytes — its in vivo correlates should therefore lie in the monocyte-derived sectors of MoMac-VERSE (IL4I1_Mac, ISG_Mo, IL1B_Mo), which is consistent with what the Calafell 2024 paper finds. Embryonic-origin TRMs (HES1_Mac, FTL_Mac) form a separate axis that is largely orthogonal to hypoxia-driven inflammatory states.
