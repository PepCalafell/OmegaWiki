---
title: "Bystander-free precision base editing of splice sites"
aliases:
  - "bystander-free base editing"
  - "single-nucleotide-precision base editing"
  - "splice-site base correction"
tags:
  - base-editing
  - genome-editing
  - precision
  - splice-site
  - TGM1
maturity: emerging
key_papers:
  - editing-skin-place-vivo-genome-correction
first_introduced: "2026"
date_updated: 2026-06-02
related_concepts: []
---

## Definition

Correction of a single pathogenic nucleotide by a cytosine base editor engineered so that it edits only the target base and leaves neighbouring "bystander" cytosines within the editing window untouched — critical when the target lies in a highly conserved sequence motif such as a splice acceptor site, where a bystander edit could itself be deleterious.

## Intuition

Standard base editors deaminate every cytosine in their activity window, so correcting a base in a conserved motif risks introducing a new harmful change next door. Splice sites are exactly such motifs. The advance is an editor narrow enough to hit only the disease-causing base — making base editing usable for the large class of splice-site mutations that were previously off-limits because of bystander risk.

## Variants

- **eTD-CBE** — next-generation high-precision cytosine base editor; up to 26% on-target editing at *TGM1* c.877-2A>G with **no** bystander editing in patient keratinocytes
- **BE4max-NG** — relaxed-PAM standard editor; ~20% editing at *both* target and bystander nucleotide (illustrating the bystander problem)
- Other engineered narrow-window CBEs / context-tuned deaminases

## Comparison

eTD-CBE vs BE4max-NG on the same *TGM1* splice-acceptor target: comparable target efficiency (26% vs 20%) but a categorical safety difference — eTD-CBE produces no bystander edit, whereas BE4max-NG edits the bystander cytosine at the same ~20% rate. For a conserved splice motif, that distinction is the difference between a safe correction and a potentially new pathogenic change.

## When to use

When the pathogenic base sits within or adjacent to a functionally constrained motif (splice sites, regulatory elements) where collateral bystander editing cannot be tolerated. Editor selection should be driven by a bystander-readout screen, not target efficiency alone.

## Key papers

- [[papers/editing-skin-place-vivo-genome-correction]]

## Open problems

- Maintaining narrow-window precision while raising on-target efficiency
- Generalising bystander-free editing across diverse splice-site and regulatory contexts
- Comprehensive off-target characterisation (sgRNA-dependent and -independent) at therapeutic scale

## My understanding

This is the first of the two advances the commentary highlights ("single-nucleotide precision"). It matters beyond ARCI: splice-site mutations are common across genetic disease, and a bystander-free editor expands the correctable mutation space well past the narrow set where neighbouring edits happen to be tolerable.
