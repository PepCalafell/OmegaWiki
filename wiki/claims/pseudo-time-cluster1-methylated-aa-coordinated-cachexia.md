---
title: "Pseudo-time VSClust analysis identifies a dominant late-increase cluster (#1, 151 metabolites) enriched in methylated amino acids and coordinated across host tissues in cachexia"
slug: pseudo-time-cluster1-methylated-aa-coordinated-cachexia
status: supported
confidence: 0.85
tags: [VSClust, pseudo-time, sarcosine, methylated-amino-acids, cachexia, cluster1]
domain: cachexia / metabolomics
source_papers:
  - multi-omics-profiling-cachexia-targeted-tissues
evidence:
  - source: multi-omics-profiling-cachexia-targeted-tissues
    type: supports
    strength: strong
    detail: "VSClust clustering of metabolite trajectories across Ctrl → Pre-cax → Cax identifies 8 clusters; Cluster #1 (late increase, 151 metabolites) defined by methylated amino acids (sarcosine, trimethyllysine) and amino-acid derivatives (aminoadipic acid, ureidopropionic acid). All host tissues contribute similarly; tumour has a distinct profile."
conditions: "C26 model; n = 4 per group; metabolites pseudo-time-ordered as Ctrl → Pre-cax → Cax (Non-cax substituting for Ctrl in tumour)."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

Pseudo-time clustering (VSClust) of metabolite trajectories across cachexia stages identifies eight characteristic profiles; the dominant Cluster #1 (151 metabolites, late increase to Cax) is enriched for methylated amino acids and amino-acid derivatives and is coordinately contributed to by all host tissues — the signature feature of the tissue-overarching response.

## Evidence summary

Fig. 2 a-c: "the most prominent cluster #1 (late increase in Cax) was defined by increased levels of several methylated amino acids (for example, sarcosine/methylglycine and trimethyllysine) and derivatives of amino acid metabolism... all host tissues contributed to a similar degree to the different clusters, highlighting the coordinated tissue response to cachexia, whereas the tumour seemed to have a more distinct profile."

## Conditions and scope

VSClust on log-transformed imputed scaled MS data; 8 clusters chosen; Sankey-style attribution to tissue and metabolite class.

## Counter-evidence

Within paper, tumour metabolomes deviate from host-tissue clusters — coordination is host-tissue specific.

## Linked ideas

## Open questions

- Whether equivalent pseudo-time clustering in patient longitudinal sampling reproduces the methylated-amino-acid signature.
