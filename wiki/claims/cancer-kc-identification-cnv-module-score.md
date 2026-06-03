---
title: "Cancer keratinocytes are stringently identified by combining CNV polyploidy with cancer module scores"
slug: cancer-kc-identification-cnv-module-score
status: supported
confidence: 0.8
tags: [cscc, cnv, malignant-cell-identification, keratinocyte]
domain: oncology
source_papers:
  - integrating-12-spatial-single-cell-technologies
evidence:
  - source: integrating-12-spatial-single-cell-technologies
    type: supports
    strength: strong
    detail: "A KC was called cancer if it showed abnormal polyploidy by consensus of two CNV inference methods AND high cancer module scores (genes up in tumour vs normal); 745 KC cancer cells identified, 82.6% classified as dysplastic KC. (p.5)"
conditions: "cSCC scRNA-seq; multi-evidence intersection rather than a single criterion."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Combining consensus CNV-based polyploidy detection with cancer module scores yields a stringently defined population of 745 KC cancer cells, of which 82.6% are independently classified as dysplastic KCs — three converging lines of evidence supporting malignant identity.

## Evidence summary

Intersection of two CNV methods plus module-score thresholds; concordance with dysplastic KC annotation provides orthogonal support. The same multi-evidence approach was applied to melanoma. (p.5)

## Conditions and scope

Single-cell cSCC data; relies on quality of CNV inference and tumour-vs-normal DE gene sets.

## Counter-evidence

CNV inference from expression is indirect; module scores depend on reference DE.

## Linked ideas

## Open questions

Sensitivity/specificity of the intersection vs ground-truth genetic clonality.
