---
title: "Positive methylation–expression coupling at VMRs"
aliases:
  - "positive methylation-gene-expression coupling"
  - "positive VMR-expression correlation"
  - "non-canonical methylation activation"
tags:
  - DNA-methylation
  - gene-expression
  - epigenetics
  - VMR
  - enhancer
maturity: stable
key_papers:
  - spatial-joint-profiling-dna-methylome-transcriptome
first_introduced: "Yin et al. *Science* 2017; Yang et al. *Cancer Cell* 2014; Li et al. *Genome Biol.* 2018"
date_updated: 2026-05-27
related_concepts:
  - variably-methylated-regions-vmr
  - spatial-dmt-method
  - non-cpg-methylation-postnatal-brain
---

## Definition

A positive methylation–expression coupling is a gene whose expression rises with — rather than falls with — the methylation level of a nearby variably methylated region (VMR). Although the textbook narrative pairs DNA methylation at regulatory elements with gene silencing, a substantial minority of loci show the opposite sign: methylation up, expression up. Spatial-DMT reveals dozens of such loci across mouse embryonic and brain tissue.

## Intuition

The "methylation = silencing" rule is true on average at promoter CpG islands. But three molecular contexts routinely produce the opposite pattern:

1. **TFs that prefer methylated motifs** — a subset of human TFs (Yin 2017) actually bind their motif *better* when CpG within it is methylated.
2. **Gene-body methylation** — methylation along expressed gene bodies often correlates positively with transcription rate; loss of gene-body methylation can silence the gene (Yang 2014).
3. **Polycomb-target hypomethylation** — Polycomb-marked promoters tend to be hypomethylated *and* repressed; loss of PRC2 leads to coupled gain of methylation and (sometimes) gain of expression (Li 2018).

Spatial-DMT operationalises this by listing genes whose nearby VMR methylation correlates positively with expression across pixels — without prejudging the mechanism.

## Formal notation

- Per-gene Pearson correlation r between VMR methylation and gene expression across pixels.
- Sign of r: negative (canonical repression) or positive (this concept).
- Adjusted p-value via Benjamini–Hochberg; significance threshold typically FDR < 0.05.

## Variants

- **Enhancer-resident positive coupling** (Yin 2017 mechanism).
- **Gene-body positive coupling** (Yang 2014 mechanism).
- **Polycomb-target positive coupling** (Li 2018 mechanism).

## Comparison

- vs **canonical negative coupling**: same statistical framework, opposite sign of r.
- vs **mCG-only or mCA-only coupling** (see [[concepts/non-cpg-methylation-postnatal-brain]]): in postnatal brain, gene-body mCA correlates positively with expression for some genes (e.g., Ank3 in [[papers/spatial-joint-profiling-dna-methylome-transcriptome]]).

## When to use

- Avoiding the false negative of "this gene is methylated, therefore it must be silenced".
- Identifying candidate methylation-binding-preferring TF targets in tissue.
- Annotating gene-body vs promoter methylation regimes in spatial methylome data.

## Known limitations

- Mechanism cannot be inferred from correlation alone — requires orthogonal data (ChIP-seq, knockouts).
- Most pipelines visualise only the canonical (negative) coupling and discard positive correlations as artefacts.

## Open problems

- Genome-wide rules for predicting which VMR–gene pairs will couple positively vs negatively from sequence + chromatin features.
- TF-resolved attribution: which positive couplings are driven by which methylation-preferring TFs?

## Key papers

- [[papers/spatial-joint-profiling-dna-methylome-transcriptome]] — Lee et al. *Nature* 2025; identifies Ank3, Atp11c, Cyfip2, Lmln, Khdrbs2 as genes with positive VMR-methylation–expression coupling in E11 mouse embryo (e.g., Ank3 has both high methylation and high expression in the brain region).

## My understanding

This concept matters because most methylome interpretation in the literature is implicitly conditioned on "methylation up ⇒ expression down" — which is a half-truth. Spatial-DMT routinely surfaces strong positive couplings in tissue, and any thesis-level interpretation of regional hypomethylation as derepression should be checked against the local sign of r. The cleanest test case in this paper is Ank3: high methylation, high expression, in the brain region — a clear violation of the canonical rule that would have been obscured in any methylome-only or transcriptome-only assay.
