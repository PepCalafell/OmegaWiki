---
title: "HOMER — motif enrichment analysis"
slug: homer-motif-enrichment-analysis
domain: "computational-biology / methods"
status: mainstream
aliases:
  - "HOMER"
  - "Hypergeometric Optimization of Motif EnRichment"
  - "findMotifsGenome.pl"
  - "de novo motif discovery"
  - "HOMER motif analysis"
  - "TF binding motif enrichment"
  - "motif analysis HOMER"
first_introduced: "Heinz et al. 2010 *Molecular Cell*"
date_updated: 2026-05-05
source_url: "http://homer.ucsd.edu/homer/"
---

## Definition

HOMER is a software suite for motif discovery and enrichment analysis from ChIP-seq, ATAC-seq, and other genomic interval datasets. It computes both *known motif* enrichment (against a curated library of vertebrate TF motifs) and *de novo motif* discovery using a hypergeometric optimization framework. Motifs are reported with fold-enrichment, P-value, and percent target/background sequences containing the motif.

## Intuition

HOMER is the standard "what TFs are likely binding these regions?" tool for ChIP-seq peak sets, differentially methylated regions, ATAC peaks, etc. Inputs are BED files; outputs are HTML reports of enriched motifs.

## Formal notation

- Input: peak/region BED + genome reference + background regions (random-genome or matched)
- Output: known-motif enrichment table + de novo motifs (PWMs) + best-match TFs

## Key variants

- findMotifs.pl — for promoter/sequence sets
- findMotifsGenome.pl — for ChIP-seq style genomic regions
- annotatePeaks.pl — for peak-feature annotation

## Known limitations

- Motif library bias toward well-studied TFs.
- Background region choice strongly affects enrichment P-values.
- De novo motifs often map to multiple similar TFs (paralog ambiguity).

## Open problems

- Cell-type-specific motif activity vs raw enrichment.
- Disentangling cobinding TFs from primary motif drivers.

## Relevance to active research

[[papers/nf-kb-tet2-promote-macrophage-reprogramming]] uses HOMER on DMP clusters C1, C2, C3 (revealing AP-1, NF-κB, RUNX/ETS motif enrichments respectively) and on HIF1α/p65 ChIP-seq peak sets (revealing HIF, NF-κB, AP-1, IRF, ETS motifs in cobound peaks). The C2-cluster NF-κB motif enrichment is one of the load-bearing observations of the paper.
