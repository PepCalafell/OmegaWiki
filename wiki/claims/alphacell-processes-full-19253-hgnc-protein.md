---
title: "AlphaCell processes the full 19,253 HGNC protein-coding genes rather than ~2,000 highly variable genes"
slug: alphacell-processes-full-19253-hgnc-protein
status: supported
confidence: 0.9
tags: [AlphaCell, genome-wide, HVG, virtual-cell, single-cell, feature-representation]
domain: methods / single-cell
source_papers:
  - towards-building-world-model-simulate-perturbation
evidence:
  - source: towards-building-world-model-simulate-perturbation
    type: supports
    strength: strong
    detail: "Quote (p.5): 'Unlike prevailing methods that restrict inputs to ~2,000 HVGs, AlphaCell processes the full set of 19,253 HGNC protein-coding genes.' Bijective mapping to HGNC eliminates one-symbol-to-many-Ensembl ambiguity."
conditions: "Input filtered to definitive set of 19,253 unique protein-coding genes aligned to HGNC standard."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

AlphaCell defines a cellular state over the full 19,253 HGNC protein-coding transcriptome rather than the ~1,000–2,000 highly variable genes used by prior models, motivated by the argument that HVG truncation systematically excludes low-abundance but high-information regulatory drivers (master TFs, receptors).

## Evidence summary

Reported in [[papers/towards-building-world-model-simulate-perturbation]] (Chuai et al., bioRxiv 2026). See [[concepts/genome-wide-cell-representation-versus-highly]] and [[foundations/hgnc-gene-nomenclature-standard]]; contrast with [[foundations/hvg-selection-scrna]].

## Conditions and scope

UMI-based scRNA-seq standardized to log(1+CP10k); strict bijective gene→channel mapping.

## Counter-evidence

None within paper; self-reported design choice.

## Linked ideas

## Open questions

- Does genome-wide input help for sparse low-depth datasets where most of the 19k genes are zero?
