---
title: "In P21 mouse brain, mCG and mCA regulate gene expression in a gene-specific manner: Prox1/Bcl11b correlate with both; Ntrk3/Satb1 only with mCG; Cux1 (CA1/2) only with mCA"
slug: mcg-mca-gene-specific-regulation-p21-brain-prox1-bcl11b-ntrk3-satb1-cux1
status: supported
confidence: 0.9
tags: [mCG, mCA, mCH, postnatal-brain, gene-specific-regulation, Prox1, Bcl11b, Cux1]
domain: epigenetics / neuroscience / spatial omics
source_papers:
  - spatial-joint-profiling-dna-methylome-transcriptome
evidence:
  - source: spatial-joint-profiling-dna-methylome-transcriptome
    type: supports
    strength: strong
    detail: "Quote (p.6): 'Prox1 and Bcl11b expression was significantly associated with both mCG and mCA (Fig. 4c,f and Extended Data Fig. 10c)... Ntrk3, a receptor tyrosine kinase crucial for nervous system function, was highly expressed in the hippocampal CA1/2 and DG regions, correlating primarily with mCG levels but not with mCA (Fig. 4d,g). Similarly, Satb1 expression in the cortex was strongly correlated with mCG but not with mCA levels (Extended Data Fig. 10b). The silencing of Cux1... in the CA1/2 region, Cux1 expression showed a negative correlation only with CA hypermethylation and seemed independent of mCG levels (Fig. 4e,h)'."
conditions: "P21 mouse brain, 20 μm pixel size; DG, CA1, CA2, CA3 and cortex regions."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

In P21 mouse brain, the regulatory partitioning of mCG vs non-CpG (mCA) methylation is gene-specific. Prox1 (DG) and Bcl11b (CA1/2) couple to both modalities; Ntrk3 (hippocampus) and Satb1 (cortex) couple only to mCG; Cux1 in CA1/2 couples only to mCA. Both modalities are predominantly repressive across the queried gene set.

## Evidence summary

Reported in [[papers/spatial-joint-profiling-dna-methylome-transcriptome]], Fig. 4c–h. Per-pixel log-transformed fold-change correlations between methylation and gene expression.

## Conditions and scope

P21 mouse brain; specific to a limited gene set; correlative, not perturbational.

## Counter-evidence

Modality-specific coupling could partially reflect coverage / dynamic-range differences between mCG and mCA assays.

## Linked ideas

## Open questions

- Genome-wide rules predicting mCG-only vs mCA-only vs both regulatory regimes per gene.
- Whether the modality-specific coupling holds in human cortex / hippocampus.
