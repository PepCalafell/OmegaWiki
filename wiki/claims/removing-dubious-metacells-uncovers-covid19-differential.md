---
title: "Removing dubious metacells uncovers COVID-19-enriched differential gene co-expression and eliminates artifact correlations"
slug: removing-dubious-metacells-uncovers-covid19-differential
status: supported
confidence: 0.8
tags: [single-cell, metacell, mcRigor, co-expression, COVID-19, B-cells]
domain: single-cell-methods
source_papers:
  - mcrigor-statistical-method-enhance-rigor-metacell
evidence:
  - source: mcrigor-statistical-method-enhance-rigor-metacell
    type: supports
    strength: moderate
    detail: "On PBMC B cells (SuperCell γ=20), using trustworthy metacells only, the adaptive immune response module is enriched in COVID-19 (p=7.6e-19); using all metacells it appears not enriched (p=0.546) due to an artifactual healthy-condition co-expression absent at single-cell resolution. Antigen-processing MHC-II module p=3.7e-31; IFN-alpha response p=0.00328."
conditions: "Human PBMC scRNA-seq, 7 hospitalized COVID-19 patients vs 6 healthy controls; co-expression is cell-type- and condition-specific; consistent with CS-CORE."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

Excluding mcRigor-detected dubious metacells before correlation estimation removes artifact co-expression and reveals B-cell gene modules differentially co-expressed in COVID-19 (notably an adaptive immune response module, p = 7.6e-19), which is masked (p = 0.546) when dubious metacells are retained.

## Evidence summary

SuperCell (γ = 20) applied separately to 3028 COVID-19 and 1994 control B cells; mcRigor flagged 22/152 and 26/99 dubious metacells respectively. Trustworthy-only correlation revealed three enriched modules (MHC-II antigen processing p = 3.7e-31; adaptive immune response p = 7.6e-19; IFN-alpha response p = 0.00328), strengthened vs single-cell data. Including dubious metacells produced a spurious strong co-expression under the healthy condition — an artifact absent at single-cell resolution. Robust across SEACells, MetaCell, MetaCell2 partitions; consistent with CS-CORE.

## Conditions and scope

Including dubious metacells in correlation estimation provably biases co-expression (proven in Methods).

## Counter-evidence

None reported.

## Linked ideas

(none yet)

## Open questions

Generalization to other diseases and cell types beyond B cells.
