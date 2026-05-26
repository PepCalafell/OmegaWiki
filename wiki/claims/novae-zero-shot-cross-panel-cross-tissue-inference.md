---
title: "Novae performs zero-shot spatial-domain inference across new tissues, gene panels, and imaging technologies"
slug: novae-zero-shot-cross-panel-cross-tissue-inference
status: supported
confidence: 0.85
tags:
  - spatial-transcriptomics
  - zero-shot
  - foundation-model
  - methodological
domain: methods
source_papers:
  - novae-graph-based-foundation-model-spatial
evidence:
  - source: novae-graph-based-foundation-model-spatial
    type: supports
    strength: strong
    detail: "On the breast benchmark (2 slides, 2 distinct panels) and colon benchmark (5 slides, 3 panels), zero-shot Novae matches or beats per-slide-trained STAGATE/GraphST/SpaceFlow/SEDR/Scanpy/NicheCompass on both FIDE (domain continuity) and JSD (cross-slide homogeneity)."
conditions: "Imaging-based spatial transcriptomics with overlap with Novae's training distribution (Xenium/MERSCOPE/CosMx, tissues represented in 18-tissue corpus)."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Zero-shot Novae — applied with no fine-tuning — produces competitive spatial-domain assignments on new slides spanning different gene panels and tissues, matching or exceeding methods trained directly on those slides.

## Evidence summary

Fig. 3b (breast benchmark) and Fig. 3d (colon benchmark): zero-shot Novae achieves higher FIDE and lower JSD than competitors across 7-, 10-, and 15-domain settings. Authors highlight this as a defining property of a true foundation model.

## Conditions and scope

In-distribution panels / tissues / platforms; zero-shot performance on out-of-distribution spatial proteomics or unseen tissues is partially supported (proteomics demonstrated but not benchmarked under zero-shot).

## Counter-evidence

The synthetic dataset benchmark excludes zero-shot Novae because the synthetic gene expression lacks biological meaning — model assumptions are violated when no biological priors hold.

## Linked ideas

— none yet.

## Open questions

- Out-of-distribution tissues / proteomics / NGS-based platforms.
