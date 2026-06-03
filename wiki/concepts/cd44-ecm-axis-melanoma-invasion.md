---
title: "CD44–ECM ligand-receptor axis in melanoma invasion"
aliases: ["CD44 ECM interactome melanoma", "CD44-collagen-integrin-FGF axis"]
tags: [melanoma, cell-cell-interaction, extracellular-matrix, therapeutic-target]
maturity: emerging
key_papers:
  - integrating-12-spatial-single-cell-technologies
first_introduced: "2025"
date_updated: 2026-06-03
related_concepts: [differential-stromal-interactions-skin-cancer, spatially-constrained-ligand-receptor-inference]
---

## Definition

The convergence of multiple extracellular-matrix and growth-factor ligands onto the receptor CD44 in the melanoma microenvironment — including collagens (COL1A1/2, COL6A1/2, COL4A1), fibronectin (FN1), MMP9, and fibroblast growth factors (FGF1/FGF2) — forming a dominant, melanoma-enriched interaction hub implicated in ECM remodelling, invasion, and as a candidate therapeutic axis (notably CD44-FGF2).

## Intuition

CD44 acts as a multi-ligand docking hub: it localises MMP9 to degrade collagen, anchors cells via fibronectin, and engages FGFs to amplify proliferative signalling. In melanoma this hub is far more active than in keratinocyte cancers, concentrating ECM-driven pro-invasive signalling on a single targetable receptor.

## Formal notation

Not applicable. Appears as L-R pairs with CD44 as receptor (COL*-CD44, FN1-CD44, MMP9-CD44, FGF1/2-CD44, MIF-CD44) enriched in melanoma interactomes.

## Variants

- Collagen-CD44 (ECM remodelling)
- FGF-CD44 / FGF-FGFR1 (proliferation)
- MMP9-CD44 (protease docking, invasion)

## Comparison

Contrasts with cSCC (SPP1-integrin/CD44 dominance) and BCC (WNT/angiogenesis dominance); CD44-ECM is a melanoma-specific signature within [[differential-stromal-interactions-skin-cancer]].

## When to use

When prioritising melanoma interaction targets, or interpreting collagen/integrin/FGF signalling in pigmented-lesion microenvironments.

## Known limitations

- CD44 isoform complexity
- Validated for a few pairs (CD44-FGF2, CD44-MMP9, CD44-FN1) only
- Therapeutic tractability of CD44 unproven

## Open problems

- Isoform-specific targeting
- Whether disrupting CD44-FGF2 blocks invasion in vivo

## Key papers

- [[integrating-12-spatial-single-cell-technologies]] — nominates CD44 as a dominant melanoma receptor and validates CD44-MMP9, CD44-FN1, CD44-FGF2 by PLA, proposing CD44-FGF2 as a therapeutic target with TCGA prognostic value.

## My understanding

A concrete, validated, melanoma-specific interaction hub — the paper's strongest candidate-target story and a clean example of omics→experimental validation.
