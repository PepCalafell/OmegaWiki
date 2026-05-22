---
title: "TF community analysis of gene regulatory networks"
aliases:
  - "TF–TF association network"
  - "TF community"
  - "TF neighbour communities"
  - "Leiden TF community detection"
  - "TF regulatory community"
  - "TF–TF co-activity network"
  - "regulatee adjacency analysis"
  - "TF community pathway enrichment"
tags: [methods, gene-regulatory-network, transcription-factor, network-biology]
maturity: emerging
key_papers: [atlas-guided-discovery-transcription-factors-cell]
first_introduced: "2025"
date_updated: 2026-05-22
related_concepts: [taiji-tf-activity-pipeline]
---

## Definition

Method that builds a TF–TF association matrix from regulatee overlap (predicted TF-target genes), clusters TFs into communities (Leiden algorithm), and assigns each community a biological pathway via gene-set enrichment of its regulatees. Communities are compared across cell states to expose **context-specific rewiring** — same TFs, different partners, different pathways.

## Intuition

Most TFs operate as committees, not soloists. Two cell states may share a TF roster yet wire them into entirely different committees, each running a different transcriptional program. Pathway-annotated communities turn an unwieldy TF list into interpretable functional modules.

## When to use

When a static TF activity score does not explain functional divergence between similar states (TEXterm vs TRM): community analysis reveals which biological pathway each TF is steering in each state.

## Known limitations

Communities depend on the regulatee inference quality (motif + ATAC + expression) and the clustering algorithm; small-edge differences can move a TF between communities.

## Key papers

- [[atlas-guided-discovery-transcription-factors-cell]] — Chung et al. 2025: identifies five TRM and five TEXterm communities; TRM-c3 maps to TGFβ response and cell adhesion, TEXterm-c1 to proteasome catabolism.
