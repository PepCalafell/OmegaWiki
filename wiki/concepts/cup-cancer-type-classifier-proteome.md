---
title: "Proteome-based cancer-type classifier for cancers of unknown primary"
aliases:
  - CUP classifier
  - cancer of unknown primary classifier
  - tissue of origin classifier proteome
  - DIA-MS cancer-type classifier
  - multi-cancer protein classifier
  - 75-protein classifier
  - TPCPA classifier
  - proteome tissue-of-origin model
  - protein-based primary tumour identifier
  - metastasis-of-unknown-primary classifier
tags: [cup, classifier, machine-learning, dia-ms, metastasis]
maturity: emerging
key_papers:
  - pan-cancer-proteome-atlas-mass-spectrometry
first_introduced: "Knol et al. 2025"
date_updated: 2026-05-25
related_concepts: []
---

## Definition
A 75-protein machine-learning classifier trained on TPCPA (top 25 features per cancer type, 17 solid cancers) that predicts cancer type from bulk DIA-MS proteome of a tumour sample, intended for use in cancers of unknown primary (CUP).

## Intuition
Cancer type can be inferred from a small set of differentially expressed proteins; using single-shot DIA-MS, this inference is portable across cohorts and laboratories. For CUP — where the primary site is clinically inscrutable — a small protein panel can route patients to tumour-type-appropriate therapy.

## Formal notation
- Top 25 differentially abundant proteins per cancer type (17 solid types) → 75 unique features after deduplication
- Multi-class classification with feature-score thresholding (darkred ≥ 0.005)

## Variants
- Primary-tumour classification (CPTAC renal AUC 0.998, DIA breast AUC 0.992)
- Metastatic-tumour classification (28 metastatic ovarian AUC 1.0; 32 metastatic CRC AUC 0.98)

## Comparison
- vs **transcriptomic CUP classifiers (e.g., CancerTYPE ID)**: protein-based; complementary modality.
- vs **methylation-based classifiers (EPICUP)**: different signal layer, possibly orthogonal.

## When to use
- Cancers of unknown primary where biopsy is amenable to MS analysis.
- Confirmation of suspected primary tumour origin from a metastatic deposit.

## Known limitations
- 17 solid cancer types only.
- Mild overfitting potential — feature selection used all samples including the test set.
- No held-out non-DIA proteomes for cross-platform validation.

## Open problems
- Cross-platform generalisation (TMT, DDA).
- Clinical-grade validation with prospective CUP cohorts.

## Key papers
- [[papers/pan-cancer-proteome-atlas-mass-spectrometry]]

## My understanding
The most clinically deployable output of TPCPA. The metastatic-cohort AUCs are striking, but the small N (~30) and partial cohort independence demand prospective validation before this is more than a proof-of-concept.
