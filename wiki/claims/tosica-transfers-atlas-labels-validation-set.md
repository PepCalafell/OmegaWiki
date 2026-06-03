---
title: "TOSICA transfers core-atlas cell labels to an independent validation set with 0.94 mean probability"
slug: "tosica-transfers-atlas-labels-validation-set"
status: supported
confidence: 0.8
tags: [annotation,transformer,validation,methodological,quantitative]
domain: methods
source_papers:
  - pan-cancer-tumor-classification-holistic-tumor
evidence:
  - source: pan-cancer-tumor-classification-holistic-tumor
    type: supports
    strength: strong
    detail: "Applying TOSICA with the core atlas as reference to 39 validation datasets (2,171,806 cells, 452 patients) gave an averaged prediction probability of 0.94, including for unseen BLCA and SARC."
conditions: "Probability reflects reference coverage; truly novel states would not be captured."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

The transformer-based TOSICA method annotated the validation set (39 datasets, 16 cancer types, 2,171,806 cells from 672 samples of 452 patients) using the core atlas as reference, achieving an averaged prediction probability of 0.94, with high confidence even for BLCA and SARC absent from the core, and reproduced reference transcriptional profiles.

## Evidence summary

Reference-mapping with probability scoring. (p.8) Quote: "an averaged prediction probability of 0.94 was achieved".

## Conditions and scope

Probability reflects reference coverage; truly novel states would not be captured.

## Counter-evidence

None recorded at ingest.

## Linked ideas

None yet.

## Open questions

How does TOSICA behave for cell states genuinely absent from the reference atlas?
