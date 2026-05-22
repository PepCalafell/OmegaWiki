---
title: "Across 20 TCGA pan-cancer cohorts, high LE score predicts worse OS and DSS, with limited exceptions"
slug: pan-cancer-tcga-le-worse-survival-20-cancers
status: supported
confidence: 0.8
tags: [TCGA, pan-cancer, leading-edge, survival, correlational]
domain: oncology/prognosis
source_papers:
  - spatial-transcriptomics-reveals-distinct-conserved-tumor
evidence:
  - source: spatial-transcriptomics-reveals-distinct-conserved-tumor
    type: supports
    strength: strong
    detail: "High LE score → worse OS in 19/20 TCGA cancers (exception: BRCA); worse DSS in 19/20 (exception: LUSC); worse PFI in 18/20 (exceptions: SKCM, LUSC)."
conditions: "Cox proportional hazards regression on TCGA bulk RNA-seq"
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement
The LE enrichment score is a pan-cancer prognostic marker, predicting worse OS / DSS / PFI in nearly all of 20 TCGA solid-tumour cohorts.

## Evidence summary
Fig. 5c–d; Supplementary Fig. 5e.

## Conditions and scope
TCGA bulk RNA-seq cohorts (20 common solid tumours), Cox PH analysis per cancer.

## Counter-evidence
BRCA (OS), LUSC (DSS, PFI) and SKCM (PFI) are exceptions to the LE-worse-prognosis pattern.

## Linked ideas

## Open questions
Whether the exceptions reflect true biology (different LE coupling) or methodological artefacts (sample-size, hormone-driven biology in BRCA).
