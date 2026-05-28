---
title: "Hypusine-eIF5A-dependent selective translation of cell-adhesion and signalling mRNAs"
aliases:
  - "hypusine-dependent selective translation"
  - "eIF5A translational control of adhesion transcripts"
tags:
  - translation
  - eIF5A
  - cell-adhesion
  - macrophage
  - ribosome-stalling
maturity: emerging
key_papers:
  - transition-monocyte-tissue-resident-macrophage-requires
first_introduced: "Carrizo et al., Nature 2026"
date_updated: 2026-05-28
related_concepts:
  - polyamine-hypusine-axis-macrophage-residency
---

## Definition

The principle that hypusinated [[foundations/eif5a-hypusine]] is selectively required to translate a defined subset of mRNAs — enriched for ribosome-stalling features such as polyproline/diproline motifs — and that in macrophages this subset is disproportionately composed of cell-adhesion and signalling transcripts whose products underpin tissue residency.

## Intuition

eIF5A acts as a translational "filter": most proteins are made fine without abundant hypusine, but a stall-prone subset drops off ribosomes when hypusination falls. Sequencing ribosome-engaged transcripts (not just total RNA) is what exposes this filter, because the affected transcripts can be present yet poorly translated.

## Formal notation

n/a — operationally: transcripts significantly depleted in ribosome-pulldown but stable in input across genotypes.

## Variants

- Polyproline-motif transcripts vs other stall-inducing sequences.
- Direct eIF5A-dependent targets vs indirectly affected (e.g. via reduced transcription factors).

## Comparison

- A mechanistic complement to [[concepts/polyamine-hypusine-axis-macrophage-residency]]: this concept is the "which transcripts" layer.

## When to use

When interpreting RiboTag/ribosome-profiling data in eIF5A/DHPS perturbations, or arguing that a protein deficit is translational rather than transcriptional.

## Known limitations

- The motif rules for hypusine dependency are incompletely defined.
- Input contamination by non-target cells can blur target calls.

## Open problems

- A predictive model of hypusine-dependent transcripts from sequence alone.

## Key papers

- [[papers/transition-monocyte-tissue-resident-macrophage-requires]] — RiboTag identifies 13 ribosome-depleted transcripts (Il1rl1, Tnik, Icos, Cd28, Axin2, Amigo2, Fam83g, Rab44, Oasl1) in DHPS-deficient macrophages.

## My understanding

The strongest causal thread in the paper: by reading the translatome rather than the transcriptome, the authors localize the defect to translation of adhesion/signalling messages, giving the polyamine–hypusine axis a concrete molecular output.
