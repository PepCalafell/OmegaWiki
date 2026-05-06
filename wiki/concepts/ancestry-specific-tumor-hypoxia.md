---
title: "Ancestry-specific tumor hypoxia"
aliases:
  - "ancestry-specific tumor hypoxia"
  - "hypoxia ancestry disparity"
  - "racial differences in tumor hypoxia"
  - "Caucasian vs Asian/African hypoxia"
  - "cancer health disparity hypoxia"
  - "ethnic-ancestry hypoxia"
  - "MAESTRO trial response disparity"
  - "evofosfamide ancestry response"
tags:
  - hypoxia
  - cancer
  - health-disparity
  - ancestry
  - BRCA
  - clinical-trial
  - precision-medicine
maturity: emerging
key_papers:
  - molecular-landmarks-tumor-hypoxia-across-cancer
first_introduced: "Bhandari et al. 2019 Nat Genet"
date_updated: 2026-05-06
related_concepts: []
---

## Definition

Ancestry-specific tumor hypoxia is the empirical observation that median tumor hypoxia score differs between subjects of different self-reported ancestral backgrounds within the same cancer type. The most robust evidence comes from BRCA in [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]], where median hypoxia scores were −7 (White, n=997 split), 11 (Asian), and 13 (Black/African American), Bonferroni P=4.08×10⁻¹³ (Kruskal-Wallis test). The signal in non-BRCA cancer types is statistically underpowered.

## Intuition

Cancer outcomes differ by ancestry, and one molecular driver may be differential tumor hypoxia. If hypoxia is more common in tumors arising in subjects of Asian or African ancestry, this could explain (i) worse baseline outcomes in those populations even after controlling for socioeconomic factors, and (ii) the higher response to evofosfamide (a hypoxia-activated prodrug) seen in Asian-descent subjects in the phase-3 MAESTRO trial. The signal is one of the few molecular precision-medicine findings that ties hypoxia to a *patient-level* demographic factor.

## Formal notation

- BRCA cohort: n=997 independent tumors with self-reported ancestry
- Median hypoxia score: White=−7, Asian=11, Black or African American=13
- Test: Kruskal-Wallis, Q=4.08×10⁻¹³ (Bonferroni-adjusted)
- 10× boxplot Tukey representation
- Sample size for ancestry analysis was twice that of any other cancer type — required to reach statistical power

## Variants

- BRCA: clearest signal (n large, ancestry distribution favorable)
- Other tumor types: signal direction often consistent (Caucasian ≤ Asian/African) but underpowered
- Subgroup analyses by BRCA molecular subtype (basal-like, HER2+, luminal): direction preserved within each subtype

## Comparison

| Cancer type | Hypoxia-ancestry power | Direction |
|---|---|---|
| BRCA | strong (Bonferroni P=4.08×10⁻¹³) | White < Asian/African |
| LUAD | underpowered | suggestive |
| PRAD | underpowered | inconclusive |
| Other 16 types | underpowered | inconclusive |

## When to use

- Stratifying clinical trials by ancestry when hypoxia is a candidate biomarker
- Hypothesis generation for cancer health disparities research
- Evaluating phase-3 trial subgroup outcomes for hypoxia-targeting agents
- NOT for individual-patient prediction without molecular hypoxia measurement

## Known limitations

- Self-reported ancestry is a coarse proxy for genetic ancestry
- TCGA ancestry distribution skews European; non-European arms underpowered for most tumor types
- Confounded by socioeconomic factors, healthcare access, age at diagnosis distribution
- Mechanistic basis (germline modifiers? environmental/lifestyle factors? tumor-intrinsic differences?) unknown

## Open problems

- Whether genetic ancestry (HLA, germline DDR variants) drives the hypoxia signal, or whether it is environmental/socioeconomic
- Validation in non-TCGA cohorts with prospective hypoxia measurement
- Does ancestry-specific hypoxia mediate the higher evofosfamide response in Asian-descent MAESTRO subjects (post-hoc finding)
- Replication in pediatric cancers and rare tumor types

## Key papers

- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — primary discovery: BRCA Caucasian < Asian/African hypoxia, Bonferroni P=4.08×10⁻¹³

## My understanding

This is one of the more clinically actionable findings in the Bhandari paper, but also one of the most easily over-interpreted. The BRCA signal is real and powered; its mechanistic basis is unknown. If validated prospectively, it would suggest that hypoxia-targeting drugs (evofosfamide, tirapazamine analogues) be developed and trialed with explicit ancestry stratification — a precedent for molecular-disparity-informed precision medicine.
