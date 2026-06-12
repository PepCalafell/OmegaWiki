---
title: "DNA methylation mediates genetic variant effects on cytokine responses"
aliases: []
tags: [mediation, dna-methylation, genetics, cytokine, trained-immunity, mqtl]
maturity: emerging
key_papers:
  - long-term-dna-methylation-changes-mediate
first_introduced: "2025"
date_updated: 2026-06-12
related_concepts: [dna-methylation-substrate-trained-immunity-epigenetic, cell-type-specific-genetic-regulation-immune]
---

## Definition

The inference, from bidirectional mediation analysis integrating genotype, methylation, and cytokine data in the same individuals, that BCG-induced DNA-methylation changes (DNAm-C) act as in silico causal mediators transmitting genetic-variant effects onto trained-immunity cytokine changes.

## Intuition

A SNP can influence a cytokine response indirectly by shaping a methylation change. Triangulating SNP–methylation–cytokine triplets and testing both directions estimates how much of a genetic effect "flows through" methylation, positioning methylation as a modulator between genotype and immune phenotype.

## Formal notation

For SNP x, mediator DNAm-C m, outcome cytokine change y: test Direction1 (m mediates x→y) and Direction2 (y mediates x→m); report proportion mediated. E.g. cg21375332 (SLC12A3) mediates 32.7% of rs604639→IFN-γ; cg25926804 (GSDMC) mediates 28.6% of rs6991078→IFN-γ.

## Variants

- Unidirectional (Direction1: methylation-mediated) vs Direction2 (TI-mediated) vs bidirectional
- Cytokine-specific: most linkages for IFN-γ, some for IL-1β/TNF-α

## Comparison

More linkages arise in the methylation-mediated direction, favoring methylation as upstream modulator of the cytokine change.

## When to use

When ordering genotype, epigenome, and immune-phenotype layers to infer mechanism from cross-sectional multi-omics.

## Known limitations

In silico, observational mediation cannot prove causality; direction can be ambiguous; nominal-significance thresholds.

## Open problems

Experimental confirmation of mediating CpGs; resolving bidirectional cases.

## Key papers

- [[long-term-dna-methylation-changes-mediate]] — performs bidirectional SNP–DNAm-C–cytokine mediation, highlighting SLC12A3 and GSDMC loci.

## My understanding

Frames methylation as the mechanistic relay between immune-response genetics and trained-immunity output, with concrete candidate loci.
