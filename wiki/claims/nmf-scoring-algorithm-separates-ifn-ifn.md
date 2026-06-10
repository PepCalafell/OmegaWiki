---
title: "An NMF scoring algorithm built on HIRISA separates IFN-I and IFN-II activity per cell type"
slug: "nmf-scoring-algorithm-separates-ifn-ifn"
status: supported
confidence: 0.85
tags:
  - interferon
  - NMF
  - methodology
  - deconvolution
domain: immunology
source_papers:
  - dissecting-type-ii-interferon-impacts-human
evidence:
  - source: dissecting-type-ii-interferon-impacts-human
    type: supports
    strength: strong
    detail: "FCs for 1,174 HIRISA-derived ISGs computed relative to controls; non-negative matrix factorization derives IFN-α and IFN-γ coefficients (scores) per cell type; IFN-γ set to zero in NK cells (no IFNGR2); transcriptomic IFN-I scores correlated with plasma IFN-α2A+β; weak negative IFN-α/IFN-γ correlation in monocytes (r=-0.38) supports independent deconvolution."
conditions: "Requires HIRISA ISG reference; per-cell-type scoring relative to cohort controls."
date_proposed: 2026-06-10
date_updated: 2026-06-10
---

## Statement

A non-negative matrix factorization (NMF) scoring algorithm built on ~1,174 HIRISA-derived ISGs separates IFN-I (IFN-α) and IFN-II (IFN-γ) activity per cell type from bulk or single-cell transcriptomic data, even when both pathways are co-active.

## Evidence summary

Supported by [[dissecting-type-ii-interferon-impacts-human]] (p.7-8). Built on [[nmf-non-negative-matrix-factorization]] and the [[ifn-ifn-ii-activity-deconvolution-scoring]] framework; validated against plasma IFN concentrations. Deployed as a web tool.

## Conditions and scope

Cell-type-resolved data; scores computed relative to matched controls; IFN-γ score zeroed in NK cells.

## Counter-evidence

IFN-γ scores showed only a nonsignificant positive trend with circulating IFN-γ (low systemic abundance).

## Linked ideas

## Open questions

How robust the deconvolution is on bulk data lacking cell-type resolution.
