---
title: "Cx3cr1-creER fate mapping (monocyte progeny)"
slug: cx3cr1-creer-fate-mapping
domain: "mouse genetics / lineage tracing / immunology"
status: mainstream
aliases:
  - "Cx3cr1-creER"
  - "Cx3cr1creER"
  - "Cx3cr1-creER R26-YFP"
  - "Yona 2013 fate-map"
  - "monocyte fate mapping"
  - "CX3CR1 lineage tracing"
  - "tamoxifen-inducible Cx3cr1 reporter"
  - "Cx3cr1-creER R26-tdTom"
  - "monocyte-derived macrophage fate map"
first_introduced: "Yona et al. *Immunity* 2013 (Cx3cr1-creER × R26-LSL-YFP)"
date_updated: 2026-05-06
source_url: "https://doi.org/10.1016/j.immuni.2012.12.001"
---

## Definition

A tamoxifen-inducible Cre/loxP fate-mapping mouse line using a Cx3cr1-creER knock-in (or Cx3cr1-creERT2) allele crossed to a Rosa26-LSL-YFP (or tdTomato) reporter. CX3CR1 is expressed on circulating monocytes, certain dendritic cell subsets, and microglia. After tamoxifen pulse, all CX3CR1-expressing cells at the time of labelling — and their downstream progeny, except for short-lived monocytes that are subsequently replaced — are permanently marked. Continuous tamoxifen administration (chow diet) maintains labelling of newly-generated CX3CR1⁺ progenitors, allowing long-term tracing of monocyte progeny through tissues.

## Intuition

The model exploits the fact that circulating monocytes are short-lived and continuously replenished from the bone marrow, while certain CX3CR1⁺ tissue populations (microglia, intestinal macrophages) are long-lived. With a brief tamoxifen pulse, label fades from short-lived populations but persists in long-lived ones — a built-in pulse-chase. With continuous tamoxifen, label accumulates in newly-recruited monocyte-derived populations, distinguishing them from already-resident, non-CX3CR1-historical lineages.

## Key variants

- **Cx3cr1-creER × R26-LSL-YFP** (Casanova-Acebes 2021 use): YFP readout
- **Cx3cr1-creERT2 × R26-LSL-tdTomato**: tdTomato readout, alternative
- **Cx3cr1-GFP knock-in** (Jung 2000): constitutive GFP — phenotypic, not fate-mapping
- **Pdzk1ip1 (Map17)-creER × R26-tdTom** (Sawai 2016): targets adult HSCs more broadly, complementary tool
- **Ms4a3-tdTom** (Liu 2019): targets granulocyte-monocyte progenitor stage; non-inducible

## Known limitations

- CX3CR1 is also expressed on a subset of dendritic cells, NK cells, and microglia — labelling is not strictly monocyte-specific
- Tamoxifen kinetics affect labelling efficiency and washout; pulse vs continuous regimens give different readouts
- Microglia (long-lived CX3CR1⁺ TRMs) retain pulse-chase label, which can create signal-bleed into the "monocyte progeny" interpretation
- Recombination efficiency varies across tissues
- Mouse-only system; no human equivalent

## Open problems

- More monocyte-restricted reporters (Ms4a3 partially fills this gap)
- Combined tracking of pulse-chase-faded vs newly-labelled cells in same animal
- Validation across tumour and inflammation contexts

## Relevance to active research

[[papers/tissue-resident-macrophages-provide-pro-tumorigenic]] uses Cx3cr1-creER × R26-LSL-YFP mice on continuous tamoxifen diet (chow TD.130858) to label adult bone-marrow-derived myeloid progenitors. After KP tumour injection, scRNA-seq of YFP⁺ vs YFP⁻ tumour-associated macrophages confirms that group I (alveolar TRM) is depleted of YFP⁺ cells (resident lineage, label-negative) while group II (MDMs) and groups III/IV (monocytes) are heavily YFP⁺ (recruited lineage). The result complements the parallel Pdzk1ip1-creER fate map and strengthens the conclusion that group I is TRM-derived and group II is MDM-derived in NSCLC.
