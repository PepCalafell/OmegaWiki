---
title: "Trajectory-based DE recovers Alzheimer-linked genes with greater statistical power than case-control"
slug: trajectory-differential-expression-recovers-alzheimer-linked
status: supported
confidence: 0.8
tags: [Alzheimer, differential-expression, SNCA, APOE, microglia, power]
domain: neuroscience
source_papers:
  - reconstructing-developmental-disease-progression-sample-level
evidence:
  - source: reconstructing-developmental-disease-progression-sample-level
    type: supports
    strength: moderate
    detail: "SNCA showed non-significant upregulation in microglia under binary case-control but robust upregulation along the trajectory; same power gain for SNX27, LRRK2, PIK3CA, PLAT, and APOE."
conditions: "Trajectory NB-GLM DE on AD snRNA-seq."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Modeling gene expression as a function of donor position along the scSLIDE Alzheimer trajectory recovers known AD-associated genes (SNCA, APOE, LRRK2, SNX27, PIK3CA, PLAT) with substantially higher statistical power than binary case-control testing, which left several non-significant.

## Evidence summary

Figure 4e and Supplementary Figure 8a / Supplementary Table 4 of [[reconstructing-developmental-disease-progression-sample-level]]. SNCA (microglia-specific overexpression causally linked to neurodegeneration) was the demonstrative example.

## Conditions and scope

Trajectory-based NB-GLM DE; demonstrated for pre-selected AD-linked genes and transcriptome-wide.

## Counter-evidence

None reported; the gain is attributed to continuous modeling.

## Linked ideas

Mechanistic payoff of [[continuous-disease-progression-modeling]]; relates to [[rho-gtpase-pathway-genes-rise-microglia]].

## Open questions

Does the power gain generalize to genes of small effect across non-microglial cell types?
