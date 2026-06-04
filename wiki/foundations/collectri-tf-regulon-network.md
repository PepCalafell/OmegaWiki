---
title: "CollecTRI — collection of TF regulons for activity inference"
slug: collectri-tf-regulon-network
domain: "methods / gene-regulatory-networks / TF-activity"
status: mainstream
aliases:
  - CollecTRI
  - CollecTRI regulons
first_introduced: "Müller-Dott et al. 2023 *Nucleic Acids Research* (Expanding the coverage of regulons from high-confidence prior knowledge)"
date_updated: 2026-06-04
source_url: "https://github.com/saezlab/CollecTRI"
---

## Definition

CollecTRI is a curated, high-confidence collection of transcription-factor regulons (TF → target-gene sets with mode of regulation) assembled from multiple prior-knowledge resources. It expands the coverage and accuracy of TF→target relationships relative to earlier resources (e.g. DoRothEA) and is the recommended regulon network for TF-activity inference in the decoupleR ecosystem.

## Intuition

A regulon is a "fan-out" from one TF to the genes it activates or represses. Given an expression matrix, the coordinated up/down movement of a TF's targets is a proxy for that TF's activity. CollecTRI provides the curated edges that make this inference reliable across cell types.

## Formal notation

Each regulon entry is a triple (TF, target, weight∈{+1,−1}); TF activity is estimated by an enrichment statistic (e.g. univariate linear model) over the target weights against an expression signature.

## Key variants

- Used with different activity-inference statistics (ULM, MLM, WSUM) via decoupleR.
- Robustness filtering: keep only regulons with ≥10 targets.

## Known limitations

- Prior-knowledge bias: well-studied TFs have richer, more accurate regulons.
- Context-independent edges; cell-type-specific rewiring is not encoded.

## Open problems

- Incorporating context-/cell-type-specific regulon activity.
- Resolving sign ambiguity for dual-function TFs.

## Relevance to active research

Provided the regulon network used to identify STAT1 and SP1 as the transcriptional regulators of the IFN-induced inflammation signature across circulating immune cells. Successor framing to [[dorothea-tf-regulon-analysis]]; paired with [[decoupler-activity-inference]].
