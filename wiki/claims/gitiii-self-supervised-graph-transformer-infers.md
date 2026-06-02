---
title: "GITIII infers single-cell-level CCIs from imaging spatial transcriptomics without ligand–receptor priors"
slug: gitiii-self-supervised-graph-transformer-infers
status: supported
confidence: 0.75
tags:
  - cell-cell-interaction
  - spatial-transcriptomics
  - graph-transformer
  - self-supervised
domain: "spatial transcriptomics / methods"
source_papers:
  - identifying-spatial-single-cell-level-interactions
evidence:
  - source: identifying-spatial-single-cell-level-interactions
    type: supports
    strength: moderate
    detail: "News & Views reports GITIII as a self-supervised graph-transformer method that resolves spatially resolved CCIs at single-cell resolution without relying on prior knowledge of ligand–receptor pairs (secondary description of Xiao et al. 2026)."
conditions: "Imaging-based spatial transcriptomics with single-cell segmentation; correlational CCI signal, not causal."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

GITIII, a self-supervised graph-transformer method, identifies spatially resolved cell–cell interactions (CCIs) at single-cell resolution from imaging-based spatial transcriptomics data, without relying on prior knowledge of ligand–receptor pairs.

## Evidence summary

Asserted in the *Nature Machine Intelligence* News & Views [[papers/identifying-spatial-single-cell-level-interactions]] (p.146), which describes the primary method paper (Xiao, Zhang, Zhao & Wang, *Nat. Mach. Intell.* **8**, 42–58, 2026): "Xiao et al. present GITIII, a self-supervised graph transformer-based method that overcomes these limitations to identify spatially resolved CCIs at single-cell resolution from imaging-based spatial transcriptomics data, without relying on prior knowledge of ligand–receptor pairs." Confidence is bounded by this being a secondary (commentary) source rather than the primary paper. See [[concepts/ligand-receptor-free-cell-cell-interaction]] and [[foundations/gitiii-graph-transformer-cci-method]].

## Conditions and scope

Applies to imaging-based spatial transcriptomics (CosMx, MERFISH, Xenium). The inferred interactions are correlational.

## Counter-evidence

None recorded. Primary-paper benchmarks not yet ingested.

## Linked ideas

None yet.

## Open questions

- How does GITIII's accuracy compare head-to-head against L–R-based methods on a common benchmark? (requires primary paper)
</content>
