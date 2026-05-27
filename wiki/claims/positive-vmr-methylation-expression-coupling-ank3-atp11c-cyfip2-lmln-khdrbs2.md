---
title: "A subset of genes (Ank3, Atp11c, Cyfip2, Lmln, Khdrbs2) shows positive correlation between gene expression and DNA methylation at nearby VMRs in E11 mouse embryo"
slug: positive-vmr-methylation-expression-coupling-ank3-atp11c-cyfip2-lmln-khdrbs2
status: supported
confidence: 0.9
tags: [VMR, positive-coupling, DNA-methylation, gene-body, non-canonical-regulation]
domain: epigenetics / spatial omics
source_papers:
  - spatial-joint-profiling-dna-methylome-transcriptome
evidence:
  - source: spatial-joint-profiling-dna-methylome-transcriptome
    type: supports
    strength: strong
    detail: "Quote (p.4): 'we also identified genes, for example, Ank3, Atp11c, Cyfip2, Lmln and Khdrbs2, for which expression is positively correlated with the methylation levels of the associated VMRs (Fig. 2d). For instance, Ank3... had high levels of expression and DNA methylation in the brain region (Fig. 2c).' Two-sided Pearson correlation, Benjamini–Hochberg adjusted p-values."
conditions: "E11 mouse embryo; specific to gene–VMR pairs identified by per-pixel correlation."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

A non-trivial subset of genes (Ank3, Atp11c, Cyfip2, Lmln, Khdrbs2) shows positive correlation between expression and nearby VMR methylation in E11 mouse embryo — violating the canonical "methylation = silencing" rule and supporting the broader concept of positive methylation–expression coupling ([[concepts/methylation-positive-coupling-gene-expression]]).

## Evidence summary

Reported in [[papers/spatial-joint-profiling-dna-methylome-transcriptome]], Fig. 2c–d. Per-pixel two-sided Pearson correlation with BH adjustment.

## Conditions and scope

E11 mouse embryo; gene-set is illustrative, not exhaustive; mechanism (enhancer, gene-body, Polycomb target) not resolved by the paper.

## Counter-evidence

The majority of VMR–gene pairs show canonical negative coupling.

## Linked ideas

## Open questions

- Which mechanism (TF preference for methylated motifs, gene-body methylation, Polycomb derepression) drives each positive-coupling gene?
- Are positive-coupling genes enriched for any chromatin / functional category?
