---
title: "Within RNA cluster R3 of E11 embryo, DNAm-defined subclusters D0 and D4 separate cells with similar transcription but distinct hypomethylation TF motifs (D0: PITX1/AP2/EBF1 facial; D4: HOXA/GATA cardiac)"
slug: epigenetic-subclustering-d0-d4-within-rna-cluster-r3-distinct-tf-motifs
status: supported
confidence: 0.8
tags: [epigenetic-priming, subclustering, TF-motif, embryogenesis, primed-state]
domain: epigenetics / developmental biology
source_papers:
  - spatial-joint-profiling-dna-methylome-transcriptome
evidence:
  - source: spatial-joint-profiling-dna-methylome-transcriptome
    type: supports
    strength: moderate
    detail: "Quote (p.8): 'Despite originating from the same RNA-defined clusters (R3), DNA methylation-defined cluster 0 (D0) and 4 (D4) cells had distinct subpopulations when stratified by their VMRs. Motif enrichment analysis of low-methylation sites in D0 and D4 identified regulatory elements associated with facial and cardiac morphogenesis (Fig. 5f), whereas corresponding gene-expression changes were limited (Fig. 5g). This may reflect epigenetically primed subpopulations that share similar transcriptional states'."
conditions: "E11 mouse embryo, 50 μm; subset of RNA cluster R3."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

Pixels indistinguishable by RNA-defined cluster (R3) can be separated by DNA-methylation-defined subclusters (D0 vs D4) into populations with distinct lineage-specific TF-motif enrichments at hypomethylated regions (D0: PITX1/AP2/EBF1 — facial morphogenesis; D4: HOXA/GATA — cardiac morphogenesis), with only limited gene-expression divergence — interpretable as epigenetically primed subpopulations sharing a transcriptional state.

## Evidence summary

Reported in [[papers/spatial-joint-profiling-dna-methylome-transcriptome]], Fig. 5f–g. Motif enrichment via [[foundations/homer-motif-enrichment-analysis]] one-sided hypergeometric test with Benjamini–Hochberg adjustment.

## Conditions and scope

E11 mouse embryo, single RNA-cluster sub-stratification (R3).

## Counter-evidence

Limited transcriptional divergence could also reflect insufficient depth / sensitivity in spatial RNA-seq.

## Linked ideas

## Open questions

- Whether D0 vs D4 cells later diverge transcriptionally (E13 or postnatal) and become committed to facial vs cardiac fates.
- Genome-wide scan for further epigenetic-priming subclusters across other RNA clusters.
