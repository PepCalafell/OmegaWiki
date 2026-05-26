---
title: "HT-SELEX (high-throughput systematic evolution of ligands by exponential enrichment)"
slug: ht-selex
domain: "biochemistry / TF binding / in vitro"
status: mainstream
aliases:
  - "HT-SELEX"
  - "HT SELEX"
  - "high-throughput SELEX"
  - "SELEX-seq"
  - "Jolma SELEX"
  - "multi-round TF–DNA selection"
  - "SELEX enrichment cycles"
first_introduced: "Jolma et al. *Genome Res* 2010 / *Cell* 2013"
date_updated: 2026-05-26
source_url: ""
---

## Definition

HT-SELEX is the high-throughput sequencing version of SELEX: a TF is incubated with a randomised DNA ligand library, bound DNA is captured (usually via tagged TF), amplified, and re-selected over multiple cycles (typically 4). Successive enrichment converges on high-affinity binding sequences; downstream PWM inference yields a binding motif. The Jolma 2013 catalogue covers hundreds of human TFs.

## Relevance to active research

[[papers/multiple-overlapping-binding-sites-determine-transcription]] uses HT-SELEX as a negative-control benchmark: HT-SELEX enrichment scores show substantially lower AUROC (regardless of cycle) than PADIT-seq for identifying lower-affinity TFBSs, because successive selection cycles bias toward high-affinity sequences and miss the lower-affinity sites that the overlapping-binding-sites model identifies as functionally important. The paper also re-analyses HT-SELEX cycle progression to confirm that sequences with more overlapping active k-mers are enriched in later rounds.
