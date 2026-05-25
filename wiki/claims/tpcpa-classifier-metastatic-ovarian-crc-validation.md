---
title: "TPCPA cancer-type classifier reaches AUC 1.0 on metastatic ovarian and AUC 0.98 on metastatic CRC samples"
slug: tpcpa-classifier-metastatic-ovarian-crc-validation
status: supported
confidence: 0.75
tags: [cup-classifier, metastatic-cancer, dia-ms, ovarian-cancer, colorectal-cancer]
domain: methods
source_papers:
  - pan-cancer-proteome-atlas-mass-spectrometry
evidence:
  - source: pan-cancer-proteome-atlas-mass-spectrometry
    type: supports
    strength: moderate
    detail: "Using the top 75 features, the classifier achieves AUC 1.0 on 28 metastatic ovarian cancer samples (ref 80) and AUC 0.98 on 32 metastatic colorectal cancer samples (unpublished Jimenez lab data), suggesting CUP applicability."
conditions: "Two cohorts only; small N; metastases of ovarian and CRC origin."
date_proposed: 2026-05-25
date_updated: 2026-05-25
---

## Statement
The TPCPA cancer-type classifier classifies metastatic ovarian samples with AUC 1.0 and metastatic CRC samples with AUC 0.98, evidencing that primary-tumor-trained protein features retain identity in metastatic deposits and supporting the cancer-of-unknown-primary (CUP) use case.

## Evidence summary
- Knol et al. 2025 Figure 6E.

## Conditions and scope
- Two metastatic cancer types only; N=28 and N=32.
- Independent acquisition workflows but the same TPCPA preprocessing pipeline.

## Counter-evidence
- The CRC test set comes from the corresponding-author lab (unpublished data), so cohort independence is partial.

## Linked ideas

## Open questions
- Does classifier performance degrade for metastases from cancer types with cross-tissue protein-marker overlap (e.g., upper GI)?
