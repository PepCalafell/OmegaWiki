---
title: "The RashX web portal classifies external rash scRNA-seq within the TH2/TH17 framework"
slug: rashx-portal-classifies-external-rash-scrna
status: supported
confidence: 0.8
tags: [skin, rashx, web-portal, classification, resource, scrna-seq]
domain: immunology / resource
source_papers:
  - classification-human-chronic-inflammatory-skin-disease
evidence:
  - source: classification-human-chronic-inflammatory-skin-disease
    type: supports
    strength: moderate
    detail: "Quote (p.8): 'Example web portal outputs showed that these samples segregated closely to their parent class.' RashX (https://rashX.ucsf.edu) accepts 10x RDS matrices, finds Trm1-like cells, runs disease-specific DE vs HC, returns heatmaps + hyperdimensionality plot."
conditions: "Proof-of-principle interface; demonstrated on example AD and PV matrices."
date_proposed: 2026-06-10
date_updated: 2026-06-10
---

## Statement

The authors built RashX (https://rashX.ucsf.edu), a web interface that places an external rash's Trm1 scRNA-seq profile within the study's TH2/TH17 AD-PV stratification, and demonstrated that example AD and PV input matrices segregated correctly to their parent classes.

## Evidence summary

Reported in Results of [[papers/classification-human-chronic-inflammatory-skin-disease]] using [[foundations/scrna-seq-10x-chromium]]. Supports [[concepts/rashx-rash-classification-web-portal]].

## Conditions and scope

Proof-of-principle; requires 10x scRNA-seq input in RDS format and the study's reference.

## Counter-evidence

Demonstrated only on example inputs; no large-scale benchmark of portal accuracy.

## Linked ideas

## Open questions

- How robust is portal classification to dataset quality and platform variation?
