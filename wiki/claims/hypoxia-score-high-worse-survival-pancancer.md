---
title: "Hypoxia score-high tumours are associated with worse overall survival across cancer types"
slug: hypoxia-score-high-worse-survival-pancancer
status: supported
confidence: 0.85
tags:
  - hypoxia
  - prognosis
  - survival
  - pancancer
  - TCGA
domain: "oncology / clinical-genomics / hypoxia"
source_papers:
  - characterization-hypoxia-associated-molecular-features-aid
evidence:
  - source: characterization-hypoxia-associated-molecular-features-aid
    type: supports
    strength: strong
    detail: "Hypoxia score-high tumours were consistently associated with worse prognosis in univariate and multivariate Cox proportional hazards models across cancer types (n=3,495). Quote (p.434): 'hypoxia score-high tumours were consistently associated with worse prognosis across cancer types in univariate or multivariate survival analysis.' Examples: HNSC log-rank P=2.9×10⁻⁴; LUAD log-rank P=5.1×10⁻⁴; pan-cohort P=1.8×10⁻¹²."
conditions: "21 TCGA cancer types with ≥30 samples in both hypoxia score-high and score-low groups. Significance shown for a subset of cancer types (HNSC, LUAD, CESC, GBM, KIRP, LIHC, LGG, UCEC, SKCM)."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

Across multiple TCGA cancer types, patients whose tumours are classified hypoxia score-high have significantly worse overall survival than hypoxia score-low patients, after adjusting for clinical confounders. This establishes the prognostic relevance of the mRNA-based hypoxia classification.

## Evidence summary

- [[papers/characterization-hypoxia-associated-molecular-features-aid]] — Cox models (univariate + multivariate), Kaplan–Meier curves across cancer types.

## Conditions and scope

- Holds for the surveyed cancer types; not every individual cancer type reached significance.
- Based on bulk mRNA classification of TCGA tumours.

## Counter-evidence

- Prognostic strength varies by cancer type; some types show FDR>0.15.

## Linked ideas

(none yet)

## Open questions

- Does hypoxia status add prognostic value beyond established clinical/molecular markers in each cancer type?
