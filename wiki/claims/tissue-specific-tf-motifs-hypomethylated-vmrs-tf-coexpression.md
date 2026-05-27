---
title: "Tissue-specific TFs are expressed in spatial clusters whose hypomethylated VMRs are enriched for their binding motifs (Hand2/Tbx20/Meis1 heart W6; Ebf1/Pbx1 brain W2; Sox9/Ebf1/Zeb2 craniofacial W0)"
slug: tissue-specific-tf-motifs-hypomethylated-vmrs-tf-coexpression
status: supported
confidence: 0.85
tags: [TF-motif-enrichment, hypomethylated-VMR, embryogenesis, HOMER]
domain: epigenetics / spatial omics
source_papers:
  - spatial-joint-profiling-dna-methylome-transcriptome
evidence:
  - source: spatial-joint-profiling-dna-methylome-transcriptome
    type: supports
    strength: strong
    detail: "Quote (p.4): 'TFs associated with heart development, Hand2, Tbx20 and Meis1, were expressed in cluster W6, the corresponding hypomethylated VMRs of which were enriched in the binding motifs of these TFs (Fig. 2e, right). Similar sets of tissue-specific TFs are identified for other embryo structures, for example, Ebf1 and Pbx1 in the brain and spinal cord and Sox9, Ebf1 and Zeb2 in the craniofacial region.' One-sided hypergeometric test, HOMER motif enrichment."
conditions: "E11 mouse embryo, 50 μm pixel size. HOMER motif enrichment + per-cluster average TF expression."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

In E11 mouse embryo, hypomethylated VMRs of each spatial cluster are enriched for binding motifs of TFs that are themselves expressed in that cluster — supporting a TF-driven local-hypomethylation model. Heart cluster W6: Hand2, Tbx20, Meis1; brain/spinal cord cluster W2: Ebf1, Pbx1; craniofacial cluster W0: Sox9, Ebf1, Zeb2.

## Evidence summary

Reported in [[papers/spatial-joint-profiling-dna-methylome-transcriptome]], Fig. 2e. Uses [[foundations/homer-motif-enrichment-analysis]] one-sided hypergeometric test.

## Conditions and scope

Correlative association between TF expression and motif enrichment at hypomethylated regions; no perturbation experiments.

## Counter-evidence

Motif enrichment does not equal binding; TFs not assayed directly by ChIP.

## Linked ideas

## Open questions

- Direct ChIP-seq / CUT&Tag of these TFs in matched tissue to confirm binding.
- Causal test (TF KO) of the TF–hypomethylation link.
