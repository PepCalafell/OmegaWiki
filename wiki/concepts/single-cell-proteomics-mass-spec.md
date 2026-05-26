---
title: "Single-cell proteomics by mass spectrometry (scp-MS)"
aliases:
  - scp-MS
  - SCoPE-MS
  - SCoPE2
  - single-cell mass spec proteomics
  - single-cell proteomics by MS
  - LC-MS single-cell proteomics
  - untargeted single-cell proteomics
  - peptide carrier proteomics
  - TMT single-cell proteomics
  - isobaric labeling single-cell
  - mass-spec-based scProteome
  - plexDIA single-cell
tags:
  - proteomics
  - single-cell
  - mass-spectrometry
  - methods
maturity: emerging
key_papers:
  - mapping-early-human-blood-cell-differentiation
first_introduced: "Specht et al. 2021 *Genome Biol* (SCoPE2); generalized in Schoof, Furtwängler et al. (SCoPE-MS / SCeptre lineage)"
date_updated: 2026-05-26
related_concepts:
  - mrna-protein-discordance
  - joint-multimodal-latent-space
---

## Definition

Single-cell proteomics by mass spectrometry (scp-MS) quantifies thousands of proteins from individual mammalian cells using LC-MS/MS, typically combined with isobaric labeling (TMT/TMTpro) and a peptide carrier channel that boosts ionization without contaminating quantification of the single-cell channels. Distinct from antibody-based single-cell protein methods (CITE-seq, AbSeq, FACS), scp-MS is untargeted and label-free in terms of which proteins are quantified — proteins are detected by their tryptic peptides rather than by pre-selected antibodies.

## Intuition

Antibody methods constrain the questions you can ask to whatever pre-existing antibody panel you committed to. scp-MS, in contrast, returns a discovery-mode proteome per cell — limited only by ionization, dynamic range, and instrument sensitivity. The cost is missing values: at current sensitivity, ~50-70% of detectable proteins are missed in any individual cell, and depth caps around 1-3k proteins per cell.

## Formal notation

For each cell *i*, scp-MS yields a vector *p_i* ∈ ℝ^P of protein abundances over P quantified proteins, with a high fraction of missing entries. A typical workflow:

1. FACS-sort one cell per well in a 384-well plate.
2. Lyse, digest with trypsin, label peptides with one TMTpro tag per well.
3. Pool 14 single-cell wells with a 200-cell peptide carrier (TMTpro-126) into one MS run.
4. Acquire on Orbitrap with real-time search-assisted acquisition (RETICLE).
5. Quantify by reporter-ion intensity; normalize, filter, and batch-correct via SCeptre.

## Variants

- **SCoPE-MS / SCoPE2**: original single-cell TMT method with peptide carrier (Slavov lab).
- **plexDIA**: data-independent acquisition variant with multiplexed precursor ions.
- **N-DISCO / nanoPOTS**: nanoflow / chip-based single-cell front-ends.
- **SCeptre-processed scp-MS**: the Schoof / Furtwängler lineage used in [[papers/mapping-early-human-blood-cell-differentiation]].

## Comparison

- vs CITE-seq: untargeted, ~10-20× deeper proteome, but ~10× more missing values and lower throughput.
- vs bulk proteomics: per-cell resolution, but ~100× shallower coverage per sample.
- vs scRNA-seq: measures the actual functional molecule (protein) with translation lag, but at coarser depth.

## When to use

- When mRNA is suspected to poorly predict protein (immature cells, quiescent states, post-transcriptionally regulated systems).
- When the question concerns chromatin regulators, metabolic enzymes, or complex-stabilized proteins (MHC-I, ribosomal subunits).
- When unbiased proteome-wide discovery is needed, not validation of a pre-selected panel.

## Known limitations

- High missingness (~50-70% per cell).
- Throughput orders of magnitude below scRNA-seq.
- Membrane proteins and very-low-abundance regulators (TFs) are under-detected.
- Requires specialized hardware (high-resolution Orbitrap with real-time search) and pipelines (SCeptre, alphaTims, MaxQuant).

## Open problems

- Reducing missingness without sacrificing throughput.
- Standardized batch correction across labs and instruments.
- Bridging scp-MS depth to ChIP-MS / IP-MS-style functional readouts in the same single cells.

## Key papers

- [[papers/mapping-early-human-blood-cell-differentiation]] — Furtwängler et al. 2025 *Science*; 2500+ CD34+ HSPCs.

## My understanding

scp-MS is graduating from a methods novelty to a usable atlas-scale tool, but only just. The Furtwängler 2025 paper is the first to demonstrate that you can recapitulate an in vivo human differentiation hierarchy entirely from MS-based proteomes — until now, only cell-line systems had been benchmarked at this scale.
