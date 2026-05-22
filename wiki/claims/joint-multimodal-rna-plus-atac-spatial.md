---
title: "Joint multimodal RNA + ATAC spatial clustering recapitulates brain anatomy better than single-modality"
slug: joint-multimodal-rna-plus-atac-spatial
status: supported
confidence: 0.75
tags:
  - multimodal
  - spatial-transcriptomics
  - spatial-atac
  - methodological
domain: methods
source_papers:
  - cellcharter-reveals-spatial-cell-niches-associated
evidence:
  - source: cellcharter-reveals-spatial-cell-niches-associated
    type: supports
    strength: moderate
    detail: "Fig. 2c, Extended Data Fig. 2d: on Zhang et al. 2023 spatial epigenome-transcriptome multiome mouse-brain data, CellCharter applied to RNA + ATAC joint VAE embeddings recovers spatial clusters matching the Allen mouse-brain reference better than using RNA or ATAC alone. Ten spatial clusters identified."
conditions: "Single sample / single multiome dataset; clusters scored qualitatively against the Allen Brain Atlas reference."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

Concatenating embeddings from data-type-appropriate VAEs (RNA + ATAC) and clustering with CellCharter recovers brain anatomy better than clustering either modality alone.

## Evidence summary

Fig. 2c: representative cluster maps for mouse brain (RNA-only vs ATAC-only vs RNA+ATAC); arrows mark clusters concurrently retrievable only with the joint embedding.

## Conditions and scope

Demonstrated on a single mouse-brain multiome sample (Zhang et al. 2023). Quantitative ARI vs ground-truth atlas not reported.

## Open questions

- Does the multimodal gain hold for tumour multiome datasets?
