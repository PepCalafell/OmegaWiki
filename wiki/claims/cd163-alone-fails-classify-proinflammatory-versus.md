---
title: "CD163 alone fails to classify proinflammatory vs immunosuppressive macrophages; multi-marker proteomic lists outperform"
slug: cd163-alone-fails-classify-proinflammatory-versus
status: supported
confidence: 0.8
tags:
  - macrophage
  - marker
  - classification
  - CD163
  - TAM
domain: immunology
source_papers:
  - delineation-signaling-routes-underlie-differences-macrophage
evidence:
  - source: delineation-signaling-routes-underlie-differences-macrophage
    type: supports
    strength: strong
    detail: "In scRNA-seq TME data, CD163 alone (across thresholds) did not cleanly separate proinflammatory vs immunosuppressive macrophages, whereas multi-marker proteomic and knowledge-based lists did."
conditions: "Public tumor scRNA-seq (HCC, brain metastases); multiple CD163 expression thresholds tested."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement
A single marker (CD163) does not reliably classify proinflammatory versus immunosuppressive macrophages in tumor scRNA-seq, whereas multi-marker proteomic and curated knowledge-based signatures clearly separate the two states.

## Evidence summary
- "CD163 alone as a marker was not able to classify proinflammatory and immunosuppressive macrophages, also when different gene expression thresholds were assessed, while the two knowledge-based lists clearly defined proinflammatory clinical macrophage subsets. This highlights a previous notion that effective macrophage classifications benefit from including multiple markers" (p.14).

## Conditions and scope
Concerns single-marker classification specifically; argues multi-marker (proteomic/literature) lists are preferable.

## Counter-evidence
Complements the separate finding that M1/M2 *gene* signatures can fail in the TME — here the failure is attributed to single-marker reliance, not the proinflammatory axis itself. See [[claims/m1-m2-signatures-fail-distinguish-tme-macrophages]].

## Linked ideas

## Open questions
Which minimal multi-marker panel best separates proinflammatory TAMs across tumor types?
