---
title: "CTHRC1+ ECM-remodeling fibroblast (eFibro_CTHRC1) — pan-cancer leading-edge CAF"
aliases:
  - CTHRC1+ CAF
  - CTHRC1+ fibroblast
  - eFibro_CTHRC1
  - ECM-remodeling fibroblast
  - matrix-remodeling CAF
  - leading-edge CAF
  - FAP+ LRRC15+ POSTN+ CAF
  - canonical ECM-remodelling CAF
  - tumor-edge CAF
  - pan-cancer ECM CAF
  - CTHRC1 collagen triple helix CAF
  - matrix-stiffness-activated fibroblast
tags:
  - pan-cancer
  - caf
  - stromal
  - ecm
  - leading-edge
  - spatial
  - immune-exclusion
  - tme
maturity: emerging
key_papers:
  - spatiotemporal-analyses-pan-cancer-single-cell
first_introduced: "2025"
date_updated: 2026-05-26
related_concepts:
  - ecm-mycaf-leading-edge-signaling-axis
  - col11a1-spp1-fibrotic-axis-cd8-exclusion-nsclc
  - pre-cafs-cancer-associated-fibroblasts-premalignant
  - cthrc1-slpi-profibrotic-spatial-ecotype
---

## Definition

An ECM-remodeling fibroblast subtype defined by high CTHRC1 expression that, across at least 23 cancer types in pan-cancer scRNA-seq, also co-expresses canonical CAF markers FAP, LRRC15, and POSTN. Functionally enriched for EMT, ECM receptor interaction, focal adhesion, and glycosaminoglycan biosynthesis (chondroitin/dermatan sulfate). Spatially localized at the leading edge between malignant and normal tissue in 78% (32/41) of analyzed ST slides.

## Intuition

CTHRC1+ CAFs operationalize the long-standing "FAP+ CAF" / "LRRC15+ CAF" / "myCAF" concepts into a single pan-cancer, spatially anchored entity: an ECM-depositing fibroblast that **walls off** the malignant region from the normal parenchyma, simultaneously preventing T-cell entry via dense matrix and via LGALS9-mediated CD8+ T-cell interactions.

## Comparison

- More canonical and pan-cancer than COL11A1+ NSCLC-specific axis ([[concepts/col11a1-spp1-fibrotic-axis-cd8-exclusion-nsclc]]); CTHRC1 is the cross-tissue marker.
- Distinct from inflammatory CAFs (iFibro_IL6 in [[papers/spatiotemporal-analyses-pan-cancer-single-cell]]) which are precancerous-enriched, not tumor-enriched.
- Distinct from pre-CAFs ([[concepts/pre-cafs-cancer-associated-fibroblasts-premalignant]]) which appear before histological malignancy.
- Likely overlaps with the myCAF leading-edge axis ([[concepts/ecm-mycaf-leading-edge-signaling-axis]]) — CTHRC1+ may be a canonical molecular label for that geometry.

## Key papers

- [[papers/spatiotemporal-analyses-pan-cancer-single-cell]] — defines eFibro_CTHRC1 across 4.5M pan-cancer cells, validates spatial leading-edge localization across 6 cancer types in ST, and shows TCGA prognostic value (KIRC P=0.00523; BLCA P=0.00568).

## When to use

- Annotating ECM-remodeling fibroblasts in any solid tumor scRNA-seq dataset — CTHRC1 + FAP + LRRC15 + POSTN is the recommended canonical marker set.
- Interpreting TCGA bulk for stromal immune-exclusion signal: the eFibro_CTHRC1 signature anti-correlates with CD8+ T infiltration across nearly all cancer types.
- Designing anti-stromal therapeutic strategies: TGFβ1 and IL-1β are the inferred shared upstream inducers (paired with [[concepts/slpi-macrophage-profibrotic-tam]] in the profibrotic ecotype).

## Open problems

- Is CTHRC1+ CAF leading-edge enrichment hypoxia-driven? Cross-reference with [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] needed.
- How early does the CTHRC1+ phenotype emerge — is it absent in IL1B-IL1R1 precursor niches ([[concepts/epithelial-proinflammatory-niche-il1b-il1r1-luad-precursor]])?
- Are LGALS9–CD44 and LGALS9–HAVCR2 interactions therapeutically tractable in this subtype?
