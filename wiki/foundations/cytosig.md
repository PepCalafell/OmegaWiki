---
title: "CytoSig"
slug: "cytosig"
domain: "single-cell genomics / cytokine signaling inference"
status: mainstream
aliases:
  - CytoSig
  - cytokine signaling activity
first_introduced: "Jiang et al., Nature Methods 2021"
date_updated: 2026-06-03
source_url: "https://cytosig.ccr.cancer.gov/"
---

## Definition

CytoSig is a data-driven framework that infers cytokine signaling activity from transcriptomic profiles using response signatures learned from thousands of cytokine-treatment experiments.

## Intuition

A cell's transcriptome encodes a footprint of the cytokines acting on it; CytoSig scores each cytokine's downstream response signature to estimate which cytokines are active, even without measuring the cytokines directly.

## Formal notation

For each cytokine, a regression of expression against curated response signatures yields an activity score (and significance) per sample/cell, reflecting predicted signaling strength.

## Key variants

- Bulk and single-cell application modes.
- Paired with perturbation datasets to predict response to cytokine modulation.

## Known limitations

- Signatures derived largely from in vitro treatments may not transfer to all in vivo contexts.
- Cannot distinguish autocrine from paracrine sources of a cytokine.

## Open problems

- Resolving overlapping signatures of related cytokines (e.g. IFN-I vs IFN-γ programs).

## Relevance to active research

Used to assign interferon-type preference to TAM subsets (IFN-I for IFIT1+ vs IFN-γ for CXCL9+ TAMs) and to nominate dominant cytokines (MCSF/GCSF, TGFB1, VEGFA) per TME group for matched therapeutic targeting.
