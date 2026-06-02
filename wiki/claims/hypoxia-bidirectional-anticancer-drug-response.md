---
title: "Tumour hypoxia bidirectionally modulates anticancer drug response, conferring both resistance and sensitivity"
slug: hypoxia-bidirectional-anticancer-drug-response
status: supported
confidence: 0.8
tags:
  - hypoxia
  - drug-resistance
  - drug-sensitivity
  - precision-oncology
  - pancancer
domain: "oncology / pharmacology / hypoxia"
source_papers:
  - characterization-hypoxia-associated-molecular-features-aid
evidence:
  - source: characterization-hypoxia-associated-molecular-features-aid
    type: supports
    strength: strong
    detail: "Using imputed TCGA drug response: tumours under hypoxic conditions were resistant to many drugs (erlotinib in LIHC rs=0.42, FDR=1.5×10⁻⁴; lapatinib in KIRP rs=0.49, FDR=7.1×10⁻⁶) but sensitive to others (thapsigargin in PAAD rs=−0.66, FDR<1.0×10⁻⁵⁵; imatinib in HNSC rs=−0.31, FDR=4.3×10⁻⁴). Quote (p.440): 'some tumours may become sensitive to several drugs under hypoxic conditions... which suggests that patients with these cancers may not benefit from hypoxia-targeted therapy.'"
conditions: "Imputed drug response for 138 anticancer drugs in TCGA patients; |rs|>0.2, FDR<0.05. Validated against known cervical-cancer paclitaxel resistance and lung Akt-inhibitor-VIII sensitivity."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

Hypoxia does not uniformly cause drug resistance: depending on the cancer type and drug, the hypoxic microenvironment can confer either resistance or increased sensitivity. This bidirectionality reframes hypoxia-targeted therapy — patients whose tumours become *more* drug-sensitive under hypoxia may not benefit from anti-hypoxia treatment, partly explaining the disappointing results of past hypoxia-targeted trials.

## Evidence summary

- [[papers/characterization-hypoxia-associated-molecular-features-aid]] — imputed patient drug-response correlations, with literature-consistent validations (Fig. 7a).

## Conditions and scope

- Imputed (not measured) patient drug response; direction is drug- and cancer-type-specific.

## Counter-evidence

- Most prior clinical trials assumed hypoxia is uniformly drug-resistance-promoting.

## Linked ideas

(none yet)

## Open questions

- Can hypoxia status prospectively stratify patients into "benefit" vs "no-benefit" arms for hypoxia-targeted therapy?
