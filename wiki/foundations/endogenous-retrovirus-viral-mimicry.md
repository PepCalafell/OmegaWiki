---
title: "Endogenous retroviruses and viral mimicry"
slug: endogenous-retrovirus-viral-mimicry
domain: "genomics / innate immunity"
status: mainstream
aliases:
  - "ERV"
  - "endogenous retrovirus"
  - "viral mimicry"
  - "transposable element derepression"
first_introduced: "Chiappinelli et al. 2015; Roulois et al. 2015 (viral mimicry by ERV derepression)"
date_updated: 2026-06-03
source_url: "https://doi.org/10.1016/j.cell.2015.07.011"
---

## Definition

Endogenous retroviruses (ERVs) are LTR-class transposable elements embedded in the genome. When normally silenced ERVs (and other repeat elements) are derepressed, their bidirectional transcription can generate double-stranded RNA that is sensed by cytosolic pattern-recognition receptors (RIG-I/MDA5), activating the TBK1–IRF3 axis and a type I interferon response — a state termed "viral mimicry".

## Intuition

The cell mistakes its own derepressed retroelement transcripts for a viral infection and mounts an interferon response. Pharmacological or epigenetic derepression of ERVs (e.g., by DNMT inhibitors, or as an off-target drug effect) can thus switch on Ifnb1 and interferon-stimulated genes.

## Formal notation

- Trigger: ERV/LTR (and SINE/LINE) derepression → cytoplasmic dsRNA → RIG-I/MDA5 → MAVS → TBK1/IRF3 → IFNβ.
- Quantified by locus-specific and family-wise TE expression from RNA-seq.

## Key variants

- DNA-sensing viral mimicry (cytosolic dsDNA → cGAS–STING → TBK1) as a parallel route.
- DNMT/HDAC-inhibitor-induced viral mimicry in cancer therapy.

## Known limitations

- Hard to pinpoint which specific repeat elements causally drive a given IFN response.
- TE quantification from short reads is mapping-ambiguous.

## Open problems

- Causal mediators linking specific drug off-targets to ERV derepression.
- Therapeutic exploitation of viral mimicry without unwanted inflammation.

## Relevance to active research

[[papers/integrative-epigenome-based-strategy-unbiased-functional]] finds that seven CKIs which unexpectedly upregulated Ifnb1 also induced transposable elements (notably ERVs/LTRs) in mouse macrophages, proposing viral-mimicry-driven interferon induction as an off-target consequence detectable by the epigenome-based approach (paralleling Trametinib-induced retroelement activation reported in pancreatic cancer).
