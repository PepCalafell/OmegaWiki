---
title: "Pdzk1ip1 (Map17)-creER fate mapping (adult HSC progeny)"
slug: pdzk1ip1-map17-creer-fate-mapping
domain: "mouse genetics / lineage tracing / immunology"
status: mainstream
aliases:
  - "Map17-creER"
  - "Pdzk1ip1-creER"
  - "Map17 fate mapping"
  - "Pdzk1ip1-creER R26-LSL-tdTom"
  - "Map17creER R26tdTom"
  - "adult HSC fate map"
  - "low-cycling HSC reporter"
  - "Sawai 2016 fate-map"
  - "MAP17 lineage tracing"
  - "tamoxifen-inducible adult HSC tracker"
first_introduced: "Sawai et al. *Immunity* 2016 (Map17/Pdzk1ip1-creER × R26-LSL-tdTomato)"
date_updated: 2026-05-06
source_url: "https://doi.org/10.1016/j.immuni.2016.08.007"
---

## Definition

A tamoxifen-inducible Cre/loxP fate-mapping system using a knock-in or transgenic Pdzk1ip1 (Map17)-creER allele crossed to a Rosa26-LSL-tdTomato (or LSL-YFP) reporter. MAP17/Pdzk1ip1 is selectively expressed by low-cycling adult hematopoietic stem cells (HSCs) but is absent from embryonic HSCs. A single dose of tamoxifen permanently labels adult HSCs and all of their downstream progeny (bone-marrow-derived monocytes, neutrophils, B/T cells), while leaving embryonically-seeded tissue-resident macrophages (TRMs) unlabelled.

## Intuition

The model exploits the developmental window in which adult HSCs are distinguishable from their embryonic precursors. Tamoxifen-induced labelling is heritable: every cell ever derived from a labelled adult HSC carries the reporter. After 4–6 months of tamoxifen pulse, the entire adult-HSC-derived hematopoietic compartment is labelled, while embryonically-seeded TRMs (microglia, alveolar macrophages, Kupffer cells, Langerhans cells) remain unlabelled. The labelling pattern thus operationally distinguishes embryonic-origin TRMs from adult-HSC-origin MDMs without requiring transplantation.

## Key variants

- **Map17-creER × R26-LSL-tdTomato** (Casanova-Acebes 2021 use): tdTomato readout, FACS- and microscopy-compatible
- **Map17-creER × R26-LSL-YFP**: YFP variant
- **Cx3cr1-creER × R26-YFP** (Yona 2013, complementary tool): targets monocyte-restricted progeny rather than all adult HSCs
- **Ms4a3-tdTom** (Liu 2019): non-Cre reporter active in granulocyte-monocyte progenitors, constitutive
- **Csf1r-Mer-iCre-Mer**: targets pan-myeloid lineage (less HSC-restricted)
- **Tie2-Cre / Cdh5-CreER**: endothelial / hematopoietic precursor labelling

## Known limitations

- Tamoxifen induction efficiency is incomplete; some adult HSCs and their progeny escape labelling, complicating absolute quantification
- Expression of MAP17/Pdzk1ip1 may not be perfectly restricted to adult HSCs in all conditions
- Long pulse-chase intervals (4–6 months) make experiments long
- Embryonic HSCs that re-enter cycling may also become labelled if they happen to be in MAP17⁺ state
- TRMs that self-renew slowly may eventually accumulate label from rare circulating progenitor recruitment events
- Mouse-only system; no direct human equivalent

## Open problems

- More restrictive promoters that label only adult HSCs (and not common myeloid progenitors)
- Combined dual-reporter systems for simultaneous labelling of embryonic vs adult lineages
- Validation in tumour and inflammation contexts where TRM dynamics may differ

## Relevance to active research

[[papers/tissue-resident-macrophages-provide-pro-tumorigenic]] uses Map17creER/+R26tdTom mice to confirm that the group I (alveolar) macrophage cluster identified by scRNA-seq in NSCLC is depleted of tdTomato⁺ cells (i.e., is independent of adult HSCs and is TRM-derived), while group II (TREM2⁺/SPP1⁺) and groups III–IV (monocytes) are heavily labelled (adult-HSC-derived). This is the central lineage-tracing evidence underpinning the TRM vs MDM ontogeny dichotomy in NSCLC. The result is reinforced by a parallel Cx3cr1-creER × R26-YFP fate map.
