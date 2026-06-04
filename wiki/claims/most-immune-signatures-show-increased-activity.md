---
title: "Most immune-relevant signatures show increased activity across inflammatory diseases vs healthy"
slug: most-immune-signatures-show-increased-activity
status: supported
confidence: 0.8
tags:
  - inflammation
  - gene-signatures
  - cross-disease
domain: immunology
source_papers:
  - interpretable-inflammation-landscape-circulating-immune-cells
evidence:
  - source: interpretable-inflammation-landscape-circulating-immune-cells
    type: supports
    strength: moderate
    detail: "A general trend of increased activity in immune-relevant signatures vs healthy donors (>50% increased average signature scores) measured by ULM on scANVI-corrected expression with LMEM disease-vs-HC contrasts."
conditions: "119 Spectra cell-type-specific factors; corrected signature activity (ULM + LMEM, FDR<0.05)."
date_proposed: 2026-06-04
date_updated: 2026-06-04
---

## Statement

Across diseases and cell types, the majority of immune-relevant signatures showed increased activity relative to healthy donors (>50% with increased average signature scores), establishing a broad activation baseline of circulating immune cells in inflammation.

## Evidence summary

Computed via decoupleR ULM over 119 Spectra factors on scANVI-corrected pseudobulks, with a linear mixed-effect model contrasting disease vs healthy control (Fig. 2a; p.634).

## Conditions and scope

Signature-level, corrected activity scores; direction varies by specific signature and cell type.

## Counter-evidence

Some signatures (e.g. IFN type 1/2) are downregulated in many IMIDs — see [[claims/ifn-type-signatures-downregulated-imids-except]].

## Linked ideas

- [[concepts/inflammation-atlas-circulating-immune-cells]]

## Open questions

- Which increases are causal vs bystander responses?
