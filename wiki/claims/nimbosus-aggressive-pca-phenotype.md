---
title: "Hypoxia + IDC-CA + PTEN-loss define a constellation 'nimbosus' associated with extreme PCa aggression"
slug: nimbosus-aggressive-pca-phenotype
status: supported
confidence: 0.85
tags:
  - prostate-cancer
  - nimbosus
  - hypoxia
  - PTEN
  - IDC-CA
  - aggressive-phenotype
  - prognostic
  - HR
domain: "oncology / cancer-genomics / prostate-cancer"
source_papers:
  - molecular-landmarks-tumor-hypoxia-across-cancer
evidence:
  - source: molecular-landmarks-tumor-hypoxia-across-cancer
    type: supports
    strength: strong
    detail: "Subjects with all three features (high hypoxia + IDC-CA-positive + PTEN allelic loss) versus all others: hazard ratio 11.10 (95% CI 3.02–47.27, P=3.15×10⁻⁵, Fisher's exact for the joint enrichment; HR from Wald test for survival). Quote (p.317): 'a constellation of co-occurring molecular features (nimbosus) are associated with aggressive disease, including hypoxia, mutant TP53, allelic loss of PTEN, chromothripsis and shorter telomeres.' Polyclonal hypoxic PCa enriched for IDC-CA (OR=3.27, P=0.024) and PTEN allelic loss (OR=3.41, P=6.15×10⁻³)."
conditions: "Localized prostate cancer with WGS, hypoxia measurement (mRNA Buffa or Ragnum), and pathologist-assessed IDC-CA. Validated in CPC-GENE and TCGA cohorts."
date_proposed: 2026-05-06
date_updated: 2026-05-06
---

## Statement

The "nimbosus" phenotype — a recurrent constellation of hypoxia + IDC-CA + PTEN allelic loss + mutant TP53 + chromothripsis + telomere shortening — defines an extreme-risk subgroup in localized prostate cancer. Subjects with the three most easily measured pillars (hypoxia + IDC-CA + PTEN deletion) have hazard ratio 11.10 (95% CI 3.02–47.27, P=3.15×10⁻⁵) for poor 5-year biochemical relapse-free outcome. The framework reframes PCa aggression from an additive list of risk factors to a *coherent molecular state* shaped by hypoxic selective pressure.

## Evidence summary

- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — primary evidence: HR=11.10 in multivariable model; OR=3.27 (IDC-CA in hypoxic polyclonal); OR=3.41 (PTEN loss in hypoxic polyclonal).
- Chua, van der Kwast, Bristow 2017 *Eur Urol* — original IDC-CA grouping prior to Bhandari extending it to molecular constellation.

## Conditions and scope

- Localized PCa cohorts with WGS + hypoxia + IDC-CA pathology.
- Empirically defined; not yet prospectively trial-validated.
- IDC-CA call quality dependent on pathologist training.

## Counter-evidence

- Direct causal proof requires longitudinal patient-derived models.
- Whether all six pillars are jointly necessary (vs just hypoxia + PTEN + IDC-CA) for the extreme HR is not separately tested.

## Linked ideas

(none yet)

## Open questions

- Is nimbosus a specific evolutionary trajectory (hypoxia → selection → PTEN loss + TP53 mutation → IDC-CA architecture) or coincident parallel features?
- Do hypoxia-targeting agents (evofosfamide) prevent or reverse nimbosus emergence?
- Does the immune microenvironment of nimbosus tumors share features with hypoxic-MAC infiltration ([[papers/nf-kb-tet2-promote-macrophage-reprogramming]])?
