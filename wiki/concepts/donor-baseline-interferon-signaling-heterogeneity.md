---
title: "Donor baseline interferon-signaling heterogeneity"
aliases:
  - interferon donor group
  - baseline ISG donor heterogeneity
  - pre-existing interferon state
maturity: emerging
tags:
  - interferon
  - donor-variability
  - ISG
  - immune-heterogeneity
key_papers:
  - single-cell-cytokine-dictionary-human-peripheral
first_introduced: "2025"
date_updated: 2026-05-28
related_concepts:
  - cytokine-cell-type-specific-response-pleiotropy
  - cross-species-human-mouse-cytokine-response
---

## Definition

The observation that healthy human donors differ systematically in their baseline (unstimulated) immune transcriptional state, with a definable subgroup carrying elevated baseline expression of interferon-stimulated genes (ISGs; e.g. IFIT1-3) across cell types. In the Human Cytokine Dictionary, donors D1/D3/D4/D10 form a correlated "interferon group" (baseline log2FC r=0.61±0.10) whose PBS-treated CD4 T cells cluster with IFN-β-treated cells of other donors.

## Intuition

Two healthy people are not transcriptionally identical at rest: some sit in a primed, "interferon-high" baseline. This pre-existing state changes how they respond to certain cytokines (e.g. an anti-inflammatory IL-10-like response to IL-32-β only in pre-inflamed donors) and biases cross-individual comparisons. It is a confounder and a biological signal at once.

## Variants

- Interferon-high vs interferon-low donor groups
- Donor-specific pre-existing IL-32-β-like monocyte state (donor 2)
- Response substructure: ≥2 donor groups internally consistent but mutually divergent

## Comparison

Distinct from [[tonic-baseline-jak-stat-homeostasis]] (which concerns the cell-intrinsic homeostatic JAK-STAT setpoint generally); here the emphasis is inter-individual variation in that setpoint and its consequence for perturbation responses.

## When to use

When interpreting PBMC cytokine/stimulation experiments across multiple human donors, or when building consensus response references — to decide whether a single consensus log2FC is meaningful or whether donor substructure dominates.

## Known limitations

- Only 12 donors — limited power to attribute heterogeneity to genetics/age/sex (though 3/4 interferon-group donors were the oldest)
- Confounds direct cross-donor and cross-species comparisons

## Open problems

- Genetic / demographic determinants of the interferon-high state
- Whether the baseline state predicts disease susceptibility or therapy response
- How many distinct baseline immune "setpoints" exist at population scale

## Key papers

- [[papers/single-cell-cytokine-dictionary-human-peripheral]]

## My understanding

A practical caution and an interesting biology: consensus cytokine responses are robust overall, but a subset of cytokines (IL-32-β, IL-1α, IL-1Ra in CD4 T cells) have responses gated by the donor's pre-existing interferon state. Relevant to any human PBMC reference panel and to biomarker interpretation in autoimmune disease.
