---
title: "Tumor-derived cGAMP as an immunotransmitter in the TME"
aliases:
  - extracellular cGAMP
  - cGAMP immunotransmitter
  - paracrine cGAMP signaling
  - SLC19A1 SLC46A2 LRRC8
tags:
  - cgas-sting
  - extracellular-signaling
  - cgamp
  - macrophage
  - dendritic-cell
  - nk-cell
maturity: stable
key_papers:
  - targeting-sting-generate-therapeutic-anti-tumor
first_introduced: "2018"
date_updated: 2026-05-27
related_concepts: []
---

## Definition

cGAMP, in addition to its intracellular role, is exported from tumor cells and imported by neighboring TME cells (macrophages via SLC46A2; T cells and others via SLC19A1; bystander cells via LRRC8 volume-regulated anion channels). Acts as a paracrine "immunotransmitter" that activates STING in non-producing cells — DCs (cross-presentation), macrophages (M1 polarization), NK cells (cytotoxicity), ECs (vascular normalization) — and, conversely, can trigger T-cell death.

## Intuition

Cancer cells produce a soluble innate-immune signal that can be received by every TME cell type expressing the right importer. Therapeutic strategies that *preserve* this endogenous cGAMP (ENPP1 inhibition) leverage tumor-autonomous DNA damage to drive STING activation across the TME — no exogenous agonist required.

## Variants

- ENPP1 hydrolyzes extracellular cGAMP; ENPP1 inhibitors preserve the signal
- MerTK blockade on macrophages enhances P2X7R-dependent macrophage uptake of cGAMP
- cGAMP recruits dendritic cells to tumors and promotes immunogenicity

## When to use

When interpreting "spontaneous" STING-IFN signatures in tumors with intact cGAS but without exogenous agonist — extracellular cGAMP is the likely propagator. When designing combination therapies, ENPP1 inhibitors are the most direct lever to amplify endogenous cGAMP.

## Key papers

- [[papers/targeting-sting-generate-therapeutic-anti-tumor]]

## Open problems

- Quantification of extracellular cGAMP concentrations in human tumors
- Which importer (SLC19A1, SLC46A2, LRRC8) dominates in which TME cell type and how to bias activation toward antitumor recipients (DCs, NK) and away from T cells

## My understanding

The "tumor cells are paracrine STING agonist factories" insight is one of the most exploitable mechanisms in the field — it suggests that the right therapeutic posture is to *amplify endogenous cGAMP* (ENPP1i) rather than *add exogenous CDNs*. Aligns with the broader Stanford/Li-Wang/Cordova ENPP1 program.
