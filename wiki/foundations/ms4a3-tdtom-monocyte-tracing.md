---
title: "Ms4a3-tdTom reporter (monocyte progeny tracing)"
slug: ms4a3-tdtom-monocyte-tracing
domain: "mouse genetics / lineage tracing / immunology"
status: mainstream
aliases:
  - "Ms4a3-tdTom"
  - "Ms4a3-Cre"
  - "Ms4a3 fate mapping"
  - "Ms4a3-Cre R26-tdTom"
  - "Liu 2019 reporter"
  - "granulocyte-monocyte progenitor reporter"
  - "GMP fate map"
  - "monocyte-restricted reporter"
  - "Ms4a3 lineage tracing"
  - "MS4A3-Cre RosatdTomato"
first_introduced: "Liu et al. *Cell* 2019 (Ms4a3-Cre × R26-LSL-tdTomato)"
date_updated: 2026-05-06
source_url: "https://doi.org/10.1016/j.cell.2019.08.009"
---

## Definition

A constitutive Cre/loxP fate-mapping mouse line in which Ms4a3-Cre (knocked into the *Ms4a3* locus) is crossed to a Rosa26-LSL-tdTomato reporter. *Ms4a3* is selectively expressed in granulocyte-monocyte progenitors (GMPs) at a transient developmental stage. Once expressed, Cre permanently labels all downstream progeny — monocytes, monocyte-derived macrophages, and granulocytes — without affecting tissue-resident macrophages of embryonic origin (microglia, alveolar macrophages, Kupffer cells, Langerhans cells), which arise from non-GMP progenitors. The system is constitutive (no tamoxifen needed), giving stable lineage labelling at steady state.

## Intuition

The model isolates a developmental bottleneck: every adult-HSC-derived monocyte and granulocyte must pass through an Ms4a3-expressing GMP intermediate, but no embryonically-seeded TRM does. Therefore Ms4a3-Cre labelling is a clean operational definition of "monocyte/granulocyte lineage" in the adult mouse, providing a complementary readout to inducible Cx3cr1-creER and Map17-creER tools without requiring tamoxifen and without the labelling efficiency issues of inducible systems.

## Key variants

- **Ms4a3-Cre × R26-LSL-tdTomato** (Liu 2019, this concept): tdTomato readout, constitutive
- **Ms4a3-Cre × R26-LSL-YFP**: YFP readout
- **Cx3cr1-creER × R26-YFP**: tamoxifen-inducible alternative; targets a broader CX3CR1⁺ population
- **Map17-creER × R26-LSL-tdTom**: targets adult HSCs more upstream; tamoxifen-inducible
- **Csf1r-Mer-iCre-Mer**: pan-myeloid; less GMP-restricted

## Known limitations

- Constitutive — no temporal control over labelling
- Recombination efficiency in GMPs is high but not 100%; some cells escape labelling
- Granulocytes and monocytes are jointly labelled; cannot distinguish neutrophil vs monocyte lineage
- Some non-GMP-derived myeloid populations may transiently express Ms4a3 in disease states
- Mouse-only system

## Open problems

- More restrictive reporters that distinguish monocyte vs granulocyte lineage post-GMP
- Inducible variants for time-resolved labelling
- Single-cell co-detection of Ms4a3-tdTom labelling with transcriptomic state

## Relevance to active research

[[papers/tissue-resident-macrophages-provide-pro-tumorigenic]] uses Ms4a3-tdTom reporter mice as a complementary lineage-tracing tool to confirm that monocyte-derived MDMs in early KP tumour lesions do not express CD169 (the Siglec1 marker used for TRM-specific depletion), thereby validating the specificity of CD169-DTR + DT for ablating only the TRM lineage. The Ms4a3 reporter also provided in [[papers/cross-tissue-single-cell-landscape-human]] (Mulder 2021 MoMac-VERSE) the foundational fate-mapping evidence to assign cluster identity to embryonic-resident vs monocyte-derived origin in human-mouse cross-mapping.
