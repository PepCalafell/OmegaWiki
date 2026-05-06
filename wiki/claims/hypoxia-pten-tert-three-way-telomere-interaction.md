---
title: "Hypoxia × PTEN × TERT three-way interaction modulates telomere length in localized PCa"
slug: hypoxia-pten-tert-three-way-telomere-interaction
status: supported
confidence: 0.75
tags:
  - hypoxia
  - PTEN
  - TERT
  - telomere
  - prostate-cancer
  - interaction
  - HIF1A
domain: "oncology / cancer-genomics / prostate-cancer"
source_papers:
  - molecular-landmarks-tumor-hypoxia-across-cancer
evidence:
  - source: molecular-landmarks-tumor-hypoxia-across-cancer
    type: supports
    strength: moderate
    detail: "In a linear model on 333 TCGA + 215 CPC-GENE PRAD samples (telomere_length ~ hypoxia + PTEN_mRNA + TERT_mRNA + interactions), the three-way hypoxia × TERT × PTEN interaction is significant (Bonferroni-adjusted P=4.34×10⁻², linear model). Single-feature components also significant: hypoxia (P=2.17×10⁻³), TERT, PTEN. PTEN-TERT mRNA correlation negative: CPC-GENE ρ=−0.36, P=4.01×10⁻⁸; TCGA ρ=−0.15, P=7.21×10⁻³. Lowest PTEN observed in hypoxic + high-TERT tumors. Quote (p.314): 'a model incorporating hypoxia, PTEN and TERT mRNA abundance demonstrated a significant interaction between these features in modulating telomere length.'"
conditions: "Localized PCa cohorts with mRNA + telomere-length estimates (TelSeq from WGS)."
date_proposed: 2026-05-06
date_updated: 2026-05-06
---

## Statement

Hypoxia, PTEN mRNA abundance, and TERT mRNA abundance together modulate telomere length in localized prostate cancer in a non-additive manner — their three-way interaction is statistically significant (Bonferroni-adjusted P=4.34×10⁻², linear model on n=333 TCGA + 215 CPC-GENE samples). PTEN and TERT show a strong negative mRNA correlation (CPC-GENE ρ=−0.36, P=4.01×10⁻⁸); the lowest PTEN expression is observed in tumors that are simultaneously hypoxic and high-TERT. This positions telomere maintenance as a downstream readout of microenvironmental hypoxia + tumor-suppressor co-dysregulation rather than an independent hallmark.

## Evidence summary

- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — primary evidence: linear model on 548 PCa samples with three-way interaction term significant.
- Mechanistic priors: TERT is a HIF1A target (hypoxia → TERT induction); PTEN loss → AKT hyperactivation → indirect TERT regulation.
- TelSeq for telomere-length estimation from WGS.

## Conditions and scope

- Localized PCa with matched WGS + mRNA.
- Statistical interaction observed; mechanistic causation requires direct experimental test.
- TelSeq estimates telomere length with limited resolution.

## Counter-evidence

- Mechanism for the specific three-way interaction is not characterized.
- Bulk mRNA confounds malignant + stromal contributions.

## Linked ideas

(none yet)

## Open questions

- Mechanistic test: does inducing hypoxia + PTEN loss in vitro recapitulate the lowest-PTEN/high-TERT/short-telomere state?
- Whether targeting TERT (imetelstat) is selectively effective in hypoxic + PTEN-loss tumors
- Validation with single-cell or spatial methods to disentangle malignant vs stromal contributions
