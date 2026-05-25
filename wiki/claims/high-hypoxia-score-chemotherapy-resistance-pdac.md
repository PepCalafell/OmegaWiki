---
title: "High hypoxia score predicts reduced sensitivity (elevated IC50) to gemcitabine, oxaliplatin, cisplatin, 5-FU, and paclitaxel in PDAC"
slug: high-hypoxia-score-chemotherapy-resistance-pdac
status: supported
confidence: 0.7
tags: [hypoxia,PDAC,chemotherapy,drug-sensitivity,gemcitabine,oxaliplatin,5FU,paclitaxel,oncoPredict,GDSC]
domain: oncology-hypoxia
source_papers:
  - development-hypoxia-responsive-macrophage-prognostic-model
evidence:
  - source: development-hypoxia-responsive-macrophage-prognostic-model
    type: supports
    strength: medium
    detail: "Quote (p.12–13, Results): 'most drugs exhibited significant differential responses between the high and low hypoxia groups, including key agents such as gemcitabine, oxaliplatin, cisplatin, 5-Fluorouracil and paclitaxel (Fig 6D). The elevated half-maximal inhibitory concentrations (IC50) of these drugs in the high hypoxia group suggested a diminished chemotherapy efficacy'. IC50 values predicted via oncoPredict from GDSC; differences tested by Wilcoxon."
conditions: "In-silico IC50 prediction (oncoPredict, GDSC training) on TCGA-PAAD bulk transcriptomes — not measured drug response in patients or PDOs. No prospective validation."
date_proposed: 2026-05-25
date_updated: 2026-05-25
---

## Statement

Patients in the high-hypoxia group (defined by the 13-gene hypoxia score) have higher predicted IC50 values for gemcitabine, oxaliplatin, cisplatin, 5-fluorouracil, and paclitaxel — the principal cytotoxic chemotherapies used in PDAC — compared to the low-hypoxia group. The IC50 values are predicted from bulk transcriptomes via oncoPredict using GDSC as training data.

## Evidence summary

Reported in [[papers/development-hypoxia-responsive-macrophage-prognostic-model]] (Ge et al., *PLoS One* 2025, Fig 6D).

## Conditions and scope

- IC50 values are *predicted in silico* from GDSC training, not measured in patient samples or PDOs.
- The directionality is consistent with the broader literature on hypoxia-driven chemoresistance (see [[concepts/hypoxia-emt-lineage-plasticity-metastasis]] and [[claims/hif1a-emt-multidrug-resistance-chemoresistance-cancer]]).
- No multivariable adjustment for tumour stage / grade; high-hypoxia samples may be enriched for advanced disease independent of biology.

## Counter-evidence

None within paper scope.

## Linked ideas

## Open questions

- Do PDAC PDOs from high-hypoxia patients show elevated measured IC50 to these agents?
- Does pretreatment hypoxia score predict response in prospective FOLFIRINOX or gemcitabine-nab-paclitaxel cohorts?
- Is hypoxia-driven chemoresistance reversible by HIF inhibitors (PX-478, belzutifan) or by hypoxia-activated prodrugs (evofosfamide)?
