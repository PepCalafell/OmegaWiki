---
title: "Partially Methylated Domains (PMDs) as a spatial mitotic-history clock"
aliases:
  - "PMD"
  - "PMDs"
  - "partially methylated domain"
  - "PMD mitotic clock"
tags:
  - DNA-methylation
  - mitotic-history
  - PMD
  - cell-cycle
  - epigenetics
maturity: stable
key_papers:
  - spatial-joint-profiling-dna-methylome-transcriptome
first_introduced: "Lister et al. *Nature* 2009; mitotic-clock reformulation Zhou et al. 2018"
date_updated: 2026-05-27
related_concepts:
  - spatial-dmt-method
---

## Definition

Partially Methylated Domains are megabase-scale genomic regions whose average CpG methylation drifts downward with each round of DNA replication because DNMT1 maintenance is locally inefficient. Their methylation level therefore encodes the integrated mitotic history of the cell: heavily divided cells (cancer, neural progenitors) have low PMD methylation; quiescent / post-mitotic cells (mature neurons) retain high PMD methylation.

## Intuition

DNMT1 maintenance ([[foundations/dnmt1-maintenance-methyltransferase]]) is imperfect at PMDs; every round of replication loses a small fraction of CpG methylation that is never re-set. So PMD methylation = "how many times has this cell divided since its last methylome reset?" — a passive mitotic clock encoded directly in the genome. Spatial-DMT reads it out per pixel.

## Formal notation

- PMD location: ~30% of the genome, mostly late-replicating B-compartment.
- Methylation decay per division: ~1–2% per replication cycle.
- Resulting gradient: low in actively dividing tissue compartments, high in differentiated post-mitotic compartments.

## Variants

- **Cancer PMD hypomethylation**: tumour PMDs are heavily hypomethylated, used as a tumor-clonality / proliferation surrogate.
- **Aging PMD drift**: PMD methylation declines with chronological age, basis of several epigenetic age clocks.
- **Spatial PMD mapping**: per-pixel PMD methylation gradients across tissue regions, as introduced in [[papers/spatial-joint-profiling-dna-methylome-transcriptome]] for E11/E13 embryos and P21 brain.

## Comparison

- vs **CpG-island methylation**: CGIs are functional regulatory units; PMDs are passive mitotic readouts. Different biology, different interpretation.
- vs **Ki67 / MKI67 staining**: protein-level cycling marker — instantaneous; PMDs are integrated mitotic history.
- vs **Replication-coupled hemimethylation tracking** (Repli-MeDIP): same biology, complementary readout.

## When to use

- Spatial inference of proliferative vs post-mitotic tissue regions without an additional stain.
- Cross-region comparison of cell turnover (e.g., dentate gyrus vs cortex; embryonic heart vs forebrain).
- Tumor proliferation index from bulk or spatial methylome alone.

## Known limitations

- Low resolution (megabase scale) — cannot localise individual genes.
- Confounded by quiescence-induced PMD remethylation (rare).
- Requires whole-genome coverage; depleted in array / RRBS data.

## Open problems

- Quantitative model linking single-pixel PMD methylation to absolute division count.
- Joint PMD + transcription readout to disentangle proliferation rate from differentiation state.

## Key papers

- [[papers/spatial-joint-profiling-dna-methylome-transcriptome]] — Lee et al. *Nature* 2025; first spatial PMD maps: low PMD methylation in embryonic heart (active cardiogenesis) and P21 dentate gyrus (adult neurogenesis); high PMD methylation in P21 cortex (post-mitotic neurons); gradient from mantle (high) to ventricular (low) zone in the developing brain.

## My understanding

PMDs convert a methylome scan into a passive proliferation map — a free additional readout from any methylome assay. Spatial-DMT makes this powerful because the gradients are visible at tissue level: in the postnatal brain, the PMD map *alone* recapitulates the proliferative-to-post-mitotic anatomy that conventionally requires Ki67 IHC. As a thesis-relevant lens, this concept is the cleanest example of a methylome-only spatial cell-state readout that does not depend on transcription.
