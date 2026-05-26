---
title: "Novae recovers similar spatial-domain distributions across lymphoid tissues (tonsil and lymph node) and across breast/lung cancers"
slug: novae-recovers-similar-spatial-domains-tonsil-lymph-node
status: supported
confidence: 0.7
tags:
  - spatial-transcriptomics
  - cross-tissue
  - lymphoid
  - correlational
domain: biology
source_papers:
  - novae-graph-based-foundation-model-spatial
evidence:
  - source: novae-graph-based-foundation-model-spatial
    type: supports
    strength: medium
    detail: "Fig. 2a heatmap: tonsil and lymph node slides cluster together at the dendrogram level; some shared domains also appear in breast and lung (e.g., cancer-related domains shared between breast and lung tumours), supporting cross-tissue conservation of certain spatial niches."
conditions: "Heatmap-level / dendrogram-level observation; not a formal statistical test of cross-tissue niche conservation."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Across the 18-tissue training corpus, spatial domains identified by Novae cluster lymphoid tissues (tonsil, lymph node) together and show shared cancer-related domains across distinct tumour tissues (e.g., breast and lung), indicating biology-driven rather than purely tissue-driven prototype use.

## Evidence summary

Fig. 2a (human-tissue heatmap with dashed lines marking tonsil–lymph node similarity); Fig. 2c (mouse-tissue heatmap with brain inter-slide similarity).

## Conditions and scope

Qualitative dendrogram analysis; no quantitative similarity score reported across tissue pairs.

## Counter-evidence

Uterine slides cluster as outliers; whole-mouse sample uses prototypes not shared with other tissues.

## Linked ideas

— none yet.

## Open questions

- Whether shared "cancer-related" domains correspond to specific known TME states (e.g., hypoxic niche, TLS).
