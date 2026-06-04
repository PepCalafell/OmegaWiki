---
title: "CYBA discriminates intestinal from skin barrier IMIDs (high→UC/CD, low→PS/PSA)"
slug: cyba-discriminative-marker-separating-intestinal-skin
status: weakly_supported
confidence: 0.7
tags:
  - CYBA
  - biomarker
  - IBD
  - psoriasis
  - monocyte
domain: immunology
source_papers:
  - interpretable-inflammation-landscape-circulating-immune-cells
evidence:
  - source: interpretable-inflammation-landscape-circulating-immune-cells
    type: supports
    strength: moderate
    detail: "d-SHAP ranking highlighted CYBA (p22phox) in monocytes: high CYBA expression drove classification of intestinal IMIDs (UC, CD) whereas reduced CYBA was relevant to skin-related IMIDs (PS, PSA)."
conditions: "Monocyte population; barrier-tissue IMIDs."
date_proposed: 2026-06-04
date_updated: 2026-06-04
---

## Statement

CYBA, encoding the p22phox subunit of phagocyte NADPH oxidase, emerged as a top disease-discriminative gene in monocytes: high CYBA expression classifies intestinal inflammatory diseases (UC, CD) while reduced CYBA classifies skin-related diseases (PS, PSA), linking phagocyte ROS set-point to barrier-tissue disease localization.

## Evidence summary

d-SHAP scatter plots for CYBA in monocytes across UC/CD/PS/PSA (Fig. 3c; Extended Data Fig. 6b,c; p.639). The authors connect this to chronic granulomatous disease (CYBA loss → impaired phagocyte ROS, recurrent barrier infections) and to ROS roles in IBD.

## Conditions and scope

Monocytes; correlative classifier-importance result, not functional validation.

## Counter-evidence

Mechanistic hypothesis (impaired barrier vs ROS accumulation) is inferred, not tested.

## Linked ideas

- [[concepts/interpretable-ml-disease-discriminative-gene-discovery]]
- Foundations: [[foundations/cyba-cytochrome-b245-light-chain]] · [[foundations/inflammatory-bowel-disease]] · [[foundations/psoriasis-disease]]

## Open questions

- Does circulating monocyte CYBA predict IBD vs psoriatic disease prospectively?
