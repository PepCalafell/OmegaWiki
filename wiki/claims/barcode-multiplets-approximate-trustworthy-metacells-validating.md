---
title: "Barcode multiplets approximate trustworthy metacells and mcRigor identifies all of them as trustworthy"
slug: barcode-multiplets-approximate-trustworthy-metacells-validating
status: supported
confidence: 0.8
tags: [single-cell, metacell, mcRigor, scATAC-seq, technical-variation]
domain: single-cell-methods
source_papers:
  - mcrigor-statistical-method-enhance-rigor-metacell
evidence:
  - source: mcrigor-statistical-method-enhance-rigor-metacell
    type: supports
    strength: moderate
    detail: "From a 5000-PBMC scATAC-seq dataset, bap identified 16 barcode multiplets (heterogeneous-bead type, 3–6 observations each). mcRigor identified all 16 as trustworthy metacells, supporting the technical-variation assumption."
conditions: "Barcode multiplets caused by heterogeneous beads — multiple barcodes tagging mRNA from the same physical cell, i.e. same biological state with purely technical variation."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

Barcode multiplets (multiple barcodes assigned to one physical cell) represent the same biological state with only technical variation, so they serve as empirical trustworthy metacells; mcRigor correctly classified all 16 such multiplets as trustworthy.

## Evidence summary

Using Lareau et al.'s bap on a public 5000-PBMC scATAC-seq dataset, 16 heterogeneous-bead barcode multiplets (3–6 cell-like observations each) were identified. Their observations were dispersed (substantial technical variation), yet mcRigor flagged all 16 as trustworthy.

## Conditions and scope

Validates the existence and magnitude of technical variation underlying the metacell definition; barcode multiplets approximate trustworthy but not dubious metacells, hence the complementary simulation-based dubious-detection assessment.

## Counter-evidence

None reported.

## Linked ideas

(none yet)

## Open questions

Whether mcRigor could conversely serve as a benchmarking tool for doublet/multiplet removal methods (authors' suggestion).
