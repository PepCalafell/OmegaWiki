---
title: "Novae is a graph-based foundation model trained on ~30M cells across 18 tissues and 3 imaging-based spatial-transcriptomics technologies"
slug: novae-trained-30m-cells-18-tissues-foundation-model
status: supported
confidence: 0.95
tags:
  - spatial-transcriptomics
  - foundation-model
  - methodological
domain: methods
source_papers:
  - novae-graph-based-foundation-model-spatial
evidence:
  - source: novae-graph-based-foundation-model-spatial
    type: supports
    strength: strong
    detail: "Trained on 78 slides representing nearly 30 million cells across 18 tissues (colon, breast, lung, liver, uterine, tonsil, prostate, whole mouse, ovarian, lymph node, skin, brain, mouse brain, mouse femur, pancreas, bone marrow, mouse colon, kidney) and three subcellular-resolution platforms (Xenium, MERSCOPE, CosMx). Weights distributed on Hugging Face Hub."
conditions: "Pretrained checkpoint on imaging-based spatial transcriptomics; NGS (Visium) not in current pretraining corpus."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Novae is the first large-scale graph-based foundation model for spatial transcriptomics, pretrained on ~30M cells from 78 slides spanning 18 tissues and three imaging-based subcellular spatial-transcriptomics technologies, and distributed openly via the Hugging Face Hub.

## Evidence summary

Abstract + Fig. 1a; ~30M cells, 18 tissues (Colon, Breast, Lung, Liver, Uterine, Tonsil, Prostate, Whole mouse, Ovarian, Lymph node, Skin, Brain, Mouse brain, Mouse femur, Pancreas, Bone marrow, Mouse colon, Kidney); platforms Xenium, MERSCOPE, CosMx.

## Conditions and scope

Imaging-based subcellular spatial transcriptomics only; NGS-based Visium and spatial proteomics are not in pretraining (proteomics is supported architecturally and demonstrated downstream).

## Counter-evidence

None; this is a direct dataset description.

## Linked ideas

— none yet.

## Open questions

- Whether expanding pretraining to Visium and proteomics modalities improves cross-modality transfer.
