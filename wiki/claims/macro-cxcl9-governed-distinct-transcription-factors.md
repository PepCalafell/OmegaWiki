---
title: "Macro-CXCL9 is governed by distinct transcription factors (LYL1, NRF1, SMARCC2, CCNT2, TCF3)"
slug: macro-cxcl9-governed-distinct-transcription-factors
status: weakly_supported
confidence: 0.5
tags: [transcription-factor, SCENIC, macrophage, CXCL9, gene-regulatory-network]
domain: oncology / immunology
source_papers:
  - multiomics-analysis-cxcl9-macrophages-immunotherapy-response
evidence:
  - source: multiomics-analysis-cxcl9-macrophages-immunotherapy-response
    type: supports
    strength: moderate
    detail: "Quote (p.4): 'The specific transcription factors for Macro-CXCL9 include LYL1, NRF1, SMARCC2, CCNT2, and TCF3.' with 'LYL1 is a critical regulator of primitive macrophages' and 'NRF1 ... regulating mitochondrial proteostasis in inflammatory macrophages.'"
conditions: "pySCENIC regulon activity inference on bladder cancer scRNA-seq; TF activity is inferred, not perturbed."
date_proposed: 2026-06-05
date_updated: 2026-06-05
---

## Statement

SCENIC regulon analysis assigns Macro-CXCL9 a distinct transcription-factor activity profile — LYL1, NRF1, SMARCC2, CCNT2, and TCF3 — differing markedly from the other bladder cancer macrophage subpopulations, with LYL1 linked to primitive macrophage regulation and NRF1 to mitochondrial proteostasis in inflammatory macrophages.

## Evidence summary

Inferred regulon finding from [[papers/multiomics-analysis-cxcl9-macrophages-immunotherapy-response]] via [[foundations/scenic-tf-regulon-inference]]. Supports the trajectory-origin concept [[concepts/macro-cxcl9-progenitor-node-tumor-macrophage]].

## Conditions and scope

Computational TF-activity inference; no genetic perturbation or ChIP validation.

## Counter-evidence

Regulon activity does not establish causal control of CXCL9 expression.

## Linked ideas

## Open questions

- Which of these TFs causally drives the Macro-CXCL9 program versus marking its differentiation state?
