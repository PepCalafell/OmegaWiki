---
title: "Spatial cluster-specific gene expression is frequently associated with low DNA methylation at neighbouring VMRs (Runx2 craniofacial, Mapt brain, Trim55 heart)"
slug: vmr-hypomethylation-correlates-cluster-specific-expression
status: supported
confidence: 0.9
tags: [VMR, DNA-methylation, gene-expression, embryogenesis]
domain: epigenetics / spatial omics
source_papers:
  - spatial-joint-profiling-dna-methylome-transcriptome
evidence:
  - source: spatial-joint-profiling-dna-methylome-transcriptome
    type: supports
    strength: strong
    detail: "Quote (p.4): 'Spatial cluster-specific gene expression is frequently associated with low DNA methylation at the neighbouring VMRs, as exemplified by signature genes Runx2, Mapt, and Trim55, which mark the craniofacial regions (jaw and upper nasal), the brain and spinal cord, and the heart, respectively (Fig. 2c)'. GO enrichment of epigenetically regulated genes identifies the corresponding developmental processes (Extended Data Figs. 5b, 6d, 7d)."
conditions: "E11 mouse embryo; 50 μm pixel size; VMR window analysis."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

Across E11 embryo spatial clusters, tissue-specific marker genes (Runx2 for craniofacial, Mapt for brain/spinal cord, Trim55 for heart) show high expression coupled to low methylation at nearby VMRs — the canonical inverse coupling.

## Evidence summary

Reported in [[papers/spatial-joint-profiling-dna-methylome-transcriptome]], Fig. 2a–c. Extended Data Figs. 5b, 6d, 7d link cluster-level GO enrichment to anatomical developmental processes.

## Conditions and scope

E11 mouse embryo; specific to VMRs proximal to a queried gene; effect size varies by gene.

## Counter-evidence

A non-trivial minority of genes show the opposite (positive) coupling — see [[claims/positive-vmr-methylation-expression-coupling-ank3-atp11c-cyfip2-lmln-khdrbs2]].

## Linked ideas

## Open questions

- Quantitative fraction of VMR–gene pairs that follow canonical vs non-canonical coupling, genome-wide.
- Stability of the coupling across developmental stages.
