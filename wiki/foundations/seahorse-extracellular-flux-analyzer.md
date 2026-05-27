---
title: "Seahorse extracellular flux analyzer (XF24 / XFe96)"
slug: seahorse-extracellular-flux-analyzer
domain: "methods / immunometabolism / bioenergetics"
status: mainstream
aliases:
  - "Seahorse XF"
  - "Seahorse XF24"
  - "Seahorse XFe96"
  - "extracellular flux analysis"
  - "Mito Stress Test"
  - "Glycolysis Stress Test"
  - "ECAR/OCR analyzer"
first_introduced: "Wu et al. 2007 (Agilent/Seahorse Bioscience platform)"
date_updated: 2026-05-27
source_url: "https://www.agilent.com/en/product/cell-analysis"
---

## Definition

The Seahorse extracellular flux analyzer measures oxygen consumption rate (OCR, proxy for mitochondrial respiration) and extracellular acidification rate (ECAR, proxy for glycolysis-derived lactic acid plus mitochondrial CO₂) in live, adherent cells in real time using optical fluorescence sensors in a transient micro-chamber above the monolayer. Sequential injection of metabolic effectors permits decomposition of bioenergetic parameters.

## Intuition

A bench-top platform to read the metabolic "speedometer" and "tachometer" of a cell population without lysis or labeling, by sealing a small volume above the cells and watching how fast O₂ disappears (OCR) and protons accumulate (ECAR).

## Formal notation

Standard stress-test injections:

- **Glycolysis Stress Test (ECAR)**: glucose → oligomycin (ATP-synthase inhibitor) → 2-DG (hexokinase inhibitor). Yields glycolysis, glycolytic capacity, glycolytic reserve.
- **Mito Stress Test (OCR)**: oligomycin → FCCP (uncoupler) → rotenone + antimycin A (Complex I + III inhibitors). Yields basal respiration, ATP-linked OCR, maximal respiration, spare capacity, non-mitochondrial OCR.

## Key variants

- XF24 (24-well, primary-cell-friendly); XFe96 (96-well, higher throughput); XFp (8-well miniature); XF Pro (latest, real-time substrate switching).

## Known limitations

- ECAR conflates glycolytic lactic acid with mitochondrial CO₂-derived carbonic acid — rotenone/antimycin A injection is needed to separate them (relevant in cells with low glycolysis like alveolar macrophages).
- Adherence-dependent — non-adherent cells require coating (Cell-Tak) and may dislodge during injections.
- Bulk readout per well; cannot resolve cell-to-cell heterogeneity.

## Open problems

- Translating ECAR/OCR to absolute ATP production requires assumptions about coupling efficiency that are violated under stress.

## Relevance to active research

Routinely used to phenotype immunometabolism. In [[papers/hif-regulates-mitochondrial-function-bone-marrow]] (Woods et al., *Sci. Rep.* 2025), the XF24 platform with Glycolysis and Mito Stress Tests separates HIF-1α-dependent vs HIF-1α-independent ECAR/OCR responses in TR-AMs vs BMDMs and identifies a compensatory OCR elevation in Hif1a⁻/⁻ BMDMs that Myc-siRNA reverses.
