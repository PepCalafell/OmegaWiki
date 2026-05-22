---
title: "scPred classifier on TC/LE/transitory/other achieves 10-fold CV ROC of 0.991 (TC), 0.922 (LE), 0.943 (transitory), 0.958 (other)"
slug: scpred-tc-le-classifier-high-roc
status: supported
confidence: 0.9
tags: [methodological, scPred, ML, OSCC, classifier]
domain: methods/spatial-transcriptomics
source_papers:
  - spatial-transcriptomics-reveals-distinct-conserved-tumor
evidence:
  - source: spatial-transcriptomics-reveals-distinct-conserved-tumor
    type: supports
    strength: strong
    detail: "10-fold cross-validation on the OSCC-trained scPred classifier yields ROC 0.991 (TC), 0.922 (LE), 0.943 (transitory) and 0.958 (other). LE has the lowest ROC owing to lower sensitivity (0.694)."
conditions: "scPred radial SVM on PCs; OSCC training data; per-spot probability output"
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement
A probability-based scPred classifier trained on OSCC TC/LE/transitory/other ST spots achieves robust 10-fold cross-validated performance, with LE the hardest class (lower sensitivity).

## Evidence summary
Fig. 4c probability distributions; Supplementary Table 2 reports ROC and per-class sensitivity.

## Conditions and scope
HPV-negative OSCC training set; classifier trained for downstream pan-cancer transfer.

## Counter-evidence
LE class has comparatively lower sensitivity (0.694), suggesting LE detection rests on a noisier decision boundary.

## Linked ideas

## Open questions
Performance under domain shift (different ST platforms, e.g. CosMx, Stereo-seq).
