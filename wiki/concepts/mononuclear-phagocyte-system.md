---
title: "Mononuclear phagocyte system (MPS)"
aliases:
  - "MPS"
  - "mononuclear phagocyte system"
  - "MNP"
  - "MNP system"
  - "mononuclear phagocytes"
  - "monocyte-macrophage-DC system"
  - "mononuclear phagocyte family"
  - "Mo/Mac/DC compartment"
  - "myeloid mononuclear phagocyte compartment"
  - "phagocyte lineage"
  - "MPS hierarchy"
  - "MNP populations"
tags:
  - macrophage
  - monocyte
  - dendritic-cell
  - immunology
  - phagocyte
  - cell-lineage
maturity: stable
key_papers:
  - cross-tissue-single-cell-landscape-human
  - physiology-diseases-tissue-resident-macrophages
first_introduced: "van Furth et al. 1972 *Bull World Health Organ*"
date_updated: 2026-05-06
related_concepts:
  - momac-verse-mnp-verse-atlas
  - macrophage-ontogeny-resident-vs-monocyte-derived
  - tumor-associated-macrophage-immunosuppression
---

## Definition

The mononuclear phagocyte system (MPS) is the family of bone-marrow-derived and embryonically-seeded immune cells comprising monocytes (classical CD14⁺CD16⁻, non-classical CD14lo⁺CD16⁺, intermediate), macrophages (tissue-resident and monocyte-derived), and dendritic cells (cDC1, cDC2, cDC2/DC3, pre-DC, mregDC, and historically pDC). Defined by Van Furth et al. in 1972 to replace the older "reticuloendothelial system", the MPS unifies these cell types based on shared phagocytic capacity, monocytic developmental potential, and antigen-handling roles.

## Intuition

MNPs are the front-line phagocytic and antigen-presenting cells of the tissue immune compartment. Although they share core functions (phagocytosis, antigen presentation, cytokine secretion), they differ widely in ontogeny (embryonic vs monocyte-derived), tissue distribution, polarisation states, and specific functional repertoire. Single-cell atlases have made it possible to map this heterogeneity at population level for the first time.

## Formal notation

- Major MNP subsets in human (per Mulder 2021):
  - Classical monocytes (cMo, CD14⁺CD16⁻)
  - Non-classical / intermediate monocytes (CD16⁺ Mo)
  - Tissue macrophages (heterogeneous; TREM2_Mac, FOLR2/HES1_Mac, IL4I1_Mac, IL1B_Mo, ISG_Mo, FTL_Mac, C1Qhi_Mac, alveolar Mac, etc.)
  - cDC1 (CADM1⁺CLEC9A⁺XCR1⁺)
  - cDC2 / DC3 (FCER1A⁺CD1C⁺CD1E⁺)
  - mregDC (mature regulatory DC)
  - pre-DC
  - (pDC excluded by Mulder 2021 because of separate lymphoid origin)
- Excludes: granulocytes (PMN), mast cells, lymphocytes, NK cells

## Variants

- Classical M1/M2 polarisation (Mills 2000) — superseded paradigm at single-cell resolution
- Tissue-resident vs monocyte-derived macrophage axis (see [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]])
- DC-centric vs Mac-centric framings of the same compartment

## Comparison

vs lymphoid system: MPS is innate, phagocytic, and antigen-presenting (bridge to adaptive immunity); the lymphoid system is adaptive, antigen-receptor-clonal.
vs granulocyte / PMN system: MPS is mononuclear, longer-lived, with broader functional plasticity; PMNs are short-lived, polynuclear, primarily acute-phase.

## When to use

When discussing the broad immune compartment that includes monocytes, macrophages, and DCs as a unified family — for instance when introducing scRNA-seq atlases of myeloid biology, or framing therapeutic targets across MAC/Mo/DC populations.

## Known limitations

- The MPS framing slightly under-represents DC-specific lymphoid origins (pDC; some DC2/DC3 plasticity)
- Distinct ontogeny of tissue-resident MACs (yolk sac, fetal liver) versus monocyte-derived MACs is not captured in the original 1972 definition
- Functional polarisation states (M1, M2, mregDC, IL4I1_Mac) are state descriptors, not lineage descriptors

## Open problems

- Cross-tissue, cross-disease, cross-species MPS reference at higher resolution
- Lineage-tracing-validated taxonomy that combines ontogeny and state

## Key papers

- [[papers/cross-tissue-single-cell-landscape-human]] — pan-tissue single-cell decomposition of the human MPS into the MNP-VERSE / MoMac-VERSE

## My understanding

The MPS framing is the canonical entry point into innate-immune cell biology and the natural superset for the MoMac-VERSE atlas. Used as the framework concept that justifies why an integrated MNP-only atlas is valuable in the first place.
