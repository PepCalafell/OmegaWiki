---
title: "DoRothEA — TF regulon activity analysis"
slug: dorothea-tf-regulon-analysis
domain: "computational-biology / methods"
status: mainstream
aliases:
  - "DoRothEA"
  - "Discriminant Regulon Expression Analysis"
  - "TF regulon scoring"
  - "regulon activity inference"
  - "TF activity from gene expression"
  - "transcription factor activity inference (DoRothEA)"
  - "VIPER + DoRothEA workflow"
first_introduced: "Garcia-Alonso et al. 2019 *Genome Research*"
date_updated: 2026-05-05
source_url: "https://saezlab.github.io/dorothea/"
---

## Definition

DoRothEA is a curated database of transcription-factor → target-gene regulons derived from ChIP-seq, motif analysis, gene-expression co-regulation, and literature curation. Each regulon is assigned a confidence level (A highest, E lowest). When combined with an enrichment method (typically VIPER or fGSEA), DoRothEA infers TF *activity* from bulk or single-cell RNA-seq by scoring how strongly each TF's downstream targets are differentially expressed.

## Intuition

Instead of measuring TF expression directly (which often correlates poorly with activity), DoRothEA reads out TFs *by their footprint* on the transcriptome. If most of a TF's known targets are up-regulated, the TF is inferred to be active.

## Formal notation

- Input: ranked DEG list or t-statistic vector
- Database: ~1500 human TFs, A–E confidence
- Scoring: VIPER or msVIPER (Z-scaled NES across regulon target sets)
- Output: per-TF NES + FDR

## Key variants

- DoRothEA (human, mouse) — original CHEA/TRRUST/literature-merged
- CollecTRI — successor curated TF-target collection by the Saez-Rodriguez lab
- SCENIC — single-cell-specific TF activity inference using motif-based regulons + co-expression

## Known limitations

- Regulons are aggregated across cell types; cell-type-specific regulatory wiring is lost.
- Direction of regulation (activator vs repressor) is sometimes mis-annotated.
- Confidence levels D and E are noisy and often filtered out.

## Open problems

- Tissue-specific regulons remain incomplete.
- Reconciling DoRothEA inferences with direct ChIP-seq evidence is non-trivial.

## Relevance to active research

[[papers/nf-kb-tet2-promote-macrophage-reprogramming]] uses DoRothEA on bulk RNA-seq comparisons to identify HIF1A as the dominant TF in iMAC21-vs-iMAC1 and STAT2/IRF1/RELA as dominant in mMAC21-vs-mMAC1. The RELA regulon NES rises from 3.8 (resting) to 5 (activated) under hypoxia, supporting NF-κB engagement.
