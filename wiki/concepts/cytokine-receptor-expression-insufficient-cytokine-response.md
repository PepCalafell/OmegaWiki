---
title: "Cytokine receptor expression is insufficient to predict cytokine response"
aliases:
  - receptor expression insufficient
  - ligand-receptor inference limitation
  - cytokine response signature required
  - receptor absent but response present
  - receptor present no response
  - downstream signature inference
  - CellPhoneDB CellChat limitation
  - L-R inference insufficient
  - cytokine response prediction
  - signature-based cytokine inference
maturity: stable
tags:
  - cytokines
  - cell-cell-communication
  - methodological
  - scRNA-seq
key_papers:
  - dictionary-immune-responses-cytokines-single-cell
first_introduced: "2024"
date_updated: 2026-05-13
related_concepts:
  - cytokine-mediated-immune-cell-cell-interactome
---

## Definition

Receptor expression alone is not a reliable predictor of in vivo cytokine response: cells with high receptor levels often fail to respond (ligand may not reach the cell, downstream pathway non-functional), and cells with low or undetectable receptor levels can mount strong responses (rapid secondary effects, undetected receptors, or sensitive direct signaling) — e.g., IL-1α/β affecting T cells, NK cells, DCs without strong receptor transcript detection.

## Intuition

Ligand–receptor inference tools (CellPhoneDB, CellChat, NicheNet variants) systematically over- or under-call interactions because they rely on transcript-level receptor expression. The Immune Dictionary + IREA approach corrects this by requiring the *downstream cytokine response signature* — a direct functional readout.

## Variants

- False positives: receptor expressed, no response signature
- False negatives: response signature present, receptor below detection
- Mismatch attributed to ligand bioavailability, post-translational receptor regulation, or rapid secondary cytokines

## When to use

Any project using CellPhoneDB / CellChat / NicheNet — flag receptor-alone inferences and corroborate with response-signature enrichment when possible.

## Key papers

- [[papers/dictionary-immune-responses-cytokines-single-cell]]

## My understanding

Methodologically important: the L-R inference paradigm dominates current scRNA-seq communication analyses but is fundamentally limited. IREA-style downstream-signature methods are the natural successor.
