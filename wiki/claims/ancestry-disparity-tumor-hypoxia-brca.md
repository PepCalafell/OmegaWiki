---
title: "Tumor hypoxia in BRCA differs by self-reported ancestry — Caucasian < Asian/African"
slug: ancestry-disparity-tumor-hypoxia-brca
status: supported
confidence: 0.8
tags:
  - hypoxia
  - ancestry
  - BRCA
  - health-disparity
  - precision-medicine
  - evofosfamide
domain: "oncology / cancer-genomics / health-disparities"
source_papers:
  - molecular-landmarks-tumor-hypoxia-across-cancer
evidence:
  - source: molecular-landmarks-tumor-hypoxia-across-cancer
    type: supports
    strength: strong
    detail: "BRCA cohort (n=997 with ancestry data): median hypoxia score White=−7, Asian=11, Black or African American=13. Bonferroni-adjusted P=4.08×10⁻¹³ (Kruskal–Wallis test). Quote (p.309): 'Among breast tumors, for which the sample size was twice that of any other cancer type, we observed a strong association with subject-reported ancestry: tumors arising in subjects of Caucasian ancestry had less hypoxia than tumors in subjects with either Asian or African ancestry (Bonferroni-adjusted P=4.08×10⁻¹³).' Authors connect this to higher efficacy of evofosfamide in subjects of Asian descent in the phase-3 MAESTRO trial."
conditions: "BRCA-specific (sample size required for adequate power; non-BRCA tumor types in TCGA are underpowered for ancestry analyses)."
date_proposed: 2026-05-06
date_updated: 2026-05-06
---

## Statement

In TCGA breast cancer (n=997 with self-reported ancestry), median tumor hypoxia score differs significantly by ancestry: White=−7, Asian=11, Black or African American=13 (Bonferroni-adjusted P=4.08×10⁻¹³, Kruskal-Wallis). Tumors in subjects of Asian or African ancestry are *more* hypoxic than those in subjects of Caucasian ancestry. This ancestry-specific hypoxia signal is consistent within BRCA molecular subtypes (basal-like, HER2+, luminal). The authors connect the finding to the higher response rate of evofosfamide (a hypoxia-activated prodrug) in Asian-descent subjects in the phase-3 MAESTRO trial.

## Evidence summary

- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — primary evidence: BRCA n=997, Bonferroni P=4.08×10⁻¹³.
- Connection to MAESTRO post-hoc finding: hypothesis-generating.

## Conditions and scope

- BRCA-specific. Non-BRCA tumor types in TCGA are underpowered for ancestry analyses.
- Self-reported ancestry; coarse proxy for genetic ancestry.
- Cross-cohort replication pending.

## Counter-evidence

- Confounding by socioeconomic factors, healthcare access not ruled out.
- Sample-size dominance of European-ancestry subjects in TCGA may bias the comparison.

## Linked ideas

(none yet)

## Open questions

- Mechanistic basis: germline modifiers (HLA, DDR variants)? Lifestyle/environmental? Tumor-intrinsic differences?
- Does the signal replicate in non-TCGA cohorts (METABRIC, AURORA)?
- Whether prospective stratification of hypoxia-targeting trials by ancestry would reveal differential benefit
- Does ancestry-specific hypoxia explain known ancestry differences in BRCA outcomes after controlling for socioeconomics?
