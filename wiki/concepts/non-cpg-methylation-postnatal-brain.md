---
title: "Non-CpG methylation (mCH / mCA) in the postnatal mammalian brain"
aliases:
  - "mCH"
  - "mCA"
  - "non-CpG methylation"
  - "mCH brain methylation"
  - "neuronal mCA"
tags:
  - DNA-methylation
  - non-CpG
  - mCA
  - mCH
  - brain
  - neurons
maturity: stable
key_papers:
  - spatial-joint-profiling-dna-methylome-transcriptome
first_introduced: "Guo et al. *Nat Neurosci* 2014; Lister et al. *Science* 2013"
date_updated: 2026-05-27
related_concepts:
  - spatial-dmt-method
  - variably-methylated-regions-vmr
---

## Definition

Non-CpG methylation (mCH, where H = A, C, or T; predominantly mCA) is methylation deposited outside the canonical symmetric CpG dyad. In mammals it is uniquely abundant in post-mitotic neurons of the postnatal brain, where mCA accumulates progressively through early life and is read by MeCP2 to repress long, gene-body-methylation-prone neuronal genes ([[foundations/mecp2-methyl-cpg-binding-protein]]).

## Intuition

Most cells barely tolerate mCH; in the postnatal mammalian brain, neurons accumulate mCA throughout postnatal development to levels rivalling mCG at some loci. Because mCH is not symmetric, it cannot be propagated by DNMT1 — it is laid down de novo by DNMT3A and read by MeCP2. Its loss (MeCP2 LoF) causes Rett syndrome; its excess (MECP2 duplication) causes neurological gain-of-dose disease. mCA is therefore a neuron-specific epigenetic axis that mCG-only assays miss.

## Formal notation

- Symmetry: mCH is asymmetric (single-strand). mCpA is the dominant context.
- Deposition: DNMT3A (de novo, postnatal); reading: MeCP2 (gene-body density-dependent).
- Tissue distribution: mCA < 1% in embryos, ~3–4% in P21 mouse brain, ~5–8% in adult human brain.
- Functional rule: long gene bodies with high mCA load are preferentially silenced by MeCP2.

## Variants

- **mCpA** — dominant non-CpG context in brain.
- **mCpT, mCpC** — minor contributions, mostly background.
- **Plant mCHG / mCHH** — non-CpG methylation in plants is far higher and mechanistically distinct.

## Comparison

- vs **mCG**: mCG is symmetric, replicated by DNMT1, ubiquitous. mCH is asymmetric, post-mitotic, brain-specific.
- vs **5hmC**: 5hmC is also enriched in brain but distinct chemistry (oxidised mCG).
- vs **gene-body mCpG**: gene-body mCG correlates positively with expression; gene-body mCA correlates negatively, especially for long neuronal genes.

## When to use

- Distinguishing neuronal maturation states in postnatal vs embryonic brain methylomes.
- Quantifying MeCP2-target gene silencing genome-wide.
- Cross-validation of single-cell or spatial methylome cell-type calls in the brain.

## Known limitations

- Requires deep coverage (mCA is ~10× sparser than mCG).
- Bisulfite / EM-seq do not distinguish mCpA from 5hmCpA chemically.
- Most analysis pipelines default to mCG; mCH support is sparser.

## Open problems

- Per-pixel / per-cell mCA mapping at spatial resolution beyond cortical regions.
- Decoupling mCA-driven from mCG-driven gene silencing at MeCP2-target loci.

## Key papers

- [[papers/spatial-joint-profiling-dna-methylome-transcriptome]] — Lee et al. *Nature* 2025; first spatially-resolved mCH/mCA map of the P21 mouse brain. Shows mCG vs mCA gene-specific regulation: Prox1, Bcl11b correlate with both; Ntrk3, Satb1 only with mCG; Cux1 (CA1/2) only with mCA — directly demonstrating modality-specific regulation in tissue context.

## My understanding

Non-CpG methylation is the most under-appreciated axis of brain epigenetics. Standard methylome workflows discard mCH or aggregate it into background, but in postnatal neurons it carries the bulk of the MeCP2-dependent regulatory signal. Spatial-DMT is the first method to spatially resolve mCG/mCA partitioning across brain anatomy — and the regulatory partitioning it reveals (mCG-only vs mCA-only vs both, gene-by-gene) suggests that "the brain methylome" is actually two semi-independent regulatory grids stacked on top of each other.
