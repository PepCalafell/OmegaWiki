---
title: "mRNA-protein discordance in single cells"
aliases:
  - mRNA-protein correlation
  - protein covariation
  - transcript-protein discordance
  - post-transcriptional regulation single-cell
  - protein-vs-mRNA mismatch
  - mRNA protein decoupling
  - translation regulation single-cell
  - protein not predicted by mRNA
  - functional proteome vs transcriptome
  - protein complex stabilization
tags:
  - multi-omics
  - proteomics
  - translation
  - post-transcriptional-regulation
  - single-cell
maturity: active
key_papers:
  - mapping-early-human-blood-cell-differentiation
first_introduced: "Documented at bulk level since the 2000s (Vogel & Marcotte 2012); systematically quantified at single-cell level by Specht et al. 2021, Furtwängler et al. 2025"
date_updated: 2026-05-26
related_concepts:
  - single-cell-proteomics-mass-spec
  - scprotvelo-translation-dynamics
---

## Definition

The observation, well-established at bulk level and now extended to single cells, that mRNA abundance is a weak predictor of protein abundance for a substantial fraction of the proteome. Drivers include translation rate variation, protein degradation, complex-mediated stabilization, and temporal lag between transcription and translation.

## Intuition

mRNA is a transient intermediate; protein is the functional molecule. If translation, degradation, and stabilization vary by gene and by cell state, mRNA cannot fully predict protein. For some genes (housekeeping, abundant, fast-turnover) mRNA is a strong proxy; for others (chromatin regulators in quiescent cells, complex subunits, slow-turnover proteins) it is not.

## Formal notation

For a gene *g* across cells, define correlation vectors:
- *r_g^mRNA* = correlation of mRNA(*g*) with pseudotime or fate probability
- *r_g^protein* = correlation of protein(*g*) with the same axis
The mRNA-protein discordance score is |*r_g^mRNA* − *r_g^protein*|.

In [[papers/mapping-early-human-blood-cell-differentiation]], the overall correlation between mRNA and protein vectors across HSPC differentiation was <0.25; an external bulk dataset of 59 breast cancer cell lines showed mRNA-protein rank correlation = 0.35, supporting that this is system-spanning.

## Variants

- **Quiescent-state discordance**: most extreme in low-effect-size states like HSC quiescence; chromatin regulators (HMGA1, HP1BP3, macroH2A1) detectable on protein, not mRNA.
- **Complex-mediated discordance**: B2M protein covaries with HLA-A/B (MHC-I) without mRNA covariation — stabilization by complex assembly.
- **Lineage-specification discordance**: smaller during active differentiation because effect sizes are larger and signal-to-noise improves.

## Comparison

- vs RNA velocity directionality errors: the erythroid Late→Early backflow seen with standard scVelo is partly a manifestation of mRNA-protein decoupling that splicing kinetics alone cannot resolve.
- vs CITE-seq agreement: CITE-seq surface markers often agree with their cognate mRNA because surface markers are typically high-abundance and fast-turnover; mRNA-protein discordance is most severe for low-abundance, slow-turnover, or complex-stabilized proteins.

## When to use

- Whenever interpreting scRNA-seq cluster identities at the level of "what does this cell *do*", not "what is this cell transcribing".
- Whenever an scRNA-seq result fails to validate at the protein / functional level — consider discordance before assuming the scRNA-seq is wrong.

## Known limitations

- Per-cell quantification of discordance currently relies on integrated, not paired, multi-omics; the discordance estimates are population-level.
- Highly missing scp-MS data underestimate the true number of discordant proteins because many are filtered out.

## Open problems

- Mechanism-by-mechanism dissection of *why* specific proteins are discordant (translation rate, degradation, stabilization).
- Paired single-cell mRNA + untargeted protein measurements (vs current unpaired integrations).
- Translating bulk-derived translation-rate priors into single-cell models.

## Key papers

- [[papers/mapping-early-human-blood-cell-differentiation]] — single-cell discordance quantified across human HSPC hierarchy.

## My understanding

This concept is one of the load-bearing interpretive frames of the Furtwängler 2025 paper: most of the biological surprises (chromatin regulators in HSCs, B2M-MHC-I co-stabilization, SOD1/TALDO1 as functional regulators) only become visible on the protein layer. For my own work on scRNA-seq atlases, this is a reminder that mRNA-only "phenotypes" need explicit caveats.
