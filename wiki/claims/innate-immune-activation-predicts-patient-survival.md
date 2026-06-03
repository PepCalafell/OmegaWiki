---
title: "Innate immune activation scores predict patient survival in a subset of TCGA cancer types"
slug: innate-immune-activation-predicts-patient-survival
status: weakly_supported
confidence: 0.6
tags: [survival, pan-cancer, TCGA, innate-immunity, correlational, prognosis]
domain: oncology / immunology
source_papers:
  - genomic-investigation-innate-sensing-pathways-tumor
evidence:
  - source: genomic-investigation-innate-sensing-pathways-tumor
    type: supports
    strength: moderate
    detail: "Partial Cox regression of ssGSEA scores vs survival per cancer type, controlling for age, gender, pathological stage, tumor purity, and immune-cell infiltrate; significant beta values (p<0.05) in a subset of cancers — hazardous in some, protective in others (Fig. 2B)."
conditions: "Direction of effect varies by cancer type; significant only in a subset; exploratory pan-cancer analysis."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Across 29 TCGA cancer types, innate-pathway activation scores are associated with overall survival in some cancers, with the prognostic direction (hazardous vs advantageous) differing by cancer type.

## Evidence summary

Partial Cox regressions controlling for major confounders yielded significant associations in a subset of cancers, demonstrating clinical relevance but heterogeneous influence of innate signaling.

## Conditions and scope

Subset of cancers only; correlational; no causal or mechanistic link to outcome established.

## Counter-evidence

Many cancer types showed no significant association; effect direction is inconsistent.

## Linked ideas

## Open questions

Why is innate activation protective in some tumors and hazardous in others?
