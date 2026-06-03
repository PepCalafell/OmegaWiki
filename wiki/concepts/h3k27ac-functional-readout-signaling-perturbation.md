---
title: "H3K27ac as a high-resolution functional readout of signaling perturbation"
aliases:
  - "H3K27ac signaling readout"
  - "epigenomic readout of pathway perturbation"
tags:
  - H3K27ac
  - epigenomics
  - signaling
  - enhancers
  - readout
maturity: emerging
key_papers:
  - integrative-epigenome-based-strategy-unbiased-functional
first_introduced: "Gualdrini et al. 2024 *Molecular Systems Biology*"
date_updated: 2026-06-03
related_concepts:
  - epigenome-based-functional-profiling-kinase-inhibitors
  - polypharmacology-clinical-kinase-inhibitors
---

## Definition

The idea that genome-wide signal-induced H3K27ac at cis-regulatory elements is a richer, higher-resolution readout of intracellular signaling-pathway perturbation than transcriptomic profiling. Because thousands of enhancers/promoters (far more than genes) change acetylation in response to a stimulus, and because the "grammar" of CREs (TF binding motifs) is known, H3K27ac dynamics encode which TFs — and thus which upstream pathways — a perturbation affects.

## Intuition

There are many more regulatory elements than genes, their acetylation responds rapidly to signaling, and they are not confounded by RNA stability or post-transcriptional regulation. So an H3K27ac map separates similar perturbations more finely than a gene-expression map.

## Formal notation

- Granularity: ~16,500 LPS-regulated CREs vs a smaller number of differentially expressed genes.
- Direct head-to-head at 2 h LPS: H3K27ac-based CKI proximity gives sharper quintile separation and captures higher pairwise Jaccard overlaps than RNA-seq-based proximity.

## Variants

- Other dynamic marks (H3K4me1, enhancer eRNAs) as alternative activity readouts.
- ATAC-seq accessibility as a complementary chromatin readout.

## Comparison

Versus RNA-seq: more features, fewer confounders, better separation of related perturbations — though RNA-seq still captures the overall correlative/anti-correlative spectrum of effects.

## When to use

When high-resolution discrimination among related perturbations (e.g., compound series, similar genetic perturbations) in a dynamic signaling system is needed.

## Known limitations

- H3K27ac is a correlate of activity, not transcription itself.
- Still indirect with respect to the kinases/TFs being inhibited.

## Open problems

- Whether the resolution advantage generalizes across cell types and slower-kinetic systems.

## Key papers

- [[papers/integrative-epigenome-based-strategy-unbiased-functional]] — demonstrates H3K27ac > RNA-seq resolution for separating kinase inhibitors.

## My understanding

A useful general principle beyond drug profiling: enhancer acetylation is a denser, cleaner sensor of signaling state than the transcriptome, which dovetails with enhancer-centric models of macrophage activation.
