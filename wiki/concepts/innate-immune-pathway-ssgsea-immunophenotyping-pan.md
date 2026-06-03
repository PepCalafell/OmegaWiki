---
title: "ssGSEA immunophenotyping of innate sensing pathways (pan-cancer)"
aliases: []
tags: [innate-immunity, ssGSEA, pan-cancer, immunophenotyping, TCGA, PRR]
maturity: emerging
key_papers:
  - genomic-investigation-innate-sensing-pathways-tumor
first_introduced: "2024"
date_updated: 2026-06-03
related_concepts: [cgas-sting-pathway-canonical-noncanonical-outputs, pattern-recognition-receptors-macrophage]
---

## Definition

A framework that quantifies the activation of individual innate pattern-recognition-receptor (PRR) signaling cascades — cGAS, TLR, CLR, NOD/NLR, and RIG-I — from bulk tumor RNA-seq by running single-sample GSEA against a custom, manually curated gene-set ontology, yielding one activation score per pathway per tumor.

## Intuition

The innate immune system is hard to study in cancer because its PRR cascades are redundant and intertwined. Rather than tracking single receptors, this approach treats each cascade as a gene set and collapses its expression into a scalar "activation" score, so that thousands of TCGA tumors can be immunophenotyped along five innate axes and related to survival, immunogenicity, and microbiome features.

## Formal notation

For pathway *p* and sample *s*, score = ssGSEA enrichment of curated gene set *G_p* over the rank-ordered transcriptome of *s* (Barbie et al. single-sample extension; raw rank metric, weight 0.75, KS statistic with 1000 permutations). Gene sets *G_p* curated from KEGG/GO/STRING plus review literature, deduplicated and verified against hg19 annotation.

## Variants

Distinct from broad immune-deconvolution (CIBERSORTx, TIMER) that estimates cell fractions: this scores *pathway activation state* rather than *cell abundance*, and the two are complementary (only some immune populations track with the scores).

## When to use

When the question is "how active is a specific innate sensing cascade in this tumor?" across large bulk-RNA cohorts, and when downstream phenotypes (survival, mutation burden, microbiome) need a continuous per-pathway readout.

## Known limitations

Exploratory and correlational; scores reflect transcriptional proxies, not protein activity or post-translational signaling. Validation rests on a small number of stimulus datasets (LPS/TLR, RSV/RIG-I-NOD). Custom ontology choices influence scores.

## Open problems

Whether pathway scores capture activation versus mere receptor expression; how to disentangle PRR self-antigen sensing from microbial sensing; extension beyond the five curated cascades.

## Key papers

- [[genomic-investigation-innate-sensing-pathways-tumor]] — introduces the custom 5-pathway ssGSEA ontology and applies it across 8,554 TCGA tumors.

## My understanding

A pragmatic, reusable immunophenotyping handle for innate sensing in any bulk-RNA cohort. Its value is hypothesis generation (it surfaced the PHF–cGAS axis) rather than mechanistic proof.
